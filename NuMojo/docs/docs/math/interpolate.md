



# interpolate

##  Module Summary
  
# ===----------------------------------------------------------------------=== # # Interpolate Module - Implements interpolation functions # Last updated: 2024-06-14 # ===----------------------------------------------------------------------=== #
## interp1d


```rust
interp1d[dtype: DType = float64](xi: NDArray[dtype], x: NDArray[dtype], y: NDArray[dtype], type: String = "linear", fill_method: String = "interpolate") -> NDArray[$0]
```  
Summary  
  
Interpolate the values of y at the points xi.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- xi: An Array.
- x: An Array.
- y: An Array.
- type: The interpolation method. Default: "linear"
- fill_method: The fill value. Default: "interpolate"
