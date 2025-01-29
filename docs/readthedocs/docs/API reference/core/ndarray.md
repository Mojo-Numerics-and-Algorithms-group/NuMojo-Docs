



# ndarray

##  Module Summary
  
Implements N-Dimensional Array
## NDArrayShape

### NDArrayShape Summary
  
  
Implements the NDArrayShape.  

### Parent Traits
  

- AnyType
- Stringable

### Fields
  
  
* ndsize `Int`  
    - Total no of elements in the corresponding array.  
* ndshape `DTypePointer[dtype, 0]`  
    - Shape of the corresponding array.  
* ndlen `Int`  
    - Length of ndshape.  

### Functions

#### __init__


```rust
__init__(inout self: Self, *shape: Int)
```  
Summary  
  
Initializes the NDArrayShape with variable shape dimensions.  
  
Args:  

- self
- \*shape: Variable number of integers representing the shape dimensions.


```rust
__init__(inout self: Self, *shape: Int, *, size: Int)
```  
Summary  
  
Initializes the NDArrayShape with variable shape dimensions and a specified size.  
  
Args:  

- self
- \*shape: Variable number of integers representing the shape dimensions.
- size: The total number of elements in the array.


```rust
__init__(inout self: Self, shape: List[Int])
```  
Summary  
  
Initializes the NDArrayShape with a list of shape dimensions.  
  
Args:  

- self
- shape: A list of integers representing the shape dimensions.


```rust
__init__(inout self: Self, shape: List[Int], size: Int)
```  
Summary  
  
Initializes the NDArrayShape with a list of shape dimensions and a specified size.  
  
Args:  

- self
- shape: A list of integers representing the shape dimensions.
- size: The specified size of the NDArrayShape.


```rust
__init__(inout self: Self, shape: VariadicList[Int])
```  
Summary  
  
Initializes the NDArrayShape with a list of shape dimensions.  
  
Args:  

- self
- shape: A list of integers representing the shape dimensions.


```rust
__init__(inout self: Self, shape: VariadicList[Int], size: Int)
```  
Summary  
  
Initializes the NDArrayShape with a list of shape dimensions and a specified size.  
  
Args:  

- self
- shape: A list of integers representing the shape dimensions.
- size: The specified size of the NDArrayShape.


```rust
__init__(inout self: Self, shape: NDArrayShape[dtype])
```  
Summary  
  
Initializes the NDArrayShape with another NDArrayShape.  
  
Args:  

- self
- shape: Another NDArrayShape to initialize from.

#### __getitem__


```rust
__getitem__(self: Self, index: Int) -> Int
```  
Summary  
  
Get shape at specified index.  
  
Args:  

- self
- index

#### __setitem__


```rust
__setitem__(inout self: Self, index: Int, val: Int)
```  
Summary  
  
Set shape at specified index.  
  
Args:  

- self
- index
- val

#### __eq__


```rust
__eq__(self: Self, other: Self) -> Bool
```  
Summary  
  
Check if two arrayshapes have identical dimensions.  
  
Args:  

- self
- other

#### __ne__


```rust
__ne__(self: Self, other: Self) -> Bool
```  
Summary  
  
Check if two arrayshapes don't have identical dimensions.  
  
Args:  

- self
- other

#### __contains__


```rust
__contains__(self: Self, val: Int) -> Bool
```  
Summary  
  
Check if any of the dimensions are equal to a value.  
  
Args:  

- self
- val

#### size


```rust
size(self: Self) -> Int
```  
Summary  
  
Get Size of array described by arrayshape.  
  
Args:  

- self

#### len


```rust
len(self: Self) -> Int
```  
Summary  
  
Get number of dimensions of the array described by arrayshape.  
  
Args:  

- self

#### load


```rust
load[width: Int = 1](self: Self, index: Int) -> SIMD[dtype, $0]
```  
Summary  
  
SIMD load dimensional information.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- index

#### store


```rust
store[width: Int = 1](inout self: Self, index: Int, val: SIMD[dtype, width])
```  
Summary  
  
SIMD store dimensional information.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- index
- val

