# `numojo.core.accelerator.kernels.unary_ops`

GPU kernels for unary operations.

GPU kernel functions and launch helpers for element-wise unary operations
on contiguous AcceleratorNDArray buffers.

Exports
-------
- Unary operation kernel functions for GPU acceleration.

## Functions


<div class="fn-card" markdown="1">

### `neg_kernel`

```mojo
def neg_kernel[dtype: DType](result: Pointer[Scalar[dtype], MutAnyOrigin], a: Pointer[Scalar[dtype], MutAnyOrigin], size: Int)
```

GPU kernel: `result[i] = -a[i]` for contiguous buffers.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `result` (`Pointer[Scalar[dtype], MutAnyOrigin]`) `[imm]`
- `a` (`Pointer[Scalar[dtype], MutAnyOrigin]`) `[imm]`
- `size` (`Int`) `[imm]`


</div>

<div class="fn-card" markdown="1">

### `launch_neg`

```mojo
def launch_neg[dtype: DType](context: DeviceContext, result: Pointer[Scalar[dtype], MutAnyOrigin], a: Pointer[Scalar[dtype], MutAnyOrigin], size: Int, sync: Bool = True)
```

Launch the GPU negation kernel over `size` contiguous elements.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `context` (`DeviceContext`) `[imm]`
- `result` (`Pointer[Scalar[dtype], MutAnyOrigin]`) `[imm]`
- `a` (`Pointer[Scalar[dtype], MutAnyOrigin]`) `[imm]`
- `size` (`Int`) `[imm]`
- `sync` (`Bool`) `[imm]`

!!! failure "Raises"


</div>
