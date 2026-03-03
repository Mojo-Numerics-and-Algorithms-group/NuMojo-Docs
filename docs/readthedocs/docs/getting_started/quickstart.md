# Quickstart

This guide helps you run NuMojo in minutes.

## Prerequisites

- Mojo toolchain installed
- `pixi` installed
- A working terminal

## Install NuMojo (recommended via Pixi)

Add this to your `pixi.toml`:

```/dev/null/pixi.toml#L1-24
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
modular = ">=25.7.0,<26"

[package.build-dependencies]
modular = ">=25.7.0,<26"
numojo = { git = "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo", branch = "main"}

[package.run-dependencies]
modular = ">=25.7.0,<26"
numojo = { git = "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo", branch = "main"}

[dependencies]
modular = ">=25.7.0,<26"
numojo = { git = "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo", branch = "main"}
```

Then install dependencies:

```/dev/null/terminal.sh#L1-1
pixi install
```

## Your first NuMojo program

Create `main.mojo`:

```/dev/null/main.mojo#L1-28
import numojo as nm
from numojo.prelude import *


fn main() raises:
    # Create arrays
    var a = nm.arange[f32](12).reshape(Shape(3, 4))
    var b = nm.ones[f32](Shape(3, 4))

    # Element-wise math
    var c = nm.add(a, b)

    # Reductions
    var total = nm.sum(c)
    var col_sum = nm.sum(c, axis=0)

    # Indexing and slicing
    var first_row = c[0, :]
    var block = c[0:2, 1:3]
    var item = c[Item(1, 2)]

    print("a:")
    print(a)
    print("c = a + 1:")
    print(c)
    print("sum(c):", total)
    print("sum(c, axis=0):")
    print(col_sum)
    print("first_row:", first_row)
    print("block:")
    print(block)
    print("item at (1, 2):", item)
```

Run it:

```/dev/null/terminal.sh#L1-1
pixi run mojo run main.mojo
```

## Matrix example

```/dev/null/matrix_example.mojo#L1-17
from numojo import Matrix
import numojo as nm


fn main() raises:
    var A = Matrix.rand(shape=(4, 4))
    var B = Matrix.rand(shape=(4, 4))

    var C = A @ B
    var s = nm.sum(C)
    var m = nm.max(C)

    print("A:")
    print(A)
    print("B:")
    print(B)
    print("C = A @ B:")
    print(C)
    print("sum(C):", s, "max(C):", m)
```

## Complex numbers example

```/dev/null/complex_example.mojo#L1-15
import numojo as nm
from numojo.prelude import *


fn main() raises:
    var z = 3 + 4 * `1j`
    var arr = nm.full[cf32](Shape(2, 2), fill_value=CScalar[cf32](z))

    print("z:", z)
    print("arr:")
    print(arr)

    var arr2 = nm.ones[cf32](Shape(2, 2))
    print("arr * arr2:")
    print(arr * arr2)
```

## What to read next

- `docs/getting-started/installation.md`
- `docs/user-guide/ndarray-creation-manipulation.md`
- `docs/user-guide/indexing.md`
- `docs/user-guide/linalg.md`
- `docs/developer-guide/architecture.md`
