# `numojo.core.complex.complex_simd`

SIMD-optimized complex number representation and operations.

This module provides the ComplexSIMD type for representing complex numbers
using SIMD operations for efficient vectorized computation. Supports arithmetic
operations (addition, subtraction, multiplication, division), conjugation,
absolute value, and other complex number functions.

Exports
-------
- `ComplexSIMD`: SIMD-based complex number type.

<div class="prose-label">Notes</div>
    - ComplexSIMD uses SoA (Struct of Arrays) layout for SIMD efficiency.
    - Parameter `cdtype` determines component precision (e.g., cf32, cf64).
    - Parameter `width` is SIMD lane count; width=1 acts as scalar complex.

## Structs

### `ComplexSIMD`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct ComplexSIMD[cdtype: ComplexDType = ComplexDType.float64, width: Int = Int(1)]
```

**Memory convention:** `register_passable_trivial`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`, `RegisterPassable`, `TrivialRegisterPassable`, `Writable`

A SIMD-enabled complex number container (SoA layout).

Fields:
    re: SIMD vector of real parts.
    im: SIMD vector of imaginary parts.

The parameter `cdtype` determines the component precision (e.g. cf32, cf64).
The parameter `width` is the SIMD lane count; when `width == 1` this acts like a scalar complex number.

<div class="prose-label">Examples</div>
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

<div class="prose-label">Parameters</div>

- `cdtype` (`ComplexDType`)
- `width` (`Int`)

</div>

#### Fields

- **`re`** (`SIMD[ComplexSIMD[cdtype, width].dtype, width]`)
- **`im`** (`SIMD[ComplexSIMD[cdtype, width].dtype, width]`)

#### Aliases

#### `dtype`

```mojo
comptime dtype
```

**Value:** `cdtype.dtype`

Component dtype (underlying real/imag dtype).

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

<div class="overload-divider">Overload 1</div>

```mojo
def __init__(other: Self) -> Self
```

<span class="badge badge-static">static</span>

Copy constructor for ComplexSIMD.

Initializes a new ComplexSIMD instance by copying the values from another instance.

<div class="prose-label">Args</div>

- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __init__(re: SIMD[Self.dtype, width], im: SIMD[Self.dtype, width]) -> Self
```

<span class="badge badge-static">static</span>

Constructs a ComplexSIMD from SIMD vectors of real and imaginary parts.

<div class="prose-label">Args</div>

- `re` (`SIMD[Self.dtype, width]`) `[imm]`: SIMD vector containing the real components.
- `im` (`SIMD[Self.dtype, width]`) `[imm]`: SIMD vector containing the imaginary components.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 3</div>

```mojo
def __init__(val: SIMD[Self.dtype, width]) -> Self
```

<span class="badge badge-static">static</span>

Constructs a ComplexSIMD where both real and imaginary parts are set to the same SIMD value.

<div class="prose-label">Args</div>

- `val` (`SIMD[Self.dtype, width]`) `[imm]`: SIMD vector to broadcast to both real and imaginary components.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__getitem__`

```mojo
def __getitem__(self, idx: Int) -> ComplexSIMD[cdtype]
```

Returns the complex number at the specified lane index.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
var c_simd = ComplexSIMD[cf32, 2](SIMD[f32, 2](1, 2), SIMD[f32, 2](3, 4))
var c0 = c_simd[0]  # 1 + 3j
var c1 = c_simd[1]  # 2 + 4j
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: SIMD lane index (0 to width-1).

<div class="prose-label">Returns</div>

- `ComplexSIMD[cdtype]`

!!! failure "Raises"
    Error if lane index is out of range for the SIMD width.


</div>

<div class="fn-card" markdown="1">

#### `__setitem__`

```mojo
def __setitem__(mut self, idx: Int, value: ComplexSIMD[cdtype])
```

Sets the complex scalar at the specified lane index.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
var c_simd = nm.ComplexSIMD[cf32, 2](SIMD[f32, 2](1, 2), SIMD[f32, 2](3, 4)) # [(1 + 3j), (2 + 4j)]
c_simd[0] = nm.CScalar[cf32](5, 6)
print(c_simd) # [(1 + 3j), (2 + 4j)] becomes [(5 + 6j), (2 + 4j)]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `idx` (`Int`) `[imm]`: SIMD lane index (0 to width-1).
- `value` (`ComplexSIMD[cdtype]`) `[imm]`: ComplexScalar whose values will be assigned.

!!! failure "Raises"
    Error if lane index is out of range for the SIMD width.


</div>

<div class="fn-card" markdown="1">

#### `__neg__`

```mojo
def __neg__(self) -> Self
```

Returns the negation of this ComplexSIMD.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__pos__`

```mojo
def __pos__(self) -> Self
```

Returns the positive value of this ComplexSIMD (identity operation).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__invert__`

