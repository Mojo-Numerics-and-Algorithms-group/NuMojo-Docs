# `numojo.core.memory.storage`

Storage (numojo.core.memory.storage)

Backend storage containers for accelerator-aware data management.

This module provides three storage structs:

- `HostStorage`: Reference-counted host (CPU) memory container.
- `DeviceStorage`: Device (GPU) memory container wrapping a `DeviceBuffer`.
- `AcceleratorDataContainer`: Unified container that selects between
  `HostStorage` and `DeviceStorage` at compile time based on a `Device` parameter.

## Structs

### `HostStorage`

```mojo
struct HostStorage[dtype: DType]
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `ImplicitlyDestructible`, `Movable`, `Sized`, `Stringable`, `Writable`

Reference-counted host (CPU) memory container.

Manages a contiguous buffer of `Scalar[dtype]` elements with two ownership
modes controlled by `Ownership`:

- **Managed**: The container owns the allocation and tracks shared
  references via an atomic reference count.  Memory is freed when the
  last reference is destroyed.
- **External**: The container holds a non-owning view into memory
  managed elsewhere.  No reference counting or deallocation is performed.

**Parameters:**

- `dtype` (`DType`): The element type stored in the buffer.

#### Fields

- **`ptr`** (`UnsafePointer[Scalar[dtype], HostStorage[dtype].origin]`): Pointer to the data array.
- **`ownership`** (`Ownership`): Ownership status of the container (Managed or External).
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

Create an empty managed container with size 0 and refcount 1.

**Args:**

- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 2

```mojo
__init__(out self, size: Int)
```

<span class="badge badge-static">static</span>

Create a managed container with a buffer of `size` elements.

The buffer is allocated but not initialized.  The reference count
starts at 1.

**Args:**

- `size` (`Int`): Number of elements to allocate (must be non-negative).
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 3

```mojo
__init__(out self, ptr: UnsafePointer[Scalar[dtype], HostStorage[dtype].origin], size: Int, copy: Bool = False)
```

<span class="badge badge-static">static</span>

Create a container from an existing buffer.

When `copy` is False the container is **external**: it stores the
pointer as-is and will never free it.  When `copy` is True the data
is deep-copied into a new **managed** allocation.

**Args:**

- `ptr` (`UnsafePointer`): Pointer to an existing data buffer (must be non-null).
- `size` (`Int`): Number of elements in the buffer (must be non-negative).
- `copy` (`Bool`): If True, deep-copy into owned storage; otherwise create
      a non-owning external view.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 4

```mojo
__init__(out self, *, ptr: UnsafePointer[Scalar[dtype], HostStorage[dtype].origin], size: Int, refcount: UnsafePointer[Atomic[DType.uint64], HostStorage[dtype].origin], ownership: Ownership)
```

<span class="badge badge-static">static</span>

Create a HostStorage that shares an existing buffer and refcount.

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

Shallow-copy constructor.

Copies the pointer and refcount, then atomically increments the
reference count for managed containers.

**Args:**

- `copy` (`Self`): The source container.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 6

```mojo
__init__(out self, *, deinit take: Self)
```

<span class="badge badge-static">static</span>

Move constructor.

Transfers all fields without touching the reference count.

**Args:**

- `take` (`Self`) `[deinit]`: The source container (consumed).
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

For managed containers the reference count is atomically
decremented.  If this was the last reference, the data buffer and
the refcount allocation are freed.  External containers are left
untouched.

**Args:**

- `self` (`Self`) `[deinit]`


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

```mojo
__getitem__(self, idx: Int) -> Scalar[dtype]
```

Return the element at index `idx`.

No bounds checking is performed.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): Element index.

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__setitem__`

```mojo
__setitem__(mut self, idx: Int, val: Scalar[dtype])
```

Set the element at index `idx` to `val`.