#### load_int


```rust
load_int(self: Self, index: Int) -> Int
```  
Summary  
  
SIMD load dimensional information.  
  
Args:  

- self
- index

#### store_int


```rust
store_int(inout self: Self, index: Int, val: Int)
```  
Summary  
  
SIMD store dimensional information.  
  
Args:  

- self
- index
- val

## NDArrayStride

### NDArrayStride Summary
  
  
Implements the NDArrayStride.  

### Parent Traits
  

- AnyType
- Stringable

### Fields
  
  
* ndoffset `Int`  
* ndstride `DTypePointer[dtype, 0]`  
* ndlen `Int`  

### Functions

#### __init__


```rust
__init__(inout self: Self, *stride: Int, *, offset: Int = 0)
```  
Summary  
  
  
  
Args:  

- self
- \*stride
- offset Default: 0


```rust
__init__(inout self: Self, stride: List[Int], offset: Int = 0)
```  
Summary  
  
  
  
Args:  

- self
- stride
- offset Default: 0


```rust
__init__(inout self: Self, stride: VariadicList[Int], offset: Int = 0)
```  
Summary  
  
  
  
Args:  

- self
- stride
- offset Default: 0


```rust
__init__(inout self: Self, stride: NDArrayStride[dtype])
```  
Summary  
  
  
  
Args:  

- self
- stride


```rust
__init__(inout self: Self, stride: NDArrayStride[dtype], offset: Int = 0)
```  
Summary  
  
  
  
Args:  

- self
- stride
- offset Default: 0


```rust
__init__(inout self: Self, *shape: Int, *, offset: Int = 0, order: String = "C")
```  
Summary  
  
  
  
Args:  

- self
- \*shape
- offset Default: 0
- order Default: "C"


```rust
__init__(inout self: Self, shape: List[Int], offset: Int = 0, order: String = "C")
```  
Summary  
  
  
  
Args:  

- self
- shape
- offset Default: 0
- order Default: "C"


```rust
__init__(inout self: Self, shape: VariadicList[Int], offset: Int = 0, order: String = "C")
```  
Summary  
  
  
  
Args:  

- self
- shape
- offset Default: 0
- order Default: "C"


```rust
__init__(inout self: Self, owned shape: NDArrayShape[dtype], offset: Int = 0, order: String = "C")
```  
Summary  
  
  
  
Args:  

- self
- shape
- offset Default: 0
- order Default: "C"

#### __getitem__


```rust
__getitem__(self: Self, index: Int) -> Int
```  
Summary  
  
  
  
Args:  

- self
- index

#### __setitem__


```rust
__setitem__(inout self: Self, index: Int, val: Int)
```  
Summary  
  
  
  
Args:  

- self
- index
- val

#### __eq__


```rust
__eq__(self: Self, other: Self) -> Bool
```  
Summary  
  
  
  
Args:  

- self
- other

#### __ne__


```rust
__ne__(self: Self, other: Self) -> Bool
```  
Summary  
  
  
  
Args:  

- self
- other

#### __contains__


```rust
__contains__(self: Self, val: Int) -> Bool
```  
Summary  
  
  
  
Args:  

- self
- val

#### len


```rust
len(self: Self) -> Int
```  
Summary  
  
  
  
Args:  

- self

#### load


```rust
load[width: Int = 1](self: Self, index: Int) -> SIMD[dtype, $0]
```  
Summary  
  
  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- index

#### store


```rust
store[width: Int = 1](inout self: Self, index: Int, val: SIMD[dtype, width])
```  
Summary  
  
  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- index
- val

#### load_unsafe


```rust
load_unsafe[width: Int = 1](self: Self, index: Int) -> Int
```  
Summary  
  
  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- index

#### store_unsafe


```rust
store_unsafe[width: Int = 1](inout self: Self, index: Int, val: SIMD[dtype, width])
```  
Summary  
  
  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- index
- val

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

### Aliases
  
`simd_width`: Vector size of the data type.
### Fields
  
  
* data `DTypePointer[dtype, 0]`  
    - Data buffer of the items in the NDArray.  
