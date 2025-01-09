



# sums

##  Module Summary
  

## sum


```Mojo
sum[dtype: DType](A: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Sum of all items in the array.  
  
Parameters:  

- dtype
  
Args:  

- A: NDArray.


Example:
```console
> print(A)
[[      0.1315377950668335      0.458650141954422       0.21895918250083923     ]
 [      0.67886471748352051     0.93469291925430298     0.51941639184951782     ]
 [      0.034572109580039978    0.52970021963119507     0.007698186207562685    ]]
2-D array  Shape: [3, 3]  DType: float32
> print(nm.sum(A))
3.5140917301177979
```


```Mojo
sum[dtype: DType](A: NDArray[dtype], axis: Int) -> NDArray[dtype]
```  
Summary  
  
Sum of array elements over a given axis.  
  
Parameters:  

- dtype
  
Args:  

- A: NDArray.
- axis: The axis along which the sum is performed.


Example:
```mojo
import numojo as nm
var A = nm.random.randn(100, 100)
print(nm.sum(A, axis=0))
```

## cumsum


```Mojo
cumsum[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Sum of all items of an array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: An NDArray.