No bounds checking is performed.

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Int`): Element index.
- `val` (`Scalar`): Value to store.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `unsafe_ptr`

```mojo
unsafe_ptr(ref self) -> ref[self_is_mut.ptr] UnsafePointer[Scalar[dtype], HostStorage[dtype].origin]
```

Return a reference to the raw data pointer.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `ref`


</div>

<div class="fn-card" markdown="1">

##### `offset`

```mojo
offset(self, offset: Int) -> UnsafePointer[Scalar[dtype], HostStorage[dtype].origin]
```

Return a pointer advanced by `offset` elements.

**Args:**

- `self` (`Self`)
- `offset` (`Int`): Number of elements to advance.

**Returns:**

- `UnsafePointer`


</div>

<div class="fn-card" markdown="1">

##### `load`

```mojo
load[width: Int](self, offset: Int) -> SIMD[dtype, width]
```

Load a SIMD vector of `width` elements starting at `offset`.

No bounds checking is performed.

**Parameters:**

- `width` (`Int`): Number of SIMD lanes.

**Args:**

- `self` (`Self`)
- `offset` (`Int`): Element index of the first lane.

**Returns:**

- `SIMD`


</div>

<div class="fn-card" markdown="1">

##### `store`

```mojo
store[width: Int](mut self, offset: Int, value: SIMD[dtype, width])
```

Store a SIMD vector of `width` elements starting at `offset`.

No bounds checking is performed.

**Parameters:**

- `width` (`Int`): Number of SIMD lanes.

**Args:**

- `self` (`Self`) `[mut]`
- `offset` (`Int`): Element index of the first lane.
- `value` (`SIMD`): The SIMD vector to write.


</div>

<div class="fn-card" markdown="1">

##### `__len__`

```mojo
__len__(self) -> Int
```

Return the number of elements.

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

Return a human-readable summary of the container.

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

Write a human-readable summary to `writer`.

**Parameters:**

- `W` (`Writer`): The writer type.

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`: Destination writer.


</div>

<div class="fn-card" markdown="1">

##### `is_refcounted`

```mojo
is_refcounted(ref self) -> Bool
```

Return True if this container tracks a reference count.

External containers and containers whose refcount pointer is null
return False.

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

Return the current reference count, or 0 if not tracked.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `UInt64`


</div>

<div class="fn-card" markdown="1">

##### `deep_copy`

```mojo
deep_copy(self) -> Self
```

Create an independent managed copy of this container.

The returned container has its own allocation and a refcount of 1,
regardless of the source ownership mode.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `share`

```mojo
share(mut self) -> Self
```

Create a new handle that shares this container's data and refcount.

The reference count is atomically incremented so both the original
and the returned container keep the allocation alive.

**Args:**

- `self` (`Self`) `[mut]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the container is externally managed (no refcount).


</div>
### `DeviceStorage`

```mojo
struct DeviceStorage[dtype: DType, device: Device]
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `ImplicitlyDestructible`, `Movable`

Device (GPU) backing storage for `AcceleratorDataContainer`.

Wraps a `DeviceBuffer[dtype]` obtained from a `DeviceContext`.
Copying a `DeviceStorage` copies the `DeviceBuffer` handle (the
runtime may share or duplicate the underlying allocation depending on
the GPU backend).

**Parameters:**

- `dtype` (`DType`): The element type stored in the buffer.
- `device` (`Device`): The target GPU device descriptor.

#### Fields

- **`buffer`** (`DeviceBuffer[dtype]`): The GPU-side data buffer.
- **`size`** (`Int`): Number of elements in the buffer.

#### Aliases

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
__init__(out self, size: Int)
```

<span class="badge badge-static">static</span>

Allocate a new GPU buffer for `size` elements.

**Args:**

- `size` (`Int`): Number of elements to allocate.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If no GPU accelerator is available.

###### Overload 2

```mojo
__init__(out self, buffer: DeviceBuffer[dtype], size: Int)
```

<span class="badge badge-static">static</span>

Wrap an existing `DeviceBuffer`.

**Args:**

- `buffer` (`DeviceBuffer`): An already-allocated device buffer.
- `size` (`Int`): Number of elements accessible in `buffer`.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 3

```mojo
__init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

Shallow-copy constructor.

Copies the `DeviceBuffer` handle.  The GPU runtime determines
whether the underlying memory is shared or duplicated.

**Args:**

- `copy` (`Self`): The source storage.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 4

```mojo
__init__(out self, *, deinit take: Self)
```

<span class="badge badge-static">static</span>

Move constructor.

Transfers the buffer handle without copying.

**Args:**

- `take` (`Self`) `[deinit]`: The source storage (consumed).
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__len__`

```mojo
__len__(self) -> Int
```

Return the number of elements.

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

Return a human-readable summary of the container.

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

Write a human-readable summary to `writer`.

**Parameters:**

- `W` (`Writer`): The writer type.

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`: Destination writer.


</div>

<div class="fn-card" markdown="1">

##### `get_buffer`

```mojo
get_buffer(ref self) -> ref[device.buffer] DeviceBuffer[dtype]
```

Return a reference to the underlying `DeviceBuffer`.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `ref`


</div>

<div class="fn-card" markdown="1">

##### `unsafe_ptr`

```mojo
unsafe_ptr(ref self) -> UnsafePointer[Scalar[dtype], MutAnyOrigin]
```

