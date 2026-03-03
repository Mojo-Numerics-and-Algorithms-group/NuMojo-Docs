# `numojo.core.layout.array_methods`

Array methods (numojo.core.layout.array_methods)

This module defines the `NewAxis` struct, which is used to represent the insertion of new axes into array shapes,
similar to the concept of `None` or `np.newaxis` in NumPy. The `NewAxis` struct can be used to indicate where
a new singleton dimension should be added to an array, enabling advanced indexing and broadcasting operations.

Example usage:
    newaxis = NewAxis()        # Adds a single new axis
    newaxis3 = NewAxis(3)      # Adds three new axes

Attributes:
    num (Int): The number of new axes to add. Defaults to 0 (single new axis).

## Aliases

### `newaxis`

```mojo
comptime newaxis
```

**Value:** `NewAxis()`

## Structs

### `NewAxis`

```mojo
struct NewAxis
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Hashable`, `ImplicitlyCopyable`, `ImplicitlyDestructible`, `Movable`, `Stringable`

Represents a new axis to be inserted into an array's shape.

The `NewAxis` struct is typically used in advanced indexing to add singleton dimensions
to arrays, facilitating broadcasting and reshaping operations.

Attributes:
    num (Int): The number of new axes to add.

#### Fields

- **`num`** (`Int`)

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

###### Overload 1

```mojo
__init__(out self)
```

<span class="badge badge-static">static</span>

Initializes a `NewAxis` instance with a default of one new axis.

Sets `num` to 0, which can be interpreted as a single new axis.

**Args:**

- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 2

```mojo
__init__(out self, num: Int)
```

<span class="badge badge-static">static</span>

Initializes a `NewAxis` instance with a specified number of new axes.

**Args:**

- `num` (`Int`): The number of new axes to add.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
__eq__(self, other: Self) -> Bool
```

Checks equality between two `NewAxis` instances.

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

Checks inequality between two `NewAxis` instances.

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

Returns a string representation of the `NewAxis` instance.

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

Returns a string representation of the `NewAxis` instance.

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>
