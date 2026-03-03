# `numojo.routines.functional`

Functional programming (numojo.routines.functional)

This module implements functional programming utilities for NDArray operations, such as `apply_along_axis`.

## Functions


<div class="fn-card" markdown="1">

### `apply_along_axis_reduce_to_int`

```mojo
apply_along_axis_reduce_to_int[dtype: DType, func1d: fn[dtype_func: DType](NDArray[dtype_func]) raises -> Scalar[DType.int]](a: NDArray[dtype], axis: Int) -> NDArray[DType.int]
```

Applies a function to a NDArray by axis and reduce that dimension. The returned data type is DType.int. When the array is 1-d, the returned array will be a 0-d array.

**Parameters:**

- `dtype` (`DType`): The data type of the input NDArray elements.
- `func1d` (`fn[dtype_func: DType](NDArray[dtype_func]) raises -> Scalar[DType.int]`): The function to apply to the NDArray.

**Args:**

- `a` (`NDArray`): The NDArray to apply the function to.
- `axis` (`Int`): The axis to apply the function to.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `apply_along_axis_reduce`

```mojo
apply_along_axis_reduce[dtype: DType, func1d: fn[dtype_func: DType](NDArray[dtype_func]) raises -> Scalar[dtype_func]](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Applies a function to a NDArray by axis and reduce that dimension. When the array is 1-d, the returned array will be a 0-d array. The target data type of the returned NDArray is different from the input NDArray. This is a function ***overload***.

**Parameters:**

- `dtype` (`DType`): The data type of the input NDArray elements.
- `func1d` (`fn[dtype_func: DType](NDArray[dtype_func]) raises -> Scalar[dtype_func]`): The function to apply to the NDArray.

**Args:**

- `a` (`NDArray`): The NDArray to apply the function to.
- `axis` (`Int`): The axis to apply the function to.

**Returns:**

- `NDArray`

!!! failure "Raises"
    Error when the array is 1-d.


</div>

<div class="fn-card" markdown="1">

### `apply_along_axis_reduce_with_dtype`

```mojo
apply_along_axis_reduce_with_dtype[dtype: DType, returned_dtype: DType, func1d: fn[dtype_func: DType, returned_dtype_func: DType](NDArray[dtype_func]) raises -> Scalar[returned_dtype_func]](a: NDArray[dtype], axis: Int) -> NDArray[returned_dtype]
```

Applies a function to a NDArray by axis and reduce that dimension. When the array is 1-d, the returned array will be a 0-d array. The function returns a different dtype than the input NDArray.

**Parameters:**

- `dtype` (`DType`): The data type of the input NDArray elements.
- `returned_dtype` (`DType`): The data type of the returned NDArray elements.
- `func1d` (`fn[dtype_func: DType, returned_dtype_func: DType](NDArray[dtype_func]) raises -> Scalar[returned_dtype_func]`): The function to apply to the NDArray.

**Args:**

- `a` (`NDArray`): The NDArray to apply the function to.
- `axis` (`Int`): The axis to apply the function to.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `apply_along_axis_preserve`

```mojo
apply_along_axis_preserve[dtype: DType, func1d: fn[dtype_func: DType](NDArray[dtype_func]) raises -> NDArray[dtype_func]](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Applies a function to a NDArray by axis without reducing that dimension. The resulting array will have the same shape as the input array.

**Parameters:**

- `dtype` (`DType`): The data type of the input NDArray elements.
- `func1d` (`fn[dtype_func: DType](NDArray[dtype_func]) raises -> NDArray[dtype_func]`): The function to apply to the NDArray.

**Args:**

- `a` (`NDArray`): The NDArray to apply the function to.
- `axis` (`Int`): The axis to apply the function to.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `apply_along_axis_inplace`

```mojo
apply_along_axis_inplace[dtype: DType, func1d: fn[dtype_func: DType](mut NDArray[dtype_func]) raises -> None](mut a: NDArray[dtype], axis: Int)
```

Applies a function to a NDArray by axis without reducing that dimension. The function is applied in-place to the input array.

**Parameters:**

- `dtype` (`DType`): The data type of the input NDArray elements.
- `func1d` (`fn[dtype_func: DType](mut NDArray[dtype_func]) raises -> None`): The function to apply to the NDArray.

**Args:**

- `a` (`NDArray`) `[mut]`: The NDArray to apply the function to.
- `axis` (`Int`): The axis to apply the function to.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `apply_along_axis_indices`

```mojo
apply_along_axis_indices[dtype: DType, func1d: fn[dtype_func: DType](NDArray[dtype_func]) raises -> NDArray[DType.int]](a: NDArray[dtype], axis: Int) -> NDArray[DType.int]
```

Applies a function to a NDArray by axis without reducing that dimension. The resulting array will have the same shape as the input array. The resulting array is an index array. It can be used for, e.g., argsort.

**Parameters:**

- `dtype` (`DType`): The data type of the input NDArray elements.
- `func1d` (`fn[dtype_func: DType](NDArray[dtype_func]) raises -> NDArray[DType.int]`): The function to apply to the NDArray.

**Args:**

- `a` (`NDArray`): The NDArray to apply the function to.
- `axis` (`Int`): The axis to apply the function to.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>
