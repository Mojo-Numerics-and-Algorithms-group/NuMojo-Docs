# `numojo.core.accelerator_ndarray`

Device-aware NDArray with accelerator support.

Device-aware NDArray that stores data in AcceleratorDataContainer with
GPU acceleration support.

Exports
-------
- `AcceleratorNDArray`: Device-aware N-dimensional array type.

## Structs

### `AcceleratorNDArray`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct AcceleratorNDArray[dtype: DType = DType.float64, device: Device = Device.CPU]
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Movable`, `Sized`, `Writable`

Device-aware N-dimensional array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Element dtype.
- `device` (`Device`): Target device (`Device.CPU`, `Device.CUDA`, `Device.ROCM`,
    `Device.MPS`).

</div>

#### Fields

- **`ndim`** (`Int`)
- **`shape`** (`NDArrayShape`)
- **`size`** (`Int`)
- **`strides`** (`NDArrayStrides`)
- **`offset`** (`Int`)
- **`flags`** (`Flags`)

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

<div class="overload-divider">Overload 1</div>

```mojo
def __init__(out self)
```

<span class="badge badge-static">static</span>

<div class="prose-label">Args</div>

- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __init__(out self, shape: NDArrayShape, order: String = "C")
```

<span class="badge badge-static">static</span>

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`
- `order` (`String`) `[imm]`
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 3</div>

```mojo
def __init__(out self, shape: List[Int], order: String = "C")
```

<span class="badge badge-static">static</span>

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `order` (`String`) `[imm]`
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 4</div>

```mojo
def __init__(out self, *shape: Int, *, order: String = "C")
```

<span class="badge badge-static">static</span>

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `order` (`String`) `[imm]`
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 5</div>

```mojo
def __init__(out self, shape: NDArrayShape, strides: NDArrayStrides, offset: Int, flags: Flags)
```

<span class="badge badge-static">static</span>

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`
- `strides` (`NDArrayStrides`) `[imm]`
- `offset` (`Int`) `[imm]`
- `flags` (`Flags`) `[imm]`
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 6</div>

```mojo
def __init__(out self, var data: AcceleratorDataContainer[dtype, device], *, is_view: Bool, shape: NDArrayShape, strides: NDArrayStrides, offset: Int, size: Int)
```

<span class="badge badge-static">static</span>

<div class="prose-label">Args</div>

- `data` (`AcceleratorDataContainer[dtype, device]`) `[var]`
- `is_view` (`Bool`) `[imm]`
- `shape` (`NDArrayShape`) `[imm]`
- `strides` (`NDArrayStrides`) `[imm]`
- `offset` (`Int`) `[imm]`
- `size` (`Int`) `[imm]`
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 7</div>

```mojo
def __init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

<div class="prose-label">Args</div>

- `copy` (`Self`) `[imm]`
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 8</div>

```mojo
def __init__(out self, *, deinit move: Self)
```

<span class="badge badge-static">static</span>

<div class="prose-label">Args</div>

- `move` (`Self`) `[deinit]`
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__getitem__`

<div class="overload-divider">Overload 1</div>

```mojo
def __getitem__(self) -> Scalar[dtype]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __getitem__(self, index: Item) -> Scalar[dtype]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `index` (`Item`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 3</div>

```mojo
def __getitem__(self, idx: Int) -> Self
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 4</div>

