# `numojo.routines.linalg.products`

Matrix and vector products (numojo.routines.linalg.products)

This module provides functions for computing products of vectors and matrices, such as cross product, dot product, and matrix multiplication.

## Functions


<div class="fn-card" markdown="1">

### `cross`

```mojo
cross[dtype: DType = DType.float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Compute the cross product of two arrays.

Parameters
    dtype: The element type.

!!! info "Constraints"
    `array1` and `array2` must be of shape (3,).

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array1` (`NDArray`): A array.
- `array2` (`NDArray`): A array.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `dot`

```mojo
dot[dtype: DType = DType.float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Compute the dot product of two arrays.

Parameters
    dtype: The element type.

!!! info "Constraints"
    `array1` and `array2` must be 1 dimensional.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array1` (`NDArray`): A array.
- `array2` (`NDArray`): A array.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `tile`

```mojo
tile[tiled_fn: Static2DTileUnitFunc, tile_x: Int, tile_y: Int](end_x: Int, end_y: Int)
```

**Parameters:**

- `tiled_fn` (`Static2DTileUnitFunc`)
- `tile_x` (`Int`)
- `tile_y` (`Int`)

**Args:**

- `end_x` (`Int`)
- `end_y` (`Int`)


</div>

<div class="fn-card" markdown="1">

### `matmul_tiled_unrolled_parallelized`

```mojo
matmul_tiled_unrolled_parallelized[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Matrix multiplication vectorized, tiled, unrolled, and parallelized.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray`)
- `B` (`NDArray`)

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `matmul_1darray`

```mojo
matmul_1darray[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Array multiplication for 1-d arrays (inner dot).

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray`)
- `B` (`NDArray`)

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `matmul_2darray`

```mojo
matmul_2darray[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Array multiplication for 2-d arrays (inner dot).

Parameter:
    dtype: Data type.

Return:
    A multiplied by B.

Notes:
The multiplication is vectorized and parallelized.

References:
    [1] https://docs.modular.com/mojo/notebooks/Matmul.
    resultompared to the reference, we increases the size of
    the SIMD vector from the default width to 16. The purpose is to
    increase the performance via SIMD.
    This reduces the execution time by ~50 percent compared to
    `matmul_parallelized` and `matmul_tiled_unrolled_parallelized` for large
    matrices.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray`): First array.
- `B` (`NDArray`): Second array.

**Returns:**

- `NDArray`

!!! failure "Raises"
    When the shape does not match.


</div>

<div class="fn-card" markdown="1">

### `matmul`

#### Overload 1

```mojo
matmul[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Array multiplication for any dimensions.

Parameter:
    dtype: Data type.

Return:
    A multiplied by B.

Notes:

When A and B are 1darray, it is equal to dot of vectors:
`(i) @ (i) -> (1)`.

When A and B are 2darray, it is equal to inner products of matrices:
`(i,j) @ (j,k) -> (i,k)`.

When A and B are more than 2d, it is equal to a stack of 2darrays:
`(i,j,k) @ (i,k,l) -> (i,j,l)` and
`(i,j,k,l) @ (i,j,l,m) -> (i,j,k,m)`.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray`): First array.
- `B` (`NDArray`): Second array.

**Returns:**

- `NDArray`

!!! failure "Raises"
    (1) The shapes of first n-2 dimensions do not match.
(2) The shape of -2 dimension of first array does not match
the shape of -1 dimension of the second array.

#### Overload 2

```mojo
matmul[dtype: DType](A: Matrix[dtype], B: Matrix[dtype]) -> Matrix[dtype]
```

Matrix multiplication.

Example:
```mojo
from numojo import Matrix
from numojo.routines.linalg import matmul
var A = Matrix.rand(shape=(1000, 1000))
var B = Matrix.rand(shape=(1000, 1000))
var result = matmul(A, B)
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)
- `B` (`Matrix`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `matmul_naive`

```mojo
matmul_naive[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Matrix multiplication with three nested loops.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray`)
- `B` (`NDArray`)

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>
