# Indexing and Slicing in NuMojo

This guide explains how to access and modify array data using NuMojo indexing APIs.

## Overview

NuMojo supports common indexing patterns similar to NumPy:

- scalar indexing
- slicing with `start:stop:step`
- multi-axis indexing
- negative indices
- boolean masking
- indexed selection and filtering helpers

Most examples below use `NDArray`, but many patterns also apply to `Matrix`.

---

## Imports used in examples

```/dev/null/indexing_imports.mojo#L1-3
import numojo as nm
from numojo.prelude import *
```

---

## 1) Scalar indexing

Use `Item(...)` for explicit coordinate-based indexing on `NDArray`.

```/dev/null/scalar_indexing.mojo#L1-11
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[i32](12).reshape(Shape(3, 4))
    print(a)

    var x = a[Item(1, 2)]
    print("a[1,2] =", x)  # coordinate (row=1, col=2)
```

You can also use method-style access in places where available:

```/dev/null/item_method.mojo#L1-8
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[f32](9).reshape(Shape(3, 3))
    print(a.item(2, 1))
```

---

## 2) Basic slicing

Slicing follows `start:stop:step` semantics.

```/dev/null/basic_slicing.mojo#L1-13
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[i32](20).reshape(Shape(4, 5))
    print("a:")
    print(a)

    print("a[1:3, :]:")
    print(a[1:3, :])

    print("a[:, 0:5:2]:")
    print(a[:, 0:5:2])
```

### Notes

- `start` is inclusive.
- `stop` is exclusive.
- `step` defaults to `1`.
- Omitted bounds imply full axis range.

---

## 3) Negative indexing

Negative indices count from the end.

```/dev/null/negative_indexing.mojo#L1-12
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[i32](12).reshape(Shape(3, 4))

    print("last row:")
    print(a[-1, :])

    print("last column:")
    print(a[:, -1])
```

---

## 4) Step slicing and reversal

Use step to subsample or reverse.

```/dev/null/step_slicing.mojo#L1-12
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[i32](16).reshape(Shape(4, 4))

    print("every other row:")
    print(a[::2, :])

    print("reverse rows:")
    print(a[::-1, :])
```

---

## 5) Multi-dimensional slicing

You can slice each axis independently.

```/dev/null/multi_axis_slicing.mojo#L1-11
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var t = nm.arange[i32](2 * 3 * 4).reshape(Shape(2, 3, 4))
    print("t shape:", t.shape)

    var view = t[:, 1:, 0:4:2]
    print("sliced tensor:")
    print(view)
```

---

## 6) Assignment via indexing

Assign to scalar positions or slices.

```/dev/null/index_assignment.mojo#L1-15
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.zeros[f32](Shape(3, 4))
    a[Item(1, 2)] = 7.5
    print("after scalar set:")
    print(a)

    var b = nm.ones[f32](Shape(2, 2))
    a[0:2, 0:2] = b
    print("after slice set:")
    print(a)
```

When assigning slices, shape compatibility matters. If shapes do not align, NuMojo raises an error.

---

## 7) Boolean masking

Create a boolean mask and select matching values.

```/dev/null/boolean_masking.mojo#L1-14
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[i32](10)
    var mask = a > 4

    print("a:")
    print(a)
    print("mask:")
    print(mask)

    print("a[mask]:")
    print(a[mask])
```

Mask shape should be compatible with the indexed array (or selected axis behavior, depending on routine).

---

## 8) `where` for conditional replacement

Use `where` to modify values based on a mask.

```/dev/null/where_example.mojo#L1-14
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[f32](8)
    var mask = a > 3

    # Replace entries where mask is true with scalar value
    nm.where(a, SIMD[f32, 1](99.0), mask)

    print(a)
```

---

## 9) `compress` for axis-based filtering

Use `compress` to select slices along a specific axis.

```/dev/null/compress_example.mojo#L1-13
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[i32](12).reshape(Shape(3, 4))
    var cond = nm.array[boolean]("[true, false, true]")

    var out = nm.compress(cond, a, axis=0)
    print("input:")
    print(a)
    print("compressed along axis=0:")
    print(out)
```

---

## 10) `take_along_axis` for index-driven selection

`take_along_axis` is useful when you already have index arrays.

```/dev/null/take_along_axis_example.mojo#L1-15
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[i32](12).reshape(Shape(3, 4))
    var idx = nm.array[int]("[[0,1,2,0],[1,0,2,1]]")

    var out = nm.take_along_axis(a, idx, axis=0)

    print("a:")
    print(a)
    print("idx:")
    print(idx)
    print("take_along_axis(a, idx, axis=0):")
    print(out)
```

---

## Matrix indexing notes

For `Matrix`, common indexing style is direct 2D indexing:

```/dev/null/matrix_indexing.mojo#L1-10
from numojo import Matrix

fn main() raises:
    var A = Matrix.rand(shape=(4, 4))
    print(A[1, 2])     # scalar
    print(A[1:3, :])   # sliced block
```

Use `Matrix` when your data is strictly 2D and matrix-centric.
Use `NDArray` for general n-dimensional workflows.

---

## Common mistakes and fixes

### 1) Using wrong index rank
If array is 3D, supplying only one scalar index often returns a slice/subarray, not a scalar.  
Use full coordinates with `Item(...)` when you need one element.

### 2) Slice assignment shape mismatch
When assigning a slice, ensure value shape matches the target slice shape.

### 3) Axis out of bounds in helper routines
For `compress`, `take_along_axis`, and reduction-like APIs, validate axis is in `[-ndim, ndim)`.

### 4) Mask shape mismatch
Boolean mask dimensions should match intended indexing behavior.

---

## Practical recommendations

- Prefer explicit `Item(...)` for scalar reads/writes in `NDArray`.
- Normalize negative axes in your own utility wrappers when building higher-level APIs.
- Keep indexing style consistent within a module for readability.
- Add tests for indexing edge cases (negative indices, empty slices, shape mismatch).

---

## Next steps

- `docs/user-guide/ndarray-creation-manipulation.md`
- `docs/user-guide/linalg.md`
- `docs/user-guide/io.md`
- `docs/developer-guide/testing.md`
