# `numojo.routines.bitwise`

Bitwise operations for integer arrays.

Element-wise bitwise operations (AND, OR, XOR, NOT/invert) for integer NDArrays.

Exports
-------
- `invert`: Bitwise NOT operation.

## Functions


<div class="fn-card" markdown="1">

### `invert`

```mojo
def invert[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_integral() or (dtype == DType.bool)
```

Element-wise invert of an array.

Examples:
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.bitwise import invert

var arr1 = nm.array[nm.i8]([1, 2, 3], shape=[3])
var result1 = invert(arr1) # result1 is [-2, -3, -4]

var arr2 = nm.array[nm.boolean]([True, False, True], shape=[3])
var result2 = invert(arr2) # result2 is [false, true, false
```

!!! info "Constraints"
    The array must be either a boolean or integral array.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>
