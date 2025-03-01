



# complex_ndarray

##  Module Summary
  
Implements N-Dimensional Complex Array Last updated: 2025-01-26
## ComplexNDArray

### ComplexNDArray Summary
  
  
Represents a Complex N-Dimensional Array.  

### Parent Traits
  

- AnyType
- CollectionElement
- Copyable
- ExplicitlyCopyable
- Movable
- Representable
- Sized
- Stringable
- UnknownDestructibility
- Writable

### Fields
  
  
* ndim `Int`  
    - Number of Dimensions.  
* shape `NDArrayShape`  
    - Size and shape of ComplexNDArray.  
* size `Int`  
    - Size of ComplexNDArray.  
* strides `NDArrayStrides`  
    - Contains offset, strides.  
* flags `Flags`  
    - Information about the memory layout of the array.  

### Functions

#### __init__


```rust
__init__(out self, owned re: NDArray[dtype], owned im: NDArray[dtype])
```  
Summary  
  
  
  
Args:  

- re
- im
- self


```rust
__init__(out self, shape: NDArrayShape, order: String = String("C"))
```  
Summary  
  
Initialize a ComplexNDArray with given shape.  
  
Args:  

- shape: Variadic shape.
- order: Memory order C or F. Default: String("C")
- self


```rust
__init__(out self, shape: List[Int], order: String = String("C"))
```  
Summary  
  
(Overload) Initialize a ComplexNDArray with given shape (list of integers).  
  
Args:  

- shape: List of shape.
- order: Memory order C or F. Default: String("C")
- self


```rust
__init__(out self, shape: VariadicList[Int], order: String = String("C"))
```  
Summary  
  
(Overload) Initialize a ComplexNDArray with given shape (variadic list of integers).  
  
Args:  

- shape: Variadic List of shape.
- order: Memory order C or F. Default: String("C")
- self


```rust
__init__(out self, shape: List[Int], offset: Int, strides: List[Int])
```  
Summary  
  
Extremely specific ComplexNDArray initializer.  
  
Args:  

- shape
- offset
- strides
- self


```rust
__init__(out self, shape: NDArrayShape, ref buffer_re: UnsafePointer[SIMD[dtype, 1]], ref buffer_im: UnsafePointer[SIMD[dtype, 1]], offset: Int, strides: NDArrayStrides)
```  
Summary  
  
Extremely specific ComplexNDArray initializer.  
  
Args:  

- shape
- buffer_re
- buffer_im
- offset
- strides
- self

#### __copyinit__


```rust
__copyinit__(out self, other: Self)
```  
Summary  
  
Copy other into self.  
  
Args:  

- other
- self

#### __moveinit__


```rust
__moveinit__(out self, owned existing: Self)
```  
Summary  
  
Move other into self.  
  
Args:  

- existing
- self

#### __getitem__


```rust
__getitem__(self, idx: Int) -> Self
```  
Summary  
  
Retreive a slice of the ComplexNDArray corresponding to the index at the first dimension.  
  
Args:  

- self
- idx


```rust
__getitem__(self, index: Item) -> ComplexSIMD[cdtype, dtype=dtype]
```  
Summary  
  
Get the value at the index list.  
  
Args:  

- self
- index


```rust
__getitem__(self, owned *slices: Slice) -> Self
```  
Summary  
  
Retreive slices of a ComplexNDArray from variadic slices.  
  
Args:  

- self
- \*slices


```rust
__getitem__(self, owned slice_list: List[Slice]) -> Self
```  
Summary  
  
