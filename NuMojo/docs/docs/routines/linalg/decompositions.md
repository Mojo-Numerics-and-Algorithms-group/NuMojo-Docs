



# decompositions

##  Module Summary
  

## lu_decomposition


```Mojo
lu_decomposition[dtype: DType](A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[dtype]]
```  
Summary  
  
Perform LU (lower-upper) decomposition for matrix.  
  
Parameters:  

- dtype: Data type of the upper and upper triangular matrices.
  
Args:  

- A: Input matrix for decoposition. It should be a row-major matrix.


For efficiency, `dtype` of the output arrays will be the same as the input
array. Thus, use `astype()` before passing the array to this function.

Example:
```
import numojo as nm
fn main() raises:
    var arr = nm.NDArray[nm.f64]("[[1,2,3], [4,5,6], [7,8,9]]")
    var U: nm.NDArray
    var L: nm.NDArray
    L, U = nm.math.linalg.solver.lu_decomposition(arr)
    print(arr)
    print(L)
    print(U)
```
```console
[[      1.0     2.0     3.0     ]
 [      4.0     5.0     6.0     ]
 [      7.0     8.0     9.0     ]]
2-D array  Shape: [3, 3]  DType: float64
[[      1.0     0.0     0.0     ]
 [      4.0     1.0     0.0     ]
 [      7.0     2.0     1.0     ]]
2-D array  Shape: [3, 3]  DType: float64
[[      1.0     2.0     3.0     ]
 [      0.0     -3.0    -6.0    ]
 [      0.0     0.0     0.0     ]]
2-D array  Shape: [3, 3]  DType: float64
```

Further reading:
    Linear Algebra And Its Applications, fourth edition, Gilbert Strang
    https://en.wikipedia.org/wiki/LU_decomposition
    https://www.scicoding.com/how-to-calculate-lu-decomposition-in-python/
    https://courses.physics.illinois.edu/cs357/sp2020/notes/ref-9-linsys.html

TODO: Optimize the speed.