



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

- in_dtype
- out_dtype
  
Args:  

- start
- stop
- step

## linspace


```rust
linspace[in_dtype: DType, out_dtype: DType = float64](start: SIMD[in_dtype, 1], stop: SIMD[in_dtype, 1], num: Int = 50, endpoint: Bool = 1, parallel: Bool = 0) -> NDArray[$1]
```  
Summary  
  
Function that computes a series of linearly spaced values starting from "start" to "stop" with given size. Wrapper function for _linspace_serial, _linspace_parallel.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- start
- stop
- num
- endpoint
- parallel

## logspace


```rust
logspace[in_dtype: DType, out_dtype: DType = float64](start: SIMD[in_dtype, 1], stop: SIMD[in_dtype, 1], num: Int, endpoint: Bool = 1, base: SIMD[in_dtype, 1] = #kgen.float_literal<10|1>, parallel: Bool = 0) -> NDArray[$1]
```  
Summary  
  
Generate a logrithmic spaced NDArray of `num` elements between `start` and `stop`. Wrapper function for _logspace_serial, _logspace_parallel functions.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- start
- stop
- num
- endpoint
- base
- parallel

## geomspace


```rust
geomspace[in_dtype: DType, out_dtype: DType = float64](start: SIMD[in_dtype, 1], stop: SIMD[in_dtype, 1], num: Int, endpoint: Bool = 1) -> NDArray[$1]
```  
Summary  
  
Generate a NDArray of `num` elements between `start` and `stop` in a geometric series.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- start
- stop
- num
- endpoint

## empty


```rust
empty[dtype: DType](*shape: Int) -> NDArray[$0]
```  
Summary  
  
Generate a NDArray of given shape with arbitrary values.  
  
Parameters:  

- dtype
  
Args:  

- \*shape: Shape of the NDArray.

## zeros


```rust
zeros[dtype: DType](*shape: Int) -> NDArray[$0]
```  
Summary  
  
Generate a NDArray of zeros with given shape.  
  
Parameters:  

- dtype
  
Args:  

- \*shape: Shape of the NDArray.

## eye


```rust
eye[dtype: DType](N: Int, M: Int) -> NDArray[$0]
```  
Summary  
  
Return a 2-D NDArray with ones on the diagonal and zeros elsewhere.  
  
Parameters:  

- dtype
  
Args:  

- N
- M

## identity


```rust
identity[dtype: DType](N: Int) -> NDArray[$0]
```  
Summary  
  
Generate an identity matrix of size N x N.  
  
Parameters:  

- dtype
  
Args:  

- N

## ones


```rust
ones[dtype: DType](*shape: Int) -> NDArray[$0]
```  
Summary  
  
Generate a NDArray of ones with given shape filled with ones.  
  
Parameters:  

- dtype
  
Args:  

- \*shape: Shape of the NDArray.

## full


```rust
full[dtype: DType](*shape: Int, *, fill_value: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Generate a NDArray of `fill_value` with given shape.  
  
Parameters:  

- dtype
  
Args:  

- \*shape: Shape of the NDArray.
- fill_value


```rust
full[dtype: DType](shape: VariadicList[Int], fill_value: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Generate a NDArray of `fill_value` with given shape.  
  
Parameters:  

- dtype
  
Args:  

- shape
- fill_value

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
  
  
