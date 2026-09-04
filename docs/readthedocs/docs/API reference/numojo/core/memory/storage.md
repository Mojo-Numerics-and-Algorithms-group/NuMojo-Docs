# `numojo.core.memory.storage`

Backend storage containers for accelerator-aware data management.

Provides reference-counted and device-aware memory storage with unified
container selection based on device type at compile time.

Exports
-------
- `HostStorage`: Reference-counted host (CPU) memory container.
- `DeviceStorage`: Device (GPU) memory container.
- `AcceleratorDataContainer`: Unified container selecting storage by device.

## Structs

### `HostStorage`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct HostStorage[dtype: DType]
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Movable`, `Sized`, `Writable`

Reference-counted host (CPU) memory container.

Manages a contiguous buffer of `Scalar[dtype]` elements with two ownership
modes controlled by `Ownership`:

- **Managed**: The container owns the allocation and tracks shared
  references via an atomic reference count.  Memory is freed when the
  last reference is destroyed.
- **External**: The container holds a non-owning view into memory
  managed elsewhere.  No reference counting or deallocation is performed.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type stored in the buffer.

</div>

#### Fields

- **`ptr`** (`Pointer[Scalar[dtype], HostStorage[dtype].origin]`): Pointer to the data array.
- **`ownership`** (`Ownership`): Ownership status of the container (Managed or External).
- **`size`** (`Int`): Number of elements in the data array.

#### Aliases

#### `origin`

```mojo
comptime origin
```

**Value:** `MutUntrackedOrigin`

Memory origin for the allocation.

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

<div class="overload-divider">Overload 1</div>

```mojo
def __init__(out self)
```

<span class="badge badge-static">static</span>

Create an empty managed container with size 0 and refcount 1.

<div class="prose-label">Args</div>

- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __init__(out self, size: Int)
```

<span class="badge badge-static">static</span>

Create a managed container with a buffer of `size` elements.

The buffer is allocated but not initialized.  The reference count
starts at 1.

<div class="prose-label">Args</div>

- `size` (`Int`) `[imm]`: Number of elements to allocate (must be non-negative).
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 3</div>

```mojo
def __init__(out self, ptr: Pointer[Scalar[dtype], Self.origin], size: Int, copy: Bool = False)
```

<span class="badge badge-static">static</span>

Create a container from an existing buffer.

When `copy` is False the container is **external**: it stores the
pointer as-is and will never free it.  When `copy` is True the data
is deep-copied into a new **managed** allocation.

<div class="prose-label">Args</div>

- `ptr` (`Pointer[Scalar[dtype], Self.origin]`) `[imm]`: Pointer to an existing data buffer (must be non-null).
- `size` (`Int`) `[imm]`: Number of elements in the buffer (must be non-negative).
- `copy` (`Bool`) `[imm]`: If True, deep-copy into owned storage; otherwise create
      a non-owning external view.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 4</div>

```mojo
def __init__(out self, *, ptr: Pointer[Scalar[dtype], Self.origin], size: Int, refcount: Pointer[Atomic[DType.uint64], Self.origin], ownership: Ownership)
```

<span class="badge badge-static">static</span>

Create a HostStorage that shares an existing buffer and refcount.

This constructor is used internally by `share()` to create a shared
handle without allocating a new refcount. No validation is performed;
the caller must ensure all arguments are valid.

<div class="prose-label">Args</div>

- `ptr` (`Pointer[Scalar[dtype], Self.origin]`) `[imm]`: Pointer to the shared data buffer.
- `size` (`Int`) `[imm]`: Number of elements in the buffer.
- `refcount` (`Pointer[Atomic[DType.uint64], Self.origin]`) `[imm]`: Pointer to the shared atomic reference count.
- `ownership` (`Ownership`) `[imm]`: Ownership mode (should be Managed for shared handles).
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 5</div>

```mojo
def __init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

Deep-copy constructor.

Matches `DataContainer`: allocate owned storage and copy the data.
Use `share()` for a shallow shared handle.

<div class="prose-label">Args</div>

- `copy` (`Self`) `[imm]`: The source container.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 6</div>

```mojo
def __init__(out self, *, deinit move: Self)
```

<span class="badge badge-static">static</span>

Move constructor.

Transfers all fields without touching the reference count.

<div class="prose-label">Args</div>

- `move` (`Self`) `[deinit]`: The source container (consumed).
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__deinit__`

