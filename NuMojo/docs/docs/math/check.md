



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

- dtype: DType - Data type of the input array.
- backend: _mf.Backend - Backend to use for the operation. Defaults to _mf.Vectorized.
  
Args:  

- array: NDArray[dtype] - Input array to check.

## isfinite


```rust
isfinite[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
Checks if each element of the input array is finite.  
  
Parameters:  

- dtype: DType - Data type of the input array.
- backend: _mf.Backend - Backend to use for the operation. Defaults to _mf.Vectorized.
  
Args:  

- array: NDArray[dtype] - Input array to check.

## isnan


```rust
isnan[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
Checks if each element of the input array is NaN.  
  
Parameters:  

- dtype: DType - Data type of the input array.
- backend: _mf.Backend - Backend to use for the operation. Defaults to _mf.Vectorized.
  
Args:  

- array: NDArray[dtype] - Input array to check.

## any


```rust
any(array: NDArray[bool]) -> SIMD[bool, 1]
```  
Summary  
  
If any True.  
  
Args:  

- array: A NDArray.

## allt


```rust
allt(array: NDArray[bool]) -> SIMD[bool, 1]
```  
Summary  
  
If all True.  
  
Args:  

- array: A NDArray.