```mojo
def __invert__(self) -> Self where (ComplexSIMD[cdtype, width].dtype == DType.bool) if (ComplexSIMD[cdtype, width].dtype == DType.bool) else ComplexSIMD[cdtype, width].dtype.is_integral()
```

Element-wise logical NOT operation on this ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__eq__`

<div class="overload-divider">Overload 1</div>

```mojo
def __eq__(self, other: Self) -> Bool
```

Checks if two ComplexSIMD instances are exactly equal.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`

<div class="overload-divider">Overload 2</div>

```mojo
def __eq__(self, other: ImaginaryUnit) -> Bool
```

Checks if this ComplexSIMD instance is equal to the imaginary unit 1j.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var z1 = ComplexSIMD[cf64, 1](0.0, 1.0)  # 0 + 1j
var z2 = ComplexSIMD[cf64, 1](1.0, 1.0)  # 1 + 1j
print(z1 == `1j`)  # True
print(z2 == `1j`)  # False
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`ImaginaryUnit`) `[imm]`: Imaginary unit (1j) to compare with this ComplexSIMD instance.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__ne__`

<div class="overload-divider">Overload 1</div>

```mojo
def __ne__(self, other: Self) -> Bool
```

Checks if two ComplexSIMD instances are not equal.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`

<div class="overload-divider">Overload 2</div>

```mojo
def __ne__(self, other: ImaginaryUnit) -> Bool
```

Checks if this ComplexSIMD instance is not equal to the imaginary unit 1j.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var z1 = ComplexSIMD[cf64, 1](0.0, 1.0)  # 0 + 1j
var z2 = ComplexSIMD[cf64, 1](1.0, 1.0)  # 1 + 1j
print(z1 != `1j`)  # False
print(z2 != `1j`)  # True
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`ImaginaryUnit`) `[imm]`: Imaginary unit (1j) to compare with this ComplexSIMD instance.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__add__`

<div class="overload-divider">Overload 1</div>

```mojo
def __add__(self, other: Self) -> Self
```

Returns the element-wise sum of two ComplexSIMD instances.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: Another ComplexSIMD instance.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __add__(self, other: Scalar[Self.dtype]) -> Self
```

Returns the sum of this ComplexSIMD instance and a scalar added to the real part.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`: Scalar value to add to the real component.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 3</div>

```mojo
def __add__(self, other: SIMD[width]) -> Self
```

Returns the sum of this ComplexSIMD instance and a SIMD vector added to the real part.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[width]`) `[imm]`: SIMD vector to add to the real component.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 4</div>

```mojo
def __add__(self, other: ImaginaryUnit) -> Self
```

Returns the sum of this ComplexSIMD instance and the imaginary unit 1j.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
var result = z + `1j`  # 3 + 3j
print(result)  # (3 + 3j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`ImaginaryUnit`) `[imm]`: Imaginary unit (1j) to add to this complex number.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__sub__`

<div class="overload-divider">Overload 1</div>

```mojo
def __sub__(self, other: Self) -> Self
```

Returns the element-wise difference of two ComplexSIMD instances.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: Another ComplexSIMD instance.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __sub__(self, other: Scalar[Self.dtype]) -> Self
```

Returns the difference of this ComplexSIMD instance and a scalar subtracted from the real part.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`: Scalar value to subtract from the real component.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 3</div>

```mojo
def __sub__(self, other: SIMD[width]) -> Self
```

Returns the difference of this ComplexSIMD instance and a SIMD vector subtracted from the real part.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[width]`) `[imm]`: SIMD vector to subtract from the real component.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 4</div>

```mojo
def __sub__(self, other: ImaginaryUnit) -> Self
```

Subtracts the imaginary unit 1j from this ComplexSIMD instance.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
var result = z - `1j`  # 3 + 1j
print(result)  # (3 + 1j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`ImaginaryUnit`) `[imm]`: Imaginary unit (1j) to subtract from this complex number.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__mul__`

<div class="overload-divider">Overload 1</div>

```mojo
def __mul__(self, other: Self) -> Self
```

Returns the element-wise product of two ComplexSIMD instances.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: Another ComplexSIMD instance.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __mul__(self, other: Scalar[Self.dtype]) -> Self
```

Returns the product of this ComplexSIMD instance and a scalar.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`: Scalar value to multiply with both real and imaginary parts.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 3</div>

```mojo
def __mul__(self, other: SIMD[width]) -> Self
```

Returns the product of this ComplexSIMD instance and a SIMD vector.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[width]`) `[imm]`: SIMD vector to multiply with both real and imaginary parts.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 4</div>

```mojo
def __mul__(self, other: ImaginaryUnit) -> Self
```

Returns the product of this ComplexSIMD instance and the imaginary unit 1j.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
var result = z * `1j`  # -2 + 3j
print(result)  # (-2 + 3j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`ImaginaryUnit`) `[imm]`: Imaginary unit (1j) to multiply with this complex number.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__truediv__`

