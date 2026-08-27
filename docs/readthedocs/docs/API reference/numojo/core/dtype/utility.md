# `numojo.core.dtype.utility`

Type checking utilities for DType inspection.

Functions for checking properties of data types (DType) at both compile time
and runtime.

Exports
-------
- `is_inttype`: Check if DType is integer.
- `is_floattype`: Check if DType is floating-point.
- `is_complextype`: Check if DType is complex.

## Functions


<div class="fn-card" markdown="1">

### `is_inttype`

#### Overload 1

```mojo
def is_inttype[dtype: DType]() -> Bool
```

Check if the given dtype is an integer type at compile time.

**Parameters:**

- `dtype` (`DType`): DType.

**Returns:**

- `Bool`

#### Overload 2

```mojo
def is_inttype(dtype: DType) -> Bool
```

Check if the given dtype is an integer type at run time.

**Args:**

- `dtype` (`DType`) `[imm]`: DType.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

### `is_floattype`

#### Overload 1

```mojo
def is_floattype[dtype: DType]() -> Bool
```

Check if the given dtype is a floating point type at compile time.

**Parameters:**

- `dtype` (`DType`): DType.

**Returns:**

- `Bool`

#### Overload 2

```mojo
def is_floattype(dtype: DType) -> Bool
```

Check if the given dtype is a floating point type at run time.

**Args:**

- `dtype` (`DType`) `[imm]`: DType.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

### `is_booltype`

#### Overload 1

```mojo
def is_booltype[dtype: DType]() -> Bool
```

Check if the given dtype is a boolean type at compile time.

**Parameters:**

- `dtype` (`DType`): DType.

**Returns:**

- `Bool`

#### Overload 2

```mojo
def is_booltype(dtype: DType) -> Bool
```

Check if the given dtype is a boolean type at run time.

**Args:**

- `dtype` (`DType`) `[imm]`: DType.

**Returns:**

- `Bool`


</div>
