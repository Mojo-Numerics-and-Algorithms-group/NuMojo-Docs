# `numojo.core.complex.complex_simd`

ComplexSIMD (numojo.core.complex.complex_simd)

Implement the ComplexSIMD type and its operations.

This module provides a ComplexSIMD type that represents complex numbers using SIMD
operations for efficient computation. It supports basic arithmetic operations
like addition, subtraction, multiplication, and division, as well as other
complex number operations like conjugation and absolute value.

## Structs

### `ComplexSIMD`

```mojo
struct ComplexSIMD[cdtype: ComplexDType = ComplexDType.float64, width: Int = 1]
```

**Memory convention:** `register_passable_trivial`  
**Implements:** `AnyType`, `Copyable`, `ImplicitlyCopyable`, `ImplicitlyDestructible`, `Movable`, `RegisterPassable`, `Stringable`, `TrivialRegisterPassable`, `Writable`

A SIMD-enabled complex number container (SoA layout).

Fields:
    re: SIMD vector of real parts.
    im: SIMD vector of imaginary parts.

The parameter `cdtype` determines the component precision (e.g. cf32, cf64).
The parameter `width` is the SIMD lane count; when `width == 1` this acts like a scalar complex number.

Examples:
```mojo
from numojo.prelude import *
var a = ComplexSIMD[cf32](1.0, 2.0)
var b = ComplexSIMD[cf32](3.0, 4.0)
print(a + b)  # (4.0 + 6.0 j)

# SIMD width=2:
var a2 = ComplexSIMD[cf32, 2](
    SIMD[cf32.dtype, 2](1.0, 1.5),
    SIMD[cf32.dtype, 2](2.0, -0.5)
)
print(a2) # ( [1.0 2.0] + [1.5 -0.5]j )
```
Convenience factories:
    ComplexSIMD[cf64].zero()
    ComplexSIMD[cf64].one()
    ComplexSIMD[cf64].i()
    ComplexSIMD[cf64].from_polar(2.0, 0.5)

**Parameters:**

- `cdtype` (`ComplexDType`)
- `width` (`Int`)

#### Fields

- **`re`** (`SIMD[ComplexSIMD[cdtype, width].dtype, width]`)
- **`im`** (`SIMD[ComplexSIMD[cdtype, width].dtype, width]`)

#### Aliases

##### `dtype`

```mojo
comptime dtype
```

**Value:** `cdtype.dtype`

Component dtype (underlying real/imag dtype).

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `True`

##### `__move_ctor_is_trivial`

```mojo
comptime __move_ctor_is_trivial
```

**Value:** `True`

##### `__copy_ctor_is_trivial`

```mojo
comptime __copy_ctor_is_trivial
```

**Value:** `True`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
__init__(other: Self) -> Self
```

<span class="badge badge-static">static</span>

Copy constructor for ComplexSIMD.

Initializes a new ComplexSIMD instance by copying the values from another instance.

**Args:**

- `other` (`Self`)

**Returns:**

- `Self`

###### Overload 2

```mojo
__init__(re: SIMD[ComplexSIMD[cdtype, width].dtype, width], im: SIMD[ComplexSIMD[cdtype, width].dtype, width]) -> Self
```

<span class="badge badge-static">static</span>

Constructs a ComplexSIMD from SIMD vectors of real and imaginary parts.

**Args:**

- `re` (`SIMD`): SIMD vector containing the real components.
- `im` (`SIMD`): SIMD vector containing the imaginary components.

**Returns:**

- `Self`

###### Overload 3

```mojo
__init__(val: SIMD[ComplexSIMD[cdtype, width].dtype, width]) -> Self
```

<span class="badge badge-static">static</span>

Constructs a ComplexSIMD where both real and imaginary parts are set to the same SIMD value.

**Args:**

- `val` (`SIMD`): SIMD vector to broadcast to both real and imaginary components.

**Returns:**

- `Self`

###### Overload 4

```mojo
__init__(re: Int, im: Int) -> Self
```

<span class="badge badge-static">static</span>

Constructs a ComplexSIMD from scalar integer real and imaginary values, broadcasted to SIMD lanes.

**Args:**

- `re` (`Int`): Integer value for the real component.
- `im` (`Int`): Integer value for the imaginary component.

**Returns:**

- `Self`

###### Overload 5

```mojo
__init__(val: Int) -> Self
```

<span class="badge badge-static">static</span>

Constructs a ComplexSIMD where both real and imaginary parts are set to the same integer value broadcasted to SIMD lanes.

**Args:**

- `val` (`Int`): Integer value to broadcast to both real and imaginary components.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

```mojo
__getitem__(self, idx: Int) -> ComplexSIMD[cdtype]
```

Returns the complex number at the specified lane index.

Example:
```mojo
from numojo.prelude import *
var c_simd = ComplexSIMD[cf32, 2](SIMD[f32, 2](1, 2), SIMD[f32, 2](3, 4))
var c0 = c_simd[0]  # 1 + 3j
var c1 = c_simd[1]  # 2 + 4j
```

**Args:**

- `self` (`Self`)
- `idx` (`Int`): SIMD lane index (0 to width-1).

**Returns:**

- `ComplexSIMD`

!!! failure "Raises"
    Error if lane index is out of range for the SIMD width.


</div>

<div class="fn-card" markdown="1">

##### `__setitem__`

```mojo
__setitem__(mut self, idx: Int, value: ComplexSIMD[cdtype])
```

Sets the complex scalar at the specified lane index.

Example:
```mojo
from numojo.prelude import *
var c_simd = nm.ComplexSIMD[cf32, 2](SIMD[f32, 2](1, 2), SIMD[f32, 2](3, 4)) # [(1 + 3j), (2 + 4j)]
c_simd[0] = nm.CScalar[cf32](5, 6)
print(c_simd) # [(1 + 3j), (2 + 4j)] becomes [(5 + 6j), (2 + 4j)]
```

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Int`): SIMD lane index (0 to width-1).
- `value` (`ComplexSIMD`): ComplexScalar whose values will be assigned.

