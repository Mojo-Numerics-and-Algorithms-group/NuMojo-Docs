# `numojo.core.accelerator_ndarray`

Device-aware NDArray with accelerator support.

Device-aware NDArray that stores data in AcceleratorDataContainer with
GPU acceleration support.

Exports
-------
- `AcceleratorNDArray`: Device-aware N-dimensional array type.

## Structs

### `AcceleratorNDArray`

```mojo
struct AcceleratorNDArray[dtype: DType = DType.float64, device: Device = Device.CPU]
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Movable`, `Sized`, `Writable`

Device-aware N-dimensional array.

**Parameters:**

- `dtype` (`DType`): Element dtype.
- `device` (`Device`): Target device (`Device.CPU`, `Device.CUDA`, `Device.ROCM`,
    `Device.MPS`).

#### Fields

- **`ndim`** (`Int`)
- **`shape`** (`NDArrayShape`)
- **`size`** (`Int`)
- **`strides`** (`NDArrayStrides`)
- **`offset`** (`Int`)
- **`flags`** (`Flags`)

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
def __init__(out self, shape: NDArrayShape, order: String = "C")
```

<span class="badge badge-static">static</span>

**Args:**

- `shape` (`NDArrayShape`) `[imm]`
- `order` (`String`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 3

```mojo
def __init__(out self, shape: List[Int], order: String = "C")
```

<span class="badge badge-static">static</span>

**Args:**

- `shape` (`List[Int]`) `[imm]`
- `order` (`String`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 4

```mojo
def __init__(out self, *shape: Int, *, order: String = "C")
```

<span class="badge badge-static">static</span>

**Args:**

- `*shape` (`Int`) `[imm]`
- `order` (`String`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 5

```mojo
def __init__(out self, shape: NDArrayShape, strides: NDArrayStrides, offset: Int, flags: Flags)
```

<span class="badge badge-static">static</span>

**Args:**

- `shape` (`NDArrayShape`) `[imm]`
- `strides` (`NDArrayStrides`) `[imm]`
- `offset` (`Int`) `[imm]`
- `flags` (`Flags`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 6

```mojo
def __init__(out self, var data: AcceleratorDataContainer[dtype, device], *, is_view: Bool, shape: NDArrayShape, strides: NDArrayStrides, offset: Int, size: Int)
```

<span class="badge badge-static">static</span>

**Args:**

- `data` (`AcceleratorDataContainer[dtype, device]`) `[var]`
- `is_view` (`Bool`) `[imm]`
- `shape` (`NDArrayShape`) `[imm]`
- `strides` (`NDArrayStrides`) `[imm]`
- `offset` (`Int`) `[imm]`
- `size` (`Int`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 7

```mojo
def __init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

**Args:**

- `copy` (`Self`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 8

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

##### `__getitem__`

###### Overload 1

```mojo
def __getitem__(self) -> Scalar[dtype]
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"

###### Overload 2

```mojo
def __getitem__(self, index: Item) -> Scalar[dtype]
```

**Args:**

- `self` (`Self`) `[imm]`
- `index` (`Item`) `[imm]`

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"

###### Overload 3

```mojo
def __getitem__(self, idx: Int) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 4

```mojo
def __getitem__(self, var *slices: Slice) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`
- `*slices` (`Slice`) `[var]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__setitem__`

```mojo
def __setitem__(mut self, index: Item, value: Scalar[dtype])
```

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`Item`) `[imm]`
- `value` (`Scalar[dtype]`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__neg__`

```mojo
def __neg__(self) -> Self
```

Elementwise negation. Requires a densely contiguous array (no broadcasting or strided views yet).

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the array is not contiguous.


</div>

<div class="fn-card" markdown="1">

##### `__add__`

```mojo
def __add__(self, other: Self) -> Self
```

Elementwise addition. See `_binary_op` for constraints.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__sub__`

```mojo
def __sub__(self, other: Self) -> Self
```

Elementwise subtraction. See `_binary_op` for constraints.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__mul__`

```mojo
def __mul__(self, other: Self) -> Self
```

Elementwise multiplication. See `_binary_op` for constraints.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__truediv__`

```mojo
def __truediv__(self, other: Self) -> Self
```

Elementwise division. See `_binary_op` for constraints.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `view`

```mojo
def view(self) -> Self
```

Create a metadata-only view sharing the same storage.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


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

<div class="fn-card" markdown="1">

##### `__len__`

```mojo
def __len__(self) -> Int
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`


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

##### `unsafe_ptr`

```mojo
def unsafe_ptr(ref self) -> Pointer[Scalar[dtype], MutAnyOrigin] where (device.type == String("cpu"))
```

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `Pointer[Scalar[dtype], MutAnyOrigin]`


</div>

<div class="fn-card" markdown="1">

##### `unsafe_device_ptr`

```mojo
def unsafe_device_ptr(ref self) -> Pointer[Scalar[dtype], MutAnyOrigin] where (device.type == String("gpu"))
```

Return the raw device pointer to the buffer's data.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `Pointer[Scalar[dtype], MutAnyOrigin]`


</div>

<div class="fn-card" markdown="1">

##### `device_context`

```mojo
def device_context(self) -> DeviceContext where (device.type == String("gpu"))
```

Return the `DeviceContext` backing this array's GPU storage.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `DeviceContext`


</div>

<div class="fn-card" markdown="1">

##### `num_elements`

```mojo
def num_elements(self) -> Int
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `normalize`

```mojo
def normalize(self, index: Int, dim: Int) -> Int
```

**Args:**

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[imm]`
- `dim` (`Int`) `[imm]`

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `item`

###### Overload 1

```mojo
def item(self, flat_index: Int) -> Scalar[dtype]
```

**Args:**

- `self` (`Self`) `[imm]`
- `flat_index` (`Int`) `[imm]`

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"

###### Overload 2

```mojo
def item(self, *indices: Int) -> Scalar[dtype]
```

**Args:**

- `self` (`Self`) `[imm]`
- `*indices` (`Int`) `[imm]`

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `itemset`

```mojo
def itemset(mut self, flat_index: Int, value: Scalar[dtype])
```

**Args:**

- `self` (`Self`) `[mut]`
- `flat_index` (`Int`) `[imm]`
- `value` (`Scalar[dtype]`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `deep_copy`

```mojo
def deep_copy(self) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `to_host`

```mojo
def to_host(self) -> AcceleratorNDArray[dtype]
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `to_device`

```mojo
def to_device[target: Device](self) -> AcceleratorNDArray[dtype, target]
```

**Parameters:**

- `target` (`Device`)

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, target]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `to`

```mojo
def to[target: Device](self) -> AcceleratorNDArray[dtype, target]
```

**Parameters:**

- `target` (`Device`)

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, target]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `sum`

