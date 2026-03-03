---
hide:
  - navigation
  - toc
---

# NuMojo

<p style="font-size:1.2em">
A library for numerical computing in <strong>Mojo 🔥</strong> — fast, vectorized, and GPU-ready.
Inspired by NumPy and SciPy.
</p>

<div style="margin: 1.5em 0; display:flex; gap:0.7em; flex-wrap:wrap;">
<a href="getting_started/quickstart/" class="md-button md-button--primary">Quickstart →</a>
<a href="getting_started/install/" class="md-button">Installation</a>
<a href="API reference/numojo/" class="md-button">API Reference</a>
<a href="https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo" class="md-button">GitHub</a>
<a href="https://discord.gg/NcnSH5n26F" class="md-button">Discord</a>
</div>

---

## What is NuMojo?

NuMojo provides fast, vectorized numerical routines for Mojo — the same role NumPy and SciPy play in
the Python ecosystem, but built from the ground up to exploit Mojo's native SIMD, parallelism, and
(future) GPU acceleration.

**NuMojo is not** a machine learning library and will never include back-propagation.

---

## Core types

| Type | Description |
|------|-------------|
| `NDArray` | General-purpose N-dimensional array for tensors, grids, batches |
| `Matrix` | Dedicated 2-D array optimized for linear-algebra workflows |
| `ComplexNDArray` | N-dimensional array of complex numbers |

---

## Highlights

=== "NDArray"

    ```mojo
    import numojo as nm
    from numojo.prelude import *

    fn main() raises:
        var A = nm.random.randn(Shape(1000, 1000))
        var B = nm.random.randn(Shape(1000, 1000))
        var C = A @ B
        var I = nm.inv(A)
        var s = A[1:3, 4:19]
        print(nm.sum(A))
    ```

=== "Matrix"

    ```mojo
    from numojo import Matrix
    import numojo as nm

    fn main() raises:
        var A = Matrix.rand(shape=(1000, 1000))
        var B = Matrix.rand(shape=(1000, 1))
        var x = nm.solve(A, B)
        print(x)
    ```

=== "ComplexNDArray"

    ```mojo
    import numojo as nm
    from numojo.prelude import *

    fn main() raises:
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
- **Linear algebra** — `matmul`, `inv`, `solve`, `lstsq`, `det`, `norm`, decompositions, …
- **Logic** — `all`, `any`, comparison, logical ops, …
- **Statistics** — `mean`, `std`, `var`, `sum`, `prod`, `min`, `max`, …
- **Sorting & searching** — `sort`, `argsort`, `argmin`, `argmax`, …
- **I/O** — file read/write, formatting, …
- **Science** — interpolation, signal processing, …

---

## Installation

The fastest way to get started:

```toml
[workspace]
channels = ["https://repo.prefix.dev/modular-community"]

[dependencies]
numojo = "=0.8.0"
```

```bash
pixi install
```

See the [full installation guide](getting_started/install.md) for all methods.

---

## Version compatibility

| NuMojo | Mojo |
|--------|------|
| v0.8.0 | ==25.7 |
| v0.7.0 | ==25.3 |
| v0.6.1 | ==25.2 |

---

## License

Apache 2.0 with LLVM Exceptions.
See [LICENSE](https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo/blob/main/LICENSE).

## Contributors

[![Contributors](https://contrib.rocks/image?repo=Mojo-Numerics-and-Algorithms-group/NuMojo)](https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo/graphs/contributors)
