



# datatypes

##  Module Summary
  
Datatypes Module - Implements datatypes aliases, conversions
## Aliases
  
`i8`: Data type alias for DType.int8  
`i16`: Data type alias for DType.int16  
`i32`: Data type alias for DType.int32  
`i64`: Data type alias for DType.int64  
`u8`: Data type alias for DType.uint8  
`u16`: Data type alias for DType.uint16  
`u32`: Data type alias for DType.uint32  
`u64`: Data type alias for DType.uint64  
`f16`: Data type alias for DType.float16  
`f32`: Data type alias for DType.float32  
`f64`: Data type alias for DType.float64
## cvtdtype


```rust
cvtdtype[in_dtype: DType, out_dtype: DType, width: Int = 1](value: SIMD[in_dtype, width]) -> SIMD[$1, $2]
```  
Summary  
  
Converts datatype of a value from in_dtype to out_dtype at run time.  
  
Parameters:  

- in_dtype: The input datatype.
- out_dtype: The output dataytpe.
- width: The width of the SIMD vector. Defualt: `1`
  
Args:  

- value: The SIMD value to be converted.


```rust
cvtdtype[in_dtype: DType, out_dtype: DType, width: Int = 1, value: SIMD[$0, $2] = __init__[stdlib::builtin::bool::Boolable](SIMD())]() -> SIMD[$1, $2]
```  
Summary  
  
Converts datatype of a value from in_dtype to out_dtype at compile time.  
  
Parameters:  

- in_dtype: The input datatype.
- out_dtype: The output dataytpe.
- width: The width of the SIMD vector. Defualt: `1`
- value: The SIMD value to be converted. Defualt: `__init__[stdlib::builtin::bool::Boolable](SIMD())`