```mojo
def sum(self) -> Scalar[dtype]
```

Sum of all elements in the array. Requires a densely contiguous array (no broadcasting or strided views yet).

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If the array is not contiguous.


</div>
## Functions


<div class="fn-card" markdown="1">

### `empty`

#### Overload 1

```mojo
def empty[dtype: DType = DType.float64, device: Device = Device.CPU](shape: NDArrayShape, order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an uninitialized accelerator array on `device`.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `shape` (`NDArrayShape`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

#### Overload 2

```mojo
def empty[dtype: DType = DType.float64, device: Device = Device.CPU](shape: List[Int], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an uninitialized accelerator array on `device`.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `shape` (`List[Int]`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

#### Overload 3

```mojo
def empty[dtype: DType = DType.float64, device: Device = Device.CPU](*shape: Int, *, order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an uninitialized accelerator array on `device`.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `*shape` (`Int`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `full`

#### Overload 1

```mojo
def full[dtype: DType = DType.float64, device: Device = Device.CPU](shape: NDArrayShape, fill_value: Scalar[dtype], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with `fill_value`.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `shape` (`NDArrayShape`) `[imm]`
- `fill_value` (`Scalar[dtype]`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

#### Overload 2

```mojo
def full[dtype: DType = DType.float64, device: Device = Device.CPU](shape: List[Int], fill_value: Scalar[dtype], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with `fill_value`.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `shape` (`List[Int]`) `[imm]`
- `fill_value` (`Scalar[dtype]`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `zeros`

#### Overload 1

```mojo
def zeros[dtype: DType = DType.float64, device: Device = Device.CPU](shape: NDArrayShape, order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with zeros.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `shape` (`NDArrayShape`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

#### Overload 2

```mojo
def zeros[dtype: DType = DType.float64, device: Device = Device.CPU](shape: List[Int], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with zeros.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `shape` (`List[Int]`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

#### Overload 3

```mojo
def zeros[dtype: DType = DType.float64, device: Device = Device.CPU](*shape: Int, *, order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with zeros.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `*shape` (`Int`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `ones`

#### Overload 1

```mojo
def ones[dtype: DType = DType.float64, device: Device = Device.CPU](shape: NDArrayShape, order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with ones.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `shape` (`NDArrayShape`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

#### Overload 2

```mojo
def ones[dtype: DType = DType.float64, device: Device = Device.CPU](shape: List[Int], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with ones.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `shape` (`List[Int]`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

#### Overload 3

```mojo
def ones[dtype: DType = DType.float64, device: Device = Device.CPU](*shape: Int, *, order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array filled with ones.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `*shape` (`Int`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `empty_like`

```mojo
def empty_like[dtype: DType, device: Device](a: AcceleratorNDArray[dtype, device], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create an uninitialized accelerator array with `a`'s shape and device.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `a` (`AcceleratorNDArray[dtype, device]`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `zeros_like`

```mojo
def zeros_like[dtype: DType, device: Device](a: AcceleratorNDArray[dtype, device], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create a zeros accelerator array with `a`'s shape and device.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `a` (`AcceleratorNDArray[dtype, device]`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `ones_like`

```mojo
def ones_like[dtype: DType, device: Device](a: AcceleratorNDArray[dtype, device], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create a ones accelerator array with `a`'s shape and device.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `a` (`AcceleratorNDArray[dtype, device]`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `full_like`

```mojo
def full_like[dtype: DType, device: Device](a: AcceleratorNDArray[dtype, device], fill_value: Scalar[dtype], order: String = "C") -> AcceleratorNDArray[dtype, device]
```

Create a filled accelerator array with `a`'s shape and device.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `a` (`AcceleratorNDArray[dtype, device]`) `[imm]`
- `fill_value` (`Scalar[dtype]`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `arange`

#### Overload 1

```mojo
def arange[dtype: DType = DType.float64, device: Device = Device.CPU](start: Scalar[dtype], stop: Scalar[dtype], step: Scalar[dtype] = 1) -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array with evenly spaced values.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `start` (`Scalar[dtype]`) `[imm]`
- `stop` (`Scalar[dtype]`) `[imm]`
- `step` (`Scalar[dtype]`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"

#### Overload 2

```mojo
def arange[dtype: DType = DType.float64, device: Device = Device.CPU](stop: Scalar[dtype]) -> AcceleratorNDArray[dtype, device]
```

Create an accelerator array with values from zero to `stop`.

**Parameters:**

- `dtype` (`DType`)
- `device` (`Device`)

**Args:**

- `stop` (`Scalar[dtype]`) `[imm]`

**Returns:**

- `AcceleratorNDArray[dtype, device]`

!!! failure "Raises"


</div>
