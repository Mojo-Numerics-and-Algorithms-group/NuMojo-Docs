# `numojo.routines.manipulation`

Array shape and layout manipulation operations.

Routines for reshaping, transposing, broadcasting, flipping, concatenating,
and other shape-changing operations on arrays.

Exports
-------
- `reshape`, `ravel`: Shape changes.
- `transpose`, `flip`: Layout changes.
- `broadcast_to`: Broadcasting.
- `concatenate`, `hstack`, `vstack`, `row_stack`, `column_stack`: Joining.
- `ndim`, `shape`, `size`: Array properties.

## Functions


<div class="fn-card" markdown="1">

### `copy_to`

```mojo
def copy_to[dtype: DType](mut dst: NDArray[dtype], src: NDArray[dtype])
```

Copies the array from src to dst.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `dst` (`NDArray[dtype]`) `[mut]`: The destination array.
- `src` (`NDArray[dtype]`) `[imm]`: The source array.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `ndim`

#### Overload 1

```mojo
def ndim[dtype: DType](array: NDArray[dtype]) -> Int
```

Returns the number of dimensions of the NDArray.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `Int`

#### Overload 2

```mojo
def ndim[cdtype: ComplexDType](array: ComplexNDArray[cdtype]) -> Int
```

Returns the number of dimensions of the NDArray.

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `array` (`ComplexNDArray[cdtype]`) `[imm]`: A NDArray.

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

### `shape`

#### Overload 1

```mojo
def shape[dtype: DType](array: NDArray[dtype]) -> NDArrayShape
```

