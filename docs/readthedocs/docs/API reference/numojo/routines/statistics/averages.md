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

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: A 1-d array.

**Returns:**

- `Scalar[returned_dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `mean`

#### Overload 1

```mojo
def mean[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype]) -> Scalar[returned_dtype]
```

Calculate the arithmetic average of all items in the array.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.

**Returns:**

- `Scalar[returned_dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def mean[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype], axis: Int) -> NDArray[returned_dtype]
```

Mean of array elements over a given axis.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `axis` (`Int`) `[imm]`: The axis along which the mean is performed.

**Returns:**

- `NDArray[returned_dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `median_1d`

```mojo
def median_1d[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype]) -> Scalar[returned_dtype]
```

Median value of all items an array. Regardless of the shape of input, it is treated as a 1-d array.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: A 1-d array.

**Returns:**

- `Scalar[returned_dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `median`

#### Overload 1

```mojo
def median[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype]) -> Scalar[returned_dtype]
```

Median value of all items of an array.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: A 1-d array.

**Returns:**

- `Scalar[returned_dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def median[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype], axis: Int) -> NDArray[returned_dtype]
```

Returns median of the array elements along the given axis.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: An array.
- `axis` (`Int`) `[imm]`: The axis along which the median is performed.

**Returns:**

- `NDArray[returned_dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `mode_1d`

```mojo
def mode_1d[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype]
```

Returns mode of all items of an array. Regardless of the shape of input, it is treated as a 1-d array.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: An NDArray.

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `mode`

#### Overload 1

```mojo
def mode[dtype: DType](array: NDArray[dtype]) -> Scalar[dtype]
```

Mode of all items of an array.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: An NDArray.

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def mode[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Returns mode of the array elements along the given axis.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: An NDArray.
- `axis` (`Int`) `[imm]`: The axis along which the mode is performed.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `stddev`

#### Overload 1

```mojo
def stddev[dtype: DType, //, returned_dtype: DType = DType.float64](A: NDArray[dtype], ddof: Int = Int(0)) -> Scalar[returned_dtype]
```

Compute the standard deviation.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`: An array.
- `ddof` (`Int`) `[imm]`: Delta degree of freedom.

**Returns:**

- `Scalar[returned_dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def stddev[dtype: DType, //, returned_dtype: DType = DType.float64](A: NDArray[dtype], axis: Int, ddof: Int = Int(0)) -> NDArray[returned_dtype]
```

Computes the standard deviation along the axis.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`: An array.
- `axis` (`Int`) `[imm]`: The axis along which the mean is performed.
- `ddof` (`Int`) `[imm]`: Delta degree of freedom.

**Returns:**

- `NDArray[returned_dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bounds.
NumojoError: If ddof is not smaller than the size of the axis.


</div>

<div class="fn-card" markdown="1">

### `variance`

#### Overload 1

```mojo
def variance[dtype: DType, //, returned_dtype: DType = DType.float64](A: NDArray[dtype], ddof: Int = Int(0)) -> Scalar[returned_dtype]
```

Compute the variance.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`: An array.
- `ddof` (`Int`) `[imm]`: Delta degree of freedom.

**Returns:**

- `Scalar[returned_dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def variance[dtype: DType, //, returned_dtype: DType = DType.float64](A: NDArray[dtype], axis: Int, ddof: Int = Int(0)) -> NDArray[returned_dtype]
```

Computes the variance along the axis.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`: An array.
- `axis` (`Int`) `[imm]`: The axis along which the mean is performed.
- `ddof` (`Int`) `[imm]`: Delta degree of freedom.

**Returns:**

- `NDArray[returned_dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bounds.
NumojoError: If ddof is not smaller than the size of the axis.


</div>
