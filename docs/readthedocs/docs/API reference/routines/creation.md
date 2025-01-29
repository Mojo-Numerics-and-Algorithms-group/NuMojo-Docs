



# creation

##  Module Summary
  
Array creation routine.
## arange


```rust
arange[dtype: DType = float64](start: SIMD[dtype, 1], stop: SIMD[dtype, 1], step: SIMD[dtype, 1] = SIMD(1)) -> NDArray[dtype]
```  
Summary  
  
Function that computes a series of values starting from "start" to "stop" with given "step" size.  
  
Parameters:  

- dtype: Datatype of the output array. Defualt: `float64`
  
Args:  

- start: Scalar[dtype] - Start value.
- stop: Scalar[dtype]  - End value.
- step: Scalar[dtype]  - Step size between each element (default 1). Default: SIMD(1)


```rust
arange[dtype: DType = float64](stop: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
(Overload) When start is 0 and step is 1.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- stop


```rust
arange[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](start: ComplexSIMD[cdtype, dtype=dtype], stop: ComplexSIMD[cdtype, dtype=dtype], step: ComplexSIMD[cdtype, dtype=dtype] = ComplexSIMD(SIMD(1), SIMD(1))) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Function that computes a series of values starting from "start" to "stop" with given "step" size.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- start: ComplexSIMD[cdtype] - Start value.
- stop: ComplexSIMD[cdtype]  - End value.
- step: ComplexSIMD[cdtype]  - Step size between each element (default 1). Default: ComplexSIMD(SIMD(1), SIMD(1))


```rust
arange[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](stop: ComplexSIMD[cdtype, dtype=dtype]) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
(Overload) When start is 0 and step is 1.  
  
Parameters:  

- cdtype Defualt: `{float64, float64}`
- dtype Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- stop

## linspace


```rust
linspace[dtype: DType = float64](start: SIMD[dtype, 1], stop: SIMD[dtype, 1], num: Int = 50, endpoint: Bool = True, parallel: Bool = False) -> NDArray[dtype]
```  
Summary  
  
Function that computes a series of linearly spaced values starting from "start" to "stop" with given size. Wrapper function for _linspace_serial, _linspace_parallel.  
  
Parameters:  

- dtype: Datatype of the output array. Defualt: `float64`
  
Args:  

- start: Start value.
- stop: End value.
- num: No of linearly spaced elements. Default: 50
- endpoint: Specifies whether to include endpoint in the final NDArray, defaults to True. Default: True
- parallel: Specifies whether the linspace should be calculated using parallelization, deafults to False. Default: False


```rust
linspace[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](start: ComplexSIMD[cdtype, dtype=dtype], stop: ComplexSIMD[cdtype, dtype=dtype], num: Int = 50, endpoint: Bool = True, parallel: Bool = False) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Function that computes a series of linearly spaced values starting from "start" to "stop" with given size. Wrapper function for _linspace_serial, _linspace_parallel.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- start: Start value.
- stop: End value.
- num: No of linearly spaced elements. Default: 50
- endpoint: Specifies whether to include endpoint in the final ComplexNDArray, defaults to True. Default: True
- parallel: Specifies whether the linspace should be calculated using parallelization, deafults to False. Default: False

## logspace


```rust
logspace[dtype: DType = float64](start: SIMD[dtype, 1], stop: SIMD[dtype, 1], num: Int, endpoint: Bool = True, base: SIMD[dtype, 1] = SIMD(#kgen.float_literal<10|1>), parallel: Bool = False) -> NDArray[dtype]
```  
Summary  
  
Generate a logrithmic spaced NDArray of `num` elements between `start` and `stop`. Wrapper function for _logspace_serial, _logspace_parallel functions.  
  
Parameters:  

- dtype: Datatype of the output array. Defualt: `float64`
  
Args:  

