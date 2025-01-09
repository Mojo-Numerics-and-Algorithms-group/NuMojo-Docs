



# extrema

##  Module Summary
  
TODO:  1) Add support for axis parameter.   2) Currently, constrained is crashing mojo, so commented it out and added raise Error. Check later. 3) Relax constrained[] to let user get whatever output they want, but make a warning instead.
## maxT


```Mojo
maxT[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Maximum value of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A NDArray.

## minT


```Mojo
minT[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Minimum value of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A NDArray.

## amin


```Mojo
amin[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Minimum value of an array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: An array.

## amax


```Mojo
amax[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Maximum value of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A array.

## mimimum


```Mojo
mimimum[dtype: DType = float64](s1: SIMD[dtype, 1], s2: SIMD[dtype, 1]) -> SIMD[dtype, 1]
```  
Summary  
  
Minimum value of two SIMD values.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- s1: A SIMD Value.
- s2: A SIMD Value.

## maximum


```Mojo
maximum[dtype: DType = float64](s1: SIMD[dtype, 1], s2: SIMD[dtype, 1]) -> SIMD[dtype, 1]
```  
Summary  
  
Maximum value of two SIMD values.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- s1: A SIMD Value.
- s2: A SIMD Value.


```Mojo
maximum[dtype: DType = float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element wise maximum of two arrays.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array1: A array.
- array2: A array.

## minimum


```Mojo
minimum[dtype: DType = float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element wise minimum of two arrays.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array1: An array.
- array2: An array.
