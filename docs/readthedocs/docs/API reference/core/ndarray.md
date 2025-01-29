



# ndarray

##  Module Summary
  
Implements basic object methods for working with N-Dimensional Array.
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
* flags `Dict[String, Bool]`  
    - Information about the memory layout of the array.  

### Functions

#### __init__


```rust
__init__(out self, shape: NDArrayShape, order: String = String("C"))
```  
Summary  
  
Initialize an NDArray with given shape.  
  
Args:  

- self
- shape: Variadic shape.
- order: Memory order C or F. Default: String("C")


```rust
__init__(out self, shape: List[Int], order: String = String("C"))
```  
Summary  
  
(Overload) Initialize an NDArray with given shape (list of integers).  
  
Args:  

- self
- shape: List of shape.
- order: Memory order C or F. Default: String("C")


```rust
__init__(out self, shape: VariadicList[Int], order: String = String("C"))
```  
Summary  
  
(Overload) Initialize an NDArray with given shape (variadic list of integers).  
  
Args:  

- self
- shape: Variadic List of shape.
- order: Memory order C or F. Default: String("C")


```rust
__init__(out self, shape: List[Int], offset: Int, strides: List[Int])
```  
Summary  
  
Extremely specific NDArray initializer.  
  
Args:  

- self
- shape
- offset
- strides


```rust
__init__(out self, shape: NDArrayShape, ref buffer: UnsafePointer[SIMD[dtype, 1]], offset: Int, strides: NDArrayStrides)
```  
Summary  
  
  
  
Args:  

- self
- shape
- buffer
- offset
- strides

#### __copyinit__


```rust
__copyinit__(out self, other: Self)
```  
Summary  
  
Copy other into self.  
  
Args:  

- self
- other

#### __moveinit__


```rust
__moveinit__(out self, owned existing: Self)
```  
Summary  
  
Move other into self.  
  
Args:  

- self
- existing

#### __del__


```rust
__del__(owned self)
```  
Summary  
  
  
  
Args:  

- self

#### __bool__


```rust
__bool__(self) -> Bool
```  
Summary  
  
If all true return true.  
  
Args:  

- self

#### __getitem__


```rust
__getitem__(self, index: Item) -> SIMD[dtype, 1]
```  
Summary  
  
Set the value at the index list.  
  
Args:  

- self
- index


```rust
__getitem__(self, idx: Int) -> Self
```  
Summary  
  
Retreive a slice of the array corresponding to the index at the first dimension.  
  
Args:  

- self
- idx


```rust
__getitem__(self, owned *slices: Slice) -> Self
```  
Summary  
  
Retreive slices of an array from variadic slices.  
  
Args:  

- self
- \*slices


```rust
__getitem__(self, owned slice_list: List[Slice]) -> Self
```  
Summary  
  
Retreive slices of an array from list of slices.  
  
Args:  

- self
- slice_list


```rust
__getitem__(self, owned *slices: Variant[Slice, Int]) -> Self
```  
Summary  
  
Get items by a series of either slices or integers.  
  
Args:  

- self
- \*slices: A series of either Slice or Int.


```rust
__getitem__(self, indices: NDArray[index]) -> Self
```  
Summary  
  
Get items from 0-th dimension of an ndarray of indices.  
  
Args:  

- self
- indices: Array of intable values.


```rust
__getitem__(self, indices: List[Int]) -> Self
```  
Summary  
  
Get items from 0-th dimension of an array. It is an overload of `__getitem__(self, indices: NDArray[DType.index]) raises -> Self`.  
  
Args:  

- self
- indices: A list of Int.


```rust
__getitem__(self, mask: NDArray[bool]) -> Self
```  
Summary  
  
Get item from an array according to a mask array.  
  
Args:  

- self
- mask: NDArray with Dtype.bool.


```rust
__getitem__(self, mask: List[Bool]) -> Self
```  
Summary  
  
Get items from 0-th dimension of an array according to mask. __getitem__(self, mask: NDArray[DType.bool]) raises -> Self.  
  
Args:  

- self
- mask: A list of boolean values.

#### __setitem__


