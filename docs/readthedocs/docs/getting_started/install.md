# Installation

NuMojo offers several installation methods to suit different development needs. Choose the method that best fits your workflow:

### Method 1: Git Installation with pixi-build-mojo (Recommended)

Install NuMojo directly from the GitHub repository to access both stable releases and cutting-edge features. This method is perfect for developers who want the latest functionality or need to work with the most recent stable version.

Add the following to your existing `pixi.toml`:

```toml
[workspace]
preview = ["pixi-build"]

[package]
name = "your_project_name"
version = "0.1.0"

[package.build]
backend = {name = "pixi-build-mojo", version = "0.*"}

[package.build.config.pkg]
name = "your_package_name"

[package.host-dependencies]
mojo = "==1.0.0"
max-core = "==26.5.0"

[package.build-dependencies]
mojo = "==1.0.0"
max-core = "==26.5.0"
numojo = { git = "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo", branch = "main"}

[package.run-dependencies]
mojo = "==1.0.0"
max-core = "==26.5.0"
numojo = { git = "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo", branch = "main"}

[dependencies]
mojo = ">=1.0.0, <1.1.0"
max-core = ">=26.5.0,<27"
numojo = { git = "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo", branch = "main"}
```

Then run:
```bash
pixi install
```

**Branch Selection:**
- **`main` branch**: Provides the latest stable release. Currently NuMojo v0.10.0, compatible with Mojo >=1.0.0, <1.1.0. For earlier NuMojo versions, use Method 2.
- **`pre-x.y` branches**: Active development branch for the next release. Note that this branch receives frequent updates and may have breaking changes in features and syntax.

The package will be automatically available in your Pixi environment, and VSCode LSP will provide intelligent code hints.

### Method 2: Stable Release via Pixi (prefix.dev)

For most users, we recommend installing a stable release through Pixi for guaranteed compatibility and reproducibility.

Add the following to your `pixi.toml` file:

```toml
[workspace]
channels = ["https://repo.prefix.dev/modular-community"]

[dependencies]
numojo = "=0.10.0"
```

Then run:
```bash
pixi install
```

**Version Compatibility:**

| NuMojo Version | Required Mojo Version |
| -------------- | --------------------- |
| v0.10.0        | ==1.0.0               |
| v0.9.0         | ==26.2                |
| v0.8.0         | ==25.7                |
| v0.7.0         | ==25.3                |
| v0.6.1         | ==25.2                |
| v0.6.0         | ==25.2                |

### Method 3: Build Standalone Package

This method creates a portable `numojo.mojopkg` file that you can use across multiple projects, perfect for offline development or hermetic builds.

1. Clone the repository:
   ```bash
   git clone https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo.git
   cd NuMojo
   ```

2. Build the package:
   ```bash
   pixi run package
   ```

3. Copy `numojo.mojopkg` to your project directory or add its parent directory to your include paths.

### Method 4: Direct Source Integration

For maximum flexibility and the ability to modify NuMojo source code during development:

1. Clone the repository to your desired location:
   ```bash
   git clone https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo.git
   ```

2. When compiling your code, include the NuMojo source path:
   ```bash
   mojo run -I "/path/to/NuMojo" your_program.mojo
   ```

3. **VSCode LSP Setup** (for code hints and autocompletion):
   - Open VSCode preferences
   - Navigate to `Mojo › Lsp: Include Dirs`
   - Click `Add Item` and enter the full path to your NuMojo directory (e.g., `/Users/YourName/Projects/NuMojo`)
   - Restart the Mojo LSP server

After setup, VSCode will provide intelligent code completion and hints for NuMojo functions!
