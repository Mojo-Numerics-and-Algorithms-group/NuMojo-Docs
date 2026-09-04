# `numojo`

Central public surface for NuMojo that exposes the primary containers, dtype helpers, common errors, and a curated set of NumPy-inspired routines.

Exports
-------
Core container types:
- `NDArray`
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
  (`numojo.core.ndarray`, `numojo.core.layout`, `numojo.routines.math`, etc.) rather than relying on
  extensive top-level re-exports.
- Public APIs in this module adhere to the Mojo docstring style guide to keep documentation precise
  and predictable for users.

FORMAT FOR DOCSTRING (See "Mojo docstring style guide" for more information)
1. Description *
2. Parameters *
3. Args *
4. Raises *
5. Constraints *
6. Returns *
7. Notes
9. References
10. Examples *
(Items marked with * are defined by the Mojo docstring style guide).

## Contents

| Name | Kind | Description |
|------|------|-------------|
| [`core`](./core/index.md) | package | Foundational data structures and utilities for NuMojo: arrays, memory layouts, dtype aliases, error handling, and complex number support. |
| [`__init__`](./__init__.md) | module | Central public surface for NuMojo that exposes the primary containers, dtype helpers, common errors, and a curated set of NumPy-inspired routines. |
| [`prelude`](./prelude.md) | module | Core types and common utilities for day-to-day NuMojo usage. |
| [`routines`](./routines/index.md) | package | NumPy-like functionality grouped by topic (math, linalg, statistics, creation, manipulation, etc.). |

