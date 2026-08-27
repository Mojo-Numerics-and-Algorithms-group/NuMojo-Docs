# `numojo.core.memory.data_container`

Reference-counted memory container for array data.

Manages memory ownership and reference counting for contiguous data buffers
used by NDArray types.

Exports
-------
- `DataContainer`: Reference-counted container for array data.
- `Ownership`: Enum for managed vs external data ownership.

## Structs

### `Ownership`

```mojo
struct Ownership
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`

Enum indicating whether a DataContainer owns its data or views external data.

- Managed: Container owns its data and uses reference counting.
- External: Container views externally managed data and does not deallocate or refcount.

#### Fields

- **`value`** (`Bool`): Ownership status as a boolean.

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

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
def __init__(out self, value: Bool)
```

<span class="badge badge-static">static</span>

Initialize Ownership with the given status.

**Args:**

- `value` (`Bool`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
def __eq__(self, other: Self) -> Bool
```

Return True if both Ownership instances have the same status.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
def __ne__(self, other: Self) -> Bool
```

Return True if Ownership instances have different statuses.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__xor__`

```mojo
def __xor__(self, other: Self) -> Bool
```

Return True if Ownership statuses differ.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
def __str__(self) -> String
```

Return "Managed" or "External" based on ownership status.

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

Write the ownership status as a string to the writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`


</div>
### `DataContainer`

```mojo
struct DataContainer[dtype: DType]
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Movable`, `Sized`, `Writable`

Reference-counted container for a contiguous buffer of elements.

DataContainer can either own its memory (managed) or provide a view into external data (external).
Managed containers use reference counting for shared ownership. External containers do not manage or free memory.

Copying a DataContainer with `.copy()` creates an independent owned copy with its own allocation.
Use `.share()` to create a shared view that increments the reference count.

Fields:
    ptr: Pointer to the data array.
    _refcount: Pointer to the atomic reference count (null for external).
    ownership: Ownership status (Managed or External).
    size: Number of elements in the data array.

**Parameters:**

- `dtype` (`DType`)

#### Fields

- **`ptr`** (`Pointer[Scalar[dtype], DataContainer[dtype].origin]`): Pointer to the data array.
- **`ownership`** (`Ownership`): Ownership status of the container.
- **`size`** (`Int`): Number of elements in the data array.

#### Aliases

##### `origin`

```mojo
comptime origin
```

**Value:** `MutUntrackedOrigin`

Memory origin for the allocation.

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
def __init__(out self)
```

<span class="badge badge-static">static</span>

Create an empty, managed DataContainer.

**Args:**

- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 2

```mojo
def __init__(out self, size: Int)
```

<span class="badge badge-static">static</span>

Create a managed DataContainer with a buffer of `size` elements.

**Args:**

- `size` (`Int`) `[imm]`: Number of elements to allocate (must be non-negative).
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 3

```mojo
def __init__(out self, ptr: Pointer[Scalar[dtype], Self.origin], size: Int, copy: Bool = False)
```

<span class="badge badge-static">static</span>

Create a DataContainer from an existing buffer.

If `copy` is True, the data is deep-copied into managed storage.
If `copy` is False, the container is external and does not manage or
free the memory.

**Args:**

- `ptr` (`Pointer[Scalar[dtype], Self.origin]`) `[imm]`: Pointer to an existing data buffer (must be non-null).
- `size` (`Int`) `[imm]`: Number of elements in the buffer (must be non-negative).
- `copy` (`Bool`) `[imm]`: If True, deep-copy into owned storage.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 4

```mojo
def __init__(out self, *, ptr: Pointer[Scalar[dtype], Self.origin], size: Int, refcount: Pointer[Atomic[DType.uint64], Self.origin], ownership: Ownership)
```

<span class="badge badge-static">static</span>

Create a DataContainer that shares an existing buffer and refcount.

This constructor is used internally by `share()` to create a shared
handle without allocating a new refcount. No validation is performed;
the caller must ensure all arguments are valid.

**Args:**

- `ptr` (`Pointer[Scalar[dtype], Self.origin]`) `[imm]`: Pointer to the shared data buffer.
- `size` (`Int`) `[imm]`: Number of elements in the buffer.
- `refcount` (`Pointer[Atomic[DType.uint64], Self.origin]`) `[imm]`: Pointer to the shared atomic reference count.
- `ownership` (`Ownership`) `[imm]`: Ownership mode (should be Managed for shared handles).
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 5

```mojo
def __init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