Retreive slices of a ComplexNDArray from list of slices.  
  
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
__getitem__(self, index: List[Int]) -> Self
```  
Summary  
  
Get items of ComplexNDArray from a list of indices.  
  
Args:  

- self
- index: List[Int].


```rust
__getitem__(self, index: NDArray[index]) -> Self
```  
Summary  
  
Get items of ComplexNDArray from an array of indices.  
  
Args:  

- self
- index


```rust
__getitem__(self, mask: NDArray[bool]) -> Self
```  
Summary  
  
Get items of ComplexNDArray corresponding to a mask.  
  
Args:  

- self
- mask: NDArray with Dtype.bool.

#### __setitem__


```rust
__setitem__(mut self, idx: Int, val: Self)
```  
Summary  
  
Set a slice of ComplexNDArray with given ComplexNDArray.  
  
Args:  

- self
- idx
- val


```rust
__setitem__(mut self, index: Item, val: ComplexSIMD[cdtype, dtype=dtype])
```  
Summary  
  
Set the value at the index list.  
  
Args:  

- self
- index
- val


```rust
__setitem__(mut self, mask: Self, value: ComplexSIMD[cdtype, dtype=dtype])
```  
Summary  
  
Set the value of the array at the indices where the mask is true.  
  
Args:  

- self
- mask
- value


```rust
__setitem__(mut self, owned *slices: Slice, *, val: Self)
```  
Summary  
  
Retreive slices of an ComplexNDArray from variadic slices.  
  
Args:  

- self
- \*slices
- val


```rust
__setitem__(mut self, owned slices: List[Slice], val: Self)
```  
Summary  
  
Sets the slices of an ComplexNDArray from list of slices and ComplexNDArray.  
  
Args:  

- self
- slices
- val


```rust
__setitem__(self, index: NDArray[index], val: Self)
```  
Summary  
  
Returns the items of the ComplexNDArray from an array of indices.  
  
Args:  

- self
- index
- val


```rust
__setitem__(mut self, mask: Self, val: Self)
```  
Summary  
  
Set the value of the ComplexNDArray at the indices where the mask is true.  
  
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
  
Unary positive returns self unless boolean type.  
  
Args:  

- self

#### __eq__


```rust
__eq__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise equivalence.  
  
Args:  

- self
- other


```rust
__eq__(self, other: ComplexSIMD[cdtype, dtype=dtype]) -> NDArray[bool]
```  
Summary  
  
Itemwise equivalence between scalar and ComplexNDArray.  
  
Args:  

- self
- other

#### __ne__


```rust
__ne__(self, other: Self) -> NDArray[bool]
```  
Summary  
  
Itemwise non-equivalence.  
  
Args:  

- self
- other


```rust
__ne__(self, other: ComplexSIMD[cdtype, dtype=dtype]) -> NDArray[bool]
```  
Summary  
  
Itemwise non-equivalence between scalar and ComplexNDArray.  
  
Args:  

- self
- other

#### __add__


```rust
__add__(self, other: ComplexSIMD[cdtype, dtype=dtype]) -> Self
```  
Summary  
  
Enables `ComplexNDArray + ComplexSIMD`.  
  
Args:  

- self
- other


```rust
__add__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `ComplexNDArray + Scalar`.  
  
Args:  

- self
- other


```rust
__add__(self, other: Self) -> Self
```  
Summary  
  
Enables `ComplexNDArray + ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__add__(self, other: NDArray[dtype]) -> Self
```  
Summary  
  
Enables `ComplexNDArray + NDArray`.  
  
Args:  

- self
- other

#### __sub__


```rust
__sub__(self, other: ComplexSIMD[cdtype, dtype=dtype]) -> Self
```  
Summary  
  
Enables `ComplexNDArray - ComplexSIMD`.  
  
Args:  

- self
- other


```rust
__sub__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `ComplexNDArray - Scalar`.  
  
Args:  

- self
- other


```rust
__sub__(self, other: Self) -> Self
```  
Summary  
  
Enables `ComplexNDArray - ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__sub__(self, other: NDArray[dtype]) -> Self
```  
Summary  
  
Enables `ComplexNDArray - NDArray`.  
  
Args:  

- self
- other

#### __mul__


```rust
__mul__(self, other: ComplexSIMD[cdtype, dtype=dtype]) -> Self
```  
Summary  
  
Enables `ComplexNDArray * ComplexSIMD`.  
  
Args:  

- self
- other


```rust
__mul__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `ComplexNDArray * Scalar`.  
  
Args:  

- self
- other


```rust
__mul__(self, other: Self) -> Self
```  
Summary  
  
Enables `ComplexNDArray * ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__mul__(self, other: NDArray[dtype]) -> Self
```  
Summary  
  
Enables `ComplexNDArray * NDArray`.  
  
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
__truediv__(self, other: ComplexSIMD[cdtype, dtype=dtype]) -> Self
```  
Summary  
  
