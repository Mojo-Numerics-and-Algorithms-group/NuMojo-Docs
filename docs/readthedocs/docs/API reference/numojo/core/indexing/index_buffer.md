# `numojo.core.indexing.index_buffer`

IndexBuffer (numojo.core.indexing.index_buffer)

Shared integer buffer backend for shape/strides/item.

This type owns a contiguous heap buffer of Ints and provides
small helpers for pointer access and SIMD load/store.

## Structs

### `IndexBuffer`

```mojo
struct IndexBuffer
```

**Memory convention:** `register_passable`  
**Implements:** `AnyType`, `Copyable`, `Equatable`, `ImplicitlyCopyable`, `ImplicitlyDestructible`, `Movable`, `RegisterPassable`, `Sized`, `Stringable`, `Writable`

Shared integer buffer backend for shape/strides/item.

#### Fields

- **`ptr`** (`UnsafePointer[Scalar[DType.int], MutExternalOrigin]`): Pointer to the buffer.
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
__init__(*, size: Int) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer of given size.

**Args:**

- `size` (`Int`): Number of elements in the buffer.

**Returns:**

- `Self`

###### Overload 2

```mojo
__init__(ptr: UnsafePointer[Scalar[DType.int], MutExternalOrigin], size: Int) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with an existing pointer and size.

**Args:**

- `ptr` (`UnsafePointer`): UnsafePointer to the buffer.
- `size` (`Int`): Number of elements in the buffer.

**Returns:**

- `Self`

###### Overload 3

```mojo
__init__() -> Self
```

<span class="badge badge-static">static</span>

Initialize an empty IndexBuffer.

**Returns:**

- `Self`

###### Overload 4

```mojo
__init__(*values: Int) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with given Int values.

**Args:**

- `*values` (`Int`): Variadic list of integer values.

**Returns:**

- `Self`

###### Overload 5

```mojo
__init__(*values: Scalar[DType.int]) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with given values.

**Args:**

- `*values` (`Scalar`): Variadic list of integer values.

**Returns:**

- `Self`

###### Overload 6

```mojo
__init__(values: List[Scalar[DType.int]]) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with a list of values.

**Args:**

- `values` (`List`): List of integer values.

**Returns:**

- `Self`

###### Overload 7

```mojo
__init__(values: List[Int]) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with a list of Int values.

**Args:**

- `values` (`List`): List of integer values.

**Returns:**

- `Self`

###### Overload 8

```mojo
__init__(values: VariadicList[Scalar[DType.int]]) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with a range of values.

**Args:**

- `values` (`VariadicList`): Range of integer values.

**Returns:**

- `Self`

###### Overload 9

```mojo
__init__(values: VariadicList[Int]) -> Self
```

<span class="badge badge-static">static</span>

Initialize an IndexBuffer with a range of values.

**Args:**

- `values` (`VariadicList`): Range of integer values.

**Returns:**

- `Self`

###### Overload 10

```mojo
__init__(*, copy: Self) -> Self
```

<span class="badge badge-static">static</span>

Copy-initialize an IndexBuffer from ancopy IndexBuffer.

**Args:**

- `copy` (`Self`): The copy IndexBuffer to copy from.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__del__`

```mojo
__del__(deinit self)
```

Deinitialize the IndexBuffer and free resources.

**Args:**

- `self` (`Self`) `[deinit]`


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

###### Overload 1

```mojo
__getitem__(self, idx: Int) -> Int
```

Get the element at the given index.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): Index of the element.

**Returns:**

- `Int`

!!! failure "Raises"

###### Overload 2

```mojo
__getitem__(self, idx: Scalar[DType.int]) -> Scalar[DType.int]
```

Get the element at the given index.

**Args:**

- `self` (`Self`)
- `idx` (`Scalar`): Index of the element.

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 3

```mojo
__getitem__(self, slice: Slice) -> Self
```

Get a sub-buffer using a slice.

**Args:**

- `self` (`Self`)
- `slice` (`Slice`): Slice object defining the sub-buffer.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__setitem__`

###### Overload 1

```mojo
__setitem__(mut self, idx: Int, value: Int)
```

Set the element at the given index.

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Int`): Index of the element.
- `value` (`Int`): Value to set.

!!! failure "Raises"

###### Overload 2

```mojo
__setitem__(mut self, idx: Scalar[DType.int], value: Scalar[DType.int])
```

Set the element at the given index.

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Scalar`): Index of the element.
- `value` (`Scalar`): Value to set.

