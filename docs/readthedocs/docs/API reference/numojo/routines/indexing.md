# `numojo.routines.indexing`

Advanced indexing operations for arrays.

Functions for generating index arrays, fancy indexing, selecting elements,
and inserting data into arrays.

Exports
-------
- `where`: Conditional element selection.
- `compress`: Extract elements based on condition.
- `take`, `take_along_axis`: Advanced indexing.
- `nonzero`, `flatnonzero`: Find non-zero elements.
- `fancy_index`: Apply fancy indexing.
- `unravel_index`, `ravel_multi_index`: Index conversion.

## Functions


<div class="fn-card" markdown="1">

### `where`

<div class="overload-divider">Overload 1</div>

```mojo
def where[dtype: DType](mut x: NDArray[dtype], scalar: Scalar[dtype], mask: NDArray[DType.bool])
```

Replaces elements in `x` with `scalar` where `mask` is True.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `x` (`NDArray[dtype]`) `[mut]`: A NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: A SIMD value.
- `mask` (`NDArray[DType.bool]`) `[imm]`: A NDArray.

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def where[dtype: DType](mut x: NDArray[dtype], y: NDArray[dtype], mask: NDArray[DType.bool])
```

Replaces elements in `x` with elements from `y` where `mask` is True.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `x` (`NDArray[dtype]`) `[mut]`: NDArray[dtype].
- `y` (`NDArray[dtype]`) `[imm]`: NDArray[dtype].
- `mask` (`NDArray[DType.bool]`) `[imm]`: NDArray[DType.bool].

!!! failure "Raises"
    NumojoError: If the shapes of `x` and `y` do not match.

<div class="overload-divider">Overload 3</div>

```mojo
def where[dtype: DType, //](condition: NDArray[dtype]) -> List[NDArray[DType.int]]
```

Returns indices where `condition` is non-zero.

Returns one 1-D integer index array per dimension of `condition`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `condition` (`NDArray[dtype]`) `[imm]`: Selector array.

<div class="prose-label">Returns</div>

- `List[NDArray[DType.int]]`

!!! failure "Raises"

<div class="overload-divider">Overload 4</div>

```mojo
def where[dtype: DType](condition: NDArray[DType.bool], x: NDArray[dtype], y: NDArray[dtype]) -> NDArray[dtype]
```

Returns elements chosen from `x` or `y` depending on `condition`.

This is the functional, non-mutating form. ``condition``, ``x``, and ``y``
are broadcast against each other. Elements where ``condition`` is True come
from ``x``; elements where it is False come from ``y``.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.array[nm.f32]("[1.0, 2.0, 3.0, 4.0]")
var b = nm.array[nm.f32]("[10.0, 20.0, 30.0, 40.0]")
var mask = nm.array[nm.boolean]("[True, False, True, False]")
print(nm.where(mask, a, b))
# [1.0  20.0  3.0  40.0]
```
.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType of `x` and `y`.

<div class="prose-label">Args</div>

- `condition` (`NDArray[DType.bool]`) `[imm]`: Boolean selector array.
- `x` (`NDArray[dtype]`) `[imm]`: Values used where ``condition`` is True.
- `y` (`NDArray[dtype]`) `[imm]`: Values used where ``condition`` is False.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If ``condition``, ``x``, and ``y`` are not broadcast-compatible.

<div class="overload-divider">Overload 5</div>

```mojo
def where[dtype: DType](condition: NDArray[DType.bool], x: NDArray[dtype], y: Scalar[dtype]) -> NDArray[dtype]
```

Returns elements from `x` or scalar `y` depending on `condition`.

Overload of ``where`` where the false-branch is a scalar broadcast.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.array[nm.f32]("[1.0, 2.0, 3.0, 4.0]")
var mask = nm.array[nm.boolean]("[True, False, True, False]")
print(nm.where(mask, a, Scalar[nm.f32](0.0)))
# [1.0  0.0  3.0  0.0]
```
.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType of `x` and `y`.

<div class="prose-label">Args</div>

- `condition` (`NDArray[DType.bool]`) `[imm]`: Boolean selector array.
- `x` (`NDArray[dtype]`) `[imm]`: Values used where ``condition`` is True.
- `y` (`Scalar[dtype]`) `[imm]`: Scalar used where ``condition`` is False.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If ``condition`` and `x` are not broadcast-compatible.

<div class="overload-divider">Overload 6</div>

```mojo
def where[dtype: DType](condition: NDArray[DType.bool], x: Scalar[dtype], y: NDArray[dtype]) -> NDArray[dtype]
```

Returns scalar `x` or elements of `y` depending on `condition`.

Overload of ``where`` where the true-branch is a scalar broadcast.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var b = nm.array[nm.f32]("[10.0, 20.0, 30.0, 40.0]")
var mask = nm.array[nm.boolean]("[True, False, True, False]")
print(nm.where(mask, Scalar[nm.f32](0.0), b))
# [0.0  20.0  0.0  40.0]
```
.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType of `x` and `y`.

<div class="prose-label">Args</div>

- `condition` (`NDArray[DType.bool]`) `[imm]`: Boolean selector array.
- `x` (`Scalar[dtype]`) `[imm]`: Scalar used where ``condition`` is True.
- `y` (`NDArray[dtype]`) `[imm]`: Values used where ``condition`` is False.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If ``condition`` and `y` are not broadcast-compatible.


</div>

<div class="fn-card" markdown="1">

### `fancy_index`

<div class="overload-divider">Overload 1</div>

```mojo
def fancy_index[dtype: DType, //](a: NDArray[dtype], index_arrays: List[NDArray[DType.int]]) -> NDArray[dtype]
```

Element-wise multi-axis fancy (advanced) indexing.

Selects elements from `a` by supplying one integer-array index per axis
as a ``List``.  All index arrays are broadcast against each other; the
output shape equals that broadcast shape.  This allows the ``a[[row_arr, col_arr, ...]]``
syntax (the outer ``[]`` is the list literal).

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](12).reshape(nm.Shape(3, 4))
var rows = nm.array[nm.int]("[0, 1]")
var cols = nm.array[nm.int]("[2, 3]")
var idx = List[nm.NDArray[DType.int]]()
idx.append(rows^)
idx.append(cols^)
print(nm.fancy_index(a, idx))
# [2  7]
# or via __getitem__:
print(a[idx])
# [2  7]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the source array.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: Source N-D array.
- `index_arrays` (`List[NDArray[DType.int]]`) `[imm]`: List of integer NDArrays — exactly `a.ndim` entries,
    one per axis.  Each array is broadcast to the common shape.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the number of index arrays does not equal `a.ndim`.
