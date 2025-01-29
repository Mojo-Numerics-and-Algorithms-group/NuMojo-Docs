



# decompositions

##  Module Summary
  

## compute_householder


```rust
compute_householder[dtype: DType](mut H: Matrix[dtype], mut R: Matrix[dtype], row: Int, column: Int)
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- H
- R
- row
- column

## compute_qr


```rust
compute_qr[dtype: DType](mut H: Matrix[dtype], work_index: Int, mut A: Matrix[dtype], row_start: Int, column_start: Int)
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- H
- work_index
- A
- row_start
- column_start

## lu_decomposition


```rust
lu_decomposition[dtype: DType](A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[dtype]]
```  
Summary  
  
Perform LU (lower-upper) decomposition for array.  
  
Parameters:  

- dtype: Data type of the upper and upper triangular matrices.
  
Args:  

- A: Input matrix for decomposition. It should be a row-major matrix.


```rust
lu_decomposition[dtype: DType](A: Matrix[dtype]) -> Tuple[Matrix[dtype], Matrix[dtype]]
```  
Summary  
  
Perform LU (lower-upper) decomposition for matrix.  
  
Parameters:  

- dtype
  
Args:  

- A

## partial_pivoting


```rust
partial_pivoting[dtype: DType](owned A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[dtype], Int]
```  
Summary  
  
Perform partial pivoting for a square matrix.  
  
Parameters:  

- dtype
  
Args:  

- A: 2-d square array.


```rust
partial_pivoting[dtype: DType](owned A: Matrix[dtype]) -> Tuple[Matrix[dtype], Matrix[dtype], Int]
```  
Summary  
  
Perform partial pivoting for matrix.  
  
Parameters:  

- dtype
  
Args:  

- A

## qr


```rust
qr[dtype: DType](owned A: Matrix[dtype]) -> Tuple[Matrix[dtype], Matrix[dtype]]
```  
Summary  
  
Compute the QR decomposition of a matrix.  
  
Parameters:  

- dtype
  
Args:  

- A: The input matrix to be factorized.
