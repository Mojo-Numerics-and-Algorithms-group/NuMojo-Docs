# `numojo.routines.manipulation`

Array shape and layout manipulation operations.

Routines for reshaping, transposing, broadcasting, flipping, concatenating,
and other shape-changing operations on arrays.

Exports
-------
- `reshape`, `ravel`, `expand_dims`, `atleast_1d`, `atleast_2d`,
  `atleast_3d`: Shape changes.
- `transpose`, `swapaxes`, `moveaxis`, `flip`, `flipud`, `fliplr`, `roll`:
  Layout changes.
- `broadcast_to`: Broadcasting.
- `repeat`, `pad`: Repeating and padding.
- `split`, `array_split`: Splitting.
- `concatenate`, `hstack`, `vstack`, `row_stack`, `column_stack`: Joining.
- `delete`, `append`: Removing and adding elements.
- `copyto`: Copying array values.
- `ndim`, `shape`, `size`: Array properties.

## Functions


<div class="fn-card" markdown="1">

### `copyto`

```mojo
def copyto[dtype: DType](mut dst: NDArray[dtype], src: NDArray[dtype])
```

Copies the array from src to dst.

<div class="prose-label">Examples</div>
`copyto(destination, source)` copies every value into `destination`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The shared element type of both arrays.

<div class="prose-label">Args</div>

- `dst` (`NDArray[dtype]`) `[mut]`: The destination array.
- `src` (`NDArray[dtype]`) `[imm]`: The source array.

!!! failure "Raises"
    NumojoError: If the source and destination sizes differ.


</div>

<div class="fn-card" markdown="1">

### `ndim`

<div class="overload-divider">Overload 1</div>

```mojo
def ndim[dtype: DType](array: NDArray[dtype]) -> Int
```

Returns the number of dimensions of the NDArray.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `Int`

<div class="overload-divider">Overload 2</div>

```mojo
def ndim[cdtype: ComplexDType](array: ComplexNDArray[cdtype]) -> Int
```

Returns the number of dimensions of the NDArray.

<div class="prose-label">Parameters</div>

- `cdtype` (`ComplexDType`)

<div class="prose-label">Args</div>

