# `numojo.routines.math.differences`

Numerical differentiation and integration helpers.

Implements gradient computation and finite differences for numerical differentiation
and integration tasks.

Exports
-------
- `gradient`: Compute gradients using the trapezoidal rule.
- `diff`: Compute n-th order finite differences.
- `ediff1d`: Compute the differences of a flattened array, with
  optional values prepended/appended.

## Functions


<div class="fn-card" markdown="1">

### `gradient`

```mojo
def gradient[dtype: DType = .float64](x: NDArray[dtype], spacing: Scalar[dtype]) -> NDArray[dtype]
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
def diff[dtype: DType = .float64](array: NDArray[dtype], n: Int = Int(1)) -> NDArray[dtype]
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

<div class="fn-card" markdown="1">

### `ediff1d`

```mojo
def ediff1d[dtype: DType](ary: NDArray[dtype], to_end: Optional[NDArray[dtype]] = None, to_begin: Optional[NDArray[dtype]] = None) -> NDArray[dtype]
```

Compute the consecutive differences of a flattened array, with optional values prepended and/or appended.

Matches `numpy.ediff1d`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var a = nm.fromstring("[1.0, 2.0, 4.0, 7.0]")
    print(nm.ediff1d(a))  # [1.0, 2.0, 3.0]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `ary` (`NDArray[dtype]`) `[imm]`: An array. It is treated as flat regardless of its shape.
- `to_end` (`Optional[NDArray[dtype]]`) `[imm]`: Values to append to the end of the differences.
- `to_begin` (`Optional[NDArray[dtype]]`) `[imm]`: Values to prepend to the start of the differences.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
