# `numojo.core.indexing.utility`

Utility functions (numojo.core.indexing.utility)

Implements N-DIMENSIONAL ARRAY UTILITY FUNCTIONS

SECTIONS OF THE FILE:
1. NDArray dtype conversions.
2. Numojo.NDArray to other collections.
3. Miscellaneous utility functions.

## Aliases

### `newaxis`

```mojo
comptime newaxis
```

**Value:** `NewAxis()`

## Structs

### `NewAxis`

```mojo
struct NewAxis
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `ImplicitlyDestructible`, `Stringable`

#### Aliases

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `True`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
__init__(out self)
```

<span class="badge badge-static">static</span>

Initializes a NewAxis instance.

**Args:**

- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

```mojo
__eq__(self, other: Self) -> Bool
```

Checks equality between two NewAxis instances.

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

```mojo
__ne__(self, other: Self) -> Bool
```

Checks inequality between two NewAxis instances.

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `__repr__`

```mojo
__repr__(self) -> String
```

Returns a string representation of the NewAxis instance.

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
__str__(self) -> String
```

Returns a string representation of the NewAxis instance.

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>
## Functions


<div class="fn-card" markdown="1">

### `bool_to_numeric`

```mojo
bool_to_numeric[dtype: DType](array: NDArray[DType.bool]) -> NDArray[dtype]
```

Convert a boolean NDArray to a numeric NDArray.

**Parameters:**

- `dtype` (`DType`): The data type of the output NDArray elements.

**Args:**

- `array` (`NDArray`): The boolean NDArray to convert.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `to_numpy`

```mojo
to_numpy[dtype: DType](array: NDArray[dtype]) -> PythonObject
```

Convert a NDArray to a numpy array.

Example:
```console
var arr = NDArray[DType.float32](3, 3, 3)
var np_arr = to_numpy(arr)
var np_arr1 = arr.to_numpy()
```

**Parameters:**

- `dtype` (`DType`): The data type of the NDArray elements.

**Args:**

- `array` (`NDArray`): The NDArray to convert.

**Returns:**

- `PythonObject`

!!! failure "Raises"


</div>
