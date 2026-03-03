# `numojo.routines.logic.comparison`

Comparison routines (numojo.routines.logic.comparison)

Implements comparison math routines for NDArrays and Matrices.

## Functions


<div class="fn-card" markdown="1">

### `greater`

#### Overload 1

```mojo
greater[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

Performs element-wise check of whether values in x are greater than values in y.

A NDArray containing True if the corresponding element in x is greater than the corresponding element in y, otherwise False.

An element of the result NDArray will be True if the corresponding element in x is greater than the corresponding element in y, and False otherwise.

**Parameters:**

- `dtype` (`DType`): The dtype of the input NDArray.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): First NDArray to compare.
- `array2` (`NDArray`): Second NDArray to compare.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
greater[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

Performs element-wise check of whether values in x are greater than a scalar.

A NDArray containing True if the element in x is greater than the scalar, otherwise False.

An element of the result NDArray will be True if the element in x is greater than the scalar, and False otherwise.

**Parameters:**

- `dtype` (`DType`): The dtype of the input NDArray.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): First NDArray to compare.
- `scalar` (`Scalar`): Scalar to compare.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `greater_equal`

#### Overload 1

```mojo
greater_equal[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

Performs element-wise check of whether values in x are greater than or equal to values in y.

A NDArray containing True if the corresponding element in x is greater than or equal to the corresponding element in y, otherwise False.

An element of the result NDArray will be True if the corresponding element in x is greater than or equal to the corresponding element in y, and False otherwise.

**Parameters:**

- `dtype` (`DType`): The dtype of the input NDArray.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): First NDArray to compare.
- `array2` (`NDArray`): Second NDArray to compare.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
greater_equal[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

Performs element-wise check of whether values in x are greater than or equal to a scalar.

A NDArray containing True if the element in x is greater than or equal to the scalar, otherwise False.

An element of the result NDArray will be True if the element in x is greater than or equal to the scalar, and False otherwise.

**Parameters:**

- `dtype` (`DType`): The dtype of the input NDArray.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): First NDArray to compare.
- `scalar` (`Scalar`): Scalar to compare.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `less`

#### Overload 1

```mojo
less[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

Performs element-wise check of whether values in x are to values in y.

A NDArray containing True if the corresponding element in x is or equal to the corresponding element in y, otherwise False.

An element of the result NDArray will be True if the corresponding element in x is or equal to the corresponding element in y, and False otherwise.

**Parameters:**

- `dtype` (`DType`): The dtype of the input NDArray.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): First NDArray to compare.
- `array2` (`NDArray`): Second NDArray to compare.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
less[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

Performs element-wise check of whether values in x are to a scalar.

A NDArray containing True if the element in x is or equal to the scalar, otherwise False.

An element of the result NDArray will be True if the element in x is or equal to the scalar, and False otherwise.

**Parameters:**

- `dtype` (`DType`): The dtype of the input NDArray.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): First NDArray to compare.
- `scalar` (`Scalar`): Scalar to compare.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `less_equal`

#### Overload 1

```mojo
less_equal[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

Performs element-wise check of whether values in x are less than or equal to values in y.

A NDArray containing True if the corresponding element in x is less than or equal to the corresponding element in y, otherwise False.

An element of the result NDArray will be True if the corresponding element in x is less than or equal to the corresponding element in y, and False otherwise.

**Parameters:**

- `dtype` (`DType`): The dtype of the input NDArray.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): First NDArray to compare.
- `array2` (`NDArray`): Second NDArray to compare.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
less_equal[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

Performs element-wise check of whether values in x are less than or equal to a scalar.

A NDArray containing True if the element in x is less than or equal to the scalar, otherwise False.

An element of the result NDArray will be True if the element in x is less than or equal to the scalar, and False otherwise.

**Parameters:**

- `dtype` (`DType`): The dtype of the input NDArray.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): First NDArray to compare.
- `scalar` (`Scalar`): Scalar to compare.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `equal`

#### Overload 1

