# `numojo.routines.linalg.decompositions`

Matrix decomposition operations.

Functions for decomposing NDArrays representing 2-D matrices (LU
decomposition with partial pivoting).

Exports
-------
- `lu_decomposition`: LU factorization.
- `qr`: QR factorization (Householder reflections).
- `cholesky`: Cholesky factorization.
- `eigh`: Eigenvalues/eigenvectors of a real symmetric matrix.
- `eig`: Eigenvalues/eigenvectors of a general real matrix.
- `svd`: Singular value decomposition.
- `matrix_rank`: Rank via singular values.
- `cond`: Condition number via singular values.

## Functions


<div class="fn-card" markdown="1">

### `lu_decomposition`

```mojo
def lu_decomposition[dtype: DType](A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[dtype]]
```

Perform LU (lower-upper) decomposition for array.

For efficiency, `dtype` of the output arrays will be the same as the input
array. Thus, use `astype()` before passing the array to this function.

<div class="prose-label">Examples</div>
```
import numojo as nm
def main() raises:
    var arr = nm.NDArray[nm.f64]("[[1,2,3], [4,5,6], [7,8,9]]")
    var U: nm.NDArray
    var L: nm.NDArray
    L, U = nm.linalg.lu_decomposition(arr)
    print(arr)
    print(L)
    print(U)
```
```console
[[      1.0     2.0     3.0     ]
 [      4.0     5.0     6.0     ]
 [      7.0     8.0     9.0     ]]
2-D array  Shape: [3, 3]  DType: float64
[[      1.0     0.0     0.0     ]
 [      4.0     1.0     0.0     ]
 [      7.0     2.0     1.0     ]]
2-D array  Shape: [3, 3]  DType: float64
[[      1.0     2.0     3.0     ]
 [      0.0     -3.0    -6.0    ]
 [      0.0     0.0     0.0     ]]
2-D array  Shape: [3, 3]  DType: float64
```

<div class="prose-label">Further Reading</div>
- Linear Algebra And Its Applications, fourth edition, Gilbert Strang
- https://en.wikipedia.org/wiki/LU_decomposition
- https://www.scicoding.com/how-to-calculate-lu-decomposition-in-python/
- https://courses.physics.illinois.edu/cs357/sp2020/notes/ref-9-linsys.html.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the upper and upper triangular matrices.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: Input matrix for decomposition. It should be a row-major matrix.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[dtype], NDArray[dtype]]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `partial_pivoting`

```mojo
def partial_pivoting[dtype: DType](var A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[dtype], Int]
```

Perform partial pivoting for a square matrix.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[var]`: 2-d square array.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[dtype], NDArray[dtype], Int]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `qr`

```mojo
def qr[dtype: DType](A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[dtype]]
```

Perform QR decomposition of a matrix using Householder reflections.

Computes the "reduced" (economy) factorization, matching
`numpy.linalg.qr` with `mode="reduced"` (the default): for an input
of shape `(m, n)`, `Q` has shape `(m, k)` with orthonormal columns
and `R` has shape `(k, n)` and is upper triangular, where
`k = min(m, n)`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var A = nm.fromstring("[[1, 2], [3, 4], [5, 6]]")
    var Q: nm.NDArray
    var R: nm.NDArray
    Q, R = nm.linalg.qr(A)
    print(Q @ R)  # reconstructs A
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the input and output matrices. Should be a
    floating-point type.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: Input matrix of shape `(m, n)`.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[dtype], NDArray[dtype]]`

!!! failure "Raises"
    NumojoError: If the array is not 2-dimensional.


</div>

<div class="fn-card" markdown="1">

### `cholesky`

```mojo
def cholesky[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```

Compute the Cholesky decomposition of a symmetric positive-definite matrix.

Finds the lower triangular matrix `L` such that `A = L @ L.T`,
matching `numpy.linalg.cholesky`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var A = nm.fromstring("[[4, 2], [2, 3]]")
    var L = nm.linalg.cholesky(A)
    print(L @ L.T)  # reconstructs A
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the input and output matrices. Should be a
    floating-point type.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: Symmetric positive-definite matrix of shape `(n, n)`.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the array is not 2-dimensional or not square.
NumojoError: If the array is not positive-definite (a
non-positive value is encountered on the diagonal during
factorization).


</div>

<div class="fn-card" markdown="1">

### `eigh`

```mojo
def eigh[dtype: DType](A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[dtype]] where dtype.is_floating_point()
```

Compute the eigenvalues and eigenvectors of a real symmetric matrix.

Uses the cyclic Jacobi eigenvalue algorithm. `A` is assumed to be
symmetric; only the values given are used (no symmetry check is
performed).

