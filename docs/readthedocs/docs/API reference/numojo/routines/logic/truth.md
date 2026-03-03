# `numojo.routines.logic.truth`

Truth value testing (numojo.routines.logic.truth)

This module implements the truth value testing functions, such as `all` and `any`, for both `NDArray` and `Matrix`.

## Functions


<div class="fn-card" markdown="1">

### `all`

#### Overload 1

```mojo
all[dtype: DType](A: Matrix[dtype]) -> Scalar[dtype]
```

Test whether all array elements evaluate to True.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`): Matrix.

**Returns:**

- `Scalar`

#### Overload 2

```mojo
all[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```

Test whether all array elements evaluate to True along axis.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)
- `axis` (`Int`)

**Returns:**

- `Matrix`

!!! failure "Raises"

#### Overload 3

```mojo
all(array: NDArray[DType.bool]) -> Scalar[DType.bool]
```

If all True.

**Args:**

- `array` (`NDArray`): A NDArray.

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `any`

#### Overload 1

```mojo
any(array: NDArray[DType.bool]) -> Scalar[DType.bool]
```

If any True.

**Args:**

- `array` (`NDArray`): A NDArray.

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 2

```mojo
any[dtype: DType](A: Matrix[dtype]) -> Scalar[dtype]
```

Test whether any array elements evaluate to True.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`): Matrix.

**Returns:**

- `Scalar`

#### Overload 3

```mojo
any[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```

Test whether any array elements evaluate to True along axis.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)
- `axis` (`Int`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>
