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

<div class="overload-divider">Overload 1</div>

```mojo
def logical_and[dtype: DType](a: NDArray[dtype], b: NDArray[dtype]) -> NDArray[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool) else dtype.is_integral()
```

Element-wise logical AND operation between two arrays.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_and

var a = nm.arange(0, 10)
var b = nm.arange(5, 15)
var result = logical_and(a > 3, b < 10)
```

!!! info "Constraints"
    - Supports only boolean and integral data types.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: First input array.
- `b` (`NDArray[dtype]`) `[imm]`: Second input array.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"
    - NumojoError: If the input arrays do not have the same shape.

<div class="overload-divider">Overload 2</div>

```mojo
def logical_and[cdtype: ComplexDType](a: ComplexNDArray[cdtype], b: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype] where (cdtype == DType.bool) if (cdtype == DType.bool) else cdtype.dtype.is_integral()
```

Element-wise logical AND operation between two complex arrays.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_and

var a = nm.arange[ci32](CScalar[ci32](0), CScalar[ci32](10))
var b = nm.arange[ci32](CScalar[ci32](5), CScalar[ci32](15))
var result = logical_and[ci32](a, b)
```

!!! info "Constraints"
    - Supports only boolean and integral complex data types.

<div class="prose-label">Parameters</div>

- `cdtype` (`ComplexDType`)

<div class="prose-label">Args</div>

- `a` (`ComplexNDArray[cdtype]`) `[imm]`: First input complex array.
- `b` (`ComplexNDArray[cdtype]`) `[imm]`: Second input complex array.

<div class="prose-label">Returns</div>

- `ComplexNDArray[cdtype]`

!!! failure "Raises"
    - NumojoError: If the input arrays do not have the same shape.


</div>

<div class="fn-card" markdown="1">

### `logical_or`

<div class="overload-divider">Overload 1</div>

```mojo
def logical_or[dtype: DType](a: NDArray[dtype], b: NDArray[dtype]) -> NDArray[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool) else dtype.is_integral()
```

Element-wise logical OR operation between two arrays.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_or

var a = nm.arange(0, 10)
var b = nm.arange(5, 15)
var result = logical_or(a < 3, b > 10)
```

!!! info "Constraints"
    - Supports only boolean and integral data types.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: First input array.
- `b` (`NDArray[dtype]`) `[imm]`: Second input array.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"
    - NumojoError: If the input arrays do not have the same shape.

<div class="overload-divider">Overload 2</div>

```mojo
def logical_or[cdtype: ComplexDType](a: ComplexNDArray[cdtype], b: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype] where (cdtype == DType.bool) if (cdtype == DType.bool) else cdtype.dtype.is_integral()
```

Element-wise logical OR operation between two complex arrays.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_or

var a = nm.arange[ci32](CScalar[ci32](0), CScalar[ci32](10))
var b = nm.arange[ci32](CScalar[ci32](5), CScalar[ci32](15))
var result = logical_or[ci32](a, b)
```

!!! info "Constraints"
    - Supports only boolean and integral complex data types.

<div class="prose-label">Parameters</div>

- `cdtype` (`ComplexDType`)

<div class="prose-label">Args</div>

- `a` (`ComplexNDArray[cdtype]`) `[imm]`: First input complex array.
- `b` (`ComplexNDArray[cdtype]`) `[imm]`: Second input complex array.

<div class="prose-label">Returns</div>

- `ComplexNDArray[cdtype]`

!!! failure "Raises"
    - NumojoError: If the input arrays do not have the same shape.


</div>

<div class="fn-card" markdown="1">

### `logical_not`

<div class="overload-divider">Overload 1</div>

```mojo
def logical_not[dtype: DType](a: NDArray[dtype]) -> NDArray[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool) else dtype.is_integral()
```

Element-wise logical NOT operation on an array.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_not

var a = nm.arange(0, 10)
var result = logical_not(a < 5)
```

!!! info "Constraints"
    - Supports only boolean and integral data types.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: Input array.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"
    - NumojoError: If the input array is not of a supported data type.

<div class="overload-divider">Overload 2</div>

```mojo
def logical_not[cdtype: ComplexDType](a: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype] where (cdtype == DType.bool) if (cdtype == DType.bool) else cdtype.dtype.is_integral()
```

Element-wise logical NOT operation on a complex array.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_not

var a = nm.arange[ci32](CScalar[ci32](0), CScalar[ci32](10))
var result = logical_not[ci32](a)
```

!!! info "Constraints"
    - Supports only boolean and integral complex data types.

<div class="prose-label">Parameters</div>

- `cdtype` (`ComplexDType`)

<div class="prose-label">Args</div>

- `a` (`ComplexNDArray[cdtype]`) `[imm]`: Input complex array.

<div class="prose-label">Returns</div>

- `ComplexNDArray[cdtype]`

!!! failure "Raises"
    - NumojoError: If the input array is not of a supported data type.


</div>

<div class="fn-card" markdown="1">

### `logical_xor`

<div class="overload-divider">Overload 1</div>

```mojo
def logical_xor[dtype: DType](a: NDArray[dtype], b: NDArray[dtype]) -> NDArray[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool) else dtype.is_integral()
```

Element-wise logical XOR operation between two arrays.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_xor

var a = nm.arange(0, 10)
var b = nm.arange(5, 15)
var result = logical_xor(a > 3, b < 10)
```

!!! info "Constraints"
    - Supports only boolean and integral data types.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: First input array.
- `b` (`NDArray[dtype]`) `[imm]`: Second input array.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"
    - NumojoError: If the input arrays do not have the same shape.

<div class="overload-divider">Overload 2</div>

```mojo
def logical_xor[cdtype: ComplexDType](a: ComplexNDArray[cdtype], b: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype] where (cdtype == DType.bool) if (cdtype == DType.bool) else cdtype.dtype.is_integral()
```

Element-wise logical XOR operation between two complex arrays.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_xor

var a = nm.arange[ci32](CScalar[ci32](0), CScalar[ci32](10))
var b = nm.arange[ci32](CScalar[ci32](5), CScalar[ci32](15))
var result = logical_xor[ci32](a, b)
```

!!! info "Constraints"
    - Supports only boolean and integral complex data types.

<div class="prose-label">Parameters</div>

- `cdtype` (`ComplexDType`)

<div class="prose-label">Args</div>

- `a` (`ComplexNDArray[cdtype]`) `[imm]`: First input complex array.
- `b` (`ComplexNDArray[cdtype]`) `[imm]`: Second input complex array.

<div class="prose-label">Returns</div>

- `ComplexNDArray[cdtype]`

!!! failure "Raises"
    - NumojoError: If the input arrays do not have the same shape.


</div>
