



# cumulative_reduce

##  Module Summary
  
Cumulative reduction statistics functions for NDArrays
## cumsum


```rust
cumsum[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[$0, 1]
```  
Summary  
  
Sum of all items of an array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: An NDArray.

## cumprod


```rust
cumprod[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[$0, 1]
```  
Summary  
  
Product of all items in an array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: An NDArray.

## cummean


```rust
cummean[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[$0, 1]
```  
Summary  
  
Arithmatic mean of all items of an array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: An NDArray.

## mode


```rust
mode[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[$0, 1]
```  
Summary  
  
Mode of all items of an array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: An NDArray.

## median


```rust
median[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[$0, 1]
```  
Summary  
  
Median value of all items of an array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: An NDArray.

## maxT


```rust
maxT[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[$0, 1]
```  
Summary  
  
Maximum value of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A NDArray.

## minT


```rust
minT[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[$0, 1]
```  
Summary  
  
Minimum value of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A NDArray.

## cumpvariance


```rust
cumpvariance[dtype: DType = float64](array: NDArray[dtype], mu: Optional[SIMD[dtype, 1]] = #kgen.none) -> SIMD[$0, 1]
```  
Summary  
  
Population variance of a array.  
  
Parameters:  

- dtype: The element type.. Defualt: `float64`
  
Args:  

- array: A NDArray.
- mu: The mean of the array, if provided. Default: #kgen.none

## cumvariance


```rust
cumvariance[dtype: DType = float64](array: NDArray[dtype], mu: Optional[SIMD[dtype, 1]] = #kgen.none) -> SIMD[$0, 1]
```  
Summary  
  
Variance of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A NDArray.
- mu: The mean of the array, if provided. Default: #kgen.none

## cumpstdev


```rust
cumpstdev[dtype: DType = float64](array: NDArray[dtype], mu: Optional[SIMD[dtype, 1]] = #kgen.none) -> SIMD[$0, 1]
```  
Summary  
  
Population standard deviation of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A NDArray.
- mu: The mean of the array, if provided. Default: #kgen.none

## cumstdev


```rust
cumstdev[dtype: DType = float64](array: NDArray[dtype], mu: Optional[SIMD[dtype, 1]] = #kgen.none) -> SIMD[$0, 1]
```  
Summary  
  
Standard deviation of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A NDArray.
- mu: The mean of the array, if provided. Default: #kgen.none

## amin


```rust
amin[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[$0, 1]
```  
Summary  
  
Minimum value of an array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: An array.

## amax


```rust
amax[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[$0, 1]
```  
Summary  
  
Maximum value of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A array.

## mimimum


```rust
mimimum[dtype: DType = float64](s1: SIMD[dtype, 1], s2: SIMD[dtype, 1]) -> SIMD[$0, 1]
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
maximum[dtype: DType = float64](s1: SIMD[dtype, 1], s2: SIMD[dtype, 1]) -> SIMD[$0, 1]
```  
Summary  
  
Maximum value of two SIMD values.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- s1: A SIMD Value.
- s2: A SIMD Value.


```rust
maximum[dtype: DType = float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
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
minimum[dtype: DType = float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Element wise minimum of two arrays.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array1: An array.
- array2: An array.

## argmax


```rust
argmax[dtype: DType](array: NDArray[dtype]) -> Int
```  
Summary  
  
Argmax of a array.  
  
Parameters:  

- dtype: The element type.
  
Args:  

- array: A array.

## argmin


```rust
argmin[dtype: DType](array: NDArray[dtype]) -> Int
```  
Summary  
  
Argmin of a array. Parameters:     dtype: The element type.  
  
Parameters:  

- dtype
  
Args:  

- array: A array.
