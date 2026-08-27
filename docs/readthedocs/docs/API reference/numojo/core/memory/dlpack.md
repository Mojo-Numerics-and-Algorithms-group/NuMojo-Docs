# `numojo.core.memory.dlpack`

Zero-copy tensor exchange via DLPack protocol.

Implements the DLPack protocol for zero-copy data exchange between NuMojo
and other array libraries (NumPy, PyTorch, JAX, etc.).

Exports
-------
- `from_dlpack`: Create NDArray from DLPack tensor.
- `to_dlpack`: Export NDArray as DLPack tensor.

References
----------
- DLPack Specification: https://dmlc.github.io/dlpack/latest/

Examples
--------
    ```mojo
    from numojo.prelude import *
    from numojo.core.memory.dlpack import from_dlpack
    from python import Python

    def main() raises:
        # Create a NuMojo array
        var arr = nm.linspace[f32](0, 5, 6)

        # Import NumPy array back to NuMojo via DLPack
        var np = Python.import_module("numpy")
        var numpy_data = np.linspace(0, 5, 6, dtype=np.float32)
        var mojo_arr = from_dlpack[f32](numpy_data)
        print(mojo_arr)

        # Import PyTorch tensor to NuMojo via DLPack
        var torch = Python.import_module("torch")
        var torch_tensor = torch.rand(Python.tuple(4, 4), dtype=torch.float64)
        var mojo_tensor = from_dlpack[f64](torch_tensor)
        print(mojo_tensor)
    ```

## Aliases

### `DLManagedTensorDeleter`

```mojo
comptime DLManagedTensorDeleter
```

**Value:** `def(Pointer[DLManagedTensor, MutUntrackedOrigin]) capturing thin -> None`

## Structs

### `DLPackVersion`

```mojo
struct DLPackVersion
```

**Memory convention:** `register_passable_trivial`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`, `RegisterPassable`, `TrivialRegisterPassable`

Represents a DLPack version structure for compatibility checking.

This structure stores major and minor version numbers to ensure compatibility
between different implementations of the DLPack protocol. The current
implementation targets DLPack version 0.8.

Attributes:
    major: Major version number.
    minor: Minor version number.

Constants:
    CURRENT_MAJOR: Current major version (0).
    CURRENT_MINOR: Current minor version (8).
    LATEST: Latest version instance.

#### Fields

- **`major`** (`UInt32`)
- **`minor`** (`UInt32`)

#### Aliases

##### `CURRENT_MAJOR`

```mojo
comptime CURRENT_MAJOR
```

**Value:** `UInt32(0)`

##### `CURRENT_MINOR`

```mojo
comptime CURRENT_MINOR
```

**Value:** `UInt32(8)`

##### `LATEST`

```mojo
comptime LATEST
```

**Value:** `DLPackVersion(UInt32(0), UInt32(8))`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
def __init__(major: UInt32, minor: UInt32) -> Self
```

<span class="badge badge-static">static</span>

**Args:**

- `major` (`UInt32`) `[imm]`
- `minor` (`UInt32`) `[imm]`

**Returns:**

- `Self`


</div>
### `DLDevice`

```mojo
struct DLDevice
```

**Memory convention:** `register_passable_trivial`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`, `RegisterPassable`, `TrivialRegisterPassable`

Represents a device context for tensor data.

Describes where the tensor data is physically located (CPU, GPU, etc.)
and which specific device instance to use if there are multiple devices
of the same type.

Attributes:
    device_type: Device type code (CPU=1, CUDA=2, OPENCL=4, etc.).
    device_id: Device ID for multiple devices of the same type (usually 0).

Constants:
    CPU: CPU device type code (1).
    CUDA: CUDA GPU device type code (2).
    OPENCL: OpenCL device type code (4).
    VULKAN: Vulkan device type code (7).
    METAL: Metal device type code (8).
    VPI: VPI device type code (9).
    ROCM: ROCm device type code (10).

#### Fields

- **`device_type`** (`Int32`): Device type code.
- **`device_id`** (`Int32`): Device ID (for multiple devices of same type).

#### Aliases

##### `CPU`

```mojo
comptime CPU
```

**Value:** `1`

##### `CUDA`

```mojo
comptime CUDA
```

**Value:** `2`

##### `OPENCL`

```mojo
comptime OPENCL
```

**Value:** `4`

##### `VULKAN`

```mojo
comptime VULKAN
```

**Value:** `7`

##### `METAL`

```mojo
comptime METAL
```

**Value:** `8`

##### `VPI`

```mojo
comptime VPI
```

**Value:** `9`

##### `ROCM`

```mojo
comptime ROCM
```

**Value:** `10`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
def __init__(device_type: Int32 = Int32(1), device_id: Int32 = Int32(0)) -> Self
```

