



# cumulative_reduce

##  Module Summary
  
Cumulative reduction statistics functions for NDArrays
## cumsum


```rust
cumsum[in_dtype: DType, out_dtype: DType = float64](array: NDArray[in_dtype]) -> SIMD[$1, 1]
```  
Summary  
  
Sum of all items of an array.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array

## cumprod


```rust
cumprod[in_dtype: DType, out_dtype: DType = float64](array: NDArray[in_dtype]) -> SIMD[$1, 1]
```  
Summary  
  
Product of all items in an array.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array

## cummean


```rust
cummean[in_dtype: DType, out_dtype: DType = float64](array: NDArray[in_dtype]) -> SIMD[$1, 1]
```  
Summary  
  
Arithmatic mean of all items of an array.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array

## mode


```rust
mode[in_dtype: DType, out_dtype: DType = float64](array: NDArray[in_dtype]) -> SIMD[$1, 1]
```  
Summary  
  
Mode of all items of an array.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array

## median


```rust
median[in_dtype: DType, out_dtype: DType = float64](array: NDArray[in_dtype]) -> SIMD[$1, 1]
```  
Summary  
  
Median value of all items of an array.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array

## maxT


```rust
maxT[in_dtype: DType, out_dtype: DType = float64](array: NDArray[in_dtype]) -> SIMD[$1, 1]
```  
Summary  
  
Maximum value of a array.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array

## minT


```rust
minT[in_dtype: DType, out_dtype: DType = float64](array: NDArray[in_dtype]) -> SIMD[$1, 1]
```  
Summary  
  
Minimum value of a array.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array

## cumpvariance


```rust
cumpvariance[in_dtype: DType, out_dtype: DType = float64](array: NDArray[in_dtype], mu: Optional[SIMD[in_dtype, 1]] = #kgen.none) -> SIMD[$1, 1]
```  
Summary  
  
Population variance of a array.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array
- mu

## cumvariance


```rust
cumvariance[in_dtype: DType, out_dtype: DType = float64](array: NDArray[in_dtype], mu: Optional[SIMD[in_dtype, 1]] = #kgen.none) -> SIMD[$1, 1]
```  
Summary  
  
Variance of a array.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array
- mu

## cumpstdev


```rust
cumpstdev[in_dtype: DType, out_dtype: DType = float64](array: NDArray[in_dtype], mu: Optional[SIMD[in_dtype, 1]] = #kgen.none) -> SIMD[$1, 1]
```  
Summary  
  
Population standard deviation of a array.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array
- mu

## cumstdev


```rust
cumstdev[in_dtype: DType, out_dtype: DType = float64](array: NDArray[in_dtype], mu: Optional[SIMD[in_dtype, 1]] = #kgen.none) -> SIMD[$1, 1]
```  
Summary  
  
Standard deviation of a array.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array
- mu

## amin


```rust
amin[in_dtype: DType, out_dtype: DType = float64](array: NDArray[in_dtype]) -> SIMD[$1, 1]
```  
Summary  
  
Minimum value of an array.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array

## amax


```rust
amax[in_dtype: DType, out_dtype: DType = float64](array: NDArray[in_dtype]) -> SIMD[$1, 1]
```  
Summary  
  
Maximum value of a array.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array

## mimimum


```rust
mimimum[in_dtype: DType, out_dtype: DType = float64](s1: SIMD[in_dtype, 1], s2: SIMD[in_dtype, 1]) -> SIMD[$1, 1]
```  
Summary  
  
Minimum value of two SIMD values.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- s1
- s2

## maximum


```rust
maximum[in_dtype: DType, out_dtype: DType = float64](s1: SIMD[in_dtype, 1], s2: SIMD[in_dtype, 1]) -> SIMD[$1, 1]
```  
Summary  
  
Maximum value of two SIMD values.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- s1
- s2


```rust
maximum[in_dtype: DType, out_dtype: DType = float64](array1: NDArray[in_dtype], array2: NDArray[in_dtype]) -> NDArray[$1]
```  
Summary  
  
Element wise maximum of two arrays.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array1
- array2

## minimum


```rust
minimum[in_dtype: DType, out_dtype: DType = float64](array1: NDArray[in_dtype], array2: NDArray[in_dtype]) -> NDArray[$1]
```  
Summary  
  
Element wise minimum of two arrays.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array1
- array2

## argmax


```rust
argmax[dtype: DType](array: NDArray[dtype]) -> Int
```  
Summary  
  
Argmax of a array.  
  
Parameters:  

- dtype
  
Args:  

- array

## argmin


```rust
argmin[dtype: DType](array: NDArray[dtype]) -> Int
```  
Summary  
  
Argmin of a array. Parameters:     dtype: The element type.  
  
Parameters:  

- dtype
  
Args:  

- array