<div class="overload-divider">Overload 1</div>

```mojo
def __truediv__(self, other: Self) -> Self
```

Performs element-wise complex division of two ComplexSIMD instances.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: Another ComplexSIMD instance to divide by.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __truediv__(self, other: Scalar[Self.dtype]) -> Self
```

Performs element-wise division of this ComplexSIMD instance by a scalar.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`: Scalar value to divide both real and imaginary parts by.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 3</div>

```mojo
def __truediv__(self, other: SIMD[width]) -> Self
```

Performs element-wise division of this ComplexSIMD instance by a SIMD vector.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[width]`) `[imm]`: SIMD vector to divide both real and imaginary parts by.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 4</div>

```mojo
def __truediv__(self, other: ImaginaryUnit) -> Self
```

Performs division of this ComplexSIMD instance by the imaginary unit 1j.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
var result = z / `1j`  # 2 - 3j
print(result)  # (2 - 3j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`ImaginaryUnit`) `[imm]`: Imaginary unit (1j) to divide this complex number by.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__pow__`

```mojo
def __pow__(self, n: Int) -> Self
```

Raises this ComplexSIMD to an integer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `n` (`Int`) `[imm]`: Integer exponent.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__and__`

```mojo
def __and__(self, other: Self) -> Self where (ComplexSIMD[cdtype, width].dtype == DType.bool) if (ComplexSIMD[cdtype, width].dtype == DType.bool) else ComplexSIMD[cdtype, width].dtype.is_integral()
```

Element-wise logical AND operation between two ComplexSIMD instances.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: Another ComplexSIMD instance.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__or__`

```mojo
def __or__(self, other: Self) -> Self where (ComplexSIMD[cdtype, width].dtype == DType.bool) if (ComplexSIMD[cdtype, width].dtype == DType.bool) else ComplexSIMD[cdtype, width].dtype.is_integral()
```

Element-wise logical OR operation between two ComplexSIMD instances.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: Another ComplexSIMD instance.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__xor__`

```mojo
def __xor__(self, other: Self) -> Self where (ComplexSIMD[cdtype, width].dtype == DType.bool) if (ComplexSIMD[cdtype, width].dtype == DType.bool) else ComplexSIMD[cdtype, width].dtype.is_integral()
```

Element-wise logical XOR operation between two ComplexSIMD instances.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: Another ComplexSIMD instance.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__radd__`

<div class="overload-divider">Overload 1</div>

```mojo
def __radd__(self, other: Scalar[Self.dtype]) -> Self
```

Returns the sum of a scalar and this ComplexSIMD instance, adding to the real part.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`: Scalar value to add to the real component.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __radd__(self, other: SIMD[width]) -> Self
```

Returns the sum of a SIMD vector and this ComplexSIMD instance, adding to the real part.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[width]`) `[imm]`: SIMD vector to add to the real component.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 3</div>

```mojo
def __radd__(self, other: ImaginaryUnit) -> Self
```

Returns the sum of the imaginary unit 1j and this ComplexSIMD instance.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
var result = `1j` + z  # 3 + 3j
print(result)  # (3 + 3j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`ImaginaryUnit`) `[imm]`: Imaginary unit (1j) to add to this complex number.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__rsub__`

<div class="overload-divider">Overload 1</div>

```mojo
def __rsub__(self, other: Scalar[Self.dtype]) -> Self
```

Returns the difference of a scalar and this ComplexSIMD instance, subtracting from the real part.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`: Scalar value to subtract from the real component.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __rsub__(self, other: SIMD[width]) -> Self
```

Returns the difference of a SIMD vector and this ComplexSIMD instance, subtracting from the real part.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[width]`) `[imm]`: SIMD vector to subtract from the real component.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 3</div>

```mojo
def __rsub__(self, other: ImaginaryUnit) -> Self
```

Returns the difference of the imaginary unit 1j and this ComplexSIMD instance.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
var result = `1j` - z  # -3 + (-1)j = -3 - 1j
print(result)  # (-3 - 1j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`ImaginaryUnit`) `[imm]`: Imaginary unit (1j) from which this complex number is subtracted.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__rmul__`

<div class="overload-divider">Overload 1</div>

```mojo
def __rmul__(self, other: Scalar[Self.dtype]) -> Self
```

Returns the product of a scalar and this ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`: Scalar value to multiply with both real and imaginary parts.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __rmul__(self, other: SIMD[width]) -> Self
```

