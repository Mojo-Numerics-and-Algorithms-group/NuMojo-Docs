# `numojo.routines.searching`

Search operations for finding array extrema indices.

Functions for finding indices of maximum and minimum values in arrays.

Exports
-------
- `argmax`: Index of maximum value.
- `argmin`: Index of minimum value.

## Functions


<div class="fn-card" markdown="1">

### `argmax_1d`

```mojo
def argmax_1d[dtype: DType](a: NDArray[dtype]) -> Int
```

Returns the index of the maximum value in the buffer. Regardless of the shape of input, it is treated as a 1-d array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.

<div class="prose-label">Returns</div>

- `Int`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `argmin_1d`

```mojo
def argmin_1d[dtype: DType](a: NDArray[dtype]) -> Int
```

Returns the index of the minimum value in the buffer. Regardless of the shape of input, it is treated as a 1-d array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.

<div class="prose-label">Returns</div>

- `Int`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `argmax`

<div class="overload-divider">Overload 1</div>

```mojo
def argmax[dtype: DType, //](a: NDArray[dtype]) -> Int
```

Returns the indices of the maximum values of the array along an axis. When no axis is specified, the array is flattened.

<div class="prose-label">Notes</div>

If there are multiple occurrences of the maximum values, the indices
of the first occurrence are returned.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.

<div class="prose-label">Returns</div>

- `Int`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def argmax[dtype: DType, //](a: NDArray[dtype], axis: Int) -> NDArray[DType.int]
```

Returns the indices of the maximum values of the array along an axis. When no axis is specified, the array is flattened.

<div class="prose-label">Notes</div>

If there are multiple occurrences of the maximum values, the indices
of the first occurrence are returned.

<div class="prose-label">Examples</div>

```mojo
from numojo.prelude import *
from python import Python

def main() raises:
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

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.
- `axis` (`Int`) `[imm]`: The axis along which to operate.

<div class="prose-label">Returns</div>

- `NDArray[DType.int]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `argmin`

<div class="overload-divider">Overload 1</div>

```mojo
def argmin[dtype: DType, //](a: NDArray[dtype]) -> Int
```

Returns the indices of the minimum values of the array along an axis. When no axis is specified, the array is flattened.

<div class="prose-label">Notes</div>

If there are multiple occurrences of the minimum values, the indices
of the first occurrence are returned.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.

<div class="prose-label">Returns</div>

- `Int`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def argmin[dtype: DType, //](a: NDArray[dtype], axis: Int) -> NDArray[DType.int]
```

Returns the indices of the minimum values of the array along an axis. When no axis is specified, the array is flattened.

<div class="prose-label">Notes</div>

If there are multiple occurrences of the minimum values, the indices
of the first occurrence are returned.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `a` (`NDArray[dtype]`) `[imm]`: An array.
- `axis` (`Int`) `[imm]`: The axis along which to operate.

<div class="prose-label">Returns</div>

- `NDArray[DType.int]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
