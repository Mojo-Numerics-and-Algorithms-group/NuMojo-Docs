# `numojo.routines.linalg.solving`

Linear equation solvers.

Solver for `Ax = y` systems using LU decomposition algorithm, and matrix
inverse computation.

Exports
-------
- `solve`: Solve linear system.
- `inv`: Matrix inverse.

## Functions


<div class="fn-card" markdown="1">

### `forward_substitution`

```mojo
def forward_substitution[dtype: DType](L: NDArray[dtype], y: NDArray[dtype]) -> NDArray[dtype]
```

Perform forward substitution to solve `Lx = y`.

Paramters:
    dtype: dtype of the resulting vector.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `L` (`NDArray[dtype]`) `[imm]`: A lower triangular matrix.
- `y` (`NDArray[dtype]`) `[imm]`: A vector.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `back_substitution`

```mojo
def back_substitution[dtype: DType](U: NDArray[dtype], y: NDArray[dtype]) -> NDArray[dtype]
```

Perform forward substitution to solve `Ux = y`.

Paramters:
    dtype: dtype of the resulting vector.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `U` (`NDArray[dtype]`) `[imm]`: A upper triangular matrix.
- `y` (`NDArray[dtype]`) `[imm]`: A vector.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `inv`

```mojo
def inv[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```

Find the inverse of a non-singular, row-major matrix.

It uses the function `solve()` to solve `AB = I` for B, where I is
an identity matrix.

The speed is faster than numpy for matrices smaller than 100x100,
and is slower for larger matrices.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the inverse matrix.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: Input matrix. It should be non-singular, square, and row-major.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `inv_lu`

```mojo
def inv_lu[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Find the inverse of a non-singular, row-major matrix.

Use LU decomposition algorithm.

The speed is faster than numpy for matrices smaller than 100x100,
and is slower for larger matrices.

`AX = I` where `I` is an identity matrix.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the inverse matrix.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: Input matrix. It should be non-singular, square, and row-major.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `solve`

```mojo
def solve[dtype: DType](A: NDArray[dtype], Y: NDArray[dtype]) -> NDArray[dtype]
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
def main() raises:
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

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the inversed matrix.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: Non-singular, square, and row-major matrix. The size is m x m.
- `Y` (`NDArray[dtype]`) `[imm]`: Array of size m x n.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
