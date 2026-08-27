---
hide:
  - navigation
  - toc
---

<div style="text-align:center; margin-top: 1em;">
<img src="https://raw.githubusercontent.com/Mojo-Numerics-and-Algorithms-group/NuMojo/main/assets/numojo_logo_360x360.png" alt="NuMojo logo" width="160">

<h1 style="border:none; margin:0.4em 0 0;">NuMojo</h1>

<p style="font-size:1.2em">
A library for numerical computing in <strong>Mojo 🔥</strong>, similar to NumPy in Python.
</p>
</div>

<div style="margin: 1.5em 0; display:flex; gap:0.7em; flex-wrap:wrap; justify-content:center;">
<a href="getting_started/quickstart/" class="md-button md-button--primary">Quickstart →</a>
<a href="getting_started/install/" class="md-button">Installation</a>
<a href="API reference/numojo/" class="md-button">API Reference</a>
<a href="https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo" class="md-button">GitHub</a>
<a href="https://discord.gg/NcnSH5n26F" class="md-button">Discord</a>
</div>

---

## What is NuMojo?

NuMojo aims to encompass the extensive numerics capabilities found in NumPy. We seek to harness the
full potential of Mojo, including vectorization, parallelization, and GPU acceleration — currently,
NuMojo extends most (if not all) standard library math functions to support array inputs.

Our vision for NuMojo is to serve as a familiar and essential building block for other Mojo libraries
needing fast math operations, without the additional weight of a machine learning back-propagation
system.

---

## Why NuMojo

- **Native to Mojo.** NuMojo's `NDArray` is a Mojo-native SIMD-backed type, not a binding around
  NumPy or MAX's tensor types, so it compiles into your program with no Python interop overhead.
- **NumPy-familiar API.** Slicing, broadcasting, `@` for matrix multiplication, and function names
  mirror NumPy where it makes sense, so existing intuition carries over.
- **Built for Mojo's strengths.** Vectorization and parallelism are used throughout the routines,
  with GPU and other accelerator support (`AcceleratorNDArray`) landing as Mojo's own device support
  matures.

---

## Core types

| Type | Description |
|------|-------------|
| `NDArray` | General-purpose N-dimensional array for tensors, grids, batches |
| `ComplexNDArray` | N-dimensional array of complex numbers |

---

## Highlights

=== "NDArray"

    ```mojo
    import numojo as nm
    from numojo.prelude import *

    def main() raises:
        var A = nm.random.randn(Shape(1000, 1000))
        var B = nm.random.randn(Shape(1000, 1000))
        var C = A @ B
        var I = nm.inv(A)
        var s = A[1:3, 4:19]
        print(nm.sum(A))
        print(nm.solve(A, B))
    ```

=== "ComplexNDArray"

    ```mojo
    import numojo as nm
    from numojo.prelude import *

    def main() raises:
        var z = CScalar[cf32](5)
        var A = nm.full[cf32](Shape(4, 4), fill_value=z)
        var B = nm.ones[cf32](Shape(4, 4))
        print(A * B)
    ```

---

## Routines at a glance

- **Creation** — `zeros`, `ones`, `arange`, `linspace`, `fromstring`, `random`, …
- **Manipulation** — `reshape`, `transpose`, `flip`, `broadcast_to`, …
- **Math** — `sin`, `cos`, `exp`, `log`, `sqrt`, arithmetic, rounding, …
- **Linear algebra** — `matmul`, `inv`, `solve`, `det`, `trace`, `lu_decomposition`, …
- **Logic** — `all`, `any`, comparison, logical ops, …
- **Statistics** — `mean`, `std`, `var`, `sum`, `prod`, `min`, `max`, …
- **Sorting & searching** — `sort`, `argsort`, `argmin`, `argmax`, …
- **I/O** — file read/write, formatting, …

See the [User Guide](user-guide/overview.md) for the full list linked to the [API Reference](API reference/numojo/index.md).

---

## Installation

The fastest way to get started, for a pinned stable release:

```toml
[workspace]
channels = ["https://repo.prefix.dev/modular-community"]

[dependencies]
numojo = "=0.10.0"
```

```bash
pixi install
```

See the [full installation guide](getting_started/install.md) for all methods,
including tracking the latest development branch.

---

## Version compatibility

| NuMojo | Mojo |
|--------|------|
| v0.10.0 | ==1.0.0 |
| v0.9.0 | ==26.2 |
| v0.8.0 | ==25.7 |
| v0.7.0 | ==25.3 |
| v0.6.1 | ==25.2 |

---

## Learn more

- [Roadmap](user-guide/roadmap.md) — planned work and long-term direction.
- [Changelog](user-guide/changelog.md) — released changes by version.
- [Contributing](developer-guide/contributing.md) — how to get involved.

---

## License

Apache 2.0 with LLVM Exceptions.
See [LICENSE](https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo/blob/main/LICENSE).

## Contributors

[![Contributors](https://contrib.rocks/image?repo=Mojo-Numerics-and-Algorithms-group/NuMojo)](https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo/graphs/contributors)