!!! failure "Raises"

###### Overload 3

```mojo
__setitem__(mut self, slice: Slice, value: Self)
```

Set a sub-buffer using a slice.

**Args:**

- `self` (`Self`) `[mut]`
- `slice` (`Slice`): Slice object defining the sub-buffer.
- `value` (`Self`): Buffer to set.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
__eq__(self, other: Self) -> Bool
```

Check if two IndexBuffers are equal.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The other IndexBuffer to compare with.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
__ne__(self, other: Self) -> Bool
```

Check if two IndexBuffers are not equal.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The other IndexBuffer to compare with.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__contains__`

###### Overload 1

```mojo
__contains__(self, value: Scalar[DType.int]) -> Bool
```

Check if the IndexBuffer contains the given value.

**Args:**

- `self` (`Self`)
- `value` (`Scalar`): Value to check for.

**Returns:**

- `Bool`

###### Overload 2

```mojo
__contains__(self, value: Int) -> Bool
```

Check if the IndexBuffer contains the given value.

**Args:**

- `self` (`Self`)
- `value` (`Int`): Value to check for.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `get_ptr`

```mojo
get_ptr(ref self) -> ref[self.ptr] UnsafePointer[Scalar[DType.int], MutExternalOrigin]
```

Get the underlying pointer of the buffer.

Notes:
The returned pointer is a reference to the internal pointer.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `ref`


</div>

<div class="fn-card" markdown="1">

##### `offset`

```mojo
offset(ref self, offset: Int) -> UnsafePointer[Scalar[DType.int], MutExternalOrigin]
```

Get a pointer offset by the given amount.

**Args:**

- `self` (`Self`) `[ref]`
- `offset` (`Int`): Offset amount.

**Returns:**

- `UnsafePointer`


</div>

<div class="fn-card" markdown="1">

##### `unsafe_load`

###### Overload 1

```mojo
unsafe_load[width: Int = 1](self, idx: Int) -> SIMD[DType.int, width]
```

Unsafely load a SIMD vector from the buffer at the given index.

**Parameters:**

- `width` (`Int`): Width of the SIMD vector.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): Index to load from.

**Returns:**

- `SIMD`

###### Overload 2

```mojo
unsafe_load[width: Int = 1](self, idx: Scalar[DType.int]) -> SIMD[DType.int, width]
```

Unsafely load a SIMD vector from the buffer at the given index.

**Parameters:**

- `width` (`Int`): Width of the SIMD vector.

**Args:**

- `self` (`Self`)
- `idx` (`Scalar`): Index to load from.

**Returns:**

- `SIMD`


</div>

<div class="fn-card" markdown="1">

##### `unsafe_store`

###### Overload 1

```mojo
unsafe_store[width: Int = 1](self, idx: Int, value: SIMD[DType.int, width])
```

Unsafely store a SIMD vector to the buffer at the given index.

**Parameters:**

- `width` (`Int`): Width of the SIMD vector.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): Index to store to.
- `value` (`SIMD`): SIMD vector to store.

###### Overload 2

```mojo
unsafe_store[width: Int = 1](self, idx: Scalar[DType.int], value: SIMD[DType.int, width])
```

Unsafely store a SIMD vector to the buffer at the given index.

**Parameters:**

- `width` (`Int`): Width of the SIMD vector.

**Args:**

- `self` (`Self`)
- `idx` (`Scalar`): Index to store to.
- `value` (`SIMD`): SIMD vector to store.


</div>

<div class="fn-card" markdown="1">

##### `extend`

###### Overload 1

```mojo
extend(self, *values: Int) -> Self
```

Extend the buffer by appending additional integer values.

**Args:**

- `self` (`Self`)
- `*values` (`Int`): Variadic list of sizes of extended dimensions.

**Returns:**

- `Self`

###### Overload 2

```mojo
extend(self, values: List[Int]) -> Self
```

Extend the buffer by appending additional integer values from a List.

**Args:**

- `self` (`Self`)
- `values` (`List`): List of sizes of extended dimensions.

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

Returns a new IndexBuffer by reversing the items.

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

Returns a new IndexBuffer by moving the value at axis to the end.

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis (index) to move. It should be in [-ndim, ndim).

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
- `axis` (`Int`): The axis (index) to drop. It should be in [0, ndim).

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `insert`

```mojo
insert(self, axis: Int, value: Int) -> Self
```

Inserts a value at the given axis (index).

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis (index) to insert at. It should be in [0, ndim].
- `value` (`Int`): The value to insert.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `join`

###### Overload 1

```mojo
join(self, *others: Self) -> Self
```

Join multiple IndexBuffers into a single IndexBuffer.

**Args:**

- `self` (`Self`)
- `*others` (`Self`): Variable number of IndexBuffer objects.

**Returns:**

- `Self`

###### Overload 2

```mojo
join(self, others: List[IndexBuffer]) -> Self
```

Join multiple IndexBuffers into a single IndexBuffer from a List.

**Args:**

- `self` (`Self`)
- `others` (`List`): List of IndexBuffer objects.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `sort`

```mojo
sort(mut self, order: Bool)
```

Sort the IndexBuffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `order` (`Bool`): If True, sort in ascending order; if False, sort in descending order.


</div>

<div class="fn-card" markdown="1">

##### `sorted`

```mojo
sorted(self, order: Bool) -> Self
```

Returns a new IndexBuffer that is sorted.

**Args:**

- `self` (`Self`)
- `order` (`Bool`): If True, sort in ascending order; if False, sort in descending order.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `arange`

```mojo
arange(start: Int, end: Int, step: Int = 1) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer with a range of values.

