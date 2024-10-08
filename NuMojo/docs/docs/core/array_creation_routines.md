



# array_creation_routines

##  Module Summary
  
Array creation routine.
## arange


```rust
arange[dtype: DType = float64](start: SIMD[dtype, 1], stop: SIMD[dtype, 1], step: SIMD[dtype, 1] = 1) -> NDArray[$0]
```  
Summary  
  
Function that computes a series of values starting from "start" to "stop" with given "step" size.  
  
Parameters:  

- dtype: Datatype of the output array. Defualt: `float64`
  
Args:  

- start: Scalar[dtype] - Start value.
- stop: Scalar[dtype]  - End value.
- step: Scalar[dtype]  - Step size between each element (default 1). Default: 1

## linspace


```rust
linspace[dtype: DType](start: SIMD[dtype, 1], stop: SIMD[dtype, 1], num: Int = 50, endpoint: Bool = 1, parallel: Bool = 0) -> NDArray[$0]
```  
Summary  
  
Function that computes a series of linearly spaced values starting from "start" to "stop" with given size. Wrapper function for _linspace_serial, _linspace_parallel.  
  
Parameters:  

- dtype: Datatype of the output array.
  
Args:  

- start: Start value.
- stop: End value.
- num: No of linearly spaced elements. Default: 50
- endpoint: Specifies whether to include endpoint in the final NDArray, defaults to True. Default: 1
- parallel: Specifies whether the linspace should be calculated using parallelization, deafults to False. Default: 0

## logspace


```rust
logspace[dtype: DType](start: SIMD[dtype, 1], stop: SIMD[dtype, 1], num: Int, endpoint: Bool = 1, base: SIMD[dtype, 1] = #kgen.float_literal<10|1>, parallel: Bool = 0) -> NDArray[$0]
```  
Summary  
  
Generate a logrithmic spaced NDArray of `num` elements between `start` and `stop`. Wrapper function for _logspace_serial, _logspace_parallel functions.  
  
Parameters:  

- dtype: Datatype of the output array.
  
Args:  

- start: The starting value of the NDArray.
- stop: The ending value of the NDArray.
- num: The number of elements in the NDArray.
- endpoint: Whether to include the `stop` value in the NDArray. Defaults to True. Default: 1
- base: Base value of the logarithm, defaults to 10. Default: #kgen.float_literal<10|1>
- parallel: Specifies whether to calculate the logarithmic spaced values using parallelization. Default: 0

## geomspace


```rust
geomspace[dtype: DType](start: SIMD[dtype, 1], stop: SIMD[dtype, 1], num: Int, endpoint: Bool = 1) -> NDArray[$0]
```  
Summary  
  
Generate a NDArray of `num` elements between `start` and `stop` in a geometric series.  
  
Parameters:  

- dtype: Datatype of the input values.
  
Args:  

- start: The starting value of the NDArray.
- stop: The ending value of the NDArray.
- num: The number of elements in the NDArray.
- endpoint: Whether to include the `stop` value in the NDArray. Defaults to True. Default: 1

## empty


```rust
empty[dtype: DType](*shape: Int) -> NDArray[$0]
```  
Summary  
  
Generate a NDArray of given shape with arbitrary values.  
  
Parameters:  

- dtype: Datatype of the NDArray elements.
  
Args:  

- \*shape: Shape of the NDArray.

## zeros


```rust
zeros[dtype: DType](*shape: Int) -> NDArray[$0]
```  
Summary  
  
Generate a NDArray of zeros with given shape.  
  
Parameters:  

- dtype: Datatype of the NDArray elements.
  
Args:  

- \*shape: Shape of the NDArray.

## eye


```rust
eye[dtype: DType](N: Int, M: Int) -> NDArray[$0]
```  
Summary  
  
Return a 2-D NDArray with ones on the diagonal and zeros elsewhere.  
  
Parameters:  

- dtype: Datatype of the NDArray elements.
  
Args:  

- N: Number of rows in the matrix.
- M: Number of columns in the matrix.

## identity


```rust
identity[dtype: DType](N: Int) -> NDArray[$0]
```  
Summary  
  
Generate an identity matrix of size N x N.  
  
Parameters:  

- dtype: Datatype of the NDArray elements.
  
Args:  

- N: Size of the matrix.

## ones


```rust
ones[dtype: DType](*shape: Int) -> NDArray[$0]
```  
Summary  
  
Generate a NDArray of ones with given shape filled with ones.  
  
Parameters:  

- dtype: Datatype of the NDArray.
  
Args:  

- \*shape: Shape of the NDArray.

## full


```rust
full[dtype: DType](*shape: Int, *, fill_value: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Generate a NDArray of `fill_value` with given shape.  
  
Parameters:  

- dtype: Datatype of the NDArray elements.
  
Args:  

- \*shape: Shape of the NDArray.
- fill_value: Value to be splatted over the NDArray.


```rust
full[dtype: DType](shape: VariadicList[Int], fill_value: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Generate a NDArray of `fill_value` with given shape.  
  
Parameters:  

- dtype: Datatype of the NDArray elements.
  
Args:  

- shape: Shape of the NDArray.
- fill_value: Value to be splatted over the NDArray.

## diagflat


```rust
diagflat[dtype: DType](inout v: NDArray[dtype], k: Int = 0) -> NDArray[$0]
```  
Summary  
  
Generate a 2-D NDArray with the flattened input as the diagonal.  
  
Parameters:  

- dtype: Datatype of the NDArray elements.
  
Args:  

- v: NDArray to be flattened and used as the diagonal.
- k: Diagonal offset. Default: 0

## tri


```rust
tri()
```  
Summary  
  
  

## tril


```rust
tril()
```  
Summary  
  
  

## triu


```rust
triu()
```  
Summary  
  
  