Deep copy constructor. Allocates new storage and copies all data.

**Args:**

- `copy` (`Self`) `[imm]`: DataContainer to copy from.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 6

```mojo
def __init__(out self, *, deinit move: Self)
```

<span class="badge badge-static">static</span>

Move constructor.

Transfers ownership without changing the reference count.

**Args:**

- `move` (`Self`) `[deinit]`: DataContainer to move from.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__deinit__`

```mojo
def __deinit__(deinit self)
```

Destructor.

Decrements the reference count and frees memory if this is the last reference.

**Args:**

- `self` (`Self`) `[deinit]`


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

```mojo
def __getitem__(self, idx: Int) -> Scalar[dtype]
```

Return the element at the specified index.

Notes:
No bounds checking is performed. Caller must ensure index is valid.

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: Index of the element to retrieve.

**Returns:**

- `Scalar[dtype]`


</div>

<div class="fn-card" markdown="1">

##### `__setitem__`

```mojo
def __setitem__(mut self, idx: Int, val: Scalar[dtype])
```

Set the element at the specified index to the given value.

Notes:
No bounds checking is performed. Caller must ensure index is valid.

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Int`) `[imm]`: Index of the element to set.
- `val` (`Scalar[dtype]`) `[imm]`: Value to assign.


</div>

<div class="fn-card" markdown="1">

##### `get_ptr`

```mojo
def get_ptr(ref self) -> ref[self_is_mut.ptr] Pointer[Scalar[dtype], Self.origin]
```

Return a reference to the data pointer.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `ref[self_is_mut.ptr] Pointer[Scalar[dtype], Self.origin]`


</div>

<div class="fn-card" markdown="1">

##### `offset`

```mojo
def offset(self, offset: Int) -> Pointer[Scalar[dtype], Self.origin]
```

Return a pointer offset by the specified number of elements.

**Args:**

- `self` (`Self`) `[imm]`
- `offset` (`Int`) `[imm]`: Number of elements to offset from the start.

**Returns:**

- `Pointer[Scalar[dtype], Self.origin]`


</div>

<div class="fn-card" markdown="1">

##### `load`

```mojo
def load[width: Int](self, offset: Int) -> SIMD[dtype, width]
```

Load a SIMD vector of the specified width from the given offset.

Notes:
No bounds checking is performed. Caller must ensure there are enough elements from `offset`.

**Parameters:**

- `width` (`Int`): Number of elements in the SIMD vector.

**Args:**

- `self` (`Self`) `[imm]`
- `offset` (`Int`) `[imm]`: Index of the first element to load.

**Returns:**

- `SIMD[dtype, width]`


</div>

<div class="fn-card" markdown="1">

##### `store`

```mojo
def store[width: Int = Int(1)](mut self, offset: Int, value: SIMD[dtype, width])
```

Store a SIMD vector of the specified width at the given offset.

Notes:
No bounds checking is performed. Caller must ensure there are enough elements from `offset`.

**Parameters:**

- `width` (`Int`): Number of elements in the SIMD vector.

**Args:**

- `self` (`Self`) `[mut]`
- `offset` (`Int`) `[imm]`: Index at which to store the SIMD vector.
- `value` (`SIMD[dtype, width]`) `[imm]`: SIMD vector to store.


</div>

<div class="fn-card" markdown="1">

##### `__len__`

```mojo
def __len__(self) -> Int
```

Return the size of the container.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
def __str__(self) -> String
```

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

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

##### `is_refcounted`

```mojo
def is_refcounted(ref self) -> Bool
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
def ref_count(ref self) -> UInt64
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
def share(self) -> Self
```

Create a shared view into this container. Increments the existing refcount for managed containers.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the container is externally managed.


</div>
