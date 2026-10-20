# `numojo.routines.statistics.percentiles`

Order statistics based on linear interpolation between sorted elements.

Exports
-------
- `quantile`: Value at a given fraction of sorted array elements.
- `percentile`: Value at a given percentage of sorted array elements.
- `quantile_1d`: Backend function for `quantile`, with or without `axis`.

## Functions


<div class="fn-card" markdown="1">

### `quantile_1d`

```mojo
def quantile_1d[dtype: DType, //, returned_dtype: DType = .float64](a: NDArray[dtype], q: Scalar[returned_dtype]) -> Scalar[returned_dtype]
```

Quantile of all items of an array using linear interpolation. Regardless of the shape of input, it is treated as a 1-d array. It is the backend function for `quantile`, with or without `axis`.

Matches `numpy.quantile` with the default (`"linear"`) interpolation
method.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var a = nm.fromstring("[1.0, 2.0, 3.0, 4.0]")
    print(nm.quantile(a, Float64(0.5)))  # 2.5
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: A 1-d array.
- `q` (`Scalar[returned_dtype]`) `[imm]`: Quantile to compute, in the inclusive range `[0, 1]`.

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

!!! failure "Raises"
    NumojoError: If `q` is not in the range `[0, 1]`.


</div>

<div class="fn-card" markdown="1">

### `quantile`

<div class="overload-divider">Overload 1</div>

```mojo
def quantile[dtype: DType, //, returned_dtype: DType = .float64](a: NDArray[dtype], q: Scalar[returned_dtype]) -> Scalar[returned_dtype]
```

Quantile of all items of an array using linear interpolation.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var a = nm.fromstring("[1.0, 2.0, 3.0, 4.0]")
    print(nm.quantile(a, Float64(0.5)))  # 2.5
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.
- `q` (`Scalar[returned_dtype]`) `[imm]`: Quantile to compute, in the inclusive range `[0, 1]`.

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

!!! failure "Raises"
    NumojoError: If `q` is not in the range `[0, 1]`.

<div class="overload-divider">Overload 2</div>

```mojo
def quantile[dtype: DType, //, returned_dtype: DType = .float64](a: NDArray[dtype], q: Scalar[returned_dtype], axis: Int) -> NDArray[returned_dtype]
```

Quantile of the array elements along the given axis.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var a = nm.fromstring("[[1.0, 2.0], [3.0, 4.0]]")
    print(nm.quantile(a, Float64(0.5), axis=0))  # [2.0, 3.0]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.
- `q` (`Scalar[returned_dtype]`) `[imm]`: Quantile to compute, in the inclusive range `[0, 1]`.
- `axis` (`Int`) `[imm]`: The axis along which the quantile is computed.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

!!! failure "Raises"
    NumojoError: If `axis` is out of bounds.
NumojoError: If `q` is not in the range `[0, 1]`.


</div>

<div class="fn-card" markdown="1">

### `percentile`

<div class="overload-divider">Overload 1</div>

```mojo
def percentile[dtype: DType, //, returned_dtype: DType = .float64](a: NDArray[dtype], p: Scalar[returned_dtype]) -> Scalar[returned_dtype]
```

Percentile of all items of an array using linear interpolation.

Equivalent to `quantile(a, p / 100)`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var a = nm.fromstring("[1.0, 2.0, 3.0, 4.0]")
    print(nm.percentile(a, Float64(50)))  # 2.5
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.
- `p` (`Scalar[returned_dtype]`) `[imm]`: Percentile to compute, in the inclusive range `[0, 100]`.

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

!!! failure "Raises"
    NumojoError: If `p` is not in the range `[0, 100]`.

<div class="overload-divider">Overload 2</div>

```mojo
def percentile[dtype: DType, //, returned_dtype: DType = .float64](a: NDArray[dtype], p: Scalar[returned_dtype], axis: Int) -> NDArray[returned_dtype]
```

Percentile of the array elements along the given axis.

Equivalent to `quantile(a, p / 100, axis=axis)`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var a = nm.fromstring("[[1.0, 2.0], [3.0, 4.0]]")
    print(nm.percentile(a, Float64(50), axis=0))  # [2.0, 3.0]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.
- `p` (`Scalar[returned_dtype]`) `[imm]`: Percentile to compute, in the inclusive range `[0, 100]`.
- `axis` (`Int`) `[imm]`: The axis along which the percentile is computed.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

!!! failure "Raises"
    NumojoError: If `axis` is out of bounds.
NumojoError: If `p` is not in the range `[0, 100]`.


</div>
