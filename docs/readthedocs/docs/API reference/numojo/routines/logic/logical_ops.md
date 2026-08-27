# `numojo.routines.logic.logical_ops`

Element-wise logical operations for arrays.

Implements logical AND, OR, XOR, and NOT operations for NDArray and
ComplexNDArray types.

Exports
-------
- `logical_and`: Logical AND operation.
- `logical_or`: Logical OR operation.
- `logical_xor`: Logical XOR operation.
- `logical_not`: Logical NOT operation.

## Functions


<div class="fn-card" markdown="1">

### `logical_and`

#### Overload 1

```mojo
def logical_and[dtype: DType](a: NDArray[dtype], b: NDArray[dtype]) -> NDArray[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool) else dtype.is_integral()
```

Element-wise logical AND operation between two arrays.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_and

var a = nm.arange(0, 10)
var b = nm.arange(5, 15)
var result = logical_and(a > 3, b < 10)
```

!!! info "Constraints"
    - Supports only boolean and integral data types.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: First input array.
- `b` (`NDArray[dtype]`) `[imm]`: Second input array.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"
    - NumojoError: If the input arrays do not have the same shape.

#### Overload 2

```mojo
def logical_and[cdtype: ComplexDType](a: ComplexNDArray[cdtype], b: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype] where (cdtype == DType.bool) if (cdtype == DType.bool) else cdtype.dtype.is_integral()
```

Element-wise logical AND operation between two complex arrays.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_and

var a = nm.arange[ci32](CScalar[ci32](0), CScalar[ci32](10))
var b = nm.arange[ci32](CScalar[ci32](5), CScalar[ci32](15))
var result = logical_and[ci32](a, b)
```

!!! info "Constraints"
    - Supports only boolean and integral complex data types.

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `a` (`ComplexNDArray[cdtype]`) `[imm]`: First input complex array.
- `b` (`ComplexNDArray[cdtype]`) `[imm]`: Second input complex array.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"
    - NumojoError: If the input arrays do not have the same shape.


</div>

<div class="fn-card" markdown="1">

### `logical_or`

#### Overload 1

```mojo
def logical_or[dtype: DType](a: NDArray[dtype], b: NDArray[dtype]) -> NDArray[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool) else dtype.is_integral()
```

Element-wise logical OR operation between two arrays.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_or

var a = nm.arange(0, 10)
var b = nm.arange(5, 15)
var result = logical_or(a < 3, b > 10)
```

!!! info "Constraints"
    - Supports only boolean and integral data types.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: First input array.
- `b` (`NDArray[dtype]`) `[imm]`: Second input array.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"
    - NumojoError: If the input arrays do not have the same shape.

#### Overload 2

```mojo
def logical_or[cdtype: ComplexDType](a: ComplexNDArray[cdtype], b: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype] where (cdtype == DType.bool) if (cdtype == DType.bool) else cdtype.dtype.is_integral()
```

Element-wise logical OR operation between two complex arrays.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_or

var a = nm.arange[ci32](CScalar[ci32](0), CScalar[ci32](10))
var b = nm.arange[ci32](CScalar[ci32](5), CScalar[ci32](15))
var result = logical_or[ci32](a, b)
```

!!! info "Constraints"
    - Supports only boolean and integral complex data types.

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `a` (`ComplexNDArray[cdtype]`) `[imm]`: First input complex array.
- `b` (`ComplexNDArray[cdtype]`) `[imm]`: Second input complex array.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"
    - NumojoError: If the input arrays do not have the same shape.


</div>

<div class="fn-card" markdown="1">

### `logical_not`

#### Overload 1

```mojo
def logical_not[dtype: DType](a: NDArray[dtype]) -> NDArray[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool) else dtype.is_integral()
```

Element-wise logical NOT operation on an array.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_not

var a = nm.arange(0, 10)
var result = logical_not(a < 5)
```

!!! info "Constraints"
    - Supports only boolean and integral data types.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: Input array.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"
    - NumojoError: If the input array is not of a supported data type.

#### Overload 2

```mojo
def logical_not[cdtype: ComplexDType](a: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype] where (cdtype == DType.bool) if (cdtype == DType.bool) else cdtype.dtype.is_integral()
```

Element-wise logical NOT operation on a complex array.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_not

var a = nm.arange[ci32](CScalar[ci32](0), CScalar[ci32](10))
var result = logical_not[ci32](a)
```

!!! info "Constraints"
    - Supports only boolean and integral complex data types.

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `a` (`ComplexNDArray[cdtype]`) `[imm]`: Input complex array.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"
    - NumojoError: If the input array is not of a supported data type.


</div>

<div class="fn-card" markdown="1">

### `logical_xor`

#### Overload 1

```mojo
def logical_xor[dtype: DType](a: NDArray[dtype], b: NDArray[dtype]) -> NDArray[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool) else dtype.is_integral()
```

Element-wise logical XOR operation between two arrays.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_xor

var a = nm.arange(0, 10)
var b = nm.arange(5, 15)
var result = logical_xor(a > 3, b < 10)
```

!!! info "Constraints"
    - Supports only boolean and integral data types.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: First input array.
- `b` (`NDArray[dtype]`) `[imm]`: Second input array.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"
    - NumojoError: If the input arrays do not have the same shape.

#### Overload 2

```mojo
def logical_xor[cdtype: ComplexDType](a: ComplexNDArray[cdtype], b: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype] where (cdtype == DType.bool) if (cdtype == DType.bool) else cdtype.dtype.is_integral()
```

Element-wise logical XOR operation between two complex arrays.

Examples:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_xor

var a = nm.arange[ci32](CScalar[ci32](0), CScalar[ci32](10))
var b = nm.arange[ci32](CScalar[ci32](5), CScalar[ci32](15))
var result = logical_xor[ci32](a, b)
```

!!! info "Constraints"
    - Supports only boolean and integral complex data types.

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `a` (`ComplexNDArray[cdtype]`) `[imm]`: First input complex array.
- `b` (`ComplexNDArray[cdtype]`) `[imm]`: Second input complex array.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"
    - NumojoError: If the input arrays do not have the same shape.


</div>