<span class="badge badge-static">static</span>

**Args:**

- `device_type` (`Int32`) `[imm]`
- `device_id` (`Int32`) `[imm]`

**Returns:**

- `Self`


</div>
### `DLDataType`

```mojo
struct DLDataType
```

**Memory convention:** `register_passable_trivial`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`, `RegisterPassable`, `TrivialRegisterPassable`

Represents a data type descriptor for tensor elements.

Describes the element type using a type code (int/float/complex/bool),
bit width (8, 16, 32, 64, etc.), and number of lanes for vector types.

Attributes:
    code: Type code (INT=0, UINT=1, FLOAT=2, BFLOAT=4, COMPLEX=5, BOOL=6).
    bits: Number of bits per element (8, 16, 32, 64, etc.).
    lanes: Number of lanes (1 for scalar types, >1 for vector types).

Constants:
    INT: Signed integer type code (0).
    UINT: Unsigned integer type code (1).
    FLOAT: Floating-point type code (2).
    BFLOAT: Brain floating-point type code (4).
    COMPLEX: Complex number type code (5).
    BOOL: Boolean type code (6).

#### Fields

- **`code`** (`UInt8`): Type code (INT, UINT, FLOAT, etc.).
- **`bits`** (`UInt8`): Number of bits per element.
- **`lanes`** (`UInt16`): Number of lanes (1 for scalar, >1 for vector types).

#### Aliases

##### `INT`

```mojo
comptime INT
```

**Value:** `0`

##### `UINT`

```mojo
comptime UINT
```

**Value:** `1`

##### `FLOAT`

```mojo
comptime FLOAT
```

**Value:** `2`

##### `BFLOAT`

```mojo
comptime BFLOAT
```

**Value:** `4`

##### `COMPLEX`

```mojo
comptime COMPLEX
```

**Value:** `5`

##### `BOOL`

```mojo
comptime BOOL
```

**Value:** `6`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
def __init__(code: UInt8, bits: UInt8, lanes: UInt16 = UInt16(1)) -> Self
```

<span class="badge badge-static">static</span>

**Args:**

- `code` (`UInt8`) `[imm]`
- `bits` (`UInt8`) `[imm]`
- `lanes` (`UInt16`) `[imm]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `from_dtype`

```mojo
def from_dtype[dtype: DType]() -> Self
```

<span class="badge badge-static">static</span>

Converts a Mojo DType to a DLDataType descriptor.

This static method maps Mojo's native data types to the DLPack type
system, determining the appropriate type code (INT, UINT, FLOAT) and bit
width based on the input DType.

**Parameters:**

- `dtype` (`DType`): Mojo data type to convert.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `to_dtype`

```mojo
def to_dtype(self) -> DType
```

Converts a DLDataType descriptor to a Mojo DType.

This method maps DLPack type descriptors back to Mojo's native data types,
supporting common floating-point (float16/32/64) and integer types
(int8/16/32/64, uint8/16/32/64).

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `DType`

!!! failure "Raises"
    NumojoError: If the type code is not supported.
NumojoError: If the bit width is not supported for the given type code.
NumojoError: If vector types (lanes > 1) are encountered (not yet
supported).


</div>
### `DLTensor`

```mojo
struct DLTensor
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`

Represents the core tensor structure containing data pointer and metadata.

This is the fundamental structure that describes a tensor's memory layout,
shape, strides, and data type without managing its lifetime. It provides
a view into tensor data without ownership semantics.

Attributes:
    data: Opaque pointer to the tensor data.
    device: Device where the data resides.
    ndim: Number of dimensions.
    dtype: Element data type descriptor.
    shape: Pointer to shape array (size = ndim).
    strides: Pointer to strides array in elements (size = ndim).
    byte_offset: Byte offset from data pointer to first element.

#### Fields

- **`data`** (`Pointer[NoneType, MutUntrackedOrigin]`): Opaque pointer to the tensor data.
- **`device`** (`DLDevice`): Device where the data resides.
- **`ndim`** (`Int32`): Number of dimensions.
- **`dtype`** (`DLDataType`): Element data type.
- **`shape`** (`Pointer[Int64, MutUntrackedOrigin]`): Shape array.
- **`strides`** (`Pointer[Int64, MutUntrackedOrigin]`): Strides in elements.
- **`byte_offset`** (`UInt64`): Byte offset from data pointer to first element.

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
def __init__(out self, data: Pointer[NoneType, MutUntrackedOrigin], device: DLDevice, ndim: Int32, dtype: DLDataType, shape: Pointer[Int64, MutUntrackedOrigin], strides: Pointer[Int64, MutUntrackedOrigin], byte_offset: UInt64 = UInt64(0))
```

