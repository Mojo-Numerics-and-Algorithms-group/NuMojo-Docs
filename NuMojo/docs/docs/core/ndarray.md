



# ndarray

##  Module Summary
  
Implements N-Dimensional Array
## NDArray

### NDArray Summary
  
  
The N-dimensional array (NDArray).  

### Parent Traits
  

- Absable
- AnyType
- CollectionElement
- Copyable
- Movable
- Representable
- Sized
- Stringable
- UnknownDestructibility
- Writable

### Aliases
  
`width`: Vector size of the data type.
### Fields
  
  
* ndim `Int`  
    - Number of Dimensions.  
* shape `NDArrayShape`  
    - Size and shape of NDArray.  
* size `Int`  
    - Size of NDArray.  
* strides `NDArrayStrides`  
    - Contains offset, strides.  
* coefficient `NDArrayStrides`  
    - Contains offset, coefficients for slicing.  
* datatype `DType`  
    - The datatype of memory.  
* order `String`  
    - Memory layout of array C (C order row major) or F (Fortran order col major).  

### Functions

#### __init__


```Mojo
__init__(out self, shape: NDArrayShape, order: String = String("C"))
```  
Summary  
  
Initialize an NDArray with given shape.  
  
Args:  

- self
- shape: Variadic shape.
- order: Memory order C or F. Default: String("C")


The memory is not filled with values.


```Mojo
__init__(out self, shape: List[Int], order: String = String("C"))
```  
Summary  
  
(Overload) Initialize an NDArray with given shape (list of integers).  
  
Args:  

- self
- shape: List of shape.
- order: Memory order C or F. Default: String("C")


```Mojo
__init__(out self, shape: VariadicList[Int], order: String = String("C"))
```  
Summary  
  
(Overload) Initialize an NDArray with given shape (variadic list of integers).  
  
Args:  

- self
- shape: Variadic List of shape.
- order: Memory order C or F. Default: String("C")


```Mojo
__init__(out self, ndim: Int, offset: Int, size: Int, shape: List[Int], strides: List[Int], coefficient: List[Int], order: String = String("C"))
```  
Summary  
  
Extremely specific NDArray initializer.  
  
Args:  

- self
- ndim
- offset
- size
- shape
- strides
- coefficient
- order Default: String("C")


```Mojo
__init__(out self, data: UnsafePointer[SIMD[dtype, 1]], ndim: Int, offset: Int, shape: List[Int], strides: List[Int], coefficient: List[Int], order: String = String("C"))
```  
Summary  
  
Extremely specific NDArray initializer.  
  
Args:  

- self
- data
- ndim
- offset
- shape
- strides
- coefficient
- order Default: String("C")

#### __copyinit__


```Mojo
__copyinit__(out self, other: Self)
```  
Summary  
  
Copy other into self.  
  
Args:  

- self
- other

#### __moveinit__


```Mojo
__moveinit__(out self, owned existing: Self)
```  
Summary  
  
Move other into self.  
  
Args:  

- self
- existing

#### __del__


```Mojo
__del__(owned self)
```  
Summary  
  
  
  
Args:  

- self

#### __bool__


```Mojo
__bool__(self) -> Bool
```  
Summary  
  
If all true return true.  
  
Args:  

- self

#### __getitem__


```Mojo
__getitem__(self, idx: Int) -> Self
```  
Summary  
  
Retreive a slice of the array corresponding to the index at the first dimension.  
  
Args:  

- self
- idx


Example:
    `arr[1]` returns the second row of the array.

```Mojo
__getitem__(self, index: Idx) -> SIMD[dtype, 1]
```  
Summary  
  
Set the value at the index list.  
  
Args:  

- self
- index


```Mojo
__getitem__(self, owned *slices: Slice) -> Self
```  
Summary  
  
Retreive slices of an array from variadic slices.  
  
Args:  

- self
- \*slices


Example:
    `arr[1:3, 2:4]` returns the corresponding sliced array (2 x 2).

```Mojo
__getitem__(self, owned slice_list: List[Slice]) -> Self
```  
Summary  
  
Retreive slices of an array from list of slices.  
  
Args:  

- self
- slice_list


Example:
    `arr[1:3, 2:4]` returns the corresponding sliced array (2 x 2).

```Mojo
__getitem__(self, owned *slices: Variant[Slice, Int]) -> Self
```  
Summary  
  
