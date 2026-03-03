# `numojo.routines.logic.logical_ops`

Logical Operations Module (numojo.routines.logic.logical_ops)

This module implements element-wise logical operations for NDArray, ComplexNDArray, and Matrix types in the NuMojo library.

## Functions


<div class="fn-card" markdown="1">

### `logical_and`

#### Overload 1

```mojo
logical_and[dtype: DType](a: NDArray[dtype], b: NDArray[dtype]) -> NDArray[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool)._mlir_value else dtype.is_integral()
```

Element-wise logical AND operation between two arrays.

Notes:
- Supports only boolean and integral data types.

Example:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_and

var a = nm.arange(0, 10)
var b = nm.arange(5, 15)
var result = logical_and(a > 3, b < 10)
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray`): First input array.
- `b` (`NDArray`): Second input array.

**Returns:**

- `NDArray`

!!! failure "Raises"
    - ShapeError: If the input arrays do not have the same shape.

#### Overload 2

```mojo
logical_and[cdtype: ComplexDType](a: ComplexNDArray[cdtype], b: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype] where (cdtype == ComplexDType.bool) if (cdtype == ComplexDType.bool) else cdtype.is_integral()
```

Element-wise logical AND operation between two arrays.

Notes:
- Supports only boolean and integral data types.

Example:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_and

var a = nm.arange(0, 10)
var b = nm.arange(5, 15)
var result = logical_and(a > 3, b < 10)
```

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `a` (`ComplexNDArray`): First input array.
- `b` (`ComplexNDArray`): Second input array.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"
    - ShapeError: If the input arrays do not have the same shape.

#### Overload 3

```mojo
logical_and[dtype: DType](a: Matrix[dtype], b: Matrix[dtype]) -> Matrix[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool)._mlir_value else dtype.is_integral()
```

Element-wise logical AND operation between two matrices.

Notes:
- Supports only boolean and integral data types.

Example:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_and

var a = Matrix.rand[i32]((2, 5))
var b = Matrix.rand[i32]((2, 5))
var result = logical_and(a > 3, b < 10)
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`Matrix`): First input matrix.
- `b` (`Matrix`): Second input matrix.

**Returns:**

- `Matrix`

!!! failure "Raises"
    - ShapeError: If the input matrices do not have the same shape.


</div>

<div class="fn-card" markdown="1">

### `logical_or`

#### Overload 1

```mojo
logical_or[dtype: DType](a: NDArray[dtype], b: NDArray[dtype]) -> NDArray[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool)._mlir_value else dtype.is_integral()
```

Element-wise logical OR operation between two arrays.

Notes:
- Supports only boolean and integral data types.

Example:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_or

var a = nm.arange(0, 10)
var b = nm.arange(5, 15)
var result = logical_or(a < 3, b > 10)
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray`): First input array.
- `b` (`NDArray`): Second input array.

**Returns:**

- `NDArray`

!!! failure "Raises"
    - ShapeError: If the input arrays do not have the same shape.

#### Overload 2

```mojo
logical_or[cdtype: ComplexDType](a: ComplexNDArray[cdtype], b: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype] where (cdtype == ComplexDType.bool) if (cdtype == ComplexDType.bool) else cdtype.is_integral()
```

Element-wise logical OR operation between two arrays.

Notes:
- Supports only boolean and integral data types.

Example:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_or

var a = nm.arange(0, 10)
var b = nm.arange(5, 15)
var result = logical_or(a < 3, b > 10)
```

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `a` (`ComplexNDArray`): First input array.
- `b` (`ComplexNDArray`): Second input array.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"
    - ShapeError: If the input arrays do not have the same shape.

#### Overload 3

```mojo
logical_or[dtype: DType](a: Matrix[dtype], b: Matrix[dtype]) -> Matrix[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool)._mlir_value else dtype.is_integral()
```

Element-wise logical OR operation between two matrices.

Notes:
- Supports only boolean and integral data types.

Example:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_or
var a = Matrix.rand[i32]((2, 5))
var b = Matrix.rand[i32]((2, 5))
var result = logical_or(a < 3, b > 10)
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`Matrix`): First input matrix.
- `b` (`Matrix`): Second input matrix.