* ndim `Int`  
    - Number of Dimensions.  
* ndshape `NDArrayShape[int32]`  
    - Size and shape of NDArray.  
* stride `NDArrayStride[int32]`  
    - Contains offset, strides.  
* coefficient `NDArrayStride[int32]`  
    - Contains offset, coefficient.  
* datatype `DType`  
    - The datatype of memory.  
* order `String`  
    - Memory layout of array C (C order row major) or F (Fortran order col major).  

### Functions

#### __init__


```rust
__init__(inout self: Self, *shape: Int, *, random: Bool = 0, order: String = "C")
```  
Summary  
  
NDArray initialization for variadic shape.  
  
Args:  

- self
- \*shape: Variadic shape.
- random: Set the values randomly. Default: 0
- order: Memory order C or F. Default: "C"


```rust
__init__(inout self: Self, shape: List[Int], random: Bool = 0, order: String = "C")
```  
Summary  
  
NDArray initialization for list shape.  
  
Args:  

- self
- shape: List of shape.
- random: Set the values randomly. Default: 0
- order: Memory order C or F. Default: "C"


```rust
__init__(inout self: Self, shape: VariadicList[Int], random: Bool = 0, order: String = "C")
```  
Summary  
  
NDArray initialization for variadic shape.  
  
Args:  

- self
- shape: Variadic List shape.
- random: Set the values randomly. Default: 0
- order: Memory order C or F. Default: "C"


```rust
__init__(inout self: Self, *shape: Int, *, fill: SIMD[dtype, 1], order: String = "C")
```  
Summary  
  
NDArray initialization for variadic shape with option to fill.  
  
Args:  

- self
- \*shape: Variadic shape.
- fill: Set all the values to this.
- order: Memory order C or F. Default: "C"


```rust
__init__(inout self: Self, shape: List[Int], fill: SIMD[dtype, 1], order: String = "C")
```  
Summary  
  
NDArray initialization for variadic shape with option to fill.  
  
Args:  

- self
- shape: List of shape.
- fill: Set all the values to this.
- order: Memory order C or F. Default: "C"


```rust
__init__(inout self: Self, shape: VariadicList[Int], fill: SIMD[dtype, 1], order: String = "C")
```  
Summary  
  
NDArray initialization for List of shape with option to fill.  
  
Args:  

- self
- shape: Variadic List of shape.
- fill: Set all the values to this.
- order: Memory order C or F. Default: "C"


```rust
__init__(inout self: Self, shape: NDArrayShape[dtype], random: Bool = 0, order: String = "C")
```  
Summary  
  
NDArray initialization for NDArrayShape.  
  
Args:  

- self
- shape: Variadic shape.
- random: Set all the values randomly. Default: 0
- order: Memory order C or F. Default: "C"


```rust
__init__(inout self: Self, shape: NDArrayShape[dtype], fill: SIMD[dtype, 1], order: String = "C")
```  
Summary  
  
NDArray initialization for NDArrayShape with option to fill.  
  
Args:  

- self
- shape: Variadic shape.
- fill: Set all the the values to this.
- order: Memory order C or F. Default: "C"


```rust
__init__(inout self: Self, data: List[SIMD[dtype, 1]], shape: List[Int], order: String = "C")
```  
Summary  
  
NDArray initialization from list of data.  
  
Args:  

- self
- data: List of data.
- shape: List of shape.
- order: Memory order C or F. Default: "C"


```rust
__init__(inout self: Self, text: String, order: String = "C")
```  
Summary  
  
NDArray initialization from string representation of an ndarray. The shape can be inferred from the string representation. The literals will be casted to the dtype of the NDArray.  
  
Args:  

- self
- text: String representation of an ndarray.
- order: Memory order C or F. Default: "C"


```rust
__init__(inout self: Self, ndim: Int, offset: Int, size: Int, shape: List[Int], strides: List[Int], coefficient: List[Int], order: String = "C")
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
- order Default: "C"


```rust
__init__(inout self: Self, data: DTypePointer[dtype, 0], ndim: Int, offset: Int, shape: List[Int], strides: List[Int], coefficient: List[Int], order: String = "C")
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
- order Default: "C"

