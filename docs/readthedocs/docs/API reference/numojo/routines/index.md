# `numojo.routines`

NumPy-like functionality grouped by topic (math, linalg, statistics, creation, manipulation, etc.).

Exports
-------
- Topic namespaces (e.g. `numojo.routines.math`, `numojo.routines.linalg`, ...).
- A curated set of convenience functions at `numojo.routines.*` for ergonomic
  internal use and power users.

Notes
-----
- Public user-facing imports should generally come from the top-level `numojo`
  module (or `numojo.prelude`) rather than importing deeply from this package.
- Keep this initializer predictable: add new re-exports only when they are
  stable and widely used.

## Contents

| Name | Kind | Description |
|------|------|-------------|
| [`bitwise`](./bitwise.md) | module | Bitwise operations for integer arrays. |
| [`constants`](./constants.md) | module | Mathematical and physical constants. |
| [`creation`](./creation.md) | module | Functions for creating and initializing NDArray and ComplexNDArray objects. |
| [`functional`](./functional.md) | module | Functional programming utilities for array operations. |
| [`indexing`](./indexing.md) | module | Advanced indexing operations for arrays. |
| [`io`](./io/index.md) | package | File I/O operations and array formatting for NuMojo. |
| [`linalg`](./linalg/index.md) | package | Linear algebra operations including matrix decompositions, norms, products, and linear system solving. |
| [`logic`](./logic/index.md) | package | Comparison operations, logical operators, and truth value evaluations for arrays. |
| [`manipulation`](./manipulation.md) | module | Array shape and layout manipulation operations. |
| [`math`](./math/index.md) | package | Arithmetic, trigonometric, hyperbolic, exponential, and utility mathematical operations for arrays. |
| [`operations`](./operations/index.md) | package | Vectorized operation execution backends for unary, binary, and predicate operations. |
| [`random`](./random.md) | module | Random number generation and sampling. |
| [`__init__`](./__init__.md) | module | NumPy-like functionality grouped by topic (math, linalg, statistics, creation, manipulation, etc.). |
| [`searching`](./searching.md) | module | Search operations for finding array extrema indices. |
| [`sorting`](./sorting.md) | module | Array sorting and indexing operations. |
| [`statistics`](./statistics/index.md) | package | Statistical functions including averages, dispersion measures, and order statistics. |

