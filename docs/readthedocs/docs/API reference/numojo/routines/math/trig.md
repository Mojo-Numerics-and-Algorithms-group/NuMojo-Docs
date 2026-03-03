# `numojo.routines.math.trig`

Trigonometric routines for NuMojo (numojo.routines.math.trig).

Implements trigonometric and inverse trigonometric functions over NDArrays and Matrices.

## Functions


<div class="fn-card" markdown="1">

### `arccos`

```mojo
arccos[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `acos`

#### Overload 1

```mojo
acos[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply acos also known as inverse cosine .

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
acos[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `arcsin`

```mojo
arcsin[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `asin`

#### Overload 1

```mojo
asin[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply asin also known as inverse sine .

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
asin[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `arctan`

```mojo
arctan[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `atan`

#### Overload 1

```mojo
atan[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply atan also known as inverse tangent .

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
atan[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `atan2`

```mojo
atan2[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Apply atan2 also known as inverse tangent. [atan2 wikipedia](https://en.wikipedia.org/wiki/Atan2).

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): An Array.
- `array2` (`NDArray`): An Array.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `cos`

#### Overload 1

```mojo
cos[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply cos also known as cosine.

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
cos[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `sin`

#### Overload 1

```mojo
sin[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply sin also known as sine .

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
sin[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `tan`

#### Overload 1

```mojo
tan[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply tan also known as tangent .

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
tan[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

### `hypot`

```mojo
hypot[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Apply hypot also known as hypotenuse which finds the longest section of a right triangle given the other two sides.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): An Array.
- `array2` (`NDArray`): An Array.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `hypot_fma`

```mojo
hypot_fma[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Apply hypot also known as hypotenuse which finds the longest section of a right triangle given the other two sides.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): An Array.
- `array2` (`NDArray`): An Array.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>
