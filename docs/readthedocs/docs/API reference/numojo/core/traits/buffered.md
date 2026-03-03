# `numojo.core.traits.buffered`

## Traits

### `Buffered`

**Extends:** `AnyType`, `Copyable`, `ImplicitlyCopyable`, `ImplicitlyDestructible`, `Movable`

A trait to denote whether the data buffer is owned or not.

There will be two implementations:
1. `OwnData`: for arrays that own their data buffer.
2. `RefData`: for arrays that do not own their data buffer.

The `RefData` type will record the origin of the data to ensure safety.

#### Aliases

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

A flag (often compiler generated) to indicate whether the implementation of `__del__` is trivial.

The implementation of `__del__` is considered to be trivial if:
- The struct has a compiler-generated trivial destructor and all its fields
  have a trivial `__del__` method.

In practice, it means that the `__del__` can be considered as no-op.

##### `__copy_ctor_is_trivial`

```mojo
comptime __copy_ctor_is_trivial
```

A flag (often compiler generated) to indicate whether the implementation of the copy constructor is trivial.

A copy constructor is considered to be trivial if:
- The struct has a compiler-generated trivial copy constructor because all
  its fields have trivial copy constructors.

In practice, it means the value can be copied by copying the bits from
one location to another without side effects.

##### `__move_ctor_is_trivial`

```mojo
comptime __move_ctor_is_trivial
```

A flag (often compiler generated) to indicate whether the implementation of move constructor is trivial.

The implementation of a move constructor is considered to be trivial if:
- The struct has a compiler-generated trivial move constructor because all
  its fields have trivial move constructors.

In practice, it means the value can be moved by moving the bits from
one location to another without side effects.

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
__init__(out self: _Self)
```

<span class="badge badge-static">static</span>

**Args:**

- `self` (`_Self`) `[out]`

**Returns:**

- `_Self`

###### Overload 2

```mojo
__init__(out self: _Self, *, copy: _Self)
```

<span class="badge badge-static">static</span>

Create a new instance of the value by copying an existing one.

**Args:**

- `copy` (`_Self`): The value to copy.
- `self` (`_Self`) `[out]`

**Returns:**

- `_Self`

###### Overload 3

```mojo
__init__(out self: _Self, *, deinit take: _Self)
```

<span class="badge badge-static">static</span>

Create a new instance of the value by moving the value of another.

**Args:**

- `take` (`_Self`) `[deinit]`: The value to move.
- `self` (`_Self`) `[out]`

**Returns:**

- `_Self`


</div>

<div class="fn-card" markdown="1">

##### `is_own_data`

```mojo
is_own_data() -> Bool
```

<span class="badge badge-static">static</span>

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_ref_data`

```mojo
is_ref_data() -> Bool
```

<span class="badge badge-static">static</span>

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
__str__(self: _Self) -> String
```

**Args:**

- `self` (`_Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `copy`

```mojo
copy(self: _Self) -> _Self
```

Explicitly construct a copy of self, a convenience method for `Self(copy=self)` when the type is inconvenient to write out.

**Args:**

- `self` (`_Self`)

**Returns:**

- `_Self`


</div>
