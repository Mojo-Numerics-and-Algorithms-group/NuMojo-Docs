# NDArray Creation and Manipulation

This guide covers common `NDArray` creation and transformation workflows in NuMojo.

## Imports used in examples

```/dev/null/imports.mojo#L1-3
import numojo as nm
from numojo.prelude import *
```

---

## 1) Creating arrays

### Zeros, ones, full, empty

```/dev/null/create_basic.mojo#L1-12
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var z = nm.zeros[f32](Shape(2, 3))
    var o = nm.ones[f32](Shape(2, 3))
    var f = nm.full[f32](Shape(2, 3), fill_value=2.5)
    var e = nm.empty[f32](Shape(2, 3))

    print(z)
    print(o)
    print(f)
    print(e)
```

Notes:
- `empty` allocates memory without initializing values.
- Prefer `zeros`/`ones`/`full` unless you immediately overwrite all values.

### Ranges and spaces

```/dev/null/create_ranges.mojo#L1-11
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[f32](10)
    var b = nm.linspace[f32](0, 1, 5)
    var c = nm.logspace[f32](0, 3, 4)
    var d = nm.geomspace[f32](1, 1000, 4)

    print(a)
    print(b)
    print(c)
    print(d)
```

### Construct from text / literals

```/dev/null/create_from_text.mojo#L1-9
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.fromstring[f32]("[[1, 2, 3], [4, 5, 6]]")
    var b = nm.array[f32]("[[10, 20], [30, 40]]")

    print(a)
    print(b)
```

---

## 2) Inspecting array metadata

```/dev/null/inspect_metadata.mojo#L1-13
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[f32](12).reshape(Shape(3, 4))

    print("ndim:", nm.ndim(a))
    print("shape:", nm.shape(a))
    print("size:", nm.size(a))
    print("dtype:", a.dtype)
    print("is C contiguous:", a.is_c_contiguous())
    print("strides:", a.strides)
```

---

## 3) Reshaping and layout transforms

### reshape

```/dev/null/reshape.mojo#L1-10
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[f32](12)
    var b = nm.reshape(a, Shape(3, 4))
    var c = nm.reshape(b, Shape(2, 2, 3))

    print(a)
    print(b)
    print(c)
```

### ravel (flatten view/copy style behavior depends on layout safety)

```/dev/null/ravel.mojo#L1-8
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[f32](12).reshape(Shape(3, 4))
    var flat = nm.ravel(a)
    print(flat)
```

### transpose

```/dev/null/transpose.mojo#L1-9
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[f32](12).reshape(Shape(3, 4))
    var t = nm.transpose(a)

    print(a)
    print(t)
```

---

## 4) Broadcasting and shape expansion

### broadcast_to

```/dev/null/broadcast_to.mojo#L1-10
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var row = nm.arange[f32](4).reshape(Shape(1, 4))
    var expanded = nm.broadcast_to(row, Shape(3, 4))

    print("row:")
    print(row)
    print("expanded:")
    print(expanded)
```

### Scalar broadcasting in arithmetic

```/dev/null/scalar_broadcast.mojo#L1-10
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[f32](6).reshape(Shape(2, 3))
    var b = nm.add(a, SIMD[f32, 1](10))
    var c = nm.mul(a, SIMD[f32, 1](2))

    print(b)
    print(c)
```

---

## 5) Common manipulation operations

### flip

```/dev/null/flip.mojo#L1-9
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[f32](12).reshape(Shape(3, 4))
    var flipped = nm.flip(a)

    print(a)
    print(flipped)
```

### Basic slicing and subarray extraction

```/dev/null/slicing_extract.mojo#L1-12
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[f32](20).reshape(Shape(4, 5))

    var row0 = a[0, :]
    var col2 = a[:, 2]
    var block = a[1:3, 1:4]
    var step = a[::2, ::2]

    print(row0)
    print(col2)
    print(block)
    print(step)
```

---

## 6) Updating values after creation

### Set by index

```/dev/null/set_by_index.mojo#L1-10
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.zeros[f32](Shape(3, 3))
    a[Item(1, 1)] = 9
    a[Item(0, 2)] = 5

    print(a)
```

### Set by slice

```/dev/null/set_by_slice.mojo#L1-10
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.zeros[f32](Shape(4, 4))
    var patch = nm.ones[f32](Shape(2, 2))
    a[1:3, 1:3] = patch

    print(a)
```

---

## 7) Patterns for real projects

### Pattern A: initialize -> transform -> reduce

```/dev/null/pattern_a.mojo#L1-12
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var x = nm.linspace[f32](0, 10, 100)
    var y = nm.sin(x)
    var y2 = nm.mul(y, y)

    print("mean(y^2):", nm.mean(y2))
    print("max(y):", nm.max(y))
    print("min(y):", nm.min(y))
```

### Pattern B: batch-friendly shaping

```/dev/null/pattern_b.mojo#L1-12
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var raw = nm.arange[f32](2 * 3 * 4)
    var batch = nm.reshape(raw, Shape(2, 3, 4))  # (batch, rows, cols)

    var flattened_batch0 = nm.ravel(batch[0, :, :])
    print("batch shape:", batch.shape)
    print("batch[0] flattened:")
    print(flattened_batch0)
```

---

## 8) Pitfalls and best practices

- Prefer explicit `Shape(...)` for readability.
- Use consistent dtype in a workflow (`f32` vs `f64`) to avoid accidental casts.
- Validate axis values before reductions/manipulations in library code.
- Use `zeros/ones/full` over `empty` unless performance profiling proves otherwise.
- Keep transformations composable:
  - create → reshape → compute → reduce.

---

## 9) Related guides

- `docs/user-guide/indexing.md`
- `docs/user-guide/linalg.md`
- `docs/user-guide/io.md`
- `docs/getting-started/ndarray-vs-matrix.md`
