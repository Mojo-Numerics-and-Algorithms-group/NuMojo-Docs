# `numojo.core.error`

Unified error system for NuMojo operations.

Provides a simple, categorized error type for all NuMojo operations with
clear, actionable error messages.

Exports
-------
- `NumojoError`: Unified error type with categories.

Categories:
    - index: Indexing errors
    - shape: Shape mismatch errors
    - broadcast: Broadcasting errors
    - memory: Memory allocation errors
    - value: Value errors
    - arithmetic: Arithmetic operation errors

## Aliases

### `RED_COLOR`

```mojo
comptime RED_COLOR
```

**Value:** `String("\1B[31m")`

### `END_COLOR`

```mojo
comptime END_COLOR
```

**Value:** `String("\1B[0m")`

## Structs

### `NumojoError`

```mojo
struct NumojoError
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Deinitable`, `Movable`, `Writable`

Unified error type for all Numojo operations.

Args:
    category: Type of error (e.g., "ShapeError", "IndexError").
    message: Main error description.
    location: Optional context about where error occurred.

Notes:
All NumojoErrors use a single unified type with different categories for better organization.
Error messages follow the format: "Category: Specific problem. Expected X but got Y."

#### Fields

- **`category`** (`String`)
- **`message`** (`String`)
- **`location`** (`Optional[String]`)

#### Aliases

##### `ErrorDict`

```mojo
comptime ErrorDict
```

**Value:** `Dict(List(String("index"), String("shape"), String("broadcast"), String("memory"), String("value"), String("arithmetic"), __list_literal__=NoneType(None)), List(String("IndexError"), String("ShapeError"), String("BroadcastError"), String("MemoryError"), String("ValueError"), String("ArithmeticError"), __list_literal__=NoneType(None)), NoneType(None))`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
def __init__(out self, category: StringLiteral, message: StringLiteral, location: StringLiteral)
```

<span class="badge badge-static">static</span>

**Args:**

- `category` (`StringLiteral`) `[imm]`
- `message` (`StringLiteral`) `[imm]`
- `location` (`StringLiteral`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 2

```mojo
def __init__(out self, category: StringLiteral, message: String, location: Optional[String] = None)
```

<span class="badge badge-static">static</span>

**Args:**

- `category` (`StringLiteral`) `[imm]`
- `message` (`String`) `[imm]`
- `location` (`Optional[String]`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 3

```mojo
def __init__(out self, category: StringLiteral, message: TString, location: StringLiteral)
```

<span class="badge badge-static">static</span>

**Args:**

- `category` (`StringLiteral`) `[imm]`
- `message` (`TString`) `[imm]`
- `location` (`StringLiteral`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
def __str__(self) -> String
```

Return string representation of the error with formatting.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `write_to`

```mojo
def write_to[W: Writer](self, mut writer: W)
```

Write error information to a writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`


</div>
## Functions


<div class="fn-card" markdown="1">

### `terminate`

```mojo
def terminate(message: String)
```

Abort the program with the given error message.

Notes:
This function is used for fatal, unrecoverable errors that require immediate termination.
The message will be displayed in red color before the program exits.

**Args:**

- `message` (`String`) `[imm]`: The error message to display before aborting.


</div>
