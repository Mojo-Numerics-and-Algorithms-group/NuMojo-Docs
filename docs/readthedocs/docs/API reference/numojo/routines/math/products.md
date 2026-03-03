# `numojo.routines.math.products`

Product routines for NuMojo (numojo.routines.math.products).

Implements product and cumulative product reductions for NDArrays and Matrices.

## Functions


<div class="fn-card" markdown="1">

### `prod`

#### Overload 1

```mojo
prod[dtype: DType](A: NDArray[dtype]) -> Scalar[dtype]
```

Returns products of all items in the array.

Example:
```console
> print(A)
[[      0.1315377950668335      0.458650141954422       0.21895918250083923     ]
[      0.67886471748352051     0.93469291925430298     0.51941639184951782     ]
[      0.034572109580039978    0.52970021963119507     0.007698186207562685    ]]
2-D array  Shape: [3, 3]  DType: float32

> print(nm.prod(A))
6.1377261317829834e-07
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray`): NDArray.

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 2

```mojo
prod[dtype: DType](A: NDArray[dtype], var axis: Int) -> NDArray[dtype]
```

Returns products of array elements over a given axis.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray`): NDArray.
- `axis` (`Int`) `[var]`: The axis along which the product is performed.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
prod[dtype: DType](A: Matrix[dtype]) -> Scalar[dtype]
```

Product of all items in the Matrix.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`): Matrix.

**Returns:**

- `Scalar`

#### Overload 4

```mojo
prod[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```

Product of items in a Matrix along the axis.

Example:
```mojo
from numojo import Matrix
var A = Matrix.rand(shape=(100, 100))
print(mat.prod(A, axis=0))
print(mat.prod(A, axis=1))
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`): Matrix.
- `axis` (`Int`): 0 or 1.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `cumprod`

#### Overload 1

```mojo
cumprod[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```

Returns cumprod of all items of an array. The array is flattened before cumprod.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `A` (`NDArray`): NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
cumprod[dtype: DType](A: NDArray[dtype], var axis: Int) -> NDArray[dtype]
```

Returns cumprod of array by axis.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `A` (`NDArray`): NDArray.
- `axis` (`Int`) `[var]`: Axis.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
cumprod[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

Cumprod of flattened matrix.

Example:
```mojo
from numojo import Matrix
var A = Matrix.rand(shape=(100, 100))
print(mat.cumprod(A))
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`): Matrix.

**Returns:**

- `Matrix`

!!! failure "Raises"

#### Overload 4

```mojo
cumprod[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```

Cumprod of Matrix along the axis.

Example:
```mojo
from numojo import Matrix
var A = Matrix.rand(shape=(100, 100))
print(mat.cumprod(A, axis=0))
print(mat.cumprod(A, axis=1))
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`): Matrix.
- `axis` (`Int`): 0 or 1.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>
