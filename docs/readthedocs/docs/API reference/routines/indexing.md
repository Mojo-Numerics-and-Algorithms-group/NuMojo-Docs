



# indexing

##  Module Summary
  
Indexing routines.
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
