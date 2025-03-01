



# complex_dtype

##  Module Summary
  

## CDType

### CDType Summary
  
  
Represents CDType and provides methods for working with it.  

### Parent Traits
  

- AnyType
- CollectionElement
- CollectionElementNew
- Copyable
- EqualityComparable
- EqualityComparableCollectionElement
- ExplicitlyCopyable
- Hashable
- KeyElement
- Movable
- Representable
- Stringable
- UnknownDestructibility
- Writable
- _HashableWithHasher

### Aliases
  
`type`:   
`invalid`: Represents an invalid or unknown data type.  
`bool`: Represents a boolean data type.  
`int8`: Represents a signed integer type whose bitwidth is 8.  
`uint8`: Represents an unsigned integer type whose bitwidth is 8.  
`int16`: Represents a signed integer type whose bitwidth is 16.  
`uint16`: Represents an unsigned integer type whose bitwidth is 16.  
`int32`: Represents a signed integer type whose bitwidth is 32.  
`uint32`: Represents an unsigned integer type whose bitwidth is 32.  
`int64`: Represents a signed integer type whose bitwidth is 64.  
`uint64`: Represents an unsigned integer type whose bitwidth is 64.  
`float8_e5m2`: Represents a FP8E5M2 floating point format from the [OFP8 standard](https://www.opencompute.org/documents/ocp-8-bit-floating-point-specification-ofp8-revision-1-0-2023-12-01-pdf-1).  
`float8_e5m2fnuz`: Represents a FP8E5M2FNUZ floating point format.  
`float8_e4m3`: Represents a FP8E4M3 floating point format from the [OFP8 standard](https://www.opencompute.org/documents/ocp-8-bit-floating-point-specification-ofp8-revision-1-0-2023-12-01-pdf-1).  
`float8_e4m3fnuz`: Represents a FP8E4M3FNUZ floating point format.  
`bfloat16`: Represents a brain floating point value whose bitwidth is 16.  
`float16`: Represents an IEEE754-2008 `binary16` floating point value.  
`float32`: Represents an IEEE754-2008 `binary32` floating point value.  
`tensor_float32`: Represents a special floating point format supported by NVIDIA Tensor Cores, with the same range as float32 and reduced precision (>=10 bits). Note that this type is only available on NVIDIA GPUs.  
`float64`: Represents an IEEE754-2008 `binary64` floating point value.  
`index`: Represents an integral type whose bitwidth is the maximum integral value on the system.
### Fields
  
  
* re_value `dtype`  
* im_value `dtype`  

### Functions

#### __init__


```rust
__init__(*, other: Self) -> Self
```  
Summary  
  
Copy this CDType.  
  
Args:  

- other


```rust
__init__(re_value: dtype, im_value: dtype) -> Self
```  
Summary  
  
Construct a CDType from MLIR dtype.  
  
Args:  

- re_value
- im_value

#### __eq__


```rust
__eq__(self, rhs: Self) -> Bool
```  
Summary  
  
Compares one CDType to another for equality.  
  
Args:  

- self
- rhs

#### __ne__


```rust
__ne__(self, rhs: Self) -> Bool
```  
Summary  
  
Compares one CDType to another for inequality.  
  
Args:  

- self
- rhs

#### __is__


```rust
__is__(self, rhs: Self) -> Bool
```  
Summary  
  
Compares one CDType to another for equality.  
  
Args:  

- self
- rhs

#### __isnot__


```rust
__isnot__(self, rhs: Self) -> Bool
```  
Summary  
  
Compares one CDType to another for inequality.  
  
Args:  

- self
- rhs

#### to_dtype


```rust
to_dtype[other: Self]() -> DType
```  
Summary  
  
Find the equivalent DType.  
  
Parameters:  

- other

#### __str__


```rust
__str__(self) -> String
```  
Summary  
  
Gets the name of the CDType.  
  
Args:  

- self

#### write_to


```rust
write_to[W: Writer](self, mut writer: W)
```  
Summary  
  
Formats this dtype to the provided Writer.  
  
Parameters:  

- W: A type conforming to the Writable trait.
  
Args:  

- self
- writer

#### __repr__


```rust
__repr__(self) -> String
```  
Summary  
  
Gets the representation of the CDType e.g. `"CDType.float32"`.  
  
Args:  

- self

#### get_value


```rust
get_value(self) -> dtype
```  
Summary  
  
Gets the associated internal kgen.dtype value.  
  
Args:  

- self

#### __hash__


```rust
__hash__(self) -> UInt
```  
Summary  
  
Return a 64-bit hash for this `CDType` value.  
  
Args:  

- self


```rust
__hash__[H: _Hasher](self, mut hasher: H)
```  
Summary  
  
Updates hasher with this `CDType` value.  
  
Parameters:  

- H: The hasher type.
  
Args:  

- self
- hasher

#### is_unsigned


```rust
is_unsigned(self) -> Bool
```  
Summary  
  
Returns True if the type parameter is unsigned and False otherwise.  
  
Args:  

- self

#### is_signed


```rust
is_signed(self) -> Bool
```  
Summary  
  
Returns True if the type parameter is signed and False otherwise.  
  
Args:  

- self

#### is_integral


```rust
is_integral(self) -> Bool
```  
Summary  
  
Returns True if the type parameter is an integer and False otherwise.  
  
Args:  

- self

#### is_floating_point


```rust
is_floating_point(self) -> Bool
```  
Summary  
  
Returns True if the type parameter is a floating-point and False otherwise.  
  
Args:  

- self

#### is_float8


```rust
is_float8(self) -> Bool
```  
Summary  
  
Returns True if the type is a 8bit-precision floating point type, e.g. float8_e5m2, float8_e5m2fnuz, float8_e4m3 and float8_e4m3fnuz.  
  
Args:  

- self

#### is_half_float


```rust
is_half_float(self) -> Bool
```  
Summary  
  
Returns True if the type is a half-precision floating point type, e.g. either fp16 or bf16.  
  
Args:  

- self

#### is_numeric


```rust
is_numeric(self) -> Bool
```  
Summary  
  
Returns True if the type parameter is numeric (i.e. you can perform arithmetic operations on).  
  
Args:  

- self

#### sizeof


```rust
sizeof(self) -> Int
```  
Summary  
  
Returns the size in bytes of the current CDType.  
  
Args:  

- self

#### bitwidth


```rust
bitwidth(self) -> Int
```  
Summary  
  
Returns the size in bits of the current CDType.  
  
Args:  

- self

#### dispatch_integral


```rust
dispatch_integral[: origin.set, //, func: fn[CDType]() capturing -> None](self)
```  
Summary  
  
Dispatches an integral function corresponding to the current CDType.  
  
Parameters:  

- 
- func: A parametrized on dtype function to dispatch.
  
Constraints:

CDType must be integral.  
  
Args:  

- self

#### dispatch_floating


```rust
dispatch_floating[: origin.set, //, func: fn[CDType]() capturing -> None](self)
```  
Summary  
  
Dispatches a floating-point function corresponding to the current CDType.  
  
Parameters:  

- 
- func: A parametrized on dtype function to dispatch.
  
Constraints:

CDType must be floating-point or integral.  
  
Args:  

- self

#### dispatch_arithmetic


```rust
dispatch_arithmetic[: origin.set, //, func: fn[CDType]() capturing -> None](self)
```  
Summary  
  
Dispatches a function corresponding to the current CDType.  
  
Parameters:  

- 
- func: A parametrized on dtype function to dispatch.
  
Args:  

- self