Returns a tuple `(w, v)` where `w` is a 1-D array of the eigenvalues
in ascending order, and `v` is a 2-D array whose column `v[:, i]` is
the normalized eigenvector corresponding to `w[i]`, such that
`A @ v[:, i] == w[i] * v[:, i]`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var A = nm.fromstring("[[2, 1], [1, 2]]")
    var w: nm.NDArray
    var v: nm.NDArray
    w, v = nm.linalg.eigh(A)
    print(w)
    print(v)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the input and output matrices. Should be a
    floating-point type.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: Symmetric matrix of shape `(n, n)`.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[dtype], NDArray[dtype]]`

!!! failure "Raises"
    NumojoError: If the array is not 2-dimensional or not square.


</div>

<div class="fn-card" markdown="1">

### `eig`

```mojo
def eig[dtype: DType](A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[dtype]] where dtype.is_floating_point()
```

Compute the eigenvalues and eigenvectors of a general real square matrix.

Uses the shifted QR algorithm (Rayleigh quotient shift) to find
the eigenvalues, then shifted inverse iteration on the original
matrix to recover the corresponding eigenvectors.

Only matrices with real eigenvalues are supported. If the QR
iteration does not converge to an (approximately) upper triangular
form, this raises, since that indicates the matrix has complex
eigenvalues.

Unlike `numpy.linalg.eig`, the eigenvalues are not returned in any
particular order.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var A = nm.fromstring("[[2, 0], [0, 3]]")
    var w: nm.NDArray
    var v: nm.NDArray
    w, v = nm.linalg.eig(A)
    print(w)
    print(v)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the input and output matrices. Should be a
    floating-point type.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: Square matrix of shape `(n, n)`.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[dtype], NDArray[dtype]]`

!!! failure "Raises"
    NumojoError: If the array is not 2-dimensional or not square.
NumojoError: If the matrix appears to have complex eigenvalues.


</div>

<div class="fn-card" markdown="1">

### `svd`

```mojo
def svd[dtype: DType](A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[dtype], NDArray[dtype]] where dtype.is_floating_point()
```

Compute the economy (reduced) singular value decomposition of `A`.

Computed via the eigendecomposition of `A.T @ A`. Only supports
matrices of full rank `min(m, n)`; raises if a singular value is
(numerically) zero.

Matches `numpy.linalg.svd(A, full_matrices=False)`: returns a
tuple `(U, s, Vh)` with `U` of shape `(m, k)`, `s` of shape `(k,)`
in descending order, and `Vh` of shape `(k, n)`, where
`k = min(m, n)`, such that `U @ diag(s) @ Vh` reconstructs `A`,
with orthonormal columns of `U` and orthonormal rows of `Vh`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var A = nm.fromstring("[[1, 2], [3, 4], [5, 6]]")
    var U: nm.NDArray
    var s: nm.NDArray
    var Vh: nm.NDArray
    U, s, Vh = nm.linalg.svd(A)
    print(U @ nm.diag(s) @ Vh)  # reconstructs A
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the input and output matrices. Should be a
    floating-point type.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: Matrix of shape `(m, n)`.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[dtype], NDArray[dtype], NDArray[dtype]]`

!!! failure "Raises"
    NumojoError: If the array is not 2-dimensional.
NumojoError: If `A` is rank-deficient.


</div>

<div class="fn-card" markdown="1">

### `matrix_rank`

```mojo
def matrix_rank[dtype: DType](A: NDArray[dtype], tol: Scalar[dtype] = 0) -> Int where dtype.is_floating_point()
```

Estimate the rank of `A` by counting the number of singular values greater than `tol`.

If `tol <= 0` (the default), a tolerance of
`largest_singular_value * 1e-6` is used.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var A = nm.fromstring("[[1, 2], [2, 4]]")  # rank 1
    print(nm.linalg.matrix_rank(A))
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the input matrix. Should be a
    floating-point type.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: Matrix of shape `(m, n)`.
- `tol` (`Scalar[dtype]`) `[imm]`: Singular values at or below this threshold are treated as
    zero.

<div class="prose-label">Returns</div>

- `Int`

!!! failure "Raises"
    NumojoError: If the array is not 2-dimensional.


</div>

<div class="fn-card" markdown="1">

### `cond`

```mojo
def cond[dtype: DType](A: NDArray[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Compute the 2-norm condition number of `A`: the ratio of its largest to smallest singular value.

Matches `numpy.linalg.cond(A)` (the default `p=2`). Other `ord`
values are not yet supported.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var A = nm.fromstring("[[1, 0], [0, 2]]")
    print(nm.linalg.cond(A))  # 2.0
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the input matrix. Should be a
    floating-point type.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: Matrix of shape `(m, n)`.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If the array is not 2-dimensional.


</div>
