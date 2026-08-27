# `numojo.core.indexing.utility`

N-dimensional array utility functions: dtype conversions, conversion to other collections, and miscellaneous indexing helpers.

Exports
-------
- `bool_to_numeric`: Convert a boolean NDArray to a numeric NDArray.
- `to_numpy`: Convert an NDArray to a NumPy array.

## Functions


<div class="fn-card" markdown="1">

### `bool_to_numeric`

```mojo
def bool_to_numeric[dtype: DType](array: NDArray[DType.bool]) -> NDArray[dtype]
```

Convert a boolean NDArray to a numeric NDArray.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the output NDArray elements.

<div class="prose-label">Args</div>

- `array` (`NDArray[DType.bool]`) `[imm]`: The boolean NDArray to convert.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `to_numpy`

```mojo
def to_numpy[dtype: DType](array: NDArray[dtype]) -> PythonObject
```

Convert a NDArray to a numpy array.

<div class="prose-label">Examples</div>
```console
var arr = NDArray[DType.float32](3, 3, 3)
var np_arr = to_numpy(arr)
var np_arr1 = arr.to_numpy()
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The NDArray to convert.

<div class="prose-label">Returns</div>

- `PythonObject`

!!! failure "Raises"


</div>
