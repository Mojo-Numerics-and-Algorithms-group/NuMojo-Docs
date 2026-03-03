# `numojo.core.indexing.traversal`

Traversal (numojo.core.indexing.traversal)

Functions to traverse a multi-dimensional array.
This module provides both recursive and iterative traversal methods,
which can be used for various indexing and slicing operations in NuMojo.

## Structs

### `TraverseMethods`

```mojo
struct TraverseMethods
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

##### `traverse_buffer_according_to_shape_and_strides`

```mojo
traverse_buffer_according_to_shape_and_strides[origin: MutOrigin](mut ptr: UnsafePointer[Scalar[DType.int], origin], shape: NDArrayShape, strides: NDArrayStrides, current_dim: Int = 0, previous_sum: Int = 0)
```

<span class="badge badge-static">static</span>

Store sequence of indices according to shape and strides into the pointer. Auxiliary function for variadic number of dimensions.

UNSAFE: Raw pointer is used!

**Parameters:**

- `origin` (`MutOrigin`): The mutability origin of the pointer.

**Args:**

- `ptr` (`UnsafePointer`) `[mut]`: Pointer to buffer of uninitialized 1-d index array.
- `shape` (`NDArrayShape`): The shape of the array.
- `strides` (`NDArrayStrides`): The strides of the array.
- `current_dim` (`Int`): Temporarily save the current dimension.
- `previous_sum` (`Int`): Temporarily save the previous summed index.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `traverse_iterative`

```mojo
traverse_iterative[dtype: DType](orig: NDArray[dtype], mut narr: NDArray[dtype], ndim: List[Int], coefficients: List[Int], strides: List[Int], offset: Int, mut index: List[Int], depth: Int)
```

<span class="badge badge-static">static</span>

Traverse a multi-dimensional array in an iterative manner.

**Parameters:**

- `dtype` (`DType`): The data type of the NDArray elements.

**Args:**

- `orig` (`NDArray`): The original array.
- `narr` (`NDArray`) `[mut]`: The array to store the result.
- `ndim` (`List`): The number of dimensions of the array.
- `coefficients` (`List`): The coefficients to traverse the sliced part of the original array.
- `strides` (`List`): The strides to traverse the new NDArray `narr`.
- `offset` (`Int`): The offset to the first element of the original NDArray.
- `index` (`List`) `[mut]`: The list of indices.
- `depth` (`Int`): The depth of the indices.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `traverse_iterative_setter`

```mojo
traverse_iterative_setter[dtype: DType](orig: NDArray[dtype], mut narr: NDArray[dtype], ndim: List[Int], coefficients: List[Int], strides: List[Int], offset: Int, mut index: List[Int])
```

<span class="badge badge-static">static</span>

Traverse a multi-dimensional array in an iterative manner for setter.

**Parameters:**

- `dtype` (`DType`): The data type of the NDArray elements.

**Args:**

- `orig` (`NDArray`): The original array (source).
- `narr` (`NDArray`) `[mut]`: The array to store the result (destination).
- `ndim` (`List`): The number of dimensions of the array.
- `coefficients` (`List`): The coefficients to traverse the sliced part of the original array.
- `strides` (`List`): The strides to traverse the new NDArray `narr`.
- `offset` (`Int`): The offset to the first element of the original NDArray.
- `index` (`List`) `[mut]`: The list of indices.

!!! failure "Raises"


</div>
