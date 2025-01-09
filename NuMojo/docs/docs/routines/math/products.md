



# products

##  Module Summary
  

## prod


```Mojo
prod(array: NDArray[dtype], axis: Int = 0) -> NDArray[dtype]
```  
Summary  
  
Product of array elements over a given axis.  
  
Args:  

- array: NDArray.
- axis: The axis along which the product is performed. Default: 0

## prodall


```Mojo
prodall(array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Product of all items in the array.  
  
Args:  

- array: NDArray.


Example:
```console
> print(A)
[[      0.1315377950668335      0.458650141954422       0.21895918250083923     ]
[      0.67886471748352051     0.93469291925430298     0.51941639184951782     ]
[      0.034572109580039978    0.52970021963119507     0.007698186207562685    ]]
2-D array  Shape: [3, 3]  DType: float32

> print(nm.math.stats.prodall(A))
6.1377261317829834e-07
```

## cumprod


```Mojo
cumprod[dtype: DType = float64](array: NDArray[dtype]) -> SIMD[dtype, 1]
```  
Summary  
  
Product of all items in an array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: An NDArray.
