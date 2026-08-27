# `numojo.routines.math.arithmetic`

Basic arithmetic operations: addition, subtraction, multiplication, division, and related functions.

This module provides element-wise arithmetic operations for NDArrays supporting both
array-array and array-scalar operations.

Exports
-------
- `add`: Element-wise addition.
- `sub`: Element-wise subtraction.
- `mul`: Element-wise multiplication.
- `div`: Element-wise division.
- `floor_div`: Element-wise floor division.
- `mod`: Element-wise modulo.
- `remainder`: Element-wise remainder.
- `fma`: Fused multiply-add.

## Functions


<div class="fn-card" markdown="1">

### `add`

#### Overload 1

```mojo
def add[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Perform addition on two arrays.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def add[dtype: DType](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Perform addition on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: A Scalar.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def add[dtype: DType](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Perform addition on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `scalar` (`Scalar[dtype]`) `[imm]`: A Scalar.
- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 4

```mojo
def add[dtype: DType](var *values: Variant[NDArray[dtype], Scalar[dtype]]) -> NDArray[dtype]
```

Perform addition on a list of arrays and a scalars.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `*values` (`Variant[NDArray[dtype], Scalar[dtype]]`) `[var]`: A list of arrays or Scalars to be added.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If there are no arrays in the input values.


</div>

<div class="fn-card" markdown="1">

### `sub`

#### Overload 1

```mojo
def sub[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Perform subtraction on two arrays.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def sub[dtype: DType](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Perform subtraction on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: A Scalar.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def sub[dtype: DType](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Perform subtraction on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `scalar` (`Scalar[dtype]`) `[imm]`: A Scalar.
- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `mod`

#### Overload 1

```mojo
def mod[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise modulo of array1 and array2.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def mod[dtype: DType](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Element-wise modulo between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: A Scalar.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def mod[dtype: DType](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise modulo between a scalar and an array.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `scalar` (`Scalar[dtype]`) `[imm]`: A Scalar.
- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `mul`

#### Overload 1

```mojo
def mul[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise product of array1 and array2.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def mul[dtype: DType](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Perform multiplication on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: A Scalar.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def mul[dtype: DType](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Perform multiplication on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `scalar` (`Scalar[dtype]`) `[imm]`: A Scalar.
- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 4

```mojo
def mul[dtype: DType](var *values: Variant[NDArray[dtype], Scalar[dtype]]) -> NDArray[dtype]
```

Perform multiplication on a list of arrays an arrays and a scalars.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `*values` (`Variant[NDArray[dtype], Scalar[dtype]]`) `[var]`: A list of arrays or Scalars to be added.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If there are no arrays in the input values.


</div>

<div class="fn-card" markdown="1">

### `div`

#### Overload 1

```mojo
def div[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise quotient of array1 and array2.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def div[dtype: DType](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Perform true division on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: A Scalar.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def div[dtype: DType](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Perform true division between a scalar and an array.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `scalar` (`Scalar[dtype]`) `[imm]`: A Scalar.
- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `floor_div`

#### Overload 1

```mojo
def floor_div[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise quotient of array1 and array2.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def floor_div[dtype: DType](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Perform true division on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: A Scalar.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def floor_div[dtype: DType](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Perform true division on between an array and a scalar.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `scalar` (`Scalar[dtype]`) `[imm]`: A Scalar.
- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `fma`

#### Overload 1

```mojo
def fma[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[dtype]
```

Apply a SIMD level fuse multiply add function of three variables and one return to a NDArray.

!!! info "Constraints"
    Both arrays must have the same shape.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array3` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def fma[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype], simd: Scalar[dtype]) -> NDArray[dtype]
```

Apply a SIMD level fuse multiply add function of three variables and one return to a NDArray.

!!! info "Constraints"
    Both arrays must have the same shape

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `simd` (`Scalar[dtype]`) `[imm]`: A SIMD[dtype,1] value to be added.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `remainder`

#### Overload 1

```mojo
def remainder[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise remainders of NDArray.

!!! info "Constraints"
    Both arrays must have the same shapes.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def remainder[dtype: DType](array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Element-wise remainders of NDArray.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: A scalar.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def remainder[dtype: DType](scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Element-wise remainders of NDArray.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `scalar` (`Scalar[dtype]`) `[imm]`: A scalar.
- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>
