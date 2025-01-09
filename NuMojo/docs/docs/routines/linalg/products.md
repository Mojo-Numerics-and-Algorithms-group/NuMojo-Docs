



# products

##  Module Summary
  
Matrix and vector products
## cross


```Mojo
cross[dtype: DType = float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Compute the cross product of two arrays.  
  
Parameters:  

- dtype Defualt: `float64`
  
Constraints:

`array1` and `array2` must be of shape (3,).  
  
Args:  

- array1: A array.
- array2: A array.


Parameters
    dtype: The element type.

## dot


```Mojo
dot[dtype: DType = float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Compute the dot product of two arrays.  
  
Parameters:  

- dtype Defualt: `float64`
  
Constraints:

`array1` and `array2` must be 1 dimensional.  
  
Args:  

- array1: A array.
- array2: A array.


Parameters
    dtype: The element type.

## tile


```Mojo
tile[: origin.set, //, tiled_fn: fn[Int, Int](Int, Int) capturing -> None, tile_x: Int, tile_y: Int](end_x: Int, end_y: Int)
```  
Summary  
  
  
  
Parameters:  

- 
- tiled_fn
- tile_x
- tile_y
  
Args:  

- end_x
- end_y

## matmul_tiled_unrolled_parallelized


```Mojo
matmul_tiled_unrolled_parallelized[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Matrix multiplication vectorized, tiled, unrolled, and parallelized.  
  
Parameters:  

- dtype
  
Args:  

- A
- B

## matmul_1d


```Mojo
matmul_1d[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Array multiplication for 1-d arrays (inner dot).  
  
Parameters:  

- dtype
  
Args:  

- A
- B

## matmul_parallelized


```Mojo
matmul_parallelized[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Matrix multiplication Vectorized and parallelized.  
  
Parameters:  

- dtype
  
Args:  

- A
- B


Conduct `matmul` using `vectorize` and `parallelize`.

Reference: https://docs.modular.com/mojo/notebooks/Matmul
Compared to the reference, this function increases the size of
the SIMD vector from the default width to 16. The purpose is to
increase the performance via SIMD.
The function reduces the execution time by ~50 percent compared to
matmul_parallelized and matmul_tiled_unrolled_parallelized for large
matrices.
## matmul_naive


```Mojo
matmul_naive[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Matrix multiplication with three nested loops.  
  
Parameters:  

- dtype
  
Args:  

- A
- B