```rust
__setitem__(mut self, idx: Int, val: Self)
```  
Summary  
  
Set a slice of array with given array.  
  
Args:  

- self
- idx
- val


```rust
__setitem__(mut self, index: Item, val: SIMD[dtype, 1])
```  
Summary  
  
Set the value at the index list.  
  
Args:  

- self
- index
- val


```rust
__setitem__(mut self, mask: NDArray[bool], value: SIMD[dtype, 1])
```  
Summary  
  
Set the value of the array at the indices where the mask is true.  
  
Args:  

- self
- mask
- value


```rust
__setitem__(mut self, *slices: Slice, *, val: Self)
```  
Summary  
  
Retreive slices of an array from variadic slices.  
  
Args:  

- self
- \*slices
- val


```rust
__setitem__(mut self, slices: List[Slice], val: Self)
```  
Summary  
  
Sets the slices of an array from list of slices and array.  
  
Args:  

- self
- slices
- val


```rust
__setitem__(mut self, *slices: Variant[Slice, Int], *, val: Self)
```  
Summary  
  
Get items by a series of either slices or integers.  
  
Args:  

- self
- \*slices
- val


```rust
__setitem__(self, index: NDArray[index], val: NDArray[dtype])
```  
Summary  
  
Returns the items of the array from an array of indices.  
  
Args:  

- self
- index
- val


```rust
__setitem__(mut self, mask: NDArray[bool], val: Self)
```  
Summary  
  
Set the value of the array at the indices where the mask is true.  
  
Args:  

- self
- mask
- val

#### __neg__


```rust
__neg__(self) -> Self
```  
Summary  
  
Unary negative returns self unless boolean type.  
  
Args:  

- self

#### __pos__


```rust
__pos__(self) -> Self
```  
Summary  
  
Unary positve returns self unless boolean type.  
  
Args:  

- self

#### __invert__


```rust
__invert__(self) -> Self
```  
Summary  
  
Element-wise inverse (~ or not), only for bools and integral types.  
  
Args:  

- self

#### __lt__


```rust
__lt__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than.  
  
Parameters:  

- OtherDtype
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__lt__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDtype]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than between scalar and Array.  
  
Parameters:  

- OtherDtype
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__lt__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than.  
  
Args:  

- self
- other


```rust
__lt__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise less than between scalar and Array.  
  
Args:  

- self
- other

#### __le__


```rust
__le__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to.  
  
Parameters:  

- OtherDtype
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__le__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDtype]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to between scalar and Array.  
  
Parameters:  

- OtherDtype
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__le__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to.  
  
Args:  

- self
- other


```rust
__le__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to between scalar and Array.  
  
Args:  

- self
- other

#### __eq__


```rust
__eq__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDtype]) -> NDArray[bool]
```  
Summary  
  
Itemwise equivalence.  
  
Parameters:  

- OtherDtype
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__eq__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise equivalence.  
  
Parameters:  

- OtherDtype
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__eq__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise equivalence.  
  
Args:  

- self
- other


```rust
__eq__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise equivalence between scalar and Array.  
  
Args:  

- self
- other

#### __ne__


```rust
__ne__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDtype]) -> NDArray[bool]
```  
Summary  
  
Itemwise nonequivelence.  
  
Parameters:  

- OtherDtype
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__ne__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise nonequivelence between scalar and Array.  
  
Parameters:  

- OtherDtype
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__ne__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise nonequivelence.  
  
Args:  

- self
- other


```rust
__ne__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise nonequivelence between scalar and Array.  
  
Args:  

- self
- other

#### __gt__


```rust
__gt__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than.  
  
Parameters:  

- OtherDtype
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__gt__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDtype]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than between scalar and Array.  
  
Parameters:  

- OtherDtype
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__gt__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than.  
  
Args:  

- self
- other


```rust
__gt__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than between scalar and Array.  
  
Args:  

- self
- other

#### __ge__


```rust
__ge__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than or equal to.  
  
Parameters:  

- OtherDtype
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__ge__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDtype]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to between scalar and Array.  
  
Parameters:  

- OtherDtype
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__ge__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than or equal to.  
  
Args:  

- self
- other


```rust
__ge__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to between scalar and Array.  
  