!!! failure "Raises"
    Error if lane index is out of range for the SIMD width.


</div>

<div class="fn-card" markdown="1">

##### `__neg__`

```mojo
__neg__(self) -> Self
```

Returns the negation of this ComplexSIMD.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__pos__`

```mojo
__pos__(self) -> Self
```

Returns the positive value of this ComplexSIMD (identity operation).

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__invert__`

```mojo
__invert__(self) -> Self where (cdtype == ComplexDType.bool) if (cdtype == ComplexDType.bool) else cdtype.is_integral()
```

Element-wise logical NOT operation on this ComplexSIMD instance.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

###### Overload 1

```mojo
__eq__(self, other: Self) -> Bool
```

Checks if two ComplexSIMD instances are exactly equal.

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Bool`

###### Overload 2

```mojo
__eq__(self, other: ImaginaryUnit) -> Bool
```

Checks if this ComplexSIMD instance is equal to the imaginary unit 1j.

Examples:
```mojo
from numojo.prelude import *

var z1 = ComplexSIMD[cf64, 1](0.0, 1.0)  # 0 + 1j
var z2 = ComplexSIMD[cf64, 1](1.0, 1.0)  # 1 + 1j
print(z1 == `1j`)  # True
print(z2 == `1j`)  # False
```

**Args:**

- `self` (`Self`)
- `other` (`ImaginaryUnit`): Imaginary unit (1j) to compare with this ComplexSIMD instance.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

###### Overload 1

```mojo
__ne__(self, other: Self) -> Bool
```

Checks if two ComplexSIMD instances are not equal.

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Bool`

###### Overload 2

```mojo
__ne__(self, other: ImaginaryUnit) -> Bool
```

Checks if this ComplexSIMD instance is not equal to the imaginary unit 1j.

Examples:
```mojo
from numojo.prelude import *

var z1 = ComplexSIMD[cf64, 1](0.0, 1.0)  # 0 + 1j
var z2 = ComplexSIMD[cf64, 1](1.0, 1.0)  # 1 + 1j
print(z1 != `1j`)  # False
print(z2 != `1j`)  # True
```

**Args:**

- `self` (`Self`)
- `other` (`ImaginaryUnit`): Imaginary unit (1j) to compare with this ComplexSIMD instance.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__add__`

###### Overload 1

```mojo
__add__(self, other: Self) -> Self
```

Returns the element-wise sum of two ComplexSIMD instances.

**Args:**

- `self` (`Self`)
- `other` (`Self`): Another ComplexSIMD instance.

**Returns:**

- `Self`

###### Overload 2

```mojo
__add__(self, other: Scalar[ComplexSIMD[cdtype, width].dtype]) -> Self
```

Returns the sum of this ComplexSIMD instance and a scalar added to the real part.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to add to the real component.

**Returns:**

- `Self`

###### Overload 3

```mojo
__add__(self, other: SIMD[other.dtype, width]) -> Self
```

Returns the sum of this ComplexSIMD instance and a SIMD vector added to the real part.

**Args:**

- `self` (`Self`)
- `other` (`SIMD`): SIMD vector to add to the real component.

**Returns:**

- `Self`

###### Overload 4

```mojo
__add__(self, other: ImaginaryUnit) -> Self
```

Returns the sum of this ComplexSIMD instance and the imaginary unit 1j.

Examples:
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
var result = z + `1j`  # 3 + 3j
print(result)  # (3 + 3j)
```

**Args:**

- `self` (`Self`)
- `other` (`ImaginaryUnit`): Imaginary unit (1j) to add to this complex number.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__sub__`

###### Overload 1

```mojo
__sub__(self, other: Self) -> Self
```

Returns the element-wise difference of two ComplexSIMD instances.

**Args:**

- `self` (`Self`)
- `other` (`Self`): Another ComplexSIMD instance.

**Returns:**

- `Self`

###### Overload 2

```mojo
__sub__(self, other: Scalar[ComplexSIMD[cdtype, width].dtype]) -> Self
```

Returns the difference of this ComplexSIMD instance and a scalar subtracted from the real part.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to subtract from the real component.

**Returns:**

- `Self`

###### Overload 3

```mojo
__sub__(self, other: SIMD[other.dtype, width]) -> Self
```

Returns the difference of this ComplexSIMD instance and a SIMD vector subtracted from the real part.

**Args:**

- `self` (`Self`)
- `other` (`SIMD`): SIMD vector to subtract from the real component.

**Returns:**

- `Self`

###### Overload 4

```mojo
__sub__(self, other: ImaginaryUnit) -> Self
```

Subtracts the imaginary unit 1j from this ComplexSIMD instance.

Examples:
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
var result = z - `1j`  # 3 + 1j
print(result)  # (3 + 1j)
```

**Args:**

