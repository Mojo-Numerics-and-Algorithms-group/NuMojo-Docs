# `numojo.core.indexing.slicing`

Slicing (numojo.core.indexing.slicing)

This module defines internal data structures and utilities for handling slicing operations in NuMojo.

## Structs

### `IndexTypeInfo`

```mojo
struct IndexTypeInfo
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `ImplicitlyCopyable`, `ImplicitlyDestructible`, `Movable`

#### Fields

- **`is_integer`** (`Bool`)
- **`is_slice`** (`Bool`)
- **`is_ellipsis`** (`Bool`)
- **`is_newaxis`** (`Bool`)

#### Aliases

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `True`

##### `__move_ctor_is_trivial`

```mojo
comptime __move_ctor_is_trivial
```

**Value:** `True`

##### `__copy_ctor_is_trivial`

```mojo
comptime __copy_ctor_is_trivial
```

**Value:** `True`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
__init__(out self, is_integer: Bool = False, is_slice: Bool = False, is_ellipsis: Bool = False, is_newaxis: Bool = False)
```

<span class="badge badge-static">static</span>

**Args:**

- `is_integer` (`Bool`)
- `is_slice` (`Bool`)
- `is_ellipsis` (`Bool`)
- `is_newaxis` (`Bool`)
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__repr__`

```mojo
__repr__(self) -> String
```

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
__str__(self) -> String
```

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `size`

```mojo
size(self) -> Int
```

Returns the number of active index types in this IndexTypeInfo.

**Args:**

- `self` (`Self`)

**Returns:**

- `Int`


</div>
### `InternalSlice`

```mojo
struct InternalSlice
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `ImplicitlyCopyable`, `ImplicitlyDestructible`, `Movable`

#### Fields

- **`start`** (`Int`)
- **`end`** (`Int`)
- **`step`** (`Int`)

#### Aliases

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `True`

##### `__move_ctor_is_trivial`

```mojo
comptime __move_ctor_is_trivial
```

**Value:** `True`

##### `__copy_ctor_is_trivial`

```mojo
comptime __copy_ctor_is_trivial
```

**Value:** `True`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
__init__(out self, start: Int, end: Int, step: Int)
```

<span class="badge badge-static">static</span>

**Args:**

- `start` (`Int`)
- `end` (`Int`)
- `step` (`Int`)
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
__eq__(self, other: Self) -> Bool
```

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
__ne__(self, other: Self) -> Bool
```

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__repr__`

```mojo
__repr__(self) -> String
```

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
__str__(self) -> String
```

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `to_tuple`

```mojo
to_tuple(self) -> Tuple[Int, Int, Int]
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Tuple`


</div>

<div class="fn-card" markdown="1">

##### `to_slice`

```mojo
to_slice(self) -> Slice
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Slice`


</div>

<div class="fn-card" markdown="1">

##### `normalize`

```mojo
normalize(self, dim: Int) -> Self
```

**Args:**

- `self` (`Self`)
- `dim` (`Int`)

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `check_bounds`

```mojo
check_bounds(self, dim: Int)
```

**Args:**

- `self` (`Self`)
- `dim` (`Int`)

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `get_slice_info`

###### Overload 1

```mojo
get_slice_info(s: Slice, dim: Int) -> Tuple[Int, Int, Int, Int]
```

<span class="badge badge-static">static</span>

Get complete slice information for a given dimension.

Notes:
For cases with step = 0, error handling should be done prior to calling this function.

**Args:**

- `s` (`Slice`): The slice to process.
- `dim` (`Int`): The dimension size to process against.

**Returns:**

- `Tuple`

###### Overload 2

```mojo
get_slice_info(self, dim: Int) -> Tuple[Int, Int, Int, Int]
```

Get complete slice information for a given dimension.

**Args:**

- `self` (`Self`)
- `dim` (`Int`): The dimension size to process against.

**Returns:**

- `Tuple`


</div>
