# `numojo.core.dtype.complex_dtype`

ComplexDType (numojo.core.dtype.complex_dtype)

ComplexDType and related utilities for working with complex data types in NuMojo.

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

```mojo
struct ComplexDType
```

**Memory convention:** `register_passable_trivial`  
**Implements:** `AnyType`, `Copyable`, `Equatable`, `Hashable`, `Identifiable`, `ImplicitlyCopyable`, `ImplicitlyDestructible`, `Movable`, `RegisterPassable`, `Representable`, `Stringable`, `TrivialRegisterPassable`, `Writable`

Represents a complex data type specification and provides methods for working with it.

`ComplexDType` behaves like an enum rather than a typical object. You don't
instantiate it, but instead use its compile-time constants (comptimees) to
declare data types for complex SIMD vectors, tensors, and other data structures.

#### Fields

- **`dtype`** (`DType`): The underlying storage for the ComplexDType value.

#### Aliases

##### `invalid`

```mojo
comptime invalid
```

**Value:** `ComplexDType(invalid)`

##### `bool`

```mojo
comptime bool
```

**Value:** `ComplexDType(bool)`

##### `int`

```mojo
comptime int
```

**Value:** `ComplexDType(int)`

##### `uint`

```mojo
comptime uint
```

**Value:** `ComplexDType(uint)`

##### `uint8`

```mojo
comptime uint8
```

**Value:** `ComplexDType(uint8)`

##### `int8`

```mojo
comptime int8
```

**Value:** `ComplexDType(int8)`

##### `uint16`

```mojo
comptime uint16
```

**Value:** `ComplexDType(uint16)`

##### `int16`

```mojo
comptime int16
```

**Value:** `ComplexDType(int16)`

##### `uint32`

```mojo
comptime uint32
```

**Value:** `ComplexDType(uint32)`

##### `int32`

```mojo
comptime int32
```

**Value:** `ComplexDType(int32)`

##### `uint64`

```mojo
comptime uint64
```

**Value:** `ComplexDType(uint64)`

##### `int64`

```mojo
comptime int64
```

**Value:** `ComplexDType(int64)`

##### `uint128`

```mojo
comptime uint128
```

**Value:** `ComplexDType(uint128)`

##### `int128`

```mojo
comptime int128
```

**Value:** `ComplexDType(int128)`

##### `uint256`

```mojo
comptime uint256
```

**Value:** `ComplexDType(uint256)`

##### `int256`

```mojo
comptime int256
```

**Value:** `ComplexDType(int256)`

##### `float8_e3m4`

```mojo
comptime float8_e3m4
```

**Value:** `ComplexDType(float8_e3m4)`

##### `float8_e4m3fn`

```mojo
comptime float8_e4m3fn
```

**Value:** `ComplexDType(float8_e4m3fn)`

##### `float8_e4m3fnuz`

```mojo
comptime float8_e4m3fnuz
```

**Value:** `ComplexDType(float8_e4m3fnuz)`

##### `float8_e5m2`

```mojo
comptime float8_e5m2
```

**Value:** `ComplexDType(float8_e5m2)`

##### `float8_e5m2fnuz`

```mojo
comptime float8_e5m2fnuz
```

**Value:** `ComplexDType(float8_e5m2fnuz)`

##### `bfloat16`

```mojo
comptime bfloat16
```

**Value:** `ComplexDType(bfloat16)`

##### `float16`

```mojo
comptime float16
```

**Value:** `ComplexDType(float16)`

##### `float32`

```mojo
comptime float32
```

**Value:** `ComplexDType(float32)`

##### `float64`

```mojo
comptime float64
```

**Value:** `ComplexDType(float64)`

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `True`

##### `__move_ctor_is_trivial`

```mojo
comptime __move_ctor_is_trivial
```

**Value:** `True`

##### `__copy_ctor_is_trivial`

```mojo
comptime __copy_ctor_is_trivial
```

**Value:** `True`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
__init__(*, mlir_value: __mlir_type.`!kgen.dtype`) -> Self
```

<span class="badge badge-static">static</span>

Construct a ComplexDType from MLIR ComplexDType.

**Args:**

- `mlir_value` (`__mlir_type.`!kgen.dtype``): The MLIR ComplexDType.

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
__eq__(self, rhs: Self) -> Bool
```