```mojo
def __deinit__(deinit self)
```

Destructor.

For managed containers the reference count is atomically
decremented.  If this was the last reference, the data buffer and
the refcount allocation are freed.  External containers are left
untouched.

<div class="prose-label">Args</div>

- `self` (`Self`) `[deinit]`


</div>

<div class="fn-card" markdown="1">

#### `__getitem__`

```mojo
def __getitem__(self, idx: Int) -> Scalar[dtype]
```

Return the element at index `idx`.

No bounds checking is performed.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: Element index.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`


</div>

<div class="fn-card" markdown="1">

#### `__setitem__`

```mojo
def __setitem__(mut self, idx: Int, val: Scalar[dtype])
```

Set the element at index `idx` to `val`.

No bounds checking is performed.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `idx` (`Int`) `[imm]`: Element index.
- `val` (`Scalar[dtype]`) `[imm]`: Value to store.


</div>

<div class="fn-card" markdown="1">

#### `unsafe_ptr`

```mojo
def unsafe_ptr(ref self) -> ref[self_is_mut.ptr] Pointer[Scalar[dtype], Self.origin]
```

Return a reference to the raw data pointer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`

<div class="prose-label">Returns</div>

- `ref[self_is_mut.ptr] Pointer[Scalar[dtype], Self.origin]`


</div>

<div class="fn-card" markdown="1">

#### `get_ptr`

```mojo
def get_ptr(ref self) -> ref[self_is_mut.ptr] Pointer[Scalar[dtype], Self.origin]
```

Return a reference to the raw data pointer.

This mirrors `DataContainer.get_ptr()`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`

<div class="prose-label">Returns</div>

- `ref[self_is_mut.ptr] Pointer[Scalar[dtype], Self.origin]`


</div>

<div class="fn-card" markdown="1">

#### `offset`

```mojo
def offset(self, offset: Int) -> Pointer[Scalar[dtype], Self.origin]
```

Return a pointer advanced by `offset` elements.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `offset` (`Int`) `[imm]`: Number of elements to advance.

<div class="prose-label">Returns</div>

- `Pointer[Scalar[dtype], Self.origin]`


</div>

<div class="fn-card" markdown="1">

#### `load`

```mojo
def load[width: Int](self, offset: Int) -> SIMD[dtype, width]
```

Load a SIMD vector of `width` elements starting at `offset`.

No bounds checking is performed.

<div class="prose-label">Parameters</div>

- `width` (`Int`): Number of SIMD lanes.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `offset` (`Int`) `[imm]`: Element index of the first lane.

<div class="prose-label">Returns</div>

- `SIMD[dtype, width]`


</div>

<div class="fn-card" markdown="1">

#### `store`

```mojo
def store[width: Int = Int(1)](mut self, offset: Int, value: SIMD[dtype, width])
```

Store a SIMD vector of `width` elements starting at `offset`.

No bounds checking is performed.

<div class="prose-label">Parameters</div>

- `width` (`Int`): Number of SIMD lanes.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `offset` (`Int`) `[imm]`: Element index of the first lane.
- `value` (`SIMD[dtype, width]`) `[imm]`: The SIMD vector to write.


</div>

<div class="fn-card" markdown="1">

#### `__len__`

```mojo
def __len__(self) -> Int
```

Return the number of elements.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `__str__`

```mojo
def __str__(self) -> String
```

Return a human-readable summary of the container.

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

Write a human-readable summary to `writer`.

<div class="prose-label">Parameters</div>

- `W` (`Writer`): The writer type.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`: Destination writer.


</div>

<div class="fn-card" markdown="1">

#### `is_refcounted`

```mojo
def is_refcounted(ref self) -> Bool
```

Return True if this container tracks a reference count.

External containers and containers whose refcount pointer is null
return False.

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `ref_count`

```mojo
def ref_count(ref self) -> UInt64
```

Return the current reference count, or 0 if not tracked.

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`

<div class="prose-label">Returns</div>

- `UInt64`


</div>

<div class="fn-card" markdown="1">

#### `share`

```mojo
def share(self) -> Self
```

Create a new handle that shares this container's data and refcount.

The reference count is atomically incremented so both the original
and the returned container keep the allocation alive.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the container is externally managed (no refcount).


</div>
### `DeviceStorage`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct DeviceStorage[dtype: DType, device: Device]
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Movable`

