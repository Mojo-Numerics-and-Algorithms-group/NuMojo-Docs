# `numojo.routines.math.trig`

Trigonometric and inverse trigonometric functions for arrays.

Element-wise trigonometric functions (sin, cos, tan) and their inverse/hyperbolic
variants (arcsin, arccos, arctan, atan2, sinh, cosh, tanh, etc.) for NDArrays.

Exports
-------
- Circular: `sin`, `cos`, `tan`, `arcsin`, `arccos`, `arctan`, `atan2`.
- Hyperbolic: `sinh`, `cosh`, `tanh`, `arcsinh`, `arccosh`, `arctanh`.
- Utilities: `hypot`, `hypot_fma`.

## Functions


<div class="fn-card" markdown="1">

### `acos`

```mojo
def acos[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse cosine.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `arccos`

```mojo
def arccos[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse cosine element-wise.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `asin`

```mojo
def asin[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse sine.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `arcsin`

```mojo
def arcsin[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse sine element-wise.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `atan`

```mojo
def atan[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse tangent.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `arctan`

```mojo
def arctan[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse tangent element-wise.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `atan2`

```mojo
def atan2[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse tangent with two arrays.

References:
    https://en.wikipedia.org/wiki/Atan2.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `cos`

```mojo
def cos[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply cosine.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `sin`

```mojo
def sin[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply sine.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `tan`

```mojo
def tan[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply tangent.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `hypot`

```mojo
def hypot[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Apply hypotenuse calculation to two arrays.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `hypot_fma`

```mojo
def hypot_fma[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Apply hypotenuse calculation using fused multiply-add.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>
