# `numojo.routines.logic.contents`

Contents routines (numojo.routines.logic.contents)

Implements Checking routines: currently not SIMD due to bool bit packing issue

## Functions


<div class="fn-card" markdown="1">

### `isinf`

```mojo
isinf[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[DType.bool]
```

Checks if each element of the input array is infinite.

**Parameters:**

- `dtype` (`DType`): DType - Data type of the input array.
- `backend` (`Backend`): _mf.Backend - Backend to use for the operation. Defaults to _mf.Vectorized.

**Args:**

- `array` (`NDArray`): NDArray[dtype] - Input array to check.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `isfinite`

```mojo
isfinite[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[DType.bool]
```

Checks if each element of the input array is finite.

**Parameters:**

- `dtype` (`DType`): DType - Data type of the input array.
- `backend` (`Backend`): _mf.Backend - Backend to use for the operation. Defaults to _mf.Vectorized.

**Args:**

- `array` (`NDArray`): NDArray[dtype] - Input array to check.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `isnan`

```mojo
isnan[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[DType.bool]
```

Checks if each element of the input array is NaN.

**Parameters:**

- `dtype` (`DType`): DType - Data type of the input array.
- `backend` (`Backend`): _mf.Backend - Backend to use for the operation. Defaults to _mf.Vectorized.

**Args:**

- `array` (`NDArray`): NDArray[dtype] - Input array to check.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `isneginf`

#### Overload 1

```mojo
isneginf[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[DType.bool]
```

Checks if each element of the input array is negative infinity.

**Parameters:**

- `dtype` (`DType`): DType - Data type of the input array.
- `backend` (`Backend`): _mf.Backend - Backend to use for the operation. Defaults to _mf.Vectorized.

**Args:**

- `array` (`NDArray`): NDArray[dtype] - Input array to check.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
isneginf[dtype: DType, backend: Backend = Vectorized](matrix: Matrix[dtype]) -> Matrix[DType.bool]
```

Checks if each element of the input Matrix is negative infinity.

**Parameters:**

- `dtype` (`DType`): DType - Data type of the input Matrix.
- `backend` (`Backend`): _mf.Backend - Backend to use for the operation. Defaults to _mf.Vectorized.

**Args:**

- `matrix` (`Matrix`): Matrix[dtype] - Input Matrix to check.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `isposinf`

#### Overload 1

```mojo
isposinf[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[DType.bool]
```

Checks if each element of the input array is positive infinity. Parameters:     dtype: DType - Data type of the input array.     backend: _mf.Backend - Backend to use for the operation. Defaults to _mf.Vectorized.

**Parameters:**

- `dtype` (`DType`)
- `backend` (`Backend`)

**Args:**

- `array` (`NDArray`): NDArray[dtype] - Input array to check.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
isposinf[dtype: DType, backend: Backend = Vectorized](matrix: Matrix[dtype]) -> Matrix[DType.bool]
```

Checks if each element of the input Matrix is positive infinity. Parameters:     dtype: DType - Data type of the input Matrix.     backend: _mf.Backend - Backend to use for the operation. Defaults to _mf.Vectorized.

**Parameters:**

- `dtype` (`DType`)
- `backend` (`Backend`)

**Args:**

- `matrix` (`Matrix`): Matrix[dtype] - Input Matrix to check.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>