**Args:**

- `start` (`Int`): Start of the range.
- `end` (`Int`): End of the range.
- `step` (`Int`): Step size of the range.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `fill`

```mojo
fill(size: Int, value: Int) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer filled with the given value.

**Args:**

- `size` (`Int`): Number of elements in the buffer.
- `value` (`Int`): Value to fill the buffer with.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `zeros`

```mojo
zeros(size: Int) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer filled with zeros.

**Args:**

- `size` (`Int`): Number of elements in the buffer.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `ones`

```mojo
ones(size: Int) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer filled with ones.

**Args:**

- `size` (`Int`): Number of elements in the buffer.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `linspace`

```mojo
linspace(start: Int, end: Int, num: Int) -> Self
```

<span class="badge badge-static">static</span>

Create a IndexBuffer with linearly spaced values.

**Args:**

- `start` (`Int`): Start of the range.
- `end` (`Int`): End of the range.
- `num` (`Int`): Number of elements in the buffer.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `invert_permutation`

```mojo
invert_permutation(perm) -> Self
```

<span class="badge badge-static">static</span>

Invert a permutation.

**Args:**

- `perm` (`Self`): IndexBuffer representing a permutation.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `rank`

```mojo
rank(self) -> Int
```

Get the number of elements in the IndexBuffer.

**Args:**

- `self` (`Self`)

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `is_empty`

```mojo
is_empty(self) -> Bool
```

Check if the IndexBuffer is empty.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `sum`

```mojo
sum(self) -> Scalar[DType.int]
```

Compute the sum of all elements in the IndexBuffer.

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

Get the number of elements in the IndexBuffer.

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

Get the official string representation of the IndexBuffer.

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

Get the string representation of the IndexBuffer.

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

Write the IndexBuffer to a writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

##### `init_value`

```mojo
init_value(mut self, idx: Int, value: Scalar[DType.int])
```

Initialize the element at the given index. No bounds checking.

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Int`): Index of the element.
- `value` (`Scalar`): Value to set.


</div>

<div class="fn-card" markdown="1">

##### `tolist`

```mojo
tolist(self) -> List[Scalar[DType.int]]
```

Convert the buffer to a list.

**Args:**

- `self` (`Self`)

**Returns:**

- `List`


</div>

<div class="fn-card" markdown="1">

##### `__iter__`

```mojo
__iter__(ref self) -> _IndexBufferIter[DType.int, origin_of(self)]
```

Get a forward iterator for the IndexBuffer.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_IndexBufferIter`


</div>

<div class="fn-card" markdown="1">

##### `__reversed__`

```mojo
__reversed__(ref self) -> _IndexBufferIter[DType.int, origin_of(self), False]
```

Get a backward iterator for the IndexBuffer.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_IndexBufferIter`


</div>
