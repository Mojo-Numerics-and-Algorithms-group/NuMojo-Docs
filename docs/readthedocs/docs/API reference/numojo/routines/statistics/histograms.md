# `numojo.routines.statistics.histograms`

Binning and counting of array elements.

Exports
-------
- `bincount`: Count of occurrences of each non-negative integer.
- `histogram`: Count of elements falling into equal-width bins.

## Functions


<div class="fn-card" markdown="1">

### `bincount`

<div class="overload-divider">Overload 1</div>

```mojo
def bincount[dtype: DType](x: NDArray[dtype], minlength: Int = Int(0)) -> NDArray[.int] where dtype.is_integral()
```

Count the occurrences of each non-negative integer in an array.

Matches `numpy.bincount` without weights.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var x = nm.fromstring[nm.i64]("[1, 1, 2, 4]")
    print(nm.bincount(x))  # [0, 2, 1, 0, 1]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type. Must be an integer type.

<div class="prose-label">Args</div>

- `x` (`NDArray[dtype]`) `[imm]`: A 1-d array of non-negative integers.
- `minlength` (`Int`) `[imm]`: The minimum number of bins for the output array.

<div class="prose-label">Returns</div>

- `NDArray[.int]`

!!! failure "Raises"
    NumojoError: If `x` is not 1-dimensional.
NumojoError: If `x` contains a negative value.

<div class="overload-divider">Overload 2</div>

```mojo
def bincount[dtype: DType, wdtype: DType](x: NDArray[dtype], weights: NDArray[wdtype], minlength: Int = Int(0)) -> NDArray[wdtype] where dtype.is_integral()
```

Sum the weights of each non-negative integer's occurrences in an array.

Matches `numpy.bincount` with weights.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var x = nm.fromstring[nm.i64]("[1, 1, 2]")
    var w = nm.fromstring("[0.5, 0.5, 2.0]")
    print(nm.bincount(x, w))  # [0.0, 1.0, 2.0]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type of `x`. Must be an integer type.
- `wdtype` (`DType`): The element type of `weights`.

<div class="prose-label">Args</div>

- `x` (`NDArray[dtype]`) `[imm]`: A 1-d array of non-negative integers.
- `weights` (`NDArray[wdtype]`) `[imm]`: A 1-d array of weights, the same length as `x`.
- `minlength` (`Int`) `[imm]`: The minimum number of bins for the output array.

<div class="prose-label">Returns</div>

- `NDArray[wdtype]`

!!! failure "Raises"
    NumojoError: If `x` is not 1-dimensional, or if `weights` is
not the same length as `x`.
NumojoError: If `x` contains a negative value.


</div>

<div class="fn-card" markdown="1">

### `histogram`

<div class="overload-divider">Overload 1</div>

```mojo
def histogram[dtype: DType, //, returned_dtype: DType = .float64](a: NDArray[dtype], bins: Int = Int(10)) -> Tuple[NDArray[.int], NDArray[returned_dtype]] where dtype.is_floating_point()
```

Compute a histogram of equal-width bins spanning the data range.

Matches `numpy.histogram` with the default `range` (the data's own
min/max).

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var a = nm.fromstring("[0.0, 0.5, 1.5, 2.5]")
    var counts_edges = nm.histogram(a, bins=3)
    print(counts_edges[0])  # counts per bin
    print(counts_edges[1])  # bin edges
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The data type of the returned bin edges,
    defaulting to float64.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array of values to bin. It is treated as flat
    regardless of its shape.
- `bins` (`Int`) `[imm]`: The number of equal-width bins.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[.int], NDArray[returned_dtype]]`

!!! failure "Raises"
    NumojoError: If `bins` is not positive.

<div class="overload-divider">Overload 2</div>

```mojo
def histogram[dtype: DType, //, returned_dtype: DType = .float64](a: NDArray[dtype], bins: Int, range_lo: Scalar[returned_dtype], range_hi: Scalar[returned_dtype]) -> Tuple[NDArray[.int], NDArray[returned_dtype]] where dtype.is_floating_point()
```

Compute a histogram of equal-width bins spanning an explicit range.

Matches `numpy.histogram` with an explicit `range`. Values outside
`[range_lo, range_hi]` are ignored, as in numpy.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var a = nm.fromstring("[0.0, 0.5, 1.5, 2.5]")
    var counts_edges = nm.histogram(a, bins=3, range_lo=0.0, range_hi=3.0)
    print(counts_edges[0])  # [1, 1, 2]
    print(counts_edges[1])  # [0.0, 1.0, 2.0, 3.0]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The data type of the returned bin edges,
    defaulting to float64.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array of values to bin. It is treated as flat
    regardless of its shape.
- `bins` (`Int`) `[imm]`: The number of equal-width bins.
- `range_lo` (`Scalar[returned_dtype]`) `[imm]`: The lower edge of the first bin.
- `range_hi` (`Scalar[returned_dtype]`) `[imm]`: The upper edge of the last bin.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[.int], NDArray[returned_dtype]]`

!!! failure "Raises"
    NumojoError: If `bins` is not positive, or if `range_lo` is
not smaller than `range_hi`.


</div>
