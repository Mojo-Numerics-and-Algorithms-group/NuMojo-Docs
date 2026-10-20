# `numojo.routines.setops`

Operations on arrays treated as sets of elements.

Exports
-------
- `unique`, `unique_counts`, `unique_index`, `unique_inverse`, `unique_all`:
  Sorted unique elements of an array (optionally along an axis), together
  with counts, first-occurrence indices, and/or reconstruction indices.
- `isin`: Test whether each element of an array is also present in
  another array.

Notes
-----
- Each function has an axis-less overload (flattens the array first) and
  an `axis` overload (treats slices along that axis as elements). NumPy's
  own `unique_all`/`unique_counts`/`unique_inverse`/`unique_values`
  (the Array API-compatible entry points) do not accept `axis`; the axis
  overloads here match the capability of NumPy's classic
  `numpy.unique(ar, axis=..., return_index=..., return_inverse=...,
  return_counts=...)` instead.

## Functions


<div class="fn-card" markdown="1">

### `unique`

<div class="overload-divider">Overload 1</div>

```mojo
def unique[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```

Returns the sorted unique elements of an array.

The input array is flattened before the unique elements are computed.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.fromstring[nm.i32]("[3, 1, 2, 1, 3, 3]")
print(nm.unique(a))  # [1, 2, 3]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def unique[dtype: DType](A: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

(overload) Returns the sorted unique slices of an array along `axis`.

Each slice obtained by indexing `A` along `axis` is treated as a
single element; two slices are equal if all their values match.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.fromstring[nm.i32]("[[1,2][3,4][1,2]]")
print(nm.unique(a, axis=0))  # [[1, 2], [3, 4]]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `axis` (`Int`) `[imm]`: The axis whose slices are compared. Supports negative
    indices.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `axis` is out of bound.


</div>

<div class="fn-card" markdown="1">

### `unique_counts`

<div class="overload-divider">Overload 1</div>

```mojo
def unique_counts[dtype: DType](A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[.int]]
```

Returns the sorted unique elements of an array together with the number of times each unique value occurs.

The input array is flattened before the unique elements are computed.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.fromstring[nm.i32]("[3, 1, 2, 1, 3, 3]")
var result = nm.unique_counts(a)
print(result[0])  # [1, 2, 3]
print(result[1])  # [2, 1, 3]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[dtype], NDArray[.int]]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def unique_counts[dtype: DType](A: NDArray[dtype], axis: Int) -> Tuple[NDArray[dtype], NDArray[.int]]
```

(overload) Returns the sorted unique slices of an array along `axis` together with the number of times each one occurs.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.fromstring[nm.i32]("[[1,2][3,4][1,2]]")
var result = nm.unique_counts(a, axis=0)
print(result[0])  # [[1, 2], [3, 4]]
print(result[1])  # [2, 1]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `axis` (`Int`) `[imm]`: The axis whose slices are compared. Supports negative
    indices.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[dtype], NDArray[.int]]`

!!! failure "Raises"
    NumojoError: If `axis` is out of bound.


</div>

<div class="fn-card" markdown="1">

### `unique_index`

<div class="overload-divider">Overload 1</div>

```mojo
def unique_index[dtype: DType](A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[.int]]
```

Returns the sorted unique elements of a flattened array together with the index of the first occurrence of each one.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.fromstring[nm.i32]("[3, 1, 2, 1, 3, 3]")
var result = nm.unique_index(a)
print(result[0])  # [1, 2, 3]
print(result[1])  # [1, 2, 0]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[dtype], NDArray[.int]]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def unique_index[dtype: DType](A: NDArray[dtype], axis: Int) -> Tuple[NDArray[dtype], NDArray[.int]]
```

(overload) Returns the sorted unique slices of an array along `axis` together with the index of the first occurrence of each one.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.fromstring[nm.i32]("[[1,2][3,4][1,2]]")
var result = nm.unique_index(a, axis=0)
print(result[0])  # [[1, 2], [3, 4]]
print(result[1])  # [0, 1]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `axis` (`Int`) `[imm]`: The axis whose slices are compared. Supports negative
    indices.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[dtype], NDArray[.int]]`