Returns the product of a SIMD vector and this ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[width]`) `[imm]`: SIMD vector to multiply with both real and imaginary parts.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 3</div>

```mojo
def __rmul__(self, other: ImaginaryUnit) -> Self
```

Returns the product of the imaginary unit 1j and this ComplexSIMD instance.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
var result = `1j` * z  # -2 + 3j
print(result)  # (-2 + 3j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`ImaginaryUnit`) `[imm]`: Imaginary unit (1j) to multiply with this complex number.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__rtruediv__`

<div class="overload-divider">Overload 1</div>

```mojo
def __rtruediv__(self, other: Scalar[Self.dtype]) -> Self
```

Performs element-wise division of a scalar by this ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`: Scalar value to be divided by this ComplexSIMD instance.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __rtruediv__(self, other: SIMD[width]) -> Self
```

Performs element-wise division of a SIMD vector by this ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[width]`) `[imm]`: SIMD vector to be divided by this ComplexSIMD instance.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 3</div>

```mojo
def __rtruediv__(self, other: ImaginaryUnit) -> Self
```

Performs division of the imaginary unit 1j by this ComplexSIMD instance.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 4.0)  # 3 + 4j
var result = `1j` / z  # 1j / (3 + 4j) = 0.16 - 0.12j
print(result)  # (0.16 - 0.12j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`ImaginaryUnit`) `[imm]`: Imaginary unit (1j) to be divided by this ComplexSIMD instance.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__iadd__`

<div class="overload-divider">Overload 1</div>

```mojo
def __iadd__(mut self, other: Self)
```

In-place addition of another ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`: Another ComplexSIMD instance.

<div class="overload-divider">Overload 2</div>

```mojo
def __iadd__(mut self, other: Scalar[Self.dtype])
```

In-place addition of a scalar to the real part of this ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Scalar[Self.dtype]`) `[imm]`: Scalar value to add to the real component.

<div class="overload-divider">Overload 3</div>

```mojo
def __iadd__(mut self, other: SIMD[width])
```

In-place addition of a SIMD vector to the real part of this ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`SIMD[width]`) `[imm]`: SIMD vector to add to the real component.

<div class="overload-divider">Overload 4</div>

```mojo
def __iadd__(mut self, other: ImaginaryUnit)
```

In-place addition of the imaginary unit 1j to this ComplexSIMD instance.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
z += `1j`  # Now z = 3 + 3j
print(z)  # (3 + 3j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`ImaginaryUnit`) `[imm]`: Imaginary unit (1j) to add to this complex number.


</div>

<div class="fn-card" markdown="1">

#### `__isub__`

<div class="overload-divider">Overload 1</div>

```mojo
def __isub__(mut self, other: Self)
```

In-place subtraction of another ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`: Another ComplexSIMD instance.

<div class="overload-divider">Overload 2</div>

```mojo
def __isub__(mut self, other: Scalar[Self.dtype])
```

In-place subtraction of a scalar from the real part of this ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Scalar[Self.dtype]`) `[imm]`: Scalar value to subtract from the real component.

<div class="overload-divider">Overload 3</div>

```mojo
def __isub__(mut self, other: SIMD[width])
```

In-place subtraction of a SIMD vector from the real part of this ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`SIMD[width]`) `[imm]`: SIMD vector to subtract from the real component.

<div class="overload-divider">Overload 4</div>

```mojo
def __isub__(mut self, other: ImaginaryUnit)
```

In-place subtraction of the imaginary unit 1j from this ComplexSIMD instance.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
z -= `1j`  # Now z = 3 + 1j
print(z)  # (3 + 1j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`ImaginaryUnit`) `[imm]`: Imaginary unit (1j) to subtract from this complex number.


</div>

<div class="fn-card" markdown="1">

#### `__imul__`

<div class="overload-divider">Overload 1</div>

```mojo
def __imul__(mut self, other: Self)
```

In-place complex multiplication with another ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`: Another ComplexSIMD instance.

<div class="overload-divider">Overload 2</div>

```mojo
def __imul__(mut self, other: Scalar[Self.dtype])
```

In-place multiplication of this ComplexSIMD instance by a scalar.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Scalar[Self.dtype]`) `[imm]`: Scalar value to multiply with both real and imaginary parts.

<div class="overload-divider">Overload 3</div>

```mojo
def __imul__(mut self, other: SIMD[width])
```

In-place multiplication of this ComplexSIMD instance by a SIMD vector.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`SIMD[width]`) `[imm]`: SIMD vector to multiply with both real and imaginary parts.

<div class="overload-divider">Overload 4</div>

```mojo
def __imul__(mut self, other: ImaginaryUnit)
```

In-place multiplication of this ComplexSIMD instance by the imaginary unit 1j.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
z *= `1j`  # Now z = -2 + 3j
print(z)  # (-2 + 3j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`ImaginaryUnit`) `[imm]`: Imaginary unit (1j) to multiply with this complex number.


</div>

<div class="fn-card" markdown="1">

