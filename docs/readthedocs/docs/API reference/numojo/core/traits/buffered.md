# `numojo.core.traits.buffered`

Trait for buffer ownership semantics.

Trait to denote whether a data buffer is owned or referenced. Implementations
distinguish between owned data (OwnData) and referenced data (RefData).

Exports
-------
- `Buffered`: Trait for buffer ownership.

## Traits

### `Buffered`

<div class="type-header" markdown="1">

<span class="badge badge-kind">trait</span>

**Extends:** `AnyType`, `Copyable`, `ImplicitlyCopyable`, `Movable`

A trait to denote whether the data buffer is owned or not.

There will be two implementations:
1. `OwnData`: for arrays that own their data buffer.
2. `RefData`: for arrays that do not own their data buffer.

The `RefData` type will record the origin of the data to ensure safety.

</div>

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

```mojo
def __init__(out self)
```

<span class="badge badge-static">static</span>

<div class="prose-label">Args</div>

- `self` (`_Self`) `[out]`

<div class="prose-label">Returns</div>

- `_Self`


</div>

<div class="fn-card" markdown="1">

#### `is_own_data`

```mojo
def is_own_data() -> Bool
```

<span class="badge badge-static">static</span>

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `is_ref_data`

```mojo
def is_ref_data() -> Bool
```

<span class="badge badge-static">static</span>

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__str__`

```mojo
def __str__(self) -> String
```

<div class="prose-label">Args</div>

- `self` (`_Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>
