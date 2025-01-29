



# sums

##  Module Summary
  

## sum


```rust
sum[dtype: DType](A: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Returns sum of all items in the array.  
  
Parameters:  

- dtype
  
Args:  

- A: NDArray.


```rust
sum[dtype: DType](A: NDArray[dtype], owned axis: Int) -> NDArray[dtype]
```  
Summary  
  
Returns sums of array elements over a given axis.  
  
Parameters:  

- dtype
  
Args:  

- A: NDArray.
- axis: The axis along which the sum is performed.


```rust
sum[dtype: DType](A: Matrix[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Sum up all items in the Matrix.  
  
Parameters:  

- dtype
  
Args:  

- A: Matrix.


```rust
sum[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```  
Summary  
  
Sum up the items in a Matrix along the axis.  
  
Parameters:  

- dtype
  
Args:  

- A: Matrix.
- axis: 0 or 1.

## cumsum


```rust
cumsum[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Returns cumsum of all items of an array. The array is flattened before cumsum.  
  
Parameters:  

- dtype: The element type.
  
Args:  

- A: NDArray.


```rust
cumsum[dtype: DType](owned A: NDArray[dtype], owned axis: Int) -> NDArray[dtype]
```  
Summary  
  
Returns cumsum of array by axis.  
  
Parameters:  

- dtype: The element type.
  
Args:  

- A: NDArray.
- axis: Axis.


```rust
cumsum[dtype: DType](owned A: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
Cumsum of flattened matrix.  
  
Parameters:  

- dtype
  
Args:  

- A: Matrix.


```rust
cumsum[dtype: DType](owned A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```  
Summary  
  
Cumsum of Matrix along the axis.  
  
Parameters:  

- dtype
  
Args:  

- A: Matrix.
- axis: 0 or 1.
