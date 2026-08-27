# `numojo.core.indexing.item`

Multi-dimensional index representation for N-dimensional array access.

The `Item` struct holds a sequence of integer indices (one per dimension) used to specify
coordinates within an N-dimensional array. For example, `arr[Item(1, 2, 3)]` accesses
element at position (1, 2, 3) in a 3D array.

Notes:
    - Each Item instance is backed by a heap-allocated IndexBuffer.
    - Indices are stored as a series of Int values.
    - Item can be used for arbitrary-dimensional array indexing.

Exports
-------
- `Item`: Array item indexing.

## Structs

### `Item`

```mojo
struct Item
```

**Memory convention:** `register_passable`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Equatable`, `ImplicitlyCopyable`, `Movable`, `RegisterPassable`, `Sized`, `Writable`

Represents a multi-dimensional index for array access.

The `Item` struct is used to specify the coordinates of an element within an N-dimensional array.
For example, `arr[Item(1, 2, 3)]` retrieves the element at position (1, 2, 3) in a 3D array.

Each `Item` instance holds a sequence of integer indices, one for each dimension of the array.
This allows for precise and flexible indexing into arrays of arbitrary dimensionality.

Example:
```mojo
from numojo.prelude import *
import numojo as nm
var arr = nm.arange[f32](0, 27).reshape(Shape(3, 3, 3))
var value = arr[Item(1, 2, 3)]  # Accesses arr[1, 2, 3]
```

#### Fields

- **`ndim`** (`Int`): Number of dimensions (length of the index tuple).

#### Aliases

##### `element_type`

```mojo
comptime element_type
```

**Value:** `DType.int`

The data type of the Item elements.

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
def __init__() -> Self
```

<span class="badge badge-static">static</span>

Initializes an empty Item.

**Returns:**

- `Self`

###### Overload 2

```mojo
def __init__(buf: IndexBuffer) -> Self
```

<span class="badge badge-static">static</span>

Initializes the Item from an IndexBuffer.

**Args:**

- `buf` (`IndexBuffer`) `[imm]`: The IndexBuffer to initialize from.

**Returns:**

- `Self`

###### Overload 3

```mojo
def __init__[T: Indexer](*args: T) -> Self
```

<span class="badge badge-static">static</span>

Construct the Item with variable arguments.

**Parameters:**

- `T` (`Indexer`): Type of values. It can be converted to `Int` with `Int()`.

**Args:**

- `*args` (`T`) `[imm]`: Initial values.

**Returns:**

- `Self`

###### Overload 4

```mojo
def __init__[T: IndexerCollectionElement](args: List[T]) -> Self
```

<span class="badge badge-static">static</span>

Construct the Item from a list.

**Parameters:**

- `T` (`IndexerCollectionElement`): Type of values. It can be converted to `Int` with `Int()`.

**Args:**

- `args` (`List[T]`) `[imm]`: Initial values.

**Returns:**

- `Self`

###### Overload 5

```mojo
def __init__(args: List[Int]) -> Self
```

<span class="badge badge-static">static</span>

Construct the Item from a list.

**Args:**

- `args` (`List[Int]`) `[imm]`: Initial values.

**Returns:**

- `Self`

###### Overload 6

```mojo
def __init__(args: VariadicList[Int]) -> Self
```

<span class="badge badge-static">static</span>

Construct the Item from a variadic list.

**Args:**

- `args` (`VariadicList[Int]`) `[imm]`: Initial values.

**Returns:**

- `Self`

###### Overload 7

```mojo
def __init__(*, ndim: Int) -> Self
```

<span class="badge badge-static">static</span>

Construct the Item with given length and initialize to zero.

**Args:**

- `ndim` (`Int`) `[imm]`: The length of the Item.

**Returns:**

- `Self`

###### Overload 8

```mojo
def __init__(*, copy: Self) -> Self
```

<span class="badge badge-static">static</span>

Copy construct the Item.

**Args:**

- `copy` (`Self`) `[imm]`: The Item to copy.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

###### Overload 1

```mojo
def __getitem__(self, idx: Int) -> Int
```

Gets the value at the specified index.

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: The index of the value to get.

**Returns:**

- `Int`

!!! failure "Raises"
    NumojoError: If index is out of range.

###### Overload 2

```mojo
def __getitem__(self, slice_index: Slice) -> Self
```

Return a sliced view of the item as a new Item.

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
def __setitem__(mut self, idx: Int, val: Int)
```

Set the value at the specified index.

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Int`) `[imm]`: The index of the value to set.
- `val` (`Int`) `[imm]`: The value to set.

!!! failure "Raises"
    NumojoError: If index is out of range.


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
def __eq__(self, other: Self) -> Bool
```

Checks if two items have identical dimensions and values.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The item to compare with.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
def __ne__(self, other: Self) -> Bool
```

Checks if two items have different dimensions or values.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The item to compare with.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__contains__`

```mojo
def __contains__(self, val: Int) -> Bool
```

Check if the Item contains the given value.

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

Load a SIMD vector from the Item at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: The starting index to load from.

**Returns:**

- `SIMD[DType.int, width]`

!!! failure "Raises"
    NumojoError: If the load exceeds the bounds of the Item.


</div>

<div class="fn-card" markdown="1">

##### `store`

```mojo
def store[width: Int = Int(1)](self, idx: Int, value: SIMD[DType.int, width])
```

Store a SIMD vector into the Item at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: The starting index to store to.
- `value` (`SIMD[DType.int, width]`) `[imm]`: The SIMD vector to store.

!!! failure "Raises"
    NumojoError: If the store exceeds the bounds of the Item.


</div>

<div class="fn-card" markdown="1">

##### `unsafe_load`

```mojo
def unsafe_load[width: Int = Int(1)](self, idx: Int) -> SIMD[DType.int, width]
```

Unsafely load a SIMD vector from the Item at the specified index.

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

Unsafely store a SIMD vector into the Item at the specified index.

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

##### `swapaxes`

```mojo
def swapaxes(self, axis1: Int, axis2: Int) -> Self
```

Returns a new item with the given axes swapped.

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
def join(self, *others: Self) -> Self
```

Join multiple items into a single item.

**Args:**

- `self` (`Self`) `[imm]`
- `*others` (`Self`) `[imm]`: Variable number of Item objects.

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

Returns a new item by flipping the items.

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

Returns a new item by moving the value of axis to the end.

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

##### `rank`

```mojo
def rank(self) -> Int
```

Returns the number of dimensions of the Item.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `sum`

```mojo
def sum(self) -> Int
```

Compute the sum of all elements in Item.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `product`

```mojo
def product(self) -> Int
```

Compute the product of all elements in the Item.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `__len__`

```mojo
def __len__(self) -> Int
```

Get the length of the Item.

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

Returns a string representation of the Item.

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

##### `__str__`

```mojo
def __str__(self) -> String
```

Returns a string representation of the Item.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `write_to`

```mojo
def write_to[W: Writer](self, mut writer: W)
```

Writes the Item representation to a writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

##### `tolist`

```mojo
def tolist(self) -> List[Int]
```

Convert the Item to a list of integers.

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
def __iter__(ref self) -> _ItemIter[origin_of(self)]
```

Iterate over elements of the Item.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_ItemIter[origin_of(self)]`


</div>

<div class="fn-card" markdown="1">

##### `__reversed__`

```mojo
def __reversed__(ref self) -> _ItemIter[origin_of(self), False]
```

Iterate over elements of the Item in reverse.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_ItemIter[origin_of(self), False]`


</div>
