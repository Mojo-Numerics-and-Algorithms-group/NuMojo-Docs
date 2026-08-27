# `numojo.routines.math.hyper`

Hyperbolic and inverse hyperbolic trigonometric functions.

Element-wise hyperbolic functions (sinh, cosh, tanh) and their inverses
(asinh, acosh, atanh) for NDArrays.

Exports
-------
- `sinh`, `cosh`, `tanh`: Hyperbolic functions.
- `asinh`, `acosh`, `atanh`: Inverse hyperbolic functions.

## Functions


<div class="fn-card" markdown="1">

### `acosh`

```mojo
def acosh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse hyperbolic cosine.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `arccosh`

```mojo
def arccosh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse hyperbolic cosine element-wise.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `asinh`

```mojo
def asinh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse hyperbolic sine.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `arcsinh`

```mojo
def arcsinh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse hyperbolic sine element-wise.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `atanh`

```mojo
def atanh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse hyperbolic tangent.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `arctanh`

```mojo
def arctanh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse hyperbolic tangent element-wise.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `cosh`

```mojo
def cosh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply hyperbolic cosine.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `sinh`

```mojo
def sinh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply hyperbolic sine.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `tanh`

```mojo
def tanh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply hyperbolic tangent.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>
