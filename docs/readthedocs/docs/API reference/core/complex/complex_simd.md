



# complex_simd

##  Module Summary
  

## Aliases
  
`ComplexScalar`: 
## ComplexSIMD

### ComplexSIMD Summary
  
  
Represents a SIMD[dtype, 1] Complex number with real and imaginary parts.  

### Parent Traits
  

- AnyType
- Stringable
- UnknownDestructibility
- Writable

### Fields
  
  
* re `SIMD[dtype, size]`  
* im `SIMD[dtype, size]`  

### Functions

#### __init__


```rust
__init__(out self, other: Self)
```  
Summary  
  
Initializes a ComplexSIMD instance by copying another instance.  
  
Args:  

- self
- other


```rust
__init__(out self, re: SIMD[dtype, size], im: SIMD[dtype, size])
```  
Summary  
  
Initializes a ComplexSIMD instance with specified real and imaginary parts.  
  
Args:  

- self
- re
- im


```rust
__init__(out self, val: SIMD[dtype, size])
```  
Summary  
  
Initializes a ComplexSIMD instance with specified real and imaginary parts.  
  
Args:  

- self
- val

#### __getitem__


```rust
__getitem__(self, idx: Int) -> SIMD[dtype, size]
```  
Summary  
  
Gets the real or imaginary part of the ComplexSIMD instance.  
  
Args:  

- self
- idx

#### __setitem__


```rust
__setitem__(mut self, idx: Int, value: Self)
```  
Summary  
  
Sets the real and imaginary parts of the ComplexSIMD instance.  
  
Args:  

- self
- idx
- value


```rust
__setitem__(mut self, idx: Int, re: SIMD[dtype, size], im: SIMD[dtype, size])
```  
Summary  
  
Sets the real and imaginary parts of the ComplexSIMD instance.  
  
Args:  

- self
- idx
- re
- im

#### __neg__


```rust
__neg__(self) -> Self
```  
Summary  
  
Negates the ComplexSIMD instance.  
  
Args:  

- self

#### __pos__


```rust
__pos__(self) -> Self
```  
Summary  
  
Returns the ComplexSIMD instance itself.  
  
Args:  

- self

#### __eq__


```rust
__eq__(self, other: Self) -> Bool
```  
Summary  
  
Checks if two ComplexSIMD instances are equal.  
  
Args:  

- self
- other

#### __ne__


```rust
__ne__(self, other: Self) -> Bool
```  
Summary  
  
Checks if two ComplexSIMD instances are not equal.  
  
Args:  

- self
- other

#### __add__


```rust
__add__(self, other: Self) -> Self
```  
Summary  
  
Adds two ComplexSIMD instances.  
  
Args:  

- self
- other

#### __sub__


```rust
__sub__(self, other: Self) -> Self
```  
Summary  
  
Subtracts another ComplexSIMD instance from this one.  
  
Args:  

- self
- other

#### __mul__


```rust
__mul__(self, other: Self) -> Self
```  
Summary  
  
Multiplies two ComplexSIMD instances.  
  
Args:  

- self
- other

#### __truediv__


```rust
__truediv__(self, other: Self) -> Self
```  
Summary  
  
Divides this ComplexSIMD instance by another.  
  
Args:  

- self
- other

#### __pow__


```rust
__pow__(self, other: Self) -> Self
```  
Summary  
  
Raises this ComplexSIMD instance to the power of another.  
  
Args:  

- self
- other


```rust
__pow__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Raises this ComplexSIMD instance to the power of a scalar.  
  
Args:  

- self
- other

#### __iadd__


```rust
__iadd__(mut self, other: Self)
```  
Summary  
  
Performs in-place addition of another ComplexSIMD instance.  
  
Args:  

- self
- other

#### __isub__


```rust
__isub__(mut self, other: Self)
```  
Summary  
  
Performs in-place subtraction of another ComplexSIMD instance.  
  
Args:  

- self
- other

#### __imul__


```rust
__imul__(mut self, other: Self)
```  
Summary  
  
Performs in-place multiplication with another ComplexSIMD instance.  
  
Args:  

- self
- other

#### __itruediv__


```rust
__itruediv__(mut self, other: Self)
```  
Summary  
  
Performs in-place division by another ComplexSIMD instance.  
  
Args:  

- self
- other

#### __str__


```rust
__str__(self) -> String
```  
Summary  
  
Returns a string representation of the ComplexSIMD instance.  
  
Args:  

- self

#### write_to


```rust
write_to[W: Writer](self, mut writer: W)
```  
Summary  
  
Writes the ComplexSIMD instance to a writer.  
  
Parameters:  

- W
  
Args:  

- self
- writer

#### __repr__


```rust
__repr__(self) -> String
```  
Summary  
  
Returns a string representation of the ComplexSIMD instance.  
  
Args:  

- self

#### __abs__


```rust
__abs__(self) -> SIMD[dtype, size]
```  
Summary  
  
Returns the magnitude of the ComplexSIMD instance.  
  
Args:  

- self

#### norm


```rust
norm(self) -> SIMD[dtype, size]
```  
Summary  
  
Returns the squared magnitude of the ComplexSIMD instance.  
  
Args:  

- self

#### conj


```rust
conj(self) -> Self
```  
Summary  
  
Returns the complex conjugate of the ComplexSIMD instance.  
  
Args:  

- self

#### real


```rust
real(self) -> SIMD[dtype, size]
```  
Summary  
  
Returns the real part of the ComplexSIMD instance.  
  
Args:  

- self

#### imag


```rust
imag(self) -> SIMD[dtype, size]
```  
Summary  
  
Returns the imaginary part of the ComplexSIMD instance.  
  
Args:  

- self
