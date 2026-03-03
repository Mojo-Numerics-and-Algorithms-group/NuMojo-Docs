# `numojo.routines.manipulation`

Manipulation routines (numojo.routines.manipulation)

This module implements routines that manipulate the shape and layout of arrays, such as reshaping, transposing, broadcasting, and flipping.

## Functions


<div class="fn-card" markdown="1">

### `copyto`

```mojo
copyto()
```


</div>

<div class="fn-card" markdown="1">

### `ndim`

#### Overload 1

```mojo
ndim[dtype: DType](array: NDArray[dtype]) -> Int
```

Returns the number of dimensions of the NDArray.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array` (`NDArray`): A NDArray.

**Returns:**

- `Int`

#### Overload 2

```mojo
ndim[cdtype: ComplexDType](array: ComplexNDArray[cdtype]) -> Int
```

Returns the number of dimensions of the NDArray.

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `array` (`ComplexNDArray`): A NDArray.

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

### `shape`

#### Overload 1

```mojo
shape[dtype: DType](array: NDArray[dtype]) -> NDArrayShape
```

Returns the shape of the NDArray.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArrayShape`

#### Overload 2

```mojo
shape[cdtype: ComplexDType](array: ComplexNDArray[cdtype]) -> NDArrayShape
```

Returns the shape of the NDArray.

Returns: The shape of the NDArray.

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `array` (`ComplexNDArray`): A NDArray.

**Returns:**

- `NDArrayShape`


</div>

<div class="fn-card" markdown="1">

### `size`

#### Overload 1

```mojo
size[dtype: DType](array: NDArray[dtype], axis: Int) -> Int
```

Returns the size of the NDArray.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array` (`NDArray`): A NDArray.
- `axis` (`Int`): The axis to get the size of.

**Returns:**

- `Int`

!!! failure "Raises"

#### Overload 2

```mojo
size[cdtype: ComplexDType](array: ComplexNDArray[cdtype], axis: Int) -> Int
```

Returns the size of the NDArray.

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `array` (`ComplexNDArray`): A NDArray.
- `axis` (`Int`): The axis to get the size of.

**Returns:**

- `Int`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `reshape`

```mojo
reshape[dtype: DType](A: NDArray[dtype], shape: NDArrayShape, order: String = "C") -> NDArray[dtype]
```

Returns an array of the same data with a new shape.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray`): A NDArray.
- `shape` (`NDArrayShape`): New shape.
- `order` (`String`): "C" or "F". Read in this order from the original array and
    write in this order into the new array.

**Returns:**

- `NDArray`

!!! failure "Raises"
    Error: If the number of elements do not match.


</div>

<div class="fn-card" markdown="1">

### `ravel`

```mojo
ravel[dtype: DType](a: NDArray[dtype], order: String = "C") -> NDArray[dtype]
```

Returns the raveled version of the NDArray.

Return:
    A contiguous flattened array.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray`): NDArray.
- `order` (`String`): The order to flatten the array.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `transpose`

#### Overload 1

```mojo
transpose[dtype: DType](A: NDArray[dtype], axes: List[Int]) -> NDArray[dtype]
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

- `A` (`NDArray`)
- `axes` (`List`)

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
transpose[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```

(overload) Transpose the array when `axes` is not given. If `axes` is not given, it is equal to flipping the axes. See docstring of `transpose`.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray`)

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
transpose[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

Transpose of matrix.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `reorder_layout`

```mojo
reorder_layout[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

Create a new Matrix with the opposite layout from A: if A is C-contiguous, then create a new F-contiguous matrix of the same shape. If A is F-contiguous, create a new C-contiguous matrix.

Copy data into the new layout.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `broadcast_to`

#### Overload 1

```mojo
broadcast_to[dtype: DType](a: NDArray[dtype], shape: NDArrayShape) -> NDArray[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray`)
- `shape` (`NDArrayShape`)

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
broadcast_to[dtype: DType](A: Matrix[dtype], shape: Tuple[Int, Int], override_order: String = "") -> Matrix[dtype]
```

Broadcasts the vector to the given shape.

Example:

```console
> from numojo import Matrix
> a = Matrix.fromstring("1 2 3", shape=(1, 3))
> print(mat.broadcast_to(a, (3, 3)))
[[1.0   2.0     3.0]
 [1.0   2.0     3.0]
 [1.0   2.0     3.0]]
> a = Matrix.fromstring("1 2 3", shape=(3, 1))
> print(mat.broadcast_to(a, (3, 3)))
[[1.0   1.0     1.0]
 [2.0   2.0     2.0]
 [3.0   3.0     3.0]]
> a = Matrix.fromstring("1", shape=(1, 1))
> print(mat.broadcast_to(a, (3, 3)))
[[1.0   1.0     1.0]
 [1.0   1.0     1.0]
 [1.0   1.0     1.0]]
> a = Matrix.fromstring("1 2", shape=(1, 2))
> print(mat.broadcast_to(a, (1, 2)))
[[1.0   2.0]]
> a = Matrix.fromstring("1 2 3 4", shape=(2, 2))
> print(mat.broadcast_to(a, (4, 2)))
Unhandled exception caught during execution: Cannot broadcast shape 2x2 to shape 4x2!
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)
- `shape` (`Tuple`)
- `override_order` (`String`)

**Returns:**

- `Matrix`

!!! failure "Raises"

#### Overload 3

```mojo
broadcast_to[dtype: DType](A: Scalar[dtype], shape: Tuple[Int, Int], order: String) -> Matrix[dtype]
```

Broadcasts the scalar to the given shape.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Scalar`)
- `shape` (`Tuple`)
- `order` (`String`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `flip`

#### Overload 1

```mojo
flip[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Returns flipped array and keep the shape.

**Parameters:**

- `dtype` (`DType`): DType.

**Args:**

- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
flip[dtype: DType](array: NDArray[dtype], var axis: Int) -> NDArray[dtype]
```

Returns flipped array along the given axis.

**Parameters:**

- `dtype` (`DType`): DType.

**Args:**

- `array` (`NDArray`): A NDArray.
- `axis` (`Int`) `[var]`: Axis along which to flip.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>
