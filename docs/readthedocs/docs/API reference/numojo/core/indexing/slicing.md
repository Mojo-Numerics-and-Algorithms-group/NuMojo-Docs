# `numojo.core.indexing.slicing`

Internal data structures and utilities for handling array slicing operations.

This module provides the internal infrastructure for slicing arrays, including
type information tracking for different index types (integer, slice, ellipsis, newaxis).

<div class="prose-label">Notes</div>
    - This module is internal to NuMojo and not part of the public API.
    - Used internally for slice parsing and validation.

Exports
-------
- `Slice`: Slice representation.

## Structs

### `IndexTypeInfo`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct IndexTypeInfo
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`

</div>

#### Fields

- **`is_integer`** (`Bool`)
- **`is_slice`** (`Bool`)
- **`is_ellipsis`** (`Bool`)
- **`is_newaxis`** (`Bool`)

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

```mojo
def __init__(out self, is_integer: Bool = False, is_slice: Bool = False, is_ellipsis: Bool = False, is_newaxis: Bool = False)
```

<span class="badge badge-static">static</span>

<div class="prose-label">Args</div>

- `is_integer` (`Bool`) `[imm]`
- `is_slice` (`Bool`) `[imm]`
- `is_ellipsis` (`Bool`) `[imm]`
- `is_newaxis` (`Bool`) `[imm]`
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__repr__`

```mojo
def __repr__(self) -> String
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>

<div class="fn-card" markdown="1">

#### `__str__`

```mojo
def __str__(self) -> String
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>

<div class="fn-card" markdown="1">

#### `size`

```mojo
def size(self) -> Int
```

Returns the number of active index types in this IndexTypeInfo.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>
### `InternalSlice`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct InternalSlice
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`

</div>

#### Fields

- **`start`** (`Int`)
- **`end`** (`Int`)
- **`step`** (`Int`)

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

```mojo
def __init__(out self, start: Int, end: Int, step: Int)
```

<span class="badge badge-static">static</span>

<div class="prose-label">Args</div>

- `start` (`Int`) `[imm]`
- `end` (`Int`) `[imm]`
- `step` (`Int`) `[imm]`
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__eq__`

```mojo
def __eq__(self, other: Self) -> Bool
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__ne__`

```mojo
def __ne__(self, other: Self) -> Bool
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__repr__`

```mojo
def __repr__(self) -> String
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>

<div class="fn-card" markdown="1">

#### `__str__`

```mojo
def __str__(self) -> String
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>

<div class="fn-card" markdown="1">

#### `to_tuple`

```mojo
def to_tuple(self) -> Tuple[Int, Int, Int]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Tuple[Int, Int, Int]`


</div>

<div class="fn-card" markdown="1">

#### `to_slice`

```mojo
def to_slice(self) -> Slice
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Slice`


</div>

<div class="fn-card" markdown="1">

#### `normalize`

```mojo
def normalize(self, dim: Int) -> Self
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `dim` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `check_bounds`

```mojo
def check_bounds(self, dim: Int)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `dim` (`Int`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `get_slice_info`

<div class="overload-divider">Overload 1</div>

```mojo
def get_slice_info(s: Slice, dim: Int) -> Tuple[Int, Int, Int, Int]
```

<span class="badge badge-static">static</span>

Get complete slice information for a given dimension.

<div class="prose-label">Notes</div>
For cases with step = 0, error handling should be done prior to calling this function.

<div class="prose-label">Args</div>

- `s` (`Slice`) `[imm]`: The slice to process.
- `dim` (`Int`) `[imm]`: The dimension size to process against.

<div class="prose-label">Returns</div>

- `Tuple[Int, Int, Int, Int]`

<div class="overload-divider">Overload 2</div>

```mojo
def get_slice_info(self, dim: Int) -> Tuple[Int, Int, Int, Int]
```

Get complete slice information for a given dimension.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `dim` (`Int`) `[imm]`: The dimension size to process against.

<div class="prose-label">Returns</div>

- `Tuple[Int, Int, Int, Int]`


</div>

<div class="fn-card" markdown="1">

#### `adjust_list`

```mojo
def adjust_list(shape: NDArrayShape, slice_list: List[Slice]) -> List[Self]
```

<span class="badge badge-static">static</span>

Normalises a list of `Slice` objects against the given array shape.

For each slice, resolves defaults, wraps negative indices, clamps
out-of-bounds values, and validates that the step is non-zero.
Returns one `InternalSlice` per input slice with concrete start, end,
and step values ready for use in traversal.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The array shape; `shape[i]` is the size of dimension `i`.
- `slice_list` (`List[Slice]`) `[imm]`: Raw slices to normalise (one per dimension to process).

<div class="prose-label">Returns</div>

- `List[Self]`

!!! failure "Raises"
    NumojoError: If any slice has a step of zero.


</div>
