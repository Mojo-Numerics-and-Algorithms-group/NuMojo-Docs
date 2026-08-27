# `numojo.core`

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

## Contents

| Name | Kind | Description |
|------|------|-------------|
| [`accelerator`](./accelerator/index.md) | package | Accelerator (GPU) support namespace for NuMojo. |
| [`accelerator_ndarray`](./accelerator_ndarray.md) | module | Device-aware NDArray with accelerator support. |
| [`complex`](./complex/index.md) | package | Complex number support for NuMojo, including SIMD complex types and complex NDArrays. |
| [`__init__`](./__init__.md) | module | Foundational data structures and utilities for NuMojo: arrays, memory layouts, dtype aliases, error handling, and complex number support. |
| [`dtype`](./dtype/index.md) | package | Dtype aliases and dtype-related utilities used across NuMojo. |
| [`error`](./error.md) | module | Unified error system for NuMojo operations. |
| [`indexing`](./indexing/index.md) | package | Indexing-related helpers and types used by NuMojo core containers. |
| [`layout`](./layout/index.md) | package | Layout metadata types used by NuMojo arrays and matrices (shape, strides, and flags). |
| [`memory`](./memory/index.md) | package | Low-level memory and storage utilities used by NuMojo core containers. |
| [`ndarray`](./ndarray.md) | module | Multi-dimensional array implementation for NuMojo. |
| [`traits`](./traits/index.md) | package | Trait and protocol abstractions used across NuMojo core containers and internals. |
| [`type_aliases`](./type_aliases.md) | module | Type aliases and symbolic constants for commonly used data types in NuMojo. |

