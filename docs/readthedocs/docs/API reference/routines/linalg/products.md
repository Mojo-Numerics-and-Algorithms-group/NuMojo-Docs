



# products

##  Module Summary
  
Matrix and vector products
## cross


```rust
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

## dot


```rust
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

## tile


```rust
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


```rust
matmul_tiled_unrolled_parallelized[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Matrix multiplication vectorized, tiled, unrolled, and parallelized.  
  
Parameters:  

- dtype
  
Args:  

- A
- B

## matmul_1darray


```rust
matmul_1darray[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Array multiplication for 1-d arrays (inner dot).  
  
Parameters:  

- dtype
  
Args:  

- A
- B

## matmul_2darray


```rust
matmul_2darray[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Array multiplication for 2-d arrays (inner dot).  
  
Parameters:  

- dtype
  
Args:  

- A: First array.
- B: Second array.

## matmul


```rust
matmul[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Array multiplication for any dimensions.  
  
Parameters:  

- dtype
  
Args:  

- A: First array.
- B: Second array.


```rust
matmul[dtype: DType](A: Matrix[dtype], B: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
Matrix multiplication.  
  
Parameters:  

- dtype
  
Args:  

- A
- B

## matmul_naive


```rust
matmul_naive[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Matrix multiplication with three nested loops.  
  
Parameters:  

- dtype
  
Args:  

- A
- B
