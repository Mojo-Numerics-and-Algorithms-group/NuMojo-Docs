# Adding Functions to NuMojo

This guide explains how to add a new function to NuMojo in a consistent, maintainable way.

## Goal

When you add a function, you should:

1. put it in the right module,
2. keep API behavior consistent with existing NuMojo patterns,
3. add tests and docs in the same PR,
4. avoid leaking internal execution/backend details into user-facing APIs.

---

## 1) Decide where the function belongs

Use this decision path:

- **General numerical routine** (NumPy-like): `numojo/routines/*`
  - math: `numojo/routines/math/*`
  - linalg: `numojo/routines/linalg/*`
  - logic/indexing/sorting/statistics/etc. in matching routine folders
- **Core type behavior** (array internals, indexing internals, memory): `numojo/core/*`
- **Domain-specific advanced routine** (SciPy-like): `numojo/science/*`

### Examples

- Add `sigmoid` (element-wise transform): `numojo/routines/math/misc.mojo` (or a dedicated file if it grows).
- Add `median_abs_deviation`: `numojo/routines/statistics/*`.
- Add low-level stride helper: `numojo/core/layout/*`.

---

## 2) Design the user-facing API first

Public API should stay simple and predictable.

### Recommended style

- Prefer:
  - `fn foo[dtype: DType](x: NDArray[dtype]) raises -> NDArray[dtype]`
- Avoid exposing backend internals in public signatures.

### Naming rules

- Follow existing NuMojo naming style in the module.
- Use clear, conventional names (`minimum`, not typo variants).
- Keep aliases minimal and intentional.

---

## 3) Implement with shared execution helpers

When adding element-wise or reduction style functions, reuse existing internal helpers whenever possible instead of rewriting loops in each function.

### Element-wise unary pattern

```mojo
import math
import numojo.routines.math._math_funcs as _mf
from numojo.core.ndarray import NDArray

fn sin[
    dtype: DType, backend: _mf.Backend = _mf.Vectorized
](array: NDArray[dtype]) raises -> NDArray[dtype]:
    return backend().math_func_1_array_in_one_array_out[dtype, math.sin](array)
```

### Element-wise binary pattern

```mojo
import numojo.routines.math._math_funcs as _mf
from numojo.core.ndarray import NDArray

fn add[
    dtype: DType, backend: _mf.Backend = _mf.Vectorized
](array1: NDArray[dtype], array2: NDArray[dtype]) raises -> NDArray[dtype]:
    return backend().math_func_2_array_in_one_array_out[
        dtype, SIMD.__add__
    ](array1, array2)
```

If the function needs special shape logic (broadcasting, axis handling), do validation first, then delegate to helpers where possible.

---

## 4) Validate inputs and raise clear errors

Prefer explicit checks up front:

- axis normalization (`-ndim <= axis < ndim`)
- shape compatibility
- dtype constraints

Use consistent error messages and categories where available. Check `NumojoError` for more information on how to raise Errors. 

### Axis validation example

```mojo
var normalized_axis = axis
if normalized_axis < 0:
    normalized_axis += a.ndim
if (normalized_axis < 0) or (normalized_axis >= a.ndim):
    raise Error(
        String("Error in `my_func`: Axis {} not in bound [-{}, {})")
        .format(axis, a.ndim, a.ndim)
    )
```

---

## 5) Add overloads only when necessary

NuMojo currently supports multiple overload patterns (`Shape`, `List`, variadic, etc.) in some modules.  
For new functions:

- start with the minimal set of overloads needed for usability,
- avoid adding many overloads if one canonical signature can serve.

---

## 6) Export the function correctly

After implementing the function, update exports consistently.

Typical places:

1. module-local `__init__.mojo` (e.g. `numojo/routines/math/__init__.mojo`)
2. `numojo/routines/__init__.mojo` (if currently re-exported there)
3. top-level `numojo/__init__.mojo` (if part of stable top-level API)

If you skip exports, users may not find the function via `import numojo as nm`.

---

## 7) Add tests in the same PR

Every new function should include tests.

### Where to add tests

- routine functions: `tests/routines/`
- core behavior: `tests/core/`

### Test style

- Use `def test_*` naming.
- Compare against NumPy where applicable using helpers in `tests/utils_for_test.mojo`.
- Add both:
  - correctness test,
  - error/edge-case test (invalid shape, invalid axis, etc.).

### Minimal test example

```mojo
from testing import TestSuite
from tests.utils_for_test import check
from python import Python
import numojo as nm
from numojo.prelude import *

def test_my_func_basic() raises:
    var np = Python.import_module("numpy")
    var a = nm.arange[f32](6).reshape(Shape(2, 3))
    var got = nm.my_func(a)
    var expected = np.my_func(np.arange(6, dtype=np.float32).reshape(2, 3))
    check(got, expected, "my_func basic mismatch")

def main():
    TestSuite.discover_tests[__functions_in_module()]().run()
```

---

## 8) Update docs in the same PR

At minimum, update:

- `docs/features.md` (if function is user-facing),
- relevant guide in `docs/user-guide/*` if this function is important to workflows.

If the function is key/public, add a small usage example to docs.

---

## 9) Check formatting and tests locally

Before opening PR:

1. format:
   - `pixi run format`
2. run tests:
   - `pixi run test`
---

## 10) PR checklist (copy into your PR)

- [ ] Function added in correct module
- [ ] Input validation + clear errors implemented
- [ ] Exports updated (`__init__.mojo` files)
- [ ] Tests added (correctness + edge/error case)
- [ ] Docs updated (`features.md` and/or user guide)
- [ ] `pixi run format` passes
- [ ] `pixi run test` passes

---

## Recommended pattern for first-time contributors

If this is your first contribution, choose one of:

- a pure element-wise unary function,
- a pure element-wise binary function,
- a simple reduction with axis support.

These are easiest to validate and review, and they help you learn NuMojo architecture quickly.

---

## Notes on future architecture

NuMojo is moving toward cleaner separation of:

- public API,
- shared execution helpers,
- backend dispatch internals.

When adding functions today, keep public signatures clean so future backend refactors won’t require breaking API changes.
