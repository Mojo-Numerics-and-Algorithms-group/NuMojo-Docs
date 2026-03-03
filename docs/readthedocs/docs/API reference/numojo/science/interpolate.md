# `numojo.science.interpolate`

Interpolate Module (numojo.science.interpolate)

Implements interpolation functions.

## Functions


<div class="fn-card" markdown="1">

### `interp1d`

```mojo
interp1d[dtype: DType = DType.float64](xi: NDArray[dtype], x: NDArray[dtype], y: NDArray[dtype], type: String = "linear", fill_method: String = "interpolate") -> NDArray[dtype]
```

Interpolate the values of y at the points xi.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `xi` (`NDArray`): An Array.
- `x` (`NDArray`): An Array.
- `y` (`NDArray`): An Array.
- `type` (`String`): The interpolation method.
- `fill_method` (`String`): The fill value.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>
