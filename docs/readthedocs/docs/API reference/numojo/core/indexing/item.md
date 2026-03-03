# `numojo.core.indexing.item`

Item (numojo.core.indexing.item)

Implements Item type.

`Item` is a series of `Int` on the heap used to index into N-dimensional arrays.
It is used for multi-dimensional indexing, such as `arr[Item(1, 2, 3)]` to access `arr[1, 2, 3]`.

## Structs

### `Item`

```mojo
struct Item
```

**Memory convention:** `register_passable`  
**Implements:** `AnyType`, `Copyable`, `Equatable`, `ImplicitlyCopyable`, `ImplicitlyDestructible`, `Movable`, `RegisterPassable`, `Representable`, `Sized`, `Stringable`, `Writable`

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

Initializes an empty Item.

**Returns:**

- `Self`

###### Overload 2

```mojo
__init__(buf: IndexBuffer) -> Self
```

<span class="badge badge-static">static</span>

Initializes the Item from an IndexBuffer.

**Args:**

- `buf` (`IndexBuffer`): The IndexBuffer to initialize from.

**Returns:**

- `Self`

###### Overload 3

```mojo
__init__[T: Indexer](*args: T) -> Self
```

<span class="badge badge-static">static</span>

Construct the Item with variable arguments.

**Parameters:**

- `T` (`Indexer`): Type of values. It can be converted to `Int` with `Int()`.

**Args:**

- `*args` (`T`): Initial values.

**Returns:**

- `Self`

###### Overload 4

```mojo
__init__[T: IndexerCollectionElement](args: List[T]) -> Self
```

<span class="badge badge-static">static</span>

Construct the Item from a list.

**Parameters:**

- `T` (`IndexerCollectionElement`): Type of values. It can be converted to `Int` with `Int()`.

**Args:**

- `args` (`List`): Initial values.

**Returns:**

- `Self`

###### Overload 5

```mojo
__init__(args: List[Int]) -> Self
```

<span class="badge badge-static">static</span>

Construct the Item from a list.

**Args:**

- `args` (`List`): Initial values.

**Returns:**

- `Self`

###### Overload 6

```mojo
__init__(args: VariadicList[Int]) -> Self
```

<span class="badge badge-static">static</span>

Construct the Item from a variadic list.

**Args:**

- `args` (`VariadicList`): Initial values.

**Returns:**

- `Self`

###### Overload 7

```mojo
__init__(*, ndim: Int) -> Self
```

<span class="badge badge-static">static</span>

Construct the Item with given length and initialize to zero.

**Args:**

- `ndim` (`Int`): The length of the Item.

**Returns:**

- `Self`

###### Overload 8

```mojo
__init__(*, copy: Self) -> Self
```

<span class="badge badge-static">static</span>

Copy construct the Item.

**Args:**

- `copy` (`Self`): The Item to copy.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

###### Overload 1

```mojo
__getitem__(self, idx: Int) -> Int
```

Gets the value at the specified index.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The index of the value to get.

**Returns:**

- `Int`

!!! failure "Raises"
    Error: If index is out of range.

###### Overload 2

```mojo
__getitem__(self, slice_index: Slice) -> Self
```

Return a sliced view of the item as a new Item.

**Args:**

- `self` (`Self`)
- `slice_index` (`Slice`): Slice object defining the sub-buffer.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__setitem__`

```mojo
__setitem__(mut self, idx: Int, val: Int)
```

Set the value at the specified index.

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Int`): The index of the value to set.
- `val` (`Int`): The value to set.

!!! failure "Raises"
    Error: If index is out of range.


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
__eq__(self, other: Self) -> Bool
```

Checks if two items have identical dimensions and values.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The item to compare with.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
__ne__(self, other: Self) -> Bool
```

Checks if two items have different dimensions or values.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The item to compare with.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__contains__`

###### Overload 1

```mojo
__contains__(self, val: Scalar[DType.int]) -> Bool
```

Check if the Item contains the given value.

**Args:**

- `self` (`Self`)
- `val` (`Scalar`): Value to check for.

**Returns:**

- `Bool`

###### Overload 2

```mojo
__contains__(self, val: Int) -> Bool
```

Checks if the given value is present in the item.

**Args:**

- `self` (`Self`)
- `val` (`Int`): The value to search for.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `load`

```mojo
load[width: Int = 1](self, idx: Int) -> SIMD[DType.int, width]
```

Load a SIMD vector from the Item at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The starting index to load from.

**Returns:**

- `SIMD`

!!! failure "Raises"
    Error: If the load exceeds the bounds of the Item.


</div>

<div class="fn-card" markdown="1">

##### `store`

```mojo
store[width: Int = 1](self, idx: Int, value: SIMD[DType.int, width])
```

Store a SIMD vector into the Item at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The starting index to store to.
- `value` (`SIMD`): The SIMD vector to store.

!!! failure "Raises"
    Error: If the store exceeds the bounds of the Item.


</div>

<div class="fn-card" markdown="1">

##### `unsafe_load`

```mojo
unsafe_load[width: Int = 1](self, idx: Int) -> SIMD[DType.int, width]
```

Unsafely load a SIMD vector from the Item at the specified index.

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

Unsafely store a SIMD vector into the Item at the specified index.

**Parameters:**

- `width` (`Int`): The width of the SIMD vector.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The starting index to store to.
- `value` (`SIMD`): The SIMD vector to store.


</div>

<div class="fn-card" markdown="1">

##### `swapaxes`

```mojo
swapaxes(self, axis1: Int, axis2: Int) -> Self
```

Returns a new item with the given axes swapped.

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
join(self, *others: Self) -> Self
```

Join multiple items into a single item.

**Args:**

- `self` (`Self`)
- `*others` (`Self`): Variable number of Item objects.

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

Returns a new item by flipping the items.

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

Returns a new item by moving the value of axis to the end.

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

##### `rank`

```mojo
rank(self) -> Int
```

Returns the number of dimensions of the Item.

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

Compute the sum of all elements in Item.

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

Compute the product of all elements in the Item.

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

Get the length of the Item.

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

Returns a string representation of the Item.

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

Returns a string representation of the Item.

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

Writes the Item representation to a writer.

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

Convert the Item to a list of integers.

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
__iter__(ref self) -> _ItemIter[origin_of(self)]
```

Iterate over elements of the Item.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_ItemIter`


</div>

<div class="fn-card" markdown="1">

##### `__reversed__`

```mojo
__reversed__(ref self) -> _ItemIter[origin_of(self), False]
```

Iterate over elements of the Item in reverse.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_ItemIter`


</div>