- `self` (`Self`)
- `other` (`ImaginaryUnit`): Imaginary unit (1j) to subtract from this complex number.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__mul__`

###### Overload 1

```mojo
__mul__(self, other: Self) -> Self
```

Returns the element-wise product of two ComplexSIMD instances.

**Args:**

- `self` (`Self`)
- `other` (`Self`): Another ComplexSIMD instance.

**Returns:**

- `Self`

###### Overload 2

```mojo
__mul__(self, other: Scalar[ComplexSIMD[cdtype, width].dtype]) -> Self
```

Returns the product of this ComplexSIMD instance and a scalar.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to multiply with both real and imaginary parts.

**Returns:**

- `Self`

###### Overload 3

```mojo
__mul__(self, other: SIMD[other.dtype, width]) -> Self
```

Returns the product of this ComplexSIMD instance and a SIMD vector.

**Args:**

- `self` (`Self`)
- `other` (`SIMD`): SIMD vector to multiply with both real and imaginary parts.

**Returns:**

- `Self`

###### Overload 4

```mojo
__mul__(self, other: ImaginaryUnit) -> Self
```

Returns the product of this ComplexSIMD instance and the imaginary unit 1j.

Examples:
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
var result = z * `1j`  # -2 + 3j
print(result)  # (-2 + 3j)
```

**Args:**

- `self` (`Self`)
- `other` (`ImaginaryUnit`): Imaginary unit (1j) to multiply with this complex number.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__truediv__`

###### Overload 1

```mojo
__truediv__(self, other: Self) -> Self
```

Performs element-wise complex division of two ComplexSIMD instances.

**Args:**

- `self` (`Self`)
- `other` (`Self`): Another ComplexSIMD instance to divide by.

**Returns:**

- `Self`

###### Overload 2

```mojo
__truediv__(self, other: Scalar[ComplexSIMD[cdtype, width].dtype]) -> Self
```

Performs element-wise division of this ComplexSIMD instance by a scalar.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to divide both real and imaginary parts by.

**Returns:**

- `Self`

###### Overload 3

```mojo
__truediv__(self, other: SIMD[other.dtype, width]) -> Self
```

Performs element-wise division of this ComplexSIMD instance by a SIMD vector.

**Args:**

- `self` (`Self`)
- `other` (`SIMD`): SIMD vector to divide both real and imaginary parts by.

**Returns:**

- `Self`

###### Overload 4

```mojo
__truediv__(self, other: ImaginaryUnit) -> Self
```

Performs division of this ComplexSIMD instance by the imaginary unit 1j.

Examples:
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
var result = z / `1j`  # 2 - 3j
print(result)  # (2 - 3j)
```

**Args:**

- `self` (`Self`)
- `other` (`ImaginaryUnit`): Imaginary unit (1j) to divide this complex number by.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__pow__`

```mojo
__pow__(self, n: Int) -> Self
```

Raises this ComplexSIMD to an integer.

**Args:**

- `self` (`Self`)
- `n` (`Int`): Integer exponent.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__and__`

```mojo
__and__(self, other: Self) -> Self where (cdtype == ComplexDType.bool) if (cdtype == ComplexDType.bool) else cdtype.is_integral()
```

Element-wise logical AND operation between two ComplexSIMD instances.

**Args:**

- `self` (`Self`)
- `other` (`Self`): Another ComplexSIMD instance.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__or__`

```mojo
__or__(self, other: Self) -> Self where (cdtype == ComplexDType.bool) if (cdtype == ComplexDType.bool) else cdtype.is_integral()
```

Element-wise logical OR operation between two ComplexSIMD instances.

**Args:**

- `self` (`Self`)
- `other` (`Self`): Another ComplexSIMD instance.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__xor__`

```mojo
__xor__(self, other: Self) -> Self where (cdtype == ComplexDType.bool) if (cdtype == ComplexDType.bool) else cdtype.is_integral()
```

Element-wise logical XOR operation between two ComplexSIMD instances.

**Args:**

- `self` (`Self`)
- `other` (`Self`): Another ComplexSIMD instance.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__radd__`

###### Overload 1

```mojo
__radd__(self, other: Scalar[ComplexSIMD[cdtype, width].dtype]) -> Self
```

Returns the sum of a scalar and this ComplexSIMD instance, adding to the real part.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to add to the real component.

**Returns:**

- `Self`

###### Overload 2

```mojo
__radd__(self, other: SIMD[other.dtype, width]) -> Self
```

Returns the sum of a SIMD vector and this ComplexSIMD instance, adding to the real part.

**Args:**

- `self` (`Self`)
- `other` (`SIMD`): SIMD vector to add to the real component.

**Returns:**

- `Self`

###### Overload 3

```mojo
__radd__(self, other: ImaginaryUnit) -> Self
```

Returns the sum of the imaginary unit 1j and this ComplexSIMD instance.

Examples:
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
var result = `1j` + z  # 3 + 3j
print(result)  # (3 + 3j)
```

**Args:**

- `self` (`Self`)
- `other` (`ImaginaryUnit`): Imaginary unit (1j) to add to this complex number.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__rsub__`

###### Overload 1

```mojo
__rsub__(self, other: Scalar[ComplexSIMD[cdtype, width].dtype]) -> Self
```

Returns the difference of a scalar and this ComplexSIMD instance, subtracting from the real part.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to subtract from the real component.

**Returns:**

- `Self`

###### Overload 2

```mojo
__rsub__(self, other: SIMD[other.dtype, width]) -> Self
```

Returns the difference of a SIMD vector and this ComplexSIMD instance, subtracting from the real part.

**Args:**

- `self` (`Self`)
- `other` (`SIMD`): SIMD vector to subtract from the real component.

**Returns:**

- `Self`

###### Overload 3

```mojo
__rsub__(self, other: ImaginaryUnit) -> Self
```

Returns the difference of the imaginary unit 1j and this ComplexSIMD instance.

Examples:
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
var result = `1j` - z  # -3 + (-1)j = -3 - 1j
print(result)  # (-3 - 1j)
```

