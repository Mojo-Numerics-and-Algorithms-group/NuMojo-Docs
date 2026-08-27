# `numojo.core.traits.buffered`

Trait for buffer ownership semantics.

Trait to denote whether a data buffer is owned or referenced. Implementations
distinguish between owned data (OwnData) and referenced data (RefData).

Exports
-------
- `Buffered`: Trait for buffer ownership.

## Traits

### `Buffered`

**Extends:** `AnyType`, `Copyable`, `ImplicitlyCopyable`, `Movable`

A trait to denote whether the data buffer is owned or not.

There will be two implementations:
1. `OwnData`: for arrays that own their data buffer.
2. `RefData`: for arrays that do not own their data buffer.

The `RefData` type will record the origin of the data to ensure safety.

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
def __init__(out self)
```

<span class="badge badge-static">static</span>

**Args:**

- `self` (`_Self`) `[out]`

**Returns:**

- `_Self`

###### Overload 2

```mojo
def __init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

Create a new instance of the value by copying an existing one.

**Args:**

- `copy` (`_Self`) `[imm]`: The value to copy.
- `self` (`_Self`) `[out]`

**Returns:**

- `_Self`

###### Overload 3

```mojo
def __init__(out self, *, deinit move: Self)
```

<span class="badge badge-static">static</span>

Create a new instance of the value by moving the value of another.

**Args:**

- `move` (`_Self`) `[deinit]`: The value to move.
- `self` (`_Self`) `[out]`

**Returns:**

- `_Self`


</div>

<div class="fn-card" markdown="1">

##### `is_own_data`

```mojo
def is_own_data() -> Bool
```

<span class="badge badge-static">static</span>

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_ref_data`

```mojo
def is_ref_data() -> Bool
```

<span class="badge badge-static">static</span>

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
def __str__(self) -> String
```

**Args:**

- `self` (`_Self`) `[imm]`

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `copy`

```mojo
def copy(self) -> Self
```

Explicitly construct a copy of self, a convenience method for `Self(copy=self)` when the type is inconvenient to write out.

Overriding this method is not allowed.

**Args:**

- `self` (`_Self`) `[imm]`

**Returns:**

- `_Self`


</div>