Device (GPU) backing storage for `AcceleratorDataContainer`.

Wraps a `DeviceBuffer[dtype]` obtained from a `DeviceContext`.
Copying a `DeviceStorage` copies the `DeviceBuffer` handle (the
runtime may share or duplicate the underlying allocation depending on
the GPU backend).

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type stored in the buffer.
- `device` (`Device`): The target GPU device descriptor.

</div>

#### Fields

- **`buffer`** (`DeviceBuffer[dtype]`): The GPU-side data buffer.
- **`handle`** (`DeviceHandle[device]`): Runtime handle that owns the device context used for this storage.
- **`size`** (`Int`): Number of elements in the buffer.

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

<div class="overload-divider">Overload 1</div>

```mojo
def __init__(out self, size: Int)
```

<span class="badge badge-static">static</span>

Allocate a new GPU buffer for `size` elements.

<div class="prose-label">Args</div>

- `size` (`Int`) `[imm]`: Number of elements to allocate.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If no GPU accelerator is available.

<div class="overload-divider">Overload 2</div>

```mojo
def __init__(out self, buffer: DeviceBuffer[dtype], size: Int)
```

<span class="badge badge-static">static</span>

Wrap an existing `DeviceBuffer`.

<div class="prose-label">Args</div>

- `buffer` (`DeviceBuffer[dtype]`) `[imm]`: An already-allocated device buffer.
- `size` (`Int`) `[imm]`: Number of elements accessible in `buffer`.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def __init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

Deep-copy constructor.

Allocates a new buffer on the same device context and copies all data.
Use `share()` for a shallow shared handle.

<div class="prose-label">Args</div>

- `copy` (`Self`) `[imm]`: The source storage.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 4</div>

```mojo
def __init__(out self, *, deinit move: Self)
```

<span class="badge badge-static">static</span>

Move constructor.

Transfers the buffer handle without copying.

<div class="prose-label">Args</div>

- `move` (`Self`) `[deinit]`: The source storage (consumed).
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__len__`

```mojo
def __len__(self) -> Int
```

Return the number of elements.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `__str__`

```mojo
def __str__(self) -> String
```

Return a human-readable summary of the container.

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

Write a human-readable summary to `writer`.

<div class="prose-label">Parameters</div>

- `W` (`Writer`): The writer type.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`: Destination writer.


</div>

<div class="fn-card" markdown="1">

#### `get_buffer`

```mojo
def get_buffer(ref self) -> ref[device.buffer] DeviceBuffer[dtype]
```

Return a reference to the underlying `DeviceBuffer`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`

<div class="prose-label">Returns</div>

- `ref[device.buffer] DeviceBuffer[dtype]`


</div>

<div class="fn-card" markdown="1">

#### `unsafe_ptr`

```mojo
def unsafe_ptr(ref self) -> Pointer[Scalar[dtype], MutAnyOrigin]
```

Return the raw device pointer to the buffer's data.

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`

<div class="prose-label">Returns</div>

- `Pointer[Scalar[dtype], MutAnyOrigin]`


</div>

<div class="fn-card" markdown="1">

#### `share`

```mojo
def share(self) -> Self
```

