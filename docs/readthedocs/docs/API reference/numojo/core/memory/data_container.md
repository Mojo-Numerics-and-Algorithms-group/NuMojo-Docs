# `numojo.core.memory.data_container`

DataContainer (numojo.core.memory.data_container)

A reference-counted container for contiguous data buffers, used for NDArray and Matrix.

DataContainer manages memory ownership and reference counting for shared or external data.

## Structs

### `Ownership`

```mojo
struct Ownership
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `ImplicitlyCopyable`, `ImplicitlyDestructible`, `Movable`

Enum indicating whether a DataContainer owns its data or views external data.

- Managed: Container owns its data and uses reference counting.
- External: Container views externally managed data and does not deallocate or refcount.

#### Fields

- **`value`** (`__mlir_type.i1`): Ownership status as a boolean.

#### Aliases

##### `Managed`

```mojo
comptime Managed
```

**Value:** `Ownership(True)`

Container owns and manages its data.

##### `External`

```mojo
comptime External
```

**Value:** `Ownership(False)`

Container views externally managed data.

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `True`

##### `__move_ctor_is_trivial`

```mojo
comptime __move_ctor_is_trivial
```

**Value:** `True`

##### `__copy_ctor_is_trivial`

```mojo
comptime __copy_ctor_is_trivial
```

**Value:** `True`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
__init__(out self, value: __mlir_type.i1)
```

<span class="badge badge-static">static</span>

Initialize Ownership with the given status.

**Args:**

- `value` (`__mlir_type.i1`)
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
__eq__(self, other: Self) -> Bool
```

Return True if both Ownership instances have the same status.

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
__ne__(self, other: Self) -> Bool
```

Return True if Ownership instances have different statuses.

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__xor__`

```mojo
__xor__(self, other: Self) -> Bool
```

Return True if Ownership statuses differ.

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
__str__(self) -> String
```

Return "Managed" or "External" based on ownership status.

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

Write the ownership status as a string to the writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`


</div>
### `DataContainer`

```mojo
struct DataContainer[dtype: DType]
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `ImplicitlyDestructible`, `Movable`, `Sized`, `Stringable`, `Writable`

Reference-counted container for a contiguous buffer of elements.

DataContainer can either own its memory (managed) or provide a view into external data (external).
Managed containers use reference counting for shared ownership. External containers do not manage or free memory.

Copying a managed DataContainer with `.copy()` increments the reference count that still points to the same data.
Copying an external container creates another non-owning view.
Use `deep_copy()` to create an owned instance.

Fields:
    ptr: Pointer to the data array.
    _refcount: Pointer to the atomic reference count (null for external).
    ownership: Ownership status (Managed or External).
    size: Number of elements in the data array.

**Parameters:**

- `dtype` (`DType`)

#### Fields

- **`ptr`** (`UnsafePointer[Scalar[dtype], DataContainer[dtype].origin]`): Pointer to the data array.
- **`ownership`** (`Ownership`): Ownership status of the container.
- **`size`** (`Int`): Number of elements in the data array.

#### Aliases

##### `origin`

```mojo
comptime origin
```

**Value:** `MutExternalOrigin`

Memory origin for the allocation.

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `False`

##### `__move_ctor_is_trivial`

```mojo
comptime __move_ctor_is_trivial
```

**Value:** `False`

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
__init__(out self)
```

<span class="badge badge-static">static</span>

Create an empty, managed DataContainer.

**Args:**

- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 2

```mojo
__init__(out self, size: Int)
```

<span class="badge badge-static">static</span>

Create a managed DataContainer with a buffer of `size` elements.

**Args:**

- `size` (`Int`): Number of elements to allocate (must be non-negative).
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 3

```mojo
__init__(out self, ptr: UnsafePointer[Scalar[dtype], DataContainer[dtype].origin], size: Int, copy: Bool = False)
```

<span class="badge badge-static">static</span>

Create a DataContainer from an existing buffer.

If `copy` is True, the data is deep-copied into managed storage.
If `copy` is False, the container is external and does not manage or
free the memory.

**Args:**

- `ptr` (`UnsafePointer`): Pointer to an existing data buffer (must be non-null).
- `size` (`Int`): Number of elements in the buffer (must be non-negative).
- `copy` (`Bool`): If True, deep-copy into owned storage.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 4

```mojo
__init__(out self, *, ptr: UnsafePointer[Scalar[dtype], DataContainer[dtype].origin], size: Int, refcount: UnsafePointer[Atomic[DType.uint64], DataContainer[dtype].origin], ownership: Ownership)
```

<span class="badge badge-static">static</span>

Create a DataContainer that shares an existing buffer and refcount.

This constructor is used internally by `share()` to create a shared
handle without allocating a new refcount. No validation is performed;
the caller must ensure all arguments are valid.

**Args:**

- `ptr` (`UnsafePointer`): Pointer to the shared data buffer.
- `size` (`Int`): Number of elements in the buffer.
- `refcount` (`UnsafePointer`): Pointer to the shared atomic reference count.
- `ownership` (`Ownership`): Ownership mode (should be Managed for shared handles).
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 5

```mojo
__init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

