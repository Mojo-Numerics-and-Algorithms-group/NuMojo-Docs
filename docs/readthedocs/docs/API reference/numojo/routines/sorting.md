# `numojo.routines.sorting`

Array sorting and indexing operations.

Sorting routines for NDArrays including sort and argsort functions
using multiple backend algorithms (binary sort, bubble sort, quick sort).

Exports
-------
- `sort`: Sort array elements in-place.
- `argsort`: Return indices that would sort array.
- `partition`: Partially sort an array so the k-th element is in its
  sorted position.
- `argpartition`: Return indices that would partition an array.
- `lexsort`: Return indices that would sort an array using several keys.

<div class="prose-label">Notes</div>
    - Multiple sorting methods available: binary sort, bubble sort, quick sort.
    - Quick sort is unstable but efficient.

## Functions


<div class="fn-card" markdown="1">

### `sort`

<div class="overload-divider">Overload 1</div>

```mojo
def sort[dtype: DType](a: NDArray[dtype], stable: Bool = False) -> NDArray[dtype]
```

Sort NDArray using quick sort method. It is not guaranteed to be unstable. When no axis is given, the output array is flattened to 1d.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The input element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `stable` (`Bool`) `[imm]`: If True, the sorting is stable. Default is False.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def sort[dtype: DType](a: NDArray[dtype], axis: Int, stable: Bool = False) -> NDArray[dtype]
```

Sort NDArray along the given axis using quick sort method. It is not guaranteed to be unstable. When no axis is given, the array is flattened before sorting.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The input element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray to sort.
- `axis` (`Int`) `[imm]`: The axis along which the array is sorted.
- `stable` (`Bool`) `[imm]`: If True, the sorting is stable. Default is False.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `sort_inplace`

```mojo
def sort_inplace[dtype: DType](mut a: NDArray[dtype], axis: Int, stable: Bool = False)
```

Sort NDArray in-place along the given axis using quick sort method. It is not guaranteed to be unstable.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The input element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[mut]`: NDArray to sort.
- `axis` (`Int`) `[imm]`: The axis along which the array is sorted.
- `stable` (`Bool`) `[imm]`: If True, the sorting is stable. Default is False.

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `argsort`

<div class="overload-divider">Overload 1</div>

```mojo
def argsort[dtype: DType](a: NDArray[dtype]) -> NDArray[.int]
```

Returns the indices that would sort an array. It is not guaranteed to be unstable. When no axis is given, the array is flattened before sorting.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The input element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.

<div class="prose-label">Returns</div>

- `NDArray[.int]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def argsort[dtype: DType](mut a: NDArray[dtype], axis: Int) -> NDArray[.int]
```

Returns the indices that would sort an array. It is not guaranteed to be unstable. When no axis is given, the array is flattened before sorting.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The input element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[mut]`: NDArray to sort.
- `axis` (`Int`) `[imm]`: The axis along which the array is sorted.

<div class="prose-label">Returns</div>

- `NDArray[.int]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound.


</div>

<div class="fn-card" markdown="1">

### `partition`

```mojo
def partition[dtype: DType, //](a: NDArray[dtype], kth: Int) -> NDArray[dtype]
```

Returns a partially sorted copy of a flattened array such that the element at position `kth` is in the position it would occupy in a fully sorted array; every element before it is less than or equal to it, and every element after it is greater than or equal to it. Regardless of the shape of input, the array is flattened first.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.fromstring[nm.i32]("[3, 1, 4, 1, 5, 9, 2, 6]")
print(nm.partition(a, kth=3))  # 4-th smallest value is at index 3
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The input element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `kth` (`Int`) `[imm]`: The index (into the flattened, sorted array) to partition
    around. Supports negative indices.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `kth` is out of bound.


</div>

<div class="fn-card" markdown="1">

### `argpartition`

```mojo
def argpartition[dtype: DType, //](a: NDArray[dtype], kth: Int) -> NDArray[.int]
```

