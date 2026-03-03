# `numojo.prelude`

NuMojo Prelude (`numojo.prelude`) ================================

The prelude is the recommended “batteries-included” import for day-to-day use.

Why it exists:
- Importing everything from `numojo` is convenient but pollutes your namespace.
- Importing every symbol manually makes headers long and repetitive.

What it exports:
- Core container types like `Matrix` and `NDArray`
- Shape/index helpers like `Shape`, `NDArrayShape`, and `Item`
- Common dtype aliases (e.g. `f32`, `f64`, `i32`, `boolean`)
- Complex number helpers (`ComplexSIMD`, `ComplexScalar`, `CScalar`, `1j`)

Usage:
```mojo
from numojo.prelude import *
```

For more functions (math, linalg, statistics, etc.), import them from
`numojo.routines.*` (or directly from `numojo`) as needed.