Get items by a series of either slices or integers.  
  
Args:  

- self
- \*slices: A series of either Slice or Int.


A decrease of dimensions may or may not happen when `__getitem__` is
called on an ndarray. An ndarray of X-D array can become Y-D array after
`__getitem__` where `Y <= X`.

Whether the dimension decerases or not depends on:
1. What types of arguments are passed into `__getitem__`.
2. The number of arguments that are passed in `__getitem__`.

PRINCIPAL: The number of dimensions to be decreased is determined by
the number of `Int` passed in `__getitem__`.

For example, `A` is a 10x10x10 ndarray (3-D). Then,

- `A[1, 2, 3]` leads to a 0-D array (scalar), since there are 3 integers.
- `A[1, 2]` leads to a 1-D array (vector), since there are 2 integers,
so the dimension decreases by 2.
- `A[1]` leads to a 2-D array (matrix), since there is 1 integer, so the
dimension decreases by 1.

The number of dimensions will not decrease when Slice is passed in
`__getitem__` or no argument is passed in for a certain dimension
(it is an implicit slide and a slide of all items will be used).

Take the same example `A` with 10x10x10 in shape. Then,

- `A[1:4, 2:5, 3:6]`, leads to a 3-D array (no decrease in dimension),
since there are 3 slices.
- `A[2:8]`, leads to a 3-D array (no decrease in dimension), since there
are 1 explicit slice and 2 implicit slices.

When there is a mixture of int and slices passed into `__getitem__`,
the number of integers will be the number of dimensions to be decreased.
Example,

- `A[1:4, 2, 2]`, leads to a 1-D array (vector), since there are 2
integers, so the dimension decreases by 2.

Note that, even though a slice contains one row, it does not reduce the
dimensions. Example,

- `A[1:2, 2:3, 3:4]`, leads to a 3-D array (no decrease in dimension),
since there are 3 slices.

Note that, when the number of integers equals to the number of
dimensions, the final outcome is an 0-D array instead of a number.
The user has to upack the 0-D array with the method`A.item(0)` to get the
corresponding number.
This behavior is different from numpy where the latter returns a number.

More examples for 1-D, 2-D, and 3-D arrays.

```console
A is a matrix
[[      -128    -95     65      -11     ]
[      8       -72     -116    45      ]
[      45      111     -30     4       ]
[      84      -120    -115    7       ]]
2-D array  Shape: [4, 4]  DType: int8

A[0]
[       -128    -95     65      -11     ]
1-D array  Shape: [4]  DType: int8

A[0, 1]
-95
0-D array  Shape: [0]  DType: int8

A[Slice(1,3)]
[[      8       -72     -116    45      ]
[      45      111     -30     4       ]]
2-D array  Shape: [2, 4]  DType: int8

A[1, Slice(2,4)]
[       -116    45      ]
1-D array  Shape: [2]  DType: int8

A[Slice(1,3), Slice(1,3)]
[[      -72     -116    ]
[      111     -30     ]]
2-D array  Shape: [2, 2]  DType: int8

A.item(0,1) as Scalar
-95

==============================
A is a vector
[       43      -127    -30     -111    ]
1-D array  Shape: [4]  DType: int8

A[0]
43
0-D array  Shape: [0]  DType: int8

A[Slice(1,3)]
[       -127    -30     ]
1-D array  Shape: [2]  DType: int8

A.item(0) as Scalar
43

==============================
A is a 3darray
[[[     -22     47      22      110     ]
[     88      6       -105    39      ]
[     -22     51      105     67      ]
[     -61     -116    60      -44     ]]
[[     33      65      125     -35     ]
[     -65     123     57      64      ]
[     38      -110    33      98      ]
[     -59     -17     68      -6      ]]
[[     -68     -58     -37     -86     ]
[     -4      101     104     -113    ]
[     103     1       4       -47     ]
[     124     -2      -60     -105    ]]
[[     114     -110    0       -30     ]
[     -58     105     7       -10     ]
[     112     -116    66      69      ]
[     83      -96     -124    48      ]]]
3-D array  Shape: [4, 4, 4]  DType: int8

A[0]
[[      -22     47      22      110     ]
[      88      6       -105    39      ]
[      -22     51      105     67      ]
[      -61     -116    60      -44     ]]
2-D array  Shape: [4, 4]  DType: int8

A[0, 1]
[       88      6       -105    39      ]
1-D array  Shape: [4]  DType: int8

A[0, 1, 2]
-105
0-D array  Shape: [0]  DType: int8

A[Slice(1,3)]
[[[     33      65      125     -35     ]
[     -65     123     57      64      ]
[     38      -110    33      98      ]
[     -59     -17     68      -6      ]]
[[     -68     -58     -37     -86     ]
[     -4      101     104     -113    ]
[     103     1       4       -47     ]
[     124     -2      -60     -105    ]]]
3-D array  Shape: [2, 4, 4]  DType: int8

A[1, Slice(2,4)]
[[      38      -110    33      98      ]
[      -59     -17     68      -6      ]]
2-D array  Shape: [2, 4]  DType: int8

A[Slice(1,3), Slice(1,3), 2]
[[      57      33      ]
[      104     4       ]]
2-D array  Shape: [2, 2]  DType: int8

A.item(0,1,2) as Scalar
-105
```


