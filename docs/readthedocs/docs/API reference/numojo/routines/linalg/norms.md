# `numojo.routines.linalg.norms`

Determinant, trace, and vector/matrix norm computation.

Exports
-------
- `det`: Determinant via LUP decomposition.
- `trace`: Sum of the diagonal elements.
- `norm`: Vector or matrix norm.

## Functions


<div class="fn-card" markdown="1">

### `det`

```mojo
def det[dtype: DType](A: NDArray[dtype]) -> Scalar[dtype]
```

Find the determinant of A using LUP decomposition.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `trace`

```mojo
def trace[dtype: DType](array: NDArray[dtype], offset: Int = Int(0), axis1: Int = Int(0), axis2: Int = Int(1)) -> NDArray[dtype]
```

Computes the trace of a ndarray.

<div class="prose-label">Examples</div>
`trace(a)` returns the sum along the main diagonal of `a`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the array.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `offset` (`Int`) `[imm]`: Offset of the diagonal from the main diagonal.
- `axis1` (`Int`) `[imm]`: First axis.
- `axis2` (`Int`) `[imm]`: Second axis.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the array is not two-dimensional or an axis is invalid.


</div>

<div class="fn-card" markdown="1">

### `norm`

<div class="overload-divider">Overload 1</div>

```mojo
def norm[dtype: DType](x: NDArray[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Computes the 2-norm (for vectors) or the Frobenius norm (for matrices) of `x`, i.e. `sqrt(sum(x**2))` over all elements.

This matches `numpy.linalg.norm(x)` (no `ord` given).

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var x = nm.fromstring("[3.0, 4.0]")
    print(nm.linalg.norm(x))  # 5.0
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type. Must be a floating-point type.

<div class="prose-label">Args</div>

- `x` (`NDArray[dtype]`) `[imm]`: A 1-D or 2-D NDArray.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def norm[dtype: DType](x: NDArray[dtype], ord: Scalar[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Computes a vector or matrix norm of `x`, matching a subset of `numpy.linalg.norm(x, ord=ord)`.

For 1-D `x`, `ord` is the order of the generalized p-norm
`sum(|x|**ord)**(1/ord)`, with `ord = inf` and `ord = -inf` special
cased to the max and min absolute value, and `ord = 0` counting the
number of non-zero elements.

For 2-D `x`, `ord` must be one of `1` (max absolute column sum),
`-1` (min absolute column sum), `2` (largest singular value, via
`svd`), `inf` (max absolute row sum), or `-inf` (min absolute row
sum).

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var x = nm.fromstring("[3.0, -4.0]")
    print(nm.linalg.norm(x, Float64(1)))  # 7.0
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type. Must be a floating-point type.

<div class="prose-label">Args</div>

- `x` (`NDArray[dtype]`) `[imm]`: A 1-D or 2-D NDArray.
- `ord` (`Scalar[dtype]`) `[imm]`: The order of the norm.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If `x` is not 1-D or 2-D, or if `ord` is an
unsupported value for a matrix.


</div>
