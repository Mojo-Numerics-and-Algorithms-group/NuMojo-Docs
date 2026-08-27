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

```mojo
struct IndexMethods
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Deinitable`, `Movable`

#### Methods


<div class="fn-card" markdown="1">

##### `get_1d_index`

###### Overload 1

```mojo
def get_1d_index(indices: List[Int], strides: NDArrayStrides) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from a list of indices and NDArrayStrides.

**Args:**

- `indices` (`List[Int]`) `[imm]`: The list of indices.
- `strides` (`NDArrayStrides`) `[imm]`: The strides of the array.

**Returns:**

- `Int`

###### Overload 2

```mojo
def get_1d_index(indices: Item, strides: NDArrayStrides) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from an Item and NDArrayStrides.

**Args:**

- `indices` (`Item`) `[imm]`: The Item containing indices.
- `strides` (`NDArrayStrides`) `[imm]`: The strides of the array.

**Returns:**

- `Int`

###### Overload 3

```mojo
def get_1d_index(indices: VariadicList[Int], strides: NDArrayStrides) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from a variadic list of indices and NDArrayStrides.

**Args:**

- `indices` (`VariadicList[Int]`) `[imm]`: The variadic list of indices.
- `strides` (`NDArrayStrides`) `[imm]`: The strides of the array.

**Returns:**

- `Int`

###### Overload 4

```mojo
def get_1d_index(indices: List[Int], strides: List[Int]) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from a list of indices and a list of strides.

**Args:**

- `indices` (`List[Int]`) `[imm]`: The list of indices.
- `strides` (`List[Int]`) `[imm]`: The list of strides.

**Returns:**

- `Int`

###### Overload 5

```mojo
def get_1d_index(indices: VariadicList[Int], strides: VariadicList[Int]) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from variadic lists of indices and strides.

**Args:**

- `indices` (`VariadicList[Int]`) `[imm]`: The variadic list of indices.
- `strides` (`VariadicList[Int]`) `[imm]`: The variadic list of strides.

**Returns:**

- `Int`

###### Overload 6

```mojo
def get_1d_index(indices: Tuple[Int, Int], strides: Tuple[Int, Int]) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index for a 2D matrix from tuples of indices and strides.

**Args:**

- `indices` (`Tuple[Int, Int]`) `[imm]`: The tuple of indices (row, col).
- `strides` (`Tuple[Int, Int]`) `[imm]`: The tuple of strides.

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `transfer_offset`

```mojo
def transfer_offset(offset: Int, strides: NDArrayStrides) -> Int
```

<span class="badge badge-static">static</span>

Transfers the offset by flipping the strides information. Used to transfer between C-contiguous and F-continuous memory layouts.

**Args:**

- `offset` (`Int`) `[imm]`: The offset in memory of an element.
- `strides` (`NDArrayStrides`) `[imm]`: The strides of the array.

**Returns:**

- `Int`

!!! failure "Raises"


</div>
