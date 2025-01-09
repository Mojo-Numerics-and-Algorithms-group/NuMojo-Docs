



# hyper

##  Module Summary
  
Implements Hyperbolic functions for arrays.
## acosh


```Mojo
acosh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply acosh also known as inverse hyperbolic cosine .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array.

## asinh


```Mojo
asinh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply asinh also known as inverse hyperbolic sine .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array.

## atanh


```Mojo
atanh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply atanh also known as inverse hyperbolic tangent .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array.

## cosh


```Mojo
cosh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply cosh also known as hyperbolic cosine .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array assumed to be in radian.

## sinh


```Mojo
sinh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply sin also known as hyperbolic sine .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array assumed to be in radian.

## tanh


```Mojo
tanh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply tan also known as hyperbolic tangent .  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized. Defualt: `Vectorized`
  
Args:  

- array: An Array assumed to be in radian.
