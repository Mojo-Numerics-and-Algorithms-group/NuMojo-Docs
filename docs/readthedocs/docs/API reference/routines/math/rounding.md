



# rounding

##  Module Summary
  

## round


```rust
round[dtype: DType](owned A: Matrix[dtype], decimals: Int = 0) -> Matrix[dtype]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- A
- decimals Default: 0

## tabs


```rust
tabs[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element-wise absolute value of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## tfloor


```rust
tfloor[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element-wise round down to nearest whole number of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## tceil


```rust
tceil[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element-wise round up to nearest whole number of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## ttrunc


```rust
ttrunc[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element-wise remove decimal value from float whole number of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## tround


```rust
tround[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element-wise round NDArray to whole number.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## roundeven


```rust
roundeven[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Performs element-wise banker's rounding on the elements of a NDArray.  
  
Parameters:  

- dtype: The dtype of the input and output array.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: Array to perform rounding on.

## nextafter


```rust
nextafter[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Computes the nextafter of the inputs.  
  
Parameters:  

- dtype: The dtype of the input and output array. Constraints: must be a floating-point type.
- backend: Sets utility function origin, default to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array1: The first input argument.
- array2: The second input argument.
