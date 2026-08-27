# `numojo.routines.math.misc`

Miscellaneous mathematical operations for NDArrays.

Element-wise mathematical operations including cube root, clipping, reciprocal
square root, square root, and scaling functions.

Exports
-------
- `cbrt`: Cube root.
- `clip`: Clip values to range.
- `rsqrt`: Reciprocal square root.
- `sqrt`: Square root.
- `scalb`: Scaling by exponent.

## Functions


<div class="fn-card" markdown="1">

### `cbrt`

```mojo
def cbrt[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise cube root of a NDArray.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `clip`

```mojo
def clip[dtype: DType, //](a: NDArray[dtype], a_min: Scalar[dtype], a_max: Scalar[dtype]) -> NDArray[dtype]
```

Limit values in an array to the range [a_min, a_max]. If a_min is greater than a_max, values are set to a_max.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `a_min` (`Scalar[dtype]`) `[imm]`: The minimum value.
- `a_max` (`Scalar[dtype]`) `[imm]`: The maximum value.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `rsqrt`

```mojo
def rsqrt[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise reciprocal square root of NDArray.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `sqrt`

```mojo
def sqrt[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise square root of a NDArray.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `scalb`

```mojo
def scalb[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Apply scalb element-wise to two arrays.

!!! info "Constraints"
    Both arrays must have the same shapes.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>
