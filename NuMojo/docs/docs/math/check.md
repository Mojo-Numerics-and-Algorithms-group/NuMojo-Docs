



# check

##  Module Summary
  
Implements Checking routines: currently not SIMD due to bool bit packing issue
## isinf


```rust
isinf[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
Checks if each element of the input array is infinite.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## isfinite


```rust
isfinite[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
Checks if each element of the input array is finite.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## isnan


```rust
isnan[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
Checks if each element of the input array is NaN.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## any


```rust
any(array: NDArray[bool]) -> SIMD[bool, 1]
```  
Summary  
  
If any True.  
  
Args:  

- array

## allt


```rust
allt(array: NDArray[bool]) -> SIMD[bool, 1]
```  
Summary  
  
If all True.  
  
Args:  

- array
