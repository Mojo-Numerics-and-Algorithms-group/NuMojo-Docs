



# extrema

##  Module Summary
  
TODO:  1) Add support for axis parameter.   2) Currently, constrained is crashing mojo, so commented it out and added raise Error. Check later. 3) Relax constrained[] to let user get whatever output they want, but make a warning instead.
## max


```rust
max[dtype: DType](array: NDArray[dtype], axis: Int = 0) -> NDArray[dtype]
```  
Summary  
  
Maximums of array elements over a given axis.  
  
Parameters:  

- dtype
  
Args:  

- array: NDArray.
- axis: The axis along which the sum is performed. Default: 0


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

## maxT


```rust
maxT[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Maximum value of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A NDArray.

## min


```rust
min[dtype: DType](array: NDArray[dtype], axis: Int = 0) -> NDArray[dtype]
```  
Summary  
  
Minumums of array elements over a given axis.  
  
Parameters:  

- dtype
  
Args:  

- array: NDArray.
- axis: The axis along which the sum is performed. Default: 0


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

## minT


```rust
minT[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Minimum value of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A NDArray.

## amin


```rust
amin[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Minimum value of an array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: An array.

## amax


```rust
amax[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Maximum value of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A array.

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
