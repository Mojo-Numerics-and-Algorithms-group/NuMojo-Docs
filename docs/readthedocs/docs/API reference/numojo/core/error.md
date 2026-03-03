# `numojo.core.error`

Error handling for Numojo library operations.

This module provides a simple, unified error system for the Numojo library.
All errors use a single NumojoError type with different categories for
better organization while keeping the implementation simple. This provides a better user experience by
providing clear error message and suggestions for fixing the error.

Currently we have a few common error categories like
- IndexError
- ShapeError
- BroadcastError
- MemoryError
- ValueError
- ArithmeticError

We can expand this list in the future as needed.

## Aliases

### `RED_COLOR`

```mojo
comptime RED_COLOR
```

**Value:** `"\1B[31m"`

### `END_COLOR`

```mojo
comptime END_COLOR
```

**Value:** `"\1B[0m"`

## Structs

### `NumojoError`

```mojo
struct NumojoError
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `ImplicitlyDestructible`, `Writable`

Unified error type for all Numojo operations.

Args:
    category: Type of error (e.g., "ShapeError", "IndexError").
    message: Main error description and suggestion.
    location: Optional context about where error occurred.

#### Fields

- **`category`** (`String`)
- **`message`** (`String`)
- **`location`** (`Optional[String]`)

#### Aliases

##### `ErrorDict`

```mojo
comptime ErrorDict
```

**Value:** `Dict(List("index", "shape", "broadcast", "memory", "value", "arithmetic", Tuple()), List("IndexError", "ShapeError", "BroadcastError", "MemoryError", "ValueError", "ArithmeticError", Tuple()), Tuple())`

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `False`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
__init__(out self, category: StringLiteral[category.value], message: StringLiteral[message.value], location: StringLiteral[location.value])
```

<span class="badge badge-static">static</span>

**Args:**

- `category` (`StringLiteral`)
- `message` (`StringLiteral`)
- `location` (`StringLiteral`)
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 2

```mojo
__init__(out self, category: StringLiteral[category.value], message: String, location: Optional[String] = None)
```

<span class="badge badge-static">static</span>

**Args:**

- `category` (`StringLiteral`)
- `message` (`String`)
- `location` (`Optional`)
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


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

##### `write_to`

```mojo
write_to[W: Writer](self, mut writer: W)
```

Write error information to a writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`


</div>
## Functions


<div class="fn-card" markdown="1">

### `terminate`

```mojo
terminate(message: String)
```

Abort the program with the given error message.

**Args:**

- `message` (`String`)


</div>
