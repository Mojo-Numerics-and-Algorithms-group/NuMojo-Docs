# `numojo.core.layout.ndstrides`

Memory layout and indexing strides.

Represents memory strides for calculating offsets when indexing into arrays.
For example, strides [12, 4] mean each element in dimension 1 is 12 bytes apart,
and each element in dimension 2 is 4 bytes apart.

Exports
-------
- `NDArrayStrides`: Stride container for memory layout.

Notes:
    - The number of elements in the strides must match the number of dimensions.
    - Strides are validated upon creation to ensure correctness.

## Structs

### `NDArrayStrides`

```mojo
struct NDArrayStrides
```

**Memory convention:** `register_passable`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Equatable`, `ImplicitlyCopyable`, `Movable`, `RegisterPassable`, `Sized`, `Writable`

Represents the strides (memory layout) of an NDArray.

Strides are stored as a series of `Int` values in memory and define how to traverse
array elements in memory for efficient indexing and iteration.

#### Fields

- **`ndim`** (`Int`): Number of dimensions of array. It must be larger than 0.

#### Aliases

##### `element_type`

```mojo
comptime element_type
```

**Value:** `DType.int`

The data type of the NDArrayStrides elements.

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
def __init__() -> Self
```

<span class="badge badge-static">static</span>

Initializes an empty NDArrayStrides.

**Returns:**

- `Self`

###### Overload 2

```mojo
def __init__(buf: IndexBuffer) -> Self
```

<span class="badge badge-static">static</span>

Initializes the NDArrayStrides from an IndexBuffer.

**Args:**

- `buf` (`IndexBuffer`) `[imm]`: The IndexBuffer to initialize from.

**Returns:**

- `Self`

###### Overload 3

```mojo
def __init__(out self, *strides: Int)
```

<span class="badge badge-static">static</span>

Initializes the NDArrayStrides from strides.

**Args:**

- `*strides` (`Int`) `[imm]`: Strides of the array.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the number of dimensions is not positive.

###### Overload 4

```mojo
def __init__(out self, strides: List[Int])
```

<span class="badge badge-static">static</span>

Initializes the NDArrayStrides from a list of strides.

**Args:**

- `strides` (`List[Int]`) `[imm]`: Strides of the array.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the number of dimensions is not positive.

###### Overload 5

```mojo
def __init__(out self, strides: VariadicList[Int])
```

<span class="badge badge-static">static</span>

Initializes the NDArrayStrides from a variadic list of strides.

**Args:**

- `strides` (`VariadicList[Int]`) `[imm]`: Strides of the array.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the number of dimensions is not positive.

###### Overload 6

```mojo
def __init__(strides: Self) -> Self
```

<span class="badge badge-static">static</span>

Initializes the NDArrayStrides from another strides. A deep-copy of the elements is conducted.

**Args:**

- `strides` (`Self`) `[imm]`: Strides of the array.

**Returns:**

- `Self`

###### Overload 7

```mojo
def __init__(out self, shape: NDArrayShape, order: String = "C")
```

<span class="badge badge-static">static</span>

Initializes the NDArrayStrides from a shape and an order.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: Shape of the array.
- `order` (`String`) `[imm]`: Order of the memory layout
    (row-major "C" or column-major "F").
    Default is "C".
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the order argument is not `C` or `F`.

###### Overload 8

```mojo
def __init__(out self, *shape: Int, *, order: String)
```

<span class="badge badge-static">static</span>

Overloads the function `__init__(shape: NDArrayStrides, order: String)`. Initializes the NDArrayStrides from a given shapes and an order.

**Args:**

- `*shape` (`Int`) `[imm]`: Shape of the array.
- `order` (`String`) `[imm]`: Order of the memory layout
    (row-major "C" or column-major "F").
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the order argument is not `C` or `F`.

###### Overload 9

```mojo
def __init__(out self, shape: List[Int], order: String = "C")
```

<span class="badge badge-static">static</span>

Overloads the function `__init__(shape: NDArrayStrides, order: String)`. Initializes the NDArrayStrides from a given shapes and an order.

**Args:**

- `shape` (`List[Int]`) `[imm]`: Shape of the array.
- `order` (`String`) `[imm]`: Order of the memory layout
    (row-major "C" or column-major "F").
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the order argument is not `C` or `F`.

###### Overload 10

```mojo
def __init__(out self, shape: VariadicList[Int], order: String = "C")
```

