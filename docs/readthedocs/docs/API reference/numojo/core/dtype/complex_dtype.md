# `numojo.core.dtype.complex_dtype`

Complex number type definitions and utilities.

Type aliases and utilities for working with complex data types in NuMojo,
including Rust-like and NumPy-like aliases.

Exports
-------
- Complex integer types: `ci8`, `ci16`, `ci32`, `ci64`, `ci128`, `ci256`
- Complex unsigned types: `cu8`, `cu16`, `cu32`, `cu64`, `cu128`
- Complex float types: `cf32`, `cf64`
- `ComplexDType`: Complex dtype enumeration.

## Aliases

### `ci8`

```mojo
comptime ci8
```

**Value:** `ComplexDType.int8`

Data type comptime for ComplexDType.int8.

### `ci16`

```mojo
comptime ci16
```

**Value:** `ComplexDType.int16`

Data type comptime for ComplexDType.int16.

### `ci32`

```mojo
comptime ci32
```

**Value:** `ComplexDType.int32`

Data type comptime for ComplexDType.int32.

### `ci64`

```mojo
comptime ci64
```

**Value:** `ComplexDType.int64`

Data type comptime for ComplexDType.int64.

### `ci128`

```mojo
comptime ci128
```

**Value:** `ComplexDType.int128`

Data type comptime for ComplexDType.int128.

### `ci256`

```mojo
comptime ci256
```

**Value:** `ComplexDType.int256`

Data type comptime for ComplexDType.int256.

### `cint`

```mojo
comptime cint
```

**Value:** `ComplexDType.int`

Data type comptime for ComplexDType.int.

### `cu8`

```mojo
comptime cu8
```

**Value:** `ComplexDType.uint8`

Data type comptime for ComplexDType.uint8.

### `cu16`

```mojo
comptime cu16
```

**Value:** `ComplexDType.uint16`

Data type comptime for ComplexDType.uint16.

### `cu32`

```mojo
comptime cu32
```

**Value:** `ComplexDType.uint32`

Data type comptime for ComplexDType.uint32.

### `cu64`

```mojo
comptime cu64
```

**Value:** `ComplexDType.uint64`

Data type comptime for ComplexDType.uint64.

### `cu128`

```mojo
comptime cu128
```

**Value:** `ComplexDType.uint128`

Data type comptime for ComplexDType.uint128.

### `cu256`

```mojo
comptime cu256
```

**Value:** `ComplexDType.uint256`

Data type comptime for ComplexDType.uint256.

### `cuint`

```mojo
comptime cuint
```

**Value:** `ComplexDType.uint`

Data type comptime for ComplexDType.uint.

### `cbf16`

```mojo
comptime cbf16
```

**Value:** `ComplexDType.bfloat16`

Data type comptime for ComplexDType.bfloat16.

### `cf16`

```mojo
comptime cf16
```

**Value:** `ComplexDType.float16`

Data type comptime for ComplexDType.float16.

### `cf32`

```mojo
comptime cf32
```

**Value:** `ComplexDType.float32`

Data type comptime for ComplexDType.float32.

### `cf64`

```mojo
comptime cf64
```

**Value:** `ComplexDType.float64`

Data type comptime for ComplexDType.float64.

### `cboolean`

```mojo
comptime cboolean
```

**Value:** `ComplexDType.bool`

Data type comptime for ComplexDType.bool.

### `cinvalid`

```mojo
comptime cinvalid
```

**Value:** `ComplexDType.invalid`

Data type comptime for ComplexDType.invalid.

## Structs

### `ComplexDType`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct ComplexDType
```

**Memory convention:** `register_passable_trivial`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Equatable`, `Hashable`, `Identifiable`, `ImplicitlyCopyable`, `Movable`, `RegisterPassable`, `TrivialRegisterPassable`, `Writable`

Represents a complex data type specification and provides methods for working with it.

`ComplexDType` behaves like an enum rather than a typical object. You don't
instantiate it, but instead use its compile-time constants (comptimees) to
declare data types for complex SIMD vectors, tensors, and other data structures.

</div>

#### Fields

- **`dtype`** (`DType`): The underlying storage for the ComplexDType value.

#### Aliases

#### `invalid`

```mojo
comptime invalid
```

**Value:** `ComplexDType(mlir_value=invalid)`

#### `bool`

```mojo
comptime bool
```

**Value:** `ComplexDType(mlir_value=bool)`

#### `int`

```mojo
comptime int
```

**Value:** `ComplexDType(mlir_value=int)`

#### `uint`

```mojo
comptime uint
```

**Value:** `ComplexDType(mlir_value=uint)`

#### `uint8`

```mojo
comptime uint8
```

**Value:** `ComplexDType(mlir_value=uint8)`

#### `int8`

```mojo
comptime int8
```

**Value:** `ComplexDType(mlir_value=int8)`

#### `uint16`

```mojo
comptime uint16
```

**Value:** `ComplexDType(mlir_value=uint16)`

#### `int16`

```mojo
comptime int16
```

**Value:** `ComplexDType(mlir_value=int16)`

#### `uint32`

```mojo
comptime uint32
```

**Value:** `ComplexDType(mlir_value=uint32)`

#### `int32`

```mojo
comptime int32
```

**Value:** `ComplexDType(mlir_value=int32)`

#### `uint64`

```mojo
comptime uint64
```

**Value:** `ComplexDType(mlir_value=uint64)`

#### `int64`

```mojo
comptime int64
```

**Value:** `ComplexDType(mlir_value=int64)`

#### `uint128`

```mojo
comptime uint128
```

**Value:** `ComplexDType(mlir_value=uint128)`

#### `int128`

```mojo
comptime int128
```

**Value:** `ComplexDType(mlir_value=int128)`

#### `uint256`

