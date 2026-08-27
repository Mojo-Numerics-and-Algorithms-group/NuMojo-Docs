# `numojo.core.accelerator.device`

Execution device for array and matrix operations.

Defines the `Device` struct, which represents an execution device for array
and matrix operations. Supports CPU and GPU devices, with GPU backends for
NVIDIA CUDA, AMD ROCm, and Apple Metal.

Exports
-------
- `Device`: Execution device.

## Aliases

### `cpu`

```mojo
comptime cpu
```

**Value:** `Device.CPU`

### `cuda`

```mojo
comptime cuda
```

**Value:** `Device.CUDA`

### `rocm`

```mojo
comptime rocm
```

**Value:** `Device.ROCM`

### `mps`

```mojo
comptime mps
```

**Value:** `Device.MPS`

## Structs

### `DeviceSpec`

```mojo
struct DeviceSpec
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Equatable`, `ImplicitlyCopyable`, `Movable`, `Writable`

Device identity.

`DeviceSpec` only describes where data should live: CPU or a GPU backend plus device index.

#### Fields

- **`backend`** (`String`): Canonical backend: "cpu", "cuda", "rocm", or "mps".
- **`id`** (`Int`): Zero-based device index. CPU always uses id 0.

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
def __init__(out self)
```

<span class="badge badge-static">static</span>

**Args:**

- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 2

```mojo
def __init__(out self, backend: String, id: Int)
```

<span class="badge badge-static">static</span>

**Args:**

- `backend` (`String`) `[imm]`
- `id` (`Int`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
def __eq__(self, other: Self) -> Bool
```

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

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_cpu`

```mojo
def is_cpu(self) -> Bool
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_gpu`

```mojo
def is_gpu(self) -> Bool
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `backend_id`

```mojo
def backend_id(self) -> Int
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `name`

```mojo
def name(self) -> String
```

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

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `__repr__`

```mojo
def __repr__(self) -> String
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
### `DeviceHandle`

```mojo
struct DeviceHandle[device: Device]
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Movable`, `Writable`

GPU handle for a compile-time `Device`.

This handle owns the runtime `DeviceContext` used by storage allocation and kernels.

**Parameters:**

- `device` (`Device`)

#### Fields

- **`context`** (`DeviceContext`)

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
def __init__(out self)
```

<span class="badge badge-static">static</span>

**Args:**

- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def __init__(out self, var context: DeviceContext)
```

<span class="badge badge-static">static</span>

**Args:**

- `context` (`DeviceContext`) `[var]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 3

```mojo
def __init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

**Args:**

