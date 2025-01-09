



# rounding

##  Module Summary
  

## tabs


```Mojo
tabs[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Elementwise absolute value of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## tfloor


```Mojo
tfloor[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Elementwise round down to nearest whole number of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## tceil


```Mojo
tceil[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Elementwise round up to nearest whole number of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## ttrunc


```Mojo
ttrunc[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Elementwise remove decimal value from float whole number of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## tround


```Mojo
tround[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Elementwise round NDArray to whole number.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## roundeven


```Mojo
roundeven[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Performs elementwise banker's rounding on the elements of a NDArray.  
  
Parameters:  

- dtype: The dtype of the input and output array.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: Array to perform rounding on.

## nextafter


```Mojo
nextafter[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Computes the nextafter of the inputs.  
  
Parameters:  

- dtype: The dtype of the input and output array. Constraints: must be a floating-point type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array1: The first input argument.
- array2: The second input argument.