Args:  

- self
- other

#### __add__


```rust
__add__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `array + scalar`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__add__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDType]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `array + array`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__add__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array + scalar`.  
  
Args:  

- self
- other


```rust
__add__(self, other: Self) -> Self
```  
Summary  
  
Enables `array + array`.  
  
Args:  

- self
- other

#### __sub__


```rust
__sub__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `array - scalar`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__sub__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDType]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `array - array`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__sub__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array - scalar`.  
  
Args:  

- self
- other


```rust
__sub__(self, other: Self) -> Self
```  
Summary  
  
Enables `array - array`.  
  
Args:  

- self
- other

#### __mul__


```rust
__mul__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `array * scalar`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__mul__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDType]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `array * array`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__mul__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array * scalar`.  
  
Args:  

- self
- other


```rust
__mul__(self, other: Self) -> Self
```  
Summary  
  
Enables `array * array`.  
  
Args:  

- self
- other

#### __matmul__


```rust
__matmul__(self, other: Self) -> Self
```  
Summary  
  
  
  
Args:  

- self
- other

#### __truediv__


```rust
__truediv__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `array / scalar`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__truediv__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDType]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `array / array`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__truediv__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array / scalar`.  
  
Args:  

- self
- other


```rust
__truediv__(self, other: Self) -> Self
```  
Summary  
  
Enables `array / array`.  
  
Args:  

- self
- other

#### __floordiv__


```rust
__floordiv__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `array // scalar`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__floordiv__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDType]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `array // array`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__floordiv__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array // scalar`.  
  
Args:  

- self
- other


```rust
__floordiv__(self, other: Self) -> Self
```  
Summary  
  
Enables `array // array`.  
  
Args:  

- self
- other

#### __mod__


```rust
__mod__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `array % scalar`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__mod__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDType]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `array % array`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__mod__(mut self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array % scalar`.  
  
Args:  

- self
- other


```rust
__mod__(mut self, other: Self) -> Self
```  
Summary  
  
Enables `array % array`.  
  
Args:  

- self
- other

#### __pow__


```rust
__pow__(self, p: Int) -> Self
```  
Summary  
  
  
  
Args:  

- self
- p


```rust
__pow__(self, p: Self) -> Self
```  
Summary  
  
  
  
Args:  

- self
- p

#### __radd__


```rust
__radd__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `scalar + array`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__radd__(mut self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar + array`.  
  
Args:  

- self
- other

#### __rsub__


```rust
__rsub__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `scalar - array`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__rsub__(mut self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar - array`.  
  
Args:  

- self
- other

#### __rmul__


```rust
__rmul__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `scalar * array`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__rmul__(mut self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar * array`.  
  
Args:  

- self
- other

#### __rtruediv__


