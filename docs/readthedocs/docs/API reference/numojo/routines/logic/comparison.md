# `numojo.routines.logic.comparison`

Comparison operations for NDArrays.

Element-wise comparison operators (greater, less, equal, etc.) returning
boolean arrays for NDArrays.

Exports
-------
- `greater`: Greater than comparison.
- `less`: Less than comparison.
- `equal`: Equality comparison.
- `greater_equal`: Greater than or equal comparison.
- `less_equal`: Less than or equal comparison.
- `not_equal`: Not equal comparison.
- `allclose`: All close comparison.

## Functions


<div class="fn-card" markdown="1">

### `greater`

<div class="overload-divider">Overload 1</div>

```mojo
def greater[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

Performs element-wise comparison to check if values in `array1` are greater than values in `array2`.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.logic.comparison import greater

var arr1 = nm.array[nm.f64]([1.0, 2.0, 3.0], shape=[3])
var arr2 = nm.array[nm.f64]([0.5, 2.5, 2.0], shape=[3])
print(greater[nm.f64](arr1, arr2))  # Output: [True, False, True]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The dtype of the input NDArray.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: First NDArray to compare.
- `array2` (`NDArray[dtype]`) `[imm]`: Second NDArray to compare.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def greater[dtype: DType](array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

Performs element-wise comparison to check if values in `array1` are greater than a scalar value.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.logic.comparison import greater

var arr = nm.array[nm.f64]([1.0, 2.0, 3.0], shape=[3])
print(greater[nm.f64](arr, 2.0))  # Output: [False, False, True]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The dtype of the input NDArray.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: NDArray to compare.
- `scalar` (`Scalar[dtype]`) `[imm]`: Scalar value to compare against.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `greater_equal`

<div class="overload-divider">Overload 1</div>

```mojo
def greater_equal[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

Performs element-wise comparison to check if values in `array1` are greater than or equal to values in `array2`.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.logic.comparison import greater_equal

var arr1 = nm.array[nm.f64]([1.0, 2.0, 3.0], shape=[3])
var arr2 = nm.array[nm.f64]([0.5, 2.0, 4.0], shape=[3])
print(greater_equal[nm.f64](arr1, arr2))  # Output: [True, True, False]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The dtype of the input NDArray.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: First NDArray to compare.
- `array2` (`NDArray[dtype]`) `[imm]`: Second NDArray to compare.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def greater_equal[dtype: DType](array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

Performs element-wise comparison to check if values in `array1` are greater than or equal to a scalar value.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.logic.comparison import greater_equal

var arr = nm.array[nm.f64]([1.0, 2.0, 3.0], shape=[3])
print(greater_equal[nm.f64](arr, 2.0))  # Output: [False, True, True]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The dtype of the input NDArray.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: NDArray to compare.
- `scalar` (`Scalar[dtype]`) `[imm]`: Scalar value to compare against.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `less`

<div class="overload-divider">Overload 1</div>

```mojo
def less[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

Performs element-wise comparison to check if values in `array1` are less than values in `array2`.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.logic.comparison import less

var arr1 = nm.array[nm.f64]([1.0, 2.0, 3.0], shape=[3])
var arr2 = nm.array[nm.f64]([0.5, 2.5, 2.0], shape=[3])
print(less[nm.f64](arr1, arr2))  # Output: [False, True, False]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The dtype of the input NDArray.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: First NDArray to compare.
- `array2` (`NDArray[dtype]`) `[imm]`: Second NDArray to compare.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def less[dtype: DType](array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

Performs element-wise comparison to check if values in `array1` are less than a scalar value.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.logic.comparison import less

var arr = nm.array[nm.f64]([1.0, 2.0, 3.0], shape=[3])
print(less[nm.f64](arr, 2.0))  # Output: [True, False, False]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The dtype of the input NDArray.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: NDArray to compare.
- `scalar` (`Scalar[dtype]`) `[imm]`: Scalar value to compare against.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `less_equal`

<div class="overload-divider">Overload 1</div>

```mojo
def less_equal[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

Performs element-wise comparison to check if values in `array1` are less than or equal to values in `array2`.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.logic.comparison import less_equal

var arr1 = nm.array[nm.f64]([1.0, 2.0, 3.0], shape=[3])
var arr2 = nm.array[nm.f64]([0.5, 2.0, 4.0], shape=[3])
print(less_equal[nm.f64](arr1, arr2))  # Output: [False, True, True]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The dtype of the input NDArray.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: First NDArray to compare.
- `array2` (`NDArray[dtype]`) `[imm]`: Second NDArray to compare.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def less_equal[dtype: DType](array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

Performs element-wise comparison to check if values in `array1` are less than or equal to a scalar value.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.logic.comparison import less_equal

var arr = nm.array[nm.f64]([1.0, 2.0, 3.0], shape=[3])
print(less_equal[nm.f64](arr, 2.0))  # Output: [True, True, False]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The dtype of the input NDArray.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: NDArray to compare.
- `scalar` (`Scalar[dtype]`) `[imm]`: Scalar value to compare against.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `equal`

<div class="overload-divider">Overload 1</div>

```mojo
def equal[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

Performs element-wise comparison to check if values in `array1` are equal to values in `array2`.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.logic.comparison import equal

var arr1 = nm.array[nm.f64]([1.0, 2.0, 3.0], shape=[3])
var arr2 = nm.array[nm.f64]([1.0, 2.5, 3.0], shape=[3])
print(equal[nm.f64](arr1, arr2))  # Output: [True, False, True]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The dtype of the input NDArray.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: First NDArray to compare.
- `array2` (`NDArray[dtype]`) `[imm]`: Second NDArray to compare.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def equal[dtype: DType](array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

Performs element-wise comparison to check if values in `array1` are equal to a scalar value.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.logic.comparison import equal

var arr = nm.array[nm.f64]([1.0, 2.0, 3.0], shape=[3])
print(equal[nm.f64](arr, 2.0))  # Output: [False, True, False]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The dtype of the input NDArray.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: NDArray to compare.
- `scalar` (`Scalar[dtype]`) `[imm]`: Scalar value to compare against.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `not_equal`

<div class="overload-divider">Overload 1</div>

```mojo
def not_equal[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

Performs element-wise comparison to check if values in `array1` are not equal to values in `array2`.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.logic.comparison import not_equal

var arr1 = nm.array[nm.f64]([1.0, 2.0, 3.0], shape=[3])
var arr2 = nm.array[nm.f64]([1.0, 2.5, 2.0], shape=[3])
print(not_equal[nm.f64](arr1, arr2))  # Output: [False, True, True]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The dtype of the input NDArray.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: First NDArray to compare.
- `array2` (`NDArray[dtype]`) `[imm]`: Second NDArray to compare.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def not_equal[dtype: DType](array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

Performs element-wise comparison to check if values in `array1` are not equal to a scalar value.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.logic.comparison import not_equal

var arr = nm.array[nm.f64]([1.0, 2.0, 3.0], shape=[3])
print(not_equal[nm.f64](arr, 2.0))  # Output: [True, False, True]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The dtype of the input NDArray.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: NDArray to compare.
- `scalar` (`Scalar[dtype]`) `[imm]`: Scalar value to compare against.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `allclose`

```mojo
def allclose[dtype: DType](a: NDArray[dtype], b: NDArray[dtype], rtol: Scalar[dtype] = 1.0000000000000001E-5, atol: Scalar[dtype] = 1.0E-8, equal_nan: Bool = False) -> Bool
```

Check if all elements of two NDArrays are equal within a given tolerance.

For each element pair (a_i, b_i), this function returns True if:
    abs(a_i - b_i) <= atol + rtol * abs(b_i)
for all elements. If `equal_nan` is True, NaN values at the same position are considered equal.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.routines.logic.comparison import allclose
var arr1 = nm.array[nm.f64]([1.0, 2.0, 3.0], shape=[3])
var arr2 = nm.array[nm.f64]([1.0, 2.00001, 2.99999], shape=[3])
print(allclose[nm.f64](arr1, arr2))  # Output: True.
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the array.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: First array to compare.
- `b` (`NDArray[dtype]`) `[imm]`: Second array to compare.
- `rtol` (`Scalar[dtype]`) `[imm]`: Relative tolerance. Default is 1e-5.
- `atol` (`Scalar[dtype]`) `[imm]`: Absolute tolerance. Default is 1e-8.
- `equal_nan` (`Bool`) `[imm]`: If True, NaNs at the same position are considered equal. Default is False.

<div class="prose-label">Returns</div>

- `Bool`

!!! failure "Raises"
    NumojoError: If the shapes of `a` and `b` do not match.


</div>

<div class="fn-card" markdown="1">

### `isclose`

```mojo
def isclose[dtype: DType](a: NDArray[dtype], b: NDArray[dtype], rtol: Scalar[dtype] = 1.0000000000000001E-5, atol: Scalar[dtype] = 1.0E-8, equal_nan: Bool = False) -> NDArray[DType.bool]
```

Perform element-wise comparison of two NDArrays to check if their values are equal within a given tolerance.

For each element pair (a_i, b_i), the result is True if:
    abs(a_i - b_i) <= atol + rtol * abs(b_i)
If `equal_nan` is True, NaN values at the same position are considered equal.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.routines.logic.comparison import isclose
var arr1 = nm.array[nm.f64]([1.0, 2.0, 3.0], shape=[3])
var arr2 = nm.array[nm.f64]([1.0, 2.00001, 2.99999], shape=[3])
print(isclose[nm.f64](arr1, arr2))  # Output: [True, True, True]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the array.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: First array to compare.
- `b` (`NDArray[dtype]`) `[imm]`: Second array to compare.
- `rtol` (`Scalar[dtype]`) `[imm]`: Relative tolerance. Default is 1e-5.
- `atol` (`Scalar[dtype]`) `[imm]`: Absolute tolerance. Default is 1e-8.
- `equal_nan` (`Bool`) `[imm]`: If True, NaNs at the same position are considered equal. Default is False.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"
    NumojoError: If the shapes of `a` and `b` do not match.


</div>

<div class="fn-card" markdown="1">

### `array_equal`

```mojo
def array_equal[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> Bool
```

Determine whether two NDArrays are exactly equal in both shape and element values.

This function compares the shapes of `array1` and `array2`, and then checks each element for equality.
The arrays are considered equal only if their shapes match and all corresponding elements are equal.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.logic.comparison import array_equal

var arr = nm.arange[i32](0, 10)
var arr2 = nm.arange[i32](0, 10)
print(array_equal[i32](arr, arr2))  # Output: True
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Data type of the array.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: First NDArray to compare.
- `array2` (`NDArray[dtype]`) `[imm]`: Second NDArray to compare.

<div class="prose-label">Returns</div>

- `Bool`

!!! failure "Raises"


</div>
