# `numojo.core.layout.ndshape`

NDArrayShape (numojo.core.layout.ndshape)

Implements NDArrayShape type representing the shape of an NDArray.
The shape is stored as a contiguous buffer of integers, with the number of dimensions (ndim) tracked separately.
The NDArrayShape provides methods for element access, shape transformations (e.g., permute, reverse),
and properties like size and rank.

## Structs

### `NDArrayShape`

```mojo
struct NDArrayShape
```

**Memory convention:** `register_passable`  
**Implements:** `AnyType`, `Copyable`, `Equatable`, `ImplicitlyCopyable`, `ImplicitlyDestructible`, `Movable`, `RegisterPassable`, `Representable`, `Sized`, `Stringable`, `Writable`

Presents the shape of `NDArray` type.

The data buffer of the NDArrayShape is a series of `Int` on memory.
The number of elements in the shape must be positive.
The elements of the shape must be positive.
The number of dimension and values of elements are checked upon
creation of the shape.

Example:
```mojo
import numojo as nm
var shape1 = nm.Shape(2, 3, 4)
print(shape1)  # Shape: (2, 3, 4)
var shape2 = nm.Shape([5, 6, 7])
print(shape2)  # Shape: (5, 6, 7)
```

#### Fields

- **`ndim`** (`Int`): Number of dimensions of array. It must be larger than 0.

#### Aliases

##### `element_type`

```mojo
comptime element_type
```

**Value:** `DType.int`

The data type of the NDArrayShape elements.

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `False`

##### `__move_ctor_is_trivial`

```mojo
comptime __move_ctor_is_trivial
```

**Value:** `True`

##### `__copy_ctor_is_trivial`

```mojo
comptime __copy_ctor_is_trivial
```

**Value:** `False`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
__init__() -> Self
```

<span class="badge badge-static">static</span>

Initializes an empty NDArrayShape.

**Returns:**

- `Self`

###### Overload 2

```mojo
__init__(var buf: IndexBuffer) -> Self
```

<span class="badge badge-static">static</span>

Initializes the NDArrayShape from an IndexBuffer.

**Args:**

- `buf` (`IndexBuffer`) `[var]`: The IndexBuffer to initialize from.

**Returns:**

- `Self`

###### Overload 3

```mojo
__init__(out self, *shape: Int)
```

<span class="badge badge-static">static</span>

Initializes the NDArrayShape with variable shape dimensions.

**Args:**

- `*shape` (`Int`): Variable number of integers representing the shape dimensions.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If any shape dimension is not positive.

###### Overload 4

```mojo
__init__(out self, shape: List[Int])
```

<span class="badge badge-static">static</span>

Initializes the NDArrayShape with a list of shape dimensions.

**Args:**

- `shape` (`List`): A list of integers representing the shape dimensions.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the number of dimensions is not positive.
Error: If any shape dimension is not positive.

###### Overload 5

```mojo
__init__(out self, shape: VariadicList[Int])
```

<span class="badge badge-static">static</span>

Initializes the NDArrayShape with a list of shape dimensions.

**Args:**

- `shape` (`VariadicList`): A variadic list of integers representing the shape dimensions.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the number of dimensions is not positive.
Error: If any shape dimension is not positive.

###### Overload 6

```mojo
__init__(shape: Self) -> Self
```

<span class="badge badge-static">static</span>

Initializes the NDArrayShape from another NDArrayShape. A deep copy of the data buffer is conducted.

**Args:**

- `shape` (`Self`): Another NDArrayShape to initialize from.

**Returns:**

- `Self`

###### Overload 7

```mojo
__init__(out self, *, ndim: Int, initialized: Bool)
```

<span class="badge badge-static">static</span>

Construct NDArrayShape with number of dimensions. This method is useful when you want to create a shape with given ndim without knowing the shape values. `ndim == 0` is allowed in this method for 0darray (numojo scalar).

Note:
After creating the shape with uninitialized values,
you must set the values before using it! Otherwise, it may lead to undefined behavior.

**Args:**

- `ndim` (`Int`): Number of dimensions.
- `initialized` (`Bool`): Whether the shape is initialized.
    If yes, the values will be set to 1.
    If no, the values will be uninitialized.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the number of dimensions is negative.

###### Overload 8

```mojo
__init__(*, copy: Self) -> Self
```

<span class="badge badge-static">static</span>

Initializes the NDArrayShape from ancopy NDArrayShape. A deep copy of the data buffer is conducted.

**Args:**

- `copy` (`Self`): Ancopy NDArrayShape to initialize from.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

###### Overload 1

```mojo
__getitem__(self, index: Int) -> Int
```

Gets shape dimension at specified index.

**Args:**

- `self` (`Self`)
- `index` (`Int`): Index to get the shape.

**Returns:**

- `Int`

!!! failure "Raises"
    Error: Index out of bound.

###### Overload 2

```mojo
__getitem__(self, index: Scalar[DType.int]) -> Scalar[DType.int]
```

Gets shape dimension at specified index.

**Args:**

- `self` (`Self`)
- `index` (`Scalar`): Index to get the shape.

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 3

```mojo
__getitem__(self, slice_index: Slice) -> Self
```

Return a sliced view of the dimension tuple as a new NDArrayShape.

**Args:**

- `self` (`Self`)
- `slice_index` (`Slice`): Slice object defining the sub-buffer.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__setitem__`

