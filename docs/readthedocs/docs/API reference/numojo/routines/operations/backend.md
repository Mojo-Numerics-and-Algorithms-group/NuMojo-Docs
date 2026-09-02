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

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct HostExecutor
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Deinitable`, `Movable`

Vectorized CPU Backend.

This struct provides static methods to apply SIMD-compatible
unary and binary functions to NDArrays, Scalars.

</div>

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

```mojo
def __init__(out self)
```

<span class="badge badge-static">static</span>

<div class="prose-label">Args</div>

- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `apply_unary`

<div class="overload-divider">Overload 1</div>

```mojo
def apply_unary[dtype: DType, simd_width: Int, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](scalar: SIMD[dtype, simd_width]) -> SIMD[dtype, simd_width]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible unary function to a SIMD value.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `simd_width` (`Int`): The SIMD width of the input and output.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible function to apply.

<div class="prose-label">Args</div>

- `scalar` (`SIMD[dtype, simd_width]`) `[imm]`: The input SIMD value.

<div class="prose-label">Returns</div>

- `SIMD[dtype, simd_width]`

<div class="overload-divider">Overload 2</div>

```mojo
def apply_unary[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](array: NDArray[dtype]) -> NDArray[dtype]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible unary function to an NDArray.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of the NDArray.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible function to apply.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The input NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `apply_binary`

<div class="overload-divider">Overload 1</div>

```mojo
def apply_binary[dtype: DType, simd_width: Int, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](simd1: SIMD[dtype, simd_width], simd2: SIMD[dtype, simd_width]) -> SIMD[dtype, simd_width]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary function to two SIMD values.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `simd_width` (`Int`): The SIMD width of the input and output.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible binary function to apply.

<div class="prose-label">Args</div>

- `simd1` (`SIMD[dtype, simd_width]`) `[imm]`: The first input SIMD value.
- `simd2` (`SIMD[dtype, simd_width]`) `[imm]`: The second input SIMD value.

<div class="prose-label">Returns</div>

- `SIMD[dtype, simd_width]`

<div class="overload-divider">Overload 2</div>

```mojo
def apply_binary[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary function to two NDArrays.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of the NDArrays.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible binary function to apply.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: The first input NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: The second input NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def apply_binary[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary function to an NDArray and a scalar.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of the NDArray.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible binary function to apply.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The input NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: The input scalar value.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 4</div>

```mojo
def apply_binary[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary function to a scalar and an NDArray.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of the NDArray.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible binary function to apply.

<div class="prose-label">Args</div>

- `scalar` (`Scalar[dtype]`) `[imm]`: The input scalar value.
- `array` (`NDArray[dtype]`) `[imm]`: The input NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 5</div>

```mojo
def apply_binary[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], Int) capturing thin -> SIMD[type, simd_w]](array: NDArray[dtype], intval: Int) -> NDArray[dtype]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary function to an NDArray and an Int scalar.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of the NDArray.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], Int) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible binary function to apply.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The input NDArray.
- `intval` (`Int`) `[imm]`: The input integer value.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `apply_unary_predicate`

<div class="overload-divider">Overload 1</div>

```mojo
def apply_unary_predicate[dtype: DType, simd_width: Int, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]](simd: SIMD[dtype, simd_width]) -> SIMD[DType.bool, simd_width]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible unary predicate to a SIMD value.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `simd_width` (`Int`): The SIMD width of the input and output.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]`): The SIMD-compatible unary predicate function to apply.

<div class="prose-label">Args</div>

- `simd` (`SIMD[dtype, simd_width]`) `[imm]`: The input SIMD value.

<div class="prose-label">Returns</div>

- `SIMD[DType.bool, simd_width]`

<div class="overload-divider">Overload 2</div>

```mojo
def apply_unary_predicate[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]](array: NDArray[dtype]) -> NDArray[DType.bool]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible unary predicate to an NDArray, returning a boolean NDArray.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of the input NDArray.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]`): The SIMD-compatible unary predicate function to apply.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The input NDArray.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `apply_binary_predicate`

<div class="overload-divider">Overload 1</div>

```mojo
def apply_binary_predicate[dtype: DType, simd_width: Int, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]](simd1: SIMD[dtype, simd_width], simd2: SIMD[dtype, simd_width]) -> SIMD[DType.bool, simd_width]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary predicate to two SIMD values.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `simd_width` (`Int`): The SIMD width of the input and output (should be 1 for SIMD).
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]`): The SIMD-compatible binary predicate function to apply.

<div class="prose-label">Args</div>

- `simd1` (`SIMD[dtype, simd_width]`) `[imm]`: The first input SIMD value.
- `simd2` (`SIMD[dtype, simd_width]`) `[imm]`: The second input SIMD value.

<div class="prose-label">Returns</div>

- `SIMD[DType.bool, simd_width]`

<div class="overload-divider">Overload 2</div>

```mojo
def apply_binary_predicate[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary predicate to two NDArrays, returning a boolean NDArray.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of the input NDArrays.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]`): The SIMD-compatible binary predicate function to apply.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: The first input NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: The second input NDArray.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def apply_binary_predicate[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]](array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible binary predicate to an NDArray and a scalar, returning a boolean NDArray.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of the input NDArray.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[DType.bool, simd_w]`): The SIMD-compatible binary predicate function to apply.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: The input NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: The input scalar value.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `apply_ternary`

<div class="overload-divider">Overload 1</div>

```mojo
def apply_ternary[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[dtype]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible ternary function to three NDArrays.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of the NDArrays.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible ternary function to apply.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: The first input NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: The second input NDArray.
- `array3` (`NDArray[dtype]`) `[imm]`: The third input NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def apply_ternary[dtype: DType, kernel: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]](array1: NDArray[dtype], array2: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

<span class="badge badge-static">static</span>

Applies a SIMD-compatible ternary function to two NDArrays and a scalar.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of the input NDArrays.
- `kernel` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w], SIMD[type, simd_w]) capturing thin -> SIMD[type, simd_w]`): The SIMD-compatible ternary function to apply.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: The first input NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: The second input NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: The input scalar value.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
## Functions


<div class="fn-card" markdown="1">

### `bool_simd_store`

```mojo
def bool_simd_store[ptr_origin: MutOrigin, //, simd_width: Int](ptr: Pointer[Scalar[DType.bool], ptr_origin], start: Int, val: SIMD[DType.bool, simd_width])
```

Workaround function for storing bools from a SIMD vector into an UnsafePointer.

<div class="prose-label">Parameters</div>

- `ptr_origin` (`MutOrigin`): Origin of the pointer.
- `simd_width` (`Int`): The SIMD width of the stored value.

<div class="prose-label">Args</div>

- `ptr` (`Pointer[Scalar[DType.bool], ptr_origin]`) `[imm]`: Pointer to be written to.
- `start` (`Int`) `[imm]`: Start position in the pointer.
- `val` (`SIMD[DType.bool, simd_width]`) `[imm]`: SIMD boolean value to store.


</div>
