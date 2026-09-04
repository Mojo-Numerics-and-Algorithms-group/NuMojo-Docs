# `numojo.core.indexing.validation`

Utilities for validating indices, shapes, and axes for various indexing and reduction operations.

Exports
-------
- `Validator`: Index validation utilities.

## Structs

### `Validator`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct Validator
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Deinitable`, `Movable`

</div>

#### Methods


<div class="fn-card" markdown="1">

#### `normalize`

```mojo
def normalize(index: Int, dim: Int) -> Int
```

<span class="badge badge-static">static</span>

Normalize a possibly negative index.

<div class="prose-label">Args</div>

- `index` (`Int`) `[imm]`: The index to normalize.
- `dim` (`Int`) `[imm]`: The size of the dimension.

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `check_bounds`

```mojo
def check_bounds(index: Int, dim: Int, axis: Int = Int(0))
```

<span class="badge badge-static">static</span>

Check if an index is within bounds for a dimension.

<div class="prose-label">Args</div>

- `index` (`Int`) `[imm]`: The index to check.
- `dim` (`Int`) `[imm]`: The size of the dimension.
- `axis` (`Int`) `[imm]`: The axis index (for error reporting).

!!! failure "Raises"
    NumojoError: If the index is out of bounds.


</div>

<div class="fn-card" markdown="1">

#### `validate_reshape`

```mojo
def validate_reshape(current_size: Int, new_shape: NDArrayShape)
```

<span class="badge badge-static">static</span>

Validate if a reshape operation is valid.

<div class="prose-label">Args</div>

- `current_size` (`Int`) `[imm]`: Current total number of elements.
- `new_shape` (`NDArrayShape`) `[imm]`: The target shape.

!!! failure "Raises"
    NumojoError: If the reshape is invalid.


</div>

<div class="fn-card" markdown="1">

#### `validate_and_normalize_axes`

```mojo
def validate_and_normalize_axes(rank: Int, axes: List[Int]) -> List[Int]
```

<span class="badge badge-static">static</span>

Validate and normalize axes for reduction operations.

<div class="prose-label">Args</div>

- `rank` (`Int`) `[imm]`: The rank of the array.
- `axes` (`List[Int]`) `[imm]`: The input axes.

<div class="prose-label">Returns</div>

- `List[Int]`

!!! failure "Raises"
    NumojoError: If any axis is invalid or duplicated.


</div>
