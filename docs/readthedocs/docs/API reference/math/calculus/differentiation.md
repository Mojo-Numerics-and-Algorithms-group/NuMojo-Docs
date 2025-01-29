



# differentiation

##  Module Summary
  

## gradient


```rust
gradient[dtype: DType](x: NDArray[dtype], spacing: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Compute the gradient of y over x using the trapezoidal rule.  
  
Parameters:  

- dtype: Input data type.
  
Constraints:

`fdtype` must be a floating-point type if `idtype` is not a floating-point type.  
  
Args:  

- x: An array.
- spacing: An array of the same shape as x containing the spacing between adjacent elements.
