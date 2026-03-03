# `numojo.routines.sorting`

Sorting routines (numojo.routines.sorting)

This module implements sorting routines for NDArrays and Matrices, including `sort` and `argsort` functions.

SECTIONS OF THIS FILE:
1. `sort` and `argsort` functions exposed to users.
2. Backend multiple sorting methods that can be used in `sort`.
    - Binary sort.
    - Bubble sort.
    - Quick sort (instable).

## Functions


<div class="fn-card" markdown="1">

### `sort`

#### Overload 1

```mojo
sort[dtype: DType](a: NDArray[dtype], stable: Bool = False) -> NDArray[dtype]
```

Sort NDArray using quick sort method. It is not guaranteed to be unstable. When no axis is given, the output array is flattened to 1d.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray`): NDArray.
- `stable` (`Bool`): If True, the sorting is stable. Default is False.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
sort[dtype: DType](a: NDArray[dtype], axis: Int, stable: Bool = False) -> NDArray[dtype]
```

Sort NDArray along the given axis using quick sort method. It is not guaranteed to be unstable. When no axis is given, the array is flattened before sorting.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray`): NDArray to sort.
- `axis` (`Int`): The axis along which the array is sorted.
- `stable` (`Bool`): If True, the sorting is stable. Default is False.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
sort[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```

Sort the Matrix. It is first flattened before sorting.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`

!!! failure "Raises"

#### Overload 4

```mojo
sort[dtype: DType](var A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```

Sort the Matrix along the given axis.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`) `[var]`
- `axis` (`Int`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `sort_inplace`

```mojo
sort_inplace[dtype: DType](mut a: NDArray[dtype], axis: Int, stable: Bool = False)
```

Sort NDArray in-place along the given axis using quick sort method. It is not guaranteed to be unstable.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray`) `[mut]`: NDArray to sort.
- `axis` (`Int`): The axis along which the array is sorted.
- `stable` (`Bool`): If True, the sorting is stable. Default is False.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `argsort`

#### Overload 1

```mojo
argsort[dtype: DType](a: NDArray[dtype]) -> NDArray[DType.int]
```

Returns the indices that would sort an array. It is not guaranteed to be unstable. When no axis is given, the array is flattened before sorting.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray`): NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
argsort[dtype: DType](mut a: NDArray[dtype], axis: Int) -> NDArray[DType.int]
```

Returns the indices that would sort an array. It is not guaranteed to be unstable. When no axis is given, the array is flattened before sorting.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray`) `[mut]`: NDArray to sort.
- `axis` (`Int`): The axis along which the array is sorted.

**Returns:**

- `NDArray`

!!! failure "Raises"
    Error: If the axis is out of bound.

#### Overload 3

```mojo
argsort[dtype: DType](A: Matrix[dtype]) -> Matrix[DType.int]
```

Argsort the Matrix. It is first flattened before sorting.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Matrix`

!!! failure "Raises"

#### Overload 4

```mojo
argsort[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[DType.int]
```

Argsort the Matrix along the given axis.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)
- `axis` (`Int`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `binary_sort_1d`

```mojo
binary_sort_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `a` (`NDArray`)

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `binary_sort`

```mojo
binary_sort[dtype: DType = DType.float64](array: NDArray[dtype]) -> NDArray[dtype]
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

- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `bubble_sort`

```mojo
bubble_sort[dtype: DType](ndarray: NDArray[dtype]) -> NDArray[dtype]
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

- `ndarray` (`NDArray`): An NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `quick_sort_1d`

```mojo
quick_sort_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```

Sort array using quick sort method. Regardless of the shape of input, it is treated as a 1-d array. It is not guaranteed to be unstable.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray`): An 1-d array.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `quick_sort_stable_1d`

```mojo
quick_sort_stable_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```

Sort array using quick sort method. Regardless of the shape of input, it is treated as a 1-d array. The sorting is stable.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray`): An 1-d array.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `quick_sort_inplace_1d`

```mojo
quick_sort_inplace_1d[dtype: DType](mut a: NDArray[dtype])
```

Sort array in-place using quick sort method. Regardless of the shape of input, it is treated as a 1-d array. It is not guaranteed to be unstable.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray`) `[mut]`: An 1-d array.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `quick_sort_stable_inplace_1d`

```mojo
quick_sort_stable_inplace_1d[dtype: DType](mut a: NDArray[dtype])
```

Sort array in-place using quick sort method. Regardless of the shape of input, it is treated as a 1-d array. The sorting is stable.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray`) `[mut]`: An 1-d array.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `argsort_quick_sort_1d`

```mojo
argsort_quick_sort_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[DType.int]
```

Returns the indices that would sort the buffer of an array. Regardless of the shape of input, it is treated as a 1-d array. It is not guaranteed to be unstable.

**Parameters:**

- `dtype` (`DType`): The input element type.

**Args:**

- `a` (`NDArray`): NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>
