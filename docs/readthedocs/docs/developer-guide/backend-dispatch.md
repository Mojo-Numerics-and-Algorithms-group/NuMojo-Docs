# Backend Dispatch Guide (Future)

This guide explains how NuMojo should route math operations internally while keeping the public API simple and stable.

## Summary

NuMojo should expose clean user-facing functions like:

- `nm.sin(x)`
- `nm.add(x, y)`
- `nm.greater(x, y)`

Backend selection (CPU SIMD, future GPU kernels) should happen internally in one place, not in user-facing signatures.

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

- **`numojo/routines/operations/*`**: internal op wrappers and shared engines
- **`numojo/routines/operations/backend/*`**: backend-specific implementations (CPU vectorized, future GPU)

Suggested flow:

1. `math.sin(x)`
2. calls `HostExecutor.apply_unary(math.sin, x)`

---

## Minimal Pattern (Sin Example)

### Public API

```mojo
import math
from numojo.core.ndarray import NDArray
from numojo.ops.execution.engine import ExecutionEngine

fn sin[dtype: DType](x: NDArray[dtype]) raises -> NDArray[dtype]:
    return HostExecutor.apply_unary[dtype, math.sin](x)
```

### CPU Vectorized Backend

```mojo
from algorithm.functional import vectorize
from sys import simd_width_of
from numojo.core.ndarray import NDArray

struct HostExecutor:
    @staticmethod
    fn apply_unary[
        dtype: DType,
        f: fn[type: DType, w: Int](SIMD[type, w]) -> SIMD[type, w],
    ](x: NDArray[dtype]) raises -> NDArray[dtype]:
        
        if x.is_c_contiguous() and x.size >= 128 and dtype.is_floating_point():
            return HostExecutor.apply_unary[dtype, f](x)
            
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
   - `operations/gpu/cuda.mojo`
   - `operations/gpu/mps.mojo` (as needed)

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
3. Choose backend implementation.

Use clear errors for unsupported op/dtype combinations.

---

## Testing Strategy for Dispatch

### What to test

1. **Correctness parity**
   - vectorized path result == scalar path result
   - compare with NumPy reference where applicable

2. **Path coverage**
   - contiguous arrays trigger vectorized path
   - strided/small arrays trigger fallback path / convert them to contiguous arrays and trigger vectorized path. 

3. **Edge cases**
   - empty arrays
   - singleton dimensions
   - non-finite values (`nan`, `inf`)

4. **Performance smoke tests**
   - verify no major regressions for common sizes

---

## Migration Plan (Incremental)

1. Introduce `ExecutionEngine.apply_unary` and `apply_binary`.
2. Migrate a small set of ops (`sin`, `cos`, `add`, `mul`) to validate pattern.
3. Remove backend parameters from those public APIs.
4. Expand migration by module (`math`, then `logic`, then `bitwise`).
5. Remove obsolete backend plumbing once all callers are migrated.

This avoids a risky all-at-once refactor.

---

## Recommended Naming

- `ExecutionEngine` for centralized routing/apply methods.
- `HostExecutor`, for backend implementations.
- `apply_unary`, `apply_binary`, `apply_compare` for shared executors.

Keep names explicit and consistent.

---

## Related Docs

- `docs/developer-guide/architecture.md`
- `docs/developer-guide/adding-functions.md`
- `docs/developer-guide/testing.md`
- `docs/developer-guide/style-guide.md`
