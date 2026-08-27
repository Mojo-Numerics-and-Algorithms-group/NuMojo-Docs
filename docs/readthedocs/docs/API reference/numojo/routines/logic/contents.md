# `numojo.routines.logic.contents`

Element properties and content checking for arrays.

Functions for checking element properties (NaN, infinite, finite) and array
contents (not SIMD due to bool bit packing issue).

Exports
-------
- `isinf`: Check for infinite elements.
- `isfinite`: Check for finite elements.
- `isnan`: Check for NaN elements.
- `isneginf`: Check for negative infinity.
- `isposinf`: Check for positive infinity.

## Functions


<div class="fn-card" markdown="1">

### `isinf`

```mojo
def isinf[dtype: DType](array: NDArray[dtype]) -> NDArray[DType.bool]
```

Checks if each element of the input array is infinite.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.contents import isinf

def main() raises:
    var arr = linspace(0, 10, 5)  # Example array: [0.0, 2.5, 5.0, 7.5, 10.0]
    print(isinf(arr))  # Output: [False, False, False, False, False]
```

**Parameters:**

- `dtype` (`DType`): Data type of the input array.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: Input array to check.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `isfinite`

```mojo
def isfinite[dtype: DType](array: NDArray[dtype]) -> NDArray[DType.bool]
```

Checks if each element of the input array is finite.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.contents import isfinite

def main() raises:
    var arr = nm.array[nm.f64]([1.0, Float64.MAX, Float64.MIN], shape=[3])
    print(isfinite(arr))  # Output: [True, True, True]
```

**Parameters:**

- `dtype` (`DType`): Data type of the input array.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: Input array to check.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `isnan`

```mojo
def isnan[dtype: DType](array: NDArray[dtype]) -> NDArray[DType.bool]
```

Checks if each element of the input array is NaN.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.contents import isnan

def main() raises:
    var arr = nm.array[nm.f64]([1.0, 0.0, Float64.MAX], shape=[3])
    print(isnan(arr))  # Output: [False, False, False]
```

**Parameters:**

- `dtype` (`DType`): Data type of the input array.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: Input array to check.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `isneginf`

```mojo
def isneginf[dtype: DType](array: NDArray[dtype]) -> NDArray[DType.bool]
```

Checks if each element of the input array is negative infinity.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.contents import isneginf

def main() raises:
    var arr = nm.array[nm.f64]([1.0, 0.0, -1.0], shape=[3])
    print(isneginf(arr))  # Output: [False, False, False]
```

**Parameters:**

- `dtype` (`DType`): Data type of the input array.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: Input array to check.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `isposinf`

```mojo
def isposinf[dtype: DType](array: NDArray[dtype]) -> NDArray[DType.bool]
```

Checks if each element of the input array is positive infinity.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.contents import isposinf

def main() raises:
    var arr = nm.array[nm.f64]([1.0, 0.0, -1.0], shape=[3])
    print(isposinf(arr))  # Output: [False, False, False]
```

**Parameters:**

- `dtype` (`DType`): Data type of the input array.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: Input array to check.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>