```Mojo
__getitem__(self, index: List[Int]) -> Self
```  
Summary  
  
Get items of array from a list of indices.  
  
Args:  

- self
- index: List[Int].


It always gets the first dimension.

Example:
```console
> var A = nm.NDArray[nm.i8](3,random=True)
> print(A)
[       14      97      -59     ]
1-D array  Shape: [3]  DType: int8
>
> print(A[List[Int](2,1,0,1,2)])
[       -59     97      14      97      -59     ]
1-D array  Shape: [5]  DType: int8
>
> var B = nm.NDArray[nm.i8](3, 3,random=True)
> print(B)
[[      -4      112     -94     ]
[      -48     -40     66      ]
[      -2      -94     -18     ]]
2-D array  Shape: [3, 3]  DType: int8
>
> print(B[List[Int](2,1,0,1,2)])
[[      -2      -94     -18     ]
[      -48     -40     66      ]
[      -4      112     -94     ]
[      -48     -40     66      ]
[      -2      -94     -18     ]]
2-D array  Shape: [5, 3]  DType: int8
>
> var C = nm.NDArray[nm.i8](3, 3, 3, random=True)
> print(C)
[[[     -126    -88     -79     ]
[     14      78      99      ]
[     -32     3       -42     ]]
[[     56      -45     -71     ]
[     -13     18      -102    ]
[     4       83      26      ]]
[[     61      -73     86      ]
[     -125    -84     66      ]
[     32      21      53      ]]]
3-D array  Shape: [3, 3, 3]  DType: int8
>
> print(C[List[Int](2,1,0,1,2)])
[[[     61      -73     86      ]
[     -125    -84     66      ]
[     32      21      53      ]]
[[     56      -45     -71     ]
[     -13     18      -102    ]
[     4       83      26      ]]
[[     -126    -88     -79     ]
[     14      78      99      ]
[     -32     3       -42     ]]
[[     56      -45     -71     ]
[     -13     18      -102    ]
[     4       83      26      ]]
[[     61      -73     86      ]
[     -125    -84     66      ]
[     32      21      53      ]]]
3-D array  Shape: [5, 3, 3]  DType: int8
```


```Mojo
__getitem__(self, index: NDArray[index]) -> Self
```  
Summary  
  
Get items of array from an array of indices.  
  
Args:  

- self
- index


Refer to `__getitem__(self, index: List[Int])`.

Example:
```console
> var X = nm.NDArray[nm.i8](3,random=True)
> print(X)
[       32      21      53      ]
1-D array  Shape: [3]  DType: int8
> print(X.argsort())
[       1       0       2       ]
1-D array  Shape: [3]  DType: index
> print(X[X.argsort()])
[       21      32      53      ]
1-D array  Shape: [3]  DType: int8
```

```Mojo
__getitem__(self, mask: NDArray[bool]) -> Self
```  
Summary  
  
Get items of array corresponding to a mask.  
  
Args:  

- self
- mask: NDArray with Dtype.bool.


Example:
    ```
    var A = numojo.core.NDArray[numojo.i16](6, random=True)
    var mask = A > 0
    print(A)
    print(mask)
    print(A[mask])
    ```

#### __setitem__


```Mojo
__setitem__(mut self, idx: Int, val: Self)
```  
Summary  
  
Set a slice of array with given array.  
  