#### `__itruediv__`

<div class="overload-divider">Overload 1</div>

```mojo
def __itruediv__(mut self, other: Self)
```

Performs in-place element-wise complex division of self by another ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`: Another ComplexSIMD instance to divide by.

<div class="overload-divider">Overload 2</div>

```mojo
def __itruediv__(mut self, other: Scalar[Self.dtype])
```

Performs in-place element-wise division of this ComplexSIMD instance by a scalar.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Scalar[Self.dtype]`) `[imm]`: Scalar value to divide both real and imaginary parts by.

<div class="overload-divider">Overload 3</div>

```mojo
def __itruediv__(mut self, other: SIMD[width])
```

Performs in-place element-wise division of this ComplexSIMD instance by a SIMD vector.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`SIMD[width]`) `[imm]`: SIMD vector to divide both real and imaginary parts by.

<div class="overload-divider">Overload 4</div>

```mojo
def __itruediv__(mut self, other: ImaginaryUnit)
```

Performs in-place division of this ComplexSIMD instance by the imaginary unit 1j.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var z = ComplexSIMD[cf64, 1](3.0, 2.0)  # 3 + 2j
z /= `1j`  # Now z = 2 - 3j
print(z)  # (2 - 3j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`ImaginaryUnit`) `[imm]`: Imaginary unit (1j) to divide this complex number by.


</div>

<div class="fn-card" markdown="1">

#### `zero`

```mojo
def zero() -> Self
```

<span class="badge badge-static">static</span>

Returns a ComplexSIMD instance with all real and imaginary components set to zero.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
var comp = ComplexSIMD[cf64].zero()  # (0 + 0j)
```

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `one`

```mojo
def one() -> Self
```

<span class="badge badge-static">static</span>

Returns a ComplexSIMD instance representing the complex number 1 + 0j.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
var comp = ComplexSIMD[cf64].one()  # (1 + 0j)
```

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `i`

```mojo
def i() -> Self
```

<span class="badge badge-static">static</span>

Returns a ComplexSIMD instance representing the imaginary unit 0 + 1j.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

# Create imaginary unit for different types
var i_f64 = ComplexSIMD[cf64].i()  # (0 + 1j)
var i_f32 = ComplexSIMD[cf32].i()  # (0 + 1j)
print(i_f64)  # (0 + 1j)

# Use in complex arithmetic
var z = 3.0 + 4.0 * ComplexSIMD[cf64].i()  # 3 + 4j
```

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `from_real_imag`

```mojo
def from_real_imag(re: Scalar[Self.dtype], im: Scalar[Self.dtype]) -> Self
```

<span class="badge badge-static">static</span>

Constructs a ComplexSIMD instance from scalar real and imaginary values.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
var comp = ComplexSIMD[cf64].from_real_imag(2.0, 3.0)  # (2.0 + 3.0j)
```

<div class="prose-label">Args</div>

- `re` (`Scalar[Self.dtype]`) `[imm]`: Scalar value for the real component.
- `im` (`Scalar[Self.dtype]`) `[imm]`: Scalar value for the imaginary component.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `from_polar`

```mojo
def from_polar(r: Scalar[Self.dtype], theta: Scalar[Self.dtype]) -> Self where ComplexSIMD[cdtype, width].dtype.is_floating_point()
```

<span class="badge badge-static">static</span>

Constructs a ComplexSIMD instance from polar coordinates.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
var comp = ComplexSIMD[cf64].from_polar(2.0, 0.5)
```

<div class="prose-label">Args</div>

- `r` (`Scalar[Self.dtype]`) `[imm]`: Magnitude (radius).
- `theta` (`Scalar[Self.dtype]`) `[imm]`: Angle (in radians).

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `reciprocal`

```mojo
def reciprocal(self) -> Self
```

Returns the element-wise reciprocal (1 / self) of the ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `elem_pow`

<div class="overload-divider">Overload 1</div>

```mojo
def elem_pow(self, other: Self) -> Self
```

Raises each component of this ComplexSIMD to the power of the corresponding component in another ComplexSIMD.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: Another ComplexSIMD instance.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def elem_pow(self, exponent: Scalar[Self.dtype]) -> Self
```

Raises each component of this ComplexSIMD to a scalar exponent.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `exponent` (`Scalar[Self.dtype]`) `[imm]`: Scalar exponent to apply to both real and imaginary parts.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `allclose`

```mojo
def allclose(self, other: Self, *, rtol: Scalar[Self.dtype] = 1.0000000000000001E-5, atol: Scalar[Self.dtype] = 1.0E-8) -> Bool
```

Checks if two ComplexSIMD instances are approximately equal within given tolerances.

For each lane, compares the real and imaginary parts using the formula:
    abs(a - b) <= atol + rtol * abs(b)
where a and b are the corresponding components of self and other.

