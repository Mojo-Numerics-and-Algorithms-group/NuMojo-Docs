



# functional

##  Module Summary
  
Functional programming.
## apply_along_axis


```rust
apply_along_axis[dtype: DType, func1d: fn[DType](NDArray[$0]) raises -> SIMD[$0, 1]](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```  
Summary  
  
Applies a function to a NDArray by axis and reduce that dimension. When the array is 1-d, the returned array will be a 0-d array.  
  
Parameters:  

- dtype: The data type of the input NDArray elements.
- func1d: The function to apply to the NDArray.
  
Args:  

- a: The NDArray to apply the function to.
- axis: The axis to apply the function to.


```rust
apply_along_axis[dtype: DType, //, returned_dtype: DType, func1d: fn[DType, DType](NDArray[$0]) raises -> SIMD[$1, 1]](a: NDArray[dtype], axis: Int) -> NDArray[returned_dtype]
```  
Summary  
  
Applies a function to a NDArray by axis and reduce that dimension. When the array is 1-d, the returned array will be a 0-d array. The target data type of the returned NDArray is different from the input NDArray. This is a function ***overload***.  
  
Parameters:  

- dtype: The data type of the input NDArray elements.
- returned_dtype: The data type of the output NDArray elements.
- func1d: The function to apply to the NDArray.
  
Args:  

- a: The NDArray to apply the function to.
- axis: The axis to apply the function to.


```rust
apply_along_axis[dtype: DType, //, func1d: fn[DType](NDArray[$0]) raises -> NDArray[$0]](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```  
Summary  
  
Applies a function to a NDArray by axis without reducing that dimension. The resulting array will have the same shape as the input array.  
  
Parameters:  

- dtype: The data type of the input NDArray elements.
- func1d: The function to apply to the NDArray.
  
Args:  

- a: The NDArray to apply the function to.
- axis: The axis to apply the function to.


```rust
apply_along_axis[dtype: DType, func1d: fn[DType](NDArray[$0]) raises -> NDArray[index]](a: NDArray[dtype], axis: Int) -> NDArray[index]
```  
Summary  
  
Applies a function to a NDArray by axis without reducing that dimension. The resulting array will have the same shape as the input array. The resulting array is an index array. It can be used for, e.g., argsort.  
  
Parameters:  

- dtype: The data type of the input NDArray elements.
- func1d: The function to apply to the NDArray.
  
Args:  

- a: The NDArray to apply the function to.
- axis: The axis to apply the function to.