```mojo
comptime uint256
```

**Value:** `ComplexDType(mlir_value=uint256)`

#### `int256`

```mojo
comptime int256
```

**Value:** `ComplexDType(mlir_value=int256)`

#### `float8_e3m4`

```mojo
comptime float8_e3m4
```

**Value:** `ComplexDType(mlir_value=float8_e3m4)`

#### `float8_e4m3fn`

```mojo
comptime float8_e4m3fn
```

**Value:** `ComplexDType(mlir_value=float8_e4m3fn)`

#### `float8_e4m3fnuz`

```mojo
comptime float8_e4m3fnuz
```

**Value:** `ComplexDType(mlir_value=float8_e4m3fnuz)`

#### `float8_e5m2`

```mojo
comptime float8_e5m2
```

**Value:** `ComplexDType(mlir_value=float8_e5m2)`

#### `float8_e5m2fnuz`

```mojo
comptime float8_e5m2fnuz
```

**Value:** `ComplexDType(mlir_value=float8_e5m2fnuz)`

#### `bfloat16`

```mojo
comptime bfloat16
```

**Value:** `ComplexDType(mlir_value=bfloat16)`

#### `float16`

```mojo
comptime float16
```

**Value:** `ComplexDType(mlir_value=float16)`

#### `float32`

```mojo
comptime float32
```

**Value:** `ComplexDType(mlir_value=float32)`

#### `float64`

```mojo
comptime float64
```

**Value:** `ComplexDType(mlir_value=float64)`

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

```mojo
def __init__(*, mlir_value: __mlir_type.`!kgen.dtype`) -> Self
```

<span class="badge badge-static">static</span>

Construct a ComplexDType from MLIR ComplexDType.

<div class="prose-label">Args</div>

- `mlir_value` (`__mlir_type.`!kgen.dtype``) `[imm]`: The MLIR ComplexDType.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__eq__`

```mojo
def __eq__(self, rhs: Self) -> Bool
```

Compares one ComplexDType to another for equality.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `rhs` (`Self`) `[imm]`: The ComplexDType to compare against.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__ne__`

```mojo
def __ne__(self, rhs: Self) -> Bool
```

Compares one ComplexDType to another for inequality.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `rhs` (`Self`) `[imm]`: The ComplexDType to compare against.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__is__`

```mojo
def __is__(self, rhs: Self) -> Bool
```

Compares one ComplexDType to another for equality.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `rhs` (`Self`) `[imm]`: The ComplexDType to compare against.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__isnot__`

```mojo
def __isnot__(self, rhs: Self) -> Bool
```

Compares one ComplexDType to another for equality.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `rhs` (`Self`) `[imm]`: The ComplexDType to compare against.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__str__`

```mojo
def __str__(self) -> String
```

Gets the name of the ComplexDType.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>

<div class="fn-card" markdown="1">

#### `write_to`

```mojo
def write_to[W: Writer](self, mut writer: W)
```

Formats this ComplexDType to the provided Writer.

<div class="prose-label">Parameters</div>

- `W` (`Writer`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`: The object to write to.


</div>

<div class="fn-card" markdown="1">

#### `__repr__`

```mojo
def __repr__(self) -> String
```

Gets the representation of the ComplexDType e.g. `"ComplexDType.float32"`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>

<div class="fn-card" markdown="1">

#### `write_repr_to`

```mojo
def write_repr_to[W: Writer](self, mut writer: W)
```

Write the string representation to a writer.

<div class="prose-label">Parameters</div>

- `W` (`Writer`): The writer type.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`: The writer to write to.


</div>

<div class="fn-card" markdown="1">

#### `get_value`

```mojo
def get_value(self) -> __mlir_type.`!kgen.dtype`
```

Gets the associated internal kgen.ComplexDType value.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `__mlir_type.`!kgen.dtype``


</div>

<div class="fn-card" markdown="1">

#### `__hash__`

```mojo
def __hash__[H: Hasher](self, mut hasher: H)
```

Updates hasher with this `ComplexDType` value.

<div class="prose-label">Parameters</div>

- `H` (`Hasher`): The hasher type.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `hasher` (`H`) `[mut]`: The hasher instance.


</div>

<div class="fn-card" markdown="1">

#### `is_unsigned`

```mojo
def is_unsigned(self) -> Bool
```

Returns True if the type parameter is unsigned and False otherwise.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `is_signed`

```mojo
def is_signed(self) -> Bool
```

Returns True if the type parameter is signed and False otherwise.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `is_integral`

```mojo
def is_integral(self) -> Bool
```

Returns True if the type parameter is an integer and False otherwise.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `is_floating_point`

```mojo
def is_floating_point(self) -> Bool
```

Returns True if the type parameter is a floating-point and False otherwise.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `is_float8`

```mojo
def is_float8(self) -> Bool
```

Returns True if the ComplexDType is a 8bit-precision floating point type, e.g. float8_e5m2, float8_e5m2fnuz, float8_e4m3fn and float8_e4m3fnuz.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `is_half_float`

```mojo
def is_half_float(self) -> Bool
```

Returns True if the ComplexDType is a half-precision floating point type, e.g. either fp16 or bf16.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `is_numeric`

```mojo
def is_numeric(self) -> Bool
```

Returns True if the type parameter is numeric (i.e. you can perform arithmetic operations on).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `size_of`

```mojo
def size_of(self) -> Int
```

Returns the size in bytes of the current DType.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `bitwidth`

```mojo
def bitwidth(self) -> Int
```

Returns the size in bits of the current ComplexDType.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `component_bitwidth`

```mojo
def component_bitwidth(self) -> Int
```

Returns the size in bits of the component type of the current ComplexDType.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `component_dtype`

```mojo
def component_dtype(self) -> DType
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `DType`


</div>
