



# math_funcs

##  Module Summary
  
Implements backend functions for mathematics
## Vectorized

### Vectorized Summary
  
  
Vectorized Backend Struct. Parameters     unroll_factor: factor by which loops are unrolled.  

### Parent Traits:
  

- AnyType
- Backend
  
Functions:
### __init__


```rust
__init__(inout self: Self)
```  
Summary  
  
  
  
Args:  

- self

### math_func_fma


```rust
math_func_fma[dtype: DType](self: Self, array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[$0]
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
math_func_fma[dtype: DType](self: Self, array1: NDArray[dtype], array2: NDArray[dtype], simd: SIMD[dtype, 1]) -> NDArray[$0]
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
math_func_1_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype]) -> NDArray[$0]
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
math_func_2_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
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
math_func_1_array_1_scalar_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
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
math_func_compare_2_arrays[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[bool, $1]](self: Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
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
math_func_is[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[bool, $1]](self: Self, array: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array

### math_func_simd_int


```rust
math_func_simd_int[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], Int) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype], intval: Int) -> NDArray[$0]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array
- intval

## VectorizedUnroll

### VectorizedUnroll Summary
  
  
Vectorized Backend Struct. Parameters     unroll_factor: factor by which loops are unrolled.  

### Parent Traits:
  

- AnyType
- Backend
  
Functions:
### __init__


```rust
__init__(inout self: Self)
```  
Summary  
  
  
  
Args:  

- self

### math_func_fma


```rust
math_func_fma[dtype: DType](self: Self, array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[$0]
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
math_func_fma[dtype: DType](self: Self, array1: NDArray[dtype], array2: NDArray[dtype], simd: SIMD[dtype, 1]) -> NDArray[$0]
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
math_func_1_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype]) -> NDArray[$0]
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
math_func_2_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
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
math_func_1_array_1_scalar_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
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
math_func_compare_2_arrays[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[bool, $1]](self: Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
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
math_func_is[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[bool, $1]](self: Self, array: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array

### math_func_simd_int


```rust
math_func_simd_int[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], Int) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype], intval: Int) -> NDArray[$0]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array
- intval

## Parallelized

### Parallelized Summary
  
  
Parrallelized Backend Struct.  

### Parent Traits:
  

- AnyType
- Backend
  
Functions:
### __init__


```rust
__init__(inout self: Self)
```  
Summary  
  
  
  
Args:  

- self

### math_func_fma


```rust
math_func_fma[dtype: DType](self: Self, array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[$0]
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
math_func_fma[dtype: DType](self: Self, array1: NDArray[dtype], array2: NDArray[dtype], simd: SIMD[dtype, 1]) -> NDArray[$0]
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
math_func_1_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype]) -> NDArray[$0]
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
math_func_2_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
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
math_func_1_array_1_scalar_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
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
math_func_compare_2_arrays[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[bool, $1]](self: Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
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
math_func_is[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[bool, $1]](self: Self, array: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array

### math_func_simd_int


```rust
math_func_simd_int[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], Int) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype], intval: Int) -> NDArray[$0]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array
- intval

## VectorizedParallelized

### VectorizedParallelized Summary
  
  
Vectorized and Parrallelized Backend Struct.  

### Parent Traits:
  

- AnyType
- Backend
  
Functions:
### __init__


```rust
__init__(inout self: Self)
```  
Summary  
  
  
  
Args:  

- self

### math_func_fma


```rust
math_func_fma[dtype: DType](self: Self, array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[$0]
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
math_func_fma[dtype: DType](self: Self, array1: NDArray[dtype], array2: NDArray[dtype], simd: SIMD[dtype, 1]) -> NDArray[$0]
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
math_func_1_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype]) -> NDArray[$0]
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
math_func_2_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
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
math_func_1_array_1_scalar_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
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
math_func_compare_2_arrays[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[bool, $1]](self: Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
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
math_func_is[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[bool, $1]](self: Self, array: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array

### math_func_simd_int


```rust
math_func_simd_int[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], Int) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype], intval: Int) -> NDArray[$0]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array
- intval

