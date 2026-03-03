# `numojo.routines.constants`

Constants (numojo.routines.constants)

This module defines physical and mathematical constants for use in numerical computations.
The constants are defined as class attributes of the `Constants` class, which is designed to be immutable and efficient for compile-time evaluation.

## Structs

### `Constants`

```mojo
struct Constants
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `ImplicitlyDestructible`, `Movable`

Define constants.

Use comptime for compile time evaluation of indefinite precision.
```mojo
import numojo as nm
fn main():
    var pi: Float64 = nm.pi
    print("Float64:", pi*pi*pi*pi*pi*pi)
    print("Literal:", nm.pi*nm.pi*nm.pi*nm.pi*nm.pi*nm.pi)
```
```console
Float64: 961.38919357530415
Literal: 961.38919357530449
```

#### Aliases

##### `c`

```mojo
comptime c
```

**Value:** `299792458`

##### `pi`

```mojo
comptime pi
```

**Value:** `3.1415926535897931`

##### `e`

```mojo
comptime e
```

**Value:** `2.7182818284590451`

##### `hbar`

```mojo
comptime hbar
```

**Value:** `1.0545718176461565E-34`

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `False`

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
__init__(out self)
```

<span class="badge badge-static">static</span>

Initializes the constants.

**Args:**

- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__del__`

```mojo
__del__(deinit self)
```

Deletes the constants.

**Args:**

- `self` (`Self`) `[deinit]`


</div>
