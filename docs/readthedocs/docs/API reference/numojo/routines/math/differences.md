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

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Input data type.

<div class="prose-label">Args</div>

- `x` (`NDArray[dtype]`) `[imm]`: An array.
- `spacing` (`Scalar[dtype]`) `[imm]`: An array of the same shape as x containing the spacing between adjacent elements.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `diff`

```mojo
def diff[dtype: DType = DType.float64](array: NDArray[dtype], n: Int = Int(1)) -> NDArray[dtype]
```

Compute the n-th order difference of the input array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A array.
- `n` (`Int`) `[imm]`: The order of the difference.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