```mojo
equal[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

Performs element-wise check of whether values in x are equal to values in y.

A NDArray containing True if the corresponding element in x is equal to the corresponding element in y, otherwise False.

An element of the result NDArray will be True if the corresponding element in x is equal to the corresponding element in y, and False otherwise.

**Parameters:**

- `dtype` (`DType`): The dtype of the input NDArray.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): First NDArray to compare.
- `array2` (`NDArray`): Second NDArray to compare.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
equal[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

Performs element-wise check of whether values in x are equal to a scalar.

A NDArray containing True if the element in x is equal to the scalar, otherwise False.

An element of the result NDArray will be True if the element in x is equal to the scalar, and False otherwise.

**Parameters:**

- `dtype` (`DType`): The dtype of the input NDArray.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): First NDArray to compare.
- `scalar` (`Scalar`): Scalar to compare.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `not_equal`

#### Overload 1

```mojo
not_equal[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

Performs element-wise check of whether values in x are not equal to values in y.

A NDArray containing True if the corresponding element in x is not equal to the corresponding element in y, otherwise False.

An element of the result NDArray will be True if the corresponding element in x is not equal to the corresponding element in y, and False otherwise.

**Parameters:**

- `dtype` (`DType`): The dtype of the input NDArray.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): First NDArray to compare.
- `array2` (`NDArray`): Second NDArray to compare.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
not_equal[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

Performs element-wise check of whether values in x are not equal to values in y.

A NDArray containing True if the element in x is not equal to the scalar, otherwise False.

An element of the result NDArray will be True if the element in x is not equal to the scalar, and False otherwise.

**Parameters:**

- `dtype` (`DType`): The dtype of the input NDArray.
- `backend` (`Backend`): Sets utility function origin, defaults to `Vectorized.

**Args:**

- `array1` (`NDArray`): First NDArray to compare.
- `scalar` (`Scalar`): Scalar to compare.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `allclose`

#### Overload 1

```mojo
allclose[dtype: DType](a: NDArray[dtype], b: NDArray[dtype], rtol: Scalar[dtype] = 1.0000000000000001E-5, atol: Scalar[dtype] = 1.0E-8, equal_nan: Bool = False) -> Bool
```

Determines whether two NDArrays are element-wise equal within a specified tolerance.

This function compares each element of `a` and `b` and returns True if all corresponding elements satisfy the condition:
    abs(a_i - b_i) <= atol + rtol * abs(b_i)
Optionally, if `equal_nan` is True, NaN values at the same positions are considered equal.

Example:
```mojo
import numojo as nm
from numojo.routines.logic.comparison import allclose
var arr1 = nm.array[nm.f32]([1.0, 2.0, 3.0])
var arr2 = nm.array[nm.f32]([1.0, 2.00001, 2.99999])
print(allclose[nm.f32](arr1, arr2))  # Output: True
```

**Parameters:**

- `dtype` (`DType`): The data type of the input NDArray.

**Args:**

- `a` (`NDArray`): First NDArray to compare.
- `b` (`NDArray`): Second NDArray to compare.
- `rtol` (`Scalar`): Relative tolerance (default: 1e-5). The maximum allowed difference, relative to the magnitude of `b`.
- `atol` (`Scalar`): Absolute tolerance (default: 1e-8). The minimum absolute difference allowed.
- `equal_nan` (`Bool`): If True, NaNs in the same position are considered equal (default: False).

**Returns:**

- `Bool`

!!! failure "Raises"

#### Overload 2

```mojo
allclose[dtype: DType](a: Matrix[dtype], b: Matrix[dtype], rtol: Scalar[dtype] = 1.0000000000000001E-5, atol: Scalar[dtype] = 1.0E-8, equal_nan: Bool = False) -> Bool
```

Determines whether two Matrix are element-wise equal within a specified tolerance.

This function compares each element of `a` and `b` and returns True if all corresponding elements satisfy the condition:
    abs(a_i - b_i) <= atol + rtol * abs(b_i)
Optionally, if `equal_nan` is True, NaN values at the same positions are considered equal.

Example:
```mojo
from numojo.prelude import *
from numojo.routines.logic.comparison import allclose
var mat1 = Matrix.rand[f32]((2, 2))
var mat2 = Matrix.rand[f32]((2, 2))
print(allclose[f32](mat1, mat2))  # Output: True
```

**Parameters:**

- `dtype` (`DType`): The data type of the input Matrix.

**Args:**

- `a` (`Matrix`): First Matrix to compare.
- `b` (`Matrix`): Second Matrix to compare.
- `rtol` (`Scalar`): Relative tolerance (default: 1e-5). The maximum allowed difference, relative to the magnitude of `b`.
- `atol` (`Scalar`): Absolute tolerance (default: 1e-8). The minimum absolute difference allowed.
- `equal_nan` (`Bool`): If True, NaNs in the same position are considered equal (default: False).

**Returns:**

- `Bool`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `isclose`

#### Overload 1

```mojo
isclose[dtype: DType](a: NDArray[dtype], b: NDArray[dtype], rtol: Scalar[dtype] = 1.0000000000000001E-5, atol: Scalar[dtype] = 1.0E-8, equal_nan: Bool = False) -> NDArray[DType.bool]
```

Performs element-wise comparison of two NDArrays to determine if their values are equal within a specified tolerance.

For each element pair (a_i, b_i), the result is True if:
    abs(a_i - b_i) <= atol + rtol * abs(b_i)
Optionally, if `equal_nan` is True, NaN values at the same positions are considered equal.

Example:
```mojo
import numojo as nm
from numojo.routines.logic.comparison import isclose
var arr1 = nm.array[nm.f32]([1.0, 2.0, 3.0])
var arr2 = nm.array[nm.f32]([1.0, 2.00001, 2.99999])
print(isclose[nm.f32](arr1, arr2))  # Output: [True, True, True]
```

**Parameters:**

- `dtype` (`DType`): The data type of the input NDArray.

**Args:**

- `a` (`NDArray`): First NDArray to compare.
- `b` (`NDArray`): Second NDArray to compare.
- `rtol` (`Scalar`): Relative tolerance (default: 1e-5). The maximum allowed difference, relative to the magnitude of `b`.
- `atol` (`Scalar`): Absolute tolerance (default: 1e-8). The minimum absolute difference allowed.
- `equal_nan` (`Bool`): If True, NaNs in the same position are considered equal (default: False).

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
isclose[dtype: DType](a: Matrix[dtype], b: Matrix[dtype], rtol: Scalar[dtype] = 1.0000000000000001E-5, atol: Scalar[dtype] = 1.0E-8, equal_nan: Bool = False) -> Matrix[DType.bool]
```

Performs element-wise comparison of two Matrix to determine if their values are equal within a specified tolerance.

For each element pair (a_i, b_i), the result is True if:
    abs(a_i - b_i) <= atol + rtol * abs(b_i)
Optionally, if `equal_nan` is True, NaN values at the same positions are considered equal.

Example:
```mojo
from numojo.prelude import *
from numojo.routines.logic.comparison import isclose
var mat1 = Matrix.rand[f32]((2, 2))
var mat2 = Matrix.rand[f32]((2, 2))
print(isclose[f32](mat1, mat2))
```

**Parameters:**

- `dtype` (`DType`): The data type of the input Matrix.

**Args:**

- `a` (`Matrix`): First Matrix to compare.
- `b` (`Matrix`): Second Matrix to compare.
- `rtol` (`Scalar`): Relative tolerance (default: 1e-5). The maximum allowed difference, relative to the magnitude of `b`.
- `atol` (`Scalar`): Absolute tolerance (default: 1e-8). The minimum absolute difference allowed.
- `equal_nan` (`Bool`): If True, NaNs in the same position are considered equal (default: False).

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `array_equal`

```mojo
array_equal[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> Bool
```

Checks if two NDArrays are equal element-wise and shape-wise.

Examples:
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.logic.comparison import array_equal

var arr = nm.arange[i32](0, 10)
var arr2 = nm.arange[i32](0, 10)
print(array_equal[i32](arr, arr2))  # Output: True
```

**Parameters:**

- `dtype` (`DType`): The dtype of the input NDArray.

**Args:**

- `array1` (`NDArray`): First NDArray to compare.
- `array2` (`NDArray`): Second NDArray to compare.

**Returns:**

- `Bool`

!!! failure "Raises"


</div>
