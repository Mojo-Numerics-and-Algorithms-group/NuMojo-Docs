# `numojo.core.layout.ndstrides`

NDArrayStrides (numojo.core.layout.ndstrides)

Implements NDArrayStrides type. NDArrayStrides represents the strides of an NDArray,
which is used to calculate the memory offset for each dimension when indexing into the array.

## Structs

### `NDArrayStrides`

```mojo
struct NDArrayStrides
```

**Memory convention:** `register_passable`  
**Implements:** `AnyType`, `Copyable`, `Equatable`, `ImplicitlyCopyable`, `ImplicitlyDestructible`, `Movable`, `RegisterPassable`, `Representable`, `Sized`, `Stringable`, `Writable`

Presents the strides of `NDArray` type.

The data buffer of the NDArrayStrides is a series of `Int` on memory.
The number of elements in the strides must be positive.
The number of dimension is checked upon creation of the strides.

#### Fields

- **`ndim`** (`Int`): Number of dimensions of array. It must be larger than 0.

#### Aliases

##### `element_type`

```mojo
comptime element_type
```

**Value:** `DType.int`

The data type of the NDArrayStrides elements.

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

Initializes an empty NDArrayStrides.

**Returns:**

- `Self`

###### Overload 2

```mojo
__init__(buf: IndexBuffer) -> Self
```

<span class="badge badge-static">static</span>

Initializes the NDArrayStrides from an IndexBuffer.

**Args:**

- `buf` (`IndexBuffer`): The IndexBuffer to initialize from.

**Returns:**

- `Self`

###### Overload 3

```mojo
__init__(out self, *strides: Int)
```

<span class="badge badge-static">static</span>

Initializes the NDArrayStrides from strides.

**Args:**

- `*strides` (`Int`): Strides of the array.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the number of dimensions is not positive.

###### Overload 4

```mojo
__init__(out self, strides: List[Int])
```

<span class="badge badge-static">static</span>

Initializes the NDArrayStrides from a list of strides.

**Args:**

- `strides` (`List`): Strides of the array.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the number of dimensions is not positive.

###### Overload 5

```mojo
__init__(out self, strides: VariadicList[Int])
```

<span class="badge badge-static">static</span>

Initializes the NDArrayStrides from a variadic list of strides.

**Args:**

- `strides` (`VariadicList`): Strides of the array.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the number of dimensions is not positive.

###### Overload 6

```mojo
__init__(strides: Self) -> Self
```

<span class="badge badge-static">static</span>

Initializes the NDArrayStrides from another strides. A deep-copy of the elements is conducted.

**Args:**

- `strides` (`Self`): Strides of the array.

**Returns:**

- `Self`

###### Overload 7

```mojo
__init__(out self, shape: NDArrayShape, order: String = "C")
```

<span class="badge badge-static">static</span>

Initializes the NDArrayStrides from a shape and an order.

**Args:**

- `shape` (`NDArrayShape`): Shape of the array.
- `order` (`String`): Order of the memory layout
    (row-major "C" or column-major "F").
    Default is "C".
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    ValueError: If the order argument is not `C` or `F`.

###### Overload 8

```mojo
__init__(out self, *shape: Int, *, order: String)
```

<span class="badge badge-static">static</span>

Overloads the function `__init__(shape: NDArrayStrides, order: String)`. Initializes the NDArrayStrides from a given shapes and an order.

**Args:**

- `*shape` (`Int`): Shape of the array.
- `order` (`String`): Order of the memory layout
    (row-major "C" or column-major "F").
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    ValueError: If the order argument is not `C` or `F`.

###### Overload 9

```mojo
__init__(out self, shape: List[Int], order: String = "C")
```

<span class="badge badge-static">static</span>

Overloads the function `__init__(shape: NDArrayStrides, order: String)`. Initializes the NDArrayStrides from a given shapes and an order.

**Args:**

- `shape` (`List`): Shape of the array.
- `order` (`String`): Order of the memory layout
    (row-major "C" or column-major "F").
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    ValueError: If the order argument is not `C` or `F`.

###### Overload 10

```mojo
__init__(out self, shape: VariadicList[Int], order: String = "C")
```

<span class="badge badge-static">static</span>

Overloads the function `__init__(shape: NDArrayStrides, order: String)`. Initializes the NDArrayStrides from a given shapes and an order.

**Args:**

- `shape` (`VariadicList`): Shape of the array.
- `order` (`String`): Order of the memory layout
    (row-major "C" or column-major "F").
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    ValueError: If the order argument is not `C` or `F`.

###### Overload 11

```mojo
__init__(out self, *, ndim: Int, initialized: Bool)
```

<span class="badge badge-static">static</span>

Construct NDArrayStrides with number of dimensions. This method is useful when you want to create a strides with given ndim without knowing the strides values. `ndim == 0` is allowed in this method for 0darray (numojo scalar).

**Args:**

- `ndim` (`Int`): Number of dimensions.
- `initialized` (`Bool`): Whether the strides is initialized.
    If yes, the values will be set to 0.
    If no, the values will be uninitialized.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the number of dimensions is negative.

###### Overload 12

```mojo
__init__(*, copy: Self) -> Self
```

<span class="badge badge-static">static</span>

Initializes the NDArrayStrides from ancopy strides. A deep-copy of the elements is conducted.

