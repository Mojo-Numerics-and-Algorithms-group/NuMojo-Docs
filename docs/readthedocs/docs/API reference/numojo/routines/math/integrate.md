# `numojo.routines.math.integrate`

Trapezoidal-rule integration of flattened arrays.

Exports
-------
- `trapezoid`: Definite integral using the composite trapezoidal rule.
- `cumtrapz`: Cumulative integral using the composite trapezoidal rule.

## Functions


<div class="fn-card" markdown="1">

### `trapezoid`

<div class="overload-divider">Overload 1</div>

```mojo
def trapezoid[dtype: DType, //, returned_dtype: DType = .float64](y: NDArray[dtype], dx: Scalar[returned_dtype] = 1) -> Scalar[returned_dtype]
```

Integrate a flattened array using the composite trapezoidal rule, with uniformly-spaced samples.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var y = nm.fromstring("[1.0, 2.0, 3.0]")
    print(nm.trapezoid(y))  # 4.0
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `y` (`NDArray[dtype]`) `[imm]`: An array of sample values. It is treated as flat regardless
    of its shape.
- `dx` (`Scalar[returned_dtype]`) `[imm]`: The uniform spacing between samples.

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def trapezoid[dtype: DType, xdtype: DType, //, returned_dtype: DType = .float64](y: NDArray[dtype], x: NDArray[xdtype]) -> Scalar[returned_dtype]
```

Integrate a flattened array using the composite trapezoidal rule, with non-uniformly-spaced sample positions.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var y = nm.fromstring("[1.0, 2.0, 3.0]")
    var x = nm.fromstring("[0.0, 1.0, 2.0]")
    print(nm.trapezoid(y, x))  # 4.0
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of `y`.
- `xdtype` (`DType`): The element type of `x`.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `y` (`NDArray[dtype]`) `[imm]`: An array of sample values. It is treated as flat regardless
    of its shape.
- `x` (`NDArray[xdtype]`) `[imm]`: The sample positions, the same length as `y`.

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

!!! failure "Raises"
    NumojoError: If `x` is not the same length as `y`.


</div>

<div class="fn-card" markdown="1">

### `cumtrapz`

<div class="overload-divider">Overload 1</div>

```mojo
def cumtrapz[dtype: DType, //, returned_dtype: DType = .float64](y: NDArray[dtype], dx: Scalar[returned_dtype] = 1, initial: Optional[Scalar[returned_dtype]] = None) -> NDArray[returned_dtype]
```

Cumulatively integrate a flattened array using the composite trapezoidal rule, with uniformly-spaced samples.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var y = nm.fromstring("[1.0, 2.0, 3.0]")
    print(nm.cumtrapz(y))  # [1.5, 4.0]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `y` (`NDArray[dtype]`) `[imm]`: An array of sample values. It is treated as flat regardless
    of its shape.
- `dx` (`Scalar[returned_dtype]`) `[imm]`: The uniform spacing between samples.
- `initial` (`Optional[Scalar[returned_dtype]]`) `[imm]`: If given, prepended to the result so its length
    matches `y`. If `None` (the default), the result has
    length `y.size - 1`.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def cumtrapz[dtype: DType, xdtype: DType, //, returned_dtype: DType = .float64](y: NDArray[dtype], x: NDArray[xdtype], initial: Optional[Scalar[returned_dtype]] = None) -> NDArray[returned_dtype]
```

Cumulatively integrate a flattened array using the composite trapezoidal rule, with non-uniformly-spaced sample positions.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var y = nm.fromstring("[1.0, 2.0, 3.0]")
    var x = nm.fromstring("[0.0, 1.0, 2.0]")
    print(nm.cumtrapz(y, x))  # [1.5, 4.0]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of `y`.
- `xdtype` (`DType`): The element type of `x`.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `y` (`NDArray[dtype]`) `[imm]`: An array of sample values. It is treated as flat regardless
    of its shape.
- `x` (`NDArray[xdtype]`) `[imm]`: The sample positions, the same length as `y`.
- `initial` (`Optional[Scalar[returned_dtype]]`) `[imm]`: If given, prepended to the result so its length
    matches `y`. If `None` (the default), the result has
    length `y.size - 1`.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

!!! failure "Raises"
    NumojoError: If `x` is not the same length as `y`.


</div>