- `copy` (`Self`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 4

```mojo
def __init__(out self, *, deinit move: Self)
```

<span class="badge badge-static">static</span>

**Args:**

- `move` (`Self`) `[deinit]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


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

##### `is_cpu`

```mojo
def is_cpu(self) -> Bool
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_gpu`

```mojo
def is_gpu(self) -> Bool
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `device_context`

```mojo
def device_context(self) -> DeviceContext
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `DeviceContext`


</div>

<div class="fn-card" markdown="1">

##### `synchronize`

```mojo
def synchronize(self)
```

**Args:**

- `self` (`Self`) `[imm]`

!!! failure "Raises"


</div>
### `Device`

```mojo
struct Device
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Equatable`, `ImplicitlyCopyable`, `Movable`, `Writable`

Represents an execution device for array operations.

A `Device` identifies where computation should run, analogous to
`torch.device` in PyTorch. Each device has a type ("cpu" or "gpu"),
an optional backend name ("cuda", "rocm", or "mps" for GPUs), and
a zero-based device index.

Use the predefined comptime constants for common devices:
    - `Device.CPU`  — CPU execution.
    - `Device.CUDA` — NVIDIA CUDA GPU.
    - `Device.ROCM` — AMD ROCm GPU.
    - `Device.MPS`  — Apple Metal GPU.

Devices can also be constructed from torch-style strings:
    ```
    var dev = Device("cuda:0")
    var cpu = Device("cpu")
    ```

#### Fields

- **`spec`** (`DeviceSpec`): Device identity.
- **`type`** (`String`): Device type: "cpu" or "gpu".
- **`name`** (`String`): Backend identifier: "" for CPU, "cuda" | "rocm" | "mps" for GPU.
- **`id`** (`Int`): Zero-based device index on the backend.

#### Aliases

##### `CPU`

```mojo
comptime CPU
```

**Value:** `Device._unchecked_init(String("cpu"), String(""), Int(0))`

CPU device.

##### `CUDA`

```mojo
comptime CUDA
```

**Value:** `Device._unchecked_init(String("gpu"), String("cuda"), Int(0))`

NVIDIA CUDA GPU device.

##### `ROCM`

```mojo
comptime ROCM
```

**Value:** `Device._unchecked_init(String("gpu"), String("rocm"), Int(0))`

AMD ROCm GPU device.

##### `MPS`

```mojo
comptime MPS
```

**Value:** `Device._unchecked_init(String("gpu"), String("mps"), Int(0))`

Apple Metal GPU device.

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
def __init__(out self)
```

<span class="badge badge-static">static</span>

Initialize a default CPU device.

**Args:**

- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 2

```mojo
def __init__(out self, text: String)
```

<span class="badge badge-static">static</span>

Initialize a device by parsing a torch-style device string.

Supported formats: "cpu", "cuda", "cuda:0", "rocm", "rocm:1",
"mps", "mps:0", "gpu".

**Args:**

- `text` (`String`) `[imm]`: A device string to parse.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error on invalid device string format.

###### Overload 3

```mojo
def __init__(out self, type: String, name: String, id: Int)
```

<span class="badge badge-static">static</span>

Initialize a device with explicit type, name, and index.

Validates the arguments and raises on invalid or unavailable devices.

**Args:**

- `type` (`String`) `[imm]`: Device type, must be "cpu" or "gpu".
- `name` (`String`) `[imm]`: Backend name ("" for CPU; "cuda", "rocm", or "mps" for GPU).
- `id` (`Int`) `[imm]`: Zero-based device index (must be 0 for CPU, >= 0 for GPU).
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
def __eq__(self, other: Self) -> Bool
```

Check equality with another device.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The device to compare against.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
def __ne__(self, other: Self) -> Bool
```

Check inequality with another device.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The device to compare against.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `from_spec`

```mojo
def from_spec(spec: DeviceSpec) -> Self
```

<span class="badge badge-static">static</span>

Validate and construct a `Device` from a canonical spec.

**Args:**

- `spec` (`DeviceSpec`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
def __str__(self) -> String
```

Return a human-readable string representation.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `__repr__`

```mojo
def __repr__(self) -> String
```

Return the canonical string representation.

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
- `writer` (`W`) `[mut]`: The writer to write to.


</div>

<div class="fn-card" markdown="1">

##### `write_to`

```mojo
def write_to[W: Writer](self, mut writer: W)
```

Write the string representation to a writer.

**Parameters:**

- `W` (`Writer`): The writer type.

**Args:**

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`: The writer to write to.


</div>

<div class="fn-card" markdown="1">

##### `is_cpu`

```mojo
def is_cpu(self) -> Bool
```

Check if this is a CPU device.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_gpu`

```mojo
def is_gpu(self) -> Bool
```

Check if this is a GPU device.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `backend_id`

```mojo
def backend_id(self) -> Int
```

Return a backend identifier.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `device_name`

```mojo
def device_name(self) -> String
```

Return device string.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `same_backend`

```mojo
def same_backend(self, other: Self) -> Bool
```

Check if two devices use the same execution backend.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_default_index`

```mojo
def is_default_index(self) -> Bool
```

Check if this device uses index 0.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_available`

```mojo
def is_available(self) -> Bool
```

Check if this device is available on the current system.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `default_device`

```mojo
def default_device() -> Self
```

<span class="badge badge-static">static</span>

Return the best available device: GPU if present, otherwise CPU.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `available_gpu`

```mojo
def available_gpu() -> String
```

<span class="badge badge-static">static</span>

Return the name of the best available GPU backend.

Checks in order: CUDA → ROCm → MPS.

**Returns:**

- `String`

!!! failure "Raises"
    NumojoError if no GPU accelerator is detected.


</div>

<div class="fn-card" markdown="1">

##### `available_devices`

```mojo
def available_devices() -> String
```

<span class="badge badge-static">static</span>

List all available devices on the current system.

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `parse_device_string`

```mojo
def parse_device_string(text: String) -> Self
```

<span class="badge badge-static">static</span>

Parse a torch-style device string into a `Device`.

Supported formats:
    - "cpu"
    - "cuda", "cuda:0", "cuda:1", ...
    - "rocm", "rocm:0", "rocm:1", ...
    - "mps", "mps:0", "mps:1", ...
    - "gpu" (resolves to best available GPU backend)

**Args:**

- `text` (`String`) `[imm]`: The device string to parse.

**Returns:**

- `Self`

!!! failure "Raises"
    Error for invalid strings, unavailable GPU backends, or invalid
device indices.


</div>
## Functions


<div class="fn-card" markdown="1">

### `is_accelerator_available`

```mojo
def is_accelerator_available[device: Device]() -> Bool
```

Check at compile time whether the given device's GPU accelerator exists.

**Parameters:**

- `device` (`Device`): The device to check.

**Returns:**

- `Bool`


</div>
