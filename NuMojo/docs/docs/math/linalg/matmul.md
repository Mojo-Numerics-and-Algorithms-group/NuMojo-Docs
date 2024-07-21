



# matmul

##  Module Summary
  
Matrix multiplication functions for NDArrays
## tile


```rust
tile[tiled_fn: fn[Int, Int](Int, Int) capturing -> None, tile_x: Int, tile_y: Int](end_x: Int, end_y: Int)
```  
Summary  
  
  
  
Parameters:  

- tiled_fn
- tile_x
- tile_y
  
Args:  

- end_x
- end_y

## matmul_tiled_unrolled_parallelized


```rust
matmul_tiled_unrolled_parallelized[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- A
- B

## matmul_parallelized


```rust
matmul_parallelized[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Conduct `matmul` using `vectorize` and `parallelize`.  
  
Parameters:  

- dtype
  
Args:  

- A
- B

## matmul_naive


```rust
matmul_naive[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- A
- B
