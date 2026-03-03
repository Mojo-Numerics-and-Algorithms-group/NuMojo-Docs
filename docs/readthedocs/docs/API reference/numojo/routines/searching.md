# `numojo.routines.searching`

"Searching routines (numojo.routines.searching)

This module implements searching routines for finding indices of extrema (argmax and argmin) in NDArrays and Matrices.

## Functions


<div class="fn-card" markdown="1">

### `argmax_1d`

```mojo
argmax_1d[dtype: DType](a: NDArray[dtype]) -> Scalar[DType.int]
```

Returns the index of the maximum value in the buffer. Regardless of the shape of input, it is treated as a 1-d array.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray`): An array.

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `argmin_1d`

```mojo
argmin_1d[dtype: DType](a: NDArray[dtype]) -> Scalar[DType.int]
```

Returns the index of the minimum value in the buffer. Regardless of the shape of input, it is treated as a 1-d array.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray`): An array.

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `argmax`

#### Overload 1

```mojo
argmax[dtype: DType, //](a: NDArray[dtype]) -> Scalar[DType.int]
```

Returns the indices of the maximum values of the array along an axis. When no axis is specified, the array is flattened.

Notes:

If there are multiple occurrences of the maximum values, the indices
of the first occurrence are returned.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray`): An array.

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 2

```mojo
argmax[dtype: DType, //](a: NDArray[dtype], axis: Int) -> NDArray[DType.int]
```

Returns the indices of the maximum values of the array along an axis. When no axis is specified, the array is flattened.

Notes:

If there are multiple occurrences of the maximum values, the indices
of the first occurrence are returned.

Examples:

```mojo
from numojo.prelude import *
from python import Python

fn main() raises:
    var np = Python.import_module("numpy")
    # Test with argmax to get maximum values
    var a = nm.random.randint(5, 4, low=0, high=10)
    var a_np = a.to_numpy()
    print(a)
    print(a_np)
    # Get indices of maximum values along axis=1
    var max_indices = nm.argmax(a, axis=1)
    var max_indices_np = np.argmax(a_np, axis=1)
    # Reshape indices for take_along_axis
    var reshaped_indices = max_indices.reshape(Shape(max_indices.shape[0], 1))
    var reshaped_indices_np = max_indices_np.reshape(max_indices_np.shape[0], 1)
    print(reshaped_indices)
    print(reshaped_indices_np)
    # Get maximum values using take_along_axis
    print(nm.indexing.take_along_axis(a, reshaped_indices, axis=1))
    print(np.take_along_axis(a_np, reshaped_indices_np, axis=1))
```
End of examples.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray`): An array.
- `axis` (`Int`): The axis along which to operate.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
argmax[dtype: DType](A: Matrix[dtype]) -> Scalar[DType.int]
```

Find index of max value in a flattened matrix.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 4

```mojo
argmax[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[DType.int]
```

Find indices of max values along the given axis.

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

### `find_extrema_index`

#### Overload 1

```mojo
find_extrema_index[dtype: DType, find_max: Bool](A: Matrix[dtype]) -> Scalar[DType.int]
```

Find index of min/max value, either in whole matrix or along an axis.

**Parameters:**

- `dtype` (`DType`)
- `find_max` (`Bool`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 2

```mojo
find_extrema_index[dtype: DType, find_max: Bool](A: Matrix[dtype], axis: Optional[Int]) -> Matrix[DType.int]
```

Find index of min/max value, either in whole matrix or along an axis.

**Parameters:**

- `dtype` (`DType`)
- `find_max` (`Bool`)

**Args:**

- `A` (`Matrix`)
- `axis` (`Optional`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `argmin`

#### Overload 1

```mojo
argmin[dtype: DType, //](a: NDArray[dtype]) -> Scalar[DType.int]
```

Returns the indices of the minimum values of the array along an axis. When no axis is specified, the array is flattened.

Notes:

If there are multiple occurrences of the minimum values, the indices
of the first occurrence are returned.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray`): An array.

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 2

```mojo
argmin[dtype: DType, //](a: NDArray[dtype], axis: Int) -> NDArray[DType.int]
```

Returns the indices of the minimum values of the array along an axis. When no axis is specified, the array is flattened.

Notes:

If there are multiple occurrences of the minimum values, the indices
of the first occurrence are returned.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `a` (`NDArray`): An array.
- `axis` (`Int`): The axis along which to operate.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
argmin[dtype: DType](A: Matrix[dtype]) -> Scalar[DType.int]
```

Index of the min. It is first flattened before sorting.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)

**Returns:**

- `Scalar`

!!! failure "Raises"

#### Overload 4

```mojo
argmin[dtype: DType](A: Matrix[dtype], axis: Int) -> Matrix[DType.int]
```

Index of the min along the given axis.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`Matrix`)
- `axis` (`Int`)

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>
