



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
- FloatableRaising
- IntableRaising
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
* flags `Flags`  
    - Information about the memory layout of the array.  

### Functions

#### __init__


```rust
__init__(out self, shape: NDArrayShape, order: String = String("C"))
```  
Summary  
  
Initializes an NDArray with given shape. The memory is not filled with values.  
  
Args:  

- shape: Variadic shape.
- order: Memory order C or F. Default: String("C")
- self


```rust
__init__(out self, shape: List[Int], order: String = String("C"))
```  
Summary  
  
(Overload) Initializes an NDArray with given shape (list of integers).  
  
Args:  

- shape: List of shape.
- order: Memory order C or F. Default: String("C")
- self


```rust
__init__(out self, shape: VariadicList[Int], order: String = String("C"))
```  
Summary  
  
(Overload) Initializes an NDArray with given shape (variadic list of integers).  
  
Args:  

- shape: Variadic List of shape.
- order: Memory order C or F. Default: String("C")
- self


```rust
__init__(out self, shape: List[Int], offset: Int, strides: List[Int])
```  
Summary  
  
Extremely specific NDArray initializer.  
  
Args:  

- shape: List of shape.
- offset: Offset value.
- strides: List of strides.
- self


```rust
__init__(out self, shape: NDArrayShape, strides: NDArrayStrides, ndim: Int, size: Int, flags: Flags)
```  
Summary  
  
Constructs an extremely specific array, with value uninitialized. The properties do not need to be compatible and are not checked. For example, it can construct a 0-D array (numojo scalar).  
  
Args:  

- shape: Shape of array.
- strides: Strides of array.
- ndim: Number of dimensions.
- size: Size of array.
- flags: Flags of array.
- self


```rust
__init__(out self, shape: NDArrayShape, ref buffer: UnsafePointer[SIMD[dtype, 1]], offset: Int, strides: NDArrayStrides)
```  
Summary  
  
Initialize an NDArray view with given shape, buffer, offset, and strides. ***Unsafe!*** This function is currently unsafe. Only for internal use.  
  
Args:  

- shape: Shape of the array.
- buffer: Unsafe pointer to the buffer.
- offset: Offset value.
- strides: Strides of the array.
- self

#### __copyinit__


```rust
__copyinit__(out self, other: Self)
```  
Summary  
  
Copy other into self. It is a deep copy. So the new array owns the data.  
  
Args:  

- other: The NDArray to copy from.
- self

#### __moveinit__


```rust
__moveinit__(out self, owned existing: Self)
```  
Summary  
  
Move other into self.  
  
Args:  

- existing: The NDArray to move from.
- self

#### __del__


```rust
__del__(owned self)
```  
Summary  
  
