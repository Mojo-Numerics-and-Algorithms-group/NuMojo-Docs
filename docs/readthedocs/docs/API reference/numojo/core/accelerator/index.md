# `numojo.core.accelerator`

Accelerator (GPU) support namespace for NuMojo.

Exports
-------
- `Device`: Abstract device interface.
- `DeviceHandle`: Handle for device instances.
- `DeviceSpec`: Device specification and capabilities.
- `cpu`: CPU device instance.
- `cuda`: CUDA device instance.
- `mps`: Metal Performance Shaders device instance.
- `rocm`: ROCm device instance.

## Contents

| Name | Kind | Description |
|------|------|-------------|
| [`__init__`](./__init__.md) | module | Accelerator (GPU) support namespace for NuMojo. |
| [`device`](./device.md) | module | Execution device for array and matrix operations. |
| [`kernels`](./kernels/index.md) | package | GPU kernel functions for `AcceleratorNDArray` operation dispatch. |

