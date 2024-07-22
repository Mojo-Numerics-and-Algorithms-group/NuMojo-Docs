



# backend

##  Module Summary
  

## Backend

### Backend Summary
  
  
A trait that defines backends for calculations in the rest of the library.  

### Parent Traits
  

- AnyType
  

### Functions

#### __init__


```rust
__init__(inout self: T, /)
```  
Summary  
  
Initialize the backend.  
  
Args:  

- self

#### math_func_fma


```rust
math_func_fma[dtype: DType](self: T, array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply a SIMD level fuse multipy add function of three variables and one return to a NDArray.  
  
Parameters:  

- dtype: The element type.
  
Args:  

- self
- array1: A NDArray.
- array2: A NDArray.
- array3: A NDArray.


```rust
math_func_fma[dtype: DType](self: T, array1: NDArray[dtype], array2: NDArray[dtype], simd: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Apply a SIMD level fuse multipy add function of three variables and one return to a NDArray.  
  
Parameters:  

- dtype: The element type.
  
Args:  

- self
- array1: A NDArray.
- array2: A NDArray.
- simd: A SIMD[dtype,1] value to be added.

#### math_func_1_array_in_one_array_out


```rust
math_func_1_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[$0, $1]](self: T, array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply a SIMD function of one variable and one return to a NDArray.  
  
Parameters:  

- dtype: The element type.
- func: The SIMD function to to apply.
  
Args:  

- self
- array: A NDArray.

#### math_func_2_array_in_one_array_out


```rust
math_func_2_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: T, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply a SIMD function of two variable and one return to a NDArray.  
  
Parameters:  

- dtype: The element type.
- func: The SIMD function to to apply.
  
Args:  

- self
- array1: A NDArray.
- array2: A NDArray.

#### math_func_1_array_1_scalar_in_one_array_out


```rust
math_func_1_array_1_scalar_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: T, array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Apply a SIMD function of two variable and one return to a NDArray.  
  
Parameters:  

- dtype: The element type.
- func: The SIMD function to to apply.
  
Args:  

- self
- array: A NDArray.
- scalar: A Scalars.

#### math_func_compare_2_arrays


```rust
math_func_compare_2_arrays[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[bool, $1]](self: T, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
Apply a SIMD comparison functions to two NDArrays.  
  
Parameters:  

- dtype: The element type.
- func: The SIMD function to to apply.
  
Args:  

- self
- array1: A NDArray.
- array2: A NDArray.

#### math_func_is


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
