# `numojo.core.accelerator.kernels.reduction_ops`

GPU kernels for reduction operations.

GPU kernel functions and launch helpers for full-array reduction operations.

Exports
-------
- Reduction operation kernel functions for GPU acceleration.

## Functions


<div class="fn-card" markdown="1">

### `sum_reduce_kernel`

```mojo
def sum_reduce_kernel[dtype: DType, block_size: Int](partial_sums: Pointer[Scalar[dtype], MutAnyOrigin], a: Pointer[Scalar[dtype], MutAnyOrigin], size: Int)
```

GPU kernel: each block reduces its chunk of `a` to one partial sum.

The host is responsible for summing the `partial_sums` buffer
(one element per block) into the final scalar result.

**Parameters:**

- `dtype` (`DType`)
- `block_size` (`Int`)

**Args:**

- `partial_sums` (`Pointer[Scalar[dtype], MutAnyOrigin]`) `[imm]`
- `a` (`Pointer[Scalar[dtype], MutAnyOrigin]`) `[imm]`
- `size` (`Int`) `[imm]`


</div>

<div class="fn-card" markdown="1">

### `launch_sum_reduce`

```mojo
def launch_sum_reduce[dtype: DType](context: DeviceContext, a: Pointer[Scalar[dtype], MutAnyOrigin], size: Int) -> Scalar[dtype]
```

Launch the GPU sum-reduction kernel and combine partial sums.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `context` (`DeviceContext`) `[imm]`: The `DeviceContext` backing `a`'s device memory.
- `a` (`Pointer[Scalar[dtype], MutAnyOrigin]`) `[imm]`: Device pointer to the first element to reduce.
- `size` (`Int`) `[imm]`: Number of contiguous elements to reduce.

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"


</div>
