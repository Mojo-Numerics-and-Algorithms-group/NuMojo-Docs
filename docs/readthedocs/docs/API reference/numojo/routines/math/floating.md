# `numojo.routines.math.floating`

Floating-point specific operations for NDArrays.

Implements floating-point helper functions such as `copysign` for element-wise
sign manipulation.

Exports
-------
- `copysign`: Copy sign from one array to another.

## Functions


<div class="fn-card" markdown="1">

### `copysign`

```mojo
def copysign[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Copy the sign of one array onto another.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    Error if shape of `array1` and `array2` do not match.


</div>
