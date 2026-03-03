# `numojo.core.accelerator.device`

Device (numojo.core.accelerator.device)

This module defines the `Device` struct, which represents an execution device for array and matrix operations.
It supports CPU and GPU devices, with GPU backends for NVIDIA CUDA, AMD ROCm, and Apple Metal.

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

### `Device`

```mojo
struct Device
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Equatable`, `ImplicitlyCopyable`, `ImplicitlyDestructible`, `Movable`, `Representable`, `Stringable`, `Writable`

Represents an execution device for array and matrix operations.

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

- **`type`** (`String`): Device type: "cpu" or "gpu".
- **`name`** (`String`): Backend identifier: "" for CPU, "cuda" | "rocm" | "mps" for GPU.
- **`id`** (`Int`): Zero-based device index on the backend.

#### Aliases

##### `CPU`

```mojo
comptime CPU
```

**Value:** `Device._unchecked_init("cpu", "", 0)`

CPU device.

##### `CUDA`

```mojo
comptime CUDA
```

**Value:** `Device._unchecked_init("gpu", "cuda", 0)`

NVIDIA CUDA GPU device.

##### `ROCM`

```mojo
comptime ROCM
```

**Value:** `Device._unchecked_init("gpu", "rocm", 0)`

AMD ROCm GPU device.

##### `MPS`

```mojo
comptime MPS
```

**Value:** `Device._unchecked_init("gpu", "mps", 0)`

Apple Metal GPU device.

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
__init__(out self)
```

<span class="badge badge-static">static</span>

Initialize a default CPU device.

**Args:**

- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 2

```mojo
__init__(out self, text: String)
```

<span class="badge badge-static">static</span>

Initialize a device by parsing a torch-style device string.

Supported formats: "cpu", "cuda", "cuda:0", "rocm", "rocm:1",
"mps", "mps:0", "gpu".

**Args:**

- `text` (`String`): A device string to parse.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error on invalid device string format.

###### Overload 3

```mojo
__init__(out self, type: String, name: String, id: Int)
```

<span class="badge badge-static">static</span>

Initialize a device with explicit type, name, and index.

Validates the arguments and falls back to CPU if the requested
GPU backend is not available on the current system.

**Args:**

- `type` (`String`): Device type, must be "cpu" or "gpu".
- `name` (`String`): Backend name ("" for CPU; "cuda", "rocm", or "mps" for GPU).
- `id` (`Int`): Zero-based device index (must be 0 for CPU, >= 0 for GPU).
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
__eq__(self, other: Self) -> Bool
```

Check equality with another device.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The device to compare against.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
__ne__(self, other: Self) -> Bool
```

Check inequality with another device.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The device to compare against.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
__str__(self) -> String
```

Return a human-readable string representation.

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `__repr__`

```mojo
__repr__(self) -> String
```

Return the canonical string representation.

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

Write the string representation to a writer.

**Parameters:**

- `W` (`Writer`): The writer type.

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`: The writer to write to.


</div>

<div class="fn-card" markdown="1">

##### `is_cpu`

```mojo
is_cpu(self) -> Bool
```

Check if this is a CPU device.

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

Check if this is a GPU device.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_available`

```mojo
is_available(self) -> Bool
```

Check if this device is available on the current system.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `default_device`

```mojo
default_device() -> Self
```

<span class="badge badge-static">static</span>

Return the best available device: GPU if present, otherwise CPU.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `available_gpu`

```mojo
available_gpu() -> String
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
available_devices() -> String
```

<span class="badge badge-static">static</span>

List all available devices on the current system.

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `parse_device_string`

```mojo
parse_device_string(text: String) -> Self
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

- `text` (`String`): The device string to parse.

**Returns:**

- `Self`

!!! failure "Raises"
    Error when "gpu" is specified but no GPU backend is available.


</div>
## Functions


<div class="fn-card" markdown="1">

### `is_accelerator_available`

```mojo
is_accelerator_available[device: Device]() -> Bool
```

Check at compile time whether the given device's GPU accelerator exists.

**Parameters:**

- `device` (`Device`): The device to check.

**Returns:**

- `Bool`


</div>