NumojoError: If the index arrays are not mutually broadcast-compatible.
NumojoError: If any index value is out of bounds for its axis.

<div class="overload-divider">Overload 2</div>

```mojo
def fancy_index[dtype: DType, //](a: NDArray[dtype], *index_arrays: NDArray[DType.int]) -> NDArray[dtype]
```

Element-wise multi-axis fancy (advanced) indexing (variadic overload).

Convenience overload that accepts index arrays as variadic positional
arguments instead of a ``List``.  Delegates to the ``List`` overload.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](12).reshape(nm.Shape(3, 4))
var rows = nm.array[nm.int]("[0, 1]")
var cols = nm.array[nm.int]("[2, 3]")
print(nm.fancy_index(a, rows, cols))
# [2  7]
```
.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the source array.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: Source N-D array.
- `*index_arrays` (`NDArray[DType.int]`) `[imm]`: Exactly `a.ndim` integer index arrays, one per axis.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the number of index arrays does not equal `a.ndim`.
NumojoError: If the index arrays are not mutually broadcast-compatible.
NumojoError: If any index value is out of bounds for its axis.


</div>

<div class="fn-card" markdown="1">

### `compress`

<div class="overload-divider">Overload 1</div>

```mojo
def compress[dtype: DType](condition: NDArray[DType.bool], a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Return selected slices of an array along given axis. If no axis is provided, the array is flattened before use.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `condition` (`NDArray[DType.bool]`) `[imm]`: 1-D array of booleans that selects which entries to return.
    If length of condition is less than the size of the array along the
    given axis, then output is filled to the length of the condition
    with False.
- `a` (`NDArray[dtype]`) `[imm]`: The array.
- `axis` (`Int`) `[imm]`: The axis along which to take slices.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound for the given array.
NumojoError: If the condition is not 1-D array.
NumojoError: If the condition length is out of bound for the given axis.

<div class="overload-divider">Overload 2</div>

```mojo
def compress[dtype: DType](condition: NDArray[DType.bool], a: NDArray[dtype]) -> NDArray[dtype]
```

Return selected slices of an array along given axis. If no axis is provided, the array is flattened before use. This is a function ***OVERLOAD***.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `condition` (`NDArray[DType.bool]`) `[imm]`: 1-D array of booleans that selects which entries to return.
    If length of condition is less than the size of the array along the
    given axis, then output is filled to the length of the condition
    with False.
- `a` (`NDArray[dtype]`) `[imm]`: The array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the condition is not 1-D array.
NumojoError: If the condition length is out of bound for the given axis.


</div>

<div class="fn-card" markdown="1">

### `take_along_axis`

```mojo
def take_along_axis[dtype: DType, //](arr: NDArray[dtype], indices: NDArray[DType.int], axis: Int = Int(0)) -> NDArray[dtype]
```

Takes values from the input array along the given axis based on indices.

<div class="prose-label">Examples</div>

```console
> var a = nm.arange[i8](12).reshape(Shape(3, 4))
> print(a)
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
> ind = nm.array[intp]("[[0, 1, 2, 0], [1, 0, 2, 1]]")
> print(ind)
[[0 1 2 0]
 [1 0 2 1]]
> print(nm.indexing.take_along_axis(a, ind, axis=0))
[[ 0  5 10  3]
 [ 4  1 10  7]]
```
.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType of the input array.

<div class="prose-label">Args</div>

- `arr` (`NDArray[dtype]`) `[imm]`: The source array.
- `indices` (`NDArray[DType.int]`) `[imm]`: The indices array.
- `axis` (`Int`) `[imm]`: The axis along which to take values. Default is 0.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bounds for the given array.
NumojoError: If the ndim of arr and indices are not the same.
NumojoError: If the shape of indices does not match the shape of the
input array except along the given axis.


</div>

<div class="fn-card" markdown="1">

### `take`

<div class="overload-divider">Overload 1</div>

```mojo
def take[dtype: DType, //](a: NDArray[dtype], indices: NDArray[DType.int], axis: Int) -> NDArray[dtype]
```

Takes elements from an array along an axis.

Output shape is `a.shape[:axis] + indices.shape + a.shape[axis+1:]`.
Negative indices into `a` along the axis are normalised. Negative `axis`
values are also normalised.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](12).reshape(nm.Shape(3, 4))