Args:  

- self
- idx
- val


Example:
    `arr[1]` returns the second row of the array.

```Mojo
__setitem__(mut self, index: Idx, val: SIMD[dtype, 1])
```  
Summary  
  
Set the value at the index list.  
  
Args:  

- self
- index
- val


```Mojo
__setitem__(mut self, owned *slices: Slice, *, val: Self)
```  
Summary  
  
Retreive slices of an array from variadic slices.  
  
Args:  

- self
- \*slices
- val


Example:
    `arr[1:3, 2:4]` returns the corresponding sliced array (2 x 2).

```Mojo
__setitem__(mut self, owned slices: List[Slice], val: Self)
```  
Summary  
  
Sets the slices of an array from list of slices and array.  
  
Args:  

- self
- slices
- val


Example:
    `arr[1:3, 2:4]` returns the corresponding sliced array (2 x 2).

```Mojo
__setitem__(self, index: NDArray[index], val: NDArray[dtype])
```  
Summary  
  
Returns the items of the array from an array of indices.  
  
Args:  

- self
- index
- val


Refer to `__getitem__(self, index: List[Int])`.

Example:
```console
> var X = nm.NDArray[nm.i8](3,random=True)
> print(X)
[       32      21      53      ]
1-D array  Shape: [3]  DType: int8
> print(X.argsort())
[       1       0       2       ]
1-D array  Shape: [3]  DType: index
> print(X[X.argsort()])
[       21      32      53      ]
1-D array  Shape: [3]  DType: int8
```

```Mojo
__setitem__(mut self, mask: NDArray[bool], val: Self)
```  
Summary  
  
Set the value of the array at the indices where the mask is true.  
  
Args:  

- self
- mask
- val


Example:
```
var A = numojo.core.NDArray[numojo.i16](6, random=True)
var mask = A > 0
print(A)
print(mask)
A[mask] = 0
print(A)
```
#### __neg__


```Mojo
__neg__(self) -> Self
```  
Summary  
  
Unary negative returens self unless boolean type.  
  
Args:  

- self


For bolean use `__invert__`(~)
#### __pos__


```Mojo
__pos__(self) -> Self
```  
Summary  
  
Unary positve returens self unless boolean type.  
  
Args:  

- self

#### __invert__


```Mojo
__invert__(self) -> Self
```  
Summary  
  
Elementwise inverse (~ or not), only for bools and integral types.  
  
Args:  

- self

#### __lt__


```Mojo
__lt__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than.  
  
Args:  

- self
- other


```Mojo
__lt__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise less than between scalar and Array.  
  
Args:  

- self
- other

#### __le__


```Mojo
__le__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to.  
  
Args:  

- self
- other


```Mojo
__le__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to between scalar and Array.  
  
Args:  

- self
- other

#### __eq__


```Mojo
__eq__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise equivelence.  
  
Args:  

- self
- other


```Mojo
__eq__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise equivelence between scalar and Array.  
  
Args:  

- self
- other

#### __ne__


```Mojo
__ne__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise nonequivelence.  
  
Args:  

- self
- other


```Mojo
__ne__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise nonequivelence between scalar and Array.  
  
Args:  

- self
- other

#### __gt__


```Mojo
__gt__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than.  
  
Args:  

- self
- other


```Mojo
__gt__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than between scalar and Array.  
  
Args:  

- self
- other

#### __ge__


```Mojo
__ge__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than or equal to.  
  
Args:  

- self
- other


```Mojo
__ge__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to between scalar and Array.  
  
Args:  

- self
- other

#### __add__


```Mojo
__add__(mut self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array + scalar`.  
  
Args:  

- self
- other


```Mojo
__add__(mut self, other: Self) -> Self
```  
Summary  
  
Enables `array + array`.  
  
Args:  

- self
- other

#### __sub__


```Mojo
__sub__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array - scalar`.  
  
Args:  

- self
- other


```Mojo
__sub__(self, other: Self) -> Self
```  
Summary  
  
Enables `array - array`.  
  
Args:  

- self
- other

#### __mul__


```Mojo
__mul__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array * scalar`.  
  
Args:  

- self
- other


```Mojo
__mul__(self, other: Self) -> Self
```  
Summary  
  
Enables `array * array`.  
  
Args:  

- self
- other

#### __matmul__


