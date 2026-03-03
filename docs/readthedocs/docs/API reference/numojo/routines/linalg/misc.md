# `numojo.routines.linalg.misc`

Miscellaneous Linear Algebra Routines (numojo.routines.linalg.misc)

This module provides miscellaneous linear algebra routines, such as extracting diagonals and checking for symmetry.

## Functions


<div class="fn-card" markdown="1">

### `diagonal`

```mojo
diagonal[dtype: DType](a: NDArray[dtype], offset: Int = 0) -> NDArray[dtype]
```

Returns specific diagonals. Currently supports only 2D arrays.

**Parameters:**

- `dtype` (`DType`): Data type of the array.

**Args:**

- `a` (`NDArray`): An NDArray.
- `offset` (`Int`): Offset of the diagonal from the main diagonal.

**Returns:**

- `NDArray`

!!! failure "Raises"
    Error: If the array is not 2D.
Error: If the offset is beyond the shape of the array.


</div>

<div class="fn-card" markdown="1">

### `issymmetric`

```mojo
issymmetric[dtype: DType](A: Matrix[dtype], rtol: Scalar[dtype] = 1.0000000000000001E-5, atol: Scalar[dtype] = 1.0E-8) -> Bool
```

Returns True if A is symmetric, False otherwise.

**Parameters:**

- `dtype` (`DType`): Data type of the Matrix Elements.

**Args:**

- `A` (`Matrix`): A Matrix.
- `rtol` (`Scalar`): Relative tolerance for comparison.
- `atol` (`Scalar`): Absolute tolerance for comparison.

**Returns:**

- `Bool`


</div>