#### __copyinit__


```rust
__copyinit__(inout self: Self, other: Self)
```  
Summary  
  
Copy other into self.  
  
Args:  

- self
- other

#### __moveinit__


```rust
__moveinit__(inout self: Self, owned existing: Self)
```  
Summary  
  
Move other into self.  
  
Args:  

- self
- existing

#### __del__


```rust
__del__(owned self: Self)
```  
Summary  
  
  
  
Args:  

- self

#### __bool__


```rust
__bool__(self: Self) -> Bool
```  
Summary  
  
If all true return true.  
  
Args:  

- self

#### __getitem__


```rust
__getitem__(self: Self, idx: Int) -> Self
```  
Summary  
  
Retreive a slice of the array corrisponding to the index at the first dimension.  
  
Args:  

- self
- idx


```rust
__getitem__(self: Self, owned *slices: Slice) -> Self
```  
Summary  
  
Retreive slices of an array from variadic slices.  
  
Args:  

- self
- \*slices


```rust
__getitem__(self: Self, owned slices: List[Slice]) -> Self
```  
Summary  
  
Retreive slices of an array from list of slices.  
  
Args:  

- self
- slices


```rust
__getitem__(self: Self, owned *slices: Variant[Slice, Int]) -> Self
```  
Summary  
  
Get items by a series of either slices or integers.  
  
Args:  

- self
- \*slices: A series of either Slice or Int.


```rust
__getitem__(self: Self, index: List[Int]) -> Self
```  
Summary  
  
Get items of array from a list of indices.  
  
Args:  

- self
- index: List[Int].


```rust
__getitem__(self: Self, index: NDArray[index]) -> Self
```  
Summary  
  
Get items of array from an array of indices.  
  
Args:  

- self
- index


```rust
__getitem__(self: Self, mask: NDArray[bool]) -> Self
```  
Summary  
  
Get items of array corrisponding to a mask.  
  
Args:  

- self
- mask: NDArray with Dtype.bool.

#### __setitem__


```rust
__setitem__(inout self: Self, index: Int, val: SIMD[dtype, 1])
```  
Summary  
  
Set the value of a single index.  
  
Args:  

- self
- index
- val


```rust
__setitem__(inout self: Self, *index: Int, *, val: SIMD[dtype, 1])
```  
Summary  
  
Set the value at the index list.  
  
Args:  

- self
- \*index
- val


```rust
__setitem__(inout self: Self, index: List[Int], val: SIMD[dtype, 1])
```  
Summary  
  
Set the value at the index list.  
  
Args:  

- self
- index
- val


```rust
__setitem__(inout self: Self, index: VariadicList[Int], val: SIMD[dtype, 1])
```  
Summary  
  
Set the value at the index corisponding to the varaidic list.  
  
Args:  

- self
- index
- val


```rust
__setitem__(inout self: Self, mask: NDArray[bool], value: Self)
```  
Summary  
  
Set the value of the array at the indices where the mask is true.  
  
Args:  

- self
- mask
- value

#### __neg__


```rust
__neg__(self: Self) -> Self
```  
Summary  
  
Unary negative returens self unless boolean type.  
  
Args:  

- self

#### __pos__


```rust
__pos__(self: Self) -> Self
```  
Summary  
  
Unary positve returens self unless boolean type.  
  
Args:  

- self

#### __invert__


```rust
__invert__(self: Self) -> Self
```  
Summary  
  
Elementwise inverse (~ or not), only for bools and integral types.  
  
Args:  

- self

#### __lt__