```Mojo
__matmul__(self, other: Self) -> Self
```  
Summary  
  
  
  
Args:  

- self
- other

#### __truediv__


```Mojo
__truediv__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array / scalar`.  
  
Args:  

- self
- other


```Mojo
__truediv__(self, other: Self) -> Self
```  
Summary  
  
Enables `array / array`.  
  
Args:  

- self
- other

#### __floordiv__


```Mojo
__floordiv__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array // scalar`.  
  
Args:  

- self
- other


```Mojo
__floordiv__(self, other: Self) -> Self
```  
Summary  
  
Enables `array // array`.  
  
Args:  

- self
- other

#### __mod__


```Mojo
__mod__(mut self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array % scalar`.  
  
Args:  

- self
- other


```Mojo
__mod__(mut self, other: Self) -> Self
```  
Summary  
  
Enables `array % array`.  
  
Args:  

- self
- other

#### __pow__


```Mojo
__pow__(self, p: Int) -> Self
```  
Summary  
  
  
  
Args:  

- self
- p


```Mojo
__pow__(self, p: Self) -> Self
```  
Summary  
  
  
  
Args:  

- self
- p

#### __radd__


```Mojo
__radd__(mut self, rhs: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar + array`.  
  
Args:  

- self
- rhs

#### __rsub__


```Mojo
__rsub__(self, s: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar - array`.  
  
Args:  

- self
- s

#### __rmul__


```Mojo
__rmul__(self, s: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar * array`.  
  
Args:  

- self
- s

#### __rtruediv__


```Mojo
__rtruediv__(self, s: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar / array`.  
  
Args:  

- self
- s

#### __rfloordiv__


```Mojo
__rfloordiv__(self, s: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar // array`.  
  
Args:  

- self
- s

#### __rmod__


```Mojo
__rmod__(mut self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar % array`.  
  
Args:  

- self
- other

#### __iadd__


```Mojo
__iadd__(mut self, other: SIMD[dtype, 1])
```  
Summary  
  
Enables `array += scalar`.  
  
Args:  

- self
- other


```Mojo
__iadd__(mut self, other: Self)
```  
Summary  
  
Enables `array *= array`.  
  
Args:  

- self
- other

#### __isub__


```Mojo
__isub__(mut self, s: SIMD[dtype, 1])
```  
Summary  
  
Enables `array -= scalar`.  
  
Args:  

- self
- s


```Mojo
__isub__(mut self, s: Self)
```  
Summary  
  
Enables `array -= array`.  
  
Args:  

- self
- s

#### __imul__


```Mojo
__imul__(mut self, s: SIMD[dtype, 1])
```  
Summary  
  
Enables `array *= scalar`.  
  
Args:  

- self
- s


```Mojo
__imul__(mut self, s: Self)
```  
Summary  
  
Enables `array *= array`.  
  
Args:  

- self
- s

#### __itruediv__


```Mojo
__itruediv__(mut self, s: SIMD[dtype, 1])
```  
Summary  
  
Enables `array /= scalar`.  
  
Args:  

- self
- s


```Mojo
__itruediv__(mut self, other: Self)
```  
Summary  
  
Enables `array /= array`.  
  
Args:  

- self
- other

#### __ifloordiv__


```Mojo
__ifloordiv__(mut self, s: SIMD[dtype, 1])
```  
Summary  
  
Enables `array //= scalar`.  
  
Args:  

- self
- s


```Mojo
__ifloordiv__(mut self, other: Self)
```  
Summary  
  
Enables `array //= array`.  
  
Args:  

- self
- other

#### __imod__


```Mojo
__imod__(mut self, other: SIMD[dtype, 1])
```  
Summary  
  
Enables `array %= scalar`.  
  
Args:  

- self
- other


```Mojo
__imod__(mut self, other: Self)
```  
Summary  
  
Enables `array %= array`.  
  
Args:  

- self
- other

#### __ipow__


```Mojo
__ipow__(mut self, p: Int)
```  
Summary  
  
  
  
Args:  

- self
- p

#### set


```Mojo
set(self, index: Int, val: SIMD[dtype, 1])
```  
Summary  
  
Linearly retreive a value from the underlying Pointer.  
  
Args:  

- self
- index
- val


Example:
```console
> Array.get(15)
```
returns the item of index 15 from the array's data buffer.