<span class="badge badge-static">static</span>

Overloads the function `__init__(shape: NDArrayStrides, order: String)`. Initializes the NDArrayStrides from a given shapes and an order.

**Args:**

- `shape` (`VariadicList[Int]`) `[imm]`: Shape of the array.
- `order` (`String`) `[imm]`: Order of the memory layout
    (row-major "C" or column-major "F").
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the order argument is not `C` or `F`.

###### Overload 11

```mojo
def __init__(out self, *, ndim: Int, initialized: Bool)
```

<span class="badge badge-static">static</span>

Construct NDArrayStrides with number of dimensions. This method is useful when you want to create a strides with given ndim without knowing the strides values. `ndim == 0` is allowed in this method for 0darray (numojo scalar).

**Args:**

- `ndim` (`Int`) `[imm]`: Number of dimensions.
- `initialized` (`Bool`) `[imm]`: Whether the strides is initialized.
    If yes, the values will be set to 0.
    If no, the values will be uninitialized.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the number of dimensions is negative.

###### Overload 12

```mojo
def __init__(*, copy: Self) -> Self
```

<span class="badge badge-static">static</span>

Initializes the NDArrayStrides from ancopy strides. A deep-copy of the elements is conducted.

**Args:**

- `copy` (`Self`) `[imm]`: Strides of the array.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

###### Overload 1

```mojo
def __getitem__(self, index: Int) -> Int
```

Gets stride at specified index.

**Args:**

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[imm]`: Index to get the shape.

**Returns:**

- `Int`

!!! failure "Raises"

###### Overload 2

```mojo
def __getitem__(self, slice_index: Slice) -> Self
```

Return a sliced view of the strides as a new NDArrayStrides.

**Args:**

- `self` (`Self`) `[imm]`
- `slice_index` (`Slice`) `[imm]`: Slice object defining the sub-buffer.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__setitem__`

```mojo
def __setitem__(mut self, index: Int, val: Int)
```

Sets stride at specified index.

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`Int`) `[imm]`: Index to set the stride.
- `val` (`Int`) `[imm]`: Value to set at the given index.

!!! failure "Raises"
    NumojoError: Index out of bound.


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
def __eq__(self, other: Self) -> Bool
```

Checks if two strides have identical dimensions and values.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The strides to compare with.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
def __ne__(self, other: Self) -> Bool
```

Checks if two strides have identical dimensions and values.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The strides to compare with.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__contains__`

```mojo
def __contains__(self, val: Int) -> Bool
```

Check if the NDArrayStrides contains the given value.

**Args:**

- `self` (`Self`) `[imm]`
- `val` (`Int`) `[imm]`: Value to check for.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `load`

```mojo
def load[width: Int = Int(1)](self, idx: Int) -> SIMD[DType.int, width]
```

Load a SIMD vector from the Strides at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: The starting index to load from.

**Returns:**

- `SIMD[DType.int, width]`

!!! failure "Raises"
    NumojoError: If the load exceeds the bounds of the Strides.


</div>

<div class="fn-card" markdown="1">

##### `store`

```mojo
def store[width: Int = Int(1)](self, idx: Int, value: SIMD[DType.int, width])
```

Store a SIMD vector into the Strides at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: The starting index to store to.
- `value` (`SIMD[DType.int, width]`) `[imm]`: The SIMD vector to store.

!!! failure "Raises"
    NumojoError: If the store exceeds the bounds of the Strides.


</div>

<div class="fn-card" markdown="1">

##### `unsafe_load`

```mojo
def unsafe_load[width: Int = Int(1)](self, idx: Int) -> SIMD[DType.int, width]
```

Unsafely load a SIMD vector from the Strides at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: The starting index to load from.

**Returns:**

- `SIMD[DType.int, width]`


</div>

<div class="fn-card" markdown="1">

##### `unsafe_store`

```mojo
def unsafe_store[width: Int = Int(1)](self, idx: Int, value: SIMD[DType.int, width])
```

Unsafely store a SIMD vector into the Strides at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: The starting index to store to.
- `value` (`SIMD[DType.int, width]`) `[imm]`: The SIMD vector to store.


</div>

<div class="fn-card" markdown="1">

##### `unsafe_get`

```mojo
def unsafe_get(self, idx: Int) -> Int
```

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `unsafe_set`

```mojo
def unsafe_set(mut self, idx: Int, value: Int)
```

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Int`) `[imm]`
- `value` (`Int`) `[imm]`