<div class="prose-label">Notes</div>
For SIMD width > 1, all lanes must satisfy the tolerance criteria.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: Another ComplexSIMD instance to compare against.
- `rtol` (`Scalar[Self.dtype]`) `[imm]`: Relative tolerance.
- `atol` (`Scalar[Self.dtype]`) `[imm]`: Absolute tolerance.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__str__`

```mojo
def __str__(self) -> String
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>

<div class="fn-card" markdown="1">

#### `write_to`

```mojo
def write_to[W: Writer](self, mut writer: W)
```

Returns a string representation of the ComplexSIMD instance.

For width == 1, the format is: (re + im j).
For width > 1, the format is: [(re0 + im0 j), (re1 + im1 j), ...].

<div class="prose-label">Parameters</div>

- `W` (`Writer`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

#### `__repr__`

```mojo
def __repr__(self) -> String
```

Returns a string representation of the ComplexSIMD instance for debugging. `ComplexSIMD[dtype](re=<real SIMD>, im=<imag SIMD>)`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `item`

```mojo
def item[name: String](self, idx: Int) -> Scalar[Self.dtype]
```

Returns the scalar value for the specified lane index and component.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
var c_simd = nm.ComplexSIMD[cf32, 2](SIMD[f32, 2](1, 2), SIMD[f32, 2](3, 4)) # [(1 + 3j), (2 + 4j)]
var re0 = c_simd.item["re"](0)  # 1.0
var im1 = c_simd.item["im"](1)  # 4.0
```

<div class="prose-label">Parameters</div>

- `name` (`String`): Name of the component ('re' or 'im').

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: Lane index to retrieve.

<div class="prose-label">Returns</div>

- `Scalar[Self.dtype]`

!!! failure "Raises"
    - Error if the component name is invalid.
- Error if lane index is out of range for the SIMD width.


</div>

<div class="fn-card" markdown="1">

#### `itemset`

```mojo
def itemset[name: String](mut self, idx: Int, val: Scalar[Self.dtype])
```

Sets the scalar value for the specified lane index and component.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
var c_simd = nm.ComplexSIMD[cf32, 2](SIMD[f32, 2](1, 2), SIMD[f32, 2](3, 4)) # [(1 + 3j), (2 + 4j)]
c_simd.itemset["re"](0, 5.0)  # Now first complex number is (5 + 3j)
c_simd.itemset["im"](1, 6.0)  # Now second complex number is (2 + 6j)
```

<div class="prose-label">Parameters</div>

- `name` (`String`): Name of the component ('re' or 'im').

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `idx` (`Int`) `[imm]`: Lane index to set.
- `val` (`Scalar[Self.dtype]`) `[imm]`: Scalar value to assign to the specified component.

!!! failure "Raises"
    - Error if the component name is invalid.
- Error if lane index is out of range for the SIMD width.


</div>

<div class="fn-card" markdown="1">

#### `real`

```mojo
def real(self) -> SIMD[Self.dtype, width]
```

Returns the real part(s) of the complex number(s).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `SIMD[Self.dtype, width]`


</div>

<div class="fn-card" markdown="1">

#### `imag`

```mojo
def imag(self) -> SIMD[Self.dtype, width]
```

Returns the imaginary part(s) of the complex number(s).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `SIMD[Self.dtype, width]`


</div>

<div class="fn-card" markdown="1">

#### `__abs__`

```mojo
def __abs__(self) -> SIMD[Self.dtype, width]
```

Returns the magnitude (absolute value) of the complex number(s).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `SIMD[Self.dtype, width]`


</div>

<div class="fn-card" markdown="1">

#### `norm`

```mojo
def norm(self) -> SIMD[Self.dtype, width]
```

Returns the squared magnitude (norm) of the complex number(s).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `SIMD[Self.dtype, width]`


</div>

<div class="fn-card" markdown="1">

#### `conj`

```mojo
def conj(self) -> Self
```

Returns the complex conjugate of the ComplexSIMD instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`


</div>
### `ImaginaryUnit`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct ImaginaryUnit
```

**Memory convention:** `register_passable_trivial`  
**Implements:** `AnyType`, `Boolable`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`, `RegisterPassable`, `TrivialRegisterPassable`, `Writable`

Constant representing the imaginary unit complex number 0 + 1j.

The ImaginaryUnit struct provides a convenient way to work with the imaginary unit
in complex arithmetic operations. It supports arithmetic operations with SIMD vectors,
scalars, and other complex numbers, enabling Python-like syntax for complex number creation.

<div class="prose-label">Examples</div>
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

</div>

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

```mojo
def __init__() -> Self
```

<span class="badge badge-static">static</span>

Constructor for ImaginaryUnit.

Creates an instance representing the imaginary unit 1j.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__bool__`

```mojo
def __bool__(self) -> Bool
```

Returns the boolean value of the imaginary unit.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

if `1j`:
    print("Imaginary unit is truthy")  # This will execute
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__neg__`

```mojo
def __neg__(self) -> ComplexSIMD
```

Returns the negation of the imaginary unit: -1j.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var result = -`1j`  # -1j
print(result)  # (0 - 1j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD`


</div>

<div class="fn-card" markdown="1">

#### `__add__`

<div class="overload-divider">Overload 1</div>

```mojo
def __add__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(mlir_value=dtype), width]
```

Returns the sum of the imaginary unit 1j and a SIMD vector.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var vec = SIMD[DType.float32, 4](1.0, 2.0, 3.0, 4.0)
var result = `1j` + vec  # [1+1j, 2+1j, 3+1j, 4+1j]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `width` (`Int`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[dtype, width]`) `[imm]`: SIMD vector to add to the imaginary unit.

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype), width]`

<div class="overload-divider">Overload 2</div>

```mojo
def __add__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(mlir_value=dtype)]
```

Returns the sum of the imaginary unit 1j and a scalar.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var result = `1j` + 3.5  # 3.5 + 1j
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`: Scalar to add to the imaginary unit.

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype)]`

<div class="overload-divider">Overload 3</div>

```mojo
def __add__(self, other: Int) -> ComplexSIMD[ComplexDType.int]
```

Returns the sum of the imaginary unit 1j and an integer.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var result = `1j` + 5  # 5 + 1j
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Int`) `[imm]`: Integer to add to the imaginary unit.

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType.int]`

<div class="overload-divider">Overload 4</div>

```mojo
def __add__(self, other: Self) -> ComplexSIMD
```

Returns the sum of the imaginary unit with itself: 1j + 1j = 2j.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var result = `1j` + `1j`  # 2j
print(result)  # (0 + 2j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: Another imaginary unit to add.

<div class="prose-label">Returns</div>

- `ComplexSIMD`


</div>

<div class="fn-card" markdown="1">

#### `__sub__`

<div class="overload-divider">Overload 1</div>

```mojo
def __sub__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(mlir_value=dtype), width]
```

Returns the difference of the imaginary unit and a SIMD vector.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `width` (`Int`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[dtype, width]`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype), width]`

<div class="overload-divider">Overload 2</div>

```mojo
def __sub__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(mlir_value=dtype)]
```

Returns the difference of the imaginary unit and a scalar.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype)]`

