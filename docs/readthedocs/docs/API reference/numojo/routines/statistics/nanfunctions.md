# `numojo.routines.statistics.nanfunctions`

Reductions that treat `NaN` elements as missing values.

Mirrors `numpy`'s `nan*` family: each function behaves like its
non-`nan`-prefixed counterpart, except that `NaN` elements are excluded
from the computation instead of propagating into the result.

Exports
-------
- `nansum`: Sum of array elements, ignoring `NaN`.
- `nanmean`: Arithmetic mean of array elements, ignoring `NaN`.
- `nanmax`: Maximum array element, ignoring `NaN`.
- `nanmin`: Minimum array element, ignoring `NaN`.
- `nanvar`: Variance of array elements, ignoring `NaN`.
- `nanstd`: Standard deviation of array elements, ignoring `NaN`.
- `nanmedian`: Median value of array elements, ignoring `NaN`.

## Functions


<div class="fn-card" markdown="1">

### `nansum_1d`

```mojo
def nansum_1d[dtype: DType, //](a: NDArray[dtype]) -> Scalar[dtype]
```

Sum all items in an array, treating `NaN` elements as zero. Regardless of the shape of input, it is treated as a 1-d array. It is the backend function for `nansum`, with or without `axis`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: A 1-d array.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `nansum`

<div class="overload-divider">Overload 1</div>

```mojo
def nansum[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Sum of all items in the array, treating `NaN` elements as zero.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.array[f64]("[1.0, nan, 3.0]")
print(nm.nansum(a))  # 4.0
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def nansum[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype] where dtype.is_floating_point()
```

Sum of array elements over a given axis, treating `NaN` elements as zero.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `axis` (`Int`) `[imm]`: The axis along which the sum is performed.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound.


</div>

<div class="fn-card" markdown="1">

### `nanmean_1d`

```mojo
def nanmean_1d[dtype: DType, //](a: NDArray[dtype]) -> Scalar[dtype]
```

Calculate the arithmetic mean of all items in an array, ignoring `NaN` elements. Regardless of the shape of input, it is treated as a 1-d array. It is the backend function for `nanmean`, with or without `axis`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: A 1-d array.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If all elements are `NaN`.


</div>

<div class="fn-card" markdown="1">

### `nanmean`

<div class="overload-divider">Overload 1</div>