```rust
__rtruediv__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, s: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `scalar / array`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- s


```rust
__rtruediv__(self, s: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar / array`.  
  
Args:  

- self
- s

#### __rfloordiv__


```rust
__rfloordiv__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `scalar // array`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other


```rust
__rfloordiv__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar // array`.  
  
Args:  

- self
- other

#### __rmod__


```rust
__rmod__(mut self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar % array`.  
  
Args:  

- self
- other


```rust
__rmod__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `scalar % array`.  
  
Parameters:  

- OtherDType
- ResultDType Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other

#### __iadd__


```rust
__iadd__(mut self, other: SIMD[dtype, 1])
```  
Summary  
  
Enables `array += scalar`.  
  
Args:  

- self
- other


```rust
__iadd__(mut self, other: Self)
```  
Summary  
  
Enables `array *= array`.  
  
Args:  

- self
- other

#### __isub__


```rust
__isub__(mut self, other: SIMD[dtype, 1])
```  
Summary  
  
Enables `array -= scalar`.  
  
Args:  

- self
- other


```rust
__isub__(mut self, other: Self)
```  
Summary  
  
Enables `array -= array`.  
  
Args:  

- self
- other

#### __imul__


```rust
__imul__(mut self, other: SIMD[dtype, 1])
```  
Summary  
  
Enables `array *= scalar`.  
  
Args:  

- self
- other


```rust
__imul__(mut self, other: Self)
```  
Summary  
  
Enables `array *= array`.  
  
Args:  

- self
- other

#### __itruediv__


```rust
__itruediv__(mut self, s: SIMD[dtype, 1])
```  
Summary  
  
Enables `array /= scalar`.  
  
Args:  

- self
- s


```rust
__itruediv__(mut self, other: Self)
```  
Summary  
  
Enables `array /= array`.  
  
Args:  

- self
- other

#### __ifloordiv__


```rust
__ifloordiv__(mut self, s: SIMD[dtype, 1])
```  
Summary  
  
Enables `array //= scalar`.  
  
Args:  

- self
- s


```rust
__ifloordiv__(mut self, other: Self)
```  
Summary  
  
Enables `array //= array`.  
  
Args:  

- self
- other

#### __imod__


```rust
__imod__(mut self, other: SIMD[dtype, 1])
```  
Summary  
  
Enables `array %= scalar`.  
  
Args:  

- self
- other


```rust
__imod__(mut self, other: Self)
```  
Summary  
  
Enables `array %= array`.  
  
Args:  

- self
- other

#### __ipow__


```rust
__ipow__(mut self, p: Int)
```  
Summary  
  
  
  
Args:  

- self
- p

#### __int__


```rust
__int__(self) -> Int
```  
Summary  
  
Get Int representation of the array.  
  
Args:  

- self

#### __abs__


```rust
__abs__(self) -> Self
```  
Summary  
  
  
  
Args:  

- self

#### __str__


```rust
__str__(self) -> String
```  
Summary  
  
Enables str(array).  
  
Args:  

- self

#### write_to


```rust
write_to[W: Writer](self, mut writer: W)
```  
Summary  
  
  
  
Parameters:  

- W
  
Args:  

- self
- writer

#### __repr__


```rust
__repr__(self) -> String
```  
Summary  
  
Compute the "official" string representation of NDArray.  
  
Args:  

- self

#### __len__


```rust
__len__(self) -> Int
```  
Summary  
  
Returns length of 0-th dimension.  
  
Args:  

- self

#### __iter__


```rust
__iter__(self) -> _NDArrayIter[self, dtype]
```  
Summary  
  
Iterate over elements of the NDArray and return sub-arrays as view.  
  
Args:  

- self

#### __reversed__


```rust
__reversed__(self) -> _NDArrayIter[self, dtype, False]
```  
Summary  
  
Iterate backwards over elements of the NDArray, returning copied value.  
  
Args:  

- self

#### vdot


```rust
vdot(self, other: Self) -> SIMD[dtype, 1]
```  
Summary  
  
Inner product of two vectors.  
  
Args:  

- self
- other

#### mdot


```rust
mdot(self, other: Self) -> Self
```  
Summary  
  
Dot product of two matrix. Matrix A: M * N. Matrix B: N * L.  
  
Args:  

- self
- other

#### row


```rust
row(self, id: Int) -> Self
```  
Summary  
  
Get the ith row of the matrix.  
  
Args:  

- self
- id

#### col


```rust
col(self, id: Int) -> Self
```  
Summary  
  
Get the ith column of the matrix.  
  
Args:  

- self
- id

#### rdot


```rust
rdot(self, other: Self) -> Self
```  
Summary  
  
Dot product of two matrix. Matrix A: M * N. Matrix B: N * L.  
  
Args:  

- self
- other

#### num_elements


```rust
num_elements(self) -> Int
```  
Summary  
  
Function to retreive size (compatability).  
  
Args:  

- self

#### load


```rust
load(self, owned index: Int) -> SIMD[dtype, 1]
```  
Summary  
  
Safely retrieve i-th item from the underlying buffer.  
  
Args:  

- self
- index


```rust
load[width: Int = 1](self, index: Int) -> SIMD[dtype, width]
```  
Summary  
  
Safely loads a SIMD element of size `width` at `index` from the underlying buffer.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- index


```rust
load[width: Int = 1](self, *indices: Int) -> SIMD[dtype, width]
```  
Summary  
  
Safely loads SIMD element of size `width` at given variadic indices from the underlying buffer.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- \*indices

#### store


```rust
store(self, owned index: Int, val: SIMD[dtype, 1])
```  
Summary  
  
Safely store a scalar to i-th item of the underlying buffer.  
  
Args:  

- self
- index
- val


```rust
store[width: Int](mut self, index: Int, val: SIMD[dtype, width])
```  
Summary  
  
Safely stores SIMD element of size `width` at `index` of the underlying buffer.  
  
Parameters:  

- width
  
Args:  

- self
- index
- val


```rust
store[width: Int = 1](mut self, *indices: Int, *, val: SIMD[dtype, width])
```  
Summary  
  
Safely stores SIMD element of size `width` at given variadic indices of the underlying buffer.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- \*indices
- val

#### T


```rust
T(self, axes: List[Int]) -> Self
```  
Summary  
  
Transpose array of any number of dimensions according to arbitrary permutation of the axes.  
  
Args:  

- self
- axes


```rust
T(self) -> Self
```  
Summary  
  
(overload) Transpose the array when `axes` is not given. If `axes` is not given, it is equal to flipping the axes. See docstring of `transpose`.  
  
Args:  

- self

#### all


```rust
all(self) -> Bool
```  
Summary  
  
If all true return true.  
  
Args:  

- self

#### any


```rust
any(self) -> Bool
```  
Summary  
  
True if any true.  
  
Args:  

- self

#### argmax


```rust
argmax(self) -> Int
```  
Summary  
  
Get location in pointer of max value.  
  
Args:  

- self

#### argmin


```rust
argmin(self) -> Int
```  
Summary  
  
Get location in pointer of min value.  
  
Args:  

- self

#### argsort


```rust
argsort(self) -> NDArray[index]
```  
Summary  
  
Sort the NDArray and return the sorted indices.  
  
Args:  

- self

#### astype


```rust
astype[target: DType](self) -> NDArray[target]
```  
Summary  
  
Convert type of array.  
  
Parameters:  

- target
  
Args:  

- self

#### copy


```rust
copy(self) -> Self
```  
Summary  
  
Returns a copy of the array that owns the data. The returned array will be continuous in memory.  
  
Args:  

- self

#### cumprod


```rust
cumprod(self) -> Self
```  
Summary  
  
Returns cumprod of all items of an array. The array is flattened before cumprod.  
  
Args:  

- self


```rust
cumprod(self, axis: Int) -> Self
```  
Summary  
  
Returns cumprod of array by axis.  
  
Args:  

- self
- axis: Axis.

#### cumsum


```rust
cumsum(self) -> Self
```  
Summary  
  
Returns cumsum of all items of an array. The array is flattened before cumsum.  
  
Args:  

- self


```rust
cumsum(self, axis: Int) -> Self
```  
Summary  
  
Returns cumsum of array by axis.  
  
Args:  

- self
- axis: Axis.

#### diagonal


```rust
diagonal(self)
```  
Summary  
  
  
  
Args:  

- self

#### fill


```rust
fill(mut self, val: SIMD[dtype, 1])
```  
Summary  
  
Fill all items of array with value.  
  
Args:  

- self
- val

#### flatten


```rust
flatten(self, order: String = String("C")) -> Self
```  
Summary  
  
Return a copy of the array collapsed into one dimension.  
  
Args:  

- self
- order: A NDArray. Default: String("C")

#### item


```rust
item(self, owned index: Int) -> ref [MutableAnyOrigin] SIMD[dtype, 1]
```  
Summary  
  
Return the scalar at the coordinates.  
  
Args:  

- self
- index: Index of item, counted in row-major way.


```rust
item(self, *index: Int) -> ref [MutableAnyOrigin] SIMD[dtype, 1]
```  
Summary  
  
Return the scalar at the coordinates.  
  
Args:  

- self
- \*index: The coordinates of the item.

#### itemset


```rust
itemset(mut self, index: Variant[Int, List[Int]], item: SIMD[dtype, 1])
```  
Summary  
  
Set the scalar at the coordinates.  
  
Args:  

- self
- index: The coordinates of the item. Can either be `Int` or `List[Int]`. If `Int` is passed, it is the index of i-th item of the whole array. If `List[Int]` is passed, it is the coordinate of the item.
- item: The scalar to be set.

#### max


```rust
max(self, axis: Int = 0) -> Self
```  
Summary  
  
Max on axis.  
  
Args:  

- self
- axis Default: 0

#### min


```rust
min(self, axis: Int = 0) -> Self
```  
Summary  
  
Min on axis.  
  
Args:  

- self
- axis Default: 0

#### mean


```rust
mean(self, axis: Int) -> Self
```  
Summary  
  
Mean of array elements over a given axis. Args:     array: NDArray.     axis: The axis along which the mean is performed. Returns:     An NDArray.  
  
Args:  

- self
- axis


```rust
mean(self) -> SIMD[dtype, 1]
```  
Summary  
  
Cumulative mean of a array.  
  
Args:  

- self

#### nditer


```rust
nditer(self) -> _NDIter[self, dtype]
```  
Summary  
  
(Overload) Return an iterator yielding the array elements according to the memory layout of the array.  
  
Args:  

- self


```rust
nditer(self, order: String) -> _NDIter[self, dtype]
```  
Summary  
  
Return an iterator yielding the array elements according to the order.  
  
Args:  

- self
- order

#### prod


```rust
prod(self) -> SIMD[dtype, 1]
```  
Summary  
  
Product of all array elements. Returns:     Scalar.  
  
Args:  

- self


```rust
prod(self, axis: Int) -> Self
```  
Summary  
  
Product of array elements over a given axis. Args:     axis: The axis along which the product is performed. Returns:     An NDArray.  
  
Args:  

- self
- axis

#### reshape


```rust
reshape(self, shape: NDArrayShape, order: String = String("C")) -> Self
```  
Summary  
  
Returns an array of the same data with a new shape.  
  
Args:  

- self
- shape: Shape of returned array.
- order: Order of the array - Row major `C` or Column major `F`. Default: String("C")

#### resize


```rust
resize(mut self, shape: NDArrayShape)
```  
Summary  
  
In-place change shape and size of array.  
  
Args:  

- self
- shape: Shape after resize.

#### round


```rust
round(self) -> Self
```  
Summary  
  
Rounds the elements of the array to a whole number.  
  
Args:  

- self

#### sort


```rust
sort(mut self)
```  
Summary  
  
Sort NDArray using quick sort method. It is not guaranteed to be unstable.  
  
Args:  

- self


```rust
sort(mut self, owned axis: Int)
```  
Summary  
  
Sort NDArray along the given axis using quick sort method. It is not guaranteed to be unstable.  
  
Args:  

- self
- axis

#### sum


```rust
sum(self) -> SIMD[dtype, 1]
```  
Summary  
  
Sum of all array elements. Returns:     Scalar.  
  
Args:  

- self


```rust
sum(self, axis: Int) -> Self
```  
Summary  
  
Sum of array elements over a given axis. Args:     axis: The axis along which the sum is performed. Returns:     An NDArray.  
  
Args:  

- self
- axis

#### tolist


```rust
tolist(self) -> List[SIMD[dtype, 1]]
```  
Summary  
  
Convert NDArray to a 1-D List.  
  
Args:  

- self

#### to_numpy


```rust
to_numpy(self) -> PythonObject
```  
Summary  
  
Convert to a numpy array.  
  
Args:  

- self

#### to_tensor


```rust
to_tensor(self) -> Tensor[dtype]
```  
Summary  
  
Convert array to tensor of the same dtype.  
  
Args:  

- self

#### trace


```rust
trace(self, offset: Int = 0, axis1: Int = 0, axis2: Int = 1) -> Self
```  
Summary  
  
Computes the trace of a ndarray.  
  
Args:  

- self
- offset: Offset of the diagonal from the main diagonal. Default: 0
- axis1: First axis. Default: 0
- axis2: Second axis. Default: 1

#### unsafe_ptr


```rust
unsafe_ptr(self) -> UnsafePointer[SIMD[dtype, 1]]
```  
Summary  
  
Retreive pointer without taking ownership.  
  
Args:  

- self