- start: The starting value of the NDArray.
- stop: The ending value of the NDArray.
- num: The number of elements in the NDArray.
- endpoint: Whether to include the `stop` value in the NDArray. Defaults to True. Default: True
- base: Base value of the logarithm, defaults to 10. Default: SIMD(#kgen.float_literal<10|1>)
- parallel: Specifies whether to calculate the logarithmic spaced values using parallelization. Default: False


```rust
logspace[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](start: ComplexSIMD[cdtype, dtype=dtype], stop: ComplexSIMD[cdtype, dtype=dtype], num: Int, endpoint: Bool = True, base: ComplexSIMD[cdtype, dtype=dtype] = ComplexSIMD(SIMD(#kgen.float_literal<10|1>), SIMD(#kgen.float_literal<10|1>)), parallel: Bool = False) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Generate a logrithmic spaced ComplexNDArray of `num` elements between `start` and `stop`. Wrapper function for _logspace_serial, _logspace_parallel functions.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- start: The starting value of the ComplexNDArray.
- stop: The ending value of the ComplexNDArray.
- num: The number of elements in the ComplexNDArray.
- endpoint: Whether to include the `stop` value in the ComplexNDArray. Defaults to True. Default: True
- base: Base value of the logarithm, defaults to 10. Default: ComplexSIMD(SIMD(#kgen.float_literal<10|1>), SIMD(#kgen.float_literal<10|1>))
- parallel: Specifies whether to calculate the logarithmic spaced values using parallelization. Default: False

## geomspace


```rust
geomspace[dtype: DType = float64](start: SIMD[dtype, 1], stop: SIMD[dtype, 1], num: Int, endpoint: Bool = True) -> NDArray[dtype]
```  
Summary  
  
Generate a NDArray of `num` elements between `start` and `stop` in a geometric series.  
  
Parameters:  

- dtype: Datatype of the input values. Defualt: `float64`
  
Args:  

- start: The starting value of the NDArray.
- stop: The ending value of the NDArray.
- num: The number of elements in the NDArray.
- endpoint: Whether to include the `stop` value in the NDArray. Defaults to True. Default: True


```rust
geomspace[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](start: ComplexSIMD[cdtype, dtype=dtype], stop: ComplexSIMD[cdtype, dtype=dtype], num: Int, endpoint: Bool = True) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Generate a ComplexNDArray of `num` elements between `start` and `stop` in a geometric series.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- start: The starting value of the ComplexNDArray.
- stop: The ending value of the ComplexNDArray.
- num: The number of elements in the ComplexNDArray.
- endpoint: Whether to include the `stop` value in the ComplexNDArray. Defaults to True. Default: True

## empty


```rust
empty[dtype: DType = float64](shape: NDArrayShape) -> NDArray[dtype]
```  
Summary  
  
Generate an empty NDArray of given shape with arbitrary values.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- shape: Shape of the NDArray.


```rust
empty[dtype: DType = float64](shape: List[Int]) -> NDArray[dtype]
```  
Summary  
  
Overload of function `empty` that reads a list of ints.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape


```rust
empty[dtype: DType = float64](shape: VariadicList[Int]) -> NDArray[dtype]
```  
Summary  
  
Overload of function `empty` that reads a variadic list of ints.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape


```rust
empty[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](shape: NDArrayShape) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Generate an empty ComplexNDArray of given shape with arbitrary values.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- shape: Shape of the ComplexNDArray.


```rust
empty[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](shape: List[Int]) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Overload of function `empty` that reads a list of ints.  
  
Parameters:  

- cdtype Defualt: `{float64, float64}`
- dtype Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- shape


```rust
empty[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](shape: VariadicList[Int]) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Overload of function `empty` that reads a variadic list of ints.  
  
Parameters:  

- cdtype Defualt: `{float64, float64}`
- dtype Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- shape

## empty_like


```rust
empty_like[dtype: DType = float64](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Generate an empty NDArray of the same shape as `array`.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- array: NDArray to be used as a reference for the shape.


```rust
empty_like[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](array: ComplexNDArray[cdtype, dtype=dtype]) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Generate an empty ComplexNDArray of the same shape as `array`.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- array: ComplexNDArray to be used as a reference for the shape.

## eye


```rust
eye[dtype: DType = float64](N: Int, M: Int) -> NDArray[dtype]
```  
Summary  
  
Return a 2-D NDArray with ones on the diagonal and zeros elsewhere.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- N: Number of rows in the matrix.
- M: Number of columns in the matrix.


```rust
eye[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](N: Int, M: Int) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Return a 2-D ComplexNDArray with ones on the diagonal and zeros elsewhere.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- N: Number of rows in the matrix.
- M: Number of columns in the matrix.

## identity


```rust
identity[dtype: DType = float64](N: Int) -> NDArray[dtype]
```  
Summary  
  
Generate an identity matrix of size N x N.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- N: Size of the matrix.


```rust
identity[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](N: Int) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Generate an Complex identity matrix of size N x N.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- N: Size of the matrix.

## ones


```rust
ones[dtype: DType = float64](shape: NDArrayShape) -> NDArray[dtype]
```  
Summary  
  
Generate a NDArray of ones with given shape filled with ones.  
  
Parameters:  

- dtype: Datatype of the NDArray. Defualt: `float64`
  
Args:  

- shape: Shape of the NDArray.


```rust
ones[dtype: DType = float64](shape: List[Int]) -> NDArray[dtype]
```  
Summary  
  
Overload of function `ones` that reads a list of ints.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape


```rust
ones[dtype: DType = float64](shape: VariadicList[Int]) -> NDArray[dtype]
```  
Summary  
  
Overload of function `ones` that reads a variadic of ints.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape


```rust
ones[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](shape: NDArrayShape) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Generate a ComplexNDArray of ones with given shape filled with ones.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- shape: Shape of the ComplexNDArray.


```rust
ones[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](shape: List[Int]) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Overload of function `ones` that reads a list of ints.  
  
Parameters:  

- cdtype Defualt: `{float64, float64}`
- dtype Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- shape


```rust
ones[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](shape: VariadicList[Int]) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Overload of function `ones` that reads a variadic of ints.  
  
Parameters:  

- cdtype Defualt: `{float64, float64}`
- dtype Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- shape

## ones_like


```rust
ones_like[dtype: DType = float64](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Generate a NDArray of the same shape as `a` filled with ones.  
  
Parameters:  

- dtype: Datatype of the NDArray. Defualt: `float64`
  
Args:  

- array: NDArray to be used as a reference for the shape.


```rust
ones_like[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](array: ComplexNDArray[cdtype, dtype=dtype]) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Generate a ComplexNDArray of the same shape as `a` filled with ones.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- array: ComplexNDArray to be used as a reference for the shape.

## zeros


```rust
zeros[dtype: DType = float64](shape: NDArrayShape) -> NDArray[dtype]
```  
Summary  
  
Generate a NDArray of zeros with given shape.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- shape: Shape of the NDArray.


```rust
zeros[dtype: DType = float64](shape: List[Int]) -> NDArray[dtype]
```  
Summary  
  
Overload of function `zeros` that reads a list of ints.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape


```rust
zeros[dtype: DType = float64](shape: VariadicList[Int]) -> NDArray[dtype]
```  
Summary  
  
Overload of function `zeros` that reads a variadic list of ints.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape


```rust
zeros[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](shape: NDArrayShape) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Generate a ComplexNDArray of zeros with given shape.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- shape: Shape of the ComplexNDArray.


```rust
zeros[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](shape: List[Int]) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Overload of function `zeros` that reads a list of ints.  
  
Parameters:  

- cdtype Defualt: `{float64, float64}`
- dtype Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- shape


```rust
zeros[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](shape: VariadicList[Int]) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Overload of function `zeros` that reads a variadic list of ints.  
  
Parameters:  

- cdtype Defualt: `{float64, float64}`
- dtype Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- shape

## zeros_like


```rust
zeros_like[dtype: DType = float64](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Generate a NDArray of the same shape as `a` filled with zeros.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- array: NDArray to be used as a reference for the shape.


```rust
zeros_like[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](array: ComplexNDArray[cdtype, dtype=dtype]) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Generate a ComplexNDArray of the same shape as `a` filled with zeros.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- array: ComplexNDArray to be used as a reference for the shape.

## full


```rust
full[dtype: DType = float64](shape: NDArrayShape, fill_value: SIMD[dtype, 1], order: String = String("C")) -> NDArray[dtype]
```  
Summary  
  
Initialize an NDArray of certain shape fill it with a given value.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape: Shape of the array.
- fill_value: Set all the values to this.
- order: Memory order C or F. Default: String("C")


```rust
full[dtype: DType = float64](shape: List[Int], fill_value: SIMD[dtype, 1], order: String = String("C")) -> NDArray[dtype]
```  
Summary  
  
Overload of function `full` that reads a list of ints.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape
- fill_value
- order Default: String("C")


```rust
full[dtype: DType = float64](shape: VariadicList[Int], fill_value: SIMD[dtype, 1], order: String = String("C")) -> NDArray[dtype]
```  
Summary  
  
Overload of function `full` that reads a variadic list of ints.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape
- fill_value
- order Default: String("C")


```rust
full[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](shape: NDArrayShape, fill_value: ComplexSIMD[cdtype, dtype=dtype], order: String = String("C")) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Initialize an ComplexNDArray of certain shape fill it with a given value.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- shape: Shape of the ComplexNDArray.
- fill_value: Set all the values to this.
- order: Memory order C or F. Default: String("C")


```rust
full[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](shape: List[Int], fill_value: ComplexSIMD[cdtype, dtype=dtype], order: String = String("C")) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Overload of function `full` that reads a list of ints.  
  
Parameters:  

- cdtype Defualt: `{float64, float64}`
- dtype Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- shape
- fill_value
- order Default: String("C")


```rust
full[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](shape: VariadicList[Int], fill_value: ComplexSIMD[cdtype, dtype=dtype], order: String = String("C")) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Overload of function `full` that reads a variadic list of ints.  
  
Parameters:  

- cdtype Defualt: `{float64, float64}`
- dtype Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- shape
- fill_value
- order Default: String("C")

## full_like


```rust
full_like[dtype: DType = float64](array: NDArray[dtype], fill_value: SIMD[dtype, 1], order: String = String("C")) -> NDArray[dtype]
```  
Summary  
  
Generate a NDArray of the same shape as `a` filled with `fill_value`.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- array: NDArray to be used as a reference for the shape.
- fill_value: Value to fill the NDArray with.
- order: Memory order C or F. Default: String("C")


```rust
full_like[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](array: ComplexNDArray[cdtype, dtype=dtype], fill_value: ComplexSIMD[cdtype, dtype=dtype], order: String = String("C")) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Generate a ComplexNDArray of the same shape as `a` filled with `fill_value`.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- array: ComplexNDArray to be used as a reference for the shape.
- fill_value: Value to fill the ComplexNDArray with.
- order: Memory order C or F. Default: String("C")

## diag


```rust
diag[dtype: DType = float64](v: NDArray[dtype], k: Int = 0) -> NDArray[dtype]
```  
Summary  
  
Extract a diagonal or construct a diagonal NDArray.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- v: NDArray to extract the diagonal from.
- k: Diagonal offset. Default: 0


```rust
diag[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](v: ComplexNDArray[cdtype, dtype=dtype], k: Int = 0) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Extract a diagonal or construct a diagonal ComplexNDArray.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- v: ComplexNDArray to extract the diagonal from.
- k: Diagonal offset. Default: 0

## diagflat


```rust
diagflat[dtype: DType = float64](v: NDArray[dtype], k: Int = 0) -> NDArray[dtype]
```  
Summary  
  
Generate a 2-D NDArray with the flattened input as the diagonal.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- v: NDArray to be flattened and used as the diagonal.
- k: Diagonal offset. Default: 0


```rust
diagflat[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](v: ComplexNDArray[cdtype, dtype=dtype], k: Int = 0) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Generate a 2-D ComplexNDArray with the flattened input as the diagonal.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- v: ComplexNDArray to be flattened and used as the diagonal.
- k: Diagonal offset. Default: 0

## tri


```rust
tri[dtype: DType = float64](N: Int, M: Int, k: Int = 0) -> NDArray[dtype]
```  
Summary  
  
Generate a 2-D NDArray with ones on and below the k-th diagonal.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- N: Number of rows in the matrix.
- M: Number of columns in the matrix.
- k: Diagonal offset. Default: 0


```rust
tri[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](N: Int, M: Int, k: Int = 0) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Generate a 2-D ComplexNDArray with ones on and below the k-th diagonal.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- N: Number of rows in the matrix.
- M: Number of columns in the matrix.
- k: Diagonal offset. Default: 0

## tril


```rust
tril[dtype: DType = float64](m: NDArray[dtype], k: Int = 0) -> NDArray[dtype]
```  
Summary  
  
Zero out elements above the k-th diagonal.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- m: NDArray to be zeroed out.
- k: Diagonal offset. Default: 0


```rust
tril[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](m: ComplexNDArray[cdtype, dtype=dtype], k: Int = 0) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Zero out elements above the k-th diagonal.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- m: ComplexNDArray to be zeroed out.
- k: Diagonal offset. Default: 0

## triu


```rust
triu[dtype: DType = float64](m: NDArray[dtype], k: Int = 0) -> NDArray[dtype]
```  
Summary  
  
Zero out elements below the k-th diagonal.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- m: NDArray to be zeroed out.
- k: Diagonal offset. Default: 0


```rust
triu[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](m: ComplexNDArray[cdtype, dtype=dtype], k: Int = 0) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Zero out elements below the k-th diagonal.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- m: ComplexNDArray to be zeroed out.
- k: Diagonal offset. Default: 0

## vander


```rust
vander[dtype: DType = float64](x: NDArray[dtype], N: Optional[Int] = Optional(None), increasing: Bool = False) -> NDArray[dtype]
```  
Summary  
  
Generate a Vandermonde matrix.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- x: 1-D input array.
- N: Number of columns in the output. If N is not specified, a square array is returned. Default: Optional(None)
- increasing: Order of the powers of the columns. If True, the powers increase from left to right, if False (the default) they are reversed. Default: False


```rust
vander[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](x: ComplexNDArray[cdtype, dtype=dtype], N: Optional[Int] = Optional(None), increasing: Bool = False) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Generate a Complex Vandermonde matrix.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- x: 1-D input array.
- N: Number of columns in the output. If N is not specified, a square array is returned. Default: Optional(None)
- increasing: Order of the powers of the columns. If True, the powers increase from left to right, if False (the default) they are reversed. Default: False

## astype


```rust
astype[dtype: DType, //, target: DType](a: NDArray[dtype]) -> NDArray[target]
```  
Summary  
  
Cast an NDArray to a different dtype.  
  
Parameters:  

- dtype: Data type of the input array, always inferred.
- target: Data type to cast the NDArray to.
  
Args:  

- a: NDArray to be casted.


```rust
astype[cdtype: CDType, //, target: CDType, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType](), target_dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](a: ComplexNDArray[cdtype, dtype=dtype]) -> ComplexNDArray[target, dtype=target_dtype]
```  
Summary  
  
Cast a ComplexNDArray to a different dtype.  
  
Parameters:  

- cdtype: Complex datatype of the input array.
- target: Complex datatype of the output array.
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
- target_dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- a: ComplexNDArray to be casted.

## fromstring


```rust
fromstring[dtype: DType = float64](text: String, order: String = String("C")) -> NDArray[dtype]
```  
Summary  
  
NDArray initialization from string representation of an ndarray. The shape can be inferred from the string representation. The literals will be casted to the dtype of the NDArray.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- text: String representation of an ndarray.
- order: Memory order C or F. Default: String("C")

## from_tensor


```rust
from_tensor[dtype: DType = float64](data: Tensor[dtype]) -> NDArray[dtype]
```  
Summary  
  
Create array from tensor.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- data: Tensor.

## array


```rust
array[dtype: DType = float64](text: String, order: String = String("C")) -> NDArray[dtype]
```  
Summary  
  
This reload is an alias of `fromstring`.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- text
- order Default: String("C")


```rust
array[dtype: DType = float64](data: List[SIMD[dtype, 1]], shape: List[Int], order: String = String("C")) -> NDArray[dtype]
```  
Summary  
  
Array creation with given data, shape and order.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- data: List of data.
- shape: List of shape.
- order: Memory order C or F. Default: String("C")


```rust
array[cdtype: CDType = {float64, float64}, *, dtype: DType = to_dtype[numojo::core::complex::complex_dtype::CDType]()](real: List[SIMD[dtype, 1]], imag: List[SIMD[dtype, 1]], shape: List[Int], order: String = String("C")) -> ComplexNDArray[cdtype, dtype=dtype]
```  
Summary  
  
Array creation with given data, shape and order.  
  
Parameters:  

- cdtype: Complex datatype of the output array. Defualt: `{float64, float64}`
- dtype: Equivalent real datatype of the output array. Defualt: `to_dtype[numojo::core::complex::complex_dtype::CDType]()`
  
Args:  

- real: List of real data.
- imag: List of imaginary data.
- shape: List of shape.
- order: Memory order C or F. Default: String("C")


```rust
array[dtype: DType = float64](data: PythonObject, order: String = String("C")) -> NDArray[dtype]
```  
Summary  
  
Array creation with given data, shape and order.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- data: A Numpy array (PythonObject).
- order: Memory order C or F. Default: String("C")


```rust
array[dtype: DType = float64](data: Tensor[dtype]) -> NDArray[dtype]
```  
Summary  
  
Create array from tensor.  
  
Parameters:  

- dtype: Datatype of the NDArray elements. Defualt: `float64`
  
Args:  

- data: Tensor.
