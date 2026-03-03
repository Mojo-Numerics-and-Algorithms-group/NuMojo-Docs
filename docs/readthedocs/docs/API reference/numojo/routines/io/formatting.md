# `numojo.routines.io.formatting`

Formatting (numojo.routines.io.formatting)

This module provides functions for formatting arrays and values for printing, including options for precision, scientific notation, and complex number formatting.

## Aliases

### `DEFAULT_PRECISION`

```mojo
comptime DEFAULT_PRECISION
```

**Value:** `4`

### `DEFAULT_SUPPRESS_SMALL`

```mojo
comptime DEFAULT_SUPPRESS_SMALL
```

**Value:** `False`

### `DEFAULT_SEPARATOR`

```mojo
comptime DEFAULT_SEPARATOR
```

**Value:** `" "`

### `DEFAULT_PADDING`

```mojo
comptime DEFAULT_PADDING
```

**Value:** `""`

### `DEFAULT_EDGE_ITEMS`

```mojo
comptime DEFAULT_EDGE_ITEMS
```

**Value:** `2`

### `DEFAULT_THRESHOLD`

```mojo
comptime DEFAULT_THRESHOLD
```

**Value:** `15`

### `DEFAULT_LINE_WIDTH`

```mojo
comptime DEFAULT_LINE_WIDTH
```

**Value:** `75`

### `DEFAULT_SIGN`

```mojo
comptime DEFAULT_SIGN
```

**Value:** `False`

### `DEFAULT_FLOAT_FORMAT`

```mojo
comptime DEFAULT_FLOAT_FORMAT
```

**Value:** `"fixed"`

### `DEFAULT_COMPLEX_FORMAT`

```mojo
comptime DEFAULT_COMPLEX_FORMAT
```

**Value:** `"parentheses"`

### `DEFAULT_NAN_STRING`

```mojo
comptime DEFAULT_NAN_STRING
```

**Value:** `"nan"`

### `DEFAULT_INF_STRING`

```mojo
comptime DEFAULT_INF_STRING
```

**Value:** `"inf"`

### `DEFAULT_FORMATTED_WIDTH`

```mojo
comptime DEFAULT_FORMATTED_WIDTH
```

**Value:** `6`

### `DEFAULT_EXPONENT_THRESHOLD`

```mojo
comptime DEFAULT_EXPONENT_THRESHOLD
```

**Value:** `4`

### `DEFAULT_SUPPRESS_SCIENTIFIC`

```mojo
comptime DEFAULT_SUPPRESS_SCIENTIFIC
```

**Value:** `False`

### `GLOBAL_PRINT_OPTIONS`

```mojo
comptime GLOBAL_PRINT_OPTIONS
```

**Value:** `PrintOptions(4, False, DEFAULT_SEPARATOR, DEFAULT_PADDING, 15, 75, 2, False, DEFAULT_FLOAT_FORMAT, DEFAULT_COMPLEX_FORMAT, DEFAULT_NAN_STRING, DEFAULT_INF_STRING, 6, 4, False)`

## Structs

### `PrintOptions`

```mojo
struct PrintOptions
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `ImplicitlyCopyable`, `ImplicitlyDestructible`, `Movable`

#### Fields

- **`precision`** (`Int`): The number of decimal places to include in the formatted string. Defaults to 4.
- **`suppress_small`** (`Bool`)
- **`separator`** (`String`): The separator between elements in the array. Defaults to a space.
- **`padding`** (`String`): The padding symbol between the elements at the edge and the brackets. Defaults to an empty string.
- **`threshold`** (`Int`)
- **`line_width`** (`Int`)
- **`edge_items`** (`Int`): The number of items to display at the beginning and end of a dimension. Defaults to 3.
- **`sign`** (`Bool`)
- **`float_format`** (`String`)
- **`complex_format`** (`String`)
- **`nan_string`** (`String`)
- **`inf_string`** (`String`)
- **`formatted_width`** (`Int`): The width of the formatted string per element of array.
- **`exponent_threshold`** (`Int`)
- **`suppress_scientific`** (`Bool`)

#### Aliases

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `False`

##### `__move_ctor_is_trivial`

```mojo
comptime __move_ctor_is_trivial
```

**Value:** `True`

##### `__copy_ctor_is_trivial`

```mojo
comptime __copy_ctor_is_trivial
```

**Value:** `False`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
__init__(out self, precision: Int = 4, suppress_small: Bool = False, separator: String = DEFAULT_SEPARATOR, padding: String = DEFAULT_PADDING, threshold: Int = 15, line_width: Int = 75, edge_items: Int = 2, sign: Bool = False, float_format: String = DEFAULT_FLOAT_FORMAT, complex_format: String = DEFAULT_COMPLEX_FORMAT, nan_string: String = DEFAULT_NAN_STRING, inf_string: String = DEFAULT_INF_STRING, formatted_width: Int = 6, exponent_threshold: Int = 4, suppress_scientific: Bool = False)
```

<span class="badge badge-static">static</span>

**Args:**

- `precision` (`Int`)
- `suppress_small` (`Bool`)
- `separator` (`String`)
- `padding` (`String`)
- `threshold` (`Int`)
- `line_width` (`Int`)
- `edge_items` (`Int`)
- `sign` (`Bool`)
- `float_format` (`String`)
- `complex_format` (`String`)
- `nan_string` (`String`)
- `inf_string` (`String`)
- `formatted_width` (`Int`)
- `exponent_threshold` (`Int`)
- `suppress_scientific` (`Bool`)
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `set_options`