<div class="overload-divider">Overload 3</div>

```mojo
def __sub__(self, other: Int) -> ComplexSIMD[ComplexDType.int]
```

Returns the difference of the imaginary unit and an integer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType.int]`

<div class="overload-divider">Overload 4</div>

```mojo
def __sub__(self, other: Self) -> Float64
```

Returns the difference of the imaginary unit with itself: 1j - 1j = 0.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var result = `1j` - `1j`  # 0
print(result)  # 0
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: Another imaginary unit to subtract.

<div class="prose-label">Returns</div>

- `Float64`


</div>

<div class="fn-card" markdown="1">

#### `__mul__`

<div class="overload-divider">Overload 1</div>

```mojo
def __mul__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(mlir_value=dtype), width]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `width` (`Int`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[dtype, width]`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype), width]`

<div class="overload-divider">Overload 2</div>

```mojo
def __mul__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(mlir_value=dtype)]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype)]`

<div class="overload-divider">Overload 3</div>

```mojo
def __mul__(self, other: Int) -> ComplexSIMD[ComplexDType.int]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType.int]`

<div class="overload-divider">Overload 4</div>

```mojo
def __mul__(self, other: Self) -> Float64
```

Returns the product of the imaginary unit with itself: 1j * 1j = -1.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var result = `1j` * `1j`  # -1
print(result)  # -1
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: Another imaginary unit to multiply with.

<div class="prose-label">Returns</div>

- `Float64`


</div>

<div class="fn-card" markdown="1">

#### `__truediv__`

<div class="overload-divider">Overload 1</div>

```mojo
def __truediv__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(mlir_value=dtype), width]
```

Returns the division of the imaginary unit by a SIMD vector.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `width` (`Int`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[dtype, width]`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype), width]`

<div class="overload-divider">Overload 2</div>

```mojo
def __truediv__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(mlir_value=dtype)]
```

Returns the division of the imaginary unit by a scalar.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype)]`

<div class="overload-divider">Overload 3</div>

```mojo
def __truediv__(self, other: Self) -> Float64
```

Returns the division of the imaginary unit by itself: 1j / 1j = 1.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var result = `1j` / `1j`  # 1
print(result)  # 1
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: Another imaginary unit to divide by.

<div class="prose-label">Returns</div>

- `Float64`


</div>

<div class="fn-card" markdown="1">

#### `__pow__`

```mojo
def __pow__(self, exponent: Int) -> ComplexSIMD
```

Returns the imaginary unit raised to an integer power.

The powers of 1j cycle with period 4:
- 1j^0 = 1
- 1j^1 = 1j
- 1j^2 = -1
- 1j^3 = -1j
- 1j^4 = 1 (cycle repeats)

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

print(`1j` ** 0)  # (1 + 0j)
print(`1j` ** 1)  # (0 + 1j)
print(`1j` ** 2)  # (-1 + 0j)
print(`1j` ** 3)  # (0 - 1j)
print(`1j` ** 4)  # (1 + 0j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `exponent` (`Int`) `[imm]`: Integer exponent.

<div class="prose-label">Returns</div>

- `ComplexSIMD`


</div>

<div class="fn-card" markdown="1">

#### `__radd__`

<div class="overload-divider">Overload 1</div>

```mojo
def __radd__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(mlir_value=dtype), width]
```

Returns the sum of a SIMD vector and the imaginary unit.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `width` (`Int`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[dtype, width]`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype), width]`

<div class="overload-divider">Overload 2</div>

```mojo
def __radd__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(mlir_value=dtype)]
```

Returns the sum of a scalar and the imaginary unit.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype)]`

