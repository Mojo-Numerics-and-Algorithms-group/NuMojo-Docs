# `numojo.core.layout.flags`

Memory layout information for NuMojo arrays.

Exports
-------
- `Flags`: Layout flags.

## Structs

### `Flags`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct Flags
```

**Memory convention:** `register_passable`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`, `RegisterPassable`

Information about the memory layout of the array. The Flags object can be accessed dictionary-like. or by using lowercased attribute names. Short names are available for convenience when using dictionary-like access.

</div>

#### Fields

- **`C_CONTIGUOUS`** (`Bool`): C_CONTIGUOUS (C): The data is in a C-style contiguous segment.
- **`F_CONTIGUOUS`** (`Bool`): F_CONTIGUOUS (F): The data is in a Fortran-style contiguous segment.
- **`OWNDATA`** (`Bool`): OWNDATA (O): The array owns the underlying data buffer.
- **`WRITEABLE`** (`Bool`): The data area can be written to. If it is False, the data is read-only and be blocked from writing. The WRITEABLE field of a view or slice is inherited from the array where it is derived. If the parent object is not writeable, the child object is also not writeable. If the parent object is writeable, the child object may be not writeable.
- **`FORC`** (`Bool`): F_CONTIGUOUS or C_CONTIGUOUS.

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

<div class="overload-divider">Overload 1</div>

```mojo
def __init__(c_contiguous: Bool, f_contiguous: Bool, owndata: Bool, writeable: Bool) -> Self
```

<span class="badge badge-static">static</span>

Initializes the Flags object with provided information.

<div class="prose-label">Args</div>

- `c_contiguous` (`Bool`) `[imm]`: The data is in a C-style contiguous segment.
- `f_contiguous` (`Bool`) `[imm]`: The data is in a Fortran-style contiguous segment.
- `owndata` (`Bool`) `[imm]`: The array owns the underlying data buffer.
- `writeable` (`Bool`) `[imm]`: The data area can be written to.
    If owndata is False, writeable is forced to be False.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __init__(out self, shape: NDArrayShape, strides: NDArrayStrides, owndata: Bool, writeable: Bool)
```

<span class="badge badge-static">static</span>

Initializes the Flags object according to the shape and strides information.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the array.
- `strides` (`NDArrayStrides`) `[imm]`: The strides of the array.
- `owndata` (`Bool`) `[imm]`: The array owns the underlying data buffer.
- `writeable` (`Bool`) `[imm]`: The data area can be written to.
    If owndata is False, writeable is forced to be False.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def __init__(shape: Tuple[Int, Int], strides: Tuple[Int, Int], owndata: Bool, writeable: Bool) -> Self
```

<span class="badge badge-static">static</span>

Initializes the Flags object according the shape and strides information.

<div class="prose-label">Args</div>

- `shape` (`Tuple[Int, Int]`) `[imm]`: The shape of the array.
- `strides` (`Tuple[Int, Int]`) `[imm]`: The strides of the array.
- `owndata` (`Bool`) `[imm]`: The array owns the underlying data buffer.
- `writeable` (`Bool`) `[imm]`: The data area can be written to.
    If owndata is False, writeable is forced to be False.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 4</div>

```mojo
def __init__(*, copy: Self) -> Self
```

<span class="badge badge-static">static</span>

Initializes the Flags object by copying the information from ancopy Flags object.

<div class="prose-label">Args</div>

- `copy` (`Self`) `[imm]`: The Flags object to copy information from.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__getitem__`

```mojo
def __getitem__(self, key: String) -> Bool
```

Get the value of the fields with the given key. The Flags object can be accessed dictionary-like. Short names are available for convenience.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `key` (`String`) `[imm]`: The key of the field to get.

<div class="prose-label">Returns</div>

- `Bool`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
