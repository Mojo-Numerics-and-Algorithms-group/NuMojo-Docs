



# averages

##  Module Summary
  
Averages and variances
## mean


```Mojo
mean(array: NDArray[dtype], axis: Int = 0) -> NDArray[dtype]
```  
Summary  
  
Mean of array elements over a given axis. Args:     array: NDArray.     axis: The axis along which the mean is performed. Returns:     An NDArray.  
  
Args:  

- array
- axis Default: 0

## meanall


```Mojo
meanall(array: NDArray[dtype]) -> SIMD[float64, 1]
```  
Summary  
  
Mean of all items in the array.  
  
Args:  

- array: NDArray.


Example:
```console
> print(A)
[[      0.1315377950668335      0.458650141954422       0.21895918250083923     ]
[      0.67886471748352051     0.93469291925430298     0.51941639184951782     ]
[      0.034572109580039978    0.52970021963119507     0.007698186207562685    ]]
2-D array  Shape: [3, 3]  DType: float32

> print(nm.math.stats.meanall(A))
0.39045463667975533
```

## max


```Mojo
max[dtype: DType](array: NDArray[dtype], axis: Int = 0) -> NDArray[dtype]
```  
Summary  
  
Maximums of array elements over a given axis.  
  
Parameters:  

- dtype
  
Args:  

- array: NDArray.
- axis: The axis along which the sum is performed. Default: 0

## min


```Mojo
min[dtype: DType](array: NDArray[dtype], axis: Int = 0) -> NDArray[dtype]
```  
Summary  
  
Minumums of array elements over a given axis.  
  
Parameters:  

- dtype
  
Args:  

- array: NDArray.
- axis: The axis along which the sum is performed. Default: 0

## cummean


```Mojo
cummean[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Arithmatic mean of all items of an array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: An NDArray.

## mode


```Mojo
mode[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Mode of all items of an array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: An NDArray.

## median


```Mojo
median[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Median value of all items of an array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: An NDArray.

## cumpvariance


```Mojo
cumpvariance[dtype: DType = float64](array: NDArray[dtype], mu: Optional[SIMD[dtype, 1]] = Optional(None)) -> SIMD[dtype, 1]
```  
Summary  
  
Population variance of a array.  
  
Parameters:  

- dtype: The element type.. Defualt: `float64`
  
Args:  

- array: A NDArray.
- mu: The mean of the array, if provided. Default: Optional(None)

## cumvariance


```Mojo
cumvariance[dtype: DType = float64](array: NDArray[dtype], mu: Optional[SIMD[dtype, 1]] = Optional(None)) -> SIMD[dtype, 1]
```  
Summary  
  
Variance of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A NDArray.
- mu: The mean of the array, if provided. Default: Optional(None)

## cumpstdev


```Mojo
cumpstdev[dtype: DType = float64](array: NDArray[dtype], mu: Optional[SIMD[dtype, 1]] = Optional(None)) -> SIMD[dtype, 1]
```  
Summary  
  
Population standard deviation of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A NDArray.
- mu: The mean of the array, if provided. Default: Optional(None)

## cumstdev


```Mojo
cumstdev[dtype: DType = float64](array: NDArray[dtype], mu: Optional[SIMD[dtype, 1]] = Optional(None)) -> SIMD[dtype, 1]
```  
Summary  
  
Standard deviation of a array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A NDArray.
- mu: The mean of the array, if provided. Default: Optional(None)