Destroys all elements in the list and free its memory.  
  
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
__getitem__(self) -> SIMD[dtype, 1]
```  
Summary  
  
Gets the value of the 0-D array.  
  
Args:  

- self


```rust
__getitem__(self, index: Item) -> SIMD[dtype, 1]
```  
Summary  
  
Get the value at the index list.  
  
Args:  

- self
- index: Index list.


```rust
__getitem__(self, idx: Int) -> Self
```  
Summary  
  
Retrieve a slice of the array corresponding to the index at the first dimension.  
  
Args:  

- self
- idx: Index to get the slice.


```rust
__getitem__(self, owned *slices: Slice) -> Self
```  
Summary  
  
Retrieve slices of an array from variadic slices.  
  
Args:  

- self
- \*slices: Variadic slices.


```rust
__getitem__(self, owned slice_list: List[Slice]) -> Self
```  
Summary  
  
Retrieve slices of an array from a list of slices.  
  
Args:  

- self
- slice_list: List of slices.


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
  
Get items from 0-th dimension of an ndarray of indices. If the original array is of shape (i,j,k) and the indices array is of shape (l, m, n), then the output array will be of shape (l,m,n,j,k).  
  
Args:  

- self
- indices: Array of indices.


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
  
Get item from an array according to a mask array. If array shape is equal to mask shape, it returns a flattened array of the values where mask is True. If array shape is not equal to mask shape, it returns items from the 0-th dimension of the array where mask is True.  
  
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
- idx: Index to set.
- val: Value to set.


```rust
__setitem__(mut self, index: Item, val: SIMD[dtype, 1])
```  
Summary  
  
Sets the value at the index list.  
  
Args:  

- self
- index: Index list.
- val: Value to set.


```rust
__setitem__(mut self, mask: NDArray[bool], value: SIMD[dtype, 1])
```  
Summary  
  
Sets the value of the array at the indices where the mask is true.  
  
Args:  

- self
- mask: Boolean mask array.
- value: Value to set.


```rust
__setitem__(mut self, *slices: Slice, *, val: Self)
```  
Summary  
  
Sets the elements of the array at the slices with given array.  
  
Args:  

- self
- \*slices: Variadic slices.
- val: A NDArray to set.


```rust
__setitem__(mut self, slices: List[Slice], val: Self)
```  
Summary  
  
Sets the slices of an array from list of slices and array.  
  
Args:  

- self
- slices: List of slices.
- val: Value to set.


```rust
__setitem__(mut self, *slices: Variant[Slice, Int], *, val: Self)
```  
Summary  
  
Gets items by a series of either slices or integers.  
  
Args:  

- self
- \*slices: Variadic slices or integers.
- val: Value to set.


```rust
__setitem__(self, index: NDArray[index], val: NDArray[dtype])
```  
Summary  
  
Returns the items of the array from an array of indices.  
  
Args:  

- self
- index: Array of indices.
- val: Value to set.


```rust
__setitem__(mut self, mask: NDArray[bool], val: Self)
```  
Summary  
  
Sets the value of the array at the indices where the mask is true.  
  
Args:  

- self
- mask: Boolean mask array.
- val: Value to set.

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

- OtherDtype: The data type of the other Scalar.
- ResultDType: The data type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other: The other Scalar to compare with.


```rust
__lt__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDtype]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than between scalar and Array.  
  
Parameters:  

- OtherDtype: The data type of the other array.
- ResultDType: The data type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other: The other array to compare with.


```rust
__lt__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than.  
  
Args:  

- self
- other: The other SIMD value to compare with.


```rust
__lt__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise less than between scalar and Array.  
  
Args:  

- self
- other: The other array to compare with.

#### __le__


```rust
__le__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to.  
  
Parameters:  

- OtherDtype: The data type of the other Scalar.
- ResultDType: The data type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other: The other Scalar to compare with.


```rust
__le__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDtype]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to between scalar and Array.  
  
Parameters:  

- OtherDtype: The data type of the other array.
- ResultDType: The data type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other: The other array to compare with.


```rust
__le__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to.  
  
Args:  

- self
- other: The other SIMD value to compare with.


```rust
__le__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to between scalar and Array.  
  
Args:  

- self
- other: The other array to compare with.

#### __eq__


```rust
__eq__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDtype]) -> NDArray[bool]
```  
Summary  
  
Itemwise equivalence.  
  
Parameters:  

- OtherDtype: The data type of the other array.
- ResultDType: The data type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other: The other array to compare with.


```rust
__eq__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise equivalence.  
  
Parameters:  

- OtherDtype: The data type of the other Scalar.
- ResultDType: The data type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other: The other Scalar to compare with.


```rust
__eq__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise equivalence.  
  
Args:  

- self
- other: The other array to compare with.


```rust
__eq__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise equivalence between scalar and Array.  
  
Args:  

- self
- other: The other SIMD value to compare with.

#### __ne__


```rust
__ne__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDtype]) -> NDArray[bool]
```  
Summary  
  
Itemwise nonequivelence.  
  
Parameters:  

- OtherDtype: The data type of the other array.
- ResultDType: The data type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other: The other array to compare with.


```rust
__ne__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise nonequivelence between scalar and Array.  
  