Copy constructor.

Increments the reference count for managed containers.

**Args:**

- `copy` (`Self`): DataContainer to copy from.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 6

```mojo
__init__(out self, *, deinit take: Self)
```

<span class="badge badge-static">static</span>

Move constructor.

Transfers ownership without changing the reference count.

**Args:**

- `take` (`Self`) `[deinit]`: DataContainer to move from.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__del__`

```mojo
__del__(deinit self)
```

Destructor.

Decrements the reference count and frees memory if this is the last reference.

**Args:**

- `self` (`Self`) `[deinit]`


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

```mojo
__getitem__(self, idx: Int) -> Scalar[dtype]
```

Return the element at the specified index.

Notes:
No bounds checking is performed. Caller must ensure index is valid.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): Index of the element to retrieve.

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__setitem__`

```mojo
__setitem__(mut self, idx: Int, val: Scalar[dtype])
```

Set the element at the specified index to the given value.

Notes:
No bounds checking is performed. Caller must ensure index is valid.

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Int`): Index of the element to set.
- `val` (`Scalar`): Value to assign.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `deep_copy`

```mojo
deep_copy(self) -> Self
```

Create a deep copy of the DataContainer.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `get_ptr`

```mojo
get_ptr(ref self) -> ref[self_is_mut.ptr] UnsafePointer[Scalar[dtype], DataContainer[dtype].origin]
```

Return a reference to the data pointer.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `ref`


</div>

<div class="fn-card" markdown="1">

##### `offset`

```mojo
offset(self, offset: Int) -> UnsafePointer[Scalar[dtype], DataContainer[dtype].origin]
```

Return a pointer offset by the specified number of elements.

**Args:**

- `self` (`Self`)
- `offset` (`Int`): Number of elements to offset from the start.

**Returns:**

- `UnsafePointer`


</div>

<div class="fn-card" markdown="1">

##### `load`

```mojo
load[width: Int](self, offset: Int) -> SIMD[dtype, width]
```

Load a SIMD vector of the specified width from the given offset.

Notes:
No bounds checking is performed. Caller must ensure there are enough elements from `offset`.

**Parameters:**

- `width` (`Int`): Number of elements in the SIMD vector.

**Args:**

- `self` (`Self`)
- `offset` (`Int`): Index of the first element to load.

**Returns:**

- `SIMD`


</div>

<div class="fn-card" markdown="1">

##### `store`

```mojo
store[width: Int](mut self, offset: Int, value: SIMD[dtype, width])
```

Store a SIMD vector of the specified width at the given offset.

Notes:
No bounds checking is performed. Caller must ensure there are enough elements from `offset`.

**Parameters:**

- `width` (`Int`): Number of elements in the SIMD vector.

**Args:**

- `self` (`Self`) `[mut]`
- `offset` (`Int`): Index at which to store the SIMD vector.
- `value` (`SIMD`): SIMD vector to store.


</div>

<div class="fn-card" markdown="1">

##### `__len__`

```mojo
__len__(self) -> Int
```

Return the size of the container.

**Args:**

- `self` (`Self`)

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
__str__(self) -> String
```

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

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

##### `is_refcounted`

```mojo
is_refcounted(ref self) -> Bool
```

Check if this container has refcounting enabled.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `ref_count`

```mojo
ref_count(ref self) -> UInt64
```

Get the current reference count.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `UInt64`


</div>

<div class="fn-card" markdown="1">

##### `share`

```mojo
share(mut self) -> Self
```

Create a shared view into this container. Increments the existing refcount for managed containers.

**Args:**

- `self` (`Self`) `[mut]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the container is externally managed.


</div>
