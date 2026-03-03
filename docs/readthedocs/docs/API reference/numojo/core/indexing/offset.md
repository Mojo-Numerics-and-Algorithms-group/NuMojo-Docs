# `numojo.core.indexing.offset`

Offset computation (numojo.core.indexing.offset)

Indexing offset calculation functions. These functions compute the flat index (offset)
in memory for a given set of multi-dimensional indices and strides.
They are used to translate multi-dimensional indexing into flat memory access,
which is essential for efficient array operations in NuMojo.

## Structs

### `IndexMethods`

```mojo
struct IndexMethods
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

##### `get_1d_index`

###### Overload 1

```mojo
get_1d_index(indices: List[Int], strides: NDArrayStrides) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from a list of indices and NDArrayStrides.

**Args:**

- `indices` (`List`): The list of indices.
- `strides` (`NDArrayStrides`): The strides of the array.

**Returns:**

- `Int`

###### Overload 2

```mojo
get_1d_index(indices: Item, strides: NDArrayStrides) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from an Item and NDArrayStrides.

**Args:**

- `indices` (`Item`): The Item containing indices.
- `strides` (`NDArrayStrides`): The strides of the array.

**Returns:**

- `Int`

###### Overload 3

```mojo
get_1d_index(indices: VariadicList[Int], strides: NDArrayStrides) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from a variadic list of indices and NDArrayStrides.

**Args:**

- `indices` (`VariadicList`): The variadic list of indices.
- `strides` (`NDArrayStrides`): The strides of the array.

**Returns:**

- `Int`

###### Overload 4

```mojo
get_1d_index(indices: List[Int], strides: List[Int]) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from a list of indices and a list of strides.

**Args:**

- `indices` (`List`): The list of indices.
- `strides` (`List`): The list of strides.

**Returns:**

- `Int`

###### Overload 5

```mojo
get_1d_index(indices: VariadicList[Int], strides: VariadicList[Int]) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index from variadic lists of indices and strides.

**Args:**

- `indices` (`VariadicList`): The variadic list of indices.
- `strides` (`VariadicList`): The variadic list of strides.

**Returns:**

- `Int`

###### Overload 6

```mojo
get_1d_index(indices: Tuple[Int, Int], strides: Tuple[Int, Int]) -> Int
```

<span class="badge badge-static">static</span>

Get the flat index for a 2D matrix from tuples of indices and strides.

**Args:**

- `indices` (`Tuple`): The tuple of indices (row, col).
- `strides` (`Tuple`): The tuple of strides.

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `transfer_offset`

```mojo
transfer_offset(offset: Int, strides: NDArrayStrides) -> Int
```

<span class="badge badge-static">static</span>

Transfers the offset by flipping the strides information. Used to transfer between C-contiguous and F-continuous memory layouts.

**Args:**

- `offset` (`Int`): The offset in memory of an element.
- `strides` (`NDArrayStrides`): The strides of the array.

**Returns:**

- `Int`

!!! failure "Raises"


</div>