```mojo
def __getitem__(self, var *slices: Slice) -> Self
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `*slices` (`Slice`) `[var]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__setitem__`

```mojo
def __setitem__(mut self, index: Item, value: Scalar[dtype])
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `index` (`Item`) `[imm]`
- `value` (`Scalar[dtype]`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__neg__`

```mojo
def __neg__(self) -> Self
```

Elementwise negation. Requires a densely contiguous array (no broadcasting or strided views yet).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the array is not contiguous.


</div>

<div class="fn-card" markdown="1">

#### `__add__`

```mojo
def __add__(self, other: Self) -> Self
```

Elementwise addition. See `_binary_op` for constraints.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__sub__`

```mojo
def __sub__(self, other: Self) -> Self
```

Elementwise subtraction. See `_binary_op` for constraints.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__mul__`

```mojo
def __mul__(self, other: Self) -> Self
```

Elementwise multiplication. See `_binary_op` for constraints.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__truediv__`

```mojo
def __truediv__(self, other: Self) -> Self
```

Elementwise division. See `_binary_op` for constraints.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `view`

```mojo
def view(self) -> Self
```

Create a metadata-only view sharing the same storage.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__str__`

```mojo
def __str__(self) -> String
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>

<div class="fn-card" markdown="1">

#### `__repr__`

```mojo
def __repr__(self) -> String
```

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

<div class="prose-label">Parameters</div>

- `W` (`Writer`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

#### `__len__`

```mojo
def __len__(self) -> Int
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `is_cpu`

```mojo
def is_cpu(self) -> Bool
```

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

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `unsafe_ptr`

```mojo
def unsafe_ptr(ref self) -> Pointer[Scalar[dtype], MutAnyOrigin] where (device.type == String("cpu"))
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`

<div class="prose-label">Returns</div>

- `Pointer[Scalar[dtype], MutAnyOrigin]`


</div>

<div class="fn-card" markdown="1">

#### `unsafe_device_ptr`

```mojo
def unsafe_device_ptr(ref self) -> Pointer[Scalar[dtype], MutAnyOrigin] where (device.type == String("gpu"))
```

Return the raw device pointer to the buffer's data.

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`

<div class="prose-label">Returns</div>

- `Pointer[Scalar[dtype], MutAnyOrigin]`


</div>

<div class="fn-card" markdown="1">

#### `device_context`

```mojo
def device_context(self) -> DeviceContext where (device.type == String("gpu"))
```

Return the `DeviceContext` backing this array's GPU storage.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `DeviceContext`


</div>

<div class="fn-card" markdown="1">

#### `num_elements`

```mojo
def num_elements(self) -> Int
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `normalize`

```mojo
def normalize(self, index: Int, dim: Int) -> Int
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[imm]`
- `dim` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `item`

<div class="overload-divider">Overload 1</div>

```mojo
def item(self, flat_index: Int) -> Scalar[dtype]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `flat_index` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def item(self, *indices: Int) -> Scalar[dtype]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `*indices` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `itemset`

```mojo
def itemset(mut self, flat_index: Int, value: Scalar[dtype])
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `flat_index` (`Int`) `[imm]`
- `value` (`Scalar[dtype]`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `deep_copy`

```mojo
def deep_copy(self) -> Self
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `to_host`

```mojo
def to_host(self) -> AcceleratorNDArray[dtype]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `to_device`

```mojo
def to_device[target: Device](self) -> AcceleratorNDArray[dtype, target]
```

<div class="prose-label">Parameters</div>

- `target` (`Device`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, target]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `to`

```mojo
def to[target: Device](self) -> AcceleratorNDArray[dtype, target]
```

<div class="prose-label">Parameters</div>

- `target` (`Device`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, target]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `sum`

```mojo
def sum(self) -> Scalar[dtype]
```

Sum of all elements in the array. Requires a densely contiguous array (no broadcasting or strided views yet).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If the array is not contiguous.


</div>
## Functions


<div class="fn-card" markdown="1">

### `empty`

<div class="overload-divider">Overload 1</div>

```mojo
def empty[dtype: DType = DType.float64, device: Device = Device.CPU](shape: NDArrayShape, order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an uninitialized accelerator array on `device`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def empty[dtype: DType = DType.float64, device: Device = Device.CPU](shape: List[Int], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an uninitialized accelerator array on `device`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

<div class="overload-divider">Overload 3</div>

```mojo
def empty[dtype: DType = DType.float64, device: Device = Device.CPU](*shape: Int, *, order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an uninitialized accelerator array on `device`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `full`

<div class="overload-divider">Overload 1</div>

```mojo
def full[dtype: DType = DType.float64, device: Device = Device.CPU](shape: NDArrayShape, fill_value: Scalar[dtype], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with `fill_value`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`
- `fill_value` (`Scalar[dtype]`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def full[dtype: DType = DType.float64, device: Device = Device.CPU](shape: List[Int], fill_value: Scalar[dtype], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with `fill_value`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `fill_value` (`Scalar[dtype]`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `zeros`

<div class="overload-divider">Overload 1</div>

```mojo
def zeros[dtype: DType = DType.float64, device: Device = Device.CPU](shape: NDArrayShape, order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with zeros.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def zeros[dtype: DType = DType.float64, device: Device = Device.CPU](shape: List[Int], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with zeros.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

<div class="overload-divider">Overload 3</div>

```mojo
def zeros[dtype: DType = DType.float64, device: Device = Device.CPU](*shape: Int, *, order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with zeros.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `ones`

<div class="overload-divider">Overload 1</div>

```mojo
def ones[dtype: DType = DType.float64, device: Device = Device.CPU](shape: NDArrayShape, order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with ones.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def ones[dtype: DType = DType.float64, device: Device = Device.CPU](shape: List[Int], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with ones.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

<div class="overload-divider">Overload 3</div>

```mojo
def ones[dtype: DType = DType.float64, device: Device = Device.CPU](*shape: Int, *, order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with ones.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `empty_like`

```mojo
def empty_like[dtype: DType, device: Device](a: AcceleratorNDArray[dtype, device], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an uninitialized accelerator array with `a`'s shape and device.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `a` (`AcceleratorNDArray[dtype, device]`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `zeros_like`

```mojo
def zeros_like[dtype: DType, device: Device](a: AcceleratorNDArray[dtype, device], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create a zeros accelerator array with `a`'s shape and device.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `a` (`AcceleratorNDArray[dtype, device]`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `ones_like`

```mojo
def ones_like[dtype: DType, device: Device](a: AcceleratorNDArray[dtype, device], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create a ones accelerator array with `a`'s shape and device.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `a` (`AcceleratorNDArray[dtype, device]`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `full_like`

```mojo
def full_like[dtype: DType, device: Device](a: AcceleratorNDArray[dtype, device], fill_value: Scalar[dtype], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create a filled accelerator array with `a`'s shape and device.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `a` (`AcceleratorNDArray[dtype, device]`) `[imm]`
- `fill_value` (`Scalar[dtype]`) `[imm]`
- `order` (`String`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `arange`

<div class="overload-divider">Overload 1</div>

```mojo
def arange[dtype: DType = DType.float64, device: Device = Device.CPU](start: Scalar[dtype], stop: Scalar[dtype], step: Scalar[dtype] = 1) -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array with evenly spaced values.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `start` (`Scalar[dtype]`) `[imm]`
- `stop` (`Scalar[dtype]`) `[imm]`
- `step` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def arange[dtype: DType = DType.float64, device: Device = Device.CPU](stop: Scalar[dtype]) -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array with values from zero to `stop`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `device` (`Device`)

<div class="prose-label">Args</div>

- `stop` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>
