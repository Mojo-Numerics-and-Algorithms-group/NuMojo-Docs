



# averages

##  Module Summary
  
Averages and variances
## mean_1d


```rust
mean_1d[dtype: DType, //, returned_dtype: DType = float64](a: NDArray[dtype]) -> SIMD[returned_dtype, 1]
```  
Summary  
  
Calculate the arithmetic average of all items in an array. Regardless of the shape of input, it is treated as a 1-d array. It is the backend function for `mean`, with or without `axis`.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- a: A 1-d array.

## mean


```rust
mean[dtype: DType, //, returned_dtype: DType = float64](a: NDArray[dtype]) -> SIMD[returned_dtype, 1]
```  
Summary  
  
Calculate the arithmetic average of all items in the array.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- a: NDArray.


```rust
mean[dtype: DType, //, returned_dtype: DType = float64](a: NDArray[dtype], axis: Int) -> NDArray[returned_dtype]
```  
Summary  
  
Mean of array elements over a given axis.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- a: NDArray.
- axis: The axis along which the mean is performed.


```rust
mean[dtype: DType, //, returned_dtype: DType = float64](a: Matrix[dtype]) -> SIMD[returned_dtype, 1]
```  
Summary  
  
Calculate the arithmetic average of all items in the Matrix.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- a: A matrix.


```rust
mean[dtype: DType, //, returned_dtype: DType = float64](a: Matrix[dtype], axis: Int) -> Matrix[returned_dtype]
```  
Summary  
  
Calculate the arithmetic average of a Matrix along the axis.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- a: A matrix.
- axis: The axis along which the mean is performed.

## median_1d


```rust
median_1d[dtype: DType, //, returned_dtype: DType = float64](a: NDArray[dtype]) -> SIMD[returned_dtype, 1]
```  
Summary  
  
Median value of all items an array. Regardless of the shape of input, it is treated as a 1-d array.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- a: A 1-d array.

## median


```rust
median[dtype: DType, //, returned_dtype: DType = float64](a: NDArray[dtype]) -> SIMD[returned_dtype, 1]
```  
Summary  
  
Median value of all items of an array.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- a: A 1-d array.


```rust
median[dtype: DType, //, returned_dtype: DType = float64](a: NDArray[dtype], axis: Int) -> NDArray[returned_dtype]
```  
Summary  
  
Returns median of the array elements along the given axis.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- a: An array.
- axis: The axis along which the median is performed.

## mode_1d


```rust
mode_1d[dtype: DType](a: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Returns mode of all items of an array. Regardless of the shape of input, it is treated as a 1-d array.  
  
Parameters:  

- dtype: The element type.
  
Args:  

- a: An NDArray.

## mode


```rust
mode[dtype: DType](array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Mode of all items of an array.  
  
Parameters:  

- dtype: The element type.
  
Args:  

- array: An NDArray.


```rust
mode[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```  
Summary  
  
Returns mode of the array elements along the given axis.  
  
Parameters:  

- dtype: The element type.
  
Args:  

- a: An NDArray.
- axis: The axis along which the mode is performed.

## std


```rust
std[dtype: DType, //, returned_dtype: DType = float64](A: NDArray[dtype], ddof: Int = 0) -> SIMD[returned_dtype, 1]
```  
Summary  
  
Compute the standard deviation.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- A: An array.
- ddof: Delta degree of freedom. Default: 0


```rust
std[dtype: DType, //, returned_dtype: DType = float64](A: NDArray[dtype], axis: Int, ddof: Int = 0) -> NDArray[returned_dtype]
```  
Summary  
  
Computes the standard deviation along the axis.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- A: An array.
- axis: The axis along which the mean is performed.
- ddof: Delta degree of freedom. Default: 0


```rust
std[dtype: DType, //, returned_dtype: DType = float64](A: Matrix[dtype], ddof: Int = 0) -> SIMD[returned_dtype, 1]
```  
Summary  
  
Compute the standard deviation.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- A: Matrix.
- ddof: Delta degree of freedom. Default: 0


```rust
std[dtype: DType, //, returned_dtype: DType = float64](A: Matrix[dtype], axis: Int, ddof: Int = 0) -> Matrix[returned_dtype]
```  
Summary  
  
Compute the standard deviation along axis.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- A: Matrix.
- axis: 0 or 1.
- ddof: Delta degree of freedom. Default: 0

## variance


```rust
variance[dtype: DType, //, returned_dtype: DType = float64](A: NDArray[dtype], ddof: Int = 0) -> SIMD[returned_dtype, 1]
```  
Summary  
  
Compute the variance.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- A: An array.
- ddof: Delta degree of freedom. Default: 0


```rust
variance[dtype: DType, //, returned_dtype: DType = float64](A: NDArray[dtype], axis: Int, ddof: Int = 0) -> NDArray[returned_dtype]
```  
Summary  
  
Computes the variance along the axis.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- A: An array.
- axis: The axis along which the mean is performed.
- ddof: Delta degree of freedom. Default: 0


```rust
variance[dtype: DType, //, returned_dtype: DType = float64](A: Matrix[dtype], ddof: Int = 0) -> SIMD[returned_dtype, 1]
```  
Summary  
  
Compute the variance.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- A: Matrix.
- ddof: Delta degree of freedom. Default: 0


```rust
variance[dtype: DType, //, returned_dtype: DType = float64](A: Matrix[dtype], axis: Int, ddof: Int = 0) -> Matrix[returned_dtype]
```  
Summary  
  
Compute the variance along axis.  
  
Parameters:  

- dtype: The element type.
- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- A: Matrix.
- axis: 0 or 1.
- ddof: Delta degree of freedom. Default: 0
