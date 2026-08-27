# `numojo.core.indexing.index_buffer`

Shared integer buffer backend for shape/strides/item.

Owns a contiguous heap buffer of Ints and provides small helpers for pointer
access and SIMD load/store.

Exports
-------
- `IndexBuffer`: Index storage.

## Structs

### `IndexBuffer`

```mojo
struct IndexBuffer
```

**Memory convention:** `register_passable`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Equatable`, `ImplicitlyCopyable`, `Movable`, `RegisterPassable`, `Sized`, `Writable`

Shared integer buffer backend for shape/strides/item.

#### Fields

- **`ptr`** (`Pointer[Int, MutUntrackedOrigin]`): Pointer to the buffer.
- **`ndim`** (`Int`): Number of elements in the buffer.

#### Aliases

##### `element_type`

```mojo
comptime element_type
```

**Value:** `DType.int`

Element type of the buffer.

##### `simd_width`

```mojo
comptime simd_width
```

**Value:** `simd_width_of[DType.int]()`

SIMD width for the element type.

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
def __init__(*, size: Int) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer of given size.

**Args:**

- `size` (`Int`) `[imm]`: Number of elements in the buffer.

**Returns:**

- `Self`

###### Overload 2

```mojo
def __init__(ptr: Pointer[Int, MutUntrackedOrigin], size: Int) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with an existing pointer and size.

**Args:**

- `ptr` (`Pointer[Int, MutUntrackedOrigin]`) `[imm]`: UnsafePointer to the buffer.
- `size` (`Int`) `[imm]`: Number of elements in the buffer.

**Returns:**

- `Self`

###### Overload 3

```mojo
def __init__() -> Self
```

<span class="badge badge-static">static</span>

Initialize an empty IndexBuffer.

**Returns:**

- `Self`

###### Overload 4

```mojo
def __init__(*values: Int) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with given values.

**Args:**

- `*values` (`Int`) `[imm]`: Variadic list of integer values.

**Returns:**

- `Self`

###### Overload 5

```mojo
def __init__(values: List[Int]) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with a list of values.

**Args:**

- `values` (`List[Int]`) `[imm]`: List of integer values.

**Returns:**

- `Self`

###### Overload 6

```mojo
def __init__(values: VariadicList[Int]) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with a range of values.

**Args:**

- `values` (`VariadicList[Int]`) `[imm]`: Range of integer values.

**Returns:**

- `Self`

###### Overload 7

```mojo
def __init__(*, copy: Self) -> Self
```

<span class="badge badge-static">static</span>

Copy-initialize an IndexBuffer from ancopy IndexBuffer.

**Args:**

- `copy` (`Self`) `[imm]`: The copy IndexBuffer to copy from.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__deinit__`

```mojo
def __deinit__(deinit self)
```

Deinitialize the IndexBuffer and free resources.

**Args:**

- `self` (`Self`) `[deinit]`


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

###### Overload 1

```mojo
def __getitem__(self, idx: Int) -> Int
```

Get the element at the given index.

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: Index of the element.

**Returns:**

- `Int`

!!! failure "Raises"

###### Overload 2

```mojo
def __getitem__(self, slice: Slice) -> Self
```

Get a sub-buffer using a slice.

**Args:**

- `self` (`Self`) `[imm]`
- `slice` (`Slice`) `[imm]`: Slice object defining the sub-buffer.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__setitem__`

###### Overload 1

```mojo
def __setitem__(mut self, idx: Int, value: Int)
```

Set the element at the given index.

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Int`) `[imm]`: Index of the element.
- `value` (`Int`) `[imm]`: Value to set.

!!! failure "Raises"

###### Overload 2

```mojo
def __setitem__(mut self, slice: Slice, value: Self)
```

Set a sub-buffer using a slice.

**Args:**

- `self` (`Self`) `[mut]`
- `slice` (`Slice`) `[imm]`: Slice object defining the sub-buffer.
- `value` (`Self`) `[imm]`: Buffer to set.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
def __eq__(self, other: Self) -> Bool
```

Check if two IndexBuffers are equal.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The other IndexBuffer to compare with.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
def __ne__(self, other: Self) -> Bool
```

