# `numojo.routines.statistics.averages`

Averages and dispersion routines for NuMojo (numojo.routines.statistics.averages).

Implements mean, median, mode, variance, and standard deviation helpers for NDArrays and Matrices.

## Functions


<div class="fn-card" markdown="1">

### `mean_1d`

```mojo
mean_1d[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype]) -> Scalar[returned_dtype]
```

Calculate the arithmetic average of all items in an array. Regardless of the shape of input, it is treated as a 1-d array. It is the backend function for `mean`, with or without `axis`.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `a` (`NDArray`): A 1-d array.

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `mean`

#### Overload 1

```mojo
mean[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype]) -> Scalar[returned_dtype]
```

Calculate the arithmetic average of all items in the array.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `a` (`NDArray`): NDArray.

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 2

```mojo
mean[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype], axis: Int) -> NDArray[returned_dtype]
```

Mean of array elements over a given axis.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `a` (`NDArray`): NDArray.
- `axis` (`Int`): The axis along which the mean is performed.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
mean[dtype: DType, //, returned_dtype: DType = DType.float64](a: Matrix[dtype]) -> Scalar[returned_dtype]
```

Calculate the arithmetic average of all items in the Matrix.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `a` (`Matrix`): A matrix.

**Returns:**

- `Scalar`

#### Overload 4

```mojo
mean[dtype: DType, //, returned_dtype: DType = DType.float64](a: Matrix[dtype], axis: Int) -> Matrix[returned_dtype]
```

Calculate the arithmetic average of a Matrix along the axis.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `a` (`Matrix`): A matrix.
- `axis` (`Int`): The axis along which the mean is performed.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `median_1d`

```mojo
median_1d[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype]) -> Scalar[returned_dtype]
```

Median value of all items an array. Regardless of the shape of input, it is treated as a 1-d array.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `a` (`NDArray`): A 1-d array.

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `median`

#### Overload 1

```mojo
median[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype]) -> Scalar[returned_dtype]
```

Median value of all items of an array.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `a` (`NDArray`): A 1-d array.

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 2

```mojo
median[dtype: DType, //, returned_dtype: DType = DType.float64](a: NDArray[dtype], axis: Int) -> NDArray[returned_dtype]
```

Returns median of the array elements along the given axis.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `a` (`NDArray`): An array.
- `axis` (`Int`): The axis along which the median is performed.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `mode_1d`

```mojo
mode_1d[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype]
```

Returns mode of all items of an array. Regardless of the shape of input, it is treated as a 1-d array.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray`): An NDArray.

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `mode`

#### Overload 1

```mojo
mode[dtype: DType](array: NDArray[dtype]) -> Scalar[dtype]
```

Mode of all items of an array.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray`): An NDArray.

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 2

```mojo
mode[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Returns mode of the array elements along the given axis.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray`): An NDArray.
- `axis` (`Int`): The axis along which the mode is performed.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `std`

#### Overload 1

```mojo
std[dtype: DType, //, returned_dtype: DType = DType.float64](A: NDArray[dtype], ddof: Int = 0) -> Scalar[returned_dtype]
```

Compute the standard deviation.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `A` (`NDArray`): An array.
- `ddof` (`Int`): Delta degree of freedom.

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 2

```mojo
std[dtype: DType, //, returned_dtype: DType = DType.float64](A: NDArray[dtype], axis: Int, ddof: Int = 0) -> NDArray[returned_dtype]
```

Computes the standard deviation along the axis.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `A` (`NDArray`): An array.
- `axis` (`Int`): The axis along which the mean is performed.
- `ddof` (`Int`): Delta degree of freedom.

**Returns:**

- `NDArray`

!!! failure "Raises"
    Error: If the axis is out of bounds.
Error: If ddof is not smaller than the size of the axis.

#### Overload 3

```mojo
std[dtype: DType, //, returned_dtype: DType = DType.float64](A: Matrix[dtype], ddof: Int = 0) -> Scalar[returned_dtype]
```

Compute the standard deviation.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `A` (`Matrix`): Matrix.
- `ddof` (`Int`): Delta degree of freedom.

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 4

```mojo
std[dtype: DType, //, returned_dtype: DType = DType.float64](A: Matrix[dtype], axis: Int, ddof: Int = 0) -> Matrix[returned_dtype]
```

Compute the standard deviation along axis.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `A` (`Matrix`): Matrix.
- `axis` (`Int`): 0 or 1.
- `ddof` (`Int`): Delta degree of freedom.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `variance`

#### Overload 1

```mojo
variance[dtype: DType, //, returned_dtype: DType = DType.float64](A: NDArray[dtype], ddof: Int = 0) -> Scalar[returned_dtype]
```

Compute the variance.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `A` (`NDArray`): An array.
- `ddof` (`Int`): Delta degree of freedom.

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 2

```mojo
variance[dtype: DType, //, returned_dtype: DType = DType.float64](A: NDArray[dtype], axis: Int, ddof: Int = 0) -> NDArray[returned_dtype]
```

Computes the variance along the axis.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `A` (`NDArray`): An array.
- `axis` (`Int`): The axis along which the mean is performed.
- `ddof` (`Int`): Delta degree of freedom.

**Returns:**

- `NDArray`

!!! failure "Raises"
    Error: If the axis is out of bounds.
Error: If ddof is not smaller than the size of the axis.

#### Overload 3

```mojo
variance[dtype: DType, //, returned_dtype: DType = DType.float64](A: Matrix[dtype], ddof: Int = 0) -> Scalar[returned_dtype]
```

Compute the variance.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `A` (`Matrix`): Matrix.
- `ddof` (`Int`): Delta degree of freedom.

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 4

```mojo
variance[dtype: DType, //, returned_dtype: DType = DType.float64](A: Matrix[dtype], axis: Int, ddof: Int = 0) -> Matrix[returned_dtype]
```

Compute the variance along axis.

**Parameters:**

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

**Args:**

- `A` (`Matrix`): Matrix.
- `axis` (`Int`): 0 or 1.
- `ddof` (`Int`): Delta degree of freedom.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>
