# `numojo.core.indexing.index_buffer`

Shared integer buffer backend for shape/strides/item.

Owns a contiguous heap buffer of Ints and provides small helpers for pointer
access and SIMD load/store.

Exports
-------
- `IndexBuffer`: Index storage.

## Structs

### `IndexBuffer`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct IndexBuffer
```

**Memory convention:** `register_passable`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Equatable`, `ImplicitlyCopyable`, `Movable`, `RegisterPassable`, `Sized`, `Writable`

Shared integer buffer backend for shape/strides/item.

</div>

#### Fields

- **`ptr`** (`Pointer[Int, MutUntrackedOrigin]`): Pointer to the buffer.
- **`ndim`** (`Int`): Number of elements in the buffer.

#### Aliases

#### `element_type`

```mojo
comptime element_type
```

**Value:** `DType.int`

Element type of the buffer.

#### `simd_width`

```mojo
comptime simd_width
```

**Value:** `simd_width_of[DType.int]()`

SIMD width for the element type.

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

<div class="overload-divider">Overload 1</div>

```mojo
def __init__(*, size: Int) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer of given size.

<div class="prose-label">Args</div>

- `size` (`Int`) `[imm]`: Number of elements in the buffer.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __init__(ptr: Pointer[Int, MutUntrackedOrigin], size: Int) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with an existing pointer and size.

<div class="prose-label">Args</div>

- `ptr` (`Pointer[Int, MutUntrackedOrigin]`) `[imm]`: UnsafePointer to the buffer.
- `size` (`Int`) `[imm]`: Number of elements in the buffer.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 3</div>

```mojo
def __init__() -> Self
```

<span class="badge badge-static">static</span>

Initialize an empty IndexBuffer.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 4</div>

```mojo
def __init__(*values: Int) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with given values.

<div class="prose-label">Args</div>

- `*values` (`Int`) `[imm]`: Variadic list of integer values.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 5</div>

```mojo
def __init__(values: List[Int]) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with a list of values.

<div class="prose-label">Args</div>

- `values` (`List[Int]`) `[imm]`: List of integer values.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 6</div>

```mojo
def __init__(values: VariadicList[Int]) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with a range of values.

<div class="prose-label">Args</div>

- `values` (`VariadicList[Int]`) `[imm]`: Range of integer values.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 7</div>

```mojo
def __init__(*, copy: Self) -> Self
```

<span class="badge badge-static">static</span>

Copy-initialize an IndexBuffer from ancopy IndexBuffer.

<div class="prose-label">Args</div>

- `copy` (`Self`) `[imm]`: The copy IndexBuffer to copy from.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__deinit__`

```mojo
def __deinit__(deinit self)
```

Deinitialize the IndexBuffer and free resources.

<div class="prose-label">Args</div>

- `self` (`Self`) `[deinit]`


</div>

<div class="fn-card" markdown="1">

#### `__getitem__`

<div class="overload-divider">Overload 1</div>

```mojo
def __getitem__(self, idx: Int) -> Int
```

Get the element at the given index.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: Index of the element.

<div class="prose-label">Returns</div>

- `Int`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def __getitem__(self, slice: Slice) -> Self
```

Get a sub-buffer using a slice.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `slice` (`Slice`) `[imm]`: Slice object defining the sub-buffer.

<div class="prose-label">Returns</div>

- `Self`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `__setitem__`

<div class="overload-divider">Overload 1</div>

```mojo
def __setitem__(mut self, idx: Int, value: Int)
```

Set the element at the given index.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `idx` (`Int`) `[imm]`: Index of the element.
- `value` (`Int`) `[imm]`: Value to set.

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def __setitem__(mut self, slice: Slice, value: Self)
```

Set a sub-buffer using a slice.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `slice` (`Slice`) `[imm]`: Slice object defining the sub-buffer.
- `value` (`Self`) `[imm]`: Buffer to set.

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `__eq__`

```mojo
def __eq__(self, other: Self) -> Bool
```

Check if two IndexBuffers are equal.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The other IndexBuffer to compare with.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__ne__`

```mojo
def __ne__(self, other: Self) -> Bool
```

