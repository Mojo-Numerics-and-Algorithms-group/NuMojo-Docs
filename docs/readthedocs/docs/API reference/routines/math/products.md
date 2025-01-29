



# products

##  Module Summary
  

## prod


```rust
prod[dtype: DType](A: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Returns products of all items in the array.  
  
Parameters:  

- dtype
  
Args:  

- A: NDArray.


```rust
prod[dtype: DType](A: NDArray[dtype], owned axis: Int) -> NDArray[dtype]
```  
Summary  
  
Returns products of array elements over a given axis.  
  
Parameters:  

- dtype
  
Args:  

- A: NDArray.
- axis: The axis along which the product is performed.


```rust
prod[dtype: DType](A: Matrix[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Product of all items in the Matrix.  
  
Parameters:  

- dtype
  
Args:  

- A: Matrix.


```rust
prod[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```  
Summary  
  
Product of items in a Matrix along the axis.  
  
Parameters:  

- dtype
  
Args:  

- A: Matrix.
- axis: 0 or 1.

## cumprod


```rust
cumprod[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Returns cumprod of all items of an array. The array is flattened before cumprod.  
  
Parameters:  

- dtype: The element type.
  
Args:  

- A: NDArray.


```rust
cumprod[dtype: DType](owned A: NDArray[dtype], owned axis: Int) -> NDArray[dtype]
```  
Summary  
  
Returns cumprod of array by axis.  
  
Parameters:  

- dtype: The element type.
  
Args:  

- A: NDArray.
- axis: Axis.


```rust
cumprod[dtype: DType](owned A: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
Cumprod of flattened matrix.  
  
Parameters:  

- dtype
  
Args:  

- A: Matrix.


```rust
cumprod[dtype: DType](owned A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```  
Summary  
  
Cumprod of Matrix along the axis.  
  
Parameters:  

- dtype
  
Args:  

- A: Matrix.
- axis: 0 or 1.
