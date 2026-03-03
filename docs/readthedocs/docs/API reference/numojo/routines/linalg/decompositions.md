# `numojo.routines.linalg.decompositions`

Decompositions (numojo.routines.linalg.decompositions)

This module provides functions for matrix decompositions, including LU decomposition, QR decomposition, and eigenvalue decomposition for symmetric matrices.

## Functions


<div class="fn-card" markdown="1">

### `lu_decomposition`

#### Overload 1

```mojo
lu_decomposition[dtype: DType](A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[dtype]]
```

Perform LU (lower-upper) decomposition for array.

For efficiency, `dtype` of the output arrays will be the same as the input
array. Thus, use `astype()` before passing the array to this function.

Example:
```
import numojo as nm
fn main() raises:
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

Further readings:
- Linear Algebra And Its Applications, fourth edition, Gilbert Strang
- https://en.wikipedia.org/wiki/LU_decomposition
- https://www.scicoding.com/how-to-calculate-lu-decomposition-in-python/
- https://courses.physics.illinois.edu/cs357/sp2020/notes/ref-9-linsys.html.

**Parameters:**

- `dtype` (`DType`): Data type of the upper and upper triangular matrices.

**Args:**

- `A` (`NDArray`): Input matrix for decomposition. It should be a row-major matrix.

**Returns:**

- `Tuple`

!!! failure "Raises"

#### Overload 2

```mojo
lu_decomposition[dtype: DType](A: Matrix[dtype]) -> Tuple[Matrix[dtype], Matrix[dtype]]
```

Perform LU (lower-upper) decomposition for matrix.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Tuple`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `partial_pivoting`

#### Overload 1

```mojo
partial_pivoting[dtype: DType](var A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[dtype], Int]
```

Perform partial pivoting for a square matrix.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray`) `[var]`: 2-d square array.

**Returns:**

- `Tuple`

!!! failure "Raises"

#### Overload 2

```mojo
partial_pivoting[dtype: DType](A: Matrix[dtype]) -> Tuple[Matrix[dtype], Matrix[dtype], Int]
```

Perform partial pivoting for matrix.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Tuple`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `qr`

```mojo
qr[dtype: DType](A: Matrix[dtype], mode: String = "reduced") -> Tuple[Matrix[dtype], Matrix[dtype]]
```

Computes the QR decomposition using Householder transformations. For best performance, the input matrix should be in column-major order.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`): The input matrix.
- `mode` (`String`): The mode of the decomposition. Can be "complete" or "reduced" simillar to numpy's QR decomposition.
    - "complete": Returns Q and R such that A = QR, where Q is m x m and R is m x n.
    - "reduced": Returns Q and R such that A = QR, where Q is m x min(m,n) and R is min(m,n) x n.

**Returns:**

- `Tuple`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `eig`

```mojo
eig[dtype: DType](A: Matrix[dtype], tol: Scalar[dtype] = 9.9999999999999998E-13, max_iter: Int = 10000) -> Tuple[Matrix[dtype], Matrix[dtype]]
```

Computes the eigenvalue decomposition for symmetric matrices using the QR algorithm. For best performance, the input matrix should be in column-major order.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`): The input matrix. Must be square and symmetric.
- `tol` (`Scalar`): Convergence tolerance for off-diagonal elements.
- `max_iter` (`Int`): Maximum number of iterations for the QR algorithm.

**Returns:**

- `Tuple`

!!! failure "Raises"
    Error: If the matrix is not square or symmetric.
Error: If the algorithm does not converge within max_iter iterations.


</div>
