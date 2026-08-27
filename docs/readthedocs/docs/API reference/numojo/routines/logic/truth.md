# `numojo.routines.logic.truth`

Truth value testing for arrays.

Functions for testing truth values (`all` and `any`) for NDArray types.

Exports
-------
- `all`: Test if all elements are truthy.
- `any`: Test if any element is truthy.

## Functions


<div class="fn-card" markdown="1">

### `all`

```mojo
def all(array: NDArray[DType.bool]) -> Scalar[DType.bool]
```

Checks whether all elements of the array evaluate to True.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.truth import all

var a = arange[i32](24).reshape(Shape(2, 3, 4))
var result = all(a > 5) # outputs False
```

**Args:**

- `array` (`NDArray[DType.bool]`) `[imm]`: Input NDArray (DType.bool).

**Returns:**

- `Scalar[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `any`

```mojo
def any(array: NDArray[DType.bool]) -> Scalar[DType.bool]
```

Checks whether any element of the array evaluate to True.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.truth import any

var a = arange[i32](24).reshape(Shape(2, 3, 4))
var result = any(a > 5) # outputs True
```

**Args:**

- `array` (`NDArray[DType.bool]`) `[imm]`: Input NDArray (DType.bool).

**Returns:**

- `Scalar[DType.bool]`

!!! failure "Raises"


</div>
