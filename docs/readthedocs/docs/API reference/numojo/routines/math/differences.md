# `numojo.routines.math.differences`

Numerical differentiation and integration helpers.

Implements gradient computation and finite differences for numerical differentiation
and integration tasks.

Exports
-------
- `gradient`: Compute gradients using the trapezoidal rule.
- `diff`: Compute n-th order finite differences.

## Functions


<div class="fn-card" markdown="1">

### `gradient`

```mojo
def gradient[dtype: DType = DType.float64](x: NDArray[dtype], spacing: Scalar[dtype]) -> NDArray[dtype]
```

Compute the gradient of y over x using the trapezoidal rule.

!!! info "Constraints"
    `fdtype` must be a floating-point type if `idtype` is not a floating-point type.

**Parameters:**

- `dtype` (`DType`): Input data type.

**Args:**

- `x` (`NDArray[dtype]`) `[imm]`: An array.
- `spacing` (`Scalar[dtype]`) `[imm]`: An array of the same shape as x containing the spacing between adjacent elements.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `diff`

```mojo
def diff[dtype: DType = DType.float64](array: NDArray[dtype], n: Int = Int(1)) -> NDArray[dtype]
```

Compute the n-th order difference of the input array.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A array.
- `n` (`Int`) `[imm]`: The order of the difference.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>
