# `numojo.routines.linalg.solving`

Linear Algebra Solver (numojo.routines.linalg.solving)

Provides:
    - Solver of `Ax = y` using LU decomposition algorithm.
    - Inverse of an invertible matrix.

## Functions


<div class="fn-card" markdown="1">

### `forward_substitution`

```mojo
forward_substitution[dtype: DType](L: NDArray[dtype], y: NDArray[dtype]) -> NDArray[dtype]
```

Perform forward substitution to solve `Lx = y`.

Paramters:
    dtype: dtype of the resulting vector.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `L` (`NDArray`): A lower triangular matrix.
- `y` (`NDArray`): A vector.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `back_substitution`

```mojo
back_substitution[dtype: DType](U: NDArray[dtype], y: NDArray[dtype]) -> NDArray[dtype]
```

Perform forward substitution to solve `Ux = y`.

Paramters:
    dtype: dtype of the resulting vector.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `U` (`NDArray`): A upper triangular matrix.
- `y` (`NDArray`): A vector.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `inv`

#### Overload 1

```mojo
inv[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```

Find the inverse of a non-singular, row-major matrix.

It uses the function `solve()` to solve `AB = I` for B, where I is
an identity matrix.

The speed is faster than numpy for matrices smaller than 100x100,
and is slower for larger matrices.

**Parameters:**

- `dtype` (`DType`): Data type of the inverse matrix.

**Args:**

- `A` (`NDArray`): Input matrix. It should be non-singular, square, and row-major.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
inv[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

Inverse of matrix.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `inv_lu`

```mojo
inv_lu[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Find the inverse of a non-singular, row-major matrix.

Use LU decomposition algorithm.

The speed is faster than numpy for matrices smaller than 100x100,
and is slower for larger matrices.

`AX = I` where `I` is an identity matrix.

**Parameters:**

- `dtype` (`DType`): Data type of the inverse matrix.

**Args:**

- `array` (`NDArray`): Input matrix. It should be non-singular, square, and row-major.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `lstsq`

```mojo
lstsq[dtype: DType](X: Matrix[dtype], y: Matrix[dtype]) -> Matrix[dtype]
```

Caclulate the OLS estimates.

Example:
```text
from numojo import Matrix
X = Matrix.rand((1000000, 5))
y = Matrix.rand((1000000, 1))
print(lstsq(X, y))
```
```text
[[0.18731374756029967]
 [0.18821352688798607]
 [0.18717162200411439]
 [0.1867570378683612]
 [0.18828715376701158]]
Size: 5x1  DType: float64
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `X` (`Matrix`)
- `y` (`Matrix`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `solve`

#### Overload 1

```mojo
solve[dtype: DType](A: NDArray[dtype], Y: NDArray[dtype]) -> NDArray[dtype]
```

Solve the linear system `AX = Y` for `X`.

`A` should be a non-singular, row-major matrix (m x m).
`Y` should be a matrix of (m x n).
`X` is a matrix of (m x n).
LU decomposition algorithm is adopted.

The speed is faster than numpy for matrices smaller than 100x100,
and is slower for larger matrices.

For efficiency, `dtype` of the output array will be the same as the input
arrays. Thus, use `astype()` before passing the arrays to this function.


An example goes as follows.

```mojo
import numojo as nm
fn main() raises:
    var A = nm.fromstring("[[1, 0, 1], [0, 2, 1], [1, 1, 1]]")
    var B = nm.fromstring("[[1, 0, 0], [0, 1, 0], [0, 0, 1]]")
    var X = nm.linalg.solve(A, B)
    print(X)
```
```console
[[      -1.0    -1.0    2.0     ]
 [      -1.0    0.0     1.0     ]
 [      2.0     1.0     -2.0    ]]
2-D array  Shape: [3, 3]  DType: float64
```

The example is also a way to calculate inverse of matrix.

**Parameters:**

- `dtype` (`DType`): Data type of the inversed matrix.

**Args:**

- `A` (`NDArray`): Non-singular, square, and row-major matrix. The size is m x m.
- `Y` (`NDArray`): Matrix of size m x n.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
solve[dtype: DType](A: Matrix[dtype], Y: Matrix[dtype]) -> Matrix[dtype]
```

Solve `AX = Y` using LUP decomposition.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)
- `Y` (`Matrix`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `solve_lu`

```mojo
solve_lu[dtype: DType](A: Matrix[dtype], Y: Matrix[dtype]) -> Matrix[dtype]
```

Solve `AX = Y` using LU decomposition.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)
- `Y` (`Matrix`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>