**Returns:**

- `Matrix`

!!! failure "Raises"
    - ShapeError: If the input matrices do not have the same shape.


</div>

<div class="fn-card" markdown="1">

### `logical_not`

#### Overload 1

```mojo
logical_not[dtype: DType](a: NDArray[dtype]) -> NDArray[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool)._mlir_value else dtype.is_integral()
```

Element-wise logical NOT operation on an array.

Notes:
- Supports only boolean and integral data types.

Example:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_not

var a = nm.arange(0, 10)
var result = logical_not(a < 5)
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray`): Input array.

**Returns:**

- `NDArray`

!!! failure "Raises"
    - ShapeError: If the input array is not of a supported data type.

#### Overload 2

```mojo
logical_not[cdtype: ComplexDType](a: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype] where (cdtype == ComplexDType.bool) if (cdtype == ComplexDType.bool) else cdtype.is_integral()
```

Element-wise logical NOT operation on an array.

Notes:
- Supports only boolean and integral data types.

Example:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_not

var a = nm.arange(0, 10)
var result = logical_not(a < 5)
```

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `a` (`ComplexNDArray`): Input array.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"
    - ShapeError: If the input array is not of a supported data type.

#### Overload 3

```mojo
logical_not[dtype: DType](a: Matrix[dtype]) -> Matrix[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool)._mlir_value else dtype.is_integral()
```

Element-wise logical NOT operation on a matrix.

Notes:
- Supports only boolean and integral data types.

Example:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_not
var a = Matrix.rand[i32]((2, 5))
var result = logical_not(a < 5)
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`Matrix`): Input matrix.

**Returns:**

- `Matrix`

!!! failure "Raises"
    - ShapeError: If the input matrix is not of a supported data type.


</div>

<div class="fn-card" markdown="1">

### `logical_xor`

#### Overload 1

```mojo
logical_xor[dtype: DType](a: NDArray[dtype], b: NDArray[dtype]) -> NDArray[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool)._mlir_value else dtype.is_integral()
```

Element-wise logical XOR operation between two arrays.

Notes:
- Supports only boolean and integral data types.

Example:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_xor

var a = nm.arange(0, 10)
var b = nm.arange(5, 15)
var result = logical_xor(a > 3, b < 10)
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray`): First input array.
- `b` (`NDArray`): Second input array.

**Returns:**

- `NDArray`

!!! failure "Raises"
    - ShapeError: If the input arrays do not have the same shape.

#### Overload 2

```mojo
logical_xor[cdtype: ComplexDType](a: ComplexNDArray[cdtype], b: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype] where (cdtype == ComplexDType.bool) if (cdtype == ComplexDType.bool) else cdtype.is_integral()
```

Element-wise logical XOR operation between two arrays.

Notes:
- Supports only boolean and integral data types.

Example:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_xor

var a = nm.arange(0, 10)
var b = nm.arange(5, 15)
var result = logical_xor(a > 3, b < 10)
```

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `a` (`ComplexNDArray`): First input array.
- `b` (`ComplexNDArray`): Second input array.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"
    - ShapeError: If the input arrays do not have the same shape.

#### Overload 3

```mojo
logical_xor[dtype: DType](a: Matrix[dtype], b: Matrix[dtype]) -> Matrix[DType.bool] where (dtype == DType.bool) if (dtype == DType.bool)._mlir_value else dtype.is_integral()
```

Element-wise logical XOR operation between two matrices.

Notes:
- Supports only boolean and integral data types.

Example:
```mojo
from numojo.prelude import *
from numojo.routines.logic.logical_ops import logical_xor
var a = Matrix.rand[i32]((2, 5))
var b = Matrix.rand[i32]((2, 5))
var result = logical_xor(a > 3, b < 10)
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`Matrix`): First input matrix.
- `b` (`Matrix`): Second input matrix.

**Returns:**

- `Matrix`

!!! failure "Raises"
    - ShapeError: If the input matrices do not have the same shape.


</div>
