# `numojo.routines.math.rounding`

Rounding, truncation, and floating-point operations.

Element-wise rounding (floor, ceiling, truncation), absolute value, banker's
rounding, and next-after floating-point operations for NDArrays.

Exports
-------
- `tabs`: Absolute value.
- `tfloor`: Floor.
- `tceil`: Ceiling.
- `ttrunc`: Truncation.
- `tround`: Rounding.
- `roundeven`: Banker's rounding.
- `nextafter`: Next representable value.

## Functions


<div class="fn-card" markdown="1">

### `tabs`

```mojo
def tabs[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise absolute value of a NDArray.

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

### `tfloor`

```mojo
def tfloor[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise floor of a NDArray.

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

### `tceil`

```mojo
def tceil[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise ceiling of a NDArray.

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

### `ttrunc`

```mojo
def ttrunc[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise truncation of a NDArray.

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

### `tround`

```mojo
def tround[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise rounding of a NDArray to a whole number.

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

### `roundeven`

```mojo
def roundeven[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise banker's rounding of a NDArray.

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

### `nextafter`

```mojo
def nextafter[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Compute the next representable value after one array toward another.

!!! info "Constraints"
    Datatype `dtype` must be a floating-point type.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: The first input array.
- `array2` (`NDArray[dtype]`) `[imm]`: The second input array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
