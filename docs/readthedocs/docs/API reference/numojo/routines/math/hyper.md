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

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `arccosh`

```mojo
def arccosh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse hyperbolic cosine element-wise.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `asinh`

```mojo
def asinh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse hyperbolic sine.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `arcsinh`

```mojo
def arcsinh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse hyperbolic sine element-wise.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `atanh`

```mojo
def atanh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse hyperbolic tangent.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `arctanh`

```mojo
def arctanh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply inverse hyperbolic tangent element-wise.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `cosh`

```mojo
def cosh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply hyperbolic cosine.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `sinh`

```mojo
def sinh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply hyperbolic sine.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `tanh`

```mojo
def tanh[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Apply hyperbolic tangent.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