Create a shallow handle sharing this device buffer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
### `AcceleratorDataContainer`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct AcceleratorDataContainer[dtype: DType, device: Device = Device.CPU]
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Movable`, `Sized`, `Writable`

Unified, reference-counted storage for Host (CPU) or Device (GPU) data.

At compile time the `device` parameter selects the backend:

- **CPU** — delegates to `HostStorage` (atomic refcounted host memory).
- **GPU** — delegates to `DeviceStorage` (device buffer handle).

Only the field corresponding to the active backend is populated;
the other remains `None`.

Shallow copies (via `__copyinit__`) share the underlying allocation
and increment the reference count.  Use `.share()` for an explicit shared handle.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type stored in the container.
- `device` (`Device`): The execution device (default `Device.CPU`).

</div>

#### Fields

- **`host_storage`** (`Optional[HostStorage[dtype]]`): Host (CPU) storage backend.  `None` for GPU containers.
- **`device_storage`** (`Optional[DeviceStorage[dtype, device]]`): Device (GPU) storage backend.  `None` for CPU containers.
- **`size`** (`Int`): Number of elements in the container.

#### Aliases

#### `origin`

```mojo
comptime origin
```

**Value:** `MutUntrackedOrigin`

Memory origin for the container.

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

<div class="overload-divider">Overload 1</div>

```mojo
def __init__(out self, size: Int)
```

<span class="badge badge-static">static</span>

Allocate storage for `size` elements on the target device.

<div class="prose-label">Args</div>

- `size` (`Int`) `[imm]`: Number of elements to allocate (must be non-negative).
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the requested GPU backend is unavailable, or the
device type is unrecognised.

<div class="overload-divider">Overload 2</div>

```mojo
def __init__(out self)
```

<span class="badge badge-static">static</span>

Create an empty container with no storage allocated.

<div class="prose-label">Args</div>

- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 3</div>

```mojo
def __init__(out self, ptr: Pointer[Scalar[dtype], MutAnyOrigin], size: Int, copy: Bool = False)
```

<span class="badge badge-static">static</span>

Create a CPU container from an existing host pointer.

When `copy` is False the underlying `HostStorage` is external
(non-owning).  When `copy` is True the data is deep-copied into
a new managed allocation.

!!! info "Constraints"
    Only valid for CPU devices.

<div class="prose-label">Args</div>

- `ptr` (`Pointer[Scalar[dtype], MutAnyOrigin]`) `[imm]`: Pointer to an existing data buffer (must be non-null).
- `size` (`Int`) `[imm]`: Number of elements in the buffer (must be non-negative).
- `copy` (`Bool`) `[imm]`: If True, deep-copy into owned storage.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 4</div>

```mojo
def __init__(out self, var host_storage: HostStorage[dtype]) where (device.type == String("cpu"))
```

<span class="badge badge-static">static</span>

Create a CPU container from an existing `HostStorage` handle.

<div class="prose-label">Args</div>

- `host_storage` (`HostStorage[dtype]`) `[var]`
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 5</div>

```mojo
def __init__(out self, var device_storage: DeviceStorage[dtype, device]) where (device.type == String("gpu"))
```

<span class="badge badge-static">static</span>

Create a GPU container from an existing `DeviceStorage` handle.

<div class="prose-label">Args</div>

- `device_storage` (`DeviceStorage[dtype, device]`) `[var]`
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 6</div>

```mojo
def __init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

Deep-copy constructor.

Copies the active backend container. Use `share()` for a shallow
shared handle.

<div class="prose-label">Args</div>

- `copy` (`Self`) `[imm]`: The source container.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 7</div>

```mojo
def __init__(out self, *, deinit move: Self)
```

<span class="badge badge-static">static</span>

Move constructor.

Transfers all fields without touching reference counts.

<div class="prose-label">Args</div>

- `move` (`Self`) `[deinit]`: The source container (consumed).
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__getitem__`

```mojo
def __getitem__(self, idx: Int) -> Scalar[dtype] where (device.type == String("cpu"))
```

Return the element at index `idx`.

No bounds checking is performed.

!!! info "Constraints"
    CPU containers only.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: Element index.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`


</div>

<div class="fn-card" markdown="1">

#### `__setitem__`

```mojo
def __setitem__(mut self, idx: Int, val: Scalar[dtype]) where (device.type == String("cpu"))
```

Set the element at index `idx` to `val`.

No bounds checking is performed.

!!! info "Constraints"
    CPU containers only.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `idx` (`Int`) `[imm]`: Element index.
- `val` (`Scalar[dtype]`) `[imm]`: Value to store.


</div>

<div class="fn-card" markdown="1">

#### `offset`

```mojo
def offset(self, offset: Int) -> Pointer[Scalar[dtype], MutUntrackedOrigin] where (device.type == String("cpu"))
```

Return a pointer advanced by `offset` elements.

!!! info "Constraints"
    CPU containers only.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `offset` (`Int`) `[imm]`: Number of elements to advance.

<div class="prose-label">Returns</div>

- `Pointer[Scalar[dtype], MutUntrackedOrigin]`


</div>

