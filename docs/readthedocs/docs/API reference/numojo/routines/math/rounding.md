# `numojo.routines.math.rounding`

Rounding routines for NuMojo (numojo.routines.math.rounding).

Offers rounding, truncation, absolute value, and next-after helpers for NDArrays.

## Functions


<div class="fn-card" markdown="1">

### `round`

```mojo
round[dtype: DType](A: Matrix[dtype], decimals: Int = 0) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)
- `decimals` (`Int`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `tabs`

```mojo
tabs[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise absolute value of NDArray.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `tfloor`

```mojo
tfloor[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise round down to nearest whole number of NDArray.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `tceil`

```mojo
tceil[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise round up to nearest whole number of NDArray.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `ttrunc`

```mojo
ttrunc[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise remove decimal value from float whole number of NDArray.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `tround`

```mojo
tround[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise round NDArray to whole number.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `roundeven`

```mojo
roundeven[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Performs element-wise banker's rounding on the elements of a NDArray.

The element-wise banker's rounding of NDArray.

This rounding goes to the nearest integer with ties toward the nearest even integer.

**Parameters:**

- `dtype` (`DType`): The dtype of the input and output array.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array` (`NDArray`): Array to perform rounding on.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `nextafter`

```mojo
nextafter[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Computes the nextafter of the inputs.

**Parameters:**

- `dtype` (`DType`): The dtype of the input and output array. Constraints: must be a floating-point type.
- `backend` (`Backend`): Sets utility function origin, default to `Vectorized`.

**Args:**

- `array1` (`NDArray`): The first input argument.
- `array2` (`NDArray`): The second input argument.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>