Not that it is different from `item()` as `get` does not checked
against C-order or F-order.
```console
> # A is a 3x3 matrix, F-order (column-major)
> A.get(3)  # Row 0, Col 1
> A.item(3)  # Row 1, Col 0
```
#### get


```Mojo
get(self, index: Int) -> SIMD[dtype, 1]
```  
Summary  
  
Linearly retreive a value from the underlying Pointer.  
  
Args:  

- self
- index


Example:
```console
> Array.get(15)
```
returns the item of index 15 from the array's data buffer.

Not that it is different from `item()` as `get` does not checked
against C-order or F-order.
```console
> # A is a 3x3 matrix, F-order (column-major)
> A.get(3)  # Row 0, Col 1
> A.item(3)  # Row 1, Col 0
```
#### __int__


```Mojo
__int__(self) -> Int
```  
Summary  
  
Get Int representation of the array.  
  
Args:  

- self


Similar to Numpy, only 0-D arrays or length-1 arrays can be converted to
scalars.

Example:
```console
> var A = NDArray[dtype](6, random=True)
> print(int(A))

Unhandled exception caught during execution: Only 0-D arrays or length-1 arrays can be converted to scalars
mojo: error: execution exited with a non-zero result: 1

> var B = NDArray[dtype](1, 1, random=True)
> print(int(B))
14
```

#### __abs__


```Mojo
__abs__(self) -> Self
```  
Summary  
  
  
  
Args:  

- self

#### __str__


```Mojo
__str__(self) -> String
```  
Summary  
  
Enables str(array).  
  
Args:  

- self

#### write_to


```Mojo
write_to[W: Writer](self, mut writer: W)
```  
Summary  
  
  
  
Parameters:  

- W
  
Args:  

- self
- writer

#### __repr__


```Mojo
__repr__(self) -> String
```  
Summary  
  
Compute the "official" string representation of NDArray.  
  
Args:  

- self


Example:

```Mojo
fn main() raises:
    var A = NDArray[DType.int8](List[Scalar[DType.int8]](14,97,-59,-4,112,), shape=List[Int](5,))
    print(repr(A))
```

It prints what can be used to construct the array itself:

```console
NDArray[DType.int8](List[Scalar[DType.int8]](14,97,-59,-4,112,), shape=List[Int](5,))
```
#### __len__


```Mojo
__len__(self) -> Int
```  
Summary  
  
  
  
Args:  

- self

#### __iter__


```Mojo
__iter__(self) -> _NDArrayIter[self, dtype]
```  
Summary  
  
Iterate over elements of the NDArray, returning copied value.  
  
Args:  

- self


Notes:
    Need to add lifetimes after the new release.
#### __reversed__


```Mojo
__reversed__(self) -> _NDArrayIter[self, dtype, False]
```  
Summary  
  
Iterate backwards over elements of the NDArray, returning copied value.  
  
Args:  

- self

#### vdot


```Mojo
vdot(self, other: Self) -> SIMD[dtype, 1]
```  
Summary  
  
Inner product of two vectors.  
  
Args:  

- self
- other

#### mdot


```Mojo
mdot(self, other: Self) -> Self
```  
Summary  
  
Dot product of two matrix. Matrix A: M * N. Matrix B: N * L.  
  
Args:  

- self
- other

#### row


```Mojo
row(self, id: Int) -> Self
```  
Summary  
  
Get the ith row of the matrix.  
  
Args:  

- self
- id

#### col


```Mojo
col(self, id: Int) -> Self
```  
Summary  
  
Get the ith column of the matrix.  
  
Args:  

- self
- id

#### rdot


```Mojo
rdot(self, other: Self) -> Self
```  
Summary  
  
Dot product of two matrix. Matrix A: M * N. Matrix B: N * L.  
  
Args:  

- self
- other

#### num_elements


```Mojo
num_elements(self) -> Int
```  
Summary  
  
Function to retreive size (compatability).  
  
Args:  

- self

#### load


```Mojo
load[width: Int = 1](self, index: Int) -> SIMD[dtype, width]
```  
Summary  
  
Loads a SIMD element of size `width` at the given index `index`.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- index


```Mojo
load[width: Int = 1](self, *index: Int) -> SIMD[dtype, width]
```  
Summary  
  
Loads a SIMD element of size `width` at given variadic indices argument.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- \*index

