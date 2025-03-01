



# random

##  Module Summary
  
numojo.routines.random ----------------------
## rand


```rust
rand[dtype: DType = float64](shape: NDArrayShape) -> NDArray[dtype]
```  
Summary  
  
Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `float64`
  
Args:  

- shape: The shape of the NDArray.


```rust
rand[dtype: DType = float64](*shape: Int) -> NDArray[dtype]
```  
Summary  
  
Overloads the function `rand(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- \*shape


```rust
rand[dtype: DType = float64](shape: List[Int]) -> NDArray[dtype]
```  
Summary  
  
Overloads the function `rand(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape


```rust
rand[dtype: DType = float64](shape: VariadicList[Int]) -> NDArray[dtype]
```  
Summary  
  
Overloads the function `rand(shape: NDArrayShape)` Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape


```rust
rand[dtype: DType = float64](shape: NDArrayShape, min: SIMD[dtype, 1], max: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Creates an array of the given shape and populate it with random samples from a uniform distribution over [min, max). This is equivalent to `min + rand() * (max - min)`.  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `float64`
  
Args:  

- shape: The shape of the NDArray.
- min: The minimum value of the random values.
- max: The maximum value of the random values.


```rust
rand[dtype: DType = float64](*shape: Int, *, min: SIMD[dtype, 1], max: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Overloads the function `rand(shape: NDArrayShape, min, max)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [min, max). This is equivalent to `min + rand() * (max - min)`.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- \*shape
- min
- max


```rust
rand[dtype: DType = float64](shape: List[Int], min: SIMD[dtype, 1], max: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Overloads the function `rand(shape: NDArrayShape, min, max)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [min, max). This is equivalent to `min + rand() * (max - min)`.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape
- min
- max

## randint


```rust
randint[dtype: DType = int64](shape: NDArrayShape, low: Int, high: Int) -> NDArray[dtype]
```  
Summary  
  
Return an array of random integers from low (inclusive) to high (exclusive). Note that it is different from the built-in `random.randint()` function which returns integer in range low (inclusive) to high (inclusive).  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `int64`
  
Args:  

- shape: The shape of the NDArray.
- low: The minimum value of the random values.
- high: The maximum value of the random values.


```rust
randint[dtype: DType = int64](*shape: Int, *, low: Int, high: Int) -> NDArray[dtype]
```  
Summary  
  
Overloads the function `randint(shape: NDArrayShape, low, high)`. Return an array of random integers from low (inclusive) to high (exclusive). Note that it is different from the built-in `random.randint()` function which returns integer in range low (inclusive) to high (inclusive).  
  
Parameters:  

- dtype Defualt: `int64`
  
Args:  

- \*shape
- low
- high


```rust
randint[dtype: DType = int64](shape: NDArrayShape, high: Int) -> NDArray[dtype]
```  
Summary  
  
Return an array of random integers from 0 (inclusive) to high (exclusive).  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `int64`
  
Args:  

- shape: The shape of the NDArray.
- high: The maximum value of the random values.


```rust
randint[dtype: DType = int64](*shape: Int, *, high: Int) -> NDArray[dtype]
```  
Summary  
  
Overloads the function `randint(shape: NDArrayShape, high)`. Return an array of random integers from 0 (inclusive) to high (exclusive).  
  
Parameters:  

- dtype Defualt: `int64`
  
Args:  

- \*shape
- high

## randn


```rust
randn[dtype: DType = float64](shape: NDArrayShape) -> NDArray[dtype]
```  
Summary  
  
Creates an array of the given shape and populate it with random samples from a standard normal distribution.  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `float64`
  
Args:  

- shape: The shape of the NDArray.


```rust
randn[dtype: DType = float64](*shape: Int) -> NDArray[dtype]
```  
Summary  
  
Overloads the function `randn(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a standard normal distribution.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- \*shape


```rust
randn[dtype: DType = float64](shape: NDArrayShape, mean: SIMD[dtype, 1], variance: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Creates an array of the given shape and populate it with random samples from a normal distribution with given mean and variance.  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `float64`
  
Args:  

- shape: The shape of the NDArray.
- mean: The mean value of the random values.
- variance: The variance of the random values.


```rust
randn[dtype: DType = float64](*shape: Int, *, mean: SIMD[dtype, 1], variance: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Overloads the function `randn(shape: NDArrayShape, mean, variance)`. Creates an array of the given shape and populate it with random samples from a normal distribution with given mean and variance.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- \*shape
- mean
- variance


```rust
randn[dtype: DType = float64](shape: List[Int], mean: SIMD[dtype, 1], variance: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Overloads the function `randn(shape: NDArrayShape, mean, variance)`. Creates an array of the given shape and populate it with random samples from a normal distribution with given mean and variance.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape
- mean
- variance

## exponential


```rust
exponential[dtype: DType = float64](shape: NDArrayShape, scale: SIMD[dtype, 1] = SIMD(#kgen.float_literal<1|1>)) -> NDArray[dtype]
```  
Summary  
  
Creates an array of the given shape and populate it with random samples from an exponential distribution with given scale parameter.  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `float64`
  
Args:  

- shape: The shape of the NDArray.
- scale: The scale parameter of the exponential distribution (lambda). Default: SIMD(#kgen.float_literal<1|1>)


```rust
exponential[dtype: DType = float64](*shape: Int, *, scale: SIMD[dtype, 1] = SIMD(#kgen.float_literal<1|1>)) -> NDArray[dtype]
```  
Summary  
  
Overloads the function `exponential(shape: NDArrayShape, rate)`. Creates an array of the given shape and populate it with random samples from an exponential distribution with given scale parameter.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- \*shape
- scale Default: SIMD(#kgen.float_literal<1|1>)


```rust
exponential[dtype: DType = float64](shape: List[Int], scale: SIMD[dtype, 1] = SIMD(#kgen.float_literal<1|1>)) -> NDArray[dtype]
```  
Summary  
  
Overloads the function `exponential(shape: NDArrayShape, rate)`. Creates an array of the given shape and populate it with random samples from an exponential distribution with given scale parameter.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape
- scale Default: SIMD(#kgen.float_literal<1|1>)
