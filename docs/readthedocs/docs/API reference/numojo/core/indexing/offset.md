# `numojo.core.indexing.offset`

Indexing offset calculation functions.

Computes the flat index (offset) in memory for a given set of
multi-dimensional indices and strides, translating multi-dimensional
indexing into flat memory access.

Exports
-------
- `IndexMethods`: Offset calculation utilities.

## Structs

### `IndexMethods`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct IndexMethods
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Deinitable`, `Movable`

</div>

#### Methods


<div class="fn-card" markdown="1">

#### `get_1d_index`

<div class="overload-divider">Overload 1</div>

```mojo
def get_1d_index(indices: List[Int], strides: NDArrayStrides) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from a list of indices and NDArrayStrides.

<div class="prose-label">Args</div>

- `indices` (`List[Int]`) `[imm]`: The list of indices.
- `strides` (`NDArrayStrides`) `[imm]`: The strides of the array.

<div class="prose-label">Returns</div>

- `Int`

<div class="overload-divider">Overload 2</div>

```mojo
def get_1d_index(indices: Item, strides: NDArrayStrides) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from an Item and NDArrayStrides.

<div class="prose-label">Args</div>

- `indices` (`Item`) `[imm]`: The Item containing indices.
- `strides` (`NDArrayStrides`) `[imm]`: The strides of the array.

<div class="prose-label">Returns</div>

- `Int`

<div class="overload-divider">Overload 3</div>

```mojo
def get_1d_index(indices: VariadicList[Int], strides: NDArrayStrides) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from a variadic list of indices and NDArrayStrides.

<div class="prose-label">Args</div>

- `indices` (`VariadicList[Int]`) `[imm]`: The variadic list of indices.
- `strides` (`NDArrayStrides`) `[imm]`: The strides of the array.

<div class="prose-label">Returns</div>

- `Int`

<div class="overload-divider">Overload 4</div>

```mojo
def get_1d_index(indices: List[Int], strides: List[Int]) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from a list of indices and a list of strides.

<div class="prose-label">Args</div>

- `indices` (`List[Int]`) `[imm]`: The list of indices.
- `strides` (`List[Int]`) `[imm]`: The list of strides.

<div class="prose-label">Returns</div>

- `Int`

<div class="overload-divider">Overload 5</div>

```mojo
def get_1d_index(indices: VariadicList[Int], strides: VariadicList[Int]) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from variadic lists of indices and strides.

<div class="prose-label">Args</div>

- `indices` (`VariadicList[Int]`) `[imm]`: The variadic list of indices.
- `strides` (`VariadicList[Int]`) `[imm]`: The variadic list of strides.

<div class="prose-label">Returns</div>

- `Int`

<div class="overload-divider">Overload 6</div>

```mojo
def get_1d_index(indices: Tuple[Int, Int], strides: Tuple[Int, Int]) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index for a 2D matrix from tuples of indices and strides.

<div class="prose-label">Args</div>

- `indices` (`Tuple[Int, Int]`) `[imm]`: The tuple of indices (row, col).
- `strides` (`Tuple[Int, Int]`) `[imm]`: The tuple of strides.

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `transfer_offset`

```mojo
def transfer_offset(offset: Int, strides: NDArrayStrides) -> Int
```

<span class="badge badge-static">static</span>

Transfers the offset by flipping the strides information. Used to transfer between C-contiguous and F-continuous memory layouts.

<div class="prose-label">Args</div>

- `offset` (`Int`) `[imm]`: The offset in memory of an element.
- `strides` (`NDArrayStrides`) `[imm]`: The strides of the array.

<div class="prose-label">Returns</div>

- `Int`

!!! failure "Raises"


</div>
