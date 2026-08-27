# `numojo.routines.__init__`

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

