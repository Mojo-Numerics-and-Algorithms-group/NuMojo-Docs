# `numojo.routines.io.torch`

Pure-Mojo reader and writer for a single plain tensor saved with `torch.save`.

A `.pt` file is a ZIP archive holding a pickled object graph plus the
tensor's raw storage. This module recognizes only the fixed pickle shape a
bare `torch.save(tensor, path)` produces, not general pickle.

Exports
-------
- `save_torch`: Write an NDArray to a `.pt` file as a single tensor.
- `load_torch`: Read an NDArray from a `.pt` file holding a single tensor.

Notes
-----
- Only a file holding exactly one plain `torch.Tensor` is understood; a
  state dict, a full model, or any other pickled object raises.
- Only dtypes with a direct PyTorch storage equivalent can round-trip:
  `bool`, the signed integers up to 64 bits, `uint8`, and
  `float16`/`bfloat16`/`float32`/`float64`.
- `load_torch` only reads `'cpu'` tensors; it raises for CUDA/MPS.
- `requires_grad` and the autograd graph are not represented by `NDArray`;
  `save_torch` always writes `requires_grad=False`.
- Only the ZIP-archive `.pt` format (PyTorch's default since 1.6) is
  understood; ZIP64 and the legacy bare-pickle format are not.
- 0-d (scalar) tensors raise: NuMojo's `NDArray` has no rank-0 support yet.

## Functions


<div class="fn-card" markdown="1">

### `load_torch`

```mojo
def load_torch[dtype: DType](path: String) -> NDArray[dtype]
```

Reads a single tensor from a PyTorch `.pt` file, with no Python or `torch` involved.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.routines.io.torch import load_torch

var a = load_torch[nm.f32]("weights.pt")
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Expected datatype of the NDArray elements.

<div class="prose-label">Args</div>

- `path` (`String`) `[imm]`: File path to read from.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `dtype` has no PyTorch storage equivalent; if the
file is not an uncompressed, non-ZIP64 `.pt` archive holding a
single plain `torch.Tensor`; if the file's dtype or device
doesn't match what was requested; or if the tensor is 0-d.


</div>

<div class="fn-card" markdown="1">

### `save_torch`

```mojo
def save_torch[dtype: DType](path: String, A: NDArray[dtype])
```

Writes an NDArray to a PyTorch `.pt` file as a single, `'cpu'`, `requires_grad=False` tensor, with no Python or `torch` involved.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.routines.io.torch import save_torch

var a = nm.arange[nm.f32](6).reshape(nm.Shape(2, 3))
save_torch("a.pt", a)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Datatype of the NDArray elements.

<div class="prose-label">Args</div>

- `path` (`String`) `[imm]`: File path to write to.
- `A` (`NDArray[dtype]`) `[imm]`: The array to save.

!!! failure "Raises"
    NumojoError: If `dtype` has no PyTorch storage equivalent (unsigned
widths above 8 bits, `int128`, `int256`, `uint128`, `uint256`);
or if `A` is 0-d (NuMojo's `NDArray` does not support rank-0
arrays yet).


</div>
