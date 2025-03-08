



# formatting

##  Module Summary
  

## Aliases
  
`DEFAULT_PRECISION`:   
`DEFAULT_SUPPRESS_SMALL`:   
`DEFAULT_SEPARATOR`:   
`DEFAULT_PADDING`:   
`DEFAULT_EDGE_ITEMS`:   
`DEFAULT_THRESHOLD`:   
`DEFAULT_LINE_WIDTH`:   
`DEFAULT_SIGN`:   
`DEFAULT_FLOAT_FORMAT`:   
`DEFAULT_COMPLEX_FORMAT`:   
`DEFAULT_NAN_STRING`:   
`DEFAULT_INF_STRING`:   
`DEFAULT_FORMATTED_WIDTH`:   
`DEFAULT_EXPONENT_THRESHOLD`:   
`DEFAULT_SUPPRESS_SCIENTIFIC`:   
`GLOBAL_PRINT_OPTIONS`: 
## PrintOptions

### PrintOptions Summary
  
  
  

### Parent Traits
  

- AnyType
- Copyable
- ExplicitlyCopyable
- Movable
- UnknownDestructibility

### Fields
  
  
* precision `Int`  
    - The number of decimal places to include in the formatted string. Defaults to 4.  
* suppress_small `Bool`  
* separator `String`  
    - The separator between elements in the array. Defaults to a space.  
* padding `String`  
    - The padding symbol between the elements at the edge and the brackets. Defaults to an empty string.  
* threshold `Int`  
* line_width `Int`  
* edge_items `Int`  
    - The number of items to display at the beginning and end of a dimension. Defaults to 3.  
* sign `Bool`  
* float_format `String`  
* complex_format `String`  
* nan_string `String`  
* inf_string `String`  
* formatted_width `Int`  
    - The width of the formatted string per element of array.  
* exponent_threshold `Int`  
* suppress_scientific `Bool`  

### Functions

#### __init__


```rust
__init__(out self, precision: Int = 4, suppress_small: Bool = False, separator: String = String(" "), padding: String = String(""), threshold: Int = 10, line_width: Int = 75, edge_items: Int = 3, sign: Bool = False, float_format: String = String("fixed"), complex_format: String = String("parentheses"), nan_string: String = String("nan"), inf_string: String = String("inf"), formatted_width: Int = 8, exponent_threshold: Int = 4, suppress_scientific: Bool = False)
```  
Summary  
  
  
  
Args:  

- precision Default: 4
- suppress_small Default: False
- separator Default: String(" ")
- padding Default: String("")
- threshold Default: 10
- line_width Default: 75
- edge_items Default: 3
- sign Default: False
- float_format Default: String("fixed")
- complex_format Default: String("parentheses")
- nan_string Default: String("nan")
- inf_string Default: String("inf")
- formatted_width Default: 8
- exponent_threshold Default: 4
- suppress_scientific Default: False
- self

#### set_options


```rust
set_options(mut self, precision: Int = 4, suppress_small: Bool = False, separator: String = String(" "), padding: String = String(""), threshold: Int = 10, line_width: Int = 75, edge_items: Int = 3, sign: Bool = False, float_format: String = String("fixed"), complex_format: String = String("parentheses"), nan_string: String = String("nan"), inf_string: String = String("inf"), formatted_width: Int = 8, exponent_threshold: Int = 4, suppress_scientific: Bool = False)
```  
Summary  
  
  
  
Args:  

- self
- precision Default: 4
- suppress_small Default: False
- separator Default: String(" ")
- padding Default: String("")
- threshold Default: 10
- line_width Default: 75
- edge_items Default: 3
- sign Default: False
- float_format Default: String("fixed")
- complex_format Default: String("parentheses")
- nan_string Default: String("nan")
- inf_string Default: String("inf")
- formatted_width Default: 8
- exponent_threshold Default: 4
- suppress_scientific Default: False

#### __enter__


```rust
__enter__(mut self) -> Self
```  
Summary  
  
  
  
Args:  

- self

#### __exit__


```rust
__exit__(mut self)
```  
Summary  
  
  
  
Args:  

- self

## set_printoptions


```rust
set_printoptions(precision: Int = 4, suppress_small: Bool = False, separator: String = String(" "), padding: String = String(""), edge_items: Int = 3)
```  
Summary  
  
  
  
Args:  

- precision Default: 4
- suppress_small Default: False
- separator Default: String(" ")
- padding Default: String("")
- edge_items Default: 3

## format_floating_scientific


```rust
format_floating_scientific[dtype: DType = float64](x: SIMD[dtype, 1], precision: Int = 10, sign: Bool = False, suppress_scientific: Bool = False, exponent_threshold: Int = 4, formatted_width: Int = 8) -> String
```  
Summary  
  
Format a float in scientific notation.  
  
Parameters:  

- dtype: Datatype of the float. Defualt: `float64`
  
Args:  

- x: The float to format.
- precision: The number of decimal places to include in the mantissa. Default: 10
- sign: Whether to include the sign of the float in the result. Defaults to False. Default: False
- suppress_scientific: Whether to suppress scientific notation for small numbers. Defaults to False. Default: False
- exponent_threshold: The threshold for suppressing scientific notation. Defaults to 4. Default: 4
- formatted_width: The width of the formatted string. Defaults to 8. Default: 8

## format_floating_precision


```rust
format_floating_precision[dtype: DType](value: SIMD[dtype, 1], precision: Int, sign: Bool = False, suppress_small: Bool = False) -> String
```  
Summary  
  
Format a floating-point value to the specified precision.  
  
Parameters:  

- dtype
  
Args:  

- value: The value to format.
- precision: The number of decimal places to include.
- sign: Whether to include the sign of the float in the result. Defaults to False. Default: False
- suppress_small: Whether to suppress small numbers. Defaults to False. Default: False


```rust
format_floating_precision[cdtype: CDType, dtype: DType](value: ComplexSIMD[cdtype, dtype=dtype], precision: Int = 4, sign: Bool = False) -> String
```  
Summary  
  
Format a complex floating-point value to the specified precision.  
  
Parameters:  

- cdtype
- dtype
  
Args:  

- value: The complex value to format.
- precision: The number of decimal places to include. Default: 4
- sign: Whether to include the sign of the float in the result. Defaults to False. Default: False

## format_value


```rust
format_value[dtype: DType](value: SIMD[dtype, 1], print_options: PrintOptions) -> String
```  
Summary  
  
Format a single value based on the print options.  
  
Parameters:  

- dtype
  
Args:  

- value: The value to format.
- print_options: The print options.


```rust
format_value[cdtype: CDType, dtype: DType](value: ComplexSIMD[cdtype, dtype=dtype], print_options: PrintOptions) -> String
```  
Summary  
  
Format a complex value based on the print options.  
  
Parameters:  

- cdtype
- dtype
  
Args:  

- value: The complex value to format.
- print_options: The print options.
