# `numojo.routines.io.formatting`

Array and value formatting utilities.

Functions for formatting arrays and values for printing with options for
precision, scientific notation, and complex number formatting.

Exports
-------
- `format_array`: Format array for display.
- `format_value`: Format scalar value.

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

**Value:** `PrintOptions(Int(4), False, String(DEFAULT_SEPARATOR), String(DEFAULT_PADDING), Int(15), Int(75), Int(2), False, String(DEFAULT_FLOAT_FORMAT), String(DEFAULT_COMPLEX_FORMAT), String(DEFAULT_NAN_STRING), String(DEFAULT_INF_STRING), Int(6), Int(4), False)`

## Structs

### `PrintOptions`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct PrintOptions
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`

</div>

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

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

```mojo
def __init__(out self, precision: Int = Int(4), suppress_small: Bool = False, separator: String = DEFAULT_SEPARATOR, padding: String = DEFAULT_PADDING, threshold: Int = Int(15), line_width: Int = Int(75), edge_items: Int = Int(2), sign: Bool = False, float_format: String = DEFAULT_FLOAT_FORMAT, complex_format: String = DEFAULT_COMPLEX_FORMAT, nan_string: String = DEFAULT_NAN_STRING, inf_string: String = DEFAULT_INF_STRING, formatted_width: Int = Int(6), exponent_threshold: Int = Int(4), suppress_scientific: Bool = False)
```

<span class="badge badge-static">static</span>

<div class="prose-label">Args</div>

- `precision` (`Int`) `[imm]`
- `suppress_small` (`Bool`) `[imm]`
- `separator` (`String`) `[imm]`
- `padding` (`String`) `[imm]`
- `threshold` (`Int`) `[imm]`
- `line_width` (`Int`) `[imm]`
- `edge_items` (`Int`) `[imm]`
- `sign` (`Bool`) `[imm]`
- `float_format` (`String`) `[imm]`
- `complex_format` (`String`) `[imm]`
- `nan_string` (`String`) `[imm]`
- `inf_string` (`String`) `[imm]`
- `formatted_width` (`Int`) `[imm]`
- `exponent_threshold` (`Int`) `[imm]`
- `suppress_scientific` (`Bool`) `[imm]`
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `set_options`

```mojo
def set_options(mut self, precision: Int = Int(4), suppress_small: Bool = False, separator: String = DEFAULT_SEPARATOR, padding: String = DEFAULT_PADDING, threshold: Int = Int(15), line_width: Int = Int(75), edge_items: Int = Int(2), sign: Bool = False, float_format: String = DEFAULT_FLOAT_FORMAT, complex_format: String = DEFAULT_COMPLEX_FORMAT, nan_string: String = DEFAULT_NAN_STRING, inf_string: String = DEFAULT_INF_STRING, formatted_width: Int = Int(6), exponent_threshold: Int = Int(4), suppress_scientific: Bool = False)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `precision` (`Int`) `[imm]`
- `suppress_small` (`Bool`) `[imm]`
- `separator` (`String`) `[imm]`
- `padding` (`String`) `[imm]`
- `threshold` (`Int`) `[imm]`
- `line_width` (`Int`) `[imm]`
- `edge_items` (`Int`) `[imm]`
- `sign` (`Bool`) `[imm]`
- `float_format` (`String`) `[imm]`
- `complex_format` (`String`) `[imm]`
- `nan_string` (`String`) `[imm]`
- `inf_string` (`String`) `[imm]`
- `formatted_width` (`Int`) `[imm]`
- `exponent_threshold` (`Int`) `[imm]`
- `suppress_scientific` (`Bool`) `[imm]`


</div>

<div class="fn-card" markdown="1">

#### `__enter__`

```mojo
def __enter__(mut self) -> Self
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__exit__`

```mojo
def __exit__(mut self)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`


</div>
## Functions


<div class="fn-card" markdown="1">

### `set_printoptions`

```mojo
def set_printoptions(precision: Int = Int(4), suppress_small: Bool = False, separator: String = DEFAULT_SEPARATOR, padding: String = DEFAULT_PADDING, edge_items: Int = Int(2))
```

<div class="prose-label">Args</div>