## VectorizedParallelizedNWorkers

### VectorizedParallelizedNWorkers Summary
  
  
Vectorized and Parrallelized Backend Struct with manual setting of number of workers.  

### Parent Traits:
  

- AnyType
- Backend
  
Functions:
### __init__


```rust
__init__(inout self: Self)
```  
Summary  
  
  
  
Args:  

- self

### math_func_fma


```rust
math_func_fma[dtype: DType](self: Self, array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[$0]
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
math_func_fma[dtype: DType](self: Self, array1: NDArray[dtype], array2: NDArray[dtype], simd: SIMD[dtype, 1]) -> NDArray[$0]
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
math_func_1_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype]) -> NDArray[$0]
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
math_func_2_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
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
math_func_1_array_1_scalar_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
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
math_func_compare_2_arrays[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[bool, $1]](self: Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
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
math_func_is[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[bool, $1]](self: Self, array: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array

### math_func_simd_int


```rust
math_func_simd_int[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], Int) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype], intval: Int) -> NDArray[$0]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array
- intval

## Naive

### Naive Summary
  
  
Naive Backend Struct.  

### Parent Traits:
  

- AnyType
- Backend
  
Functions:
### __init__


```rust
__init__(inout self: Self)
```  
Summary  
  
  
  
Args:  

- self

### math_func_fma


```rust
math_func_fma[dtype: DType](self: Self, array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[$0]
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
math_func_fma[dtype: DType](self: Self, array1: NDArray[dtype], array2: NDArray[dtype], simd: SIMD[dtype, 1]) -> NDArray[$0]
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
math_func_1_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype]) -> NDArray[$0]
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
math_func_2_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
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
math_func_1_array_1_scalar_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
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
math_func_compare_2_arrays[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[bool, $1]](self: Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
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
math_func_is[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[bool, $1]](self: Self, array: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array

### math_func_simd_int


```rust
math_func_simd_int[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], Int) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype], intval: Int) -> NDArray[$0]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array
- intval

## VectorizedVerbose

### VectorizedVerbose Summary
  
  
Vectorized Backend Struct.  

### Parent Traits:
  

- AnyType
- Backend
  
Functions:
### __init__


```rust
__init__(inout self: Self)
```  
Summary  
  
  
  
Args:  

- self

### math_func_fma


```rust
math_func_fma[dtype: DType](self: Self, array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[$0]
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
math_func_fma[dtype: DType](self: Self, array1: NDArray[dtype], array2: NDArray[dtype], simd: SIMD[dtype, 1]) -> NDArray[$0]
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
math_func_1_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype]) -> NDArray[$0]
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
math_func_2_array_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
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
math_func_1_array_1_scalar_in_one_array_out[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[$0, $1]](self: Self, array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
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
math_func_compare_2_arrays[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], SIMD[$0, $1]) -> SIMD[bool, $1]](self: Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[bool]
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
math_func_is[dtype: DType, func: fn[DType, Int](SIMD[$0, $1]) -> SIMD[bool, $1]](self: Self, array: NDArray[dtype]) -> NDArray[bool]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array

### math_func_simd_int


```rust
math_func_simd_int[dtype: DType, func: fn[DType, Int](SIMD[$0, $1], Int) -> SIMD[$0, $1]](self: Self, array1: NDArray[dtype], intval: Int) -> NDArray[$0]
```  
Summary  
  
  
  
Parameters:  

- dtype
- func
  
Args:  

- self
- array1
- intval

## bool_simd_store


```rust
bool_simd_store[width: Int](ptr: DTypePointer[bool, 0], start: Int, val: SIMD[bool, width])
```  
Summary  
  
  
  
Parameters:  

- width
  
Args:  

- ptr
- start
- val
