# `numojo.routines.io.npy`

Pure-Mojo reader and writer for NumPy's `.npy` array format.

`.npy` is a documented, self-contained binary format: a short magic prelude
followed by an ASCII header describing dtype/shape/order, followed by the raw
payload. This is distinct from `numojo.routines.io.files.save`/`load`, which route
through Python's `numpy.save`/`numpy.load` and therefore require Python.

Exports
-------
- `save_npy`: Write an NDArray to a `.npy` file.
- `load_npy`: Read an NDArray from a `.npy` file.

Notes
-----
- Only dtypes with a direct NumPy equivalent can round-trip: `bool`, the
  signed/unsigned integers up to 64 bits, and `float16`/`float32`/`float64`.
  NuMojo-only widths (`int128`, `int256`, `uint128`, `uint256`) and
  `bfloat16` have no NumPy dtype, so both directions raise for them.
- `save_npy` always writes format version 1.0 in C order (row-major); the
  source array is made contiguous first if it is not already.
- `load_npy` accepts version 1.0 and 2.0 headers, and both C- and
  Fortran-ordered payloads (the returned array matches the file's order).
  It rejects big-endian dtypes (`.npy` written on a big-endian machine) since
  nothing here byte-swaps.

## Functions


<div class="fn-card" markdown="1">

### `save_npy`

```mojo
def save_npy[dtype: DType](path: String, A: NDArray[dtype])
```

Writes an array to a `.npy` file (NumPy format version 1.0), with no Python involved.

The bytes are what `numpy.save` would write for the same array (C
order), so `numpy.load(path)` reads it back with the right dtype and
shape.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.routines.io.npy import save_npy, load_npy

var a = nm.arange[nm.f32](6).reshape(nm.Shape(2, 3))
save_npy("a.npy", a)
var b = load_npy[nm.f32]("a.npy")
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Datatype of the NDArray elements.

<div class="prose-label">Args</div>

- `path` (`String`) `[imm]`: File path to write to.
- `A` (`NDArray[dtype]`) `[imm]`: The array to save.

!!! failure "Raises"
    NumojoError: If `dtype` has no NumPy equivalent (`int128`, `int256`,
`uint128`, `uint256`, or `bfloat16`).


</div>

<div class="fn-card" markdown="1">

### `load_npy`

```mojo
def load_npy[dtype: DType](path: String) -> NDArray[dtype]
```

Reads an array from a `.npy` file written by `numpy.save` (or by `save_npy`), with no Python involved.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.routines.io.npy import load_npy

var a = load_npy[nm.f32]("a.npy")
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Expected datatype of the NDArray elements.

<div class="prose-label">Args</div>

- `path` (`String`) `[imm]`: File path to read from.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `dtype` has no NumPy equivalent; if the file is not
a `.npy` file, is truncated, or uses an unsupported format
version; if the file's dtype does not match `dtype` (including
big-endian files, which nothing here byte-swaps); or if the
payload size disagrees with the header.


</div>