#### store


```Mojo
store[width: Int](mut self, index: Int, val: SIMD[dtype, width])
```  
Summary  
  
Stores the SIMD element of size `width` at index `index`.  
  
Parameters:  

- width
  
Args:  

- self
- index
- val


```Mojo
store[width: Int = 1](mut self, *index: Int, *, val: SIMD[dtype, width])
```  
Summary  
  
Stores the SIMD element of size `width` at the given variadic indices argument.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- \*index
- val

#### T


```Mojo
T(self, axes: List[Int]) -> Self
```  
Summary  
  
Transpose array of any number of dimensions according to arbitrary permutation of the axes.  
  
Args:  

- self
- axes


If `axes` is not given, it is equal to flipping the axes.

Defined in `numojo.routines.manipulation.transpose`.

```Mojo
T(self) -> Self
```  
Summary  
  
(overload) Transpose the array when `axes` is not given. If `axes` is not given, it is equal to flipping the axes. See docstring of `transpose`.  
  
Args:  

- self


Defined in `numojo.routines.manipulation.transpose`.
#### all


```Mojo
all(self) -> Bool
```  
Summary  
  
If all true return true.  
  
Args:  

- self

#### any


```Mojo
any(self) -> Bool
```  
Summary  
  
True if any true.  
  
Args:  

- self

#### argmax


```Mojo
argmax(self) -> Int
```  
Summary  
  
Get location in pointer of max value.  
  
Args:  

- self

#### argmin


```Mojo
argmin(self) -> Int
```  
Summary  
  
Get location in pointer of min value.  
  
Args:  

- self

#### argsort


```Mojo
argsort(self) -> NDArray[index]
```  
Summary  
  
Sort the NDArray and return the sorted indices.  
  
Args:  

- self


See `numojo.routines.sorting.argsort()`.

#### astype


```Mojo
astype[type: DType](self) -> NDArray[type]
```  
Summary  
  
Convert type of array.  
  
Parameters:  

- type
  
Args:  

- self

#### cumprod


```Mojo
cumprod(self) -> SIMD[dtype, 1]
```  
Summary  
  
Cumulative product of a array.  
  
Args:  

- self

#### cumsum


```Mojo
cumsum(self) -> SIMD[dtype, 1]
```  
Summary  
  
Cumulative Sum of a array.  
  
Args:  

- self

#### diagonal


```Mojo
diagonal(self)
```  
Summary  
  
  
  
Args:  

- self

#### fill


```Mojo
fill(mut self, val: SIMD[dtype, 1])
```  
Summary  
  
Fill all items of array with value.  
  
Args:  

- self
- val

#### flatten


```Mojo
flatten(mut self)
```  
Summary  
  
Convert shape of array to one dimensional.  
  
Args:  

- self

#### item


```Mojo
item(self, *index: Int) -> SIMD[dtype, 1]
```  
Summary  
  
Return the scalar at the coordinates.  
  
Args:  

- self
- \*index: The coordinates of the item.


If one index is given, get the i-th item of the array.
It first scans over the first row, even it is a colume-major array.

If more than one index is given, the length of the indices must match
the number of dimensions of the array.

Example:
```console
> var A = nm.NDArray[dtype](3, 3, random=True, order="F")
> print(A)
[[      14      -4      -48     ]
[      97      112     -40     ]
[      -59     -94     66      ]]
2-D array  Shape: [3, 3]  DType: int8

> for i in A:
>     print(i)  # Return rows
[       14      -4      -48     ]
1-D array  Shape: [3]  DType: int8
[       97      112     -40     ]
1-D array  Shape: [3]  DType: int8
[       -59     -94     66      ]
1-D array  Shape: [3]  DType: int8

> for i in range(A.size()):
>    print(A.item(i))  # Return 0-d arrays
c strides Stride: [3, 1]
14
c strides Stride: [3, 1]
-4
c strides Stride: [3, 1]
-48
c strides Stride: [3, 1]
97
c strides Stride: [3, 1]
112
c strides Stride: [3, 1]
-40
c strides Stride: [3, 1]
-59
c strides Stride: [3, 1]
-94
c strides Stride: [3, 1]
66
==============================
```

#### itemset


```Mojo
itemset(mut self, index: Variant[Int, List[Int]], item: SIMD[dtype, 1])
```  
Summary  
  
