



# integral

##  Module Summary
  

## trapz


```rust
trapz[in_dtype: DType, out_dtype: DType = float32](y: NDArray[in_dtype], x: NDArray[in_dtype]) -> SIMD[$1, 1]
```  
Summary  
  
Compute the integral of y over x using the trapezoidal rule.  
  
Parameters:  

- in_dtype: Input data type.
- out_dtype: Output data type, defaults to float32.
  
Args:  

- y: An array.
- x: An array.