<div class="fn-card" markdown="1">

#### `load`

```mojo
def load[width: Int](self, offset: Int) -> SIMD[dtype, width] where (device.type == String("cpu"))
```

Load a SIMD vector of `width` elements starting at `offset`.

No bounds checking is performed.

!!! info "Constraints"
    CPU containers only.

<div class="prose-label">Parameters</div>

- `width` (`Int`): Number of SIMD lanes.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `offset` (`Int`) `[imm]`: Element index of the first lane.

<div class="prose-label">Returns</div>

- `SIMD[dtype, width]`


</div>

<div class="fn-card" markdown="1">

#### `store`

```mojo
def store[width: Int = Int(1)](mut self, offset: Int, value: SIMD[dtype, width]) where (device.type == String("cpu"))
```

Store a SIMD vector of `width` elements starting at `offset`.

No bounds checking is performed.

!!! info "Constraints"
    CPU containers only.

<div class="prose-label">Parameters</div>

- `width` (`Int`): Number of SIMD lanes.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `offset` (`Int`) `[imm]`: Element index of the first lane.
- `value` (`SIMD[dtype, width]`) `[imm]`: The SIMD vector to write.


</div>

<div class="fn-card" markdown="1">

#### `__len__`

```mojo
def __len__(self) -> Int
```

Return the number of elements.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `__str__`

```mojo
def __str__(self) -> String
```

Return a human-readable summary of the container.

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

Write a human-readable summary to `writer`.

<div class="prose-label">Parameters</div>

- `W` (`Writer`): The writer type.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`: Destination writer.


</div>

<div class="fn-card" markdown="1">

#### `share`

```mojo
def share(self) -> Self
```

Create a new handle that shares this container's storage.

For CPU containers the `HostStorage` refcount is atomically
incremented.  For GPU containers the `DeviceStorage` handle is
copied (the runtime manages device-side sharing).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the active storage is missing or cannot be shared.


</div>

<div class="fn-card" markdown="1">

#### `is_cpu`

```mojo
def is_cpu(self) -> Bool
```

Return True if this container targets a CPU device.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `is_gpu`

```mojo
def is_gpu(self) -> Bool
```

Return True if this container targets a GPU device.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `is_cuda`

```mojo
def is_cuda(self) -> Bool
```

Return True if this container targets an NVIDIA CUDA device.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `is_rocm`

```mojo
def is_rocm(self) -> Bool
```

Return True if this container targets an AMD ROCm device.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `is_mps`

```mojo
def is_mps(self) -> Bool
```

Return True if this container targets an Apple Metal device.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `host_ptr`

```mojo
def host_ptr(self) -> Pointer[Scalar[dtype], MutAnyOrigin] where (device == Device.CPU)
```

Return the raw host pointer to the CPU allocation.

!!! info "Constraints"
    Only valid when `device` is `Device.CPU`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Pointer[Scalar[dtype], MutAnyOrigin]`


</div>

<div class="fn-card" markdown="1">

#### `device_ptr`

```mojo
def device_ptr(self) -> Pointer[Scalar[dtype], MutAnyOrigin] where (device == Device.CUDA) or (device == Device.ROCM) or (device == Device.MPS)
```

Return the raw device pointer to the GPU allocation.

!!! info "Constraints"
    Only valid for GPU devices (CUDA / ROCm / MPS).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Pointer[Scalar[dtype], MutAnyOrigin]`


</div>

<div class="fn-card" markdown="1">

#### `host_buffer`

```mojo
def host_buffer(self) -> HostStorage[dtype] where (device == Device.CPU)
```

Return a shallow copy of the underlying `HostStorage`.

The returned copy shares the same data pointer and refcount
(the refcount is incremented).

!!! info "Constraints"
    Only valid for CPU containers.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `HostStorage[dtype]`


</div>

<div class="fn-card" markdown="1">

#### `device_buffer`

```mojo
def device_buffer(self) -> DeviceStorage[dtype, device] where (device == Device.CUDA) or (device == Device.ROCM) or (device == Device.MPS)
```

Return a shallow copy of the underlying `DeviceStorage`.

!!! info "Constraints"
    Only valid for GPU devices (CUDA / ROCm / MPS).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `DeviceStorage[dtype, device]`


</div>
