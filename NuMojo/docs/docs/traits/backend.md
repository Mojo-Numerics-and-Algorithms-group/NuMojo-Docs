



# backend

##  Module Summary
  

## Backend

### Backend Summary
  
  
A trait that defines backends for calculations in the rest of the library.  

### Parent Traits:
  

- AnyType
  
Functions:
### __init__


```rust
__init__(inout self: T, /)
```  
Summary  
  
Initialize the backend.  
  
Args:  

- self

### math_func_fma


```rust
math_func_fma[dtype: DType](self: T, array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply a SIMD level fuse multipy add function of three variables and one return to a NDArray.  
  
Parameters:  

- dtype
  
Args:  

- self
- array1
- array2
- array3


```rust
math_func_fma[dtype: DType](self: T, array1: NDArray[dtype], array2: NDArray[dtype], simd: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Apply a SIMD level fuse multipy add function of three variables and one return to a NDArray.  
  
Parameters:  

- dtype
  
Args:  

- self
- array1
- array2
- simd

### math_func_1_array_in_one_array_out


```rust
math_func_1_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[$0, $1]](self: T, array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply a SIMD function of one variable and one return to a NDArray.  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array

### math_func_2_array_in_one_array_out


```rust
math_func_2_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: T, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply a SIMD function of two variable and one return to a NDArray.  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array1
- array2

### math_func_1_array_1_scalar_in_one_array_out


```rust
math_func_1_array_1_scalar_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: T, array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Apply a SIMD function of two variable and one return to a NDArray.  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array
- scalar

### math_func_compare_2_arrays


```rust
math_func_compare_2_arrays[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[bool, $1]](self: T, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array1
- array2

### math_func_is


```rust
math_func_is[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[bool, $1]](self: T, array: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array
