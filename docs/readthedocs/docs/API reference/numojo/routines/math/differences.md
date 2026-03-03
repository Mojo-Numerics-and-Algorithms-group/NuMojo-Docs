# `numojo.routines.math.differences`

Difference routines for NuMojo (numojo.routines.math.differences).

Implements gradient and trapezoidal integration helpers for numerical differentiation and integration tasks.

## Functions


<div class="fn-card" markdown="1">

### `gradient`

```mojo
gradient[dtype: DType = DType.float64](x: NDArray[dtype], spacing: Scalar[dtype]) -> NDArray[dtype]
```

Compute the gradient of y over x using the trapezoidal rule.

!!! info "Constraints"
    `fdtype` must be a floating-point type if `idtype` is not a floating-point type.

**Parameters:**

- `dtype` (`DType`): Input data type.

**Args:**

- `x` (`NDArray`): An array.
- `spacing` (`Scalar`): An array of the same shape as x containing the spacing between adjacent elements.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `trapz`

```mojo
trapz[dtype: DType = DType.float64](y: NDArray[dtype], x: NDArray[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Compute the integral of y over x using the trapezoidal rule.

!!! info "Constraints"
    `x` and `y` must have the same shape.
`dtype` must be a floating-point type.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `y` (`NDArray`): An array.
- `x` (`NDArray`): An array.

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>
