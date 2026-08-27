# `numojo.core.indexing.slicing`

Internal data structures and utilities for handling array slicing operations.

This module provides the internal infrastructure for slicing arrays, including
type information tracking for different index types (integer, slice, ellipsis, newaxis).

Notes:
    - This module is internal to NuMojo and not part of the public API.
    - Used internally for slice parsing and validation.

Exports
-------
- `Slice`: Slice representation.

## Structs

### `IndexTypeInfo`

```mojo
struct IndexTypeInfo
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`

#### Fields

- **`is_integer`** (`Bool`)
- **`is_slice`** (`Bool`)
- **`is_ellipsis`** (`Bool`)
- **`is_newaxis`** (`Bool`)

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
def __init__(out self, is_integer: Bool = False, is_slice: Bool = False, is_ellipsis: Bool = False, is_newaxis: Bool = False)
```

<span class="badge badge-static">static</span>

**Args:**

- `is_integer` (`Bool`) `[imm]`
- `is_slice` (`Bool`) `[imm]`
- `is_ellipsis` (`Bool`) `[imm]`
- `is_newaxis` (`Bool`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__repr__`

```mojo
def __repr__(self) -> String
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
def __str__(self) -> String
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `size`

```mojo
def size(self) -> Int
```

Returns the number of active index types in this IndexTypeInfo.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`


</div>
### `InternalSlice`

```mojo
struct InternalSlice
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `ImplicitlyCopyable`, `Movable`

#### Fields

- **`start`** (`Int`)
- **`end`** (`Int`)
- **`step`** (`Int`)

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
def __init__(out self, start: Int, end: Int, step: Int)
```

<span class="badge badge-static">static</span>

**Args:**

- `start` (`Int`) `[imm]`
- `end` (`Int`) `[imm]`
- `step` (`Int`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
def __eq__(self, other: Self) -> Bool
```

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
def __ne__(self, other: Self) -> Bool
```

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__repr__`

```mojo
def __repr__(self) -> String
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
def __str__(self) -> String
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `to_tuple`

```mojo
def to_tuple(self) -> Tuple[Int, Int, Int]
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Tuple[Int, Int, Int]`


</div>

<div class="fn-card" markdown="1">

##### `to_slice`

```mojo
def to_slice(self) -> Slice
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Slice`


</div>

<div class="fn-card" markdown="1">

##### `normalize`

```mojo
def normalize(self, dim: Int) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`
- `dim` (`Int`) `[imm]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `check_bounds`

```mojo
def check_bounds(self, dim: Int)
```

**Args:**

- `self` (`Self`) `[imm]`
- `dim` (`Int`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `get_slice_info`

###### Overload 1

```mojo
def get_slice_info(s: Slice, dim: Int) -> Tuple[Int, Int, Int, Int]
```

<span class="badge badge-static">static</span>

Get complete slice information for a given dimension.

Notes:
For cases with step = 0, error handling should be done prior to calling this function.

**Args:**

- `s` (`Slice`) `[imm]`: The slice to process.
- `dim` (`Int`) `[imm]`: The dimension size to process against.

**Returns:**

- `Tuple[Int, Int, Int, Int]`

###### Overload 2

```mojo
def get_slice_info(self, dim: Int) -> Tuple[Int, Int, Int, Int]
```

Get complete slice information for a given dimension.

**Args:**

- `self` (`Self`) `[imm]`
- `dim` (`Int`) `[imm]`: The dimension size to process against.

**Returns:**

- `Tuple[Int, Int, Int, Int]`


</div>

<div class="fn-card" markdown="1">

##### `adjust_list`

```mojo
def adjust_list(shape: NDArrayShape, slice_list: List[Slice]) -> List[Self]
```

<span class="badge badge-static">static</span>

Normalises a list of `Slice` objects against the given array shape.

For each slice, resolves defaults, wraps negative indices, clamps
out-of-bounds values, and validates that the step is non-zero.
Returns one `InternalSlice` per input slice with concrete start, end,
and step values ready for use in traversal.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: The array shape; `shape[i]` is the size of dimension `i`.
- `slice_list` (`List[Slice]`) `[imm]`: Raw slices to normalise (one per dimension to process).

**Returns:**

- `List[Self]`

!!! failure "Raises"
    NumojoError: If any slice has a step of zero.


</div>
