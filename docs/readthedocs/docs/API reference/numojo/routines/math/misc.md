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

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `clip`

```mojo
def clip[dtype: DType, //](a: NDArray[dtype], a_min: Scalar[dtype], a_max: Scalar[dtype]) -> NDArray[dtype]
```

Limit values in an array to the range [a_min, a_max]. If a_min is greater than a_max, values are set to a_max.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `a_min` (`Scalar[dtype]`) `[imm]`: The minimum value.
- `a_max` (`Scalar[dtype]`) `[imm]`: The maximum value.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `rsqrt`

```mojo
def rsqrt[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise reciprocal square root of NDArray.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `sqrt`

```mojo
def sqrt[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise square root of a NDArray.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

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

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>
