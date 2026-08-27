# `numojo.routines.math.extrema`

Minimum and maximum operations for arrays.

Element-wise min/max comparisons and axis-aware reduction operations
for NDArrays and Matrices.

Exports
-------
- `min`, `max`: Element-wise minimum and maximum.
- `minimum`, `maximum`: Element-wise operations (aliases).

## Functions


<div class="fn-card" markdown="1">

### `extrema_1d`

```mojo
def extrema_1d[dtype: DType, //, is_max: Bool](a: NDArray[dtype]) -> Scalar[dtype]
```

Find the max or min value in the buffer.

The input is treated as a 1-D array regardless of shape. This is the
backend routine for `max` and `min`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.
- `is_max` (`Bool`): If True, find max value, otherwise find min value.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `max`

<div class="overload-divider">Overload 1</div>

```mojo
def max[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype]
```

Find the max value of an array.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.arange[f32](0, 6).reshape(Shape(2, 3))
var m = nm.max(a)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def max[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Find the max value of an array along an axis.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.arange[f32](0, 6).reshape(Shape(2, 3))
var m = nm.max(a, axis=0)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.
- `axis` (`Int`) `[imm]`: The axis along which the max is performed.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `extrema_1d_max`

```mojo
def extrema_1d_max[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype]
```

Find the max value in a 1-D array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `min`

<div class="overload-divider">Overload 1</div>

```mojo
def min[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype]
```

Find the min value of an array.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.arange[f32](0, 6).reshape(Shape(2, 3))
var m = nm.min(a)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def min[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Find the min value of an array along an axis.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.arange[f32](0, 6).reshape(Shape(2, 3))
var m = nm.min(a, axis=1)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.
- `axis` (`Int`) `[imm]`: The axis along which the min is performed.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `minimum`

<div class="overload-divider">Overload 1</div>

```mojo
def minimum[dtype: DType = DType.float64](s1: Scalar[dtype], s2: Scalar[dtype]) -> Scalar[dtype]
```

Minimum value of two SIMD values.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `s1` (`Scalar[dtype]`) `[imm]`: A SIMD Value.
- `s2` (`Scalar[dtype]`) `[imm]`: A SIMD Value.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

<div class="overload-divider">Overload 2</div>

```mojo
def minimum[dtype: DType = DType.float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise minimum of two arrays.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.array[f32]("[1, 3, 2]")
var b = nm.array[f32]("[2, 1, 4]")
var m = nm.minimum(a, b)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: An array.
- `array2` (`NDArray[dtype]`) `[imm]`: An array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `maximum`

<div class="overload-divider">Overload 1</div>

```mojo
def maximum[dtype: DType = DType.float64](s1: Scalar[dtype], s2: Scalar[dtype]) -> Scalar[dtype]
```

Maximum value of two SIMD values.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `s1` (`Scalar[dtype]`) `[imm]`: A SIMD Value.
- `s2` (`Scalar[dtype]`) `[imm]`: A SIMD Value.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

<div class="overload-divider">Overload 2</div>

```mojo
def maximum[dtype: DType = DType.float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise maximum of two arrays.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.array[f32]("[1, 3, 2]")
var b = nm.array[f32]("[2, 1, 4]")
var m = nm.maximum(a, b)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: A array.
- `array2` (`NDArray[dtype]`) `[imm]`: A array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>
