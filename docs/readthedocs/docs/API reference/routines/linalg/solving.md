



# solving

##  Module Summary
  
Linear Algebra Solver
## forward_substitution


```rust
forward_substitution[dtype: DType](L: NDArray[dtype], y: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Perform forward substitution to solve `Lx = y`.  
  
Parameters:  

- dtype
  
Args:  

- L: A lower triangular matrix.
- y: A vector.

## back_substitution


```rust
back_substitution[dtype: DType](U: NDArray[dtype], y: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Perform forward substitution to solve `Ux = y`.  
  
Parameters:  

- dtype
  
Args:  

- U: A upper triangular matrix.
- y: A vector.

## inv


```rust
inv[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Find the inverse of a non-singular, row-major matrix.  
  
Parameters:  

- dtype: Data type of the inverse matrix.
  
Args:  

- A: Input matrix. It should be non-singular, square, and row-major.


```rust
inv[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
Inverse of matrix.  
  
Parameters:  

- dtype
  
Args:  

- A

## inv_lu


```rust
inv_lu[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Find the inverse of a non-singular, row-major matrix.  
  
Parameters:  

- dtype: Data type of the inverse matrix.
  
Args:  

- array: Input matrix. It should be non-singular, square, and row-major.

## lstsq


```rust
lstsq[dtype: DType](X: Matrix[dtype], y: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
Caclulate the OLS estimates.  
  
Parameters:  

- dtype
  
Args:  

- X
- y

## solve


```rust
solve[dtype: DType](A: NDArray[dtype], Y: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Solve the linear system `AX = Y` for `X`.  
  
Parameters:  

- dtype: Data type of the inversed matrix.
  
Args:  

- A: Non-singular, square, and row-major matrix. The size is m x m.
- Y: Matrix of size m x n.


```rust
solve[dtype: DType](A: Matrix[dtype], Y: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
Solve `AX = Y` using LUP decomposition.  
  
Parameters:  

- dtype
  
Args:  

- A
- Y

## solve_lu


```rust
solve_lu[dtype: DType](A: Matrix[dtype], Y: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
Solve `AX = Y` using LU decomposition.  
  
Parameters:  

- dtype
  
Args:  

- A
- Y