!!! failure "Raises"
    NumojoError: If `axis` is out of bound.


</div>

<div class="fn-card" markdown="1">

### `unique_inverse`

<div class="overload-divider">Overload 1</div>

```mojo
def unique_inverse[dtype: DType](A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[.int]]
```

Returns the sorted unique elements of a flattened array together with the indices that reconstruct it from those unique elements.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.fromstring[nm.i32]("[3, 1, 2, 1, 3, 3]")
var result = nm.unique_inverse(a)
print(result[0])  # [1, 2, 3]
print(result[1])  # [2, 0, 1, 0, 2, 2]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[dtype], NDArray[.int]]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def unique_inverse[dtype: DType](A: NDArray[dtype], axis: Int) -> Tuple[NDArray[dtype], NDArray[.int]]
```

(overload) Returns the sorted unique slices of an array along `axis` together with the indices that reconstruct it from those slices.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.fromstring[nm.i32]("[[1,2][3,4][1,2]]")
var result = nm.unique_inverse(a, axis=0)
print(result[0])  # [[1, 2], [3, 4]]
print(result[1])  # [0, 1, 0]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `axis` (`Int`) `[imm]`: The axis whose slices are compared. Supports negative
    indices.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[dtype], NDArray[.int]]`

!!! failure "Raises"
    NumojoError: If `axis` is out of bound.


</div>

<div class="fn-card" markdown="1">

### `unique_all`

<div class="overload-divider">Overload 1</div>

```mojo
def unique_all[dtype: DType](A: NDArray[dtype]) -> Tuple[NDArray[dtype], NDArray[.int], NDArray[.int], NDArray[.int]]
```

Returns the sorted unique elements of a flattened array together with first-occurrence indices, inverse indices, and counts, all in one call.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.fromstring[nm.i32]("[3, 1, 2, 1, 3, 3]")
var result = nm.unique_all(a)
print(result[0])  # values:  [1, 2, 3]
print(result[1])  # index:   [1, 2, 0]
print(result[2])  # inverse: [2, 0, 1, 0, 2, 2]
print(result[3])  # counts:  [2, 1, 3]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[dtype], NDArray[.int], NDArray[.int], NDArray[.int]]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def unique_all[dtype: DType](A: NDArray[dtype], axis: Int) -> Tuple[NDArray[dtype], NDArray[.int], NDArray[.int], NDArray[.int]]
```

(overload) Returns the sorted unique slices of an array along `axis` together with first-occurrence indices, inverse indices, and counts, all in one call.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.fromstring[nm.i32]("[[1,2][3,4][1,2]]")
var result = nm.unique_all(a, axis=0)
print(result[0])  # values:  [[1, 2], [3, 4]]
print(result[1])  # index:   [0, 1]
print(result[2])  # inverse: [0, 1, 0]
print(result[3])  # counts:  [2, 1]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `axis` (`Int`) `[imm]`: The axis whose slices are compared. Supports negative
    indices.

<div class="prose-label">Returns</div>

- `Tuple[NDArray[dtype], NDArray[.int], NDArray[.int], NDArray[.int]]`

!!! failure "Raises"
    NumojoError: If `axis` is out of bound.


</div>

<div class="fn-card" markdown="1">

### `isin`

```mojo
def isin[dtype: DType, //](element: NDArray[dtype], test_elements: NDArray[dtype], invert: Bool = False) -> NDArray[.bool]
```

Tests whether each element of `element` is also present in `test_elements`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.fromstring[nm.i32]("[1, 2, 3, 4, 5]")
var b = nm.fromstring[nm.i32]("[2, 4]")
print(nm.isin(a, b))  # [False, True, False, True, False]
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): DType.

<div class="prose-label">Args</div>

- `element` (`NDArray[dtype]`) `[imm]`: An NDArray whose elements are tested for membership.
- `test_elements` (`NDArray[dtype]`) `[imm]`: The values against which each element of
    `element` is tested.
- `invert` (`Bool`) `[imm]`: If True, the returned array is inverted (True where the
    value is *not* in `test_elements`). Default is False.

<div class="prose-label">Returns</div>

- `NDArray[.bool]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
