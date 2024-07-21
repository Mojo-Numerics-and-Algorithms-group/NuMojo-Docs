



# array_creation_routines

##  Module Summary
  
Array creation routine.
## arange


```rust
arange[in_dtype: DType, out_dtype: DType = float64](start: SIMD[in_dtype, 1], stop: SIMD[in_dtype, 1], step: SIMD[in_dtype, 1] = 1) -> NDArray[$1]
```  
Summary  
  
Function that computes a series of values starting from "start" to "stop" with given "step" size.  
  
Parameters:  

- in_dtype: Input datatype of the input values.
- out_dtype: Output datatype of the output NDArray.
  
Args:  

- start: Scalar[in_dtype] - Start value.
- stop: Scalar[in_dtype]  - End value.
- step: Scalar[in_dtype]  - Step size between each element (default 1).

## linspace


```rust
linspace[in_dtype: DType, out_dtype: DType = float64](start: SIMD[in_dtype, 1], stop: SIMD[in_dtype, 1], num: Int = 50, endpoint: Bool = 1, parallel: Bool = 0) -> NDArray[$1]
```  
Summary  
  
Function that computes a series of linearly spaced values starting from "start" to "stop" with given size. Wrapper function for _linspace_serial, _linspace_parallel.  
  
Parameters:  

- in_dtype: Datatype of the input values.
- out_dtype: Datatype of the output NDArray.
  
Args:  

- start: Start value.
- stop: End value.
- num: No of linearly spaced elements.
- endpoint: Specifies whether to include endpoint in the final NDArray, defaults to True.
- parallel: Specifies whether the linspace should be calculated using parallelization, deafults to False.

## logspace


```rust
logspace[in_dtype: DType, out_dtype: DType = float64](start: SIMD[in_dtype, 1], stop: SIMD[in_dtype, 1], num: Int, endpoint: Bool = 1, base: SIMD[in_dtype, 1] = #kgen.float_literal<10|1>, parallel: Bool = 0) -> NDArray[$1]
```  
Summary  
  
Generate a logrithmic spaced NDArray of `num` elements between `start` and `stop`. Wrapper function for _logspace_serial, _logspace_parallel functions.  
  
Parameters:  

- in_dtype: Datatype of the input values.
- out_dtype: Datatype of the output NDArray.
  
Args:  

- start: The starting value of the NDArray.
- stop: The ending value of the NDArray.
- num: The number of elements in the NDArray.
- endpoint: Whether to include the `stop` value in the NDArray. Defaults to True.
- base: Base value of the logarithm, defaults to 10.
- parallel: Specifies whether to calculate the logarithmic spaced values using parallelization.

## geomspace


```rust
geomspace[in_dtype: DType, out_dtype: DType = float64](start: SIMD[in_dtype, 1], stop: SIMD[in_dtype, 1], num: Int, endpoint: Bool = 1) -> NDArray[$1]
```  
Summary  
  
Generate a NDArray of `num` elements between `start` and `stop` in a geometric series.  
  
Parameters:  

- in_dtype: Datatype of the input values.
- out_dtype: Datatype of the output NDArray.
  
Args:  

- start: The starting value of the NDArray.
- stop: The ending value of the NDArray.
- num: The number of elements in the NDArray.
- endpoint: Whether to include the `stop` value in the NDArray. Defaults to True.

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
diagflat()
```  
Summary  
  
  

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
  
  