Return the raw device pointer to the buffer's data.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `UnsafePointer`


</div>
### `AcceleratorDataContainer`

```mojo
struct AcceleratorDataContainer[dtype: DType, device: Device = Device.CPU]
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `ImplicitlyDestructible`, `Movable`, `Sized`, `Stringable`, `Writable`

Unified, reference-counted storage for Host (CPU) or Device (GPU) data.

At compile time the `device` parameter selects the backend:

- **CPU** — delegates to `HostStorage` (atomic refcounted host memory).
- **GPU** — delegates to `DeviceStorage` (device buffer handle).

Only the field corresponding to the active backend is populated;
the other remains `None`.

Shallow copies (via `__copyinit__`) share the underlying allocation
and increment the reference count.  Use `deep_copy()` for an
independent owned copy.

**Parameters:**

- `dtype` (`DType`): The element type stored in the container.
- `device` (`Device`): The execution device (default `Device.CPU`).

#### Fields

- **`host_storage`** (`Optional[HostStorage[dtype]]`): Host (CPU) storage backend.  `None` for GPU containers.
- **`device_storage`** (`Optional[DeviceStorage[dtype, device]]`): Device (GPU) storage backend.  `None` for CPU containers.
- **`size`** (`Int`): Number of elements in the container.

#### Aliases

##### `origin`

```mojo
comptime origin
```

**Value:** `MutExternalOrigin`

Memory origin for the container.

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `(_all_trivial_del[_NoneType, HostStorage[dtype]]() & _all_trivial_del[_NoneType, DeviceStorage[dtype, device]]())`

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
__init__(out self, size: Int)
```

<span class="badge badge-static">static</span>

Allocate storage for `size` elements on the target device.

**Args:**

- `size` (`Int`): Number of elements to allocate (must be non-negative).
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the requested GPU backend is unavailable, or the
device type is unrecognised.

###### Overload 2

```mojo
__init__(out self)
```

<span class="badge badge-static">static</span>

Create an empty container with no storage allocated.

**Args:**

- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 3

```mojo
__init__(out self, ptr: UnsafePointer[Scalar[dtype], MutAnyOrigin], size: Int, copy: Bool = False)
```

<span class="badge badge-static">static</span>

Create a CPU container from an existing host pointer.

When `copy` is False the underlying `HostStorage` is external
(non-owning).  When `copy` is True the data is deep-copied into
a new managed allocation.

!!! info "Constraints"
    Only valid for CPU devices.

**Args:**

- `ptr` (`UnsafePointer`): Pointer to an existing data buffer (must be non-null).
- `size` (`Int`): Number of elements in the buffer (must be non-negative).
- `copy` (`Bool`): If True, deep-copy into owned storage.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 4

```mojo
__init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

Shallow-copy constructor.

Shares the underlying storage.  For CPU containers this increments
the `HostStorage` atomic refcount; for GPU containers this copies
the `DeviceStorage` handle (automatic reference counting).

**Args:**

- `copy` (`Self`): The source container.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 5

```mojo
__init__(out self, *, deinit take: Self)
```

<span class="badge badge-static">static</span>

Move constructor.

Transfers all fields without touching reference counts.

**Args:**

- `take` (`Self`) `[deinit]`: The source container (consumed).
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

```mojo
__getitem__(self, idx: Int) -> Scalar[dtype] where (device.type == "cpu")
```

Return the element at index `idx`.

No bounds checking is performed.

!!! info "Constraints"
    CPU containers only.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): Element index.

**Returns:**

- `Scalar`


</div>

<div class="fn-card" markdown="1">

##### `__setitem__`

```mojo
__setitem__(mut self, idx: Int, val: Scalar[dtype]) where (device.type == "cpu")
```

Set the element at index `idx` to `val`.

No bounds checking is performed.

!!! info "Constraints"
    CPU containers only.

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Int`): Element index.
- `val` (`Scalar`): Value to store.


</div>

<div class="fn-card" markdown="1">

##### `offset`

```mojo
offset(self, offset: Int) -> UnsafePointer[Scalar[dtype], MutExternalOrigin] where (device.type == "cpu")
```

Return a pointer advanced by `offset` elements.

!!! info "Constraints"
    CPU containers only.

**Args:**

- `self` (`Self`)
- `offset` (`Int`): Number of elements to advance.

**Returns:**

- `UnsafePointer`


</div>

<div class="fn-card" markdown="1">

##### `load`

```mojo
load[width: Int](self, offset: Int) -> SIMD[dtype, width] where (device.type == "cpu")
```

