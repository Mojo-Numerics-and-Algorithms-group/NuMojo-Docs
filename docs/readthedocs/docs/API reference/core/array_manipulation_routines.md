



# array_manipulation_routines

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
shape[dtype: DType](array: NDArray[dtype]) -> NDArrayShape[int32]
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
reshape[dtype: DType](inout array: NDArray[dtype], shape: VariadicList[Int], order: String = "C")
```  
Summary  
  
    Reshapes the NDArray to given Shape.  
  
Parameters:  

- dtype
  
Args:  

- array: A NDArray.
- shape: Variadic integers of shape.
- order: Order of the array - Row major `C` or Column major `F`. Default: "C"

## ravel


```rust
ravel[dtype: DType](inout array: NDArray[dtype], order: String = "C")
```  
Summary  
  
Returns the raveled version of the NDArray.  
  
Parameters:  

- dtype
  
Args:  

- array
- order Default: "C"

## where


```rust
where[dtype: DType](inout x: NDArray[dtype], scalar: SIMD[dtype, 1], mask: NDArray[bool])
```  
Summary  
  
Replaces elements in `x` with `scalar` where `mask` is True.  
  
Parameters:  

- dtype: DType.
  
Args:  

- x: A NDArray.
- scalar: A SIMD value.
- mask: A NDArray.


```rust
where[dtype: DType](inout x: NDArray[dtype], y: NDArray[dtype], mask: NDArray[bool])
```  
Summary  
  
Replaces elements in `x` with elements from `y` where `mask` is True.  
  
Parameters:  

- dtype: DType.
  
Args:  

- x: NDArray[dtype].
- y: NDArray[dtype].
- mask: NDArray[DType.bool].

## flip


```rust
flip[dtype: DType](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Flips the NDArray along the given axis.  
  
Parameters:  

- dtype: DType.
  
Args:  

- array: A NDArray.
