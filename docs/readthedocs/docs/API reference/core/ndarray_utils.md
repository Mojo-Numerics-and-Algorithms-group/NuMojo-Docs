



# ndarray_utils

##  Module Summary
  
Implements N-DIMENSIONAL ARRAY UTILITY FUNCTIONS
## bool_to_numeric


```rust
bool_to_numeric[dtype: DType](array: NDArray[bool]) -> NDArray[$0]
```  
Summary  
  
Convert a boolean NDArray to a numeric NDArray.  
  
Parameters:  

- dtype: The data type of the output NDArray elements.
  
Args:  

- array: The boolean NDArray to convert.

## to_numpy


```rust
to_numpy[dtype: DType](array: NDArray[dtype]) -> PythonObject
```  
Summary  
  
Convert a NDArray to a numpy array.  
  
Parameters:  

- dtype: The data type of the NDArray elements.
  
Args:  

- array: The NDArray to convert.
