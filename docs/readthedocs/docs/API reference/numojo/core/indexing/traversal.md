# `numojo.core.indexing.traversal`

Functions to traverse a multi-dimensional array.

Provides both recursive and iterative traversal methods, used for various
indexing and slicing operations in NuMojo.

Exports
-------
- `TraverseMethods`: Traversal utilities.

## Structs

### `TraverseMethods`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct TraverseMethods
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Deinitable`, `Movable`

</div>

#### Methods


<div class="fn-card" markdown="1">

#### `traverse_buffer_according_to_shape_and_strides`

```mojo
def traverse_buffer_according_to_shape_and_strides[origin: MutOrigin](mut ptr: Pointer[Int, origin], shape: NDArrayShape, strides: NDArrayStrides, current_dim: Int = Int(0), previous_sum: Int = Int(0))
```

<span class="badge badge-static">static</span>

Store sequence of indices according to shape and strides into the pointer. Auxiliary function for variadic number of dimensions.

UNSAFE: Raw pointer is used!

<div class="prose-label">Parameters</div>

- `origin` (`MutOrigin`): The mutability origin of the pointer.

<div class="prose-label">Args</div>

- `ptr` (`Pointer[Int, origin]`) `[mut]`: Pointer to buffer of uninitialized 1-d index array.
- `shape` (`NDArrayShape`) `[imm]`: The shape of the array.
- `strides` (`NDArrayStrides`) `[imm]`: The strides of the array.
- `current_dim` (`Int`) `[imm]`: Temporarily save the current dimension.
- `previous_sum` (`Int`) `[imm]`: Temporarily save the previous summed index.

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `traverse_iterative`

```mojo
def traverse_iterative[dtype: DType](orig: NDArray[dtype], mut narr: NDArray[dtype], ndim: List[Int], coefficients: List[Int], strides: List[Int], offset: Int, mut index: List[Int], depth: Int)
```

<span class="badge badge-static">static</span>

Traverse a multi-dimensional array in an iterative manner.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `orig` (`NDArray[dtype]`) `[imm]`: The original array.
- `narr` (`NDArray[dtype]`) `[mut]`: The array to store the result.
- `ndim` (`List[Int]`) `[imm]`: The number of dimensions of the array.
- `coefficients` (`List[Int]`) `[imm]`: The coefficients to traverse the sliced part of the original array.
- `strides` (`List[Int]`) `[imm]`: The strides to traverse the new NDArray `narr`.
- `offset` (`Int`) `[imm]`: The offset to the first element of the original NDArray.
- `index` (`List[Int]`) `[mut]`: The list of indices.
- `depth` (`Int`) `[imm]`: The depth of the indices.

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `traverse_iterative_setter`

```mojo
def traverse_iterative_setter[dtype: DType](orig: NDArray[dtype], mut narr: NDArray[dtype], ndim: List[Int], coefficients: List[Int], strides: List[Int], offset: Int, mut index: List[Int])
```

<span class="badge badge-static">static</span>

Traverse a multi-dimensional array in an iterative manner for setter.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `orig` (`NDArray[dtype]`) `[imm]`: The original array (source).
- `narr` (`NDArray[dtype]`) `[mut]`: The array to store the result (destination).
- `ndim` (`List[Int]`) `[imm]`: The number of dimensions of the array.
- `coefficients` (`List[Int]`) `[imm]`: The coefficients to traverse the sliced part of the
    destination array (narr), scaled by narr's strides and step.
- `strides` (`List[Int]`) `[imm]`: The strides to walk through orig (the source value array).
    Since orig is always made contiguous before this call, these
    are C-order strides of orig's shape.
- `offset` (`Int`) `[imm]`: The buffer offset of the first destination element in narr.
- `index` (`List[Int]`) `[mut]`: The list of indices (mutated in place as a counter).

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
