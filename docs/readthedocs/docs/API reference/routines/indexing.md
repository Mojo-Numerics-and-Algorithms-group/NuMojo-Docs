



# indexing

##  Module Summary
  
Implement indexing routines.
## where


```rust
where[dtype: DType](mut x: NDArray[dtype], scalar: SIMD[dtype, 1], mask: NDArray[bool])
```  
Summary  
  
Replaces elements in `x` with `scalar` where `mask` is True.  
  
Parameters:  

- dtype: DType.
  
Args:  

- x: A NDArray.
- scalar: A SIMD value.
- mask: A NDArray.


```rust
where[dtype: DType](mut x: NDArray[dtype], y: NDArray[dtype], mask: NDArray[bool])
```  
Summary  
  
Replaces elements in `x` with elements from `y` where `mask` is True.  
  
Parameters:  

- dtype: DType.
  
Args:  

- x: NDArray[dtype].
- y: NDArray[dtype].
- mask: NDArray[DType.bool].

## compress


```rust
compress[dtype: DType](condition: NDArray[bool], a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```  
Summary  
  
Return selected slices of an array along given axis. If no axis is provided, the array is flattened before use.  
  
Parameters:  

- dtype: DType.
  
Args:  

- condition: 1-D array of booleans that selects which entries to return. If length of condition is less than the size of the array along the given axis, then output is filled to the length of the condition with False.
- a: The array.
- axis: The axis along which to take slices.


```rust
compress[dtype: DType](condition: NDArray[bool], a: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Return selected slices of an array along given axis. If no axis is provided, the array is flattened before use. This is a function ***OVERLOAD***.  
  
Parameters:  

- dtype: DType.
  
Args:  

- condition: 1-D array of booleans that selects which entries to return. If length of condition is less than the size of the array along the given axis, then output is filled to the length of the condition with False.
- a: The array.