**Args:**

- `self` (`Self`)
- `other` (`ImaginaryUnit`): Imaginary unit (1j) from which this complex number is subtracted.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__rmul__`

###### Overload 1

```mojo
__rmul__(self, other: Scalar[ComplexSIMD[cdtype, width].dtype]) -> Self
```

Returns the product of a scalar and this ComplexSIMD instance.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to multiply with both real and imaginary parts.

**Returns:**

- `Self`

###### Overload 2

```mojo
__rmul__(self, other: SIMD[other.dtype, width]) -> Self
```

Returns the product of a SIMD vector and this ComplexSIMD instance.

**Args:**

- `self` (`Self`)
- `other` (`SIMD`): SIMD vector to multiply with both real and imaginary parts.

**Returns:**

- `Self`

###### Overload 3

```mojo
__rmul__(self, other: ImaginaryUnit) -> Self
```

Returns the product of the imaginary unit 1j and this ComplexSIMD instance.

Examples:
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
var result = `1j` * z  # -2 + 3j
print(result)  # (-2 + 3j)
```

**Args:**

- `self` (`Self`)
- `other` (`ImaginaryUnit`): Imaginary unit (1j) to multiply with this complex number.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__rtruediv__`

###### Overload 1

```mojo
__rtruediv__(self, other: Scalar[ComplexSIMD[cdtype, width].dtype]) -> Self
```

Performs element-wise division of a scalar by this ComplexSIMD instance.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to be divided by this ComplexSIMD instance.

**Returns:**

- `Self`

###### Overload 2

```mojo
__rtruediv__(self, other: SIMD[other.dtype, width]) -> Self
```

Performs element-wise division of a SIMD vector by this ComplexSIMD instance.

**Args:**

- `self` (`Self`)
- `other` (`SIMD`): SIMD vector to be divided by this ComplexSIMD instance.

**Returns:**

- `Self`

###### Overload 3

```mojo
__rtruediv__(self, other: ImaginaryUnit) -> Self
```

Performs division of the imaginary unit 1j by this ComplexSIMD instance.

Examples:
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 4.0)  # 3 + 4j
var result = `1j` / z  # 1j / (3 + 4j) = 0.16 - 0.12j
print(result)  # (0.16 - 0.12j)
```

**Args:**

- `self` (`Self`)
- `other` (`ImaginaryUnit`): Imaginary unit (1j) to be divided by this ComplexSIMD instance.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__iadd__`

###### Overload 1

```mojo
__iadd__(mut self, other: Self)
```

In-place addition of another ComplexSIMD instance.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`): Another ComplexSIMD instance.

###### Overload 2

```mojo
__iadd__(mut self, other: Scalar[ComplexSIMD[cdtype, width].dtype])
```

In-place addition of a scalar to the real part of this ComplexSIMD instance.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`): Scalar value to add to the real component.

###### Overload 3

```mojo
__iadd__(mut self, other: SIMD[other.dtype, width])
```

In-place addition of a SIMD vector to the real part of this ComplexSIMD instance.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`SIMD`): SIMD vector to add to the real component.

###### Overload 4

```mojo
__iadd__(mut self, other: ImaginaryUnit)
```

In-place addition of the imaginary unit 1j to this ComplexSIMD instance.

Examples:
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
z += `1j`  # Now z = 3 + 3j
print(z)  # (3 + 3j)
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`ImaginaryUnit`): Imaginary unit (1j) to add to this complex number.


</div>

<div class="fn-card" markdown="1">

##### `__isub__`

###### Overload 1

```mojo
__isub__(mut self, other: Self)
```

In-place subtraction of another ComplexSIMD instance.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`): Another ComplexSIMD instance.

###### Overload 2

```mojo
__isub__(mut self, other: Scalar[ComplexSIMD[cdtype, width].dtype])
```

In-place subtraction of a scalar from the real part of this ComplexSIMD instance.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`): Scalar value to subtract from the real component.

###### Overload 3

```mojo
__isub__(mut self, other: SIMD[other.dtype, width])
```

In-place subtraction of a SIMD vector from the real part of this ComplexSIMD instance.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`SIMD`): SIMD vector to subtract from the real component.

###### Overload 4

```mojo
__isub__(mut self, other: ImaginaryUnit)
```

In-place subtraction of the imaginary unit 1j from this ComplexSIMD instance.

Examples:
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
z -= `1j`  # Now z = 3 + 1j
print(z)  # (3 + 1j)
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`ImaginaryUnit`): Imaginary unit (1j) to subtract from this complex number.


</div>

<div class="fn-card" markdown="1">

##### `__imul__`

###### Overload 1

```mojo
__imul__(mut self, other: Self)
```

In-place complex multiplication with another ComplexSIMD instance.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`): Another ComplexSIMD instance.

###### Overload 2

```mojo
__imul__(mut self, other: Scalar[ComplexSIMD[cdtype, width].dtype])
```

In-place multiplication of this ComplexSIMD instance by a scalar.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`): Scalar value to multiply with both real and imaginary parts.

###### Overload 3

```mojo
__imul__(mut self, other: SIMD[other.dtype, width])
```

In-place multiplication of this ComplexSIMD instance by a SIMD vector.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`SIMD`): SIMD vector to multiply with both real and imaginary parts.

###### Overload 4

```mojo
__imul__(mut self, other: ImaginaryUnit)
```

In-place multiplication of this ComplexSIMD instance by the imaginary unit 1j.

Examples:
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
z *= `1j`  # Now z = -2 + 3j
print(z)  # (-2 + 3j)
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`ImaginaryUnit`): Imaginary unit (1j) to multiply with this complex number.


</div>

<div class="fn-card" markdown="1">

##### `__itruediv__`

###### Overload 1

```mojo
__itruediv__(mut self, other: Self)
```

Performs in-place element-wise complex division of self by another ComplexSIMD instance.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`): Another ComplexSIMD instance to divide by.