###### Overload 1

```mojo
__setitem__(mut self, index: Scalar[DType.int], val: Scalar[DType.int])
```

Sets shape at specified index.

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`Scalar`): Index to set the shape.
- `val` (`Scalar`): Value to set at the given index.

!!! failure "Raises"
    Error: Index out of bound.

###### Overload 2

```mojo
__setitem__(mut self, index: Int, val: Int)
```

Sets shape at specified index.

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`Int`): Index to set the shape.
- `val` (`Int`): Value to set at the given index.

!!! failure "Raises"
    Error: Index out of bound.


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
__eq__(self, other: Self) -> Bool
```

Checks if two shapes have identical dimensions and values.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The shape to compare with.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
__ne__(self, other: Self) -> Bool
```

Checks if two shapes have identical dimensions and values.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The shape to compare with.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__contains__`

###### Overload 1

```mojo
__contains__(self, val: Int) -> Bool
```

Checks if the given value is present in the shape dimensions.

**Args:**

- `self` (`Self`)
- `val` (`Int`): The value to search for.

**Returns:**

- `Bool`

###### Overload 2

```mojo
__contains__(self, val: Scalar[DType.int]) -> Bool
```

Check if the NDArrayShape contains the given value.

**Args:**

- `self` (`Self`)
- `val` (`Scalar`): Value to check for.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `load`

```mojo
load[width: Int = 1](self, idx: Int) -> SIMD[DType.int, width]
```

Load a SIMD vector from the Shape at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The starting index to load from.

**Returns:**

- `SIMD`

!!! failure "Raises"
    Error: If the load exceeds the bounds of the Shape.


</div>

<div class="fn-card" markdown="1">

##### `store`

```mojo
store[width: Int = 1](self, idx: Int, value: SIMD[DType.int, width])
```

Store a SIMD vector into the Shape at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The starting index to store to.
- `value` (`SIMD`): The SIMD vector to store.

!!! failure "Raises"
    Error: If the store exceeds the bounds of the Shape.


</div>

<div class="fn-card" markdown="1">

##### `unsafe_load`

```mojo
unsafe_load[width: Int = 1](self, idx: Int) -> SIMD[DType.int, width]
```

Unsafely load a SIMD vector from the Shape at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The starting index to load from.

**Returns:**

- `SIMD`


</div>

<div class="fn-card" markdown="1">

##### `unsafe_store`

```mojo
unsafe_store[width: Int = 1](self, idx: Int, value: SIMD[DType.int, width])
```

Unsafely store a SIMD vector into the Shape at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The starting index to store to.
- `value` (`SIMD`): The SIMD vector to store.


</div>

<div class="fn-card" markdown="1">

##### `row_major`

```mojo
row_major(self) -> NDArrayStrides
```

Create row-major (C-style) strides from a shape.

Row-major means the last dimension has stride 1 and strides increase
going backwards through dimensions.

**Args:**

- `self` (`Self`)

**Returns:**

- `NDArrayStrides`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `col_major`

```mojo
col_major(self) -> NDArrayStrides
```

Create column-major (Fortran-style) strides from a shape.

Column-major means the first dimension has stride 1 and strides increase
going forward through dimensions.

**Args:**

- `self` (`Self`)

**Returns:**

- `NDArrayStrides`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `reverse`

```mojo
reverse(self) -> Self
```

Return a new shape with dimensions reversed.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `permute`

```mojo
permute(self, axes: List[Int]) -> Self
```

Return a new shape with axes reordered.

**Args:**

- `self` (`Self`)
- `axes` (`List`): New axis order. Must contain each axis exactly once.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If axes length doesn't match ndim or contains invalid/duplicate axes.


</div>

<div class="fn-card" markdown="1">

##### `join`

```mojo
join(self, *shapes: Self) -> Self
```

Join multiple shapes into a single shape.

**Args:**

- `self` (`Self`)
- `*shapes` (`Self`): Variable number of NDArrayShape objects.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `swapaxes`

```mojo
swapaxes(self, axis1: Int, axis2: Int) -> Self
```

Returns a new shape with the given axes swapped.

**Args:**

- `self` (`Self`)
- `axis1` (`Int`): The first axis to swap.
- `axis2` (`Int`): The second axis to swap.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `extend`

```mojo
extend(self, *values: Int) -> Self
```

Extend the shape by sizes of extended dimensions.

**Args:**

- `self` (`Self`)
- `*values` (`Int`): Sizes of extended dimensions.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `flip`

```mojo
flip(mut self)
```

Flip the items in-place.

**Args:**

- `self` (`Self`) `[mut]`


</div>

<div class="fn-card" markdown="1">

##### `flipped`

```mojo
flipped(self) -> Self
```

Returns a new shape by flipping the items.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `move_axis_to_end`

```mojo
move_axis_to_end(self, axis: Int) -> Self
```

Returns a new shape by moving the value of axis to the end.

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis (index) to move.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `pop`

```mojo
pop(self, axis: Int) -> Self
```

Drops the item at the given axis (index).

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis (index) to drop.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `rank`

```mojo
rank(self) -> Int
```

Returns the number of dimensions of the shape.

**Args:**

- `self` (`Self`)

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `size`

```mojo
size(self) -> Int
```

Returns the total number of elements in the array.

**Args:**

- `self` (`Self`)

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `sum`

```mojo
sum(self) -> Scalar[DType.int]
```

Compute the sum of all elements in NDArrayShape.

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`


