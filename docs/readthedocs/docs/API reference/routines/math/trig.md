



# trig

##  Module Summary
  
Implements Trigonometry functions for arrays.
## arccos


```rust
arccos[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- A

## acos


```rust
acos[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply acos also known as inverse cosine .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array.


```rust
acos[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- A

## arcsin


```rust
arcsin[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- A

## asin


```rust
asin[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply asin also known as inverse sine .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array.


```rust
asin[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- A

## arctan


```rust
arctan[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- A

## atan


```rust
atan[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply atan also known as inverse tangent .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array.


```rust
atan[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- A

## atan2


```rust
atan2[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply atan2 also known as inverse tangent. [atan2 wikipedia](https://en.wikipedia.org/wiki/Atan2).  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: An Array.
- array2: An Array.

## cos


```rust
cos[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply cos also known as cosine.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array assumed to be in radian.


```rust
cos[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- A

## sin


```rust
sin[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply sin also known as sine .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array assumed to be in radian.


```rust
sin[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- A

## tan


```rust
tan[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply tan also known as tangent .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array assumed to be in radian.


```rust
tan[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- A

## hypot


```rust
hypot[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply hypot also known as hypotenuse which finds the longest section of a right triangle given the other two sides.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: An Array.
- array2: An Array.

## hypot_fma


```rust
hypot_fma[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply hypot also known as hypotenuse which finds the longest section of a right triangle given the other two sides.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: An Array.
- array2: An Array.