###### Overload 2

```mojo
__itruediv__(mut self, other: Scalar[ComplexSIMD[cdtype, width].dtype])
```

Performs in-place element-wise division of this ComplexSIMD instance by a scalar.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`): Scalar value to divide both real and imaginary parts by.

###### Overload 3

```mojo
__itruediv__(mut self, other: SIMD[other.dtype, width])
```

Performs in-place element-wise division of this ComplexSIMD instance by a SIMD vector.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`SIMD`): SIMD vector to divide both real and imaginary parts by.

###### Overload 4

```mojo
__itruediv__(mut self, other: ImaginaryUnit)
```

Performs in-place division of this ComplexSIMD instance by the imaginary unit 1j.

Examples:
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
z /= `1j`  # Now z = 2 - 3j
print(z)  # (2 - 3j)
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`ImaginaryUnit`): Imaginary unit (1j) to divide this complex number by.


</div>

<div class="fn-card" markdown="1">

##### `zero`

```mojo
zero() -> Self
```

<span class="badge badge-static">static</span>

Returns a ComplexSIMD instance with all real and imaginary components set to zero.

Example:
```mojo
from numojo.prelude import *
var comp = ComplexSIMD[cf64].zero()  # (0 + 0j)
```

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `one`

```mojo
one() -> Self
```

<span class="badge badge-static">static</span>

Returns a ComplexSIMD instance representing the complex number 1 + 0j.

Example:
```mojo
from numojo.prelude import *
var comp = ComplexSIMD[cf64].one()  # (1 + 0j)
```

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `i`

```mojo
i() -> Self
```

<span class="badge badge-static">static</span>

Returns a ComplexSIMD instance representing the imaginary unit 0 + 1j.

Examples:
```mojo
from numojo.prelude import *

# Create imaginary unit for different types
var i_f64 = ComplexSIMD[cf64].i()  # (0 + 1j)
var i_f32 = ComplexSIMD[cf32].i()  # (0 + 1j)
print(i_f64)  # (0 + 1j)

# Use in complex arithmetic
var z = 3.0 + 4.0 * ComplexSIMD[cf64].i()  # 3 + 4j
```

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `from_real_imag`

```mojo
from_real_imag(re: Scalar[ComplexSIMD[cdtype, width].dtype], im: Scalar[ComplexSIMD[cdtype, width].dtype]) -> Self
```

<span class="badge badge-static">static</span>

Constructs a ComplexSIMD instance from scalar real and imaginary values.

Example:
```mojo
from numojo.prelude import *
var comp = ComplexSIMD[cf64].from_real_imag(2.0, 3.0)  # (2.0 + 3.0j)
```

**Args:**

- `re` (`Scalar`): Scalar value for the real component.
- `im` (`Scalar`): Scalar value for the imaginary component.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `from_polar`

```mojo
from_polar(r: Scalar[ComplexSIMD[cdtype, width].dtype], theta: Scalar[ComplexSIMD[cdtype, width].dtype]) -> Self where ComplexSIMD[cdtype, width].dtype.is_floating_point()
```

<span class="badge badge-static">static</span>

Constructs a ComplexSIMD instance from polar coordinates.

Example:
```mojo
from numojo.prelude import *
var comp = ComplexSIMD[cf64].from_polar(2.0, 0.5)
```

**Args:**

- `r` (`Scalar`): Magnitude (radius).
- `theta` (`Scalar`): Angle (in radians).

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `reciprocal`

```mojo
reciprocal(self) -> Self
```

Returns the element-wise reciprocal (1 / self) of the ComplexSIMD instance.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `elem_pow`

###### Overload 1

```mojo
elem_pow(self, other: Self) -> Self
```

Raises each component of this ComplexSIMD to the power of the corresponding component in another ComplexSIMD.

**Args:**

- `self` (`Self`)
- `other` (`Self`): Another ComplexSIMD instance.

**Returns:**

- `Self`

###### Overload 2

```mojo
elem_pow(self, exponent: Scalar[ComplexSIMD[cdtype, width].dtype]) -> Self
```

Raises each component of this ComplexSIMD to a scalar exponent.

**Args:**

- `self` (`Self`)
- `exponent` (`Scalar`): Scalar exponent to apply to both real and imaginary parts.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `allclose`

```mojo
allclose(self, other: Self, *, rtol: Scalar[ComplexSIMD[cdtype, width].dtype] = 1.0000000000000001E-5, atol: Scalar[ComplexSIMD[cdtype, width].dtype] = 1.0E-8) -> Bool
```

Checks if two ComplexSIMD instances are approximately equal within given tolerances.

For each lane, compares the real and imaginary parts using the formula:
    abs(a - b) <= atol + rtol * abs(b)
where a and b are the corresponding components of self and other.

Note:
For SIMD width > 1, all lanes must satisfy the tolerance criteria.

**Args:**

- `self` (`Self`)
- `other` (`Self`): Another ComplexSIMD instance to compare against.
- `rtol` (`Scalar`): Relative tolerance.
- `atol` (`Scalar`): Absolute tolerance.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
__str__(self) -> String
```

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `write_to`

```mojo
write_to[W: Writer](self, mut writer: W)
```

Returns a string representation of the ComplexSIMD instance.

