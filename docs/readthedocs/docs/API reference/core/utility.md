



# utility

##  Module Summary
  
Implements N-DIMENSIONAL ARRAY UTILITY FUNCTIONS
## bool_to_numeric


```rust
bool_to_numeric[dtype: DType](array: NDArray[bool]) -> NDArray[dtype]
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

## to_tensor


```rust
to_tensor[dtype: DType](a: NDArray[dtype]) -> Tensor[dtype]
```  
Summary  
  
Convert to a tensor.  
  
Parameters:  

- dtype
  
Args:  

- a

## is_inttype


```rust
is_inttype[dtype: DType]() -> Bool
```  
Summary  
  
Check if the given dtype is an integer type at compile time.  
  
Parameters:  

- dtype: DType.


```rust
is_inttype(dtype: DType) -> Bool
```  
Summary  
  
Check if the given dtype is an integer type at run time.  
  
Args:  

- dtype: DType.

## is_floattype


```rust
is_floattype[dtype: DType]() -> Bool
```  
Summary  
  
Check if the given dtype is a floating point type at compile time.  
  
Parameters:  

- dtype: DType.


```rust
is_floattype(dtype: DType) -> Bool
```  
Summary  
  
Check if the given dtype is a floating point type at run time.  
  
Args:  

- dtype: DType.

## is_booltype


```rust
is_booltype[dtype: DType]() -> Bool
```  
Summary  
  
Check if the given dtype is a boolean type at compile time.  
  
Parameters:  

- dtype: DType.


```rust
is_booltype(dtype: DType) -> Bool
```  
Summary  
  
Check if the given dtype is a boolean type at run time.  
  
Args:  

- dtype: DType.
