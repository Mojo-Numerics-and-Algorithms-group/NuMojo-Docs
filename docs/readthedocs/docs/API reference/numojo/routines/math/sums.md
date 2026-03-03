# `numojo.routines.math.sums`

Summation routines for NuMojo (numojo.routines.math.sums).

Provides sum reductions along axes for NDArrays and Matrices, covering both flattened and axis-aware workflows.

## Functions


<div class="fn-card" markdown="1">

### `sum`

#### Overload 1

```mojo
sum[dtype: DType](A: NDArray[dtype]) -> Scalar[dtype]
```

Returns sum of all items in the array.

Example:
```console
> print(A)
[[      0.1315377950668335      0.458650141954422       0.21895918250083923     ]
 [      0.67886471748352051     0.93469291925430298     0.51941639184951782     ]
 [      0.034572109580039978    0.52970021963119507     0.007698186207562685    ]]
2-D array  Shape: [3, 3]  DType: float32
> print(nm.sum(A))
3.5140917301177979
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
sum[dtype: DType](A: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Returns sums of array elements over a given axis.

Example:
```mojo
import numojo as nm
var A = nm.random.randn(100, 100)
print(nm.sum(A, axis=0))
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray`): NDArray.
- `axis` (`Int`): The axis along which the sum is performed.

**Returns:**

- `NDArray`

!!! failure "Raises"
    Error: If the axis is out of bound.
Error: If the number of dimensions is 1.

#### Overload 3

```mojo
sum[dtype: DType](A: Matrix[dtype]) -> Scalar[dtype]
```

Sum up all items in the Matrix.

Example:
```mojo
from numojo import Matrix
var A = Matrix.rand(shape=(100, 100))
print(mat.sum(A))
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`): Matrix.

**Returns:**

- `Scalar`

#### Overload 4

```mojo
sum[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```

Sum up the items in a Matrix along the axis.

Example:
```mojo
from numojo import Matrix
var A = Matrix.rand(shape=(100, 100))
print(mat.sum(A, axis=0))
print(mat.sum(A, axis=1))
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

### `cumsum`

#### Overload 1

```mojo
cumsum[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```

Returns cumsum of all items of an array. The array is flattened before cumsum.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `A` (`NDArray`): NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
cumsum[dtype: DType](A: NDArray[dtype], var axis: Int) -> NDArray[dtype]
```

Returns cumsum of array by axis.

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
cumsum[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

Cumsum of flattened matrix.

Example:
```mojo
from numojo import Matrix
var A = Matrix.rand(shape=(100, 100))
print(mat.cumsum(A))
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
cumsum[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```

Cumsum of Matrix along the axis.

Example:
```mojo
from numojo import Matrix
var A = Matrix.rand(shape=(100, 100))
print(mat.cumsum(A, axis=0))
print(mat.cumsum(A, axis=1))
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
