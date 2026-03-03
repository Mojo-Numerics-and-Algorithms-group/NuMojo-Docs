# Input and Output (I/O)

This guide covers practical I/O workflows in NuMojo:
- saving and loading arrays
- text export/import
- display formatting
- interoperability notes (including DLPack workflows)

NuMojo currently focuses on numerical array I/O patterns similar to NumPy.

---

## 1) Saving and loading binary data

NuMojo provides binary save/load helpers for arrays.

## Save an array

```/dev/null/example_save.mojo#L1-11
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[f32](12).reshape(Shape(3, 4))
    nm.save(a, "array_data.nm")
    print("Saved:", a.shape, a.dtype)
```

## Load an array

```/dev/null/example_load.mojo#L1-10
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var b = nm.load[f32]("array_data.nm")
    print("Loaded:")
    print(b)
    print("Shape:", b.shape, "DType:", b.dtype)
```

### Notes
- Keep dtype explicit when required by your load path.
- Use binary save/load when you want better fidelity and performance than text files.

---

## 2) Text-based I/O (`savetxt` / `loadtxt`)

Text files are useful for debugging, inspection, and interoperability with simple tools.

## Save as text

```/dev/null/example_savetxt.mojo#L1-10
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var x = nm.linspace[f64](0, 1, 6).reshape(Shape(2, 3))
    nm.savetxt(x, "array.txt")
    print("Text file written.")
```

## Load from text

```/dev/null/example_loadtxt.mojo#L1-10
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var y = nm.loadtxt[f64]("array.txt")
    print("Loaded from text:")
    print(y)
```

### When to use text I/O
- sharing quick results with teammates
- sanity-checking values in a human-readable format
- passing data through CSV-like workflows (if formatting constraints are simple)

### Caveat
Text parsing/serialization is slower and can lose precision compared to binary formats.

---

## 3) Print formatting for arrays

Use `set_printoptions` to control how arrays are displayed.

```/dev/null/example_printoptions.mojo#L1-15
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.random.randn[f64](Shape(3, 3))
    print("Default:")
    print(a)

    nm.set_printoptions(precision=3, suppress=True)
    print("Formatted:")
    print(a)
```

Typical formatting controls include:
- precision
- suppression of scientific notation for small values
- line width/threshold behaviors (depending on current implementation)

Use formatting options for logs and notebooks, not as a data persistence strategy.

---

## 4) DLPack interoperability (NumPy/PyTorch workflows)

NuMojo includes DLPack utilities in core memory modules for zero-copy style interoperability where supported by producer/consumer frameworks.

High-level flow:
1. create array/tensor in external framework (NumPy/PyTorch/etc.)
2. pass DLPack capsule/object
3. construct NuMojo array from it

Example pattern (conceptual):

```/dev/null/example_dlpack_pattern.mojo#L1-15
from python import Python
from numojo.core.memory.dlpack import from_dlpack
from numojo.prelude import *

fn main() raises:
    var np = Python.import_module("numpy")
    var arr_np = np.random.rand(4, 4).astype(np.float32)

    # Depending on producer support, pass dlpack capsule or compatible object
    var arr_nm = from_dlpack[f32](arr_np)
    print(arr_nm)
```

### DLPack guidance
- validate dtype and shape assumptions explicitly
- be clear about ownership/lifetime semantics when sharing memory
- test mutability expectations (read-only vs writable) in both directions

---

## 5) Recommended I/O strategy by use case

### Experimentation / quick checks
- `savetxt` / `loadtxt`
- formatted printing with `set_printoptions`

### Production-ish pipelines
- binary `save` / `load`
- deterministic dtype handling
- explicit shape checks after load

### Cross-framework interoperability
- DLPack path for in-memory transfer
- add validation and fallback copy paths in critical code

---

## 6) Validation checklist after loading data

After any load operation, verify:
1. dtype is expected
2. shape matches downstream assumptions
3. value range/statistics are sane (min/max/mean spot check)
4. memory layout assumptions hold if needed for performance-sensitive paths

Example:

```/dev/null/example_post_load_validation.mojo#L1-16
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.load[f32]("array_data.nm")

    if a.shape != Shape(3, 4):
        raise Error("Unexpected shape after load")

    print("min:", nm.min(a))
    print("max:", nm.max(a))
    print("mean:", nm.mean(a))
```

---

## 7) Common mistakes

- relying on printed output as your persistent storage format
- forgetting dtype on load paths that require it
- assuming text I/O preserves full floating precision
- skipping shape validation after load
- assuming DLPack always implies writable zero-copy semantics

---

## 8) Related docs

- `docs/getting-started/quickstart.md`
- `docs/user-guide/ndarray-creation-manipulation.md`
- `docs/user-guide/indexing.md`
- `docs/user-guide/linalg.md`
- `docs/developer-guide/ndarray-basic-structure.md`
