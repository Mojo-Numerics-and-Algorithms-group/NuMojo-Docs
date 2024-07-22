



# trig

##  Module Summary
  
Implements Trigonometry functions for arrays.
## acos


```rust
acos[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply acos also known as inverse cosine .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array.

## asin


```rust
asin[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply asin also known as inverse sine .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array.

## atan


```rust
atan[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply atan also known as inverse tangent .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array.

## atan2


```rust
atan2[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply atan2 also known as inverse tangent. [atan2 wikipedia](https://en.wikipedia.org/wiki/Atan2).  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array1: An Array.
- array2: An Array.

## cos


```rust
cos[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply cos also known as cosine.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array assumed to be in radian.

## sin


```rust
sin[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply sin also known as sine .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array assumed to be in radian.

## tan


```rust
tan[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply tan also known as tangent .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array assumed to be in radian.

## hypot


```rust
hypot[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply hypot also known as hypotenuse which finds the longest section of a right triangle given the other two sides.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array1: An Array.
- array2: An Array.

## hypot_fma


```rust
hypot_fma[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply hypot also known as hypotenuse which finds the longest section of a right triangle given the other two sides.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array1: An Array.
- array2: An Array.

## acosh


```rust
acosh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply acosh also known as inverse hyperbolic cosine .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array.

## asinh


```rust
asinh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply asinh also known as inverse hyperbolic sine .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array.

## atanh


```rust
atanh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply atanh also known as inverse hyperbolic tangent .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array.

## cosh


```rust
cosh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply cosh also known as hyperbolic cosine .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array assumed to be in radian.

## sinh


```rust
sinh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply sin also known as hyperbolic sine .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array assumed to be in radian.

## tanh


```rust
tanh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply tan also known as hyperbolic tangent .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array assumed to be in radian.
