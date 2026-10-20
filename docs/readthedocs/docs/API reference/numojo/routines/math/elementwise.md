# `numojo.routines.math.elementwise`

Common NumPy-compatible unary and binary mathematical operations.

Exports
-------
- `sign`, `square`, `negative`, `positive`: Unary operations.
- `power`: Element-wise exponentiation (also exported as `pow`).
- `fmax`, `fmin`: NaN-ignoring extrema.
- `fmod`: Remainder with the sign of the dividend.
- `rint`: Round floating-point values to the nearest integer.

## Functions


<div class="fn-card" markdown="1">

### `sign`

```mojo
def sign[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Return the element-wise indication of the sign of an array.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var values = nm.array[f64]("[-3.5, 0.0, 2.5]")
var result = nm.sign(values)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The input array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `square`

```mojo
def square[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Return the element-wise square of an array.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var values = nm.array[f64]("[-2.0, 0.0, 3.0]")
var result = nm.square(values)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The input array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `negative`

```mojo
def negative[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Return the numerical negative of each array element.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var values = nm.array[f64]("[-2.0, 0.0, 3.0]")
var result = nm.negative(values)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The input array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `positive`

```mojo
def positive[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Return the numerical positive of each array element.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var values = nm.array[f64]("[-2.0, 0.0, 3.0]")
var result = nm.positive(values)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The input array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `power`

<div class="overload-divider">Overload 1</div>

```mojo
def power[dtype: DType](base: NDArray[dtype], exponent: NDArray[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Raise each element in one array to the corresponding array exponent.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var base = nm.array[f64]("[2.0, 3.0, 4.0]")
var exponent = nm.array[f64]("[3.0, 2.0, 0.5]")
var result = nm.power(base, exponent)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `base` (`NDArray[dtype]`) `[imm]`: The base array.
- `exponent` (`NDArray[dtype]`) `[imm]`: The exponent array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def power[dtype: DType](base: NDArray[dtype], exponent: Scalar[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Raise each array element to a scalar exponent.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var base = nm.array[f64]("[2.0, 3.0, 4.0]")
var exponent: Scalar[f64] = 2.0
var result = nm.power(base, exponent)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `base` (`NDArray[dtype]`) `[imm]`: The base array.
- `exponent` (`Scalar[dtype]`) `[imm]`: The scalar exponent.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def power[dtype: DType](base: Scalar[dtype], exponent: NDArray[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Raise a scalar base to each exponent in an array.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var base: Scalar[f64] = 2.0
var exponent = nm.array[f64]("[1.0, 2.0, 3.0]")
var result = nm.power(base, exponent)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `base` (`Scalar[dtype]`) `[imm]`: The scalar base.
- `exponent` (`NDArray[dtype]`) `[imm]`: The exponent array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `fmax`

<div class="overload-divider">Overload 1</div>

```mojo
def fmax[dtype: DType](lhs: NDArray[dtype], rhs: NDArray[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Return the element-wise maximum while ignoring a single NaN.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var lhs = nm.array[f64]("[1.0, 5.0, 3.0]")
var rhs = nm.array[f64]("[2.0, 4.0, 6.0]")
var result = nm.fmax(lhs, rhs)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `lhs` (`NDArray[dtype]`) `[imm]`: The first input array.
- `rhs` (`NDArray[dtype]`) `[imm]`: The second input array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def fmax[dtype: DType](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Return the maximum of each array element and a scalar, ignoring NaN.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var values = nm.array[f64]("[1.0, 5.0, 3.0]")
var limit: Scalar[f64] = 4.0
var result = nm.fmax(values, limit)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The input array.
- `scalar` (`Scalar[dtype]`) `[imm]`: The scalar input.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def fmax[dtype: DType](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Return the maximum of a scalar and each array element, ignoring NaN.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var limit: Scalar[f64] = 4.0
var values = nm.array[f64]("[1.0, 5.0, 3.0]")
var result = nm.fmax(limit, values)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `scalar` (`Scalar[dtype]`) `[imm]`: The scalar input.
- `array` (`NDArray[dtype]`) `[imm]`: The input array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `fmin`

<div class="overload-divider">Overload 1</div>

```mojo
def fmin[dtype: DType](lhs: NDArray[dtype], rhs: NDArray[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Return the element-wise minimum while ignoring a single NaN.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var lhs = nm.array[f64]("[1.0, 5.0, 3.0]")
var rhs = nm.array[f64]("[2.0, 4.0, 6.0]")
var result = nm.fmin(lhs, rhs)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `lhs` (`NDArray[dtype]`) `[imm]`: The first input array.
- `rhs` (`NDArray[dtype]`) `[imm]`: The second input array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def fmin[dtype: DType](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Return the minimum of each array element and a scalar, ignoring NaN.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var values = nm.array[f64]("[1.0, 5.0, 3.0]")
var limit: Scalar[f64] = 4.0
var result = nm.fmin(values, limit)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The input array.
- `scalar` (`Scalar[dtype]`) `[imm]`: The scalar input.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def fmin[dtype: DType](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Return the minimum of a scalar and each array element, ignoring NaN.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var limit: Scalar[f64] = 4.0
var values = nm.array[f64]("[1.0, 5.0, 3.0]")
var result = nm.fmin(limit, values)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `scalar` (`Scalar[dtype]`) `[imm]`: The scalar input.
- `array` (`NDArray[dtype]`) `[imm]`: The input array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `fmod`

<div class="overload-divider">Overload 1</div>

```mojo
def fmod[dtype: DType](lhs: NDArray[dtype], rhs: NDArray[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Return the element-wise remainder with the dividend's sign.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var lhs = nm.array[f64]("[-7.5, 5.0, 7.5]")
var rhs = nm.array[f64]("[2.0, -2.0, 2.0]")
var result = nm.fmod(lhs, rhs)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `lhs` (`NDArray[dtype]`) `[imm]`: The dividend array.
- `rhs` (`NDArray[dtype]`) `[imm]`: The divisor array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def fmod[dtype: DType](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Return each array element modulo a scalar with the dividend's sign.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var values = nm.array[f64]("[-7.5, 5.0, 7.5]")
var divisor: Scalar[f64] = 2.0
var result = nm.fmod(values, divisor)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The dividend array.
- `scalar` (`Scalar[dtype]`) `[imm]`: The scalar divisor.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def fmod[dtype: DType](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_numeric()
```

Return a scalar modulo each array element with the dividend's sign.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var dividend: Scalar[f64] = 8.0
var divisors = nm.array[f64]("[3.0, -3.0, 5.0]")
var result = nm.fmod(dividend, divisors)
```

!!! info "Constraints"
    The element type must be numeric.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `scalar` (`Scalar[dtype]`) `[imm]`: The scalar dividend.
- `array` (`NDArray[dtype]`) `[imm]`: The divisor array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `rint`

```mojo
def rint[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Round each floating-point element to the nearest integer value.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var values = nm.array[f64]("[-2.5, -1.5, 1.5, 2.5]")
var result = nm.rint(values)
```

!!! info "Constraints"
    The element type must be floating point.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The input array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