For width == 1, the format is: (re + im j).
For width > 1, the format is: [(re0 + im0 j), (re1 + im1 j), ...].

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

##### `__repr__`

```mojo
__repr__(self) -> String
```

Returns a string representation of the ComplexSIMD instance for debugging. `ComplexSIMD[dtype](re=<real SIMD>, im=<imag SIMD>)`.

**Args:**

- `self` (`Self`)

**Returns:**

- `String`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `item`

```mojo
item[name: String](self, idx: Int) -> Scalar[ComplexSIMD[cdtype, width].dtype]
```

Returns the scalar value for the specified lane index and component.

Example:
```mojo
from numojo.prelude import *
var c_simd = nm.ComplexSIMD[cf32, 2](SIMD[f32, 2](1, 2), SIMD[f32, 2](3, 4)) # [(1 + 3j), (2 + 4j)]
var re0 = c_simd.item["re"](0)  # 1.0
var im1 = c_simd.item["im"](1)  # 4.0
```

**Parameters:**

- `name` (`String`): Name of the component ('re' or 'im').

**Args:**

- `self` (`Self`)
- `idx` (`Int`): Lane index to retrieve.

**Returns:**

- `Scalar`

!!! failure "Raises"
    - Error if the component name is invalid.
- Error if lane index is out of range for the SIMD width.


</div>

<div class="fn-card" markdown="1">

##### `itemset`

```mojo
itemset[name: String](mut self, idx: Int, val: Scalar[ComplexSIMD[cdtype, width].dtype])
```

Sets the scalar value for the specified lane index and component.

Example:
```mojo
from numojo.prelude import *
var c_simd = nm.ComplexSIMD[cf32, 2](SIMD[f32, 2](1, 2), SIMD[f32, 2](3, 4)) # [(1 + 3j), (2 + 4j)]
c_simd.itemset["re"](0, 5.0)  # Now first complex number is (5 + 3j)
c_simd.itemset["im"](1, 6.0)  # Now second complex number is (2 + 6j)
```

**Parameters:**

- `name` (`String`): Name of the component ('re' or 'im').

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Int`): Lane index to set.
- `val` (`Scalar`): Scalar value to assign to the specified component.

!!! failure "Raises"
    - Error if the component name is invalid.
- Error if lane index is out of range for the SIMD width.


</div>

<div class="fn-card" markdown="1">

##### `real`

```mojo
real(self) -> SIMD[ComplexSIMD[cdtype, width].dtype, width]
```

Returns the real part(s) of the complex number(s).

**Args:**

- `self` (`Self`)

**Returns:**

- `SIMD`


</div>

<div class="fn-card" markdown="1">

##### `imag`

```mojo
imag(self) -> SIMD[ComplexSIMD[cdtype, width].dtype, width]
```

Returns the imaginary part(s) of the complex number(s).

**Args:**

- `self` (`Self`)

**Returns:**

- `SIMD`


</div>

<div class="fn-card" markdown="1">

##### `__abs__`

```mojo
__abs__(self) -> SIMD[ComplexSIMD[cdtype, width].dtype, width]
```

Returns the magnitude (absolute value) of the complex number(s).

**Args:**

- `self` (`Self`)

**Returns:**

- `SIMD`


</div>

<div class="fn-card" markdown="1">

##### `norm`

```mojo
norm(self) -> SIMD[ComplexSIMD[cdtype, width].dtype, width]
```

Returns the squared magnitude (norm) of the complex number(s).

**Args:**

- `self` (`Self`)

**Returns:**

- `SIMD`


</div>

<div class="fn-card" markdown="1">

##### `conj`

```mojo
conj(self) -> Self
```

Returns the complex conjugate of the ComplexSIMD instance.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`


</div>
### `ImaginaryUnit`

```mojo
struct ImaginaryUnit
```

**Memory convention:** `register_passable_trivial`  
**Implements:** `AnyType`, `Boolable`, `Copyable`, `ImplicitlyCopyable`, `ImplicitlyDestructible`, `Movable`, `RegisterPassable`, `Stringable`, `TrivialRegisterPassable`, `Writable`

Constant representing the imaginary unit complex number 0 + 1j.

The ImaginaryUnit struct provides a convenient way to work with the imaginary unit
in complex arithmetic operations. It supports arithmetic operations with SIMD vectors,
scalars, and other complex numbers, enabling Python-like syntax for complex number creation.

Examples:
```mojo
from numojo.prelude import *

# Create complex numbers using the imaginary unit
var z1 = 3 + 4 * `1j`  # 3 + 4j
var z2 = `1j` * 2      # 0 + 2j
var z3 = 5.0 + `1j`    # 5 + 1j

# Powers of the imaginary unit
print(`1j` ** 0)  # 1 + 0j
print(`1j` ** 1)  # 0 + 1j
print(`1j` ** 2)  # -1 + 0j
print(`1j` ** 3)  # 0 - 1j

# SIMD complex vectors
var c4 = SIMD[f32, 4](1.0) + `1j` * SIMD[f32, 4](2.0)  # ComplexSIMD[cf32, 4]
var c5 = SIMD[f64, 2](3.0, 4.0) + `1j`                 # ComplexSIMD[cf64, 2]
var d = SIMD[f32, 2](1) + SIMD[f32, 2](2) * `1j`         # creates [( 1 + 2 j) (1 + 2 j)]

# Mathematical properties
var c6 = `1j` * `1j`                     # -1 (Scalar[f64])
var c7 = `1j` ** 3                       # (0 - 1j) (ComplexScalar[cf64])
var c8 = (1 + `1j`) / `1j`               # (1 - 1j) (ComplexScalar[cf64])
```

#### Aliases

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `True`