<span class="badge badge-static">static</span>

**Args:**

- `data` (`Pointer[NoneType, MutUntrackedOrigin]`) `[imm]`
- `device` (`DLDevice`) `[imm]`
- `ndim` (`Int32`) `[imm]`
- `dtype` (`DLDataType`) `[imm]`
- `shape` (`Pointer[Int64, MutUntrackedOrigin]`) `[imm]`
- `strides` (`Pointer[Int64, MutUntrackedOrigin]`) `[imm]`
- `byte_offset` (`UInt64`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>
### `DLManagedTensor`

```mojo
struct DLManagedTensor
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`

Represents a managed tensor structure that includes a deleter callback for lifetime management.

This structure wraps a DLTensor with a deleter callback and optional
context pointer for resource cleanup. The deleter is called by the
consumer when they're done with the data, ensuring proper memory management
in cross-framework data sharing scenarios.

Attributes:
    dl_tensor: The underlying tensor structure.
    manager_ctx: Context pointer for the deleter (stores metadata, refcount,
        etc.).
    deleter: Cleanup function called when consumer finishes using the tensor.

Note:
This implements the older DLPack API. The current specification uses
DLManagedTensorVersioned with a version field for forward compatibility.

#### Fields

- **`dl_tensor`** (`DLTensor`): The underlying tensor.
- **`manager_ctx`** (`Pointer[NoneType, MutUntrackedOrigin]`): Context pointer for the deleter (stores metadata, refcount, etc.).
- **`deleter`** (`def(Pointer[DLManagedTensor, MutUntrackedOrigin]) capturing thin -> None`): Cleanup function called when consumer is done.

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
def __init__(out self, dl_tensor: DLTensor, manager_ctx: Pointer[NoneType, MutUntrackedOrigin], deleter: def(Pointer[Self, MutUntrackedOrigin]) capturing thin -> None)
```

<span class="badge badge-static">static</span>

**Args:**

- `dl_tensor` (`DLTensor`) `[imm]`
- `manager_ctx` (`Pointer[NoneType, MutUntrackedOrigin]`) `[imm]`
- `deleter` (`def(Pointer[Self, MutUntrackedOrigin]) capturing thin -> None`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>
### `DLPackMetadata`

```mojo
struct DLPackMetadata[dtype: DType]
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`

Represents a metadata container for DLPack tensor lifetime management.

This structure stores all the metadata needed to manage the lifetime of a
DLPack tensor, including shape, strides, and the underlying data container.
It ensures proper cleanup of allocated resources when the tensor is no
longer needed.

Attributes:
    shape: Pointer to shape array.
    strides: Pointer to strides array.
    ndim: Number of dimensions.
    data_container: Container managing the actual tensor data.

**Parameters:**

- `dtype` (`DType`): Data type of the tensor elements.

#### Fields

- **`shape`** (`Pointer[Int64, MutUntrackedOrigin]`)
- **`strides`** (`Pointer[Int64, MutUntrackedOrigin]`)
- **`ndim`** (`Int`)
- **`data_container`** (`DataContainer[dtype]`)

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
def __init__(out self, shape: Pointer[Int64, MutUntrackedOrigin], strides: Pointer[Int64, MutUntrackedOrigin], ndim: Int, var data_container: DataContainer[dtype])
```

<span class="badge badge-static">static</span>

**Args:**

- `shape` (`Pointer[Int64, MutUntrackedOrigin]`) `[imm]`
- `strides` (`Pointer[Int64, MutUntrackedOrigin]`) `[imm]`
- `ndim` (`Int`) `[imm]`
- `data_container` (`DataContainer[dtype]`) `[var]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 2

```mojo
def __init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

**Args:**

- `copy` (`Self`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__deinit__`

```mojo
def __deinit__(deinit self)
```

**Args:**

- `self` (`Self`) `[deinit]`


</div>
## Functions


<div class="fn-card" markdown="1">

### `to_dlpack`

```mojo
def to_dlpack[dtype: DType](arr: NDArray[dtype]) -> Pointer[DLManagedTensor, MutUntrackedOrigin]
```

Exports a NuMojo NDArray to a DLPack managed tensor for zero-copy sharing.

This function converts a NuMojo NDArray into a DLPack-compatible managed
tensor that can be consumed by other array libraries (NumPy, PyTorch, JAX,
etc.) without copying the underlying data. The function allocates shape and
strides arrays, creates metadata for lifetime management, and returns a
pointer to a DLManagedTensor.

Notes:
- The consumer is responsible for calling the deleter when done.
- Do not modify the original array while the DLPack tensor is in use.
- The returned tensor shares memory with the original array.

**Parameters:**

- `dtype` (`DType`): Data type of the array elements.

**Args:**

- `arr` (`NDArray[dtype]`) `[imm]`: The NDArray to export.

**Returns:**

- `Pointer[DLManagedTensor, MutUntrackedOrigin]`

!!! failure "Raises"
    NumojoError: If enabling views on the data container fails.


</div>

<div class="fn-card" markdown="1">

### `from_dlpack`

```mojo
def from_dlpack[dtype: DType](capsule: PythonObject) -> NDArray[dtype]
```

Imports a tensor from any DLPack-compatible library into a NuMojo NDArray using zero-copy. This function accepts a Python object that implements the DLPack protocol (i.e., has a __dlpack__() method), such as NumPy, PyTorch, JAX, or CuPy tensors. It extracts the underlying memory and metadata through the PyCapsule interface, validates device and data type compatibility, and returns a NuMojo NDArray that shares memory with the original tensor.

Notes:
- The returned NDArray shares memory with the source tensor. Changes to
    one will be reflected in the other.
- Only CPU tensors are currently supported.
- If strides are not provided in the DLPack tensor, C-contiguous strides
    are assumed.

**Parameters:**

- `dtype` (`DType`): The expected data type of the array elements.

**Args:**

- `capsule` (`PythonObject`) `[imm]`: A PythonObject representing a DLPack-compatible tensor. The
    object must implement the __dlpack__() method, which returns a
    PyCapsule containing a pointer to a DLManagedTensor.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the received DLManagedTensor pointer is null.
NumojoError: If the tensor is not on CPU (only CPU tensors are currently
supported).
NumojoError: If the data type does not match the expected dtype parameter.


</div>

<div class="fn-card" markdown="1">

### `from_numpy`

```mojo
def from_numpy[dtype: DType](array: PythonObject) -> NDArray[dtype]
```

Imports a NumPy array into a NuMojo NDArray via zero-copy.

This is a fast path specifically optimized for NumPy that uses the
`__array_interface__` protocol to extract the data pointer directly,
avoiding PyCapsule overhead entirely.
This method is generally faster than using from_dlpack for NumPy arrays.

Notes:
- The imported array shares memory with the source. Modifications to
  either will be visible in both.
- This uses NumPy's `__array_interface__` instead of the DLPack protocol.
- Strides are converted from bytes to elements automatically.

**Parameters:**

- `dtype` (`DType`): Expected data type of the array elements.

**Args:**

- `array` (`PythonObject`) `[imm]`: A NumPy ndarray object.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the array is not on CPU (only CPU tensors are supported).


</div>
