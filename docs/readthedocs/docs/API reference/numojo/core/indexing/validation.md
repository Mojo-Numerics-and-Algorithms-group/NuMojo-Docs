# `numojo.core.indexing.validation`

Validation (numojo.core.indexing.validation)

Contains utilities for validating indices, shapes, and axes for various indexing and reduction operations.

## Structs

### `Validator`

```mojo
struct Validator
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `ImplicitlyDestructible`

#### Aliases

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `True`

#### Methods


<div class="fn-card" markdown="1">

##### `normalize`

```mojo
normalize(index: Int, dim: Int) -> Int
```

<span class="badge badge-static">static</span>

Normalize a possibly negative index.

**Args:**

- `index` (`Int`): The index to normalize.
- `dim` (`Int`): The size of the dimension.

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `check_bounds`

```mojo
check_bounds(index: Int, dim: Int, axis: Int = 0)
```

<span class="badge badge-static">static</span>

Check if an index is within bounds for a dimension.

**Args:**

- `index` (`Int`): The index to check.
- `dim` (`Int`): The size of the dimension.
- `axis` (`Int`): The axis index (for error reporting).

!!! failure "Raises"
    Error: If the index is out of bounds.


</div>

<div class="fn-card" markdown="1">

##### `validate_reshape`

```mojo
validate_reshape(current_size: Int, new_shape: NDArrayShape)
```

<span class="badge badge-static">static</span>

Validate if a reshape operation is valid.

**Args:**

- `current_size` (`Int`): Current total number of elements.
- `new_shape` (`NDArrayShape`): The target shape.

!!! failure "Raises"
    Error: If the reshape is invalid.


</div>

<div class="fn-card" markdown="1">

##### `validate_and_normalize_axes`

```mojo
validate_and_normalize_axes(rank: Int, axes: List[Int]) -> List[Int]
```

<span class="badge badge-static">static</span>

Validate and normalize axes for reduction operations.

**Args:**

- `rank` (`Int`): The rank of the array.
- `axes` (`List`): The input axes.

**Returns:**

- `List`

!!! failure "Raises"
    Error: If any axis is invalid or duplicated.


</div>
