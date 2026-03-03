# `numojo.routines.indexing`

Indexing routines (numojo.routines.indexing)

- Generating index arrays
- Indexing-like operations
- Inserting data into arrays
- Iterating over arrays

## Functions


<div class="fn-card" markdown="1">

### `where`

#### Overload 1

```mojo
where[dtype: DType](mut x: NDArray[dtype], scalar: Scalar[dtype], mask: NDArray[DType.bool])
```

Replaces elements in `x` with `scalar` where `mask` is True.

**Parameters:**

- `dtype` (`DType`): DType.

**Args:**

- `x` (`NDArray`) `[mut]`: A NDArray.
- `scalar` (`Scalar`): A SIMD value.
- `mask` (`NDArray`): A NDArray.

!!! failure "Raises"

#### Overload 2

```mojo
where[dtype: DType](mut x: NDArray[dtype], y: NDArray[dtype], mask: NDArray[DType.bool])
```

Replaces elements in `x` with elements from `y` where `mask` is True.

**Parameters:**

- `dtype` (`DType`): DType.

**Args:**

- `x` (`NDArray`) `[mut]`: NDArray[dtype].
- `y` (`NDArray`): NDArray[dtype].
- `mask` (`NDArray`): NDArray[DType.bool].

!!! failure "Raises"
    ShapeMismatchError: If the shapes of `x` and `y` do not match.


</div>

<div class="fn-card" markdown="1">

### `compress`

#### Overload 1

```mojo
compress[dtype: DType](condition: NDArray[DType.bool], a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Return selected slices of an array along given axis. If no axis is provided, the array is flattened before use.

**Parameters:**

- `dtype` (`DType`): DType.

**Args:**

- `condition` (`NDArray`): 1-D array of booleans that selects which entries to return.
    If length of condition is less than the size of the array along the
    given axis, then output is filled to the length of the condition
    with False.
- `a` (`NDArray`): The array.
- `axis` (`Int`): The axis along which to take slices.

**Returns:**

- `NDArray`

!!! failure "Raises"
    Error: If the axis is out of bound for the given array.
Error: If the condition is not 1-D array.
Error: If the condition length is out of bound for the given axis.
Error: If the condition contains no True values.

#### Overload 2

```mojo
compress[dtype: DType](condition: NDArray[DType.bool], a: NDArray[dtype]) -> NDArray[dtype]
```

Return selected slices of an array along given axis. If no axis is provided, the array is flattened before use. This is a function ***OVERLOAD***.

**Parameters:**

- `dtype` (`DType`): DType.

**Args:**

- `condition` (`NDArray`): 1-D array of booleans that selects which entries to return.
    If length of condition is less than the size of the array along the
    given axis, then output is filled to the length of the condition
    with False.
- `a` (`NDArray`): The array.

**Returns:**

- `NDArray`

!!! failure "Raises"
    Error: If the condition is not 1-D array.
Error: If the condition length is out of bound for the given axis.
Error: If the condition contains no True values.


</div>

<div class="fn-card" markdown="1">

### `take_along_axis`

```mojo
take_along_axis[dtype: DType, //](arr: NDArray[dtype], indices: NDArray[DType.int], axis: Int = 0) -> NDArray[dtype]
```

Takes values from the input array along the given axis based on indices.

Examples:

```console
> var a = nm.arange[i8](12).reshape(Shape(3, 4))
> print(a)
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
> ind = nm.array[intp]("[[0, 1, 2, 0], [1, 0, 2, 1]]")
> print(ind)
[[0 1 2 0]
 [1 0 2 1]]
> print(nm.indexing.take_along_axis(a, ind, axis=0))
[[ 0  5 10  3]
 [ 4  1 10  7]]
```
.

**Parameters:**

- `dtype` (`DType`): DType of the input array.

**Args:**

- `arr` (`NDArray`): The source array.
- `indices` (`NDArray`): The indices array.
- `axis` (`Int`): The axis along which to take values. Default is 0.

**Returns:**

- `NDArray`

!!! failure "Raises"
    Error: If the axis is out of bounds for the given array.
Error: If the ndim of arr and indices are not the same.
Error: If the shape of indices does not match the shape of the
input array except along the given axis.


</div>
