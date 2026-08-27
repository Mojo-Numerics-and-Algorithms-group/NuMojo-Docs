# `numojo.core.memory`

Low-level memory and storage utilities used by NuMojo core containers.

Exports
-------
- `DataContainer`: Abstract data container interface.
- `HostStorage`: Host (CPU) memory storage.
- `DeviceStorage`: Device (GPU) memory storage.
- `AcceleratorDataContainer`: Accelerator-aware data container.
- `from_dlpack`: DLPack interoperability function.

## Contents

| Name | Kind | Description |
|------|------|-------------|
| [`data_container`](./data_container.md) | module | Reference-counted memory container for array data. |
| [`dlpack`](./dlpack.md) | module | Zero-copy tensor exchange via DLPack protocol. |
| [`__init__`](./__init__.md) | module | Low-level memory and storage utilities used by NuMojo core containers. |
| [`storage`](./storage.md) | module | Backend storage containers for accelerator-aware data management. |

