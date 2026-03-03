# `numojo.routines.math.hyper`

Hyperbolic routines for NuMojo (numojo.routines.math.hyper).

Implements hyperbolic and inverse hyperbolic trigonometric functions operating on NDArrays and Matrices.

## Functions


<div class="fn-card" markdown="1">

### `arccosh`

```mojo
arccosh[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `acosh`

#### Overload 1

```mojo
acosh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply acosh also known as inverse hyperbolic cosine .

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array` (`NDArray`): An Array.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
acosh[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `arcsinh`

```mojo
arcsinh[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `asinh`

#### Overload 1

```mojo
asinh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply asinh also known as inverse hyperbolic sine .

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array` (`NDArray`): An Array.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
asinh[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `arctanh`

```mojo
arctanh[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `atanh`

#### Overload 1

```mojo
atanh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply atanh also known as inverse hyperbolic tangent .

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array` (`NDArray`): An Array.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
atanh[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `cosh`

#### Overload 1

```mojo
cosh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply cosh also known as hyperbolic cosine .

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array` (`NDArray`): An Array assumed to be in radian.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
cosh[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `sinh`

#### Overload 1

```mojo
sinh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply sin also known as hyperbolic sine .

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array` (`NDArray`): An Array assumed to be in radian.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
sinh[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `tanh`

#### Overload 1

```mojo
tanh[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply tan also known as hyperbolic tangent .

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array` (`NDArray`): An Array assumed to be in radian.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
tanh[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>
