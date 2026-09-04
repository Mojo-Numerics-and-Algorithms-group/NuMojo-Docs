# `numojo.core.__init__`

Foundational data structures and utilities for NuMojo: arrays, memory layouts, dtype aliases, error handling, and complex number support.

Exports
-------
- `NDArray`, `AcceleratorNDArray`: Core array containers.
- `ComplexNDArray`, `ComplexSIMD`: Complex number support.
- `NDArrayShape`, `NDArrayStrides`, `Flags`, `newaxis`: Layout metadata.
- `IndexMethods`, `Item`, `TraverseMethods`, `Validator`: Indexing helpers.
- `DataContainer`, `HostStorage`, `DeviceStorage`, `AcceleratorDataContainer`:
  Memory storage types.
- `NumojoError`, `terminate`: Error handling.
- Dtype aliases (`i8`, `f32`, `boolean`, ...) and complex counterparts.

