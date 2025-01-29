



# random

##  Module Summary
  
Random values array generation.
## rand


```rust
rand[dtype: DType = float64](*shape: Int) -> NDArray[dtype]
```  
Summary  
  
Generate a random NDArray of the given shape and dtype.  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `float64`
  
Args:  

- \*shape: The shape of the NDArray.


```rust
rand[dtype: DType = float64](*shape: Int, *, min: SIMD[dtype, 1], max: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Generate a random NDArray of the given shape and dtype with values between `min` and `max`.  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `float64`
  
Args:  

- \*shape: The shape of the NDArray.
- min: The minimum value of the random values.
- max: The maximum value of the random values.


```rust
rand[dtype: DType = float64](shape: List[Int], min: SIMD[dtype, 1], max: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Generate a random NDArray of the given shape and dtype with values between `min` and `max`.  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `float64`
  
Args:  

- shape: The shape of the NDArray.
- min: The minimum value of the random values.
- max: The maximum value of the random values.

## randn


```rust
randn[dtype: DType = float64](*shape: Int, *, mean: SIMD[dtype, 1] = SIMD(0), variance: SIMD[dtype, 1] = SIMD(1)) -> NDArray[dtype]
```  
Summary  
  
Generate a random NDArray of the given shape and dtype with values having a mean and variance.  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `float64`
  
Args:  

- \*shape: The shape of the NDArray.
- mean: The mean value of the random values. Default: SIMD(0)
- variance: The variance of the random values. Default: SIMD(1)


```rust
randn[dtype: DType = float64](shape: List[Int], mean: SIMD[dtype, 1] = SIMD(0), variance: SIMD[dtype, 1] = SIMD(1)) -> NDArray[dtype]
```  
Summary  
  
Generate a random NDArray of the given shape and dtype with values having a mean and variance.  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `float64`
  
Args:  

- shape: The shape of the NDArray.
- mean: The mean value of the random values. Default: SIMD(0)
- variance: The variance of the random values. Default: SIMD(1)

## rand_exponential


```rust
rand_exponential[dtype: DType = float64](*shape: Int, *, rate: SIMD[dtype, 1] = SIMD(#kgen.float_literal<1|1>)) -> NDArray[dtype]
```  
Summary  
  
Generate a random NDArray of the given shape and dtype with values from an exponential distribution.  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `float64`
  
Args:  

- \*shape: The shape of the NDArray.
- rate: The rate parameter of the exponential distribution (lambda). Default: SIMD(#kgen.float_literal<1|1>)


```rust
rand_exponential[dtype: DType = float64](shape: List[Int], rate: SIMD[dtype, 1] = SIMD(#kgen.float_literal<1|1>)) -> NDArray[dtype]
```  
Summary  
  
Generate a random NDArray of the given shape and dtype with values from an exponential distribution.  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `float64`
  
Args:  

- shape: The shape of the NDArray as a List[Int].
- rate: The rate parameter of the exponential distribution (lambda). Default: SIMD(#kgen.float_literal<1|1>)
