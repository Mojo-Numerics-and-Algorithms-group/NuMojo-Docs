



# differentiation

##  Module Summary
  

## gradient


```rust
gradient[in_dtype: DType, out_dtype: DType = float32](x: NDArray[in_dtype], spacing: SIMD[in_dtype, 1]) -> NDArray[$1]
```  
Summary  
  
Compute the integral of y over x using the trapezoidal rule.  
  
Parameters:  

- in_dtype: Input data type.
- out_dtype: Output data type, defaults to float32.
  
Args:  

- x: An array.
- spacing: An array of the same shape as x containing the spacing between adjacent elements.