Returns the indices that would partition a flattened array such that the element at position `kth` of the partitioned array is in the position it would occupy in a fully sorted array. Regardless of the shape of input, the array is flattened first.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.fromstring[nm.i32]("[3, 1, 4, 1, 5, 9, 2, 6]")
print(nm.argpartition(a, kth=3))
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The input element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `kth` (`Int`) `[imm]`: The index (into the flattened, sorted array) to partition
    around. Supports negative indices.

<div class="prose-label">Returns</div>

- `NDArray[.int]`

!!! failure "Raises"
    NumojoError: If `kth` is out of bound.


</div>

<div class="fn-card" markdown="1">

### `lexsort`

```mojo
def lexsort[dtype: DType, //](keys: List[NDArray[dtype]]) -> NDArray[.int]
```

Returns the indices that would lexicographically sort a sequence of key arrays of equal length. The last key is treated as the primary sort key, the second-to-last as the secondary sort key, and so on.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var surnames = nm.fromstring[nm.i32]("[1, 2, 1, 2]")
var ages = nm.fromstring[nm.i32]("[30, 25, 20, 25]")
# Sort by surname, breaking ties by age.
print(nm.lexsort(List(ages, surnames)))
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The input element type.

<div class="prose-label">Args</div>

- `keys` (`List[NDArray[dtype]]`) `[imm]`: A non-empty list of 1-d NDArrays of equal length to sort
    by, ordered from least to most significant.

<div class="prose-label">Returns</div>

- `NDArray[.int]`

!!! failure "Raises"
    NumojoError: If `keys` is empty, or if the key arrays do not all
have the same length.


</div>

<div class="fn-card" markdown="1">

### `binary_sort_1d`

```mojo
def binary_sort_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `binary_sort`

```mojo
def binary_sort[dtype: DType = .float64](array: NDArray[dtype]) -> NDArray[dtype]
```

Binary sorting of NDArray.

<div class="prose-label">Examples</div>
```py
var arr = numojo.core.random.rand[numojo.i16](100)
var sorted_arr = numojo.core.sort.binary_sort(arr)
print(sorted_arr)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `bubble_sort`

```mojo
def bubble_sort[dtype: DType](ndarray: NDArray[dtype]) -> NDArray[dtype]
```

Bubble sort the NDArray. Average complexity: O(n^2) comparisons, O(n^2) swaps. Worst-case complexity: O(n^2) comparisons, O(n^2) swaps. Worst-case space complexity: O(n).

<div class="prose-label">Examples</div>
```py
var arr = numojo.core.random.rand[numojo.i16](100)
var sorted_arr = numojo.core.sort.bubble_sort(arr)
print(sorted_arr)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The input element type.

<div class="prose-label">Args</div>

- `ndarray` (`NDArray[dtype]`) `[imm]`: An NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `quick_sort_1d`

```mojo
def quick_sort_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```

Sort array using quick sort method. Regardless of the shape of input, it is treated as a 1-d array. It is not guaranteed to be unstable.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The input element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An 1-d array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `quick_sort_stable_1d`

```mojo
def quick_sort_stable_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```

Sort array using quick sort method. Regardless of the shape of input, it is treated as a 1-d array. The sorting is stable.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The input element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An 1-d array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `quick_sort_inplace_1d`

```mojo
def quick_sort_inplace_1d[dtype: DType](mut a: NDArray[dtype])
```

Sort array in-place using quick sort method. Regardless of the shape of input, it is treated as a 1-d array. It is not guaranteed to be unstable.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The input element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[mut]`: An 1-d array.

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `quick_sort_stable_inplace_1d`

```mojo
def quick_sort_stable_inplace_1d[dtype: DType](mut a: NDArray[dtype])
```

Sort array in-place using quick sort method. Regardless of the shape of input, it is treated as a 1-d array. The sorting is stable.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The input element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[mut]`: An 1-d array.

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `argsort_quick_sort_1d`

```mojo
def argsort_quick_sort_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[.int]
```

Returns the indices that would sort the buffer of an array. Regardless of the shape of input, it is treated as a 1-d array. It is not guaranteed to be unstable.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The input element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.

<div class="prose-label">Returns</div>

- `NDArray[.int]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
