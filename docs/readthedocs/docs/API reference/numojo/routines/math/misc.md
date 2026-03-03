# `numojo.routines.math.misc`

Miscellaneous math routines for NuMojo (numojo.routines.math.misc).

Offers utilities such as cube root, clipping, reciprocal square root, square root, and scalb for NDArrays.

## Functions


<div class="fn-card" markdown="1">

### `cbrt`

```mojo
cbrt[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise cuberoot of NDArray.

!!! info "Constraints"
    Both arrays must have the same shapes.

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

### `clip`

```mojo
clip[dtype: DType, //](a: NDArray[dtype], a_min: Scalar[dtype], a_max: Scalar[dtype]) -> NDArray[dtype]
```

Limit the values in an array between [a_min, a_max]. If a_min is greater than a_max, the value is equal to a_max.

**Parameters:**

- `dtype` (`DType`): The data type.

**Args:**

- `a` (`NDArray`): A array.
- `a_min` (`Scalar`): The minimum value.
- `a_max` (`Scalar`): The maximum value.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `rsqrt`

```mojo
rsqrt[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise reciprocal squareroot of NDArray.

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

### `sqrt`

```mojo
sqrt[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise square root of NDArray.

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

### `scalb`

```mojo
scalb[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Calculate the scalb of array1 and array2.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array1` (`NDArray`): A NDArray.
- `array2` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>