- `precision` (`Int`) `[imm]`
- `suppress_small` (`Bool`) `[imm]`
- `separator` (`String`) `[imm]`
- `padding` (`String`) `[imm]`
- `edge_items` (`Int`) `[imm]`


</div>

<div class="fn-card" markdown="1">

### `format_floating_scientific`

```mojo
def format_floating_scientific[dtype: DType = DType.float64](x: Scalar[dtype], precision: Int = Int(10), sign: Bool = False, suppress_scientific: Bool = False, exponent_threshold: Int = Int(4), formatted_width: Int = Int(8)) -> String
```

Format a float in scientific notation.

Notes: A scientific notation takes the form `-a.bbbbe+ii`. It will take
`7 + precision` letters in total.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Datatype of the float.

<div class="prose-label">Args</div>

- `x` (`Scalar[dtype]`) `[imm]`: The float to format.
- `precision` (`Int`) `[imm]`: The number of decimal places to include in the mantissa.
- `sign` (`Bool`) `[imm]`: Whether to include the sign of the float in the result. Defaults to False.
- `suppress_scientific` (`Bool`) `[imm]`: Whether to suppress scientific notation for small numbers.
    Defaults to False.
- `exponent_threshold` (`Int`) `[imm]`: The threshold for suppressing scientific notation.
    Defaults to 4.
- `formatted_width` (`Int`) `[imm]`: The width of the formatted string. Defaults to 8.

<div class="prose-label">Returns</div>

- `String`

!!! failure "Raises"
    NumojoError: If the dtype is not a floating-point type or if precision is negative.


</div>

<div class="fn-card" markdown="1">

### `format_floating_precision`

<div class="overload-divider">Overload 1</div>

```mojo
def format_floating_precision[dtype: DType](value: Scalar[dtype], precision: Int, sign: Bool = False, suppress_small: Bool = False) -> String
```

Format a floating-point value to the specified precision.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `value` (`Scalar[dtype]`) `[imm]`: The value to format.
- `precision` (`Int`) `[imm]`: The number of decimal places to include.
- `sign` (`Bool`) `[imm]`: Whether to include the sign of the float in the result.
    Defaults to False.
- `suppress_small` (`Bool`) `[imm]`: Whether to suppress small numbers. Defaults to False.

<div class="prose-label">Returns</div>

- `String`

!!! failure "Raises"
    NumojoError: If precision is negative or if the value cannot be formatted.

<div class="overload-divider">Overload 2</div>

```mojo
def format_floating_precision[cdtype: ComplexDType](value: ComplexSIMD[cdtype], precision: Int = Int(4), sign: Bool = False) -> String
```

Format a complex floating-point value to the specified precision.

<div class="prose-label">Parameters</div>

- `cdtype` (`ComplexDType`)

<div class="prose-label">Args</div>

- `value` (`ComplexSIMD[cdtype]`) `[imm]`: The complex value to format.
- `precision` (`Int`) `[imm]`: The number of decimal places to include.
- `sign` (`Bool`) `[imm]`: Whether to include the sign of the float in the result.
    Defaults to False.

<div class="prose-label">Returns</div>

- `String`

!!! failure "Raises"
    NumojoError: If the complex value cannot be formatted.


</div>

<div class="fn-card" markdown="1">

### `format_value`

<div class="overload-divider">Overload 1</div>

```mojo
def format_value[dtype: DType](value: Scalar[dtype], print_options: PrintOptions) -> String
```

Format a single value based on the print options.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `value` (`Scalar[dtype]`) `[imm]`: The value to format.
- `print_options` (`PrintOptions`) `[imm]`: The print options.

<div class="prose-label">Returns</div>

- `String`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def format_value[cdtype: ComplexDType](value: ComplexSIMD[cdtype], print_options: PrintOptions) -> String
```

Format a complex value based on the print options.

<div class="prose-label">Parameters</div>

- `cdtype` (`ComplexDType`)

<div class="prose-label">Args</div>

- `value` (`ComplexSIMD[cdtype]`) `[imm]`: The complex value to format.
- `print_options` (`PrintOptions`) `[imm]`: The print options.

<div class="prose-label">Returns</div>

- `String`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