Enables `ComplexNDArray / ComplexSIMD`.  
  
Args:  

- self
- other


```rust
__truediv__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `ComplexNDArray / ComplexSIMD`.  
  
Args:  

- self
- other


```rust
__truediv__(self, other: Self) -> Self
```  
Summary  
  
Enables `ComplexNDArray / ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__truediv__(self, other: NDArray[dtype]) -> Self
```  
Summary  
  
Enables `ComplexNDArray / NDArray`.  
  
Args:  

- self
- other

#### __radd__


```rust
__radd__(mut self, other: ComplexSIMD[cdtype, dtype=dtype]) -> Self
```  
Summary  
  
Enables `ComplexSIMD + ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__radd__(mut self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `Scalar + ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__radd__(mut self, other: NDArray[dtype]) -> Self
```  
Summary  
  
Enables `NDArray + ComplexNDArray`.  
  
Args:  

- self
- other

#### __rsub__


```rust
__rsub__(mut self, other: ComplexSIMD[cdtype, dtype=dtype]) -> Self
```  
Summary  
  
Enables `ComplexSIMD - ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__rsub__(mut self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `Scalar - ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__rsub__(mut self, other: NDArray[dtype]) -> Self
```  
Summary  
  
Enables `NDArray - ComplexNDArray`.  
  
Args:  

- self
- other

#### __rmul__


```rust
__rmul__(self, other: ComplexSIMD[cdtype, dtype=dtype]) -> Self
```  
Summary  
  
Enables `ComplexSIMD * ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__rmul__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `Scalar * ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__rmul__(self, other: NDArray[dtype]) -> Self
```  
Summary  
  
Enables `NDArray * ComplexNDArray`.  
  
Args:  

- self
- other

#### __rtruediv__


```rust
__rtruediv__(mut self, other: ComplexSIMD[cdtype, dtype=dtype]) -> Self
```  
Summary  
  
Enables `ComplexSIMD / ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__rtruediv__(mut self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Enables `Scalar / ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__rtruediv__(mut self, other: NDArray[dtype]) -> Self
```  
Summary  
  
Enables `NDArray / ComplexNDArray`.  
  
Args:  

- self
- other

#### __iadd__


```rust
__iadd__(mut self, other: ComplexSIMD[cdtype, dtype=dtype])
```  
Summary  
  
Enables `ComplexNDArray += ComplexSIMD`.  
  
Args:  

- self
- other


```rust
__iadd__(mut self, other: SIMD[dtype, 1])
```  
Summary  
  
Enables `ComplexNDArray += Scalar`.  
  
Args:  

- self
- other


```rust
__iadd__(mut self, other: Self)
```  
Summary  
  
Enables `ComplexNDArray += ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__iadd__(mut self, other: NDArray[dtype])
```  
Summary  
  
Enables `ComplexNDArray += NDArray`.  
  
Args:  

- self
- other

#### __isub__


```rust
__isub__(mut self, other: ComplexSIMD[cdtype, dtype=dtype])
```  
Summary  
  
Enables `ComplexNDArray -= ComplexSIMD`.  
  
Args:  

- self
- other


```rust
__isub__(mut self, other: SIMD[dtype, 1])
```  
Summary  
  
Enables `ComplexNDArray -= Scalar`.  
  
Args:  

- self
- other


```rust
__isub__(mut self, other: Self)
```  
Summary  
  
Enables `ComplexNDArray -= ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__isub__(mut self, other: NDArray[dtype])
```  
Summary  
  
Enables `ComplexNDArray -= NDArray`.  
  
Args:  

- self
- other

#### __imul__


```rust
__imul__(mut self, other: ComplexSIMD[cdtype, dtype=dtype])
```  
Summary  
  
Enables `ComplexNDArray *= ComplexSIMD`.  
  
Args:  

- self
- other


```rust
__imul__(mut self, other: SIMD[dtype, 1])
```  
Summary  
  
Enables `ComplexNDArray *= Scalar`.  
  
Args:  

- self
- other


```rust
__imul__(mut self, other: Self)
```  
Summary  
  
Enables `ComplexNDArray *= ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__imul__(mut self, other: NDArray[dtype])
```  
Summary  
  
Enables `ComplexNDArray *= NDArray`.  
  
Args:  

- self
- other

#### __itruediv__


```rust
__itruediv__(mut self, other: ComplexSIMD[cdtype, dtype=dtype])
```  
Summary  
  
Enables `ComplexNDArray /= ComplexSIMD`.  
  
Args:  

- self
- other


```rust
__itruediv__(mut self, other: SIMD[dtype, 1])
```  
Summary  
  
Enables `ComplexNDArray /= Scalar`.  
  
Args:  

- self
- other


```rust
__itruediv__(mut self, other: Self)
```  
Summary  
  
Enables `ComplexNDArray /= ComplexNDArray`.  
  
Args:  

- self
- other


```rust
__itruediv__(mut self, other: NDArray[dtype])
```  
Summary  
  
Enables `ComplexNDArray /= NDArray`.  
  
Args:  

- self
- other

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
  
Compute the "official" string representation of ComplexNDArray. An example is: ``` fn main() raises:     var A = ComplexNDArray[cf32](List[ComplexSIMD[cf32]](14,97,-59,-4,112,), shape=List[Int](5,))     print(repr(A)) ``` It prints what can be used to construct the array itself: ```console     ComplexNDArray[cf32](List[ComplexSIMD[cf32]](14,97,-59,-4,112,), shape=List[Int](5,)) ```.  
  
Args:  

- self

#### __len__


```rust
__len__(self) -> Int
```  
Summary  
  
  
  
Args:  

- self

#### load


```rust
load[width: Int = 1](self, index: Int) -> ComplexSIMD[cdtype, dtype=dtype]
```  
Summary  
  
Safely loads a SIMD element of size `width` at `index` from the underlying buffer.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- index


```rust
load[width: Int = 1](self, *indices: Int) -> ComplexSIMD[cdtype, dtype=dtype]
```  
Summary  
  
Safely loads a SIMD element of size `width` at given variadic indices from the underlying buffer.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- \*indices

#### store


```rust
store[width: Int = 1](mut self, index: Int, val: ComplexSIMD[cdtype, dtype=dtype])
```  
Summary  
  
Safely stores SIMD element of size `width` at `index` of the underlying buffer.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- index
- val


```rust
store[width: Int = 1](mut self, *indices: Int, *, val: ComplexSIMD[cdtype, dtype=dtype])
```  
Summary  
  
Safely stores SIMD element of size `width` at given variadic indices of the underlying buffer.  
  
Parameters:  

- width Defualt: `1`
  
Args:  

- self
- \*indices
- val

#### item


```rust
item(self, owned index: Int) -> ComplexSIMD[cdtype, dtype=dtype]
```  
Summary  
  
Return the scalar at the coordinates.  
  
Args:  

- self
- index: Index of item, counted in row-major way.


```rust
item(self, *index: Int) -> ComplexSIMD[cdtype, dtype=dtype]
```  
Summary  
  
Return the scalar at the coordinates.  
  
Args:  

- self
- \*index: The coordinates of the item.

#### itemset


```rust
itemset(mut self, index: Variant[Int, List[Int]], item: ComplexSIMD[cdtype, dtype=dtype])
```  
Summary  
  
Set the scalar at the coordinates.  
  
Args:  

- self
- index: The coordinates of the item. Can either be `Int` or `List[Int]`. If `Int` is passed, it is the index of i-th item of the whole array. If `List[Int]` is passed, it is the coordinate of the item.
- item: The scalar to be set.

#### conj


```rust
conj(self) -> Self
```  
Summary  
  
Return the complex conjugate of the ComplexNDArray.  
  
Args:  

- self

#### to_ndarray


```rust
to_ndarray(self, type: String = String("re")) -> NDArray[dtype]
```  
Summary  
  
  
  
Args:  

- self
- type Default: String("re")