```rust
__lt__(self: Self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than.  
  
Args:  

- self
- other


```rust
__lt__(self: Self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise less than between scalar and Array.  
  
Args:  

- self
- other

#### __le__


```rust
__le__(self: Self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to.  
  
Args:  

- self
- other


```rust
__le__(self: Self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to between scalar and Array.  
  
Args:  

- self
- other

#### __eq__


```rust
__eq__(self: Self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise equivelence.  
  
Args:  

- self
- other


```rust
__eq__(self: Self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise equivelence between scalar and Array.  
  
Args:  

- self
- other

#### __ne__


```rust
__ne__(self: Self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise nonequivelence.  
  
Args:  

- self
- other


```rust
__ne__(self: Self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise nonequivelence between scalar and Array.  
  
Args:  

- self
- other

#### __gt__


```rust
__gt__(self: Self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than.  
  
Args:  

- self
- other


```rust
__gt__(self: Self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than between scalar and Array.  
  
Args:  

- self
- other

#### __ge__


```rust
__ge__(self: Self, other: SIMD[dtype, 1]) -> NDArray[bool]
```  
Summary  
  
Itemwise greater than or equal to.  
  
Args:  

- self
- other


```rust
__ge__(self: Self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise less than or equal to between scalar and Array.  
  
Args:  

- self
- other

#### __add__


```rust
__add__(inout self: Self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array + scalar`.  
  
Args:  

- self
- other


```rust
__add__(inout self: Self, other: Self) -> Self
```  
Summary  
  
Enables `array + array`.  
  
Args:  

- self
- other

#### __sub__


```rust
__sub__(self: Self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array - scalar`.  
  
Args:  

- self
- other


```rust
__sub__(self: Self, other: Self) -> Self
```  
Summary  
  
Enables `array - array`.  
  
Args:  

- self
- other

#### __mul__


```rust
__mul__(self: Self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array * scalar`.  
  
Args:  

- self
- other


```rust
__mul__(self: Self, other: Self) -> Self
```  
Summary  
  
Enables `array * array`.  
  
Args:  

- self
- other

#### __matmul__


```rust
__matmul__(self: Self, other: Self) -> Self
```  
Summary  
  
  
  
Args:  

- self
- other

#### __truediv__


```rust
__truediv__(self: Self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array / scalar`.  
  
Args:  

- self
- other


```rust
__truediv__(self: Self, other: Self) -> Self
```  
Summary  
  
Enables `array / array`.  
  
Args:  

- self
- other

#### __floordiv__


```rust
__floordiv__(self: Self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array // scalar`.  
  
Args:  

- self
- other


```rust
__floordiv__(self: Self, other: Self) -> Self
```  
Summary  
  
Enables `array // array`.  
  
Args:  

- self
- other

#### __mod__


```rust
__mod__(inout self: Self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `array % scalar`.  
  
Args:  

- self
- other


```rust
__mod__(inout self: Self, other: Self) -> Self
```  
Summary  
  
Enables `array % array`.  
  
Args:  

- self
- other

#### __pow__


```rust
__pow__(self: Self, p: Int) -> Self
```  
Summary  
  
  
  
Args:  

- self
- p


```rust
__pow__(self: Self, p: Self) -> Self
```  
Summary  
  
  
  
Args:  

- self
- p

#### __radd__


```rust
__radd__(inout self: Self, rhs: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar + array`.  
  
Args:  

- self
- rhs

#### __rsub__


```rust
__rsub__(self: Self, s: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar - array`.  
  
Args:  

- self
- s

#### __rmul__


```rust
__rmul__(self: Self, s: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar * array`.  
  
Args:  

- self
- s

#### __rtruediv__


```rust
__rtruediv__(self: Self, s: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar / array`.  
  
Args:  

- self
- s

#### __rfloordiv__


```rust
__rfloordiv__(self: Self, s: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar // array`.  
  
Args:  

- self
- s

#### __rmod__


```rust
__rmod__(inout self: Self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `scalar % array`.  
  
Args:  

- self
- other

#### __iadd__


```rust
__iadd__(inout self: Self, other: SIMD[dtype, 1])
```  
Summary  
  
Enables `array += scalar`.  
  
Args:  

- self
- other


```rust
__iadd__(inout self: Self, other: Self)
```  
Summary  
  
Enables `array *= array`.  
  
Args:  

- self
- other

#### __isub__


```rust
__isub__(inout self: Self, s: SIMD[dtype, 1])
```  
Summary  
  
Enables `array -= scalar`.  
  
Args:  

- self
- s


```rust
__isub__(inout self: Self, s: Self)
```  
Summary  
  
Enables `array -= array`.  
  
Args:  

- self
- s

#### __imul__


```rust
__imul__(inout self: Self, s: SIMD[dtype, 1])
```  
Summary  
  
Enables `array *= scalar`.  
  
Args:  

- self
- s


```rust
__imul__(inout self: Self, s: Self)
```  
Summary  
  
Enables `array *= array`.  
  
Args:  

- self
- s

#### __itruediv__


```rust
__itruediv__(inout self: Self, s: SIMD[dtype, 1])
```  
Summary  
  
Enables `array /= scalar`.  
  
Args:  

- self
- s


```rust
__itruediv__(inout self: Self, other: Self)
```  
Summary  
  
Enables `array /= array`.  
  
Args:  

- self
- other

#### __ifloordiv__


```rust
__ifloordiv__(inout self: Self, s: SIMD[dtype, 1])
```  
Summary  
  
Enables `array //= scalar`.  
  
Args:  

- self
- s


```rust
__ifloordiv__(inout self: Self, other: Self)
```  
Summary  
  
Enables `array //= array`.  
  
Args:  

- self
- other

#### __imod__


```rust
__imod__(inout self: Self, other: SIMD[dtype, 1])
```  
Summary  
  
Enables `array %= scalar`.  
  
Args:  

- self
- other


```rust
__imod__(inout self: Self, other: Self)
```  
Summary  
  
Enables `array %= array`.  
  
Args:  

- self
- other

#### __ipow__


```rust
__ipow__(inout self: Self, p: Int)
```  
Summary  
  
  
  
Args:  

- self
- p

#### get_scalar


```rust
get_scalar(self: Self, index: Int) -> SIMD[dtype, 1]
```  
Summary  
  
Linearly retreive a value from the underlying Pointer.  
  
Args:  

- self
- index

#### vdot


```rust
vdot(self: Self, other: Self) -> SIMD[dtype, 1]
```  
Summary  
  
Inner product of two vectors.  
  
Args:  

- self
- other

#### mdot


```rust
mdot(self: Self, other: Self) -> Self
```  
Summary  
  
Dot product of two matrix. Matrix A: M * N. Matrix B: N * L.  
  
Args:  

- self
- other

#### row


```rust
row(self: Self, id: Int) -> Self
```  
Summary  
  
Get the ith row of the matrix.  
  
Args:  

- self
- id

#### col


```rust
col(self: Self, id: Int) -> Self
```  
Summary  
  
Get the ith column of the matrix.  
  
Args:  

- self
- id

#### rdot


```rust
rdot(self: Self, other: Self) -> Self
```  
Summary  
  
Dot product of two matrix. Matrix A: M * N. Matrix B: N * L.  
  
Args:  

- self
- other

#### size


```rust
size(self: Self) -> Int
```  
Summary  
  
Function to retreive size.  
  
Args:  

- self

#### num_elements


```rust
num_elements(self: Self) -> Int
```  
Summary  
  
Function to retreive size (compatability).  
  
Args:  

- self

#### shape


```rust
shape(self: Self) -> NDArrayShape[int32]
```  
Summary  
  
Get the shape as an NDArray Shape.  
  
Args:  

- self

#### load


```rust
load[width: Int = 1](self: Self, index: Int) -> SIMD[dtype, $0]
```  
Summary  
  
Loads a SIMD element of size `width` at the given index `index`.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- index


```rust
load[width: Int = 1](self: Self, *index: Int) -> SIMD[dtype, $0]
```  
Summary  
  
Loads a SIMD element of size `width` at given variadic indices argument.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- \*index

#### store


```rust
store[width: Int](inout self: Self, index: Int, val: SIMD[dtype, width])
```  
Summary  
  
Stores the SIMD element of size `width` at index `index`.  
  
Parameters:  

- width
  
Args:  

- self
- index
- val


```rust
store[width: Int = 1](inout self: Self, *index: Int, *, val: SIMD[dtype, width])
```  
Summary  
  
Stores the SIMD element of size `width` at the given variadic indices argument.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- \*index
- val

#### all


```rust
all(self: Self) -> Bool
```  
Summary  
  
If all true return true.  
  
Args:  

- self

#### any


```rust
any(self: Self) -> Bool
```  
Summary  
  
True if any true.  
  
Args:  

- self

#### argmax


```rust
argmax(self: Self) -> Int
```  
Summary  
  
Get location in pointer of max value.  
  
Args:  

- self

#### argmin


```rust
argmin(self: Self) -> Int
```  
Summary  
  
Get location in pointer of min value.  
  
Args:  

- self

#### argsort


```rust
argsort(self: Self) -> NDArray[index]
```  
Summary  
  
Sort the NDArray and return the sorted indices.  
  
Args:  

- self

#### astype


```rust
astype[type: DType](inout self: Self) -> NDArray[$0]
```  
Summary  
  
Convert type of array.  
  
Parameters:  

- type
  
Args:  

- self

#### cumprod


```rust
cumprod(self: Self) -> SIMD[dtype, 1]
```  
Summary  
  
Cumulative product of a array.  
  
Args:  

- self

#### cumsum


```rust
cumsum(self: Self) -> SIMD[dtype, 1]
```  
Summary  
  
Cumulative Sum of a array.  
  
Args:  

- self

#### diagonal


```rust
diagonal(self: Self)
```  
Summary  
  
  
  
Args:  

- self

#### fill


```rust
fill(inout self: Self, val: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Fill all items of array with value.  
  
Args:  

- self
- val

#### flatten


```rust
flatten(inout self: Self, inplace: Bool = 0) -> Optional[NDArray[dtype]]
```  
Summary  
  
Convert shape of array to one dimensional.  
  
Args:  

- self
- inplace Default: 0

#### item


```rust
item(self: Self, *index: Int) -> SIMD[dtype, 1]
```  
Summary  
  
Return the scalar at the coordinates.  
  
Args:  

- self
- \*index: The coordinates of the item.

#### max


```rust
max(self: Self, axis: Int = 0) -> Self
```  
Summary  
  
Max on axis.  
  
Args:  

- self
- axis Default: 0

#### min


```rust
min(self: Self, axis: Int = 0) -> Self
```  
Summary  
  
Min on axis.  
  
Args:  

- self
- axis Default: 0

#### mean


```rust
mean(self: Self, axis: Int) -> Self
```  
Summary  
  
Mean of array elements over a given axis. Args:     array: NDArray.     axis: The axis along which the mean is performed. Returns:     An NDArray.  
  
Args:  

- self
- axis


```rust
mean(self: Self) -> SIMD[dtype, 1]
```  
Summary  
  
Cumulative mean of a array.  
  
Args:  

- self

#### prod


```rust
prod(self: Self, axis: Int) -> Self
```  
Summary  
  
Product of array elements over a given axis. Args:     array: NDArray.     axis: The axis along which the product is performed. Returns:     An NDArray.  
  
Args:  

- self
- axis

#### sort


```rust
sort(self: Self) -> Self
```  
Summary  
  
Sort the array using quickstort.  
  
Args:  

- self

#### sum


```rust
sum(self: Self, axis: Int) -> Self
```  
Summary  
  
Sum of array elements over a given axis. Args:     axis: The axis along which the sum is performed. Returns:     An NDArray.  
  
Args:  

- self
- axis

#### reshape


```rust
reshape(inout self: Self, *shape: Int, *, order: String = "C")
```  
Summary  
  
Reshapes the NDArray to given Shape.  
  
Args:  

- self
- \*shape: Variadic list of shape.
- order: Order of the array - Row major `C` or Column major `F`. Default: "C"

#### unsafe_ptr


```rust
unsafe_ptr(self: Self) -> DTypePointer[dtype, 0]
```  
Summary  
  
Retreive pointer without taking ownership.  
  
Args:  

- self

#### to_numpy


```rust
to_numpy(self: Self) -> PythonObject
```  
Summary  
  
Convert to a numpy array.  
  
Args:  

- self