Load a SIMD vector of `width` elements starting at `offset`.

No bounds checking is performed.

!!! info "Constraints"
    CPU containers only.

**Parameters:**

- `width` (`Int`): Number of SIMD lanes.

**Args:**

- `self` (`Self`)
- `offset` (`Int`): Element index of the first lane.

**Returns:**

- `SIMD`


</div>

<div class="fn-card" markdown="1">

##### `store`

```mojo
store[width: Int](mut self, offset: Int, value: SIMD[dtype, width]) where (device.type == "cpu")
```

Store a SIMD vector of `width` elements starting at `offset`.

No bounds checking is performed.

!!! info "Constraints"
    CPU containers only.

**Parameters:**

- `width` (`Int`): Number of SIMD lanes.

**Args:**

- `self` (`Self`) `[mut]`
- `offset` (`Int`): Element index of the first lane.
- `value` (`SIMD`): The SIMD vector to write.


</div>

<div class="fn-card" markdown="1">

##### `__len__`

```mojo
__len__(self) -> Int
```

Return the number of elements.

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

Return a human-readable summary of the container.

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

Write a human-readable summary to `writer`.

**Parameters:**

- `W` (`Writer`): The writer type.

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`: Destination writer.


</div>

<div class="fn-card" markdown="1">

##### `deep_copy`

```mojo
deep_copy(self) -> Self
```

Create an independent managed copy of this container.

For CPU containers the data is copied via `memcpy`.  For GPU
containers the copy is enqueued on the device context.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `share`

```mojo
share(mut self) -> Self
```

Create a new handle that shares this container's storage.

For CPU containers the `HostStorage` refcount is atomically
incremented.  For GPU containers the `DeviceStorage` handle is
copied (the runtime manages device-side sharing).

**Args:**

- `self` (`Self`) `[mut]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the active storage is missing or cannot be shared.


</div>

<div class="fn-card" markdown="1">

##### `is_cpu`

```mojo
is_cpu(self) -> Bool
```

Return True if this container targets a CPU device.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_gpu`

```mojo
is_gpu(self) -> Bool
```

Return True if this container targets a GPU device.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_cuda`

```mojo
is_cuda(self) -> Bool
```

Return True if this container targets an NVIDIA CUDA device.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_rocm`

```mojo
is_rocm(self) -> Bool
```

Return True if this container targets an AMD ROCm device.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_mps`

```mojo
is_mps(self) -> Bool
```

Return True if this container targets an Apple Metal device.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `host_ptr`

```mojo
host_ptr(self) -> UnsafePointer[Scalar[dtype], MutAnyOrigin] where (device == Device.CPU)
```

Return the raw host pointer to the CPU allocation.

!!! info "Constraints"
    Only valid when `device` is `Device.CPU`.

**Args:**

- `self` (`Self`)

**Returns:**

- `UnsafePointer`


</div>

<div class="fn-card" markdown="1">

##### `device_ptr`

```mojo
device_ptr(self) -> UnsafePointer[Scalar[dtype], MutAnyOrigin] where (device == Device.CUDA) if (device == Device.CUDA) else (device == Device.ROCM) if (device == Device.CUDA) if (device == Device.CUDA) else (device == Device.ROCM) else (device == Device.MPS)
```

Return the raw device pointer to the GPU allocation.

!!! info "Constraints"
    Only valid for GPU devices (CUDA / ROCm / MPS).

**Args:**

- `self` (`Self`)

**Returns:**

- `UnsafePointer`


</div>

<div class="fn-card" markdown="1">

##### `host_buffer`

```mojo
host_buffer(self) -> HostStorage[dtype] where (device == Device.CPU)
```

Return a shallow copy of the underlying `HostStorage`.

The returned copy shares the same data pointer and refcount
(the refcount is incremented).

!!! info "Constraints"
    Only valid for CPU containers.

**Args:**

- `self` (`Self`)

**Returns:**

- `HostStorage`


</div>

<div class="fn-card" markdown="1">

##### `device_buffer`

```mojo
device_buffer(self) -> DeviceStorage[dtype, device] where (device == Device.CUDA) if (device == Device.CUDA) else (device == Device.ROCM) if (device == Device.CUDA) if (device == Device.CUDA) else (device == Device.ROCM) else (device == Device.MPS)
```

Return a shallow copy of the underlying `DeviceStorage`.

!!! info "Constraints"
    Only valid for GPU devices (CUDA / ROCm / MPS).

**Args:**

- `self` (`Self`)

**Returns:**

- `DeviceStorage`


</div>
