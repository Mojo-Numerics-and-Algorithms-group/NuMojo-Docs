# `numojo.routines.linalg.products`

Array and vector product operations.

Functions for computing products of vectors and arrays (dot product, matrix
multiplication, cross product).

Exports
-------
- `dot`: Dot product of vectors.
- `matmul`: Matrix multiplication.
- `cross`: Cross product.

## Functions


<div class="fn-card" markdown="1">

### `cross`

```mojo
def cross[dtype: DType = DType.float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Compute the cross product of two arrays.

Parameters
    dtype: The element type.

!!! info "Constraints"
    `array1` and `array2` must be of shape (3,).

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A array.
- `array2` (`NDArray[dtype]`) `[imm]`: A array.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `dot`

```mojo
def dot[dtype: DType = DType.float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Compute the dot product of two arrays.

Parameters
    dtype: The element type.

!!! info "Constraints"
    `array1` and `array2` must be 1 dimensional.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A array.
- `array2` (`NDArray[dtype]`) `[imm]`: A array.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `tile`

```mojo
def tile[tiled_fn: def[tile_x: Int, tile_y: Int](Int, Int) capturing thin -> None, tile_x: Int, tile_y: Int](end_x: Int, end_y: Int)
```

**Parameters:**

- `tiled_fn` (`def[tile_x: Int, tile_y: Int](Int, Int) capturing thin -> None`)
- `tile_x` (`Int`)
- `tile_y` (`Int`)

**Args:**

- `end_x` (`Int`) `[imm]`
- `end_y` (`Int`) `[imm]`


</div>

<div class="fn-card" markdown="1">

### `matmul_tiled_unrolled_parallelized`

```mojo
def matmul_tiled_unrolled_parallelized[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Array multiplication vectorized, tiled, unrolled, and parallelized.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`
- `B` (`NDArray[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `matmul_1darray`

```mojo
def matmul_1darray[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Array multiplication for 1-d arrays (inner dot).

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`
- `B` (`NDArray[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `matmul_2darray`

```mojo
def matmul_2darray[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
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

- `A` (`NDArray[dtype]`) `[imm]`: First array.
- `B` (`NDArray[dtype]`) `[imm]`: Second array.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"
    When the shape does not match.


</div>

<div class="fn-card" markdown="1">

### `matmul`

```mojo
def matmul[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
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

- `A` (`NDArray[dtype]`) `[imm]`: First array.
- `B` (`NDArray[dtype]`) `[imm]`: Second array.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"
    (1) The shapes of first n-2 dimensions do not match.
(2) The shape of -2 dimension of first array does not match
the shape of -1 dimension of the second array.


</div>

<div class="fn-card" markdown="1">

### `matmul_naive`

```mojo
def matmul_naive[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Array multiplication with three nested loops.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`
- `B` (`NDArray[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>
