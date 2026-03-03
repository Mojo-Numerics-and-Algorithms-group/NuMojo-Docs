# `numojo`

NuMojo Top-Level Package (`numojo`) ==================================

Central public surface for NuMojo that exposes the primary containers, dtype helpers, common errors,
and a curated set of NumPy-inspired routines.

Exports
-------
Core container types:
- `Matrix` and `NDArray`
- `Shape` / `NDArrayShape`, `Strides` / `NDArrayStrides`

Core utilities:
- dtype aliases (`f32`, `f64`, `i32`, `i64`, ...) along with their complex counterparts and SIMD helpers
- shared error types such as `NumojoError`, `IndexError`, and `ShapeError`

Routines
--------
Re-exports a carefully selected subset of functionality from `numojo.routines` covering creation,
manipulation, math, logic, statistics, I/O, and related domains so users have a stable convenience import.

Notes
-----
- This module is intended to provide a stable import surface for users.
- Internal code should prefer importing directly from the canonical submodules/packages
  (`numojo.core.matrix`, `numojo.core.layout`, `numojo.routines.math`, etc.) rather than relying on
  extensive top-level re-exports.
- Public APIs in this module adhere to the Mojo docstring style guide to keep documentation precise
  and predictable for users.

FORMAT FOR DOCSTRING (See "Mojo docstring style guide" for more information)
1. Description *
2. Parameters *
3. Args *
4. Constraints *
5. Returns *
6. Raises *
7. SEE ALSO
8. NOTES
9. REFERENCES
10. Examples *
(Items marked with * are defined by the Mojo docstring style guide.)

## Contents

| Name | Kind | Description |
|------|------|-------------|
| [`core`](./core/index.md) | package | Core (numojo.core) |
| [`__init__`](./__init__.md) | module | NuMojo Top-Level Package (`numojo`) ================================== |
| [`prelude`](./prelude.md) | module | NuMojo Prelude (`numojo.prelude`) ================================ |
| [`routines`](./routines/index.md) | package | Routines module (numojo.routines) |
| [`science`](./science/index.md) | package | NuMojo Science Package (numojo.science) |

