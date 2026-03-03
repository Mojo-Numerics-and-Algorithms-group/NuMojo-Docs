# Installation

NuMojo supports multiple installation paths depending on your workflow.

## Prerequisites

- A supported platform (`osx-arm64` or `linux-64`)
- `pixi` installed
- Compatible Mojo/Modular toolchain (managed through `pixi.toml`)

---

## Method 1 — Install from source (recommended for contributors)

Use this if you want to run tests, modify source, or contribute.

### 1) Clone the repository

```bash
git clone https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo.git
cd NuMojo
```

### 2) Create environment

```bash
pixi install
```

### 3) Run validation

```bash
pixi run final
```

This runs formatting + tests.

---

## Method 2 — Use NuMojo in your own Pixi project (git dependency)

Use this when you want NuMojo directly from GitHub in another project.

Add the following to your project `pixi.toml` (adjust names as needed):

```toml
[workspace]
preview = ["pixi-build"]

[package]
name = "your_project_name"
version = "0.1.0"

[package.build]
backend = { name = "pixi-build-mojo", version = "0.*" }

[package.build.config.pkg]
name = "your_package_name"

[package.host-dependencies]
modular = ">=25.7.0,<26"

[package.build-dependencies]
modular = ">=25.7.0,<26"
numojo = { git = "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo", branch = "main" }

[package.run-dependencies]
modular = ">=25.7.0,<26"
numojo = { git = "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo", branch = "main" }

[dependencies]
modular = ">=25.7.0,<26"
numojo = { git = "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo", branch = "main" }
```

Then install:

```bash
pixi install
```

### Branch choice

- `main`: stable branch
- `pre-x.y`: active development branch (can include breaking changes)

---

## Method 3 — Install stable package from prefix.dev

Use this for reproducible, pinned setups in projects that don't need source edits.

In your `pixi.toml`:

```toml
[workspace]
channels = ["https://repo.prefix.dev/modular-community"]

[dependencies]
numojo = "=0.8.0"
```

Then:

```bash
pixi install
```

### Compatibility table

| NuMojo Version | Required Mojo Version |
| --- | --- |
| v0.8.0 | ==25.7 |
| v0.7.0 | ==25.3 |
| v0.6.1 | ==25.2 |
| v0.6.0 | ==25.2 |

---

## Method 4 — Build standalone `numojo.mojopkg`

Use this for offline or hermetic workflows.

From the NuMojo repo root:

```bash
pixi run package
```

This generates `numojo.mojopkg`. Copy it to your target project directory (or add its parent path to include dirs).

---

## Method 5 — Direct source include (no package build)

Use this for fast local iteration while editing NuMojo source.

```bash
mojo run -I "/path/to/NuMojo" your_program.mojo
```

Example:

```bash
mojo run -I "/Users/yourname/Projects/NuMojo" app.mojo
```

---

## VSCode / LSP setup

To enable autocompletion and symbol resolution for NuMojo:

1. Open VSCode settings
2. Go to `Mojo › Lsp: Include Dirs`
3. Add the absolute path to your NuMojo folder
4. Restart Mojo LSP

---

## Verify installation

Create a quick file like `check_numojo.mojo`:

```mojo
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[f32](10)
    print(a)
    print(nm.sum(a))
```

Run:

```bash
mojo run -I "/path/to/NuMojo" check_numojo.mojo
```

If this runs successfully, your installation is working.

---

## Troubleshooting

### Dependency resolution issues
- Ensure your `modular` version is compatible with your selected NuMojo version.
- Recreate environment:
  ```bash
  pixi install --locked
  ```

### Package not found in editor
- Verify LSP include path points to the NuMojo root.
- Restart VSCode and Mojo LSP.

### Import works in terminal but not in editor
- Editor often uses separate language-server include paths; configure `Mojo › Lsp: Include Dirs` explicitly.
