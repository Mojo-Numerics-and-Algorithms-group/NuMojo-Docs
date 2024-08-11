



# integral

##  Module Summary
  

## trapz


```rust
trapz[dtype: DType = float64](y: NDArray[dtype], x: NDArray[dtype]) -> SIMD[$0, 1]
```  
Summary  
  
Compute the integral of y over x using the trapezoidal rule.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Constraints:

`x` and `y` must have the same shape. `fdtype` must be a floating-point type if `idtype` is not a floating-point type.  
  
Args:  

- y: An array.
- x: An array.