Set the scalar at the coordinates.  
  
Args:  

- self
- index: The coordinates of the item. Can either be `Int` or `List[Int]`. If `Int` is passed, it is the index of i-th item of the whole array. If `List[Int]` is passed, it is the coordinate of the item.
- item: The scalar to be set.


Note:
    This is similar to `numpy.ndarray.itemset`.
    The difference is that we takes in `List[Int]`, but numpy takes in a tuple.

An example goes as follows.

```
import numojo as nm

fn main() raises:
    var A = nm.zeros[nm.i16](3, 3)
    print(A)
    A.itemset(5, 256)
    print(A)
    A.itemset(List(1,1), 1024)
    print(A)
```
```console
[[      0       0       0       ]
 [      0       0       0       ]
 [      0       0       0       ]]
2-D array  Shape: [3, 3]  DType: int16
[[      0       0       0       ]
 [      0       0       256     ]
 [      0       0       0       ]]
2-D array  Shape: [3, 3]  DType: int16
[[      0       0       0       ]
 [      0       1024    256     ]
 [      0       0       0       ]]
2-D array  Shape: [3, 3]  DType: int16
```
#### max


```Mojo
max(self, axis: Int = 0) -> Self
```  
Summary  
  
Max on axis.  
  
Args:  

- self
- axis Default: 0

#### min


```Mojo
min(self, axis: Int = 0) -> Self
```  
Summary  
  
Min on axis.  
  
Args:  

- self
- axis Default: 0

#### mean


```Mojo
mean(self, axis: Int) -> Self
```  
Summary  
  
Mean of array elements over a given axis. Args:     array: NDArray.     axis: The axis along which the mean is performed. Returns:     An NDArray.  
  
Args:  

- self
- axis


```Mojo
mean(self) -> SIMD[dtype, 1]
```  
Summary  
  
Cumulative mean of a array.  
  
Args:  

- self

#### prod


```Mojo
prod(self, axis: Int) -> Self
```  
Summary  
  
Product of array elements over a given axis. Args:     array: NDArray.     axis: The axis along which the product is performed. Returns:     An NDArray.  
  
Args:  

- self
- axis

#### round


```Mojo
round(self) -> Self
```  
Summary  
  
Rounds the elements of the array to a whole number.  
  
Args:  

- self

#### sort


```Mojo
sort(mut self)
```  
Summary  
  
Sort NDArray using quick sort method. It is not guaranteed to be unstable.  
  
Args:  

- self


When no axis is given, the array is flattened before sorting.

See `numojo.sorting.sort` for more information.

```Mojo
sort(mut self, owned axis: Int)
```  
Summary  
  
Sort NDArray along the given axis using quick sort method. It is not guaranteed to be unstable.  
  
Args:  

- self
- axis


When no axis is given, the array is flattened before sorting.

See `numojo.sorting.sort` for more information.
#### sum


```Mojo
sum(self, axis: Int) -> Self
```  
Summary  
  
Sum of array elements over a given axis. Args:     axis: The axis along which the sum is performed. Returns:     An NDArray.  
  
Args:  

- self
- axis

#### tolist


```Mojo
tolist(self) -> List[SIMD[dtype, 1]]
```  
Summary  
  
Convert NDArray to a 1-D List.  
  
Args:  

- self

#### trace


```Mojo
trace(self, offset: Int = 0, axis1: Int = 0, axis2: Int = 1) -> Self
```  
Summary  
  
Computes the trace of a ndarray.  
  
Args:  

- self
- offset: Offset of the diagonal from the main diagonal. Default: 0
- axis1: First axis. Default: 0
- axis2: Second axis. Default: 1

#### reshape


```Mojo
reshape(mut self, *shape: Int, *, order: String = String("C"))
```  
Summary  
  
Reshapes the NDArray to given Shape.  
  
Args:  

- self
- \*shape: Variadic list of shape.
- order: Order of the array - Row major `C` or Column major `F`. Default: String("C")

#### unsafe_ptr


```Mojo
unsafe_ptr(self) -> UnsafePointer[SIMD[dtype, 1]]
```  
Summary  
  
Retreive pointer without taking ownership.  
  
Args:  

- self

#### to_numpy


```Mojo
to_numpy(self) -> PythonObject
```  
Summary  
  
Convert to a numpy array.  
  
Args:  

- self
