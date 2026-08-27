# `numojo.routines.math.exponents`

Exponential and logarithmic functions for arrays.

Element-wise exponential functions (exp, exp2, expm1) and logarithmic functions
(log, log2, log10, log1p) for NDArrays.

Exports
-------
- `exp`, `exp2`, `expm1`: Exponential functions.
- `log`, `log2`, `log10`, `log1p`: Logarithmic functions.

## Functions


<div class="fn-card" markdown="1">

### `exp`

#### Overload 1

```mojo
def exp[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Compute the element-wise exponential of an array.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *

var arr = nm.linspace[f64](0.0, 1.0, 10)
var result = nm.exp(arr)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def exp[dtype: DType](value: Scalar[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Compute the exponential of a scalar.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *

var value: Scalar[f32] = 1.0
var result = nm.exp(value)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `value` (`Scalar[dtype]`) `[imm]`: A Scalar.

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `exp2`

#### Overload 1

```mojo
def exp2[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Compute the element-wise base-2 exponential of an array.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *

var arr = nm.linspace[f64](0.0, 1.0, 10)
var result = nm.exp2(arr)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def exp2[dtype: DType](value: Scalar[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Compute the base-2 exponential of a scalar.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *

var value: Scalar[f32] = 1.0
var result = nm.exp2(value)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `value` (`Scalar[dtype]`) `[imm]`: A Scalar.

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `expm1`

#### Overload 1

```mojo
def expm1[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Compute the element-wise exp(x) - 1 of an array.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *
var arr = nm.linspace[f64](0.0, 1.0, 10)
var result = nm.expm1(arr)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def expm1[dtype: DType](value: Scalar[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Compute exp(value) - 1 for a scalar.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *
var value: Scalar[f32] = 1.0
var result = nm.expm1(value)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `value` (`Scalar[dtype]`) `[imm]`: A Scalar.

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `log`

#### Overload 1

```mojo
def log[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Compute the element-wise natural logarithm of an array.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *
var arr = nm.arange[f64](1.0, 10.0, 1.0)
var result = nm.log(arr)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def log[dtype: DType](value: Scalar[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Compute the natural logarithm of a scalar.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *

var result = nm.log(10.0)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `value` (`Scalar[dtype]`) `[imm]`: A Scalar.

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `log2`

#### Overload 1

```mojo
def log2[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Compute the element-wise base-2 logarithm of an array.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *

var arr = nm.arange[f64](1.0, 10.0, 1.0)
var result = nm.log2(arr)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def log2[dtype: DType](value: Scalar[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Compute the base-2 logarithm of a scalar.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *
var result = nm.log2(10.0)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `value` (`Scalar[dtype]`) `[imm]`: A Scalar.

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `log10`

#### Overload 1

```mojo
def log10[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Compute the element-wise base-10 logarithm of an array.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *
var arr = nm.arange[f64](1.0, 10.0, 1.0)
var result = nm.log10(arr)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def log10[dtype: DType](value: Scalar[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Compute the base-10 logarithm of a scalar.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *

var result = nm.log10(10.0)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `value` (`Scalar[dtype]`) `[imm]`: A Scalar.

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `log1p`

#### Overload 1

```mojo
def log1p[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Compute the element-wise ln(1 + x) of an array.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *

var arr = nm.linspace[f64](0.0, 1.0, 10)
var result = nm.log1p(arr)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def log1p[dtype: DType](value: Scalar[dtype]) -> Scalar[dtype] where dtype.is_floating_point()
```

Compute ln(1 + value) for a scalar.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *
var result = nm.log1p(1.0)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `value` (`Scalar[dtype]`) `[imm]`: A Scalar.

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"


</div>
