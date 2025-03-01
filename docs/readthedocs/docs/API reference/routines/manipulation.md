



# manipulation

##  Module Summary
  
Array manipulation routines.
## copyto


```rust
copyto()
```  
Summary  
  
  

## ndim


```rust
ndim[dtype: DType](array: NDArray[dtype]) -> Int
```  
Summary  
  
Returns the number of dimensions of the NDArray.  
  
Parameters:  

- dtype
  
Args:  

- array: A NDArray.

## shape


```rust
shape[dtype: DType](array: NDArray[dtype]) -> NDArrayShape
```  
Summary  
  
Returns the shape of the NDArray.  
  
Parameters:  

- dtype
  
Args:  

- array: A NDArray.

## size


```rust
size[dtype: DType](array: NDArray[dtype], axis: Int) -> Int
```  
Summary  
  
Returns the size of the NDArray.  
  
Parameters:  

- dtype
  
Args:  

- array: A NDArray.
- axis: The axis to get the size of.

## reshape


```rust
reshape[dtype: DType](owned A: NDArray[dtype], shape: NDArrayShape, order: String = String("C")) -> NDArray[dtype]
```  
Summary  
  
    Returns an array of the same data with a new shape.  
  
Parameters:  

- dtype
  
Args:  

- A: A NDArray.
- shape: New shape.
- order: "C" or "F". Read in this order from the original array and write in this order into the new array. Default: String("C")

## ravel


```rust
ravel[dtype: DType](a: NDArray[dtype], order: String = String("C")) -> NDArray[dtype]
```  
Summary  
  
Returns the raveled version of the NDArray.  
  
Parameters:  

- dtype
  
Args:  

- a: NDArray.
- order: The order to flatten the array. Default: String("C")

## transpose


```rust
transpose[dtype: DType](A: NDArray[dtype], axes: List[Int]) -> NDArray[dtype]
```  
Summary  
  
Transpose array of any number of dimensions according to arbitrary permutation of the axes.  
  
Parameters:  

- dtype
  
Args:  

- A
- axes


```rust
transpose[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
(overload) Transpose the array when `axes` is not given. If `axes` is not given, it is equal to flipping the axes. See docstring of `transpose`.  
  
Parameters:  

- dtype
  
Args:  

- A


```rust
transpose[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
Transpose of matrix.  
  
Parameters:  

- dtype
  
Args:  

- A

## broadcast_to


```rust
broadcast_to[dtype: DType](a: NDArray[dtype], shape: NDArrayShape) -> NDArray[dtype]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- a
- shape


```rust
broadcast_to[dtype: DType](A: Matrix[dtype], shape: Tuple[Int, Int]) -> Matrix[dtype]
```  
Summary  
  
Broadcasts the vector to the given shape.  
  
Parameters:  

- dtype
  
Args:  

- A
- shape


```rust
broadcast_to[dtype: DType](A: SIMD[dtype, 1], shape: Tuple[Int, Int]) -> Matrix[dtype]
```  
Summary  
  
Broadcasts the scalar to the given shape.  
  
Parameters:  

- dtype
  
Args:  

- A
- shape

## flip


```rust
flip[dtype: DType](owned A: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Returns flipped array and keep the shape.  
  
Parameters:  

- dtype: DType.
  
Args:  

- A: A NDArray.


```rust
flip[dtype: DType](owned A: NDArray[dtype], owned axis: Int) -> NDArray[dtype]
```  
Summary  
  
Returns flipped array along the given axis.  
  
Parameters:  

- dtype: DType.
  
Args:  

- A: A NDArray.
- axis: Axis along which to flip.
