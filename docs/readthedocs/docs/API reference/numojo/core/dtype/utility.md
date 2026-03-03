# `numojo.core.dtype.utility`

Data type utility functions (numojo.core.dtype.utility)

This module provides utility functions for checking properties of data types (DType) at both compile time and run time.

## Functions


<div class="fn-card" markdown="1">

### `is_inttype`

#### Overload 1

```mojo
is_inttype[dtype: DType]() -> Bool
```

Check if the given dtype is an integer type at compile time.

**Parameters:**

- `dtype` (`DType`): DType.

**Returns:**

- `Bool`

#### Overload 2

```mojo
is_inttype(dtype: DType) -> Bool
```

Check if the given dtype is an integer type at run time.

**Args:**

- `dtype` (`DType`): DType.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

### `is_floattype`

#### Overload 1

```mojo
is_floattype[dtype: DType]() -> Bool
```

Check if the given dtype is a floating point type at compile time.

**Parameters:**

- `dtype` (`DType`): DType.

**Returns:**

- `Bool`

#### Overload 2

```mojo
is_floattype(dtype: DType) -> Bool
```

Check if the given dtype is a floating point type at run time.

**Args:**

- `dtype` (`DType`): DType.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

### `is_booltype`

#### Overload 1

```mojo
is_booltype[dtype: DType]() -> Bool
```

Check if the given dtype is a boolean type at compile time.

**Parameters:**

- `dtype` (`DType`): DType.

**Returns:**

- `Bool`

#### Overload 2

```mojo
is_booltype(dtype: DType) -> Bool
```

Check if the given dtype is a boolean type at run time.

**Args:**

- `dtype` (`DType`): DType.

**Returns:**

- `Bool`


</div>
