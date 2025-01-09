



# manipulation

##  Module Summary
  
Array manipulation routines.
## copyto


```Mojo
copyto()
```  
Summary  
  
  

## ndim


```Mojo
ndim[dtype: DType](array: NDArray[dtype]) -> Int
```  
Summary  
  
Returns the number of dimensions of the NDArray.  
  
Parameters:  

- dtype
  
Args:  

- array: A NDArray.

## shape


```Mojo
shape[dtype: DType](array: NDArray[dtype]) -> NDArrayShape
```  
Summary  
  
Returns the shape of the NDArray.  
  
Parameters:  

- dtype
  
Args:  

- array: A NDArray.

## size


```Mojo
size[dtype: DType](array: NDArray[dtype], axis: Int) -> Int
```  
Summary  
  
Returns the size of the NDArray.  
  
Parameters:  

- dtype
  
Args:  

- array: A NDArray.
- axis: The axis to get the size of.

## reshape


```Mojo
reshape[dtype: DType](mut array: NDArray[dtype], shape: VariadicList[Int], order: String = String("C"))
```  
Summary  
  
    Reshapes the NDArray to given Shape.  
  
Parameters:  

- dtype
  
Args:  

- array: A NDArray.
- shape: Variadic integers of shape.
- order: Order of the array - Row major `C` or Column major `F`. Default: String("C")

## ravel


```Mojo
ravel[dtype: DType](mut array: NDArray[dtype], order: String = String("C"))
```  
Summary  
  
Returns the raveled version of the NDArray.  
  
Parameters:  

- dtype
  
Args:  

- array
- order Default: String("C")

## flatten


```Mojo
flatten[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Flattens the NDArray.  
  
Parameters:  

- dtype: Dataype of the NDArray elements.
  
Args:  

- array: A NDArray.

## transpose


```Mojo
transpose[dtype: DType](A: NDArray[dtype], axes: List[Int]) -> NDArray[dtype]
```  
Summary  
  
Transpose array of any number of dimensions according to arbitrary permutation of the axes.  
  
Parameters:  

- dtype
  
Args:  

- A
- axes


If `axes` is not given, it is equal to flipping the axes.
```mojo
import numojo as nm
var A = nm.random.rand(2,3,4,5)
nm.transpose(A)  # A is a 4darray.
nm.transpose(A, axes=List(3,2,1,0))
```

Examples.
```mojo
import numojo as nm
# A is a 2darray
nm.transpose(A, axes=List(0, 1))  # equal to transpose of matrix
# A is a 3darray
nm.transpose(A, axes=List(2, 1, 0))  # transpose 0-th and 2-th dimensions
```

```Mojo
transpose[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
(overload) Transpose the array when `axes` is not given. If `axes` is not given, it is equal to flipping the axes. See docstring of `transpose`.  
  
Parameters:  

- dtype
  
Args:  

- A

## flip


```Mojo
flip[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Flips the NDArray along the given axis.  
  
Parameters:  

- dtype: DType.
  
Args:  

- array: A NDArray.