```mojo
set_options(mut self, precision: Int = 4, suppress_small: Bool = False, separator: String = DEFAULT_SEPARATOR, padding: String = DEFAULT_PADDING, threshold: Int = 15, line_width: Int = 75, edge_items: Int = 2, sign: Bool = False, float_format: String = DEFAULT_FLOAT_FORMAT, complex_format: String = DEFAULT_COMPLEX_FORMAT, nan_string: String = DEFAULT_NAN_STRING, inf_string: String = DEFAULT_INF_STRING, formatted_width: Int = 6, exponent_threshold: Int = 4, suppress_scientific: Bool = False)
```

**Args:**

- `self` (`Self`) `[mut]`
- `precision` (`Int`)
- `suppress_small` (`Bool`)
- `separator` (`String`)
- `padding` (`String`)
- `threshold` (`Int`)
- `line_width` (`Int`)
- `edge_items` (`Int`)
- `sign` (`Bool`)
- `float_format` (`String`)
- `complex_format` (`String`)
- `nan_string` (`String`)
- `inf_string` (`String`)
- `formatted_width` (`Int`)
- `exponent_threshold` (`Int`)
- `suppress_scientific` (`Bool`)


</div>

<div class="fn-card" markdown="1">

##### `__enter__`

```mojo
__enter__(mut self) -> Self
```

**Args:**

- `self` (`Self`) `[mut]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__exit__`

```mojo
__exit__(mut self)
```

**Args:**

- `self` (`Self`) `[mut]`


</div>
## Functions


<div class="fn-card" markdown="1">

### `set_printoptions`

```mojo
set_printoptions(precision: Int = 4, suppress_small: Bool = False, separator: String = DEFAULT_SEPARATOR, padding: String = DEFAULT_PADDING, edge_items: Int = 2)
```

**Args:**

- `precision` (`Int`)
- `suppress_small` (`Bool`)
- `separator` (`String`)
- `padding` (`String`)
- `edge_items` (`Int`)


</div>

<div class="fn-card" markdown="1">

### `format_floating_scientific`

```mojo
format_floating_scientific[dtype: DType = DType.float64](x: Scalar[dtype], precision: Int = 10, sign: Bool = False, suppress_scientific: Bool = False, exponent_threshold: Int = 4, formatted_width: Int = 8) -> String
```

Format a float in scientific notation.

Notes: A scientific notation takes the form `-a.bbbbe+ii`. It will take
`7 + precision` letters in total.

**Parameters:**

- `dtype` (`DType`): Datatype of the float.

**Args:**

- `x` (`Scalar`): The float to format.
- `precision` (`Int`): The number of decimal places to include in the mantissa.
- `sign` (`Bool`): Whether to include the sign of the float in the result. Defaults to False.
- `suppress_scientific` (`Bool`): Whether to suppress scientific notation for small numbers.
    Defaults to False.
- `exponent_threshold` (`Int`): The threshold for suppressing scientific notation.
    Defaults to 4.
- `formatted_width` (`Int`): The width of the formatted string. Defaults to 8.

**Returns:**

- `String`

!!! failure "Raises"
    Error: If the dtype is not a floating-point type or if precision is negative.


</div>

<div class="fn-card" markdown="1">

### `format_floating_precision`

#### Overload 1

```mojo
format_floating_precision[dtype: DType](value: Scalar[dtype], precision: Int, sign: Bool = False, suppress_small: Bool = False) -> String
```

Format a floating-point value to the specified precision.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `value` (`Scalar`): The value to format.
- `precision` (`Int`): The number of decimal places to include.
- `sign` (`Bool`): Whether to include the sign of the float in the result.
    Defaults to False.
- `suppress_small` (`Bool`): Whether to suppress small numbers. Defaults to False.

**Returns:**

- `String`

!!! failure "Raises"
    Error: If precision is negative or if the value cannot be formatted.

#### Overload 2

```mojo
format_floating_precision[cdtype: ComplexDType](value: ComplexSIMD[cdtype], precision: Int = 4, sign: Bool = False) -> String
```

Format a complex floating-point value to the specified precision.

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `value` (`ComplexSIMD`): The complex value to format.
- `precision` (`Int`): The number of decimal places to include.
- `sign` (`Bool`): Whether to include the sign of the float in the result.
    Defaults to False.

**Returns:**

- `String`

!!! failure "Raises"
    Error: If the complex value cannot be formatted.


</div>

<div class="fn-card" markdown="1">

### `format_value`

#### Overload 1

```mojo
format_value[dtype: DType](value: Scalar[dtype], print_options: PrintOptions) -> String
```

Format a single value based on the print options.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `value` (`Scalar`): The value to format.
- `print_options` (`PrintOptions`): The print options.

**Returns:**

- `String`

!!! failure "Raises"

#### Overload 2

```mojo
format_value[cdtype: ComplexDType](value: ComplexSIMD[cdtype], print_options: PrintOptions) -> String
```

Format a complex value based on the print options.

**Parameters:**

- `cdtype` (`ComplexDType`)

**Args:**

- `value` (`ComplexSIMD`): The complex value to format.
- `print_options` (`PrintOptions`): The print options.

**Returns:**

- `String`

!!! failure "Raises"


</div>