```mojo
def nanmean[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Calculate the arithmetic mean of all items in the array, ignoring `NaN` elements.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.array[f64]("[1.0, nan, 3.0]")
print(nm.nanmean(a))  # 2.0
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If all elements are `NaN`.

<div class="overload-divider">Overload 2</div>

```mojo
def nanmean[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype] where dtype.is_floating_point()
```

Mean of array elements over a given axis, ignoring `NaN` elements.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `axis` (`Int`) `[imm]`: The axis along which the mean is performed.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound.
NumojoError: If a slice along the axis is all `NaN`.


</div>

<div class="fn-card" markdown="1">

### `nanextrema_1d`

```mojo
def nanextrema_1d[dtype: DType, //, is_max: Bool](a: NDArray[dtype]) -> Scalar[dtype]
```

Find the max or min value in the buffer, ignoring `NaN` elements.

The input is treated as a 1-D array regardless of shape. This is the
backend routine for `nanmax` and `nanmin`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `is_max` (`Bool`): If True, find max value, otherwise find min value.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If all elements are `NaN`.


</div>

<div class="fn-card" markdown="1">

### `nanextrema_1d_max`

```mojo
def nanextrema_1d_max[dtype: DType, //](a: NDArray[dtype]) -> Scalar[dtype]
```

Find the max value in a 1-D array, ignoring `NaN` elements.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `nanextrema_1d_min`

```mojo
def nanextrema_1d_min[dtype: DType, //](a: NDArray[dtype]) -> Scalar[dtype]
```

Find the min value in a 1-D array, ignoring `NaN` elements.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `nanmax`

<div class="overload-divider">Overload 1</div>

```mojo
def nanmax[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Find the max value of an array, ignoring `NaN` elements.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.array[f64]("[1.0, nan, 3.0]")
print(nm.nanmax(a))  # 3.0
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If all elements are `NaN`.

<div class="overload-divider">Overload 2</div>

```mojo
def nanmax[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype] where dtype.is_floating_point()
```

Find the max value of an array along an axis, ignoring `NaN` elements.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.
- `axis` (`Int`) `[imm]`: The axis along which the max is performed.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound.
NumojoError: If a slice along the axis is all `NaN`.


</div>

<div class="fn-card" markdown="1">

### `nanmin`

<div class="overload-divider">Overload 1</div>

```mojo
def nanmin[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Find the min value of an array, ignoring `NaN` elements.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.array[f64]("[1.0, nan, 3.0]")
print(nm.nanmin(a))  # 1.0
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If all elements are `NaN`.

<div class="overload-divider">Overload 2</div>

```mojo
def nanmin[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype] where dtype.is_floating_point()
```

Find the min value of an array along an axis, ignoring `NaN` elements.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.
- `axis` (`Int`) `[imm]`: The axis along which the min is performed.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound.
NumojoError: If a slice along the axis is all `NaN`.


</div>

<div class="fn-card" markdown="1">

### `nanvar_1d`

```mojo
def nanvar_1d[dtype: DType, //](a: NDArray[dtype], ddof: Int = Int(0)) -> Scalar[dtype] where dtype.is_floating_point()
```

Compute the variance of all items in a 1-d array, ignoring `NaN` elements. It is the backend function for `nanvar`, with or without `axis`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: A 1-d array.
- `ddof` (`Int`) `[imm]`: Delta degree of freedom.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If all elements are `NaN`.
NumojoError: If `ddof` is not smaller than the number of non-`NaN`
elements.


</div>

<div class="fn-card" markdown="1">

### `nanvar`

<div class="overload-divider">Overload 1</div>

```mojo
def nanvar[dtype: DType](a: NDArray[dtype], ddof: Int = Int(0)) -> Scalar[dtype] where dtype.is_floating_point()
```

Compute the variance of all items in the array, ignoring `NaN` elements.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.array[f64]("[1.0, nan, 3.0]")
print(nm.nanvar(a))  # 1.0
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `ddof` (`Int`) `[imm]`: Delta degree of freedom.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If all elements are `NaN`.
NumojoError: If `ddof` is not smaller than the number of non-`NaN`
elements.

<div class="overload-divider">Overload 2</div>

```mojo
def nanvar[dtype: DType](a: NDArray[dtype], axis: Int, ddof: Int = Int(0)) -> NDArray[dtype] where dtype.is_floating_point()
```

Variance of array elements over a given axis, ignoring `NaN` elements.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `axis` (`Int`) `[imm]`: The axis along which the variance is performed.
- `ddof` (`Int`) `[imm]`: Delta degree of freedom.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound.
NumojoError: If a slice along the axis is all `NaN`.
NumojoError: If `ddof` is not smaller than the number of non-`NaN`
elements in a slice.


</div>

<div class="fn-card" markdown="1">

### `nanstd`

<div class="overload-divider">Overload 1</div>

```mojo
def nanstd[dtype: DType](a: NDArray[dtype], ddof: Int = Int(0)) -> Scalar[dtype] where dtype.is_floating_point()
```

Compute the standard deviation of all items in the array, ignoring `NaN` elements.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.array[f64]("[1.0, nan, 3.0]")
print(nm.nanstd(a))  # 1.0
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `ddof` (`Int`) `[imm]`: Delta degree of freedom.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If all elements are `NaN`.
NumojoError: If `ddof` is not smaller than the number of non-`NaN`
elements.

<div class="overload-divider">Overload 2</div>

```mojo
def nanstd[dtype: DType](a: NDArray[dtype], axis: Int, ddof: Int = Int(0)) -> NDArray[dtype] where dtype.is_floating_point()
```

Standard deviation of array elements over a given axis, ignoring `NaN` elements.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `axis` (`Int`) `[imm]`: The axis along which the standard deviation is performed.
- `ddof` (`Int`) `[imm]`: Delta degree of freedom.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound.
NumojoError: If a slice along the axis is all `NaN`.
NumojoError: If `ddof` is not smaller than the number of non-`NaN`
elements in a slice.


</div>

<div class="fn-card" markdown="1">

### `nanmedian_1d`

```mojo
def nanmedian_1d[dtype: DType, //](a: NDArray[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Compute the median of all items in a 1-d array, ignoring `NaN` elements. It is the backend function for `nanmedian`, with or without `axis`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: A 1-d array.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If all elements are `NaN`.


</div>

<div class="fn-card" markdown="1">

### `nanmedian`

<div class="overload-divider">Overload 1</div>

```mojo
def nanmedian[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Compute the median of all items in the array, ignoring `NaN` elements.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.array[f64]("[1.0, nan, 3.0]")
print(nm.nanmedian(a))  # 2.0
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If all elements are `NaN`.

<div class="overload-divider">Overload 2</div>

```mojo
def nanmedian[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype] where dtype.is_floating_point()
```

Median of array elements over a given axis, ignoring `NaN` elements.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `axis` (`Int`) `[imm]`: The axis along which the median is performed.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound.
NumojoError: If a slice along the axis is all `NaN`.


</div>
