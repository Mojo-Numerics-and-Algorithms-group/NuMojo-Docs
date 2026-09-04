---
hide:
  - navigation
  - toc
---

<div style="text-align:center; margin-top: 1em;">
<img src="https://raw.githubusercontent.com/Mojo-Numerics-and-Algorithms-group/NuMojo/main/assets/numojo_logo_360x360.png" alt="NuMojo logo" width="120">
</div>

# NuMojo documentation

NuMojo is a library for numerical computing in Mojo, similar to NumPy in Python.

[GitHub](https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo) |
[Discord](https://discord.gg/NcnSH5n26F) |
[Changelog](user-guide/changelog.md) |
[Installing NuMojo](getting_started/install.md)

<div class="grid cards" markdown>

-   :material-rocket-launch-outline: __Getting started__

    ---

    New to NuMojo? Install it and run your first program in a few minutes.

    [:octicons-arrow-right-24: Quickstart](getting_started/quickstart.md)

-   :material-book-open-variant: __User guide__

    ---

    Browse available functions and routines by topic, with links into the
    full API reference.

    [:octicons-arrow-right-24: User guide](user-guide/overview.md)

-   :material-api: __API reference__

    ---

    The complete reference for every module, struct, and function in
    NuMojo, generated from the source.

    [:octicons-arrow-right-24: API reference](API reference/numojo/index.md)

-   :material-source-branch: __Contributor's guide__

    ---

    Want to add a feature or fix a bug? Here's how the project is
    organized and what to run before opening a PR.

    [:octicons-arrow-right-24: Contributing](developer-guide/contributing.md)

</div>

## What is NuMojo?

NuMojo aims to encompass the extensive numerics capabilities found in NumPy. It seeks to harness
the full potential of Mojo, including vectorization, parallelization, and GPU acceleration, and
currently extends most (if not all) standard library math functions to support array inputs.

Its `NDArray` is a Mojo-native, SIMD-backed array type rather than a binding around NumPy or MAX's
tensor types, so it compiles directly into a Mojo program with no Python interop overhead. The API
follows NumPy conventions where they make sense — slicing, broadcasting, `@` for matrix
multiplication — so existing intuition carries over.

NuMojo is meant to serve as a building block for other Mojo libraries and programs that need fast
math operations, without the additional weight of a machine learning back-propagation system.

## Installing NuMojo

For a pinned stable release:

```toml
[workspace]
channels = ["https://repo.prefix.dev/modular-community"]

[dependencies]
numojo = "=0.10.0"
```

```bash
pixi install
```

See [Installation](getting_started/install.md) for all methods, including tracking the latest
development branch.
