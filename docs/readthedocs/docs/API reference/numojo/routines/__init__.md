# `numojo.routines.__init__`

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

