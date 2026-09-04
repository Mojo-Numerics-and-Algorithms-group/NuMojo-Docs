# `numojo.core.layout.array_methods`

The `NewAxis` struct, used to represent the insertion of new axes into array shapes, similar to `None` / `np.newaxis` in NumPy.

Indicates where a new singleton dimension should be added to an array,
enabling advanced indexing and broadcasting operations.

Exports
-------
- `NewAxis`: Add singleton dimension.
- `newaxis`: Default `NewAxis` instance.

<div class="prose-label">Examples</div>
    ```mojo
    var a = NewAxis()      # Adds a single new axis
    var b = NewAxis(3)     # Adds three new axes
    ```

## Aliases

### `newaxis`

```mojo
comptime newaxis
```

**Value:** `NewAxis()`

## Structs

### `NewAxis`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct NewAxis
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Hashable`, `ImplicitlyCopyable`, `Movable`, `Writable`

Represents a new axis to be inserted into an array's shape.

The `NewAxis` struct is typically used in advanced indexing to add singleton dimensions
to arrays, facilitating broadcasting and reshaping operations.

Attributes:
    num (Int): The number of new axes to add.

</div>

#### Fields

- **`num`** (`Int`)

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

<div class="overload-divider">Overload 1</div>

```mojo
def __init__(out self)
```

<span class="badge badge-static">static</span>

Initializes a `NewAxis` instance with a default of one new axis.

Sets `num` to 0, which can be interpreted as a single new axis.

<div class="prose-label">Args</div>

- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __init__(out self, num: Int)
```

<span class="badge badge-static">static</span>

Initializes a `NewAxis` instance with a specified number of new axes.

<div class="prose-label">Args</div>

- `num` (`Int`) `[imm]`: The number of new axes to add.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__eq__`

```mojo
def __eq__(self, other: Self) -> Bool
```

Checks equality between two `NewAxis` instances.

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

Checks inequality between two `NewAxis` instances.

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

Returns a string representation of the `NewAxis` instance.

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

Returns a string representation of the `NewAxis` instance.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>