##### `__move_ctor_is_trivial`

```mojo
comptime __move_ctor_is_trivial
```

**Value:** `True`

##### `__copy_ctor_is_trivial`

```mojo
comptime __copy_ctor_is_trivial
```

**Value:** `True`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
__init__() -> Self
```

<span class="badge badge-static">static</span>

Constructor for ImaginaryUnit.

Creates an instance representing the imaginary unit 1j.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__bool__`

```mojo
__bool__(self) -> Bool
```

Returns the boolean value of the imaginary unit.

Examples:
```mojo
from numojo.prelude import *

if `1j`:
    print("Imaginary unit is truthy")  # This will execute
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__neg__`

```mojo
__neg__(self) -> ComplexSIMD
```

Returns the negation of the imaginary unit: -1j.

Examples:
```mojo
from numojo.prelude import *

var result = -`1j`  # -1j
print(result)  # (0 - 1j)
```

**Args:**

- `self` (`Self`)

**Returns:**

- `ComplexSIMD`


</div>

<div class="fn-card" markdown="1">

##### `__add__`

###### Overload 1

```mojo
__add__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(dtype), width]
```

Returns the sum of the imaginary unit 1j and a SIMD vector.

Examples:
```mojo
from numojo.prelude import *

var vec = SIMD[DType.float32, 4](1.0, 2.0, 3.0, 4.0)
var result = `1j` + vec  # [1+1j, 2+1j, 3+1j, 4+1j]
```

**Parameters:**

- `dtype` (`DType`)
- `width` (`Int`)

**Args:**

- `self` (`Self`)
- `other` (`SIMD`): SIMD vector to add to the imaginary unit.

**Returns:**

- `ComplexSIMD`

###### Overload 2

```mojo
__add__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(dtype)]
```

Returns the sum of the imaginary unit 1j and a scalar.

Examples:
```mojo
from numojo.prelude import *

var result = `1j` + 3.5  # 3.5 + 1j
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar to add to the imaginary unit.

**Returns:**

- `ComplexSIMD`

###### Overload 3

```mojo
__add__(self, other: Int) -> ComplexSIMD[ComplexDType.int]
```

Returns the sum of the imaginary unit 1j and an integer.

Examples:
```mojo
from numojo.prelude import *

var result = `1j` + 5  # 5 + 1j
```

**Args:**

- `self` (`Self`)
- `other` (`Int`): Integer to add to the imaginary unit.

**Returns:**

- `ComplexSIMD`

###### Overload 4

```mojo
__add__(self, other: Self) -> ComplexSIMD
```

Returns the sum of the imaginary unit with itself: 1j + 1j = 2j.

Examples:
```mojo
from numojo.prelude import *

var result = `1j` + `1j`  # 2j
print(result)  # (0 + 2j)
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Another imaginary unit to add.

**Returns:**

- `ComplexSIMD`


</div>

<div class="fn-card" markdown="1">

##### `__sub__`

###### Overload 1

```mojo
__sub__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(dtype), width]
```

Returns the difference of the imaginary unit and a SIMD vector.

**Parameters:**

- `dtype` (`DType`)
- `width` (`Int`)

**Args:**

- `self` (`Self`)
- `other` (`SIMD`)

**Returns:**

- `ComplexSIMD`

###### Overload 2

```mojo
__sub__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(dtype)]
```

Returns the difference of the imaginary unit and a scalar.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `other` (`Scalar`)

**Returns:**

- `ComplexSIMD`

###### Overload 3

```mojo
__sub__(self, other: Int) -> ComplexSIMD[ComplexDType.int]
```

Returns the difference of the imaginary unit and an integer.

**Args:**

- `self` (`Self`)
- `other` (`Int`)

**Returns:**

- `ComplexSIMD`

###### Overload 4

```mojo
__sub__(self, other: Self) -> Float64
```

Returns the difference of the imaginary unit with itself: 1j - 1j = 0.

Examples:
```mojo
from numojo.prelude import *

var result = `1j` - `1j`  # 0
print(result)  # 0
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Another imaginary unit to subtract.

**Returns:**

- `Float64`


</div>

<div class="fn-card" markdown="1">

##### `__mul__`

###### Overload 1

```mojo
__mul__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(dtype), width]
```

**Parameters:**

- `dtype` (`DType`)
- `width` (`Int`)

**Args:**

- `self` (`Self`)
- `other` (`SIMD`)

**Returns:**

- `ComplexSIMD`

###### Overload 2

```mojo
__mul__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(dtype)]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `other` (`Scalar`)

**Returns:**

- `ComplexSIMD`

###### Overload 3

```mojo
__mul__(self, other: Int) -> ComplexSIMD[ComplexDType.int]
```

**Args:**

- `self` (`Self`)
- `other` (`Int`)

**Returns:**

- `ComplexSIMD`

###### Overload 4

```mojo
__mul__(self, other: Self) -> Float64
```

Returns the product of the imaginary unit with itself: 1j * 1j = -1.

Examples:
```mojo
from numojo.prelude import *

var result = `1j` * `1j`  # -1
print(result)  # -1
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Another imaginary unit to multiply with.

**Returns:**

- `Float64`


</div>

<div class="fn-card" markdown="1">

##### `__truediv__`

###### Overload 1

```mojo
__truediv__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(dtype), width]
```

Returns the division of the imaginary unit by a SIMD vector.

**Parameters:**

- `dtype` (`DType`)
- `width` (`Int`)

**Args:**

- `self` (`Self`)
- `other` (`SIMD`)

**Returns:**

- `ComplexSIMD`

###### Overload 2

```mojo
__truediv__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(dtype)]
```

Returns the division of the imaginary unit by a scalar.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `other` (`Scalar`)

**Returns:**

- `ComplexSIMD`

###### Overload 3

```mojo
__truediv__(self, other: Self) -> Float64
```

Returns the division of the imaginary unit by itself: 1j / 1j = 1.

Examples:
```mojo
from numojo.prelude import *

