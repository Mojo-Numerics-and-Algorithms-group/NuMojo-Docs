# `numojo.routines.constants`

Mathematical and physical constants.

Physical and mathematical constants (pi, e, c) defined for compile-time
evaluation with indefinite precision.

Exports
-------
- `pi`: Mathematical constant π.
- `e`: Euler's number.
- `c`: Speed of light.

## Structs

### `Constants`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct Constants
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Movable`

Define constants.

Use comptime for compile time evaluation of indefinite precision.
```mojo
import numojo as nm
def main():
    var pi: Float64 = nm.pi
    print("Float64:", pi*pi*pi*pi*pi*pi)
    print("Literal:", nm.pi*nm.pi*nm.pi*nm.pi*nm.pi*nm.pi)
```

</div>

#### Aliases

#### `c`

```mojo
comptime c
```

**Value:** `299792458`

#### `pi`

```mojo
comptime pi
```

**Value:** `3.1415926535897931`

#### `e`

```mojo
comptime e
```

**Value:** `2.7182818284590451`

#### `hbar`

```mojo
comptime hbar
```

**Value:** `1.0545718176461565E-34`

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

```mojo
def __init__(out self)
```

<span class="badge badge-static">static</span>

Initializes the constants.

<div class="prose-label">Args</div>

- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__deinit__`

```mojo
def __deinit__(deinit self)
```

Deletes the constants.

<div class="prose-label">Args</div>

- `self` (`Self`) `[deinit]`


</div>
