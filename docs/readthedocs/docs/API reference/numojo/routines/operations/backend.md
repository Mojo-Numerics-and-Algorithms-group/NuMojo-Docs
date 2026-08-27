# `numojo.routines.operations.backend`

Vectorized backend for math operations.

Defines backend structures and SIMD primitives for math operations.

Exports
-------
- `HostExecutor`: CPU backend executor.

## Aliases

### `MIN_SIMD_WIDTHS_PER_TASK`

```mojo
comptime MIN_SIMD_WIDTHS_PER_TASK
```

**Value:** `8`

Minimum number of SIMD-widths of work each parallel task should get before splitting across cores is worth the thread-dispatch overhead. This is a heuristic that can be tuned.

## Structs

### `HostExecutor`

```mojo
struct HostExecutor
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Deinitable`, `Movable`

Vectorized CPU Backend.

This struct provides static methods to apply SIMD-compatible
unary and binary functions to NDArrays, Scalars.

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
def __init__(out self)
```

<span class="badge badge-static">static</span>

**Args:**

- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `apply_unary`

###### Overload 1

```mojo
def apply_unary[dtype: DType, simd_width: Int, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](scalar: SIMD[dtype, simd_width]) -> SIMD[dtype, simd_width]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible unary function to a SIMD value.

**Parameters:**

- `dtype` (`DType`): The element type.
- `simd_width` (`Int`): The SIMD width of the input and output.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible function to apply.

**Args:**

- `scalar` (`SIMD[dtype, simd_width]`) `[imm]`: The input SIMD value.

**Returns:**

- `SIMD[dtype, simd_width]`

###### Overload 2

```mojo
def apply_unary[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](array: NDArray[dtype]) -> NDArray[dtype]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible unary function to an NDArray.

**Parameters:**

- `dtype` (`DType`): The element type of the NDArray.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible function to apply.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: The input NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `apply_binary`

###### Overload 1

```mojo
def apply_binary[dtype: DType, simd_width: Int, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](simd1: SIMD[dtype, simd_width], simd2: SIMD[dtype, simd_width]) -> SIMD[dtype, simd_width]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary function to two SIMD values.

**Parameters:**

- `dtype` (`DType`): The element type.
- `simd_width` (`Int`): The SIMD width of the input and output.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible binary function to apply.

**Args:**

- `simd1` (`SIMD[dtype, simd_width]`) `[imm]`: The first input SIMD value.
- `simd2` (`SIMD[dtype, simd_width]`) `[imm]`: The second input SIMD value.

**Returns:**

- `SIMD[dtype, simd_width]`

###### Overload 2

```mojo
def apply_binary[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary function to two NDArrays.

**Parameters:**

- `dtype` (`DType`): The element type of the NDArrays.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible binary function to apply.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: The first input NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: The second input NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

###### Overload 3

```mojo
def apply_binary[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary function to an NDArray and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type of the NDArray.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible binary function to apply.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: The input NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: The input scalar value.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

###### Overload 4

```mojo
def apply_binary[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary function to a scalar and an NDArray.

**Parameters:**

- `dtype` (`DType`): The element type of the NDArray.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible binary function to apply.

**Args:**

- `scalar` (`Scalar[dtype]`) `[imm]`: The input scalar value.
- `array` (`NDArray[dtype]`) `[imm]`: The input NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

###### Overload 5

```mojo
def apply_binary[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], Int) capturing thin -> SIMD[type, simd_w]](array: NDArray[dtype], intval: Int) -> NDArray[dtype]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary function to an NDArray and an Int scalar.

**Parameters:**

- `dtype` (`DType`): The element type of the NDArray.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], Int) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible binary function to apply.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: The input NDArray.
- `intval` (`Int`) `[imm]`: The input integer value.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `apply_unary_predicate`

###### Overload 1

```mojo
def apply_unary_predicate[dtype: DType, simd_width: Int, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]](simd: SIMD[dtype, simd_width]) -> SIMD[DType.bool, simd_width]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible unary predicate to a SIMD value.

**Parameters:**

- `dtype` (`DType`): The element type.
- `simd_width` (`Int`): The SIMD width of the input and output.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]`): The SIMD-compatible unary predicate function to apply.

**Args:**

- `simd` (`SIMD[dtype, simd_width]`) `[imm]`: The input SIMD value.

**Returns:**

- `SIMD[DType.bool, simd_width]`

###### Overload 2

```mojo
def apply_unary_predicate[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]](array: NDArray[dtype]) -> NDArray[DType.bool]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible unary predicate to an NDArray, returning a boolean NDArray.

**Parameters:**

- `dtype` (`DType`): The element type of the input NDArray.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]`): The SIMD-compatible unary predicate function to apply.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: The input NDArray.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `apply_binary_predicate`

###### Overload 1

```mojo
def apply_binary_predicate[dtype: DType, simd_width: Int, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]](simd1: SIMD[dtype, simd_width], simd2: SIMD[dtype, simd_width]) -> SIMD[DType.bool, simd_width]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary predicate to two SIMD values.

**Parameters:**

- `dtype` (`DType`): The element type.
- `simd_width` (`Int`): The SIMD width of the input and output (should be 1 for SIMD).
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]`): The SIMD-compatible binary predicate function to apply.

**Args:**

- `simd1` (`SIMD[dtype, simd_width]`) `[imm]`: The first input SIMD value.
- `simd2` (`SIMD[dtype, simd_width]`) `[imm]`: The second input SIMD value.

**Returns:**

- `SIMD[DType.bool, simd_width]`

###### Overload 2

```mojo
def apply_binary_predicate[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary predicate to two NDArrays, returning a boolean NDArray.

**Parameters:**

- `dtype` (`DType`): The element type of the input NDArrays.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]`): The SIMD-compatible binary predicate function to apply.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: The first input NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: The second input NDArray.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"

###### Overload 3

```mojo
def apply_binary_predicate[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]](array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary predicate to an NDArray and a scalar, returning a boolean NDArray.

**Parameters:**

- `dtype` (`DType`): The element type of the input NDArray.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]`): The SIMD-compatible binary predicate function to apply.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: The input NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: The input scalar value.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `apply_ternary`

###### Overload 1

```mojo
def apply_ternary[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[dtype]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible ternary function to three NDArrays.

**Parameters:**

- `dtype` (`DType`): The element type of the NDArrays.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible ternary function to apply.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: The first input NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: The second input NDArray.
- `array3` (`NDArray[dtype]`) `[imm]`: The third input NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

###### Overload 2

```mojo
def apply_ternary[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](array1: NDArray[dtype], array2: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible ternary function to two NDArrays and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type of the input NDArrays.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible ternary function to apply.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: The first input NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: The second input NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: The input scalar value.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>
## Functions


<div class="fn-card" markdown="1">

### `bool_simd_store`

```mojo
def bool_simd_store[ptr_origin: MutOrigin, //, simd_width: Int](ptr: Pointer[Scalar[DType.bool], ptr_origin], start: Int, val: SIMD[DType.bool, simd_width])
```

Workaround function for storing bools from a SIMD vector into an UnsafePointer.

**Parameters:**

- `ptr_origin` (`MutOrigin`): Origin of the pointer.
- `simd_width` (`Int`): The SIMD width of the stored value.

**Args:**

- `ptr` (`Pointer[Scalar[DType.bool], ptr_origin]`) `[imm]`: Pointer to be written to.
- `start` (`Int`) `[imm]`: Start position in the pointer.
- `val` (`SIMD[DType.bool, simd_width]`) `[imm]`: SIMD boolean value to store.


</div>
