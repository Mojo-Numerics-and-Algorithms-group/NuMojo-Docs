# `numojo.core.accelerator.kernels.binary_ops`

GPU kernels for binary operations.

GPU kernel functions and launch helpers for element-wise binary operations
on contiguous AcceleratorNDArray buffers.

Exports
-------
- Binary operation kernel functions for GPU acceleration.

## Aliases

### `ADD`

```mojo
comptime ADD
```

**Value:** `0`

### `SUB`

```mojo
comptime SUB
```

**Value:** `1`

### `MUL`

```mojo
comptime MUL
```

**Value:** `2`

### `DIV`

```mojo
comptime DIV
```

**Value:** `3`

## Functions


<div class="fn-card" markdown="1">

### `binary_op_kernel`

```mojo
def binary_op_kernel[dtype: DType, op_code: Int](result: Pointer[Scalar[dtype], MutAnyOrigin], a: Pointer[Scalar[dtype], MutAnyOrigin], b: Pointer[Scalar[dtype], MutAnyOrigin], size: Int)
```

GPU kernel: `result[i] = op(a[i], b[i])` for contiguous buffers.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `op_code` (`Int`)

<div class="prose-label">Args</div>

- `result` (`Pointer[Scalar[dtype], MutAnyOrigin]`) `[imm]`
- `a` (`Pointer[Scalar[dtype], MutAnyOrigin]`) `[imm]`
- `b` (`Pointer[Scalar[dtype], MutAnyOrigin]`) `[imm]`
- `size` (`Int`) `[imm]`


</div>

<div class="fn-card" markdown="1">

### `launch_config`

```mojo
def launch_config(size: Int) -> Tuple[Int, Int]
```

Compute (grid_dim, block_dim) for a one-thread-per-element launch.

<div class="prose-label">Args</div>

- `size` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `Tuple[Int, Int]`


</div>

<div class="fn-card" markdown="1">

### `launch_binary_op`

```mojo
def launch_binary_op[dtype: DType, op_code: Int](context: DeviceContext, result: Pointer[Scalar[dtype], MutAnyOrigin], a: Pointer[Scalar[dtype], MutAnyOrigin], b: Pointer[Scalar[dtype], MutAnyOrigin], size: Int, sync: Bool = True)
```

Launch the GPU binary-op kernel over `size` contiguous elements.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `op_code` (`Int`)

<div class="prose-label">Args</div>

- `context` (`DeviceContext`) `[imm]`
- `result` (`Pointer[Scalar[dtype], MutAnyOrigin]`) `[imm]`
- `a` (`Pointer[Scalar[dtype], MutAnyOrigin]`) `[imm]`
- `b` (`Pointer[Scalar[dtype], MutAnyOrigin]`) `[imm]`
- `size` (`Int`) `[imm]`
- `sync` (`Bool`) `[imm]`

!!! failure "Raises"


</div>