Check if two IndexBuffers are not equal.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The other IndexBuffer to compare with.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__contains__`

```mojo
def __contains__(self, value: Int) -> Bool
```

Check if the IndexBuffer contains the given value.

**Args:**

- `self` (`Self`) `[imm]`
- `value` (`Int`) `[imm]`: Value to check for.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `get_ptr`

```mojo
def get_ptr(ref self) -> ref[self.ptr] Pointer[Int, MutUntrackedOrigin]
```

Get the underlying pointer of the buffer.

Notes:
The returned pointer is a reference to the internal pointer.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `ref[self.ptr] Pointer[Int, MutUntrackedOrigin]`


</div>

<div class="fn-card" markdown="1">

##### `offset`

```mojo
def offset(ref self, offset: Int) -> Pointer[Int, MutUntrackedOrigin]
```

Get a pointer offset by the given amount.

**Args:**

- `self` (`Self`) `[ref]`
- `offset` (`Int`) `[imm]`: Offset amount.

**Returns:**

- `Pointer[Int, MutUntrackedOrigin]`


</div>

<div class="fn-card" markdown="1">

##### `unsafe_load`

```mojo
def unsafe_load[width: Int = Int(1)](self, idx: Int) -> SIMD[DType.int, width]
```

Unsafely load a SIMD vector from the buffer at the given index.

**Parameters:**

- `width` (`Int`): Width of the SIMD vector.

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: Index to load from.

**Returns:**

- `SIMD[DType.int, width]`


</div>

<div class="fn-card" markdown="1">

##### `unsafe_store`

```mojo
def unsafe_store[width: Int = Int(1)](self, idx: Int, value: SIMD[DType.int, width])
```

Unsafely store a SIMD vector to the buffer at the given index.

**Parameters:**

- `width` (`Int`): Width of the SIMD vector.

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: Index to store to.
- `value` (`SIMD[DType.int, width]`) `[imm]`: SIMD vector to store.


</div>

<div class="fn-card" markdown="1">

##### `extend`

###### Overload 1

```mojo
def extend(self, *values: Int) -> Self
```

Extend the buffer by appending additional integer values.

**Args:**

- `self` (`Self`) `[imm]`
- `*values` (`Int`) `[imm]`: Variadic list of sizes of extended dimensions.

**Returns:**

- `Self`

###### Overload 2

```mojo
def extend(self, values: List[Int]) -> Self
```

Extend the buffer by appending additional integer values from a List.

**Args:**

- `self` (`Self`) `[imm]`
- `values` (`List[Int]`) `[imm]`: List of sizes of extended dimensions.

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

Returns a new IndexBuffer by reversing the items.

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

Returns a new IndexBuffer by moving the value at axis to the end.

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis (index) to move. It should be in [-ndim, ndim).

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `pop`

```mojo
def pop(self, axis: Int) -> Self
```

Drops the item at the given axis (index).

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis (index) to drop. It should be in [0, ndim).

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `insert`

```mojo
def insert(self, axis: Int, value: Int) -> Self
```

Inserts a value at the given axis (index).

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis (index) to insert at. It should be in [0, ndim].
- `value` (`Int`) `[imm]`: The value to insert.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `join`

###### Overload 1

```mojo
def join(self, *others: Self) -> Self
```

Join multiple IndexBuffers into a single IndexBuffer.

**Args:**

- `self` (`Self`) `[imm]`
- `*others` (`Self`) `[imm]`: Variable number of IndexBuffer objects.

**Returns:**

- `Self`

###### Overload 2

```mojo
def join(self, others: List[Self]) -> Self
```

Join multiple IndexBuffers into a single IndexBuffer from a List.

**Args:**

- `self` (`Self`) `[imm]`
- `others` (`List[Self]`) `[imm]`: List of IndexBuffer objects.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `sort`

```mojo
def sort(mut self, order: Bool)
```

Sort the IndexBuffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `order` (`Bool`) `[imm]`: If True, sort in ascending order; if False, sort in descending order.


</div>

<div class="fn-card" markdown="1">

##### `sorted`

```mojo
def sorted(self, order: Bool) -> Self
```

Returns a new IndexBuffer that is sorted.

**Args:**

- `self` (`Self`) `[imm]`
- `order` (`Bool`) `[imm]`: If True, sort in ascending order; if False, sort in descending order.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `arange`

```mojo
def arange(start: Int, end: Int, step: Int = Int(1)) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer with a range of values.

**Args:**

- `start` (`Int`) `[imm]`: Start of the range.
- `end` (`Int`) `[imm]`: End of the range.
- `step` (`Int`) `[imm]`: Step size of the range.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `fill`

```mojo
def fill(size: Int, value: Int) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer filled with the given value.

**Args:**

- `size` (`Int`) `[imm]`: Number of elements in the buffer.
- `value` (`Int`) `[imm]`: Value to fill the buffer with.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `zeros`

```mojo
def zeros(size: Int) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer filled with zeros.

**Args:**

- `size` (`Int`) `[imm]`: Number of elements in the buffer.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `ones`

```mojo
def ones(size: Int) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer filled with ones.

**Args:**

- `size` (`Int`) `[imm]`: Number of elements in the buffer.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `linspace`

```mojo
def linspace(start: Int, end: Int, num: Int) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer with linearly spaced values.

**Args:**

- `start` (`Int`) `[imm]`: Start of the range.
- `end` (`Int`) `[imm]`: End of the range.
- `num` (`Int`) `[imm]`: Number of elements in the buffer.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `invert_permutation`

```mojo
def invert_permutation(perm) -> Self
```

<span class="badge badge-static">static</span>

Invert a permutation.

**Args:**

- `perm` (`Self`) `[imm]`: IndexBuffer representing a permutation.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `rank`

```mojo
def rank(self) -> Int
```

Get the number of elements in the IndexBuffer.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `is_empty`

```mojo
def is_empty(self) -> Bool
```

Check if the IndexBuffer is empty.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `sum`

```mojo
def sum(self) -> Int
```

Compute the sum of all elements in the IndexBuffer.

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

Compute the product of all elements in the IndexBuffer.

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

Get the number of elements in the IndexBuffer.

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

Get the official string representation of the IndexBuffer.

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

Get the string representation of the IndexBuffer.

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

Write the IndexBuffer to a writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

##### `init_value`

```mojo
def init_value(mut self, idx: Int, value: Int)
```

Initialize the element at the given index. No bounds checking.

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Int`) `[imm]`: Index of the element.
- `value` (`Int`) `[imm]`: Value to set.


</div>

<div class="fn-card" markdown="1">

##### `tolist`

```mojo
def tolist(self) -> List[Int]
```

Convert the buffer to a list.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `List[Int]`


</div>

<div class="fn-card" markdown="1">

##### `__iter__`

```mojo
def __iter__(ref self) -> _IndexBufferIter[DType.int, origin_of(self)]
```

Get a forward iterator for the IndexBuffer.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_IndexBufferIter[DType.int, origin_of(self)]`


</div>

<div class="fn-card" markdown="1">

##### `__reversed__`

```mojo
def __reversed__(ref self) -> _IndexBufferIter[DType.int, origin_of(self), False]
```

Get a backward iterator for the IndexBuffer.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_IndexBufferIter[DType.int, origin_of(self), False]`


</div>
