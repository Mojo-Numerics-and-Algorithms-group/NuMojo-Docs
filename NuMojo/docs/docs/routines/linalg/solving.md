



# solving

##  Module Summary
  
Linear Algebra Solver
## forward_substitution


```Mojo
forward_substitution[dtype: DType](L: NDArray[dtype], y: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Perform forward substitution to solve `Lx = y`.  
  
Parameters:  

- dtype
  
Args:  

- L: A lower triangular matrix.
- y: A vector.


Paramters:
    dtype: dtype of the resulting vector.

## back_substitution


```Mojo
back_substitution[dtype: DType](U: NDArray[dtype], y: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Perform forward substitution to solve `Ux = y`.  
  
Parameters:  

- dtype
  
Args:  

- U: A upper triangular matrix.
- y: A vector.


Paramters:
    dtype: dtype of the resulting vector.

## inv


```Mojo
inv[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Find the inverse of a non-singular, row-major matrix.  
  
Parameters:  

- dtype: Data type of the inversed matrix.
  
Args:  

- A: Input matrix. It should be non-singular, square, and row-major.


It uses the function `solve()` to solve `AB = I` for B, where I is
an identity matrix.

The speed is faster than numpy for matrices smaller than 100x100,
and is slower for larger matrices.

## inv_raw


```Mojo
inv_raw[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Find the inverse of a non-singular, square matrix.  
  
Parameters:  

- dtype: Data type of the inversed matrix.
  
Args:  

- array: Input matrix. It should be non-singular and square.


WARNING: This function is slower than `inv`.
as it does not adopt parallelization by using raw methods.

An example goes as follows:

```
import numojo as nm
fn main() raises:
    var A = nm.NDArray("[[1,0,1], [0,2,1], [1,1,1]]")
    var B = nm.math.linalg.solver.inv_raw(A)
    print("Original matrix:")
    print(A)
    print("Reversed matrix:")
    print(B)
    print("Verify whether AB = I:")
    print(A @ B)
```
```console
Original matrix:
[[      1.0     0.0     1.0     ]
 [      0.0     2.0     1.0     ]
 [      1.0     1.0     1.0     ]]
2-D array  Shape: [3, 3]  DType: float64
Reversed matrix:
[[      -1.0    -1.0    2.0     ]
 [      -1.0    0.0     1.0     ]
 [      2.0     1.0     -2.0    ]]
2-D array  Shape: [3, 3]  DType: float64
Verify whether AB = I:
[[      1.0     0.0     0.0     ]
 [      0.0     1.0     0.0     ]
 [      0.0     0.0     1.0     ]]
2-D array  Shape: [3, 3]  DType: float64
```

TODO: Optimize the speed.
## inv_lu


```Mojo
inv_lu[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Find the inverse of a non-singular, row-major matrix.  
  
Parameters:  

- dtype: Data type of the inversed matrix.
  
Args:  

- array: Input matrix. It should be non-singular, square, and row-major.


Use LU decomposition algorithm.

The speed is faster than numpy for matrices smaller than 100x100,
and is slower for larger matrices.

TODO: Fix the issues in parallelization.
`AX = I` where `I` is an identity matrix.

## solve


```Mojo
solve[dtype: DType](A: NDArray[dtype], Y: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Solve the linear system `AX = Y` for `X`.  
  
Parameters:  

- dtype: Data type of the inversed matrix.
  
Args:  

- A: Non-singular, square, and row-major matrix. The size is m x m.
- Y: Matrix of size m x n.


`A` should be a non-singular, row-major matrix (m x m).
`Y` should be a matrix of (m x n).
`X` is a matrix of (m x n).
LU decomposition algorithm is adopted.

The speed is faster than numpy for matrices smaller than 100x100,
and is slower for larger matrices.

For efficiency, `dtype` of the output array will be the same as the input
arrays. Thus, use `astype()` before passing the arrays to this function.

TODO: Use LAPACK for large matrices when it is available.

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