</div>

<div class="fn-card" markdown="1">

##### `permute`

```mojo
def permute(self, axes: List[Int]) -> Self
```

Return new strides with axes reordered.

**Args:**

- `self` (`Self`) `[imm]`
- `axes` (`List[Int]`) `[imm]`: New axis order. Must contain each axis exactly once.

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If axes length doesn't match ndim or contains invalid/duplicate axes.


</div>

<div class="fn-card" markdown="1">

##### `swapaxes`

```mojo
def swapaxes(self, axis1: Int, axis2: Int) -> Self
```

Returns a new strides with the given axes swapped.

**Args:**

- `self` (`Self`) `[imm]`
- `axis1` (`Int`) `[imm]`: The first axis to swap.
- `axis2` (`Int`) `[imm]`: The second axis to swap.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `join`

```mojo
def join(self, *strides: Self) -> Self
```

Join multiple strides into a single strides.

**Args:**

- `self` (`Self`) `[imm]`
- `*strides` (`Self`) `[imm]`: Variable number of NDArrayStrides objects.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `extend`

```mojo
def extend(self, *values: Int) -> Self
```

Extend the shape by sizes of extended dimensions.

**Args:**

- `self` (`Self`) `[imm]`
- `*values` (`Int`) `[imm]`: Sizes of extended dimensions.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `flip`

```mojo
def flip(mut self)
```

Flip the items in-place.

**Args:**

- `self` (`Self`) `[mut]`


</div>

<div class="fn-card" markdown="1">

##### `flipped`

```mojo
def flipped(self) -> Self
```

Returns a new strides by flipping the items.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `move_axis_to_end`

```mojo
def move_axis_to_end(self, axis: Int) -> Self
```

Returns a new strides by moving the value of axis to the end.

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis (index) to move.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `pop`

```mojo
def pop(self, axis: Int) -> Self
```

Drops information of certain axis.

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis (index) to drop.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `is_contiguous`

```mojo
def is_contiguous(self, shape: NDArrayShape) -> Bool
```

Check if strides represent a contiguous layout for the shape.

**Args:**

- `self` (`Self`) `[imm]`
- `shape` (`NDArrayShape`) `[imm]`: The shape of the array.

**Returns:**

- `Bool`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__len__`

```mojo
def __len__(self) -> Int
```

Gets number of elements in the strides. It equals to the number of dimensions of the array.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `__repr__`

```mojo
def __repr__(self) -> String
```

Returns a string of the strides of the array.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
def __str__(self) -> String
```

Returns a string of the strides of the array.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `write_repr_to`

```mojo
def write_repr_to[W: Writer](self, mut writer: W)
```

Write the string representation to a writer.

**Parameters:**

- `W` (`Writer`): The writer type.

**Args:**

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

##### `write_to`

```mojo
def write_to[W: Writer](self, mut writer: W)
```

Writes the strides representation to a writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

##### `row_major`

```mojo
def row_major(shape: NDArrayShape) -> Self
```

<span class="badge badge-static">static</span>

Create row-major (C-style) strides from a shape.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: The shape of the array.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `col_major`

```mojo
def col_major(shape: NDArrayShape) -> Self
```

<span class="badge badge-static">static</span>

Create column-major (Fortran-style) strides from a shape.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: The shape of the array.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `default`

```mojo
def default(shape: NDArrayShape) -> Self
```

<span class="badge badge-static">static</span>

Create default (row-major) strides from a shape.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: The shape of the array.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `tolist`

```mojo
def tolist(self) -> List[Int]
```

Convert the strides to a list of integers.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `List[Int]`


</div>

<div class="fn-card" markdown="1">

##### `normalize_index`

```mojo
def normalize_index(self, index: Int) -> Int
```

Normalizes the given index to be within the valid range [0, ndim).

**Args:**

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[imm]`: The index to normalize.

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `__iter__`

```mojo
def __iter__(ref self) -> _StrideIter[origin_of(self)]
```

Iterate over elements of the NDArrayStrides, returning copied values.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_StrideIter[origin_of(self)]`


</div>

<div class="fn-card" markdown="1">

##### `__reversed__`

```mojo
def __reversed__(ref self) -> _StrideIter[origin_of(self), False]
```

Iterate over elements of the NDArrayStrides, returning copied values.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_StrideIter[origin_of(self), False]`


</div>