Parameters:  

- OtherDtype: The data type of the other Scalar.
- ResultDType: The data type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other: The other Scalar to compare with.


```rust
__ne__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise nonequivelence.  
  
Args:  

- self
- other: The other SIMD value to compare with.


```rust
__ne__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise nonequivelence between scalar and Array.  
  
Args:  

- self
- other: The other array to compare with.

#### __gt__


```rust
__gt__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than.  
  
Parameters:  

- OtherDtype: The data type of the other Scalar.
- ResultDType: The data type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other: The other Scalar to compare with.


```rust
__gt__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDtype]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than between scalar and Array.  
  
Parameters:  

- OtherDtype: The data type of the other array.
- ResultDType: The data type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other: The other array to compare with.


```rust
__gt__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than.  
  
Args:  

- self
- other: The other SIMD value to compare with.


```rust
__gt__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than between scalar and Array.  
  
Args:  

- self
- other: The other array to compare with.

#### __ge__


```rust
__ge__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than or equal to.  
  
Parameters:  

- OtherDtype: The data type of the other Scalar.
- ResultDType: The data type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other: The other Scalar to compare with.


```rust
__ge__[OtherDtype: DType, ResultDType: DType = result[::DType,::DType]()](self, other: NDArray[OtherDtype]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than or equal to between scalar and Array.  
  
Parameters:  

- OtherDtype: The data type of the other array.
- ResultDType: The data type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other: The other array to compare with.


```rust
__ge__(self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than or equal to.  
  
Args:  

- self
- other: The other SIMD value to compare with.


```rust
__ge__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than or equal to between Array and Array.  
  
Args:  

- self
- other: The other array to compare with.

#### __add__


```rust
__add__[OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](self, other: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Enables `array + scalar`.  
  
Parameters:  

- OtherDType: The data type of the other Scalar.
- ResultDType: The data type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- self
- other: The other Scalar to compare with.


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
__pow__(self, rhs: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Power of items.  
  
Args:  

- self
- rhs


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

#### item


```rust
item(self, owned index: Int) -> ref [MutableAnyOrigin] SIMD[dtype, 1]
```  
Summary  
  
Return the scalar at the coordinates. If one index is given, get the i-th item of the array (not buffer). It first scans over the first row, even it is a colume-major array. If more than one index is given, the length of the indices must match the number of dimensions of the array. If the ndim is 0 (0-D array), get the value as a mojo scalar.  
  
Args:  

- self
- index: Index of item, counted in row-major way.


```rust
item(self, *index: Int) -> ref [MutableAnyOrigin] SIMD[dtype, 1]
```  
Summary  
  
Return the scalar at the coordinates. If one index is given, get the i-th item of the array (not buffer). It first scans over the first row, even it is a colume-major array. If more than one index is given, the length of the indices must match the number of dimensions of the array. For 0-D array (numojo scalar), return the scalar value.  
  
Args:  

- self
- \*index: The coordinates of the item.

#### load


```rust
load(self, owned index: Int) -> SIMD[dtype, 1]
```  
Summary  
  
Safely retrieve i-th item from the underlying buffer.  
  
Args:  

- self
- index: Index of the item.


```rust
load[width: Int = 1](self, index: Int) -> SIMD[dtype, width]
```  
Summary  
  
Safely loads a SIMD element of size `width` at `index` from the underlying buffer.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- index: Index of the item.


```rust
load[width: Int = 1](self, *indices: Int) -> SIMD[dtype, width]
```  
Summary  
  
Safely loads SIMD element of size `width` at given variadic indices from the underlying buffer.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- \*indices: Variadic indices.

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

#### store


```rust
store(self, owned index: Int, val: SIMD[dtype, 1])
```  
Summary  
  
Safely store a scalar to i-th item of the underlying buffer.  
  
Args:  

- self
- index: Index of the item.
- val: Value to store.


```rust
store[width: Int](mut self, index: Int, val: SIMD[dtype, width])
```  
Summary  
  
Safely stores SIMD element of size `width` at `index` of the underlying buffer.  
  
Parameters:  

- width
  
Args:  

- self
- index: Index of the item.
- val: Value to store.


```rust
store[width: Int = 1](mut self, *indices: Int, *, val: SIMD[dtype, width])
```  
Summary  
  
Safely stores SIMD element of size `width` at given variadic indices of the underlying buffer.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- \*indices: Variadic indices.
- val: Value to store.

#### __int__


```rust
__int__(self) -> Int
```  
Summary  
  
Gets `Int` representation of the array.  
  
Args:  

- self

#### __float__


```rust
__float__(self) -> SIMD[float64, 1]
```  
Summary  
  
Gets `Float64` representation of the array.  
  
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
  
Enables String(array).  
  
Args:  

- self

#### write_to


```rust
write_to[W: Writer](self, mut writer: W)
```  
Summary  
  
Writes the array to a writer.  
  
Parameters:  

- W
  
Args:  

- self
- writer: The writer to write the array to.

#### __repr__


```rust
__repr__(self) -> String
```  
Summary  
  
Computes the "official" string representation of NDArray. You can construct the array using this representation.  
  
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
  
Iterates over elements of the NDArray and return sub-arrays as view.  
  
Args:  

- self

#### __reversed__


```rust
__reversed__(self) -> _NDArrayIter[self, dtype, False]
```  
Summary  
  
Iterates backwards over elements of the NDArray, returning copied value.  
  
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
  
Sort the NDArray and return the sorted indices. See `numojo.argsort()`.  
  
Args:  

- self


```rust
argsort(self, axis: Int) -> NDArray[index]
```  
Summary  
  
Sort the NDArray and return the sorted indices. See `numojo.argsort()`.  
  
Args:  

- self
- axis

#### astype


```rust
astype[target: DType](self) -> NDArray[target]
```  
Summary  
  
Convert type of array.  
  
Parameters:  

- target: Target data type.
  
Args:  

- self

#### clip


```rust
clip(self, a_min: SIMD[dtype, 1], a_max: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Limit the values in an array between [a_min, a_max]. If a_min is greater than a_max, the value is equal to a_max. See `numojo.clip()` for more details.  
  
Args:  

- self
- a_min: The minimum value.
- a_max: The maximum value.

#### compress


```rust
compress[dtype: DType](self, condition: NDArray[bool], axis: Int) -> Self
```  
Summary  
  
Return selected slices of an array along given axis. If no axis is provided, the array is flattened before use.  
  
Parameters:  

- dtype: DType.
  
Args:  

- self
- condition: 1-D array of booleans that selects which entries to return. If length of condition is less than the size of the array along the given axis, then output is filled to the length of the condition with False.
- axis: The axis along which to take slices.


```rust
compress[dtype: DType](self, condition: NDArray[bool]) -> Self
```  
Summary  
  
Return selected slices of an array along given axis. If no axis is provided, the array is flattened before use. This is a function ***OVERLOAD***.  
  
Parameters:  

- dtype: DType.
  
Args:  

- self
- condition: 1-D array of booleans that selects which entries to return. If length of condition is less than the size of the array along the given axis, then output is filled to the length of the condition with False.

#### col


```rust
col(self, id: Int) -> Self
```  
Summary  
  
Get the ith column of the matrix.  
  
Args:  

- self
- id: The column index.

#### copy


```rust
copy(self) -> Self
```  
Summary  
  
Returns a copy of the array that owns the data. The returned array will be contiguous in memory.  
  
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
diagonal[dtype: DType](self, offset: Int = 0) -> Self
```  
Summary  
  
Returns specific diagonals. Currently supports only 2D arrays.  
  
Parameters:  

- dtype: Data type of the array.
  
Args:  

- self
- offset: Offset of the diagonal from the main diagonal. Default: 0

#### fill


```rust
fill(mut self, val: SIMD[dtype, 1])
```  
Summary  
  
Fill all items of array with value.  
  
Args:  

- self
- val: Value to fill.

#### flatten


```rust
flatten(self, order: String = String("C")) -> Self
```  
Summary  
  
Return a copy of the array collapsed into one dimension.  
  
Args:  

- self
- order: A NDArray. Default: String("C")

#### iter_along_axis


```rust
iter_along_axis[forward: Bool = True](self, axis: Int, order: String = String("C")) -> _NDAxisIter[self, dtype, forward]
```  
Summary  
  
Returns an iterator yielding 1-d array slices along the given axis.  
  
Parameters:  

- forward: If True, iterate from the beginning to the end. If False, iterate from the end to the beginning. Defualt: `True`
  
Args:  

- self
- axis: The axis by which the iteration is performed.
- order: The order to traverse the array. Default: String("C")

#### iter_over_dimension


```rust
iter_over_dimension[forward: Bool = True](self, dimension: Int) -> _NDArrayIter[self, dtype, forward]
```  
Summary  
  
Returns an iterator yielding `ndim-1` arrays over the given dimension.  
  
Parameters:  

- forward: If True, iterate from the beginning to the end. If False, iterate from the end to the beginning. Defualt: `True`
  
Args:  

- self
- dimension: The dimension by which the iteration is performed.

#### max


```rust
max(self) -> SIMD[dtype, 1]
```  
Summary  
  
Finds the max value of an array. When no axis is given, the array is flattened before sorting.  
  
Args:  

- self


```rust
max(self, axis: Int) -> Self
```  
Summary  
  
Finds the max value of an array along the axis. The number of dimension will be reduced by 1. When no axis is given, the array is flattened before sorting.  
  
Args:  

- self
- axis: The axis along which the max is performed.

#### mdot


```rust
mdot(self, other: Self) -> Self
```  
Summary  
  
Dot product of two matrix. Matrix A: M * N. Matrix B: N * L.  
  
Args:  

- self
- other: The other matrix.

#### mean


```rust
mean[returned_dtype: DType = float64](self) -> SIMD[returned_dtype, 1]
```  
Summary  
  
Mean of a array.  
  
Parameters:  

- returned_dtype Defualt: `float64`
  
Args:  

- self


```rust
mean[returned_dtype: DType = float64](self, axis: Int) -> NDArray[returned_dtype]
```  
Summary  
  
Mean of array elements over a given axis.  
  
Parameters:  

- returned_dtype Defualt: `float64`
  
Args:  

- self
- axis: The axis along which the mean is performed.

#### median


```rust
median[returned_dtype: DType = float64](self) -> SIMD[returned_dtype, 1]
```  
Summary  
  
Median of a array.  
  
Parameters:  

- returned_dtype Defualt: `float64`
  
Args:  

- self


```rust
median[returned_dtype: DType = float64](self, axis: Int) -> NDArray[returned_dtype]
```  
Summary  
  
Median of array elements over a given axis.  
  
Parameters:  

- returned_dtype Defualt: `float64`
  
Args:  

- self
- axis: The axis along which the median is performed.

#### min


```rust
min(self) -> SIMD[dtype, 1]
```  
Summary  
  
Finds the min value of an array. When no axis is given, the array is flattened before sorting.  
  
Args:  

- self


```rust
min(self, axis: Int) -> Self
```  
Summary  
  
Finds the min value of an array along the axis. The number of dimension will be reduced by 1. When no axis is given, the array is flattened before sorting.  
  
Args:  

- self
- axis: The axis along which the min is performed.

#### nditer


```rust
nditer(self) -> _NDIter[self, dtype]
```  
Summary  
  
***Overload*** Return an iterator yielding the array elements according to the memory layout of the array.  
  
Args:  

- self


```rust
nditer(self, order: String) -> _NDIter[self, dtype]
```  
Summary  
  
Return an iterator yielding the array elements according to the order.  
  
Args:  

- self
- order: Order of the array.

#### num_elements


```rust
num_elements(self) -> Int
```  
Summary  
  
Function to retreive size (compatability).  
  
Args:  

- self

#### prod


```rust
prod(self) -> SIMD[dtype, 1]
```  
Summary  
  
Product of all array elements.  
  
Args:  

- self


```rust
prod(self, axis: Int) -> Self
```  
Summary  
  
Product of array elements over a given axis.  
  
Args:  

- self
- axis: The axis along which the product is performed.

#### rdot


```rust
rdot(self, other: Self) -> Self
```  
Summary  
  
Dot product of two matrix. Matrix A: M * N. Matrix B: N * L.  
  
Args:  

- self
- other: The other matrix.

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

#### row


```rust
row(self, id: Int) -> Self
```  
Summary  
  
Get the ith row of the matrix.  
  
Args:  

- self
- id: The row index.

#### sort


```rust
sort(mut self, axis: Int = -1)
```  
Summary  
  
Sorts the array in-place along the given axis using quick sort method. The deault axis is -1. See `numojo.sorting.sort` for more information.  
  
Args:  

- self
- axis: The axis along which the array is sorted. Defaults to -1. Default: -1

#### std


```rust
std[returned_dtype: DType = float64](self, ddof: Int = 0) -> SIMD[returned_dtype, 1]
```  
Summary  
  
Compute the standard deviation. See `numojo.std`.  
  
Parameters:  

- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- self
- ddof: Delta degree of freedom. Default: 0


```rust
std[returned_dtype: DType = float64](self, axis: Int, ddof: Int = 0) -> NDArray[returned_dtype]
```  
Summary  
  
Compute the standard deviation along the axis. See `numojo.std`.  
  
Parameters:  

- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- self
- axis: The axis along which the mean is performed.
- ddof: Delta degree of freedom. Default: 0

#### sum


```rust
sum(self) -> SIMD[dtype, 1]
```  
Summary  
  
Returns sum of all array elements.  
  
Args:  

- self


```rust
sum(self, axis: Int) -> Self
```  
Summary  
  
Sum of array elements over a given axis.  
  
Args:  

- self
- axis: The axis along which the sum is performed.

#### T


```rust
T(self, axes: List[Int]) -> Self
```  
Summary  
  
Transpose array of any number of dimensions according to arbitrary permutation of the axes.  
  
Args:  

- self
- axes: List of axes.


```rust
T(self) -> Self
```  
Summary  
  
***Overload*** Transposes the array when `axes` is not given. If `axes` is not given, it is equal to flipping the axes. See docstring of `transpose`.  
  
Args:  

- self

#### tolist


```rust
tolist(self) -> List[SIMD[dtype, 1]]
```  
Summary  
  
Converts NDArray to a 1-D List.  
  
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

#### variance


```rust
variance[returned_dtype: DType = float64](self, ddof: Int = 0) -> SIMD[returned_dtype, 1]
```  
Summary  
  
Returns the variance of array.  
  
Parameters:  

- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- self
- ddof: Delta degree of freedom. Default: 0


```rust
variance[returned_dtype: DType = float64](self, axis: Int, ddof: Int = 0) -> NDArray[returned_dtype]
```  
Summary  
  
Returns the variance of array along the axis. See `numojo.variance`.  
  
Parameters:  

- returned_dtype: The returned data type, defaulting to float64. Defualt: `float64`
  
Args:  

- self
- axis: The axis along which the mean is performed.
- ddof: Delta degree of freedom. Default: 0

#### vdot


```rust
vdot(self, other: Self) -> SIMD[dtype, 1]
```  
Summary  
  
Inner product of two vectors.  
  
Args:  

- self
- other: The other vector.
