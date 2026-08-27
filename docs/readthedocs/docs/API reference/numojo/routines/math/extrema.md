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

**Parameters:**

- `dtype` (`DType`): The element type.
- `is_max` (`Bool`): If True, find max value, otherwise find min value.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: An array.

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `max`

#### Overload 1

```mojo
def max[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype]
```

Find the max value of an array.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.arange[f32](0, 6).reshape(Shape(2, 3))
var m = nm.max(a)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: An array.

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def max[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Find the max value of an array along an axis.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.arange[f32](0, 6).reshape(Shape(2, 3))
var m = nm.max(a, axis=0)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: An array.
- `axis` (`Int`) `[imm]`: The axis along which the max is performed.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `extrema_1d_max`

```mojo
def extrema_1d_max[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype]
```

Find the max value in a 1-D array.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `min`

#### Overload 1

```mojo
def min[dtype: DType](a: NDArray[dtype]) -> Scalar[dtype]
```

Find the min value of an array.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.arange[f32](0, 6).reshape(Shape(2, 3))
var m = nm.min(a)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: An array.

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def min[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Find the min value of an array along an axis.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.arange[f32](0, 6).reshape(Shape(2, 3))
var m = nm.min(a, axis=1)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: An array.
- `axis` (`Int`) `[imm]`: The axis along which the min is performed.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `minimum`

#### Overload 1

```mojo
def minimum[dtype: DType = DType.float64](s1: Scalar[dtype], s2: Scalar[dtype]) -> Scalar[dtype]
```

Minimum value of two SIMD values.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `s1` (`Scalar[dtype]`) `[imm]`: A SIMD Value.
- `s2` (`Scalar[dtype]`) `[imm]`: A SIMD Value.

**Returns:**

- `Scalar[dtype]`

#### Overload 2

```mojo
def minimum[dtype: DType = DType.float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise minimum of two arrays.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.array[f32]("[1, 3, 2]")
var b = nm.array[f32]("[2, 1, 4]")
var m = nm.minimum(a, b)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: An array.
- `array2` (`NDArray[dtype]`) `[imm]`: An array.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `maximum`

#### Overload 1

```mojo
def maximum[dtype: DType = DType.float64](s1: Scalar[dtype], s2: Scalar[dtype]) -> Scalar[dtype]
```

Maximum value of two SIMD values.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `s1` (`Scalar[dtype]`) `[imm]`: A SIMD Value.
- `s2` (`Scalar[dtype]`) `[imm]`: A SIMD Value.

**Returns:**

- `Scalar[dtype]`

#### Overload 2

```mojo
def maximum[dtype: DType = DType.float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise maximum of two arrays.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.array[f32]("[1, 3, 2]")
var b = nm.array[f32]("[2, 1, 4]")
var m = nm.maximum(a, b)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A array.
- `array2` (`NDArray[dtype]`) `[imm]`: A array.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>
