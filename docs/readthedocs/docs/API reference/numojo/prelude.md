# `numojo.prelude`

Core types and common utilities for day-to-day NuMojo usage.

Exports
-------
- Container types: `NDArray`.
- Shape/index helpers: `Shape`, `NDArrayShape`, `Item`.
- Dtype aliases: `f32`, `f64`, `i32`, `boolean`.
- Complex helpers: `ComplexSIMD`, `ComplexScalar`, `CScalar`, `1j`.

Usage:
```mojo
from numojo.prelude import *
```

For more functions (math, linalg, statistics), import from `numojo.routines.*`.