print(nm.indexing.take(a, nm.array[nm.int]("[2, 0, 1]"), axis=0))
# shape (3, 4): rows 2, 0, 1
#
print(nm.indexing.take(a, nm.array[nm.int]("[1, 3]"), axis=1))
# shape (3, 2): cols 1, 3
```
.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the source array.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: Source array.
- `indices` (`NDArray[DType.int]`) `[imm]`: Indices of values to take along the axis.
- `axis` (`Int`) `[imm]`: Axis along which to select. Negative values count from the end.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `axis` is out of bounds.
NumojoError: If any index is out of bounds for the given axis.

<div class="overload-divider">Overload 2</div>

```mojo
def take[dtype: DType, //](a: NDArray[dtype], indices: NDArray[DType.int]) -> NDArray[dtype]
```

Takes elements from a flattened array by linear indices.

Equivalent to `take(a.flatten(), indices, axis=0)`. The output shape
matches `indices.shape`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](12).reshape(nm.Shape(3, 4))
print(nm.indexing.take(a, nm.array[nm.int]("[0, 5, 11]")))
# [0, 5, 11]
```
.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the source array.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: Source array (flattened before indexing).
- `indices` (`NDArray[DType.int]`) `[imm]`: Linear indices into the flattened source. May be any shape.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If any index is out of bounds for the flattened array.


</div>

<div class="fn-card" markdown="1">

### `put`

<div class="overload-divider">Overload 1</div>

```mojo
def put[dtype: DType, //](mut a: NDArray[dtype], indices: NDArray[DType.int], values: NDArray[dtype])
```

Replaces values at flat (linear) index positions of `a` in-place.

Equivalent to `a.flatten()[indices] = values`, but writes directly into
`a` (any array order). If `values` has fewer elements than `indices`, it
is repeated (broadcast) cyclically over `indices`. `values` must not be empty
unless `indices` is also empty.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](6)
nm.indexing.put(a, nm.array[nm.int]("[0, 2]"), nm.array[nm.i32]("[10, 20]"))
print(a)
# [10, 1, 20, 3, 4, 5]
```
.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the source array.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[mut]`: Destination array to be modified in-place.
- `indices` (`NDArray[DType.int]`) `[imm]`: Linear (flat) indices into `a`. May be any shape. Negative
    indices are normalised (counted from the end).
