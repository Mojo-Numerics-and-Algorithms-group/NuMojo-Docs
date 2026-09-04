# `numojo.routines.statistics.averages`

Statistical averages and dispersion measures for arrays.

Implements mean, median, mode, variance, and standard deviation for NDArrays.

Exports
-------
- `mean`: Arithmetic mean.
- `median`: Median value.
- `mode`: Most frequent value.
- `var`: Variance.
- `std`: Standard deviation.

## Functions


<div class="fn-card" markdown="1">

### `mean_1d`

```mojo
def mean_1d[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype]) -> Scalar[returned_dtype]
```

Calculate the arithmetic average of all items in an array. Regardless of the shape of input, it is treated as a 1-d array. It is the backend function for `mean`, with or without `axis`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: A 1-d array.

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `mean`

<div class="overload-divider">Overload 1</div>

```mojo
def mean[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype]) -> Scalar[returned_dtype]
```

Calculate the arithmetic average of all items in the array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def mean[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype], axis: Int) -> NDArray[returned_dtype]
```

Mean of array elements over a given axis.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `axis` (`Int`) `[imm]`: The axis along which the mean is performed.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `median_1d`

```mojo
def median_1d[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype]) -> Scalar[returned_dtype]
```

Median value of all items an array. Regardless of the shape of input, it is treated as a 1-d array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: A 1-d array.

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `median`

<div class="overload-divider">Overload 1</div>

```mojo
def median[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype]) -> Scalar[returned_dtype]
```

Median value of all items of an array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: A 1-d array.

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def median[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype], axis: Int) -> NDArray[returned_dtype]
```

Returns median of the array elements along the given axis.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.
- `axis` (`Int`) `[imm]`: The axis along which the median is performed.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `mode_1d`

```mojo
def mode_1d[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype]
```

Returns mode of all items of an array. Regardless of the shape of input, it is treated as a 1-d array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An NDArray.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `mode`

<div class="overload-divider">Overload 1</div>

```mojo
def mode[dtype: DType](array: NDArray[dtype]) -> Scalar[dtype]
```

Mode of all items of an array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: An NDArray.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def mode[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Returns mode of the array elements along the given axis.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An NDArray.
- `axis` (`Int`) `[imm]`: The axis along which the mode is performed.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `stddev`

<div class="overload-divider">Overload 1</div>

```mojo
def stddev[dtype: DType, //, returned_dtype: DType = DType.float64](A: NDArray[dtype], ddof: Int = Int(0)) -> Scalar[returned_dtype]
```

Compute the standard deviation.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: An array.
- `ddof` (`Int`) `[imm]`: Delta degree of freedom.

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def stddev[dtype: DType, //, returned_dtype: DType = DType.float64](A: NDArray[dtype], axis: Int, ddof: Int = Int(0)) -> NDArray[returned_dtype]
```

Computes the standard deviation along the axis.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: An array.
- `axis` (`Int`) `[imm]`: The axis along which the mean is performed.
- `ddof` (`Int`) `[imm]`: Delta degree of freedom.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bounds.
NumojoError: If ddof is not smaller than the size of the axis.


</div>

<div class="fn-card" markdown="1">

### `variance`

<div class="overload-divider">Overload 1</div>

```mojo
def variance[dtype: DType, //, returned_dtype: DType = DType.float64](A: NDArray[dtype], ddof: Int = Int(0)) -> Scalar[returned_dtype]
```

Compute the variance.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: An array.
- `ddof` (`Int`) `[imm]`: Delta degree of freedom.

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def variance[dtype: DType, //, returned_dtype: DType = DType.float64](A: NDArray[dtype], axis: Int, ddof: Int = Int(0)) -> NDArray[returned_dtype]
```

Computes the variance along the axis.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: An array.
- `axis` (`Int`) `[imm]`: The axis along which the mean is performed.
- `ddof` (`Int`) `[imm]`: Delta degree of freedom.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bounds.
NumojoError: If ddof is not smaller than the size of the axis.


</div>
