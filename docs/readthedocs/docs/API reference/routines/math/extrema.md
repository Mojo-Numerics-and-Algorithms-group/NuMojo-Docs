



# extrema

##  Module Summary
  
Extrema finding
## extrema_1d


```rust
extrema_1d[dtype: DType, //, is_max: Bool](a: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Finds the max or min value in the buffer. Regardless of the shape of input, it is treated as a 1-d array. It is the backend function for `max` and `min`, with or without `axis`.  
  
Parameters:  

- dtype: The element type.
- is_max: If True, find max value, otherwise find min value.
  
Args:  

- a: An array.

## max


```rust
max[dtype: DType](a: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Finds the max value of an array. When no axis is given, the array is flattened before sorting.  
  
Parameters:  

- dtype: The element type.
  
Args:  

- a: An array.


```rust
max[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```  
Summary  
  
Finds the max value of an array along the axis. The number of dimension will be reduced by 1. When no axis is given, the array is flattened before sorting.  
  
Parameters:  

- dtype: The element type.
  
Args:  

- a: An array.
- axis: The axis along which the max is performed.


```rust
max[dtype: DType](A: Matrix[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Find max item. It is first flattened before sorting.  
  
Parameters:  

- dtype
  
Args:  

- A


```rust
max[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```  
Summary  
  
Find max item along the given axis.  
  
Parameters:  

- dtype
  
Args:  

- A
- axis

## min


```rust
min[dtype: DType](a: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Finds the min value of an array. When no axis is given, the array is flattened before sorting.  
  
Parameters:  

- dtype: The element type.
  
Args:  

- a: An array.


```rust
min[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```  
Summary  
  
Finds the min value of an array along the axis. The number of dimension will be reduced by 1. When no axis is given, the array is flattened before sorting.  
  
Parameters:  

- dtype: The element type.
  
Args:  

- a: An array.
- axis: The axis along which the max is performed.


```rust
min[dtype: DType](A: Matrix[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Find min item. It is first flattened before sorting.  
  
Parameters:  

- dtype
  
Args:  

- A


```rust
min[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```  
Summary  
  
Find min item along the given axis.  
  
Parameters:  

- dtype
  
Args:  

- A
- axis

## mimimum


```rust
mimimum[dtype: DType = float64](s1: SIMD[dtype, 1], s2: SIMD[dtype, 1]) -> SIMD[dtype, 1]
```  
Summary  
  
Minimum value of two SIMD values.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- s1: A SIMD Value.
- s2: A SIMD Value.

## maximum


```rust
maximum[dtype: DType = float64](s1: SIMD[dtype, 1], s2: SIMD[dtype, 1]) -> SIMD[dtype, 1]
```  
Summary  
  
Maximum value of two SIMD values.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- s1: A SIMD Value.
- s2: A SIMD Value.


```rust
maximum[dtype: DType = float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element wise maximum of two arrays.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array1: A array.
- array2: A array.

## minimum


```rust
minimum[dtype: DType = float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element wise minimum of two arrays.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array1: An array.
- array2: An array.
