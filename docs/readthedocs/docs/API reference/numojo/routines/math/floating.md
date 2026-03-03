# `numojo.routines.math.floating`

Floating-point routines for NuMojo (numojo.routines.math.floating).

Offers floating-point specific utilities such as `copysign` on NDArrays.

## Functions


<div class="fn-card" markdown="1">

### `copysign`

```mojo
copysign[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Copy the sign of the first NDArray and apply it to the second NDArray.

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
