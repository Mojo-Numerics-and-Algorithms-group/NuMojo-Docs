# `numojo.routines.math.extrema`

Extrema routines for NuMojo (numojo.routines.math.extrema).

Contains min/max helpers for NDArrays and Matrices, including axis-aware reductions and matrix-friendly implementations.

## Functions


<div class="fn-card" markdown="1">

### `extrema_1d`

```mojo
extrema_1d[dtype: DType, //, is_max: Bool](a: NDArray[dtype]) -> Scalar[dtype]
```

Finds the max or min value in the buffer. Regardless of the shape of input, it is treated as a 1-d array. It is the backend function for `max` and `min`, with or without `axis`.

**Parameters:**

- `dtype` (`DType`): The element type.
- `is_max` (`Bool`): If True, find max value, otherwise find min value.

**Args:**

- `a` (`NDArray`): An array.

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `max`

#### Overload 1

```mojo
max[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype]
```

Finds the max value of an array. When no axis is given, the array is flattened before sorting.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray`): An array.

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 2

```mojo
max[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Finds the max value of an array along the axis. The number of dimension will be reduced by 1. When no axis is given, the array is flattened before sorting.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray`): An array.
- `axis` (`Int`): The axis along which the max is performed.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
max[dtype: DType](A: Matrix[dtype]) -> Scalar[dtype]
```

Find max item. It is first flattened before sorting.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 4

```mojo
max[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```

Find max item along the given axis.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)
- `axis` (`Int`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `extrema_1d_max`

```mojo
extrema_1d_max[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype]
```

Finds the max value in a 1-D array.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray`)

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `matrix_extrema`

```mojo
matrix_extrema[dtype: DType, find_max: Bool](A: Matrix[dtype]) -> Scalar[dtype]
```

Generic implementation for finding global min/max in a matrix. Works with any memory layout (row-major or column-major).

**Parameters:**

- `dtype` (`DType`)
- `find_max` (`Bool`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `matrix_extrema_axis`

```mojo
matrix_extrema_axis[dtype: DType, find_max: Bool](A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```

Generic implementation for finding min/max along an axis in a matrix. Works with any memory layout (row-major or column-major).

**Parameters:**

- `dtype` (`DType`)
- `find_max` (`Bool`)

**Args:**

- `A` (`Matrix`)
- `axis` (`Int`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `min`

#### Overload 1

```mojo
min[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype]
```

Finds the min value of an array. When no axis is given, the array is flattened before sorting.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray`): An array.

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 2

```mojo
min[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Finds the min value of an array along the axis. The number of dimension will be reduced by 1. When no axis is given, the array is flattened before sorting.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray`): An array.
- `axis` (`Int`): The axis along which the max is performed.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
min[dtype: DType](A: Matrix[dtype]) -> Scalar[dtype]
```

Find min item.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 4

```mojo
min[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```

Find min item along the given axis.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)
- `axis` (`Int`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `mimimum`

```mojo
mimimum[dtype: DType = DType.float64](s1: Scalar[dtype], s2: Scalar[dtype]) -> Scalar[dtype]
```

Minimum value of two SIMD values.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `s1` (`Scalar`): A SIMD Value.
- `s2` (`Scalar`): A SIMD Value.

**Returns:**

- `Scalar`


</div>

<div class="fn-card" markdown="1">

### `maximum`

#### Overload 1

```mojo
maximum[dtype: DType = DType.float64](s1: Scalar[dtype], s2: Scalar[dtype]) -> Scalar[dtype]
```

Maximum value of two SIMD values.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `s1` (`Scalar`): A SIMD Value.
- `s2` (`Scalar`): A SIMD Value.

**Returns:**

- `Scalar`

#### Overload 2

```mojo
maximum[dtype: DType = DType.float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element wise maximum of two arrays.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray`): A array.
- `array2` (`NDArray`): A array.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `minimum`

```mojo
minimum[dtype: DType = DType.float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element wise minimum of two arrays.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray`): An array.
- `array2` (`NDArray`): An array.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>