<div class="overload-divider">Overload 3</div>

```mojo
def __radd__(self, other: Int) -> ComplexSIMD[ComplexDType.int]
```

Returns the sum of an integer and the imaginary unit.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType.int]`


</div>

<div class="fn-card" markdown="1">

#### `__rsub__`

<div class="overload-divider">Overload 1</div>

```mojo
def __rsub__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(mlir_value=dtype), width]
```

Returns the difference of a SIMD vector and the imaginary unit.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `width` (`Int`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[dtype, width]`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype), width]`

<div class="overload-divider">Overload 2</div>

```mojo
def __rsub__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(mlir_value=dtype)]
```

Returns the difference of a scalar and the imaginary unit.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype)]`

<div class="overload-divider">Overload 3</div>

```mojo
def __rsub__(self, other: Int) -> ComplexSIMD[ComplexDType.int]
```

Returns the difference of an integer and the imaginary unit.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType.int]`


</div>

<div class="fn-card" markdown="1">

#### `__rmul__`

<div class="overload-divider">Overload 1</div>

```mojo
def __rmul__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(mlir_value=dtype), width]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `width` (`Int`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[dtype, width]`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype), width]`

<div class="overload-divider">Overload 2</div>

```mojo
def __rmul__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(mlir_value=dtype)]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype)]`

<div class="overload-divider">Overload 3</div>

```mojo
def __rmul__(self, other: Int) -> ComplexSIMD[ComplexDType.int]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType.int]`


</div>

<div class="fn-card" markdown="1">

#### `__rtruediv__`

<div class="overload-divider">Overload 1</div>

```mojo
def __rtruediv__[dtype: DType, width: Int](self, other: SIMD[dtype, width]) -> ComplexSIMD[ComplexDType(mlir_value=dtype), width]
```

Returns the division of a SIMD vector by the imaginary unit.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)
- `width` (`Int`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`SIMD[dtype, width]`) `[imm]`: SIMD vector to be divided by the imaginary unit.

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype), width]`

<div class="overload-divider">Overload 2</div>

```mojo
def __rtruediv__[dtype: DType](self, other: Scalar[dtype]) -> ComplexSIMD[ComplexDType(mlir_value=dtype)]
```

Returns the division of a scalar by the imaginary unit.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`: Scalar to be divided by the imaginary unit.

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType(mlir_value=dtype)]`

<div class="overload-divider">Overload 3</div>

```mojo
def __rtruediv__(self, other: Int) -> ComplexSIMD[ComplexDType.int]
```

Returns the division of an integer by the imaginary unit.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Int`) `[imm]`: Integer to be divided by the imaginary unit.

<div class="prose-label">Returns</div>

- `ComplexSIMD[ComplexDType.int]`


</div>

<div class="fn-card" markdown="1">

#### `conj`

```mojo
def conj(self) -> ComplexSIMD
```

Returns the complex conjugate of the imaginary unit.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *

var conj_i = `1j`.conj()  # -1j
print(conj_i)  # (0 - 1j)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `ComplexSIMD`


</div>

<div class="fn-card" markdown="1">

#### `__str__`

```mojo
def __str__(self) -> String
```

Returns the string representation of the imaginary unit.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>

<div class="fn-card" markdown="1">

#### `write_to`

```mojo
def write_to[W: Writer](self, mut writer: W)
```

Writes the string representation of the imaginary unit to a writer.

<div class="prose-label">Parameters</div>

- `W` (`Writer`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`: Writer instance to write the string representation to.


</div>
