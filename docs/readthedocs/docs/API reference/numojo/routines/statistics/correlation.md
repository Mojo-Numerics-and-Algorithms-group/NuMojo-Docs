# `numojo.routines.statistics.correlation`

Covariance and correlation-coefficient matrices for 2-D arrays.

Exports
-------
- `cov`: Covariance matrix of a set of variables.
- `corrcoef`: Pearson correlation-coefficient matrix of a set of variables.

## Functions


<div class="fn-card" markdown="1">

### `cov`

```mojo
def cov[dtype: DType, //, returned_dtype: DType = .float64](m: NDArray[dtype], rowvar: Bool = True, ddof: Int = Int(1)) -> NDArray[returned_dtype]
```

Compute the covariance matrix of a set of variables.

Matches `numpy.cov` for a 2-D input: each row (or, if `rowvar` is
`False`, each column) is treated as a variable, with observations
in the other dimension.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var m = nm.fromstring("[[0.0, 2.0], [1.0, 1.0], [2.0, 0.0]]")
    print(nm.cov(m, rowvar=False))
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `m` (`NDArray[dtype]`) `[imm]`: A 2-D array of variables and observations.
- `rowvar` (`Bool`) `[imm]`: If `True` (the default), each row represents a
    variable. If `False`, each column represents a variable.
- `ddof` (`Int`) `[imm]`: Delta degrees of freedom used in the normalizer
    `n_obs - ddof`. Defaults to `1` (matches numpy's default
    `bias=False`).

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

!!! failure "Raises"
    NumojoError: If `m` is not 2-dimensional.
NumojoError: If `ddof` is not smaller than the number of
observations.


</div>

<div class="fn-card" markdown="1">

### `corrcoef`

```mojo
def corrcoef[dtype: DType, //, returned_dtype: DType = .float64](m: NDArray[dtype], rowvar: Bool = True) -> NDArray[returned_dtype]
```

Compute the Pearson correlation-coefficient matrix of a set of variables.

Matches `numpy.corrcoef` for a 2-D input: the covariance matrix
(see `cov`) is normalized so that the diagonal is all `1`s.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
def main() raises:
    var m = nm.fromstring("[[0.0, 2.0], [1.0, 1.0], [2.0, 0.0]]")
    print(nm.corrcoef(m, rowvar=False))
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `returned_dtype` (`DType`): The returned data type, defaulting to float64.

<div class="prose-label">Args</div>

- `m` (`NDArray[dtype]`) `[imm]`: A 2-D array of variables and observations.
- `rowvar` (`Bool`) `[imm]`: If `True` (the default), each row represents a
    variable. If `False`, each column represents a variable.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

!!! failure "Raises"
    NumojoError: If `m` is not 2-dimensional.
NumojoError: If there are fewer than 2 observations.


</div>