- `values` (`NDArray[dtype]`) `[imm]`: Values to write. Broadcast cyclically if shorter than
    `indices`.

!!! failure "Raises"
    NumojoError: If any index is out of bounds for the flattened array.
NumojoError: If `values` is empty while `indices` is not.

<div class="overload-divider">Overload 2</div>

```mojo
def put[dtype: DType, //](mut a: NDArray[dtype], indices: NDArray[DType.int], value: Scalar[dtype])
```

Replaces values at flat (linear) index positions of `a` in-place with a single broadcast scalar.

This is a function ***OVERLOAD*** of `put` for the scalar-`value` case.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](6)
nm.indexing.put(a, nm.array[nm.int]("[0, 2]"), Scalar[nm.i32](99))
print(a)
# [99, 1, 99, 3, 4, 5]
```
.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the source array.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[mut]`: Destination array to be modified in-place.
- `indices` (`NDArray[DType.int]`) `[imm]`: Linear (flat) indices into `a`. May be any shape. Negative
    indices are normalised (counted from the end).
- `value` (`Scalar[dtype]`) `[imm]`: Scalar value written to every selected position.

!!! failure "Raises"
    NumojoError: If any index is out of bounds for the flattened array.


</div>

<div class="fn-card" markdown="1">

### `unravel_index`

<div class="overload-divider">Overload 1</div>

```mojo
def unravel_index(index: Int, shape: NDArrayShape, order: String = "C") -> List[Int]
```

Converts a flat index into coordinates for `shape`.

<div class="prose-label">Args</div>

- `index` (`Int`) `[imm]`: Flat linear index.
- `shape` (`NDArrayShape`) `[imm]`: Target shape.
- `order` (`String`) `[imm]`: `"C"` for row-major order or `"F"` for column-major order.

<div class="prose-label">Returns</div>

- `List[Int]`

!!! failure "Raises"
    NumojoError: If `index` is out of bounds for the flattened array.
NumojoError: If `order` is not `"C"` or `"F"`.

<div class="overload-divider">Overload 2</div>

```mojo
def unravel_index(indices: NDArray[DType.int], shape: NDArrayShape, order: String = "C") -> List[NDArray[DType.int]]
```

Converts flat indices into coordinate arrays for `shape`.

<div class="prose-label">Notes</div>
Each output coordinate array has the same shape as `indices`.

<div class="prose-label">Args</div>

- `indices` (`NDArray[DType.int]`) `[imm]`: Flat linear indices.
- `shape` (`NDArrayShape`) `[imm]`: Target shape.
- `order` (`String`) `[imm]`: `"C"` for row-major order or `"F"` for column-major order.

<div class="prose-label">Returns</div>

- `List[NDArray[DType.int]]`

!!! failure "Raises"
    NumojoError: If any index is out of bounds for the flattened array.
NumojoError: If `order` is not `"C"` or `"F"`.

<div class="overload-divider">Overload 3</div>

```mojo
def unravel_index(index: Int, shape: List[Int], order: String = "C") -> List[Int]
```

Overload of `unravel_index` accepting a shape list.

<div class="prose-label">Args</div>

