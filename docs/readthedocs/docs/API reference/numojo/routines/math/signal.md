# `numojo.routines.math.signal`

Discrete convolution and one-dimensional linear interpolation.

Exports
-------
- `convolve`: Discrete, linear convolution of two 1-d arrays.
- `interp`: One-dimensional linear interpolation.

## Functions


<div class="fn-card" markdown="1">

### `convolve`

```mojo
def convolve[dtype: DType, //, returned_dtype: DType = .float64](a: NDArray[dtype], v: NDArray[dtype], mode: String = "full") -> NDArray[returned_dtype]
```

Compute the discrete, linear convolution of two 1-d arrays.

Matches `numpy.convolve`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var a = nm.fromstring("[1.0, 2.0, 3.0]")
    var v = nm.fromstring("[0.0, 1.0, 0.5]")
    print(nm.convolve(a, v))  # [0.0, 1.0, 2.5, 4.0, 1.5]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: A 1-d array.
- `v` (`NDArray[dtype]`) `[imm]`: A 1-d array.
- `mode` (`String`) `[imm]`: One of `"full"` (the default), `"same"`, or `"valid"`.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

!!! failure "Raises"
    NumojoError: If `a` or `v` is not 1-dimensional, or either is
empty.
NumojoError: If `mode` is not one of `"full"`, `"same"`, or
`"valid"`.


</div>

<div class="fn-card" markdown="1">

### `interp`

<div class="overload-divider">Overload 1</div>

```mojo
def interp[dtype: DType, xpdtype: DType, fpdtype: DType, //, returned_dtype: DType = .float64](x: Scalar[dtype], xp: NDArray[xpdtype], fp: NDArray[fpdtype], left: Optional[Scalar[returned_dtype]] = None, right: Optional[Scalar[returned_dtype]] = None) -> Scalar[returned_dtype]
```

One-dimensional linear interpolation of a scalar sample point.

Matches `numpy.interp` for a scalar `x`. `xp` must be sorted in
increasing order.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var xp = nm.fromstring("[1.0, 2.0, 3.0]")
    var fp = nm.fromstring("[3.0, 2.0, 0.0]")
    print(nm.interp(Float64(2.5), xp, fp))  # 1.0
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of `x`.
- `xpdtype` (`DType`): The element type of `xp`.
- `fpdtype` (`DType`): The element type of `fp`.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `x` (`Scalar[dtype]`) `[imm]`: The sample point at which to interpolate.
- `xp` (`NDArray[xpdtype]`) `[imm]`: The x-coordinates of the data points, increasing.
- `fp` (`NDArray[fpdtype]`) `[imm]`: The y-coordinates of the data points, the same length as
    `xp`.
- `left` (`Optional[Scalar[returned_dtype]]`) `[imm]`: The value to return for `x < xp[0]`. Defaults to
    `fp[0]`.
- `right` (`Optional[Scalar[returned_dtype]]`) `[imm]`: The value to return for `x > xp[-1]`. Defaults to
    `fp[-1]`.

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

!!! failure "Raises"
    NumojoError: If `xp` and `fp` are not 1-dimensional and the
same length, or if `xp` is empty.

<div class="overload-divider">Overload 2</div>

```mojo
def interp[dtype: DType, xpdtype: DType, fpdtype: DType, //, returned_dtype: DType = .float64](x: NDArray[dtype], xp: NDArray[xpdtype], fp: NDArray[fpdtype], left: Optional[Scalar[returned_dtype]] = None, right: Optional[Scalar[returned_dtype]] = None) -> NDArray[returned_dtype]
```

One-dimensional linear interpolation at an array of sample points.

Matches `numpy.interp`. `xp` must be sorted in increasing order.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var x = nm.fromstring("[0.0, 1.5, 4.0]")
    var xp = nm.fromstring("[1.0, 2.0, 3.0]")
    var fp = nm.fromstring("[3.0, 2.0, 0.0]")
    print(nm.interp(x, xp, fp))  # [3.0, 1.5, 0.0]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of `x`.
- `xpdtype` (`DType`): The element type of `xp`.
- `fpdtype` (`DType`): The element type of `fp`.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `x` (`NDArray[dtype]`) `[imm]`: An array of sample points. It is treated as flat
    regardless of its shape.
- `xp` (`NDArray[xpdtype]`) `[imm]`: The x-coordinates of the data points, increasing.
- `fp` (`NDArray[fpdtype]`) `[imm]`: The y-coordinates of the data points, the same length as
    `xp`.
- `left` (`Optional[Scalar[returned_dtype]]`) `[imm]`: The value to return for `x < xp[0]`. Defaults to
    `fp[0]`.
- `right` (`Optional[Scalar[returned_dtype]]`) `[imm]`: The value to return for `x > xp[-1]`. Defaults to
    `fp[-1]`.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

!!! failure "Raises"
    NumojoError: If `xp` and `fp` are not 1-dimensional and the
same length, or if `xp` is empty.


</div>
