# `numojo.routines.linalg.norms`

Norms and other numbers (numojo.routines.linalg.norms)

This module provides functions for computing quantities related to linear algebra, such as determinants and traces.

## Functions


<div class="fn-card" markdown="1">

### `det`

#### Overload 1

```mojo
det[dtype: DType](A: NDArray[dtype]) -> Scalar[dtype]
```

Find the determinant of A using LUP decomposition.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray`)

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 2

```mojo
det[dtype: DType](A: Matrix[dtype]) -> Scalar[dtype]
```

Find the determinant of A using LUP decomposition.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `trace`

#### Overload 1

```mojo
trace[dtype: DType](array: NDArray[dtype], offset: Int = 0, axis1: Int = 0, axis2: Int = 1) -> NDArray[dtype]
```

Computes the trace of a ndarray.

**Parameters:**

- `dtype` (`DType`): Data type of the array.

**Args:**

- `array` (`NDArray`): A NDArray.
- `offset` (`Int`): Offset of the diagonal from the main diagonal.
- `axis1` (`Int`): First axis.
- `axis2` (`Int`): Second axis.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
trace[dtype: DType](A: Matrix[dtype], offset: Int = 0) -> Scalar[dtype]
```

Return the sum along diagonals of the array.

Similar to `numpy.trace`.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)
- `offset` (`Int`)

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>
