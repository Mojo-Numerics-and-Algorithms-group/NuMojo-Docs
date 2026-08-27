# `numojo.core.type_aliases`

Type aliases and symbolic constants for commonly used data types in NuMojo.

This module provides convenient, user-friendly aliases for core types such as shapes,
strides, and complex scalars, as well as a symbolic constant for the imaginary unit.

Exports
-------
- `Shape`: Alias for NDArrayShape.
- `Strides`: Alias for NDArrayStrides.
- `ComplexScalar`, `CScalar`: Aliases for scalar complex numbers.
- `1j`: Imaginary unit constant (0 + 1j).

## Aliases

### `Shape`

```mojo
comptime Shape
```

**Value:** `NDArrayShape`

Alias for NDArrayShape, representing the shape of an n-dimensional array.

### `Strides`

```mojo
comptime Strides
```

**Value:** `NDArrayStrides`

Alias for NDArrayStrides, representing the memory strides of an n-dimensional array.

### `ComplexScalar`

```mojo
comptime ComplexScalar
```

**Value:** `ComplexSIMD[_]`

Alias for a scalar (width=1) complex SIMD value.

### `CScalar`

```mojo
comptime CScalar
```

**Value:** `ComplexSIMD[_]`

Alias for a scalar complex number, equivalent to ComplexScalar.

### `1j`

```mojo
comptime 1j
```

**Value:** `ImaginaryUnit()`

Constant representing the imaginary unit (0 + 1j).

Allows Python-like syntax for complex numbers, e.g., (3 + 4 * `1j`).