</div>

<div class="fn-card" markdown="1">

##### `product`

```mojo
product(self) -> Scalar[DType.int]
```

Compute the product of all elements in the IndexBuffer.

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`


</div>

<div class="fn-card" markdown="1">

##### `__len__`

```mojo
__len__(self) -> Int
```

Gets number of elements in the shape. It equals the number of dimensions of the array.

**Args:**

- `self` (`Self`)

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `__repr__`

```mojo
__repr__(self) -> String
```

Returns a string of the shape of the array.

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
__str__(self) -> String
```

Returns a string of the shape of the array.

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `write_to`

```mojo
write_to[W: Writer](self, mut writer: W)
```

Writes the shape representation to a writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

##### `tolist`

```mojo
tolist(self) -> List[Int]
```

Convert the shape to a list of integers.

**Args:**

- `self` (`Self`)

**Returns:**

- `List`


</div>

<div class="fn-card" markdown="1">

##### `normalize_index`

```mojo
normalize_index(self, index: Int) -> Int
```

Normalizes the given index to be within the valid range [0, ndim).

**Args:**

- `self` (`Self`)
- `index` (`Int`): The index to normalize.

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `__iter__`

```mojo
__iter__(ref self) -> _ShapeIter[origin_of(self)]
```

Iterate over elements of the NDArrayShape, returning copied values.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_ShapeIter`


</div>

<div class="fn-card" markdown="1">

##### `__reversed__`

```mojo
__reversed__(ref self) -> _ShapeIter[origin_of(self), False]
```

Iterate over elements of the NDArrayShape in reverse order, returning copied values.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_ShapeIter`


</div>