Check if two IndexBuffers are not equal.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The other IndexBuffer to compare with.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__contains__`

```mojo
def __contains__(self, value: Int) -> Bool
```

Check if the IndexBuffer contains the given value.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `value` (`Int`) `[imm]`: Value to check for.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `get_ptr`

```mojo
def get_ptr(ref self) -> ref[self.ptr] Pointer[Int, MutUntrackedOrigin]
```

Get the underlying pointer of the buffer.

<div class="prose-label">Notes</div>
The returned pointer is a reference to the internal pointer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`

<div class="prose-label">Returns</div>

- `ref[self.ptr] Pointer[Int, MutUntrackedOrigin]`


</div>

<div class="fn-card" markdown="1">

#### `offset`

```mojo
def offset(ref self, offset: Int) -> Pointer[Int, MutUntrackedOrigin]
```

Get a pointer offset by the given amount.

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`
- `offset` (`Int`) `[imm]`: Offset amount.

<div class="prose-label">Returns</div>

- `Pointer[Int, MutUntrackedOrigin]`


</div>

<div class="fn-card" markdown="1">

#### `unsafe_load`

```mojo
def unsafe_load[width: Int = Int(1)](self, idx: Int) -> SIMD[DType.int, width]
```

Unsafely load a SIMD vector from the buffer at the given index.

<div class="prose-label">Parameters</div>

- `width` (`Int`): Width of the SIMD vector.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: Index to load from.

<div class="prose-label">Returns</div>

- `SIMD[DType.int, width]`


</div>

<div class="fn-card" markdown="1">

#### `unsafe_store`

```mojo
def unsafe_store[width: Int = Int(1)](self, idx: Int, value: SIMD[DType.int, width])
```

Unsafely store a SIMD vector to the buffer at the given index.

<div class="prose-label">Parameters</div>

- `width` (`Int`): Width of the SIMD vector.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: Index to store to.
- `value` (`SIMD[DType.int, width]`) `[imm]`: SIMD vector to store.


</div>

<div class="fn-card" markdown="1">

#### `extend`

<div class="overload-divider">Overload 1</div>

```mojo
def extend(self, *values: Int) -> Self
```

Extend the buffer by appending additional integer values.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `*values` (`Int`) `[imm]`: Variadic list of sizes of extended dimensions.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def extend(self, values: List[Int]) -> Self
```

Extend the buffer by appending additional integer values from a List.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `values` (`List[Int]`) `[imm]`: List of sizes of extended dimensions.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `flip`

```mojo
def flip(mut self)
```

Flip the items in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`


</div>

<div class="fn-card" markdown="1">

#### `flipped`

```mojo
def flipped(self) -> Self
```

Returns a new IndexBuffer by reversing the items.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `move_axis_to_end`

```mojo
def move_axis_to_end(self, axis: Int) -> Self
```

Returns a new IndexBuffer by moving the value at axis to the end.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis (index) to move. It should be in [-ndim, ndim).

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `pop`

```mojo
def pop(self, axis: Int) -> Self
```

Drops the item at the given axis (index).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis (index) to drop. It should be in [0, ndim).

<div class="prose-label">Returns</div>

- `Self`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `insert`

```mojo
def insert(self, axis: Int, value: Int) -> Self
```

Inserts a value at the given axis (index).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis (index) to insert at. It should be in [0, ndim].
- `value` (`Int`) `[imm]`: The value to insert.

<div class="prose-label">Returns</div>

- `Self`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `join`

<div class="overload-divider">Overload 1</div>

```mojo
def join(self, *others: Self) -> Self
```

Join multiple IndexBuffers into a single IndexBuffer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `*others` (`Self`) `[imm]`: Variable number of IndexBuffer objects.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def join(self, others: List[Self]) -> Self
```

Join multiple IndexBuffers into a single IndexBuffer from a List.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `others` (`List[Self]`) `[imm]`: List of IndexBuffer objects.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `sort`

```mojo
def sort(mut self, order: Bool)
```

Sort the IndexBuffer in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `order` (`Bool`) `[imm]`: If True, sort in ascending order; if False, sort in descending order.


</div>

