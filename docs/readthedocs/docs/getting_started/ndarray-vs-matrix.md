# NDArray vs Matrix in NuMojo

NuMojo provides two primary array types: `NDArray` and `Matrix`.  
Both are useful, but they serve slightly different purposes.

## Quick rule of thumb

- Use **`NDArray`** when your data can be **1D, 2D, 3D, or higher**.
- Use **`Matrix`** when your data is **always 2D** and your workflow is primarily linear algebra.

---

## What is `NDArray`?

`NDArray` is the general-purpose n-dimensional container in NuMojo.

Use it for:

- tensors and multi-axis scientific data
- flexible slicing/indexing across arbitrary dimensions
- routines that should work on any dimensionality

Typical examples:

- signal batches with shape `(batch, channels, time)`
- image stacks with shape `(n, h, w, c)`
- simulation grids with shape `(x, y, z)`

---

## What is `Matrix`?

`Matrix` is a dedicated 2D array type specialized for matrix workflows.

Use it for:

- classic linear algebra pipelines
- code where shape is always `(rows, cols)`
- APIs and methods designed around matrix semantics

Typical examples:

- solving `Ax = b`
- matrix factorizations
- 2D table-like numerical data

---

## API style differences

Both types support many similar operations, but usage style can differ:

- `NDArray` often appears in function-oriented routines:
  - `nm.sum(a, axis=...)`
  - `nm.reshape(a, Shape(...))`
- `Matrix` often supports matrix-specific methods:
  - `A.inv()`
  - matrix-oriented indexing patterns

NuMojo also provides top-level routines that work with both where applicable.

---

## Performance guidance

Choose the type that matches your domain model first, then optimize.

- If your data is inherently n-dimensional, forcing it into `Matrix` is usually a bad fit.
- If your data is strictly 2D and linear-algebra-heavy, `Matrix` is often clearer and may be more optimized for those operations.

---

## Interoperability mindset

A practical approach in real projects:

1. Keep core tensor data in `NDArray`.
2. Convert/reshape to 2D where a matrix algorithm is needed.
3. Convert back to `NDArray` layout as needed for downstream steps.

---

## Example: choosing by intent

```mojo
import numojo as nm
from numojo.prelude import *

fn main() raises:
    # NDArray: general n-dimensional use
    var tensor = nm.random.randn(Shape(4, 3, 2))
    print("tensor ndim =", tensor.ndim)

    # Matrix: dedicated 2D linear algebra use
    var A = Matrix.rand(shape=(4, 4))
    var B = Matrix.rand(shape=(4, 1))
    var x = nm.solve(A, B)
    print("solution shape =", x.shape)
```

---

## Common mistakes

- Using `Matrix` for 3D/4D data pipelines.
- Using `NDArray` for purely 2D linear algebra code without a reason.
- Mixing indexing styles inconsistently in one module.

---

## Recommendation for new contributors

When adding a new feature:

- If algorithm is shape-agnostic and naturally n-dimensional, implement for `NDArray` first.
- If algorithm is mathematically matrix-specific (decomposition, solver kernels), implement for `Matrix` first.
- If both are valid, factor shared internals and expose both cleanly.

This keeps NuMojo coherent for both users and maintainers.