- `array` (`ComplexNDArray[cdtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

### `shape`

<div class="overload-divider">Overload 1</div>

```mojo
def shape[dtype: DType](array: NDArray[dtype]) -> NDArrayShape
```

Returns the shape of the NDArray.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArrayShape`

<div class="overload-divider">Overload 2</div>

```mojo
def shape[cdtype: ComplexDType](array: ComplexNDArray[cdtype]) -> NDArrayShape
```

Returns the shape of the NDArray.

Returns: The shape of the NDArray.

<div class="prose-label">Parameters</div>

- `cdtype` (`ComplexDType`)

<div class="prose-label">Args</div>

- `array` (`ComplexNDArray[cdtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArrayShape`


</div>

<div class="fn-card" markdown="1">

### `size`

<div class="overload-divider">Overload 1</div>

```mojo
def size[dtype: DType](array: NDArray[dtype], axis: Int) -> Int
```

Returns the size of the NDArray.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `axis` (`Int`) `[imm]`: The axis to get the size of.

<div class="prose-label">Returns</div>

- `Int`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def size[cdtype: ComplexDType](array: ComplexNDArray[cdtype], axis: Int) -> Int
```

Returns the size of the NDArray.

<div class="prose-label">Parameters</div>

- `cdtype` (`ComplexDType`)

<div class="prose-label">Args</div>

- `array` (`ComplexNDArray[cdtype]`) `[imm]`: A NDArray.
- `axis` (`Int`) `[imm]`: The axis to get the size of.

<div class="prose-label">Returns</div>

- `Int`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `reshape`

```mojo
def reshape[dtype: DType](A: NDArray[dtype], shape: NDArrayShape, order: String = "C") -> NDArray[dtype]
```

Returns an array of the same data with a new shape.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `shape` (`NDArrayShape`) `[imm]`: New shape.
- `order` (`String`) `[imm]`: "C" or "F". Read in this order from the original array and
    write in this order into the new array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the number of elements do not match.


</div>

<div class="fn-card" markdown="1">

### `ravel`

```mojo
def ravel[dtype: DType](a: NDArray[dtype], order: String = "C") -> NDArray[dtype]
```

Returns the raveled version of the NDArray.

Return:
    A contiguous flattened array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `order` (`String`) `[imm]`: The order to flatten the array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `expand_dims`

```mojo
def expand_dims[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Inserts a new axis of size 1 at the given position.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.array[nm.i32]("[1, 2, 3]")
print(nm.expand_dims(a, axis=0).shape)  # [1, 3]
print(nm.expand_dims(a, axis=1).shape)  # [3, 1]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `axis` (`Int`) `[imm]`: Position in the resulting array's shape where the new axis
    is placed. Supports negative indices, counted from
    `a.ndim + 1` (the resulting array's rank).

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound.


</div>

<div class="fn-card" markdown="1">

### `atleast_1d`

```mojo
def atleast_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```

Views the input as an array with at least one dimension.

A 0-d array is reshaped to shape `(1,)`; arrays that already have
1 or more dimensions are returned unchanged.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.array[nm.i32]("[1, 2, 3]")
print(nm.atleast_1d(a).shape)  # [3]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `atleast_2d`

```mojo
def atleast_2d[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```

Views the input as an array with at least two dimensions.

A 0-d or 1-d array of size `n` is reshaped to shape `(1, n)`; arrays
that already have 2 or more dimensions are returned unchanged.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.array[nm.i32]("[1, 2, 3]")
print(nm.atleast_2d(a).shape)  # [1, 3]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `atleast_3d`

```mojo
def atleast_3d[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```

Views the input as an array with at least three dimensions.

Follows numpy's convention: a 1-d array of size `n` becomes shape
`(1, n, 1)`; a 2-d array of shape `(m, n)` becomes shape `(m, n, 1)`;
a 0-d array becomes shape `(1, 1, 1)`. Arrays that already have 3 or
more dimensions are returned unchanged.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.array[nm.i32]("[[1, 2], [3, 4]]")
print(nm.atleast_3d(a).shape)  # [2, 2, 1]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `transpose`

<div class="overload-divider">Overload 1</div>

```mojo
def transpose[dtype: DType](A: NDArray[dtype], axes: List[Int]) -> NDArray[dtype]
```

Transpose array of any number of dimensions according to arbitrary permutation of the axes.

If `axes` is not given, it is equal to flipping the axes.
```mojo
import numojo as nm
var A = nm.random.rand(2,3,4,5)
print(nm.transpose(A))  # A is a 4darray.
print(nm.transpose(A, axes=[3,2,1,0]))
```

Examples.
```mojo
import numojo as nm
var arr2d = nm.random.rand(2,3)
print(nm.transpose(arr2d, axes=[0, 1]))  # equal to transpose of matrix
var arr3d = nm.random.rand(2,3,4)
print(nm.transpose(arr3d, axes=[2, 1, 0]))  # transpose 0-th and 2-th dimensions
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`
- `axes` (`List[Int]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def transpose[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```

(overload) Transpose the array when `axes` is not given. If `axes` is not given, it is equal to flipping the axes. See docstring of `transpose`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `swapaxes`

```mojo
def swapaxes[dtype: DType](A: NDArray[dtype], axis1: Int, axis2: Int) -> NDArray[dtype]
```

Interchange two axes of an array.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.random.rand(2, 3, 4)
print(nm.swapaxes(a, 0, 2).shape)  # [4, 3, 2]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `axis1` (`Int`) `[imm]`: First axis. Supports negative indices.
- `axis2` (`Int`) `[imm]`: Second axis. Supports negative indices.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If either axis is out of bound.


</div>

<div class="fn-card" markdown="1">

### `moveaxis`

<div class="overload-divider">Overload 1</div>

```mojo
def moveaxis[dtype: DType](A: NDArray[dtype], source: List[Int], destination: List[Int]) -> NDArray[dtype]
```

Moves axes of an array to new positions. Other axes remain in their original order.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.random.rand(2, 3, 4, 5)
print(nm.moveaxis(a, [0], [-1]).shape)  # [3, 4, 5, 2]
print(nm.moveaxis(a, [0, 1], [-1, -2]).shape)  # [4, 5, 3, 2]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `source` (`List[Int]`) `[imm]`: Original positions of the axes to move. Supports negative
    indices.
- `destination` (`List[Int]`) `[imm]`: Destination positions for each of the original axes.
    Supports negative indices.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `source` and `destination` do not have the same
number of elements, or if an axis is out of bound / repeated.

<div class="overload-divider">Overload 2</div>

```mojo
def moveaxis[dtype: DType](A: NDArray[dtype], source: Int, destination: Int) -> NDArray[dtype]
```

(overload) Moves a single axis of an array to a new position.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.random.rand(2, 3, 4, 5)
print(nm.moveaxis(a, 0, -1).shape)  # [3, 4, 5, 2]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `source` (`Int`) `[imm]`: Original position of the axis to move. Supports negative
    indices.
- `destination` (`Int`) `[imm]`: Destination position for the axis. Supports negative
    indices.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound.


</div>

<div class="fn-card" markdown="1">

### `broadcast_to`

```mojo
def broadcast_to[dtype: DType](a: NDArray[dtype], shape: NDArrayShape) -> NDArray[dtype]
```

Returns a non-owning view of `a` broadcast to `shape`, following NumPy broadcasting rules (trailing-dimension alignment, size-1 dims stretch).

<div class="prose-label">Notes</div>
The returned array shares the underlying buffer with `a` (refcounted,
zero-copy): broadcast dimensions get stride 0, so no new memory is
allocated. Because stride-0 dimensions are never C-contiguous, any
operation that needs a flat contiguous buffer (e.g. SIMD elementwise
kernels) will materialize the view via `.contiguous()` on demand.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: The array to broadcast.
- `shape` (`NDArrayShape`) `[imm]`: The target shape.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `a.shape` cannot be broadcast to `shape`.


</div>

<div class="fn-card" markdown="1">

### `flip`

<div class="overload-divider">Overload 1</div>

```mojo
def flip[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Returns flipped array and keep the shape.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def flip[dtype: DType](array: NDArray[dtype], var axis: Int) -> NDArray[dtype]
```

Returns flipped array along the given axis.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `axis` (`Int`) `[var]`: Axis along which to flip.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `flipud`

```mojo
def flipud[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Reverses the order of elements along axis 0 (up/down).

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.array[nm.i32]("[[1, 2], [3, 4]]")
print(nm.flipud(a))  # [[3, 4], [1, 2]]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the array has zero dimensions.


</div>

<div class="fn-card" markdown="1">

### `fliplr`

```mojo
def fliplr[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Reverses the order of elements along axis 1 (left/right).

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.array[nm.i32]("[[1, 2], [3, 4]]")
print(nm.fliplr(a))  # [[2, 1], [4, 3]]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the array has fewer than 2 dimensions.


</div>

<div class="fn-card" markdown="1">

### `roll`

<div class="overload-divider">Overload 1</div>

```mojo
def roll[dtype: DType](A: NDArray[dtype], shift: Int, axis: Int) -> NDArray[dtype]
```

Rolls array elements along a given axis. Elements that roll beyond the last position are re-introduced at the first.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](0, 10, 1)
print(nm.roll(a, 2, axis=0))  # [8, 9, 0, 1, 2, 3, 4, 5, 6, 7]
print(nm.roll(a, -2, axis=0))  # [2, 3, 4, 5, 6, 7, 8, 9, 0, 1]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `shift` (`Int`) `[imm]`: The number of places by which elements are shifted. Can be
    negative, in which case elements are shifted towards the
    beginning.
- `axis` (`Int`) `[imm]`: Axis along which elements are shifted. Supports negative
    indices.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound.

<div class="overload-divider">Overload 2</div>

```mojo
def roll[dtype: DType](A: NDArray[dtype], shift: Int) -> NDArray[dtype]
```

(overload) Rolls array elements. The array is flattened before shifting, and then restored to its original shape.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](0, 6, 1)
var b = nm.reshape(a, nm.Shape(2, 3))
print(nm.roll(b, 1))  # [[5, 0, 1], [2, 3, 4]]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `shift` (`Int`) `[imm]`: The number of places by which elements are shifted.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def roll[dtype: DType](A: NDArray[dtype], shift: List[Int], axis: List[Int]) -> NDArray[dtype]
```

(overload) Rolls array elements along multiple axes. If the same axis is repeated, the shifts accumulate.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.reshape(nm.arange[nm.i32](0, 12, 1), nm.Shape(3, 4))
var shift: List[Int] = [1, -1]
var axis: List[Int] = [0, 1]
print(nm.roll(a, shift, axis))
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `shift` (`List[Int]`) `[imm]`: The number of places by which elements are shifted, one per
    entry of `axis`.
- `axis` (`List[Int]`) `[imm]`: Axes along which elements are shifted. Supports negative
    indices.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `shift` and `axis` do not have the same number of
elements, or if an axis is out of bound.


</div>

<div class="fn-card" markdown="1">

### `repeat`

<div class="overload-divider">Overload 1</div>

```mojo
def repeat[dtype: DType](A: NDArray[dtype], repeats: Int, axis: Int) -> NDArray[dtype]
```

Repeats each slice of an array along the given axis a fixed number of times.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.reshape(nm.arange[nm.i32](0, 6, 1), nm.Shape(2, 3))
print(nm.repeat(a, 2, axis=0).shape)  # [4, 3]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `repeats` (`Int`) `[imm]`: The number of repetitions for each slice. Must be
    non-negative.
- `axis` (`Int`) `[imm]`: The axis along which to repeat. Supports negative indices.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `repeats` is negative or `axis` is out of bound.

<div class="overload-divider">Overload 2</div>

```mojo
def repeat[dtype: DType](A: NDArray[dtype], repeats: List[Int], axis: Int) -> NDArray[dtype]
```

(overload) Repeats each slice of an array along the given axis a variable number of times, one count per slice.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](0, 3, 1)
var repeats: List[Int] = [1, 2, 3]
print(nm.repeat(a, repeats, axis=0))  # [0, 1, 1, 2, 2, 2]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `repeats` (`List[Int]`) `[imm]`: The number of repetitions for each slice along `axis`.
    Must have the same length as `A.shape[axis]`, and all values
    must be non-negative.
- `axis` (`Int`) `[imm]`: The axis along which to repeat. Supports negative indices.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the length of `repeats` does not match
`A.shape[axis]`, if any value of `repeats` is negative, or if
`axis` is out of bound.

<div class="overload-divider">Overload 3</div>

```mojo
def repeat[dtype: DType](A: NDArray[dtype], repeats: Int) -> NDArray[dtype]
```

(overload) Repeats each element of a flattened array a fixed number of times.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](0, 3, 1)
print(nm.repeat(a, 2))  # [0, 0, 1, 1, 2, 2]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `repeats` (`Int`) `[imm]`: The number of repetitions for each element. Must be
    non-negative.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `repeats` is negative.

<div class="overload-divider">Overload 4</div>

```mojo
def repeat[dtype: DType](A: NDArray[dtype], repeats: List[Int]) -> NDArray[dtype]
```

(overload) Repeats each element of a flattened array a variable number of times, one count per element.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](0, 3, 1)
var repeats: List[Int] = [1, 2, 3]
print(nm.repeat(a, repeats))  # [0, 1, 1, 2, 2, 2]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `repeats` (`List[Int]`) `[imm]`: The number of repetitions for each element of the
    flattened `A`. Must have the same length as `A.size`, and all
    values must be non-negative.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the length of `repeats` does not match `A.size`,
or if any value of `repeats` is negative.


</div>

<div class="fn-card" markdown="1">

### `pad`

<div class="overload-divider">Overload 1</div>

```mojo
def pad[dtype: DType](A: NDArray[dtype], pad_width: List[List[Int]], mode: String = "constant", constant_values: Scalar[dtype] = 0) -> NDArray[dtype]
```

Pads an array.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](0, 3, 1)
var width: List[Int] = [1, 2]
var pad_width = List[List[Int]]()
pad_width.append(width)
print(nm.pad(a, pad_width))  # [0, 0, 1, 2, 0, 0]
print(nm.pad(a, pad_width, mode="edge"))  # [0, 0, 1, 2, 2, 2]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `pad_width` (`List[List[Int]]`) `[imm]`: Number of values padded to the edges of each axis, as
    `[before, after]` pairs. A single `[before, after]` pair
    broadcasts to every axis; otherwise one pair per axis of `A`
    is required.
- `mode` (`String`) `[imm]`: Padding mode. One of `"constant"`, `"edge"`, `"reflect"`,
    `"symmetric"`, or `"wrap"`.
- `constant_values` (`Scalar[dtype]`) `[imm]`: The value to pad with when `mode` is
    `"constant"`. Ignored otherwise.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `pad_width` has an invalid length or contains
negative values, or if `mode` is not supported.

<div class="overload-divider">Overload 2</div>

```mojo
def pad[dtype: DType](A: NDArray[dtype], pad_width: Int, mode: String = "constant", constant_values: Scalar[dtype] = 0) -> NDArray[dtype]
```

(overload) Pads every axis of an array with the same number of elements on both sides. See docstring of `pad`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](0, 3, 1)
print(nm.pad(a, 2))  # [0, 0, 0, 1, 2, 0, 0]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `pad_width` (`Int`) `[imm]`: Number of values padded to both edges of every axis.
    Must be non-negative.
- `mode` (`String`) `[imm]`: Padding mode. One of `"constant"`, `"edge"`, `"reflect"`,
    `"symmetric"`, or `"wrap"`.
- `constant_values` (`Scalar[dtype]`) `[imm]`: The value to pad with when `mode` is
    `"constant"`. Ignored otherwise.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `pad_width` is negative, or if `mode` is not
supported.


</div>

<div class="fn-card" markdown="1">

### `split`

<div class="overload-divider">Overload 1</div>

```mojo
def split[dtype: DType](A: NDArray[dtype], sections: Int, axis: Int = Int(0)) -> List[NDArray[dtype]]
```

Splits an array into `sections` equal arrays along `axis`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](0, 6, 1)
var parts = nm.split(a, 3)
print(parts[0])  # [0, 1]
print(parts[1])  # [2, 3]
print(parts[2])  # [4, 5]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `sections` (`Int`) `[imm]`: The number of equal sections to split the array into.
    Must divide `A.shape[axis]` evenly.
- `axis` (`Int`) `[imm]`: The axis along which to split. Supports negative indices.
    Defaults to 0.

<div class="prose-label">Returns</div>

- `List[NDArray[dtype]]`

!!! failure "Raises"
    NumojoError: If `sections` is not positive, if `axis` is out of
bound, or if `A.shape[axis]` is not evenly divisible by
`sections`.

<div class="overload-divider">Overload 2</div>

```mojo
def split[dtype: DType](A: NDArray[dtype], indices: List[Int], axis: Int = Int(0)) -> List[NDArray[dtype]]
```

(overload) Splits an array along `axis` at the given boundary indices.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](0, 6, 1)
var indices: List[Int] = [2, 4]
var parts = nm.split(a, indices)
print(parts[0])  # [0, 1]
print(parts[1])  # [2, 3]
print(parts[2])  # [4, 5]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `indices` (`List[Int]`) `[imm]`: The boundary indices at which to split. Need not be
    sorted; supports negative indices, and out-of-range values are
    clamped, matching Python slice semantics.
- `axis` (`Int`) `[imm]`: The axis along which to split. Supports negative indices.
    Defaults to 0.

<div class="prose-label">Returns</div>

- `List[NDArray[dtype]]`

!!! failure "Raises"
    NumojoError: If `axis` is out of bound.


</div>

<div class="fn-card" markdown="1">

### `array_split`

<div class="overload-divider">Overload 1</div>

```mojo
def array_split[dtype: DType](A: NDArray[dtype], sections: Int, axis: Int = Int(0)) -> List[NDArray[dtype]]
```

Splits an array into `sections` arrays along `axis`, as equally as possible. Unlike `split`, `A.shape[axis]` need not be evenly divisible by `sections`: the first `A.shape[axis] % sections` sub-arrays get one extra element.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](0, 7, 1)
var parts = nm.array_split(a, 3)
print(parts[0])  # [0, 1, 2]
print(parts[1])  # [3, 4]
print(parts[2])  # [5, 6]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `sections` (`Int`) `[imm]`: The number of sections to split the array into. Must be
    positive.
- `axis` (`Int`) `[imm]`: The axis along which to split. Supports negative indices.
    Defaults to 0.

<div class="prose-label">Returns</div>

- `List[NDArray[dtype]]`

!!! failure "Raises"
    NumojoError: If `sections` is not positive, or if `axis` is out of
bound.

<div class="overload-divider">Overload 2</div>

```mojo
def array_split[dtype: DType](A: NDArray[dtype], indices: List[Int], axis: Int = Int(0)) -> List[NDArray[dtype]]
```

(overload) Same as `split` with explicit boundary indices. See docstring of `split`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`
- `indices` (`List[Int]`) `[imm]`
- `axis` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `List[NDArray[dtype]]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `concatenate`

```mojo
def concatenate[dtype: DType](*arrays: NDArray[dtype], *, axis: Int = Int(0)) -> NDArray[dtype]
```

Join a sequence of arrays along an existing axis.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f64](0, 6, 1)
var a2d = nm.reshape(a, nm.Shape(2, 3))
var b = nm.arange[nm.f64](6, 12, 1)
var b2d = nm.reshape(b, nm.Shape(2, 3))
var c = nm.concatenate(a2d, b2d, axis=0)  # Shape (4, 3)
var d = nm.concatenate(a2d, b2d, axis=1)  # Shape (2, 6)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the arrays.

<div class="prose-label">Args</div>

- `*arrays` (`NDArray[dtype]`) `[imm]`: The arrays to concatenate. All arrays must have the same
    shape except in the dimension corresponding to `axis`.
- `axis` (`Int`) `[imm]`: The axis along which the arrays will be joined. Default is 0.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the list of arrays is empty.
NumojoError: If the arrays do not have the same number of dimensions.
NumojoError: If the array shapes are incompatible along non-concatenation axes.


</div>

<div class="fn-card" markdown="1">

### `column_stack`

```mojo
def column_stack[dtype: DType](*arrays: NDArray[dtype]) -> NDArray[dtype]
```

Stack 1-D arrays as columns into a 2-D array, or concatenate 2-D+ arrays along the second axis (like `numpy.column_stack`).

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f64](0, 3, 1)   # Shape (3,)
var b = nm.arange[nm.f64](3, 6, 1)   # Shape (3,)
var c = nm.column_stack(a, b)         # Shape (3, 2)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the arrays.

<div class="prose-label">Args</div>

- `*arrays` (`NDArray[dtype]`) `[imm]`: The arrays to stack. 1-D arrays are treated as column
    vectors. All arrays must have the same number of rows
    (first dimension).

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the list of arrays is empty.


</div>

<div class="fn-card" markdown="1">

### `row_stack`

```mojo
def row_stack[dtype: DType](*arrays: NDArray[dtype]) -> NDArray[dtype]
```

Stack arrays vertically (row-wise), equivalent to `numpy.row_stack` / `numpy.vstack`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f64](0, 3, 1)  # Shape (3,)
var b = nm.arange[nm.f64](3, 6, 1)  # Shape (3,)
var c = nm.row_stack(a, b)           # Shape (2, 3)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the arrays.

<div class="prose-label">Args</div>

- `*arrays` (`NDArray[dtype]`) `[imm]`: The arrays to stack. 1-D arrays of shape `(N,)` are
    reshaped to `(1, N)` before concatenation.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the list of arrays is empty.


</div>

<div class="fn-card" markdown="1">

### `hstack`

```mojo
def hstack[dtype: DType](*arrays: NDArray[dtype]) -> NDArray[dtype]
```

Stack arrays in sequence horizontally (column-wise), equivalent to `numpy.hstack`.

For 1-D arrays, this concatenates along axis 0.
For 2-D+ arrays, this concatenates along axis 1.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f64](0, 3, 1)  # Shape (3,)
var b = nm.arange[nm.f64](3, 6, 1)  # Shape (3,)
var c = nm.hstack(a, b)              # Shape (6,)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the arrays.

<div class="prose-label">Args</div>

- `*arrays` (`NDArray[dtype]`) `[imm]`: The arrays to stack.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the list of arrays is empty.


</div>

<div class="fn-card" markdown="1">

### `vstack`

```mojo
def vstack[dtype: DType](*arrays: NDArray[dtype]) -> NDArray[dtype]
```

Stack arrays in sequence vertically (row-wise), equivalent to `numpy.vstack`.

For 1-D arrays of shape `(N,)`, they are reshaped to `(1, N)` first.
Then concatenated along axis 0.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f64](0, 3, 1)  # Shape (3,)
var b = nm.arange[nm.f64](3, 6, 1)  # Shape (3,)
var c = nm.vstack(a, b)              # Shape (2, 3)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the arrays.

<div class="prose-label">Args</div>

- `*arrays` (`NDArray[dtype]`) `[imm]`: The arrays to stack.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the list of arrays is empty.


</div>

<div class="fn-card" markdown="1">

### `delete`

<div class="overload-divider">Overload 1</div>

```mojo
def delete[dtype: DType](A: NDArray[dtype], obj: List[Int], axis: Optional[Int] = None) -> NDArray[dtype]
```

Returns a copy of an array with the sub-arrays at `obj` removed along `axis`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](0, 5, 1)
print(nm.delete(a, [1, 2]))  # [0, 3, 4]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `obj` (`List[Int]`) `[imm]`: Indices of the slices to remove along `axis`. Supports
    negative indices; repeated indices are only removed once.
- `axis` (`Optional[Int]`) `[imm]`: The axis along which to remove slices. Supports negative
    indices. If not given, `A` is flattened before removing
    elements.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `axis` is out of bound, or if any index in `obj`
is out of bound for the corresponding axis.

<div class="overload-divider">Overload 2</div>

```mojo
def delete[dtype: DType](A: NDArray[dtype], obj: Int, axis: Optional[Int] = None) -> NDArray[dtype]
```

(overload) Removes a single slice at index `obj` along `axis`. See docstring of `delete`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`
- `obj` (`Int`) `[imm]`
- `axis` (`Optional[Int]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `append`

```mojo
def append[dtype: DType](A: NDArray[dtype], values: NDArray[dtype], axis: Optional[Int] = None) -> NDArray[dtype]
```

Appends `values` to the end of `A`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](0, 3, 1)
var b = nm.arange[nm.i32](3, 6, 1)
print(nm.append(a, b))  # [0, 1, 2, 3, 4, 5]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `values` (`NDArray[dtype]`) `[imm]`: The values to append. If `axis` is given, `values` must
    have the same number of dimensions as `A`, and the same shape
    except along `axis`.
- `axis` (`Optional[Int]`) `[imm]`: The axis along which to append. Supports negative indices.
    If not given, both `A` and `values` are flattened before
    appending.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `axis` is out of bound, or if the shapes of `A`
and `values` are incompatible.


</div>
