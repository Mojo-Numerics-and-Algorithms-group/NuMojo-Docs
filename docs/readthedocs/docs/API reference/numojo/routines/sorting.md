# `numojo.routines.sorting`

Array sorting and indexing operations.

Sorting routines for NDArrays including sort and argsort functions
using multiple backend algorithms (binary sort, bubble sort, quick sort).

Exports
-------
- `sort`: Sort array elements in-place.
- `argsort`: Return indices that would sort array.

Notes:
    - Multiple sorting methods available: binary sort, bubble sort, quick sort.
    - Quick sort is unstable but efficient.

## Functions


<div class="fn-card" markdown="1">

### `sort`

#### Overload 1

```mojo
def sort[dtype: DType](a: NDArray[dtype], stable: Bool = False) -> NDArray[dtype]
```

Sort NDArray using quick sort method. It is not guaranteed to be unstable. When no axis is given, the output array is flattened to 1d.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.
- `stable` (`Bool`) `[imm]`: If True, the sorting is stable. Default is False.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def sort[dtype: DType](a: NDArray[dtype], axis: Int, stable: Bool = False) -> NDArray[dtype]
```

Sort NDArray along the given axis using quick sort method. It is not guaranteed to be unstable. When no axis is given, the array is flattened before sorting.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: NDArray to sort.
- `axis` (`Int`) `[imm]`: The axis along which the array is sorted.
- `stable` (`Bool`) `[imm]`: If True, the sorting is stable. Default is False.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `sort_inplace`

```mojo
def sort_inplace[dtype: DType](mut a: NDArray[dtype], axis: Int, stable: Bool = False)
```

Sort NDArray in-place along the given axis using quick sort method. It is not guaranteed to be unstable.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray[dtype]`) `[mut]`: NDArray to sort.
- `axis` (`Int`) `[imm]`: The axis along which the array is sorted.
- `stable` (`Bool`) `[imm]`: If True, the sorting is stable. Default is False.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `argsort`

#### Overload 1

```mojo
def argsort[dtype: DType](a: NDArray[dtype]) -> NDArray[DType.int]
```

Returns the indices that would sort an array. It is not guaranteed to be unstable. When no axis is given, the array is flattened before sorting.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.

**Returns:**

- `NDArray[DType.int]`

!!! failure "Raises"

#### Overload 2

```mojo
def argsort[dtype: DType](mut a: NDArray[dtype], axis: Int) -> NDArray[DType.int]
```

Returns the indices that would sort an array. It is not guaranteed to be unstable. When no axis is given, the array is flattened before sorting.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray[dtype]`) `[mut]`: NDArray to sort.
- `axis` (`Int`) `[imm]`: The axis along which the array is sorted.

**Returns:**

- `NDArray[DType.int]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound.


</div>

<div class="fn-card" markdown="1">

### `binary_sort_1d`

```mojo
def binary_sort_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `binary_sort`

```mojo
def binary_sort[dtype: DType = DType.float64](array: NDArray[dtype]) -> NDArray[dtype]
```

Binary sorting of NDArray.

Example:
```py
var arr = numojo.core.random.rand[numojo.i16](100)
var sorted_arr = numojo.core.sort.binary_sort(arr)
print(sorted_arr)
```

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `bubble_sort`

```mojo
def bubble_sort[dtype: DType](ndarray: NDArray[dtype]) -> NDArray[dtype]
```

Bubble sort the NDArray. Average complexity: O(n^2) comparisons, O(n^2) swaps. Worst-case complexity: O(n^2) comparisons, O(n^2) swaps. Worst-case space complexity: O(n).

Example:
```py
var arr = numojo.core.random.rand[numojo.i16](100)
var sorted_arr = numojo.core.sort.bubble_sort(arr)
print(sorted_arr)
```

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `ndarray` (`NDArray[dtype]`) `[imm]`: An NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `quick_sort_1d`

```mojo
def quick_sort_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```

Sort array using quick sort method. Regardless of the shape of input, it is treated as a 1-d array. It is not guaranteed to be unstable.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: An 1-d array.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `quick_sort_stable_1d`

```mojo
def quick_sort_stable_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```

Sort array using quick sort method. Regardless of the shape of input, it is treated as a 1-d array. The sorting is stable.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: An 1-d array.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `quick_sort_inplace_1d`

```mojo
def quick_sort_inplace_1d[dtype: DType](mut a: NDArray[dtype])
```

Sort array in-place using quick sort method. Regardless of the shape of input, it is treated as a 1-d array. It is not guaranteed to be unstable.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray[dtype]`) `[mut]`: An 1-d array.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `quick_sort_stable_inplace_1d`

```mojo
def quick_sort_stable_inplace_1d[dtype: DType](mut a: NDArray[dtype])
```

Sort array in-place using quick sort method. Regardless of the shape of input, it is treated as a 1-d array. The sorting is stable.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray[dtype]`) `[mut]`: An 1-d array.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `argsort_quick_sort_1d`

```mojo
def argsort_quick_sort_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[DType.int]
```

Returns the indices that would sort the buffer of an array. Regardless of the shape of input, it is treated as a 1-d array. It is not guaranteed to be unstable.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: NDArray.

**Returns:**

- `NDArray[DType.int]`

!!! failure "Raises"


</div>
