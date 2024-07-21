



# comparison

##  Module Summary
  
Implements comparison math currently not using backend due to bool bitpacking issue
## greater


```rust
greater[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
Performs elementwise check of whether values in x are greater than values in y.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2

## greater_equal


```rust
greater_equal[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
Performs elementwise check of whether values in x are greater than or equal to values in y.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2

## less


```rust
less[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
Performs elementwise check of whether values in x are to values in y.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2

## less_equal


```rust
less_equal[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
Performs elementwise check of whether values in x are less than or equal to values in y.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2

## equal


```rust
equal[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
Performs elementwise check of whether values in x are equal to values in y.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2

## not_equal


```rust
not_equal[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
Performs elementwise check of whether values in x are not equal to values in y.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2