Compares one ComplexDType to another for equality.

**Args:**

- `self` (`Self`)
- `rhs` (`Self`): The ComplexDType to compare against.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
__ne__(self, rhs: Self) -> Bool
```

Compares one ComplexDType to another for inequality.

**Args:**

- `self` (`Self`)
- `rhs` (`Self`): The ComplexDType to compare against.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__is__`

```mojo
__is__(self, rhs: Self) -> Bool
```

Compares one ComplexDType to another for equality.

**Args:**

- `self` (`Self`)
- `rhs` (`Self`): The ComplexDType to compare against.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__isnot__`

```mojo
__isnot__(self, rhs: Self) -> Bool
```

Compares one ComplexDType to another for equality.

**Args:**

- `self` (`Self`)
- `rhs` (`Self`): The ComplexDType to compare against.

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
__str__(self) -> String
```

Gets the name of the ComplexDType.

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `write_to`

```mojo
write_to[W: Writer](self, mut writer: W)
```

Formats this ComplexDType to the provided Writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`: The object to write to.


</div>

<div class="fn-card" markdown="1">

##### `__repr__`

```mojo
__repr__(self) -> String
```

Gets the representation of the ComplexDType e.g. `"ComplexDType.float32"`.

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `get_value`

```mojo
get_value(self) -> __mlir_type.`!kgen.dtype`
```

Gets the associated internal kgen.ComplexDType value.

**Args:**

- `self` (`Self`)

**Returns:**

- `__mlir_type.`!kgen.dtype``


</div>

<div class="fn-card" markdown="1">

##### `__hash__`

```mojo
__hash__[H: Hasher](self, mut hasher: H)
```

Updates hasher with this `ComplexDType` value.

**Parameters:**

- `H` (`Hasher`): The hasher type.

**Args:**

- `self` (`Self`)
- `hasher` (`H`) `[mut]`: The hasher instance.


</div>

<div class="fn-card" markdown="1">

##### `is_unsigned`

```mojo
is_unsigned(self) -> Bool
```

Returns True if the type parameter is unsigned and False otherwise.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_signed`

```mojo
is_signed(self) -> Bool
```

Returns True if the type parameter is signed and False otherwise.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_integral`

```mojo
is_integral(self) -> Bool
```

Returns True if the type parameter is an integer and False otherwise.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_floating_point`

```mojo
is_floating_point(self) -> Bool
```

Returns True if the type parameter is a floating-point and False otherwise.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_float8`

```mojo
is_float8(self) -> Bool
```

Returns True if the ComplexDType is a 8bit-precision floating point type, e.g. float8_e5m2, float8_e5m2fnuz, float8_e4m3fn and float8_e4m3fnuz.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_half_float`

```mojo
is_half_float(self) -> Bool
```

Returns True if the ComplexDType is a half-precision floating point type, e.g. either fp16 or bf16.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_numeric`

```mojo
is_numeric(self) -> Bool
```

Returns True if the type parameter is numeric (i.e. you can perform arithmetic operations on).

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `size_of`

```mojo
size_of(self) -> Int
```

Returns the size in bytes of the current DType.

**Args:**

- `self` (`Self`)

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `bitwidth`

```mojo
bitwidth(self) -> Int
```

Returns the size in bits of the current ComplexDType.

**Args:**

- `self` (`Self`)

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `component_bitwidth`

```mojo
component_bitwidth(self) -> Int
```

Returns the size in bits of the component type of the current ComplexDType.

**Args:**

- `self` (`Self`)

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `__mlir_type`

```mojo
__mlir_type(self) -> __mlir_type.`!kgen.deferred`
```

Returns the MLIR type of the current DType as an MLIR type.

**Args:**

- `self` (`Self`)

**Returns:**

- `__mlir_type.`!kgen.deferred``


</div>

<div class="fn-card" markdown="1">

##### `component_dtype`

```mojo
component_dtype(self) -> DType
```

**Args:**

- `self` (`Self`)

**Returns:**

- `DType`


</div>