var result = `1j` / `1j`  # 1
print(result)  # 1
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Another imaginary unit to divide by.

**Returns:**

- `Float64`


</div>

<div class="fn-card" markdown="1">

##### `__pow__`

```mojo
__pow__(self, exponent: Int) -> ComplexSIMD
```

Returns the imaginary unit raised to an integer power.

The powers of 1j cycle with period 4:
- 1j^0 = 1
- 1j^1 = 1j
- 1j^2 = -1
- 1j^3 = -1j
- 1j^4 = 1 (cycle repeats)

Examples:
```mojo
from numojo.prelude import *

print(`1j` ** 0)  # (1 + 0j)
print(`1j` ** 1)  # (0 + 1j)
print(`1j` ** 2)  # (-1 + 0j)
print(`1j` ** 3)  # (0 - 1j)
print(`1j` ** 4)  # (1 + 0j)
```

**Args:**

- `self` (`Self`)
- `exponent` (`Int`): Integer exponent.

**Returns:**

- `ComplexSIMD`


</div>

<div class="fn-card" markdown="1">

##### `__radd__`

###### Overload 1

```mojo
__radd__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(dtype), width]
```

Returns the sum of a SIMD vector and the imaginary unit.

**Parameters:**

- `dtype` (`DType`)
- `width` (`Int`)

**Args:**

- `self` (`Self`)
- `other` (`SIMD`)

**Returns:**

- `ComplexSIMD`

###### Overload 2

```mojo
__radd__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(dtype)]
```

Returns the sum of a scalar and the imaginary unit.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `other` (`Scalar`)

**Returns:**

- `ComplexSIMD`

###### Overload 3

```mojo
__radd__(self, other: Int) -> ComplexSIMD[ComplexDType.int]
```

Returns the sum of an integer and the imaginary unit.

**Args:**

- `self` (`Self`)
- `other` (`Int`)

**Returns:**

- `ComplexSIMD`


</div>

<div class="fn-card" markdown="1">

##### `__rsub__`

###### Overload 1

```mojo
__rsub__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(dtype), width]
```

Returns the difference of a SIMD vector and the imaginary unit.

**Parameters:**

- `dtype` (`DType`)
- `width` (`Int`)

**Args:**

- `self` (`Self`)
- `other` (`SIMD`)

**Returns:**

- `ComplexSIMD`

###### Overload 2

```mojo
__rsub__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(dtype)]
```

Returns the difference of a scalar and the imaginary unit.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `other` (`Scalar`)

**Returns:**

- `ComplexSIMD`

###### Overload 3

```mojo
__rsub__(self, other: Int) -> ComplexSIMD[ComplexDType.int]
```

Returns the difference of an integer and the imaginary unit.

**Args:**

- `self` (`Self`)
- `other` (`Int`)

**Returns:**

- `ComplexSIMD`


</div>

<div class="fn-card" markdown="1">

##### `__rmul__`

###### Overload 1

```mojo
__rmul__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(dtype), width]
```

**Parameters:**

- `dtype` (`DType`)
- `width` (`Int`)

**Args:**

- `self` (`Self`)
- `other` (`SIMD`)

**Returns:**

- `ComplexSIMD`

###### Overload 2

```mojo
__rmul__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(dtype)]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `other` (`Scalar`)

**Returns:**

- `ComplexSIMD`

###### Overload 3

```mojo
__rmul__(self, other: Int) -> ComplexSIMD[ComplexDType.int]
```

**Args:**

- `self` (`Self`)
- `other` (`Int`)

**Returns:**

- `ComplexSIMD`


</div>

<div class="fn-card" markdown="1">

##### `__rtruediv__`

###### Overload 1

```mojo
__rtruediv__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(dtype), width]
```

Returns the division of a SIMD vector by the imaginary unit.

**Parameters:**

- `dtype` (`DType`)
- `width` (`Int`)

**Args:**

- `self` (`Self`)
- `other` (`SIMD`): SIMD vector to be divided by the imaginary unit.

**Returns:**

- `ComplexSIMD`

###### Overload 2

```mojo
__rtruediv__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(dtype)]
```

Returns the division of a scalar by the imaginary unit.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar to be divided by the imaginary unit.

**Returns:**

- `ComplexSIMD`

###### Overload 3

```mojo
__rtruediv__(self, other: Int) -> ComplexSIMD[ComplexDType.int]
```

Returns the division of an integer by the imaginary unit.

**Args:**

- `self` (`Self`)
- `other` (`Int`): Integer to be divided by the imaginary unit.

**Returns:**

- `ComplexSIMD`


</div>

<div class="fn-card" markdown="1">

##### `conj`

```mojo
conj(self) -> ComplexSIMD
```

Returns the complex conjugate of the imaginary unit.

Examples:
```mojo
from numojo.prelude import *

var conj_i = `1j`.conj()  # -1j
print(conj_i)  # (0 - 1j)
```

**Args:**

- `self` (`Self`)

**Returns:**

- `ComplexSIMD`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
__str__(self) -> String
```

Returns the string representation of the imaginary unit.

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `write_to`

```mojo
write_to[W: Writer](self, mut writer: W)
```

Writes the string representation of the imaginary unit to a writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`: Writer instance to write the string representation to.


</div>
