# `numojo.routines.bitwise`

Bit-wise operations module (`numojo.routines.bitwise`)

This module implements bit-wise operations on NDArrays, such as bitwise AND, OR, XOR, and NOT (invert).

## Functions


<div class="fn-card" markdown="1">

### `invert`

```mojo
invert[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_integral() if dtype.is_integral() else (dtype == DType.bool)
```

Element-wise invert of an array.

!!! info "Constraints"
    The array must be either a boolean or integral array.

**Parameters:**

- `dtype` (`DType`): The element type.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized`.

**Args:**

- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>