- `index` (`Int`) `[imm]`
- `shape` (`List[Int]`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `List[Int]`

!!! failure "Raises"

<div class="overload-divider">Overload 4</div>

```mojo
def unravel_index(indices: NDArray[DType.int], shape: List[Int], order: String = "C") -> List[NDArray[DType.int]]
```

Overload of `unravel_index` accepting a shape list.

<div class="prose-label">Args</div>

- `indices` (`NDArray[DType.int]`) `[imm]`
- `shape` (`List[Int]`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `List[NDArray[DType.int]]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `ravel_multi_index`

<div class="overload-divider">Overload 1</div>

```mojo
def ravel_multi_index(multi_index: List[NDArray[DType.int]], shape: NDArrayShape, order: String = "C") -> NDArray[DType.int]
```

Converts coordinate arrays into flat indices for `shape`.

Coordinate arrays are broadcast against each other. The result shape is the
broadcast shape of those coordinate arrays.

<div class="prose-label">Args</div>

- `multi_index` (`List[NDArray[DType.int]]`) `[imm]`: List of integer coordinate arrays, one per dimension.
- `shape` (`NDArrayShape`) `[imm]`: Target shape.
- `order` (`String`) `[imm]`: `"C"` for row-major order or `"F"` for column-major order.

<div class="prose-label">Returns</div>

- `NDArray[DType.int]`

!!! failure "Raises"
    NumojoError: If the number of coordinate arrays does not equal `shape.ndim`.
NumojoError: If coordinate arrays are not broadcast-compatible.
NumojoError: If any coordinate is out of bounds for its dimension.
NumojoError: If `order` is not `"C"` or `"F"`.

<div class="overload-divider">Overload 2</div>

```mojo
def ravel_multi_index(multi_index: List[NDArray[DType.int]], shape: List[Int], order: String = "C") -> NDArray[DType.int]
```

Overload of `ravel_multi_index` accepting a shape list.

<div class="prose-label">Args</div>

- `multi_index` (`List[NDArray[DType.int]]`) `[imm]`
- `shape` (`List[Int]`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[DType.int]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `flatnonzero`

```mojo
def flatnonzero[dtype: DType, //](a: NDArray[dtype]) -> NDArray[DType.int]
```

Returns flat indices of non-zero elements.

<div class="prose-label">Notes</div>
Indices are reported in C-order over the flattened array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: Input array.

<div class="prose-label">Returns</div>

- `NDArray[DType.int]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `nonzero`

```mojo
def nonzero[dtype: DType, //](a: NDArray[dtype]) -> List[NDArray[DType.int]]
```

Returns the indices of elements that are non-zero.

Returns a list of 1-D index arrays, one per dimension of `a`. Each array
contains the coordinates of non-zero elements along that dimension.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.array[nm.i32]("[3, 0, 5, 0, 2]")
var idx = nm.nonzero(a)
print(idx[0])  # [0, 2, 4]

var b = nm.array[nm.i32]("[[1, 0], [0, 4]]")
var idx2 = nm.nonzero(b)
print(idx2[0])  # [0, 1]  (row indices)
print(idx2[1])  # [0, 1]  (col indices)
```
.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the source array.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: Input array.

<div class="prose-label">Returns</div>

- `List[NDArray[DType.int]]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `searchsorted`

<div class="overload-divider">Overload 1</div>

```mojo
def searchsorted[dtype: DType, //](a: NDArray[dtype], v: NDArray[dtype], side: String = "left") -> NDArray[DType.int]
```

Finds indices where elements of `v` should be inserted into sorted 1-D array `a` to keep it sorted.

Uses binary search. `a` must be a 1-D array, assumed (not verified)
to be sorted in ascending order.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.array[nm.i32]("[1, 3, 5, 7]")
print(nm.indexing.searchsorted(a, nm.array[nm.i32]("[2, 6]")))
# [1, 3]
```
.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the source array.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: 1-D sorted source array.
- `v` (`NDArray[dtype]`) `[imm]`: Array of values to find insertion indices for.
- `side` (`String`) `[imm]`: `"left"` (default) returns the leftmost valid insertion index;
    `"right"` returns the rightmost.

<div class="prose-label">Returns</div>

- `NDArray[DType.int]`

!!! failure "Raises"
    NumojoError: If `a` is not 1-D.
NumojoError: If `side` is not `"left"` or `"right"`.

<div class="overload-divider">Overload 2</div>

```mojo
def searchsorted[dtype: DType, //](a: NDArray[dtype], v: Scalar[dtype], side: String = "left") -> Int
```

Finds the index where scalar `v` should be inserted into sorted 1-D array `a` to keep it sorted.

This is a function ***OVERLOAD*** of `searchsorted` for a scalar `v`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.array[nm.i32]("[1, 3, 5, 7]")
print(nm.indexing.searchsorted(a, Scalar[nm.i32](4)))
# 2
```
.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the source array.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: 1-D sorted source array.
- `v` (`Scalar[dtype]`) `[imm]`: Scalar value to find the insertion index for.
- `side` (`String`) `[imm]`: `"left"` (default) returns the leftmost valid insertion index;
    `"right"` returns the rightmost.

<div class="prose-label">Returns</div>

- `Int`

!!! failure "Raises"
    NumojoError: If `a` is not 1-D.
NumojoError: If `side` is not `"left"` or `"right"`.


</div>
