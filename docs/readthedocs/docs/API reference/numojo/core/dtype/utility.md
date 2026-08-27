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

<div class="overload-divider">Overload 1</div>

```mojo
def is_inttype[dtype: DType]() -> Bool
```

Check if the given dtype is an integer type at compile time.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Returns</div>

- `Bool`

<div class="overload-divider">Overload 2</div>

```mojo
def is_inttype(dtype: DType) -> Bool
```

Check if the given dtype is an integer type at run time.

<div class="prose-label">Args</div>

- `dtype` (`DType`) `[imm]`: DType.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

### `is_floattype`

<div class="overload-divider">Overload 1</div>

```mojo
def is_floattype[dtype: DType]() -> Bool
```

Check if the given dtype is a floating point type at compile time.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Returns</div>

- `Bool`

<div class="overload-divider">Overload 2</div>

```mojo
def is_floattype(dtype: DType) -> Bool
```

Check if the given dtype is a floating point type at run time.

<div class="prose-label">Args</div>

- `dtype` (`DType`) `[imm]`: DType.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

### `is_booltype`

<div class="overload-divider">Overload 1</div>

```mojo
def is_booltype[dtype: DType]() -> Bool
```

Check if the given dtype is a boolean type at compile time.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Returns</div>

- `Bool`

<div class="overload-divider">Overload 2</div>

```mojo
def is_booltype(dtype: DType) -> Bool
```

Check if the given dtype is a boolean type at run time.

<div class="prose-label">Args</div>

- `dtype` (`DType`) `[imm]`: DType.

<div class="prose-label">Returns</div>

- `Bool`


</div>
