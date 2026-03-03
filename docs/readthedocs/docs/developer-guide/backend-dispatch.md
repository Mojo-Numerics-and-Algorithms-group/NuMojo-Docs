# Backend Dispatch Guide

This guide explains how NuMojo should route math operations internally while keeping the public API simple and stable.

## Summary

NuMojo should expose clean user-facing functions like:

- `nm.sin(x)`
- `nm.add(x, y)`
- `nm.greater(x, y)`

Backend selection (CPU SIMD, CPU scalar fallback, future GPU kernels) should happen internally in one place, not in user-facing signatures.

---

## Goals

1. Keep public API minimal and ergonomic.
2. Centralize execution policy and backend routing.
3. Avoid duplicating loop logic across modules.
4. Make future GPU integration additive (no API breakage).

---

## Design Principles

### 1) Public API never exposes backend parameters

Do this:

- `fn sin[dtype: DType](x: NDArray[dtype]) -> NDArray[dtype]`

Do not do this in public API:

- `fn sin[dtype, backend](...)`

Backend choices are internal implementation details.

### 2) Use a shared execution engine

Implement generic executors once:

- unary elementwise apply
- binary elementwise apply
- compare apply
- reduction apply (later)

Operation wrappers should call these executors rather than re-implement loops.

### 3) Dispatch policy lives in one internal layer

A central engine chooses execution path based on:

- dtype support
- contiguity/layout
- array size thresholds
- target device (future)

This keeps behavior consistent across all ops.

---

## Recommended Layering

- **`numojo/api/*`**: user-facing functions (`sin`, `add`, etc.)
- **`numojo/ops/*`**: internal op wrappers and shared engines
- **`numojo/ops/backend/*`**: backend-specific implementations (CPU vectorized/scalar, future GPU)

Suggested flow:

1. `api.math.sin(x)`
2. calls `ops.elementwise.sin(x)`
3. calls `ExecutionEngine.apply_unary(math.sin, x)`
4. engine dispatches to backend implementation

---

## Minimal Pattern (Sin Example)

### Public API

```/dev/null/api_math_trig.mojo#L1-8
import math
from numojo.core.ndarray import NDArray
from numojo.ops.execution.engine import ExecutionEngine

fn sin[dtype: DType](x: NDArray[dtype]) raises -> NDArray[dtype]:
    return ExecutionEngine.apply_unary[dtype, math.sin](x)
```

### Execution Engine

```/dev/null/execution_engine.mojo#L1-22
from numojo.core.ndarray import NDArray
from numojo.ops.backend.cpu.vectorized import CpuVectorized
from numojo.ops.backend.cpu.scalar import CpuScalar

struct ExecutionEngine:
    @staticmethod
    fn apply_unary[
        dtype: DType,
        f: fn[type: DType, w: Int](SIMD[type, w]) -> SIMD[type, w],
    ](x: NDArray[dtype]) raises -> NDArray[dtype]:
        if x.is_c_contiguous() and x.size >= 128 and dtype.is_floating_point():
            return CpuVectorized.apply_unary[dtype, f](x)
        return CpuScalar.apply_unary[dtype, f](x)
```

### CPU Vectorized Backend

```/dev/null/cpu_vectorized.mojo#L1-18
from algorithm.functional import vectorize
from sys import simd_width_of
from numojo.core.ndarray import NDArray

struct CpuVectorized:
    @staticmethod
    fn apply_unary[
        dtype: DType,
        f: fn[type: DType, w: Int](SIMD[type, w]) -> SIMD[type, w],
    ](x: NDArray[dtype]) raises -> NDArray[dtype]:
        var out = NDArray[dtype](x.shape)
        comptime width = simd_width_of[dtype]()

        @parameter
        fn body[w: Int](i: Int) unified {mut out, read x}:
            out._buf.ptr.store(i, f[dtype, w](x._buf.ptr.load[width=w](i)))

        vectorize[width](x.size, body)
        return out^
```

---

## Why this is better than per-function backend wiring

- no backend noise in public signatures
- one place to tune thresholds and dispatch policy
- easier testing (engine behavior tested once)
- easier to add new ops (`sin/cos/exp/...` reuse same unary path)

---

## CPU Paths to Support Initially

1. **CPU vectorized path**
   - contiguous arrays
   - supported dtypes
   - medium/large arrays

2. **CPU scalar fallback**
   - unsupported dtype for SIMD path
   - non-contiguous or small arrays
   - correctness-first fallback

This gives robust behavior now and a stable architecture for future acceleration.

---

## Future GPU Integration

When GPU kernels become available:

1. Add backend modules:
   - `ops/backend/gpu/cuda.mojo`
   - `ops/backend/gpu/mps.mojo` (as needed)

2. Extend engine policy:

- if array is on GPU and op supported -> GPU kernel
- else -> CPU path (copy or explicit error depending on policy)

3. Public API stays unchanged.

---

## Dispatch Policy Recommendations

Keep policy deterministic and documented.

Suggested checks in order:

1. Validate dtype/op support.
2. Normalize layout assumptions (contiguous fast path vs fallback).
3. Evaluate size threshold for vectorization.
4. Choose backend implementation.
5. Fallback to scalar if fast path unavailable.

Use clear errors for unsupported op/dtype combinations.

---

## Testing Strategy for Dispatch

### What to test

1. **Correctness parity**
   - vectorized path result == scalar path result
   - compare with NumPy reference where applicable

2. **Path coverage**
   - contiguous arrays trigger vectorized path
   - strided/small arrays trigger fallback path

3. **Edge cases**
   - empty arrays
   - singleton dimensions
   - non-finite values (`nan`, `inf`)

4. **Performance smoke tests**
   - verify no major regressions for common sizes

### Suggested test organization

- operation correctness tests stay under routine/module tests
- dispatch behavior tests in a focused internal test file
- avoid testing private details too tightly; assert behavior, not implementation quirks

---

## Migration Plan (Incremental)

1. Introduce `ExecutionEngine.apply_unary` and `apply_binary`.
2. Migrate a small set of ops (`sin`, `cos`, `add`, `mul`) to validate pattern.
3. Remove backend parameters from those public APIs.
4. Expand migration by module (`math`, then `logic`, then `bitwise`).
5. Remove obsolete backend plumbing once all callers are migrated.

This avoids a risky all-at-once refactor.

---

## Common Pitfalls

- Reintroducing backend generics in public modules.
- Copy-pasting loop code into each op instead of reusing engine.
- Hiding unsupported dtype failures with silent behavior changes.
- Mixing dispatch policy across many files.

---

## Recommended Naming

- `ExecutionEngine` for centralized routing/apply methods.
- `CpuVectorized`, `CpuScalar` for backend implementations.
- `apply_unary`, `apply_binary`, `apply_compare` for shared executors.

Keep names explicit and consistent.

---

## Related Docs

- `docs/developer-guide/architecture.md`
- `docs/developer-guide/adding-functions.md`
- `docs/developer-guide/testing.md`
- `docs/developer-guide/style-guide.md`
