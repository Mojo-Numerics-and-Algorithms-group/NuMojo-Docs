



# misc

##  Module Summary
  

## cbrt


```rust
cbrt[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element-wise cuberoot of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array: A NDArray.

## clip


```rust
clip[dtype: DType, //](a: NDArray[dtype], a_min: SIMD[dtype, 1], a_max: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Limit the values in an array between [a_min, a_max]. If a_min is greater than a_max, the value is equal to a_max.  
  
Parameters:  

- dtype: The data type.
  
Args:  

- a: A array.
- a_min: The minimum value.
- a_max: The maximum value.

## rsqrt


```rust
rsqrt[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element-wise reciprocal squareroot of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## sqrt


```rust
sqrt[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element-wise square root of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## scalb


```rust
scalb[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Calculate the scalb of array1 and array2.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array1: A NDArray.
- array2: A NDArray.
