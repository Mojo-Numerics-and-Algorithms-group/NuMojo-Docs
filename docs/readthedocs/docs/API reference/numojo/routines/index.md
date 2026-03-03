# `numojo.routines`

Routines module (numojo.routines)

This modules groups NumPy-like functionality by topic (math, linalg, statistics,
creation, manipulation, etc.).

What this `__init__` exports:
- Topic namespaces (e.g. `numojo.routines.math`, `numojo.routines.linalg`, ...)
- A curated set of convenience functions at `numojo.routines.*` for ergonomic
  internal use and power users.

Notes / conventions:
- Public user-facing imports should generally come from the top-level `numojo`
  module (or `numojo.prelude`) rather than importing deeply from this package.
- Keep this initializer predictable: add new re-exports only when they are
  stable and widely used.

## Contents

| Name | Kind | Description |
|------|------|-------------|
| [`bitwise`](./bitwise.md) | module | Bit-wise operations module (`numojo.routines.bitwise`) |
| [`constants`](./constants.md) | module | Constants (numojo.routines.constants) |
| [`creation`](./creation.md) | module | Creation routines (numojo.routines.creation) |
| [`functional`](./functional.md) | module | Functional programming (numojo.routines.functional) |
| [`indexing`](./indexing.md) | module | Indexing routines (numojo.routines.indexing) |
| [`io`](./io/index.md) | package | I/O routines (numojo.routines.io) |
| [`linalg`](./linalg/index.md) | package | Linear algebra routines (numojo.routines.linalg) |
| [`logic`](./logic/index.md) | package | Logic routines for NuMojo (numojo.routines.logic). |
| [`manipulation`](./manipulation.md) | module | Manipulation routines (numojo.routines.manipulation) |
| [`math`](./math/index.md) | package | Math routines for NuMojo (numojo.routines.math). |
| [`random`](./random.md) | module | Random (numojo.routines.random) |
| [`__init__`](./__init__.md) | module | Routines module (numojo.routines) |
| [`searching`](./searching.md) | module | "Searching routines (numojo.routines.searching) |
| [`sorting`](./sorting.md) | module | Sorting routines (numojo.routines.sorting) |
| [`statistics`](./statistics/index.md) | package | Statistics routines for NuMojo (numojo.routines.statistics). |

