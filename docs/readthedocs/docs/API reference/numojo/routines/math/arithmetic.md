# `numojo.routines.math.arithmetic`

Arithmetic routines for NuMojo (numojo.routines.math.arithmetic).

Implements addition, subtraction, multiplication, division, floor division, fused multiply-add, and remainder helpers for NDArrays.

## Functions


<div class="fn-card" markdown="1">

### `add`

#### Overload 1

```mojo
add[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Perform addition on two arrays.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array1` (`NDArray`): A NDArray.
- `array2` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
add[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Perform addition on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array` (`NDArray`): A NDArray.
- `scalar` (`Scalar`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
add[dtype: DType, backend: Backend = Vectorized](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Perform addition on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `scalar` (`Scalar`): A NDArray.
- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 4

```mojo
add[dtype: DType, backend: Backend = Vectorized](var *values: Variant[NDArray[dtype], Scalar[dtype]]) -> NDArray[dtype]
```

Perform addition on a list of arrays and a scalars.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `*values` (`Variant`) `[var]`: A list of arrays or Scalars to be added.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `sub`

#### Overload 1

```mojo
sub[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Perform subtraction on two arrays.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array1` (`NDArray`): A NDArray.
- `array2` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
sub[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Perform subtraction on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array` (`NDArray`): A NDArray.
- `scalar` (`Scalar`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
sub[dtype: DType, backend: Backend = Vectorized](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Perform subtraction on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `scalar` (`Scalar`): A NDArray.
- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `diff`

```mojo
diff[dtype: DType = DType.float64](array: NDArray[dtype], n: Int) -> NDArray[dtype]
```

Compute the n-th order difference of the input array.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray`): A array.
- `n` (`Int`): The order of the difference.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `mod`

#### Overload 1

```mojo
mod[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise modulo of array1 and array2.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array1` (`NDArray`): A NDArray.
- `array2` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
mod[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Perform subtraction on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array` (`NDArray`): A NDArray.
- `scalar` (`Scalar`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
mod[dtype: DType, backend: Backend = Vectorized](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Perform subtraction on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `scalar` (`Scalar`): A NDArray.
- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `mul`

#### Overload 1

```mojo
mul[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise product of array1 and array2.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array1` (`NDArray`): A NDArray.
- `array2` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
mul[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Perform multiplication on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array` (`NDArray`): A NDArray.
- `scalar` (`Scalar`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
mul[dtype: DType, backend: Backend = Vectorized](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Perform multiplication on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `scalar` (`Scalar`): A NDArray.
- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 4

```mojo
mul[dtype: DType, backend: Backend = Vectorized](var *values: Variant[NDArray[dtype], Scalar[dtype]]) -> NDArray[dtype]
```

Perform multiplication on a list of arrays an arrays and a scalars.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `*values` (`Variant`) `[var]`: A list of arrays or Scalars to be added.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `div`

#### Overload 1

```mojo
div[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise quotient of array1 and array2.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array1` (`NDArray`): A NDArray.
- `array2` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
div[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Perform true division on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array` (`NDArray`): A NDArray.
- `scalar` (`Scalar`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
div[dtype: DType, backend: Backend = Vectorized](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Perform true division on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `scalar` (`Scalar`): A NDArray.
- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `floor_div`

#### Overload 1

```mojo
floor_div[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise quotient of array1 and array2.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array1` (`NDArray`): A NDArray.
- `array2` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
floor_div[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Perform true division on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array` (`NDArray`): A NDArray.
- `scalar` (`Scalar`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
floor_div[dtype: DType, backend: Backend = Vectorized](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Perform true division on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `scalar` (`Scalar`): A NDArray.
- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `fma`

#### Overload 1

```mojo
fma[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[dtype]
```

Apply a SIMD level fuse multiply add function of three variables and one return to a NDArray.

!!! info "Constraints"
    Both arrays must have the same shape.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array1` (`NDArray`): A NDArray.
- `array2` (`NDArray`): A NDArray.
- `array3` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
fma[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype], simd: Scalar[dtype]) -> NDArray[dtype]
```

Apply a SIMD level fuse multiply add function of three variables and one return to a NDArray.

!!! info "Constraints"
    Both arrays must have the same shape

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array1` (`NDArray`): A NDArray.
- `array2` (`NDArray`): A NDArray.
- `simd` (`Scalar`): A SIMD[dtype,1] value to be added.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `remainder`

```mojo
remainder[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise remainders of NDArray.

!!! info "Constraints"
    Both arrays must have the same shapes.

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
