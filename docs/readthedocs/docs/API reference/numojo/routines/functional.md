# `numojo.routines.functional`

Functional programming utilities for array operations.

Implements functional utilities for NDArray operations such as `apply_along_axis`,
allowing application of functions along array axes.

Exports
-------
- `apply_along_axis_reduce`: Apply a reducing function along an axis.
- `apply_along_axis_reduce_with_dtype`: Apply a reducing function with explicit return dtype.
- `apply_along_axis_reduce_to_int`: Apply a reducing function returning integers.

## Functions


<div class="fn-card" markdown="1">

### `apply_along_axis_reduce_to_int`

```mojo
def apply_along_axis_reduce_to_int[dtype: DType, func1d: def[dtype_func: DType](NDArray[dtype_func]) raises capturing thin -> Int](a: NDArray[dtype], axis: Int) -> NDArray[DType.int]
```

Applies a function to a NDArray by axis and reduce that dimension. The returned data type is DType.int. When the array is 1-d, the returned array will be a 0-d array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the input NDArray elements.
- `func1d` (`def[dtype_func: DType](NDArray[dtype_func]) raises capturing thin -> Int`): The function to apply to the NDArray.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: The NDArray to apply the function to.
- `axis` (`Int`) `[imm]`: The axis to apply the function to.

<div class="prose-label">Returns</div>

- `NDArray[DType.int]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `apply_along_axis_reduce`

```mojo
def apply_along_axis_reduce[dtype: DType, func1d: def[dtype_func: DType](NDArray[dtype_func]) raises capturing thin -> Scalar[dtype_func]](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Applies a function to a NDArray by axis and reduce that dimension. When the array is 1-d, the returned array will be a 0-d array. The target data type of the returned NDArray is different from the input NDArray. This is a function ***overload***.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the input NDArray elements.
- `func1d` (`def[dtype_func: DType](NDArray[dtype_func]) raises capturing thin -> Scalar[dtype_func]`): The function to apply to the NDArray.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: The NDArray to apply the function to.
- `axis` (`Int`) `[imm]`: The axis to apply the function to.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    Error when the array is 1-d.


</div>

<div class="fn-card" markdown="1">

### `apply_along_axis_reduce_with_dtype`

```mojo
def apply_along_axis_reduce_with_dtype[dtype: DType, returned_dtype: DType, func1d: def[dtype_func: DType, returned_dtype_func: DType](NDArray[dtype_func]) raises capturing thin -> Scalar[returned_dtype_func]](a: NDArray[dtype], axis: Int) -> NDArray[returned_dtype]
```

Applies a function to a NDArray by axis and reduce that dimension. When the array is 1-d, the returned array will be a 0-d array. The function returns a different dtype than the input NDArray.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the input NDArray elements.
- `returned_dtype` (`DType`): The data type of the returned NDArray elements.
- `func1d` (`def[dtype_func: DType, returned_dtype_func: DType](NDArray[dtype_func]) raises capturing thin -> Scalar[returned_dtype_func]`): The function to apply to the NDArray.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: The NDArray to apply the function to.
- `axis` (`Int`) `[imm]`: The axis to apply the function to.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `apply_along_axis_preserve`

```mojo
def apply_along_axis_preserve[dtype: DType, func1d: def[dtype_func: DType](NDArray[dtype_func]) raises capturing thin -> NDArray[dtype_func]](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Applies a function to a NDArray by axis without reducing that dimension. The resulting array will have the same shape as the input array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the input NDArray elements.
- `func1d` (`def[dtype_func: DType](NDArray[dtype_func]) raises capturing thin -> NDArray[dtype_func]`): The function to apply to the NDArray.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: The NDArray to apply the function to.
- `axis` (`Int`) `[imm]`: The axis to apply the function to.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `apply_along_axis_inplace`

```mojo
def apply_along_axis_inplace[dtype: DType, func1d: def[dtype_func: DType](mut NDArray[dtype_func]) raises capturing thin -> None](mut a: NDArray[dtype], axis: Int)
```

Applies a function to a NDArray by axis without reducing that dimension. The function is applied in-place to the input array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the input NDArray elements.
- `func1d` (`def[dtype_func: DType](mut NDArray[dtype_func]) raises capturing thin -> None`): The function to apply to the NDArray.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[mut]`: The NDArray to apply the function to.
- `axis` (`Int`) `[imm]`: The axis to apply the function to.

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `apply_along_axis_indices`

```mojo
def apply_along_axis_indices[dtype: DType, func1d: def[dtype_func: DType](NDArray[dtype_func]) raises capturing thin -> NDArray[DType.int]](a: NDArray[dtype], axis: Int) -> NDArray[DType.int]
```

Applies a function to a NDArray by axis without reducing that dimension. The resulting array will have the same shape as the input array. The resulting array is an index array. It can be used for, e.g., argsort.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the input NDArray elements.
- `func1d` (`def[dtype_func: DType](NDArray[dtype_func]) raises capturing thin -> NDArray[DType.int]`): The function to apply to the NDArray.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: The NDArray to apply the function to.
- `axis` (`Int`) `[imm]`: The axis to apply the function to.

<div class="prose-label">Returns</div>

- `NDArray[DType.int]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