Returns the shape of the NDArray.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArrayShape`

#### Overload 2

```mojo
def shape[cdtype: ComplexDType](array: ComplexNDArray[cdtype]) -> NDArrayShape
```

Returns the shape of the NDArray.

Returns: The shape of the NDArray.

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `array` (`ComplexNDArray[cdtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArrayShape`


</div>

<div class="fn-card" markdown="1">

### `size`

#### Overload 1

```mojo
def size[dtype: DType](array: NDArray[dtype], axis: Int) -> Int
```

Returns the size of the NDArray.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `axis` (`Int`) `[imm]`: The axis to get the size of.

**Returns:**

- `Int`

!!! failure "Raises"

#### Overload 2

```mojo
def size[cdtype: ComplexDType](array: ComplexNDArray[cdtype], axis: Int) -> Int
```

Returns the size of the NDArray.

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `array` (`ComplexNDArray[cdtype]`) `[imm]`: A NDArray.
- `axis` (`Int`) `[imm]`: The axis to get the size of.

**Returns:**

- `Int`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `reshape`

```mojo
def reshape[dtype: DType](A: NDArray[dtype], shape: NDArrayShape, order: String = "C") -> NDArray[dtype]
```

Returns an array of the same data with a new shape.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `shape` (`NDArrayShape`) `[imm]`: New shape.
- `order` (`String`) `[imm]`: "C" or "F". Read in this order from the original array and
    write in this order into the new array.

**Returns:**

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

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `order` (`String`) `[imm]`: The order to flatten the array.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `transpose`

#### Overload 1

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

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`
- `axes` (`List[Int]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def transpose[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```

(overload) Transpose the array when `axes` is not given. If `axes` is not given, it is equal to flipping the axes. See docstring of `transpose`.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `broadcast_to`

```mojo
def broadcast_to[dtype: DType](a: NDArray[dtype], shape: NDArrayShape) -> NDArray[dtype]
```

Returns a non-owning view of `a` broadcast to `shape`, following NumPy broadcasting rules (trailing-dimension alignment, size-1 dims stretch).

Notes:
The returned array shares the underlying buffer with `a` (refcounted,
zero-copy): broadcast dimensions get stride 0, so no new memory is
allocated. Because stride-0 dimensions are never C-contiguous, any
operation that needs a flat contiguous buffer (e.g. SIMD elementwise
kernels) will materialize the view via `.contiguous()` on demand.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: The array to broadcast.
- `shape` (`NDArrayShape`) `[imm]`: The target shape.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `a.shape` cannot be broadcast to `shape`.


</div>

<div class="fn-card" markdown="1">

### `flip`

#### Overload 1

```mojo
def flip[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Returns flipped array and keep the shape.

**Parameters:**

- `dtype` (`DType`): DType.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def flip[dtype: DType](array: NDArray[dtype], var axis: Int) -> NDArray[dtype]
```

Returns flipped array along the given axis.

**Parameters:**

- `dtype` (`DType`): DType.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `axis` (`Int`) `[var]`: Axis along which to flip.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `concatenate`

```mojo
def concatenate[dtype: DType](*arrays: NDArray[dtype], *, axis: Int = Int(0)) -> NDArray[dtype]
```

Join a sequence of arrays along an existing axis.

Examples:
```mojo
import numojo as nm
var a = nm.arange[nm.f64](0, 6, 1)
var a2d = nm.reshape(a, nm.Shape(2, 3))
var b = nm.arange[nm.f64](6, 12, 1)
var b2d = nm.reshape(b, nm.Shape(2, 3))
var c = nm.concatenate(a2d, b2d, axis=0)  # Shape (4, 3)
var d = nm.concatenate(a2d, b2d, axis=1)  # Shape (2, 6)
```

**Parameters:**

- `dtype` (`DType`): The data type of the arrays.

**Args:**

- `*arrays` (`NDArray[dtype]`) `[imm]`: The arrays to concatenate. All arrays must have the same
    shape except in the dimension corresponding to `axis`.
- `axis` (`Int`) `[imm]`: The axis along which the arrays will be joined. Default is 0.

**Returns:**

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

Examples:
```mojo
import numojo as nm
var a = nm.arange[nm.f64](0, 3, 1)   # Shape (3,)
var b = nm.arange[nm.f64](3, 6, 1)   # Shape (3,)
var c = nm.column_stack(a, b)         # Shape (3, 2)
```

**Parameters:**

- `dtype` (`DType`): The data type of the arrays.

**Args:**

- `*arrays` (`NDArray[dtype]`) `[imm]`: The arrays to stack. 1-D arrays are treated as column
    vectors. All arrays must have the same number of rows
    (first dimension).

**Returns:**

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

Examples:
```mojo
import numojo as nm
var a = nm.arange[nm.f64](0, 3, 1)  # Shape (3,)
var b = nm.arange[nm.f64](3, 6, 1)  # Shape (3,)
var c = nm.row_stack(a, b)           # Shape (2, 3)
```

**Parameters:**

- `dtype` (`DType`): The data type of the arrays.

**Args:**

- `*arrays` (`NDArray[dtype]`) `[imm]`: The arrays to stack. 1-D arrays of shape `(N,)` are
    reshaped to `(1, N)` before concatenation.

**Returns:**

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

Examples:
```mojo
import numojo as nm
var a = nm.arange[nm.f64](0, 3, 1)  # Shape (3,)
var b = nm.arange[nm.f64](3, 6, 1)  # Shape (3,)
var c = nm.hstack(a, b)              # Shape (6,)
```

**Parameters:**

- `dtype` (`DType`): The data type of the arrays.

**Args:**

- `*arrays` (`NDArray[dtype]`) `[imm]`: The arrays to stack.

**Returns:**

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

Examples:
```mojo
import numojo as nm
var a = nm.arange[nm.f64](0, 3, 1)  # Shape (3,)
var b = nm.arange[nm.f64](3, 6, 1)  # Shape (3,)
var c = nm.vstack(a, b)              # Shape (2, 3)
```

**Parameters:**

- `dtype` (`DType`): The data type of the arrays.

**Args:**

- `*arrays` (`NDArray[dtype]`) `[imm]`: The arrays to stack.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the list of arrays is empty.


</div>