**Args:**

- `copy` (`Self`): Strides of the array.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

###### Overload 1

```mojo
__getitem__(self, index: Int) -> Int
```

Gets stride at specified index.

**Args:**

- `self` (`Self`)
- `index` (`Int`): Index to get the stride.

**Returns:**

- `Int`

!!! failure "Raises"

###### Overload 2

```mojo
__getitem__(self, index: Scalar[DType.int]) -> Scalar[DType.int]
```

Gets stride at specified index.

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

Return a sliced view of the strides as a new NDArrayStrides.

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

Sets stride at specified index.

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`Scalar`): Index to set the stride.
- `val` (`Scalar`): Value to set at the given index.

!!! failure "Raises"
    Error: Index out of bound.

###### Overload 2

```mojo
__setitem__(mut self, index: Int, val: Int)
```

Sets stride at specified index.

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

Checks if two strides have identical dimensions and values.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The strides to compare with.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
__ne__(self, other: Self) -> Bool
```

Checks if two strides have identical dimensions and values.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The strides to compare with.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__contains__`

###### Overload 1

```mojo
__contains__(self, val: Int) -> Bool
```

Checks if the given value is present in the strides.

**Args:**

- `self` (`Self`)
- `val` (`Int`): The value to search for.

**Returns:**

- `Bool`

###### Overload 2

```mojo
__contains__(self, val: Scalar[DType.int]) -> Bool
```

Check if the NDArrayStrides contains the given value.

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

Load a SIMD vector from the Strides at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The starting index to load from.

**Returns:**

- `SIMD`

!!! failure "Raises"
    Error: If the load exceeds the bounds of the Strides.


</div>

<div class="fn-card" markdown="1">

##### `store`

```mojo
store[width: Int = 1](self, idx: Int, value: SIMD[DType.int, width])
```

Store a SIMD vector into the Strides at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The starting index to store to.
- `value` (`SIMD`): The SIMD vector to store.

!!! failure "Raises"
    Error: If the store exceeds the bounds of the Strides.


</div>

<div class="fn-card" markdown="1">

##### `unsafe_load`

```mojo
unsafe_load[width: Int = 1](self, idx: Int) -> SIMD[DType.int, width]
```

Unsafely load a SIMD vector from the Strides at the specified index.

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

Unsafely store a SIMD vector into the Strides at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The starting index to store to.
- `value` (`SIMD`): The SIMD vector to store.


</div>

<div class="fn-card" markdown="1">

##### `permute`

```mojo
permute(self, axes: List[Int]) -> Self
```

Return new strides with axes reordered.

**Args:**

- `self` (`Self`)
- `axes` (`List`): New axis order. Must contain each axis exactly once.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If axes length doesn't match ndim or contains invalid/duplicate axes.


</div>

<div class="fn-card" markdown="1">

##### `swapaxes`

```mojo
swapaxes(self, axis1: Int, axis2: Int) -> Self
```

Returns a new strides with the given axes swapped.

**Args:**

- `self` (`Self`)
- `axis1` (`Int`): The first axis to swap.
- `axis2` (`Int`): The second axis to swap.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `join`

```mojo
join(self, *strides: Self) -> Self
```

Join multiple strides into a single strides.

**Args:**

- `self` (`Self`)
- `*strides` (`Self`): Variable number of NDArrayStrides objects.

**Returns:**

- `Self`


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

Returns a new strides by flipping the items.

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

Returns a new strides by moving the value of axis to the end.

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

Drops information of certain axis.

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis (index) to drop.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `is_contiguous`

```mojo
is_contiguous(self, shape: NDArrayShape) -> Bool
```

Check if strides represent a contiguous layout for the shape.

**Args:**

- `self` (`Self`)
- `shape` (`NDArrayShape`): The shape of the array.

**Returns:**

- `Bool`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__len__`

```mojo
__len__(self) -> Int
```

Gets number of elements in the strides. It equals to the number of dimensions of the array.

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

Returns a string of the strides of the array.

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

Returns a string of the strides of the array.

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

Writes the strides representation to a writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

##### `row_major`

```mojo
row_major(shape: NDArrayShape) -> Self
```

<span class="badge badge-static">static</span>

Create row-major (C-style) strides from a shape.

**Args:**

- `shape` (`NDArrayShape`): The shape of the array.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `col_major`

```mojo
col_major(shape: NDArrayShape) -> Self
```

<span class="badge badge-static">static</span>

Create column-major (Fortran-style) strides from a shape.

**Args:**

- `shape` (`NDArrayShape`): The shape of the array.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `default`

```mojo
default(shape: NDArrayShape) -> Self
```

<span class="badge badge-static">static</span>

Create default (row-major) strides from a shape.

**Args:**

- `shape` (`NDArrayShape`): The shape of the array.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `tolist`

```mojo
tolist(self) -> List[Int]
```

Convert the strides to a list of integers.

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
__iter__(ref self) -> _StrideIter[origin_of(self)]
```

Iterate over elements of the NDArrayStrides, returning copied values.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_StrideIter`


</div>

<div class="fn-card" markdown="1">

##### `__reversed__`

```mojo
__reversed__(ref self) -> _StrideIter[origin_of(self), False]
```

Iterate over elements of the NDArrayStrides, returning copied values.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_StrideIter`


</div>