<div class="fn-card" markdown="1">

#### `sorted`

```mojo
def sorted(self, order: Bool) -> Self
```

Returns a new IndexBuffer that is sorted.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `order` (`Bool`) `[imm]`: If True, sort in ascending order; if False, sort in descending order.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `arange`

```mojo
def arange(start: Int, end: Int, step: Int = Int(1)) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer with a range of values.

<div class="prose-label">Args</div>

- `start` (`Int`) `[imm]`: Start of the range.
- `end` (`Int`) `[imm]`: End of the range.
- `step` (`Int`) `[imm]`: Step size of the range.

<div class="prose-label">Returns</div>

- `Self`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `fill`

```mojo
def fill(size: Int, value: Int) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer filled with the given value.

<div class="prose-label">Args</div>

- `size` (`Int`) `[imm]`: Number of elements in the buffer.
- `value` (`Int`) `[imm]`: Value to fill the buffer with.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `zeros`

```mojo
def zeros(size: Int) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer filled with zeros.

<div class="prose-label">Args</div>

- `size` (`Int`) `[imm]`: Number of elements in the buffer.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `ones`

```mojo
def ones(size: Int) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer filled with ones.

<div class="prose-label">Args</div>

- `size` (`Int`) `[imm]`: Number of elements in the buffer.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `linspace`

```mojo
def linspace(start: Int, end: Int, num: Int) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer with linearly spaced values.

<div class="prose-label">Args</div>

- `start` (`Int`) `[imm]`: Start of the range.
- `end` (`Int`) `[imm]`: End of the range.
- `num` (`Int`) `[imm]`: Number of elements in the buffer.

<div class="prose-label">Returns</div>

- `Self`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `invert_permutation`

```mojo
def invert_permutation(perm) -> Self
```

<span class="badge badge-static">static</span>

Invert a permutation.

<div class="prose-label">Args</div>

- `perm` (`Self`) `[imm]`: IndexBuffer representing a permutation.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `rank`

```mojo
def rank(self) -> Int
```

Get the number of elements in the IndexBuffer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `is_empty`

```mojo
def is_empty(self) -> Bool
```

Check if the IndexBuffer is empty.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `sum`

```mojo
def sum(self) -> Int
```

Compute the sum of all elements in the IndexBuffer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `product`

```mojo
def product(self) -> Int
```

Compute the product of all elements in the IndexBuffer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `__len__`

```mojo
def __len__(self) -> Int
```

Get the number of elements in the IndexBuffer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `__repr__`

```mojo
def __repr__(self) -> String
```

Get the official string representation of the IndexBuffer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>

<div class="fn-card" markdown="1">

#### `__str__`

```mojo
def __str__(self) -> String
```

Get the string representation of the IndexBuffer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>

<div class="fn-card" markdown="1">

#### `write_to`

```mojo
def write_to[W: Writer](self, mut writer: W)
```

Write the IndexBuffer to a writer.

<div class="prose-label">Parameters</div>

- `W` (`Writer`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

#### `init_value`

```mojo
def init_value(mut self, idx: Int, value: Int)
```

Initialize the element at the given index. No bounds checking.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `idx` (`Int`) `[imm]`: Index of the element.
- `value` (`Int`) `[imm]`: Value to set.


</div>

<div class="fn-card" markdown="1">

#### `tolist`

```mojo
def tolist(self) -> List[Int]
```

Convert the buffer to a list.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `List[Int]`


</div>

<div class="fn-card" markdown="1">

#### `__iter__`

```mojo
def __iter__(ref self) -> _IndexBufferIter[DType.int, origin_of(self)]
```

Get a forward iterator for the IndexBuffer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`

<div class="prose-label">Returns</div>

- `_IndexBufferIter[DType.int, origin_of(self)]`


</div>

<div class="fn-card" markdown="1">

#### `__reversed__`

```mojo
def __reversed__(ref self) -> _IndexBufferIter[DType.int, origin_of(self), False]
```

Get a backward iterator for the IndexBuffer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`

<div class="prose-label">Returns</div>

- `_IndexBufferIter[DType.int, origin_of(self), False]`


</div>
