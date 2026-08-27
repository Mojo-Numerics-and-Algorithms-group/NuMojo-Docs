# `numojo.core.ndarray`

Multi-dimensional array implementation for NuMojo.

Core data structure for N-dimensional arrays with efficient storage, indexing,
slicing, and operations. Supports various memory layouts and data types.

Exports
-------
- `NDArray`: Multi-dimensional array type.
- `_NDArrayIter`: Iterator for NDArray traversal.
- `_NDAxisIter`: Iterator along specific axis.
- `_NDIter`: Generic NDArray iterator.

## Aliases

### `IndexTypes`

```mojo
comptime IndexTypes
```

**Value:** `Variant[Int, NewAxis, EllipsisType, Slice]`

IndexTypes is used to represent the different kinds of indices that can be used for indexing and slicing operations on the NDArray.

## Structs

### `NDArray`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct NDArray[dtype: DType = DType.float64]
```

**Memory convention:** `memory_only`  
**Implements:** `Absable`, `AnyType`, `Copyable`, `Deinitable`, `FloatableRaising`, `IntableRaising`, `Movable`, `Sized`, `Writable`

The N-dimensional array (NDArray).

The array can be uniquely defined by the following:
    1. The data buffer of all items.
    2. The shape of the array.
    3. The strides (Length of item to travel to next dimension).
    4. The datatype of the elements.

The following attributes are also helpful:
    - The number of dimensions
    - Size of the array (number of items)
    - The order of the array: Row vs Columns major

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): Type of item in NDArray. Default type is DType.float64.

</div>

#### Fields

- **`ndim`** (`Int`): Number of Dimensions.
- **`shape`** (`NDArrayShape`): Size and shape of NDArray.
- **`size`** (`Int`): Size of NDArray.
- **`strides`** (`NDArrayStrides`): Contains offset, strides.
- **`offset`** (`Int`): Offset of the first element in the data buffer.
- **`flags`** (`Flags`): Information about the memory layout of the array.
- **`print_options`** (`PrintOptions`): Per-instance print options (formerly global).

#### Aliases

#### `origin`

```mojo
comptime origin
```

**Value:** `MutUntrackedOrigin`

Origin of the data buffer.

#### `width`

```mojo
comptime width
```

**Value:** `simd_width_of[dtype]()`

Vector size of the data type.

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

<div class="overload-divider">Overload 1</div>

```mojo
def __init__(out self, shape: NDArrayShape, order: String = "C")
```

<span class="badge badge-static">static</span>

Initializes an NDArray with the given shape.

The memory is not filled with values.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.NDArray[nm.f32](
    nm.Shape(2, 3), order="C"
)
```

<div class="prose-label">Notes</div>
This constructor should not be used by users directly. Use factory
functions in `numojo.routines.creation` module instead.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the array.
- `order` (`String`) `[imm]`: Memory order "C" or "F".
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __init__(out self, shape: List[Int], strides: List[Int], offset: Int)
```

<span class="badge badge-static">static</span>

Initializes an NDArray with a specific shape, offset, and strides.

<div class="prose-label">Notes</div>
- This constructor is intended for advanced use cases requiring
  precise control over memory layout.
- The resulting array is uninitialized and should be filled before
  use.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
var shape = [2, 3]
var offset = 0
var strides = [3, 1]
var arr = NDArray[f32](
    shape, strides, offset
)
```

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`: A list of integers specifying the shape of the array.
- `strides` (`List[Int]`) `[imm]`: A list of integers specifying the stride for each
    dimension.
- `offset` (`Int`) `[imm]`: The integer offset into the underlying buffer.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 3</div>

```mojo
def __init__(out self, shape: NDArrayShape, strides: NDArrayStrides, ndim: Int, size: Int, offset: Int, flags: Flags)
```

<span class="badge badge-static">static</span>

Initializes an NDArray with explicit shape, strides, number of dimensions, size, offset, and flags.

Creates an uninitialized NDArray with the provided properties. No
compatibility checks are performed between shape, strides, ndim, size,
offset, or flags. This allows construction of arrays with arbitrary
metadata, including 0-D arrays (scalars).

<div class="prose-label">Notes</div>
- This constructor is intended for advanced or internal use cases
  requiring manual control.
- The resulting array is uninitialized; values must be set before
  use.
- No validation is performed on the consistency of the provided
  arguments.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the array.
- `strides` (`NDArrayStrides`) `[imm]`: The strides for each dimension.
- `ndim` (`Int`) `[imm]`: The number of dimensions.
- `size` (`Int`) `[imm]`: The total number of elements.
- `offset` (`Int`) `[imm]`: The offset of the first element in the data buffer.
- `flags` (`Flags`) `[imm]`: The memory layout flags.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 4</div>

```mojo
def __init__(out self, var data: DataContainer[dtype], is_view: Bool, shape: NDArrayShape, strides: NDArrayStrides, offset: Int)
```

<span class="badge badge-static">static</span>

Initializes an NDArray as either an owning array or a non-owning view based on the provided DataContainer and the `is_view` flag.

<div class="prose-label">Notes</div>
Ownership is determined by `is_view` and the DataContainer's reference count:
- If `is_view` is True and ref count is 1, the created NDArray will be a view and does not own the data.
- If `is_view` is False and ref count is 1, the NDArray owns the data. This is used to create deep copy of arrays.

<div class="prose-label">Args</div>

- `data` (`DataContainer[dtype]`) `[var]`: Reference-counted DataContainer holding array data.
- `is_view` (`Bool`) `[imm]`: If True, creates a non-owning view; if False, owns the data i.e equivalent to deep copy.
- `shape` (`NDArrayShape`) `[imm]`: Shape of the view.
- `strides` (`NDArrayStrides`) `[imm]`: Strides for the view.
- `offset` (`Int`) `[imm]`: Offset of the first element in the data buffer.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 5</div>

```mojo
def __init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

Copies `copy` into `self`.

Performs a deep copy. The new array owns its data.

<div class="prose-label">Args</div>

- `copy` (`Self`) `[imm]`: The NDArray to copy from.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 6</div>

```mojo
def __init__(out self, *, deinit move: Self)
```

<span class="badge badge-static">static</span>

Moves `move` into `self`.

<div class="prose-label">Args</div>

- `move` (`Self`) `[deinit]`: The NDArray to move from.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__deinit__`

```mojo
def __deinit__(deinit self)
```

Destroys all elements and frees memory.

<div class="prose-label">Args</div>

- `self` (`Self`) `[deinit]`


</div>

<div class="fn-card" markdown="1">

#### `__bool__`

```mojo
def __bool__(self) -> Bool
```

Returns `True` if all elements are truthy.

<div class="prose-label">Examples</div>

```console
>>> import numojo
>>> var A = numojo.random.rand[numojo.i16](2, 2, 2)
>>> print(bool(A))
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`

!!! failure "Raises"
    NumojoError: If the array is not 0-D or length-1.


</div>

<div class="fn-card" markdown="1">

#### `__getitem__`

<div class="overload-divider">Overload 1</div>

```mojo
def __getitem__(self) -> Scalar[dtype]
```

Gets the value of the 0-D array.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange(3)[0]
print(a[])  # gets value of the 0-D array.
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If the array is not 0-D.

<div class="overload-divider">Overload 2</div>

```mojo
def __getitem__(self, index: Item) -> Scalar[dtype]
```

Gets the value at the index list.

<div class="prose-label">Examples</div>

```console
>>>import numojo
>>>var a = numojo.arange(0, 10, 1).reshape(
...    numojo.Shape(2, 5)
...)
>>>print(a[Item(1, 2)])
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `index` (`Item`) `[imm]`: The index list.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If the length of `index` does not match the number of
dimensions.
NumojoError: If any of the index elements exceeds the size of the
dimension of the array.

<div class="overload-divider">Overload 3</div>

```mojo
def __getitem__(self, idx: Int) -> Self
```

Gets a single first-axis slice (first dimension).

Returns a slice of the array taken at the first (axis 0) position
specified by `idx`. The resulting array's dimensionality is reduced by
exactly one. If the source is 1-D, the result is a 0-D array (numojo
scalar wrapper). Negative indices are supported and are normalized
relative to the first dimension.

<div class="prose-label">Notes</div>
Order preservation: The resulting copy preserves the source array's
memory order (C or F). Performance fast path: For C-contiguous
arrays the slice is a single contiguous block and is copied with one
`memcpy`. For F-contiguous or arbitrary strided layouts a unified
stride-based element loop is used. (Future enhancement: return a
non-owning view instead of copying.)

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *

var a = nm.arange(0, 12, 1).reshape(Shape(3, 4))
print(a.shape)        # (3,4)
print(a[1].shape)     # (4,)  -- 1-D slice
print(a[-1].shape)    # (4,)  -- negative index

var b = nm.arange(6).reshape(nm.Shape(6))
print(b[2])           # 0-D array (scalar wrapper)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: The integer index along the first dimension. Accepts negative
    indices in the range `[-shape[0], shape[0])`.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the array is 0-D (cannot slice a scalar).
NumojoError: If `idx` is out of bounds after normalization.

<div class="overload-divider">Overload 4</div>

```mojo
def __getitem__(self, var *slices: Slice) -> Self
```

Retrieves a slice or sub-array from the current array using variadic slice arguments.

Delegates to `__getitem__(*slices: IndexTypes)` after wrapping each
`Slice` into the `IndexTypes` variant. This ensures a single canonical
parsing and dispatch path.

<div class="prose-label">Notes</div>
- Negative indices and step sizes are supported.
- Missing trailing dimensions are implicitly treated as full slices.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f32](10).reshape(nm.Shape(2, 5))
var b = a[:, 2:4]
print(b)  # 2x2 sliced array
```

!!! info "Constraints"
    - The number of slices provided must not exceed the number of array
dimensions.
- Each slice must be valid for its corresponding dimension.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `*slices` (`Slice`) `[var]`: A variadic list of `Slice` objects, one for each dimension
    to be sliced.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If any slice is out of bounds for its corresponding
dimension.
NumojoError: If the number of slices is greater than `ndim`.

<div class="overload-divider">Overload 5</div>

```mojo
def __getitem__(self, *slices: Variant[Int, NewAxis, EllipsisType, Slice]) -> Self
```

Gets items of an NDArray with a series of either slices or integers.

<div class="prose-label">Notes</div>
A decrease of dimensions may or may not happen when `__getitem__` is
called on an ndarray. An ndarray of X-D array can become Y-D array
after `__getitem__` where `Y <= X`.

Whether the dimension decreases or not depends on:
1. What types of arguments are passed into `__getitem__`.
2. The number of arguments that are passed in `__getitem__`.

PRINCIPAL: The number of dimensions to be decreased is determined by
the number of `Int` passed in `__getitem__`.

For example, `A` is a 10x10x10 ndarray (3-D). Then,

- `A[1, 2, 3]` leads to a 0-D array (scalar), since there are 3
  integers.
- `A[1, 2]` leads to a 1-D array (vector), since there are 2
  integers,
so the dimension decreases by 2.
- `A[1]` leads to a 2-D array (matrix), since there is 1 integer, so
  the
dimension decreases by 1.

The number of dimensions will not decrease when Slice is passed in
`__getitem__` or no argument is passed in for a certain dimension
(it is an implicit slide and a slide of all items will be used).

Take the same example `A` with 10x10x10 in shape. Then,

- `A[1:4, 2:5, 3:6]`, leads to a 3-D array (no decrease in
  dimension),
since there are 3 slices.
- `A[2:8]`, leads to a 3-D array (no decrease in dimension), since
there are 1 explicit slice and 2 implicit slices.

When there is a mixture of int and slices passed into `__getitem__`,
the number of integers will be the number of dimensions to be
decreased. Example,

- `A[1:4, 2, 2]`, leads to a 1-D array (vector), since there are 2
integers, so the dimension decreases by 2.

Note that, even though a slice contains one row, it does not reduce
the dimensions. Example,

- `A[1:2, 2:3, 3:4]`, leads to a 3-D array (no decrease in
dimension), since there are 3 slices.

Note that, when the number of integers equals to the number of
dimensions, the final outcome is an 0-D array instead of a number.
The user has to unpack the 0-D array with the method `A.item(0)` to
get the corresponding number.

More examples for 1-D, 2-D, and 3-D arrays.

<div class="prose-label">Examples</div>

```console
A is a matrix
[[      -128    -95     65      -11     ]
 [      8       -72     -116    45      ]
 [      45      111     -30     4       ]
 [      84      -120    -115    7       ]]
2-D array  Shape: [4, 4]  DType: int8

A[0]
[       -128    -95     65      -11     ]
1-D array  Shape: [4]  DType: int8

A[0, 1]
-95
0-D array  Shape: [0]  DType: int8

A[Slice(1,3)]
[[      8       -72     -116    45      ]
 [      45      111     -30     4       ]]
2-D array  Shape: [2, 4]  DType: int8

A[1, Slice(2,4)]
[       -116    45      ]
1-D array  Shape: [2]  DType: int8

A[Slice(1,3), Slice(1,3)]
[[      -72     -116    ]
 [      111     -30     ]]
2-D array  Shape: [2, 2]  DType: int8

A.item(0,1) as Scalar
-95

==============================
A is a vector
[       43      -127    -30     -111    ]
1-D array  Shape: [4]  DType: int8

A[0]
43
0-D array  Shape: [0]  DType: int8

A[Slice(1,3)]
[       -127    -30     ]
1-D array  Shape: [2]  DType: int8

A.item(0) as Scalar
43

==============================
A is a 3darray
[[[     -22     47      22      110     ]
  [     88      6       -105    39      ]
  [     -22     51      105     67      ]
  [     -61     -116    60      -44     ]]
 [[     33      65      125     -35     ]
  [     -65     123     57      64      ]
  [     38      -110    33      98      ]
  [     -59     -17     68      -6      ]]
 [[     -68     -58     -37     -86     ]
  [     -4      101     104     -113    ]
  [     103     1       4       -47     ]
  [     124     -2      -60     -105    ]]
[[     114     -110    0       -30     ]
  [     -58     105     7       -10     ]
  [     112     -116    66      69      ]
  [     83      -96     -124    48      ]]]
3-D array  Shape: [4, 4, 4]  DType: int8

A[0]
[[      -22     47      22      110     ]
 [      88      6       -105    39      ]
 [      -22     51      105     67      ]
 [      -61     -116    60      -44     ]]
2-D array  Shape: [4, 4]  DType: int8

A[0, 1]
[       88      6       -105    39      ]
1-D array  Shape: [4]  DType: int8

A[0, 1, 2]
-105
0-D array  Shape: [0]  DType: int8

A[Slice(1,3)]
[[[     33      65      125     -35     ]
  [     -65     123     57      64      ]
  [     38      -110    33      98      ]
  [     -59     -17     68      -6      ]]
 [[     -68     -58     -37     -86     ]
  [     -4      101     104     -113    ]
  [     103     1       4       -47     ]
  [     124     -2      -60     -105    ]]]
3-D array  Shape: [2, 4, 4]  DType: int8

A[1, Slice(2,4)]
[[      38      -110    33      98      ]
 [      -59     -17     68      -6      ]]
2-D array  Shape: [2, 4]  DType: int8

A[Slice(1,3), Slice(1,3), 2]
[[      57      33      ]
 [      104     4       ]]
2-D array  Shape: [2, 2]  DType: int8

A.item(0,1,2) as Scalar
-105
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `*slices` (`Variant[Int, NewAxis, EllipsisType, Slice]`) `[imm]`: A series of either `Slice` or `Int`.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the number of slices is greater than the number of
dimensions of the array.

<div class="overload-divider">Overload 6</div>

```mojo
def __getitem__(self, indices: NDArray[DType.int]) -> Self
```

Gets items from the 0-th dimension of an array by an array of indices.

If the original array is of shape `(i, j, k)` and the indices array is
of shape `(l, m, n)`, then the output array will be of shape `(l, m, n,
j, k)`.

<div class="prose-label">Examples</div>

```console
>>>var a = nm.arange[i8](6)
>>>print(a)
[       0       1       2       3       4       5       ]
1-D array  Shape: [6]  DType: int8  C-cont: True  F-cont: True  own data: True
>>>print(a[nm.array[isize]("[4, 2, 5, 1, 0, 2]")])
[       4       2       5       1       0       2       ]
1-D array  Shape: [6]  DType: int8  C-cont: True  F-cont: True  own data: True

var b = nm.arange[i8](12).reshape(Shape(2, 2, 3))
print(b)
[[[     0       1       2       ]
  [     3       4       5       ]]
 [[     6       7       8       ]
  [     9       10      11      ]]]
3-D array  Shape: [2, 2, 3]  DType: int8  C-cont: True  F-cont: False  own data: True
print(b[nm.array[isize]("[1, 0, 1]")])
[[[     6       7       8       ]
  [     9       10      11      ]]
 [[     0       1       2       ]
  [     3       4       5       ]]
 [[     6       7       8       ]
  [     9       10      11      ]]]
3-D array  Shape: [3, 2, 3]  DType: int8  C-cont: True  F-cont: False  own data: True
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `indices` (`NDArray[DType.int]`) `[imm]`: The array of indices.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the elements of indices are greater than the size of the
corresponding dimension of the array.

<div class="overload-divider">Overload 7</div>

```mojo
def __getitem__(self, indices: List[Int]) -> Self
```

Gets items from the 0-th dimension of an array by a list of integer indices.

Overloads `__getitem__(indices: NDArray[DType.int])`.

<div class="prose-label">Examples</div>

```console
>>>var a = nm.arange[i8](6)
>>>print(a)
[       0       1       2       3       4       5       ]
1-D array  Shape: [6]  DType: int8  C-cont: True  F-cont: True  own data: True
>>>print(a[List[Int](4, 2, 5, 1, 0, 2)])
[       4       2       5       1       0       2       ]
1-D array  Shape: [6]  DType: int8  C-cont: True  F-cont: True  own data: True

var b = nm.arange[i8](12).reshape(Shape(2, 2, 3))
print(b)
[[[     0       1       2       ]
[     3       4       5       ]]
[[     6       7       8       ]
[     9       10      11      ]]]
3-D array  Shape: [2, 2, 3]  DType: int8  C-cont: True  F-cont: False  own data: True
print(b[List[Int](2, 0, 1)])
[[[     0       0       0       ]
[     0       67      95      ]]
[[     0       1       2       ]
[     3       4       5       ]]
[[     6       7       8       ]
[     9       10      11      ]]]
3-D array  Shape: [3, 2, 3]  DType: int8  C-cont: True  F-cont: False  own data: True
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `indices` (`List[Int]`) `[imm]`: A list of `Int`.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the elements of indices are greater than the size of the
corresponding dimension of the array.

<div class="overload-divider">Overload 8</div>

```mojo
def __getitem__(self, index_arrays: List[NDArray[DType.int]]) -> Self
```

Element-wise multi-axis fancy (advanced) indexing via a list of index arrays.

Each element of `index_arrays` is an integer array indexing one axis.
All arrays are broadcast against each other; the output shape equals
that broadcast shape. The outer ``[]`` is the list literal.

The number of index arrays must equal `self.ndim`.

<div class="prose-label">Examples</div>

```console
>>> var a = nm.arange[nm.i32](12).reshape(nm.Shape(3, 4))
>>> var rows = nm.array[nm.int]("[0, 1, 2]")
>>> var cols = nm.array[nm.int]("[2, 3, 0]")
>>> print(a[[rows, cols]])
[       2       7       8       ]
1-D array  Shape: [3]  DType: int32
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `index_arrays` (`List[NDArray[DType.int]]`) `[imm]`: A list of integer NDArrays, one per axis.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the number of index arrays does not equal `self.ndim`.
NumojoError: If the index arrays are not mutually broadcast-compatible.
NumojoError: If any index value is out of bounds for its axis.

<div class="overload-divider">Overload 9</div>

```mojo
def __getitem__(self, mask: NDArray[DType.bool]) -> Self
```

Gets items from an array according to a boolean mask array.

If array shape equals mask shape, returns a flattened array of the
values where mask is `True`. If array shape does not equal mask shape,
returns items from the 0-th dimension of the array where mask is `True`.

<div class="prose-label">Examples</div>

```console
>>>var a = nm.arange[i8](6)
>>>print(a)
[       0       1       2       3       4       5       ]
1-D array  Shape: [6]  DType: int8  C-cont: True  F-cont: True  own data: True
>>>print(a[nm.array[boolean]("[1,0,1,1,0,1]")])
[       0       2       3       5       ]
1-D array  Shape: [4]  DType: int8  C-cont: True  F-cont: True  own data: True

var b = nm.arange[i8](12).reshape(Shape(2, 2, 3))
print(b)
[[[     0       1       2       ]
[     3       4       5       ]]
[[     6       7       8       ]
[     9       10      11      ]]]
3-D array  Shape: [2, 2, 3]  DType: int8  C-cont: True  F-cont: False  own data: True
>>>print(b[nm.array[boolean]("[0,1]")])
[[[     6       7       8       ]
[     9       10      11      ]]]
3-D array  Shape: [1, 2, 3]  DType: int8  C-cont: True  F-cont: True  own data: True
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `mask` (`NDArray[DType.bool]`) `[imm]`: An NDArray with `DType.bool`.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the mask is not a 1-D array. Currently only 1-D mask
arrays are supported.

<div class="overload-divider">Overload 10</div>

```mojo
def __getitem__(self, mask: List[Bool]) -> Self
```

Gets items from the 0-th dimension of an array according to a boolean list mask.

Overloads `__getitem__(mask: NDArray[DType.bool])`.

<div class="prose-label">Examples</div>

```console
>>>var a = nm.arange[i8](6)
>>>print(a)
[       0       1       2       3       4       5       ]
1-D array  Shape: [6]  DType: int8  C-cont: True  F-cont: True  own data: True
>>>print(a[List[Bool](True, False, True, True, False, True)])
[       0       2       3       5       ]
1-D array  Shape: [4]  DType: int8  C-cont: True  F-cont: True  own data: True

var b = nm.arange[i8](12).reshape(Shape(2, 2, 3))
print(b)
[[[     0       1       2       ]
[     3       4       5       ]]
[[     6       7       8       ]
[     9       10      11      ]]]
3-D array  Shape: [2, 2, 3]  DType: int8  C-cont: True  F-cont: False  own data: True
>>>print(b[List[Bool](False, True)])
[[[     6       7       8       ]
[     9       10      11      ]]]
3-D array  Shape: [1, 2, 3]  DType: int8  C-cont: True  F-cont: True  own data: True
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `mask` (`List[Bool]`) `[imm]`: A list of boolean values.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the mask is not a 1-D array. Currently only 1-D mask
arrays are supported.


</div>

<div class="fn-card" markdown="1">

#### `__setitem__`

<div class="overload-divider">Overload 1</div>

```mojo
def __setitem__(mut self, idx: Int, val: Self)
```

Assigns a single first-axis slice.

Replaces the sub-array at axis-0 position `idx` with `val`. The shape of
`val` must exactly match `self.shape[1:]` and its dimensionality must be
`self.ndim - 1`. Negative indices are supported. A fast contiguous
`memcpy` path is used for C-order source and destination; otherwise a
stride-based loop writes each element (works for F-order and arbitrary
layouts).

<div class="prose-label">Notes</div>
Future work: broadcasting, zero-copy view assignment, and detection
of additional block-copy patterns in non-C-order layouts.

<div class="prose-label">Examples</div>
```console
>>> import numojo as nm
>>> var A = nm.arange[nm.f32](
...     0, 12, 1
... ).reshape(nm.Shape(3, 4))
>>> var row = nm.full[nm.f32](
...     nm.Shape(4), fill_value=99.0
... )
>>> A[1] = row  # Replaces second row.
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `idx` (`Int`) `[imm]`: The index along the first dimension (supports negative values
    in `[-shape[0], shape[0])`).
- `val` (`Self`) `[imm]`: The NDArray providing replacement data; shape must equal
    `self.shape[1:]`.

!!! failure "Raises"
    NumojoError: Target array is 0-D or index out of bounds.
NumojoError: `val.ndim != self.ndim - 1`.
NumojoError: `val.shape != self.shape[1:]`.

<div class="overload-divider">Overload 2</div>

```mojo
def __setitem__(mut self, var index: Item, val: Scalar[dtype])
```

Sets the value at the index list.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
from numojo.prelude import *
var A = nm.random.rand[nm.i16](2, 2, 2)
A[Item(0, 1, 1)] = 10
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `index` (`Item`) `[var]`: The index list.
- `val` (`Scalar[dtype]`) `[imm]`: The value to set.

!!! failure "Raises"
    NumojoError: If the length of index does not match the number of
dimensions.
NumojoError: If any of the indices is out of bound.

<div class="overload-divider">Overload 3</div>

```mojo
def __setitem__(mut self, *slices: Slice, *, val: Self)
```

Sets the elements of the array at the slices with the given array.

<div class="prose-label">Examples</div>
```mojo
import numojo

var A = numojo.random.rand[numojo.i16](2, 2, 2)
A[1:3, 2:4] = numojo.random.rand[numojo.i16](2, 2)
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `*slices` (`Slice`) `[imm]`: The variadic slices.
- `val` (`Self`) `[imm]`: The NDArray to set.

!!! failure "Raises"
    NumojoError: If the length of slices does not match the number of
dimensions.
NumojoError: If any of the slices is out of bound.

<div class="overload-divider">Overload 4</div>

```mojo
def __setitem__(mut self, index: NDArray[DType.int], val: Self)
```

Sets the items of the array from an array of indices.

<div class="prose-label">Examples</div>

```console
> var X = nm.NDArray[nm.i8](3,random=True)
> print(X)
[       32      21      53      ]
1-D array  Shape: [3]  DType: int8
> print(X.argsort())
[       1       0       2       ]
1-D array  Shape: [3]  DType: index
> print(X[X.argsort()])
[       21      32      53      ]
1-D array  Shape: [3]  DType: int8
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `index` (`NDArray[DType.int]`) `[imm]`: The array of indices.
- `val` (`Self`) `[imm]`: The value to set.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__neg__`

```mojo
def __neg__(self) -> Self
```

Returns a negated copy of the array.

For boolean arrays, use `__invert__` (`~`).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__pos__`

```mojo
def __pos__(self) -> Self
```

Returns a positive copy of the array.

Does not accept boolean type arrays.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__invert__`

```mojo
def __invert__(self) -> Self where dtype.is_integral() or (dtype == DType.bool)
```

Computes element-wise bitwise inversion.

Only works for boolean and integral types.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__lt__`

<div class="overload-divider">Overload 1</div>

```mojo
def __lt__(self, other: Scalar[dtype]) -> NDArray[DType.bool]
```

Computes itemwise less-than with a scalar.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`: The other SIMD value to compare with.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __lt__(self, other: Self) -> NDArray[DType.bool]
```

Computes itemwise less-than with an array.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The other array to compare with.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__le__`

<div class="overload-divider">Overload 1</div>

```mojo
def __le__(self, other: Scalar[dtype]) -> NDArray[DType.bool]
```

Computes itemwise less-than-or-equal-to with a scalar.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`: The other SIMD value to compare with.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __le__(self, other: Self) -> NDArray[DType.bool]
```

Computes itemwise less-than-or-equal-to with an array.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The other array to compare with.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__eq__`

<div class="overload-divider">Overload 1</div>

```mojo
def __eq__(self, other: Self) -> NDArray[DType.bool]
```

Computes itemwise equality.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The other array to compare with.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __eq__(self, other: Scalar[dtype]) -> NDArray[DType.bool]
```

Computes itemwise equality with a scalar.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`: The other SIMD value to compare with.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__ne__`

<div class="overload-divider">Overload 1</div>

```mojo
def __ne__(self, other: Scalar[dtype]) -> NDArray[DType.bool]
```

Computes itemwise inequality with a scalar.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`: The other SIMD value to compare with.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __ne__(self, other: Self) -> NDArray[DType.bool]
```

Computes itemwise inequality with an array.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The other array to compare with.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__gt__`

<div class="overload-divider">Overload 1</div>

```mojo
def __gt__(self, other: Scalar[dtype]) -> NDArray[DType.bool]
```

Computes itemwise greater-than with a scalar.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`: The other SIMD value to compare with.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __gt__(self, other: Self) -> NDArray[DType.bool]
```

Computes itemwise greater-than with an array.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The other array to compare with.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__ge__`

<div class="overload-divider">Overload 1</div>

```mojo
def __ge__(self, other: Scalar[dtype]) -> NDArray[DType.bool]
```

Computes itemwise greater-than-or-equal-to with a scalar.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`: The other SIMD value to compare with.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __ge__(self, other: Self) -> NDArray[DType.bool]
```

Computes itemwise greater-than-or-equal-to with an array.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The other array to compare with.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__add__`

<div class="overload-divider">Overload 1</div>

```mojo
def __add__(self, other: Scalar[dtype]) -> Self
```

Enables `array + scalar`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __add__(self, other: Self) -> Self
```

Enables `array + array`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__sub__`

<div class="overload-divider">Overload 1</div>

```mojo
def __sub__(self, other: Scalar[dtype]) -> Self
```

Enables `array - scalar`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __sub__(self, other: Self) -> Self
```

Enables `array - array`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__mul__`

<div class="overload-divider">Overload 1</div>

```mojo
def __mul__(self, other: Scalar[dtype]) -> Self
```

Enables `array * scalar`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __mul__(self, other: Self) -> Self
```

Enables `array * array`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__matmul__`

```mojo
def __matmul__(self, other: Self) -> Self
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__truediv__`

<div class="overload-divider">Overload 1</div>

```mojo
def __truediv__(self, other: Scalar[dtype]) -> Self
```

Enables `array / scalar`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __truediv__(self, other: Self) -> Self
```

Enables `array / array`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__floordiv__`

<div class="overload-divider">Overload 1</div>

```mojo
def __floordiv__(self, other: Scalar[dtype]) -> Self
```

Enables `array // scalar`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __floordiv__(self, other: Self) -> Self
```

Enables `array // array`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__mod__`

<div class="overload-divider">Overload 1</div>

```mojo
def __mod__(mut self, other: Scalar[dtype]) -> Self
```

Enables `array % scalar`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __mod__(mut self, other: Self) -> Self
```

Enables `array % array`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__pow__`

<div class="overload-divider">Overload 1</div>

```mojo
def __pow__(self, p: Int) -> Self
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `p` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __pow__(self, rhs: Scalar[dtype]) -> Self
```

Computes element-wise power of items.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `rhs` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 3</div>

```mojo
def __pow__(self, p: Self) -> Self
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `p` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__radd__`

```mojo
def __radd__(mut self, other: Scalar[dtype]) -> Self
```

Enables `scalar + array`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__rsub__`

```mojo
def __rsub__(mut self, other: Scalar[dtype]) -> Self
```

Enables `scalar - array`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__rmul__`

```mojo
def __rmul__(self, other: Scalar[dtype]) -> Self
```

Enables `scalar * array`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__rtruediv__`

```mojo
def __rtruediv__(self, s: Scalar[dtype]) -> Self
```

Enables `scalar / array`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `s` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__rfloordiv__`

```mojo
def __rfloordiv__(self, other: Scalar[dtype]) -> Self
```

Enables `scalar // array`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__rmod__`

```mojo
def __rmod__(mut self, other: Scalar[dtype]) -> Self
```

Enables `scalar % array`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__iadd__`

<div class="overload-divider">Overload 1</div>

```mojo
def __iadd__(mut self, other: Scalar[dtype])
```

Enables `array += scalar`. View-safe: modifies buffer in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Scalar[dtype]`) `[imm]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __iadd__(mut self, other: Self)
```

Enables `array += array`. View-safe: modifies buffer in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__isub__`

<div class="overload-divider">Overload 1</div>

```mojo
def __isub__(mut self, other: Scalar[dtype])
```

Enables `array -= scalar`. View-safe: modifies buffer in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Scalar[dtype]`) `[imm]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __isub__(mut self, other: Self)
```

Enables `array -= array`. View-safe: modifies buffer in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__imul__`

<div class="overload-divider">Overload 1</div>

```mojo
def __imul__(mut self, other: Scalar[dtype])
```

Enables `array *= scalar`. View-safe: modifies buffer in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Scalar[dtype]`) `[imm]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __imul__(mut self, other: Self)
```

Enables `array *= array`. View-safe: modifies buffer in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__itruediv__`

<div class="overload-divider">Overload 1</div>

```mojo
def __itruediv__(mut self, s: Scalar[dtype])
```

Enables `array /= scalar`. View-safe: modifies buffer in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `s` (`Scalar[dtype]`) `[imm]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __itruediv__(mut self, other: Self)
```

Enables `array /= array`. View-safe: modifies buffer in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__ifloordiv__`

<div class="overload-divider">Overload 1</div>

```mojo
def __ifloordiv__(mut self, s: Scalar[dtype])
```

Enables `array //= scalar`. View-safe: modifies buffer in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `s` (`Scalar[dtype]`) `[imm]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __ifloordiv__(mut self, other: Self)
```

Enables `array //= array`. View-safe: modifies buffer in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__imod__`

<div class="overload-divider">Overload 1</div>

```mojo
def __imod__(mut self, other: Scalar[dtype])
```

Enables `array %= scalar`. View-safe: modifies buffer in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Scalar[dtype]`) `[imm]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def __imod__(mut self, other: Self)
```

Enables `array %= array`. View-safe: modifies buffer in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__ipow__`

```mojo
def __ipow__(mut self, p: Int)
```

Enables `array **= int`. View-safe: modifies buffer in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `p` (`Int`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `view`

```mojo
def view(mut self) -> Self
```

Create a non-owning view of the current NDArray.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var arr = nm.NDArray[nm.f32](nm.Shape(3, 4))
var v = arr.view()  # Create a view into arr
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `view_with_layout`

```mojo
def view_with_layout(self, shape: NDArrayShape, strides: NDArrayStrides, offset: Int) -> Self
```

Create a non-owning view with explicit logical layout metadata.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `shape` (`NDArrayShape`) `[imm]`
- `strides` (`NDArrayStrides`) `[imm]`
- `offset` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `normalize`

```mojo
def normalize(self, idx: Int, dim: Int) -> Int
```

Normalizes a potentially negative index to its positive equivalent within the bounds of the given dimension.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: The index to normalize. Can be negative to indicate indexing
    from the end (e.g., -1 refers to the last element).
- `dim` (`Int`) `[imm]`: The size of the dimension to normalize against.

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `item`

<div class="overload-divider">Overload 1</div>

```mojo
def item(self, var index: Int) -> Scalar[dtype]
```

Returns the scalar at the given linear index.

If one index is given, gets the i-th item of the array (not buffer). It
first scans over the first row, even if it is a column-major array. If
more than one index is given, the length of the indices must match the
number of dimensions of the array. If the ndim is 0 (0-D array), gets
the value as a Mojo scalar.

<div class="prose-label">Examples</div>

```console
>>> var A = nm.random.randn[nm.f16](2, 2, 2)
>>> A = A.reshape(A.shape, order="F")
>>> print(A)
[[[     0.2446289       0.5419922       ]
[     0.09643555      -0.90722656     ]]
[[     1.1806641       0.24389648      ]
[     0.5234375       1.0390625       ]]]
3-D array  Shape: [2, 2, 2]  DType: float16  order: F
>>> for i in range(A.size):
...     print(A.item(i))
0.2446289
0.5419922
0.09643555
-0.90722656
1.1806641
0.24389648
0.5234375
1.0390625
>>> print(A.item(0, 1, 1))
-0.90722656
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[var]`: The index of the item, counted in row-major order.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If the array is a 0-D array.
NumojoError: If index is equal to or larger than the array size.

<div class="overload-divider">Overload 2</div>

```mojo
def item(self, *index: Int) -> Scalar[dtype]
```

Returns the scalar at the given coordinates.

If one index is given, gets the i-th item of the array (not buffer). It
first scans over the first row, even if it is a column-major array. If
more than one index is given, the length of the indices must match the
number of dimensions of the array. For 0-D array (numojo scalar),
returns the scalar value.

<div class="prose-label">Examples</div>

```console
>>> var A = nm.random.randn[nm.f16](2, 2, 2)
>>> A = A.reshape(A.shape, order="F")
>>> print(A)
[[[     0.2446289       0.5419922       ]
[     0.09643555      -0.90722656     ]]
[[     1.1806641       0.24389648      ]
[     0.5234375       1.0390625       ]]]
3-D array  Shape: [2, 2, 2]  DType: float16  order: F
>>> print(A.item(0, 1, 1))
-0.90722656
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `*index` (`Int`) `[imm]`: The coordinates of the item.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If the number of indices is not equal to the number of
dimensions of the array.
NumojoError: If the index is equal to or larger than the size of the
dimension.


</div>

<div class="fn-card" markdown="1">

#### `unsafe_get`

```mojo
def unsafe_get(self, index: Int) -> Scalar[dtype]
```

Return the scalar at a logical flat index without bounds checks.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`


</div>

<div class="fn-card" markdown="1">

#### `unsafe_set`

```mojo
def unsafe_set(mut self, index: Int, value: Scalar[dtype])
```

Store a scalar at a logical flat index without bounds checks.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `index` (`Int`) `[imm]`
- `value` (`Scalar[dtype]`) `[imm]`


</div>

<div class="fn-card" markdown="1">

#### `unsafe_load`

```mojo
def unsafe_load[width: Int = Int(1)](self, index: Int) -> SIMD[dtype, width]
```

Unsafely retrieves the i-th item from the underlying buffer as a SIMD element of size `width`.

This method does not perform boundary checks. Use the `load` method for
safe retrieval.

<div class="prose-label">Parameters</div>

- `width` (`Int`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[imm]`: The index of the item.

<div class="prose-label">Returns</div>

- `SIMD[dtype, width]`


</div>

<div class="fn-card" markdown="1">

#### `load`

<div class="overload-divider">Overload 1</div>

```mojo
def load(self, var index: Int) -> Scalar[dtype]
```

Safely retrieves the i-th item from the underlying buffer.

`A.load(i)` differs from `A._buf.ptr[i]` due to boundary check.

<div class="prose-label">Examples</div>

```console
> array.load(15)
```
Returns the item of index 15 from the array's data buffer.

Note that it does not check against C-order or F-order.
```console
> # A is a 3x3 matrix, F-order (column-major).
> A.load(3)  # Row 0, Col 1.
> A.item(3)  # Row 1, Col 0.
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[var]`: The index of the item.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"
    NumojoError: If the index is out of bounds.

<div class="overload-divider">Overload 2</div>

```mojo
def load[width: Int = Int(1)](self, var index: Int) -> SIMD[dtype, width]
```

Safely loads a SIMD element of size `width` at `index` from the underlying buffer.

To bypass boundary checks, use `self._buf.ptr.load` directly.

<div class="prose-label">Parameters</div>

- `width` (`Int`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[var]`: The index of the item.

<div class="prose-label">Returns</div>

- `SIMD[dtype, width]`

!!! failure "Raises"
    NumojoError: If the index is out of boundary.

<div class="overload-divider">Overload 3</div>

```mojo
def load[width: Int = Int(1)](self, *indices: Int) -> SIMD[dtype, width]
```

Safely loads a SIMD element of size `width` at given variadic indices from the underlying buffer.

To bypass boundary checks, use `self._buf.ptr.load` directly.

<div class="prose-label">Examples</div>

```console
>>> import numojo
>>> var A = numojo.random.randn[numojo.f16](2, 2, 2)
>>> print(A.load(0, 1, 1))
```.

<div class="prose-label">Parameters</div>

- `width` (`Int`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `*indices` (`Int`) `[imm]`: The variadic indices.

<div class="prose-label">Returns</div>

- `SIMD[dtype, width]`

!!! failure "Raises"
    NumojoError: If the length of indices does not match the number of
dimensions.
NumojoError: If any of the indices is out of bound.


</div>

<div class="fn-card" markdown="1">

#### `set`

<div class="overload-divider">Overload 1</div>

```mojo
def set(mut self, mask: NDArray[DType.bool], *, val: Scalar[dtype])
```

Sets elements where `mask` is `True` to a scalar value.

Supports three mask shapes:
- Exact shape match: writes to every True element.
- 1-D mask of length `shape[0]`: fills each selected axis-0 slice.
- k-D mask matching `shape[:k]`: fills each selected k-dimensional block.

<div class="prose-label">Notes</div>
Use `arr.set(mask, val=scalar)` rather than `arr[mask] = scalar`
— Mojo cannot distinguish the scalar from the NDArray overload at
the `__setitem__` level.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var A = nm.arange[nm.f32](6)
var mask = A > Float32(2.0)
A.set(mask, val=Float32(0.0))
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `mask` (`NDArray[DType.bool]`) `[imm]`: Boolean mask array.
- `val` (`Scalar[dtype]`) `[imm]`: The scalar value to write at every True position.

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def set(mut self, *slices: Variant[Slice, Int], *, val: Self)
```

Sets elements selected by mixed integer/slice indices from an NDArray.

Integer entries select a single position in the corresponding dimension
(unit-length slice). Slice entries select a range. Trailing dimensions
not covered by `slices` are treated as full-range.

<div class="prose-label">Notes</div>
Use `arr.set(i, s, val=patch)` rather than `arr[i, s] = patch`
— Mojo cannot construct `Variant[Slice, Int]` from a mixed
`Int`+`Slice` literal pair at the `__setitem__` subscript site.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](16).reshape(nm.Shape(4, 4))
var patch = nm.full[nm.i32](nm.Shape(2), fill_value=7)
a.set(1, Slice(1, 3), val=patch)  # row 1, cols 1-2
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `*slices` (`Variant[Slice, Int]`) `[imm]`: Variadic mix of `Slice` and `Int` index entries.
- `val` (`Self`) `[imm]`: The NDArray value to write into the selected region.

!!! failure "Raises"

<div class="overload-divider">Overload 3</div>

```mojo
def set(mut self, *slices: Slice, *, val: Scalar[dtype])
```

Sets all elements in the slice region to a scalar value.

<div class="prose-label">Notes</div>
Use `arr.set(s1, s2, val=scalar)` rather than `arr[s1, s2] = scalar`
— Mojo cannot distinguish the scalar from the NDArray overload at
the `__setitem__` level.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](16).reshape(nm.Shape(4, 4))
a.set(Slice(1, 3), Slice(1, 3), val=99)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `*slices` (`Slice`) `[imm]`: Variadic slices, one per dimension. Trailing dimensions
    default to the full range.
- `val` (`Scalar[dtype]`) `[imm]`: The scalar value to broadcast into every selected position.

!!! failure "Raises"

<div class="overload-divider">Overload 4</div>

```mojo
def set(mut self, *slices: Variant[Slice, Int], *, val: Scalar[dtype])
```

Sets elements selected by mixed integer/slice indices to a scalar.

Integer entries select a single position in the corresponding dimension;
slice entries select a range. All-integer arguments write one element
directly. Mixed or slice-only arguments fill every selected position.

<div class="prose-label">Notes</div>
Use `arr.set(..., val=scalar)` rather than `arr[...] = scalar`
— Mojo cannot distinguish the scalar from the NDArray overload at
the `__setitem__` level.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](16).reshape(nm.Shape(4, 4))
a.set(1, 2, val=99)                     # single element
a.set(1, Slice(2, 4), val=0)            # row 1, cols 2-3
a.set(Slice(1, 3), Slice(2, 4), val=7)  # sub-matrix
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `*slices` (`Variant[Slice, Int]`) `[imm]`: Variadic mix of `Slice` and `Int` index entries.
- `val` (`Scalar[dtype]`) `[imm]`: The scalar value to write.

!!! failure "Raises"

<div class="overload-divider">Overload 5</div>

```mojo
def set(mut self, mask: NDArray[DType.bool], *, val: Self)
```

Sets elements where `mask` is `True` from an NDArray value.

Supported `val` shapes (same three mask cases as the scalar overload):
- Exact-shape mask: elementwise, size-1 broadcast, or compact 1-D.
- 1-D mask of length `shape[0]`: single sub-array or per-index array.
- k-D mask matching `shape[:k]`: single sub-array or per-index array.

<div class="prose-label">Notes</div>
Use `arr.set(mask, val=values)` rather than `arr[mask] = values`
— Mojo cannot distinguish the scalar from the NDArray overload at
the `__setitem__` level.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
var A = nm.arange[nm.f32](6).reshape(nm.Shape(2, 3))
var mask = A > Float32(2.0)
var vals = nm.array[nm.f32]("[10.0, 20.0, 30.0]")
A.set(mask, val=vals)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `mask` (`NDArray[DType.bool]`) `[imm]`: Boolean mask array.
- `val` (`Self`) `[imm]`: The NDArray value(s) to write.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `itemset`

<div class="overload-divider">Overload 1</div>

```mojo
def itemset(mut self, index: Int, item: Scalar[dtype])
```

Sets the scalar at the given coordinate.

<div class="prose-label">Examples</div>

```
import numojo as nm
def main() raises:
    var A = nm.zeros[nm.i16](3, 3)
    print(A)
    A.itemset(5, 256)
    print(A)
```
```console
[[      0       0       0       ]
[      0       0       0       ]
[      0       0       0       ]]
2-D array  Shape: [3, 3]  DType: int16
[[      0       0       0       ]
[      0       0       256     ]
[      0       0       0       ]]
2-D array  Shape: [3, 3]  DType: int16
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `index` (`Int`) `[imm]`: The coordinates of the item. It is the index of the
    i-th item of the whole array.
- `item` (`Scalar[dtype]`) `[imm]`: The scalar to be set.

!!! failure "Raises"
    NumojoError: If the index is out of bound.
NumojoError: If the length of index does not match the number of
dimensions.

<div class="overload-divider">Overload 2</div>

```mojo
def itemset(mut self, var indices: List[Int], item: Scalar[dtype])
```

Sets the scalar at the given coordinates.

<div class="prose-label">Notes</div>
This overload accepts a `List[Int]` of coordinates.

<div class="prose-label">Examples</div>

```
import numojo as nm
def main() raises:
    var A = nm.zeros[nm.i16](3, 3)
    print(A)
    A.itemset(List(1,1), 1024)
    print(A)
```
```console
[[      0       0       0       ]
[      0       0       0       ]
[      0       0       0       ]]
2-D array  Shape: [3, 3]  DType: int16
[[      0       0       0       ]
[      0       1024    0       ]
[      0       0       0       ]]
2-D array  Shape: [3, 3]  DType: int16
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `indices` (`List[Int]`) `[var]`: The coordinates of the item.
- `item` (`Scalar[dtype]`) `[imm]`: The scalar to be set.

!!! failure "Raises"
    NumojoError: If the index is out of bound.
NumojoError: If the length of index does not match the number of
dimensions.


</div>

<div class="fn-card" markdown="1">

#### `unsafe_store`

```mojo
def unsafe_store[width: Int = Int(1)](mut self, index: Int, val: SIMD[dtype, width])
```

Unsafely stores a SIMD element to the i-th item of the underlying buffer.

`A.unsafe_store(i, a)` is equivalent to `A._buf.ptr.store(i, a)`. It
does not perform boundary check and is faster than `store`.

<div class="prose-label">Parameters</div>

- `width` (`Int`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `index` (`Int`) `[imm]`: The index of the item.
- `val` (`SIMD[dtype, width]`) `[imm]`: The value to store.


</div>

<div class="fn-card" markdown="1">

#### `store`

<div class="overload-divider">Overload 1</div>

```mojo
def store(mut self, var index: Int, val: Scalar[dtype])
```

Safely stores a scalar to the i-th item of the underlying buffer.

`A.store(i, a)` differs from `A._buf.ptr[i] = a` due to boundary check.

<div class="prose-label">Examples</div>

```console
> array.store(15, val = 100)
```
Sets the item of index 15 of the array's data buffer to 100. Note that
it does not check against C-order or F-order.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `index` (`Int`) `[var]`: The index of the item.
- `val` (`Scalar[dtype]`) `[imm]`: The value to store.

!!! failure "Raises"
    NumojoError: If the index is out of boundary.

<div class="overload-divider">Overload 2</div>

```mojo
def store[width: Int = Int(1)](mut self, index: Int, val: SIMD[dtype, width])
```

Safely stores a SIMD element of size `width` at `index` of the underlying buffer.

To bypass boundary checks, use `self._buf.ptr.store` directly.

<div class="prose-label">Examples</div>

```console
> array.store(15, val = 100)
```
sets the item of index 15 of the array's data buffer to 100.

<div class="prose-label">Parameters</div>

- `width` (`Int`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `index` (`Int`) `[imm]`: The index of the item.
- `val` (`SIMD[dtype, width]`) `[imm]`: The value to store.

!!! failure "Raises"
    NumojoError: If the index is out of boundary.

<div class="overload-divider">Overload 3</div>

```mojo
def store[width: Int = Int(1)](mut self, *indices: Int, *, val: SIMD[dtype, width])
```

Safely stores a SIMD element of size `width` at given variadic indices of the underlying buffer.

To bypass boundary checks, use `self._buf.ptr.store` directly.

<div class="prose-label">Examples</div>

```console
>>> import numojo
>>> var A = numojo.random.rand[numojo.i16](2, 2, 2)
>>> A.store(0, 1, 1, val=100)
```.

<div class="prose-label">Parameters</div>

- `width` (`Int`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `*indices` (`Int`) `[imm]`: The variadic indices.
- `val` (`SIMD[dtype, width]`) `[imm]`: The value to store.

!!! failure "Raises"
    NumojoError: If the index is out of boundary.


</div>

<div class="fn-card" markdown="1">

#### `__int__`

```mojo
def __int__(self) -> Int
```

Gets `Int` representation of the array.

Only 0-D arrays or length-1 arrays can be converted to scalars.

<div class="prose-label">Examples</div>

```console
> var A = NDArray[dtype](6, random=True)
> print(Int(A))

Unhandled exception caught during execution: Only 0-D arrays or length-1 arrays can be converted to scalars
mojo: error: execution exited with a non-zero result: 1

> var B = NDArray[dtype](1, 1, random=True)
> print(Int(B))
14
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`

!!! failure "Raises"
    NumojoError: If the array is not 0-D or length-1.


</div>

<div class="fn-card" markdown="1">

#### `__float__`

```mojo
def __float__(self) -> Float64
```

Gets `Float64` representation of the array.

Only 0-D arrays or length-1 arrays can be converted to scalars.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Float64`

!!! failure "Raises"
    NumojoError: If the array is not 0-D or length-1.


</div>

<div class="fn-card" markdown="1">

#### `__abs__`

```mojo
def __abs__(self) -> Self
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__str__`

```mojo
def __str__(self) -> String
```

Returns the string representation of the array.

Enables `String(array)`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>

<div class="fn-card" markdown="1">

#### `write_to`

```mojo
def write_to[W: Writer](self, mut writer: W)
```

Writes the array to a writer.

<div class="prose-label">Parameters</div>

- `W` (`Writer`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`: The writer to write the array to.


</div>

<div class="fn-card" markdown="1">

#### `__repr__`

```mojo
def __repr__(self) -> String
```

Computes the "official" string representation of the NDArray.

You can construct the array using this representation.

<div class="prose-label">Examples</div>

```console
>>>import numojo as nm
>>>var b = nm.arange[nm.f32](20).reshape(Shape(4, 5))
>>>print(repr(b))
numojo.array[f32](
'''
[[0.0, 1.0, 2.0, 3.0, 4.0]
[5.0, 6.0, 7.0, 8.0, 9.0]
[10.0, 11.0, 12.0, 13.0, 14.0]
[15.0, 16.0, 17.0, 18.0, 19.0]]
'''
)
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `String`


</div>

<div class="fn-card" markdown="1">

#### `write_repr_to`

```mojo
def write_repr_to[W: Writer](self, mut writer: W)
```

Write the string representation to a writer.

<div class="prose-label">Parameters</div>

- `W` (`Writer`): The writer type.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

#### `__len__`

```mojo
def __len__(self) -> Int
```

Returns the length of the 0-th dimension.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `__iter__`

```mojo
def __iter__(self) -> _NDArrayIter[origin_of(self), dtype]
```

Iterates over elements of the NDArray and returns sub-arrays as views.

<div class="prose-label">Examples</div>

```
>>> var a = nm.random.arange[nm.i8](2, 3, 4).reshape(nm.Shape(2, 3, 4))
>>> for i in a:
...     print(i)
[[      0       1       2       3       ]
[      4       5       6       7       ]
[      8       9       10      11      ]]
2-D array  Shape: [3, 4]  DType: int8  C-cont: True  F-cont: False  own data: False
[[      12      13      14      15      ]
[      16      17      18      19      ]
[      20      21      22      23      ]]
2-D array  Shape: [3, 4]  DType: int8  C-cont: True  F-cont: False  own data: False
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `_NDArrayIter[origin_of(self), dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `__reversed__`

```mojo
def __reversed__(self) -> _NDArrayIter[origin_of(self), dtype, False]
```

Iterates backwards over elements of the NDArray, returning copied values.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `_NDArrayIter[origin_of(self), dtype, False]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `all`

```mojo
def all(self) -> Bool where (dtype == DType.bool) if (dtype == DType.bool) else dtype.is_integral()
```

Returns `True` if all elements are truthy.

This method is offset and stride-aware via `contiguous()`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`

!!! failure "Raises"
    NumojoError: If the array elements are not Boolean or Integer.


</div>

<div class="fn-card" markdown="1">

#### `any`

```mojo
def any(self) -> Bool where (dtype == DType.bool) if (dtype == DType.bool) else dtype.is_integral()
```

Returns `True` if any element is truthy.

This method is offset- and stride-aware via `contiguous()`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`

!!! failure "Raises"
    NumojoError: If the array elements are not Boolean or Integer.


</div>

<div class="fn-card" markdown="1">

#### `argmax`

<div class="overload-divider">Overload 1</div>

```mojo
def argmax(self) -> Int
```

Returns the indices of the maximum values along an axis. When no axis is specified, the array is flattened. See `numojo.argmax()` for more details.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def argmax(self, axis: Int) -> NDArray[DType.int]
```

Returns the indices of the maximum values along an axis. See `numojo.argmax()` for more details.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[DType.int]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `argmin`

<div class="overload-divider">Overload 1</div>

```mojo
def argmin(self) -> Int
```

Returns the indices of the minimum values along an axis. When no axis is specified, the array is flattened. See `numojo.argmin()` for more details.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def argmin(self, axis: Int) -> NDArray[DType.int]
```

Returns the indices of the minimum values along an axis. See `numojo.argmin()` for more details.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[DType.int]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `argsort`

<div class="overload-divider">Overload 1</div>

```mojo
def argsort(mut self) -> NDArray[DType.int]
```

Sorts the NDArray and returns the sorted indices. See `numojo.argsort()` for more details.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`

<div class="prose-label">Returns</div>

- `NDArray[DType.int]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def argsort(mut self, axis: Int) -> NDArray[DType.int]
```

Sorts the NDArray and returns the sorted indices. See `numojo.argsort()` for more details.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `axis` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[DType.int]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `astype`

```mojo
def astype[target: DType](self) -> NDArray[target]
```

Converts the type of the array.

<div class="prose-label">Parameters</div>

- `target` (`DType`): The target data type.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[target]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `clip`

```mojo
def clip(self, a_min: Scalar[dtype], a_max: Scalar[dtype]) -> Self
```

Limits the values in an array between `[a_min, a_max]`.

If `a_min` is greater than `a_max`, the value is equal to `a_max`. See
`clip()` for more details.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `a_min` (`Scalar[dtype]`) `[imm]`: The minimum value.
- `a_max` (`Scalar[dtype]`) `[imm]`: The maximum value.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `compress`

<div class="overload-divider">Overload 1</div>

```mojo
def compress(self, condition: NDArray[DType.bool], axis: Int) -> Self
```

Returns selected slices of an array along a given axis.

If no axis is provided, the array is flattened before use.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `condition` (`NDArray[DType.bool]`) `[imm]`: A 1-D array of booleans that selects which entries to
    return. If length of condition is less than the size of the
    array along the given axis, then output is filled to the length
    of the condition with `False`.
- `axis` (`Int`) `[imm]`: The axis along which to take slices.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the axis is out of bound for the given array.
NumojoError: If the condition is not a 1-D array.
NumojoError: If the condition length is out of bound for the given axis.
NumojoError: If the condition contains no `True` values.

<div class="overload-divider">Overload 2</div>

```mojo
def compress(self, condition: NDArray[DType.bool]) -> Self
```

Returns selected slices of an array along a given axis.

If no axis is provided, the array is flattened before use. This is a
function ***OVERLOAD***.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `condition` (`NDArray[DType.bool]`) `[imm]`: A 1-D array of booleans that selects which entries to
    return. If length of condition is less than the size of the
    array along the given axis, then output is filled to the length
    of the condition with `False`.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the condition is not a 1-D array.
NumojoError: If the condition length is out of bound for the given axis.
NumojoError: If the condition contains no `True` values.


</div>

<div class="fn-card" markdown="1">

#### `nonzero`

```mojo
def nonzero(self) -> List[NDArray[DType.int]]
```

Returns the indices of non-zero elements, one array per dimension. Each array in the returned list contains the coordinates of non-zero elements along that dimension, in C-order.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.array[nm.i32]("[3, 0, 5, 0, 2]")
var idx = a.nonzero()
print(idx[0])  # [0, 2, 4]

var b = nm.array[nm.i32]("[[1, 0], [0, 4]]")
var idx2 = b.nonzero()
print(idx2[0])  # [0, 1]
print(idx2[1])  # [0, 1]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `List[NDArray[DType.int]]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `flatnonzero`

```mojo
def flatnonzero(self) -> NDArray[DType.int]
```

Returns flat indices of non-zero elements.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[DType.int]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `contiguous`

```mojo
def contiguous(self) -> Self
```

Returns a new C-contiguous array owning a copy of the data.

Always creates a new owned array, even if the source is already
C-contiguous. This ensures consistent behavior: the caller can
always assume the result is independent of the source.

For the already-contiguous fast path, data is copied with a single
`memcpy`. For non-contiguous views, a stride-aware element-by-element
copy is performed.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f32](24).reshape(nm.Shape(2, 3, 4))
var v = a[0:2:1, 0:3:2]  # non-contiguous view
var c = v.contiguous()    # new C-contiguous owned copy
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `col`

```mojo
def col(self, id: Int) -> Self
```

Gets the i-th column of the matrix.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `id` (`Int`) `[imm]`: The column index.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `cumprod`

<div class="overload-divider">Overload 1</div>

```mojo
def cumprod(self) -> Self
```

Returns the cumulative product of all items of an array. The array is flattened before computation.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def cumprod(self, axis: Int) -> Self
```

Returns the cumulative product of the array along the given axis.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `cumsum`

<div class="overload-divider">Overload 1</div>

```mojo
def cumsum(self) -> Self
```

Returns the cumulative sum of all items of an array. The array is flattened before computation.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def cumsum(self, axis: Int) -> Self
```

Returns the cumulative sum of the array along the given axis.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `diagonal`

```mojo
def diagonal(self, offset: Int = Int(0), axis1: Int = Int(0), axis2: Int = Int(1)) -> Self
```

Returns specific diagonals.

For 2-D arrays (the default `axis1=0, axis2=1`), returns the 1-D
diagonal at the given `offset`. For N-D arrays, `axis1`/`axis2`
select the two axes whose 2-D sub-array diagonals are extracted; the
result has those two axes removed and replaced by a trailing
diagonal axis.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `offset` (`Int`) `[imm]`: The offset of the diagonal from the main diagonal.
- `axis1` (`Int`) `[imm]`: First axis of the 2-D sub-arrays from which the
    diagonals should be taken. Defaults to 0.
- `axis2` (`Int`) `[imm]`: Second axis of the 2-D sub-arrays from which the
    diagonals should be taken. Defaults to 1.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the array has fewer than 2 dimensions.
NumojoError: If `axis1` or `axis2` is out of bounds, or equal.
NumojoError: If the offset is beyond the shape of the array.


</div>

<div class="fn-card" markdown="1">

#### `take`

<div class="overload-divider">Overload 1</div>

```mojo
def take(self, indices: NDArray[DType.int], axis: Int) -> Self
```

Takes elements from the array along an axis.

Output shape is `self.shape[:axis] + indices.shape + self.shape[axis+1:]`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](12).reshape(nm.Shape(3, 4))
print(a.take(nm.array[nm.int]("[2, 0, 1]"), axis=0))
# [[8, 9, 10, 11], [0, 1, 2, 3], [4, 5, 6, 7]]

print(a.take(nm.array[nm.int]("[1, 3]"), axis=1))
# [[1, 3], [5, 7], [9, 11]]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `indices` (`NDArray[DType.int]`) `[imm]`: Indices to select along the axis. May be any shape.
    Negative indices are normalised.
- `axis` (`Int`) `[imm]`: Axis along which to select. Negative values count from the
    end.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If `axis` is out of bounds.
NumojoError: If any index is out of bounds for the given axis.

<div class="overload-divider">Overload 2</div>

```mojo
def take(self, indices: NDArray[DType.int]) -> Self
```

Takes elements from the flattened array by linear indices.

Equivalent to `self.flatten().take(indices, axis=0)`. Output shape
matches `indices.shape`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](12).reshape(nm.Shape(3, 4))
print(a.take(nm.array[nm.int]("[0, 5, 11]")))
# [0, 5, 11]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `indices` (`NDArray[DType.int]`) `[imm]`: Linear indices into the flattened array. May be any shape.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If any index is out of bounds for the flattened array.


</div>

<div class="fn-card" markdown="1">

#### `take_along_axis`

```mojo
def take_along_axis(self, indices: NDArray[DType.int], axis: Int = Int(0)) -> Self
```

Takes values from the array along the given axis based on indices.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i8](12).reshape(nm.Shape(3, 4))
var ind = nm.array[nm.int]("[[0, 1, 2, 0], [1, 0, 2, 1]]")
print(a.take_along_axis(ind, axis=0))
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `indices` (`NDArray[DType.int]`) `[imm]`: The indices array.
- `axis` (`Int`) `[imm]`: The axis along which to take values. Default is 0.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the axis is out of bounds for the array.
NumojoError: If the ndim of self and indices are not the same.
NumojoError: If the shape of indices does not match the shape of self
except along the given axis.


</div>

<div class="fn-card" markdown="1">

#### `fancy_index`

```mojo
def fancy_index(self, *index_arrays: NDArray[DType.int]) -> Self
```

Element-wise multi-axis fancy (advanced) indexing.

Selects elements from the array by supplying one integer-array index
per axis.  All index arrays are broadcast against each other; the
output shape equals that broadcast shape.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](12).reshape(nm.Shape(3, 4))
var rows = nm.array[nm.int]("[0, 1]")
var cols = nm.array[nm.int]("[2, 3]")
print(a.fancy_index(rows, cols))
# [2  7]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `*index_arrays` (`NDArray[DType.int]`) `[imm]`: Exactly `self.ndim` integer index arrays, one per
    axis.  Each is broadcast to the common shape before indexing.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the number of index arrays does not equal `self.ndim`.
NumojoError: If the index arrays are not mutually broadcast-compatible.
NumojoError: If any index value is out of bounds for its axis.


</div>

<div class="fn-card" markdown="1">

#### `where`

<div class="overload-divider">Overload 1</div>

```mojo
def where(self, x: Self, y: Self) -> Self where (dtype == DType.bool)
```

Returns elements chosen from `x` or `y` depending on this mask.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `x` (`Self`) `[imm]`
- `y` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def where(self, x: Self, y: Scalar[dtype]) -> Self where (dtype == DType.bool)
```

Returns elements from `x` or scalar `y` depending on this mask.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `x` (`Self`) `[imm]`
- `y` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 3</div>

```mojo
def where(self, x: Scalar[dtype], y: Self) -> Self where (dtype == DType.bool)
```

Returns scalar `x` or elements from `y` depending on this mask.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `x` (`Scalar[dtype]`) `[imm]`
- `y` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `put`

<div class="overload-divider">Overload 1</div>

```mojo
def put(mut self, indices: NDArray[DType.int], values: Self)
```

Replaces values at flat (linear) index positions in-place.

Equivalent to `self.flatten()[indices] = values`, but writes
directly into `self`. If `values` has fewer elements than
`indices`, it is repeated (broadcast) cyclically over `indices`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](6)
a.put(nm.array[nm.int]("[0, 2]"), nm.array[nm.i32]("[10, 20]"))
print(a)
# [10, 1, 20, 3, 4, 5]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `indices` (`NDArray[DType.int]`) `[imm]`: Linear (flat) indices into `self`. May be any shape.
    Negative indices are normalised (counted from the end).
- `values` (`Self`) `[imm]`: Values to write. Broadcast cyclically if shorter than
    `indices`.

!!! failure "Raises"
    NumojoError: If any index is out of bounds for the flattened array.
NumojoError: If `values` is empty while `indices` is not.

<div class="overload-divider">Overload 2</div>

```mojo
def put(mut self, indices: NDArray[DType.int], value: Scalar[dtype])
```

Replaces values at flat (linear) index positions in-place with a single broadcast scalar.

This is a method ***OVERLOAD*** of `put` for the scalar-`value` case.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.arange[nm.i32](6)
a.put(nm.array[nm.int]("[0, 2]"), Scalar[nm.i32](99))
print(a)
# [99, 1, 99, 3, 4, 5]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `indices` (`NDArray[DType.int]`) `[imm]`: Linear (flat) indices into `self`. May be any shape.
    Negative indices are normalised (counted from the end).
- `value` (`Scalar[dtype]`) `[imm]`: Scalar value written to every selected position.

!!! failure "Raises"
    NumojoError: If any index is out of bounds for the flattened array.


</div>

<div class="fn-card" markdown="1">

#### `searchsorted`

<div class="overload-divider">Overload 1</div>

```mojo
def searchsorted(self, v: Self, side: String = "left") -> NDArray[DType.int]
```

Finds indices where elements of `v` should be inserted into `self` (assumed sorted, 1-D) to keep it sorted. Uses binary search.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.array[nm.i32]("[1, 3, 5, 7]")
print(a.searchsorted(nm.array[nm.i32]("[2, 6]")))
# [1, 3]
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `v` (`Self`) `[imm]`: Array of values to find insertion indices for.
- `side` (`String`) `[imm]`: `"left"` (default) returns the leftmost valid insertion
    index; `"right"` returns the rightmost.

<div class="prose-label">Returns</div>

- `NDArray[DType.int]`

!!! failure "Raises"
    NumojoError: If `self` is not 1-D.
NumojoError: If `side` is not `"left"` or `"right"`.

<div class="overload-divider">Overload 2</div>

```mojo
def searchsorted(self, v: Scalar[dtype], side: String = "left") -> Int
```

Finds the index where scalar `v` should be inserted into `self` (assumed sorted, 1-D) to keep it sorted.

This is a method ***OVERLOAD*** of `searchsorted` for a scalar `v`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

var a = nm.array[nm.i32]("[1, 3, 5, 7]")
print(a.searchsorted(Scalar[nm.i32](4)))
# 2
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `v` (`Scalar[dtype]`) `[imm]`: Scalar value to find the insertion index for.
- `side` (`String`) `[imm]`: `"left"` (default) returns the leftmost valid insertion
    index; `"right"` returns the rightmost.

<div class="prose-label">Returns</div>

- `Int`

!!! failure "Raises"
    NumojoError: If `self` is not 1-D.
NumojoError: If `side` is not `"left"` or `"right"`.


</div>

<div class="fn-card" markdown="1">

#### `fill`

```mojo
def fill(mut self, val: Scalar[dtype])
```

Fills all items of the array with the given value.

This method is offset- and stride-aware, so it correctly fills
both owned arrays and non-contiguous views.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `val` (`Scalar[dtype]`) `[imm]`: The value to fill.


</div>

<div class="fn-card" markdown="1">

#### `flatten`

```mojo
def flatten(self, order: String = "C") -> Self
```

Returns a copy of the array collapsed into one dimension.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `order` (`String`) `[imm]`: The order of the array.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `is_c_contiguous`

```mojo
def is_c_contiguous(self) -> Bool
```

Checks if the array is strictly C-contiguous (dense row-major).

A C-contiguous array has strides that exactly match a dense row-major
layout with no padding: `stride[-1] == 1` and each preceding stride
equals the product of the subsequent dimension sizes.

Computed from the current strides and shape (not cached flags),
so the result is always up-to-date.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f32](12).reshape(nm.Shape(3, 4))
print(a.is_c_contiguous())  # True
var v = a[0:3:1, 0:4:2]    # stride = (4, 2) → not C-contiguous
print(v.is_c_contiguous())  # False
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `is_f_contiguous`

```mojo
def is_f_contiguous(self) -> Bool
```

Checks if the array is strictly F-contiguous (dense column-major).

An F-contiguous array has strides that exactly match a dense
Fortran-style layout with no padding: `stride[0] == 1` and each
subsequent stride equals the product of the preceding dimension sizes.

Computed from the current strides and shape (not cached flags).

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f32](12).reshape(
    nm.Shape(3, 4), order="F"
)
print(a.is_f_contiguous())  # True
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `is_row_contiguous`

```mojo
def is_row_contiguous(self) -> Bool
```

Checks if elements within each row (last axis) are contiguous.

This is a relaxation of C-contiguous: only the innermost (last)
stride must be 1. Higher dimensions may have gaps (padding
between rows).

Hierarchy: `is_c_contiguous() → is_row_contiguous()` (but not
vice versa).

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f32](20).reshape(nm.Shape(4, 5))
print(a.is_row_contiguous())  # True (C-contiguous → row-contiguous)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `is_col_contiguous`

```mojo
def is_col_contiguous(self) -> Bool
```

Checks if elements within each column (first axis) are contiguous.

This is a relaxation of F-contiguous: only the outermost (first)
stride must be 1. Higher dimensions may have gaps (padding
between columns).

Hierarchy: `is_f_contiguous() → is_col_contiguous()` (but not
vice versa).

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f32](12).reshape(
    nm.Shape(3, 4), order="F"
)
print(a.is_col_contiguous())  # True
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `iter_along_axis`

```mojo
def iter_along_axis[forward: Bool = True](self, axis: Int, order: String = "C") -> _NDAxisIter[dtype, forward]
```

Returns an iterator yielding 1-D array slices along the given axis.

<div class="prose-label">Examples</div>

```mojo
from numojo.prelude import *
var a = nm.arange[i8](24).reshape(Shape(2, 3, 4))
print(a)
for i in a.iter_along_axis(axis=0):
    print(String(i))
```

This prints:

```console
[[[ 0  1  2  3]
[ 4  5  6  7]
[ 8  9 10 11]]
[[12 13 14 15]
[16 17 18 19]
[20 21 22 23]]]
3D-array  Shape(2,3,4)  Strides(12,4,1)  DType: i8  C-cont: True  F-cont: False  own data: True
[ 0 12]
[ 1 13]
[ 2 14]
[ 3 15]
[ 4 16]
[ 5 17]
[ 6 18]
[ 7 19]
[ 8 20]
[ 9 21]
[10 22]
[11 23]
```

Another example:

```mojo
from numojo.prelude import *
var a = nm.arange[i8](24).reshape(Shape(2, 3, 4))
print(a)
for i in a.iter_along_axis(axis=2):
    print(String(i))
```

This prints:

```console
[[[ 0  1  2  3]
[ 4  5  6  7]
[ 8  9 10 11]]
[[12 13 14 15]
[16 17 18 19]
[20 21 22 23]]]
3D-array  Shape(2,3,4)  Strides(12,4,1)  DType: i8  C-cont: True  F-cont: False  own data: True
[0 1 2 3]
[4 5 6 7]
[ 8  9 10 11]
[12 13 14 15]
[16 17 18 19]
[20 21 22 23]
```.

<div class="prose-label">Parameters</div>

- `forward` (`Bool`): If `True`, iterates from the beginning to the end. If
    `False`, iterates from the end to the beginning.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis by which the iteration is performed.
- `order` (`String`) `[imm]`: The order to traverse the array.

<div class="prose-label">Returns</div>

- `_NDAxisIter[dtype, forward]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound for the given array.


</div>

<div class="fn-card" markdown="1">

#### `iter_over_dimension`

```mojo
def iter_over_dimension[forward: Bool = True](self, dimension: Int) -> _NDArrayIter[origin_of(self), dtype, forward]
```

Returns an iterator yielding `ndim-1` arrays over the given dimension.

<div class="prose-label">Parameters</div>

- `forward` (`Bool`): If `True`, iterates from the beginning to the end. If
    `False`, iterates from the end to the beginning.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `dimension` (`Int`) `[imm]`: The dimension by which the iteration is performed.

<div class="prose-label">Returns</div>

- `_NDArrayIter[origin_of(self), dtype, forward]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound for the given array.


</div>

<div class="fn-card" markdown="1">

#### `max`

<div class="overload-divider">Overload 1</div>

```mojo
def max(self) -> Scalar[dtype]
```

Finds the max value of an array.

When no axis is given, the array is flattened before sorting.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def max(self, axis: Int) -> Self
```

Finds the max value of an array along the axis. The number of dimensions will be reduced by 1.

When no axis is given, the array is flattened before sorting.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis along which the max is performed.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `mean`

<div class="overload-divider">Overload 1</div>

```mojo
def mean[returned_dtype: DType = DType.float64](self) -> Scalar[returned_dtype]
```

Computes the mean of the array.

<div class="prose-label">Parameters</div>

- `returned_dtype` (`DType`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def mean[returned_dtype: DType = DType.float64](self, axis: Int) -> NDArray[returned_dtype]
```

Computes the mean of array elements over a given axis.

<div class="prose-label">Parameters</div>

- `returned_dtype` (`DType`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis along which the mean is performed.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `median`

<div class="overload-divider">Overload 1</div>

```mojo
def median[returned_dtype: DType = DType.float64](self) -> Scalar[returned_dtype]
```

Computes the median of the array.

<div class="prose-label">Parameters</div>

- `returned_dtype` (`DType`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def median[returned_dtype: DType = DType.float64](self, axis: Int) -> NDArray[returned_dtype]
```

Computes the median of array elements over a given axis.

<div class="prose-label">Parameters</div>

- `returned_dtype` (`DType`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis along which the median is performed.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `min`

<div class="overload-divider">Overload 1</div>

```mojo
def min(self) -> Scalar[dtype]
```

Finds the min value of an array.

When no axis is given, the array is flattened before sorting.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def min(self, axis: Int) -> Self
```

Finds the min value of an array along the axis. The number of dimensions will be reduced by 1.

When no axis is given, the array is flattened before sorting.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis along which the min is performed.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `nditer`

<div class="overload-divider">Overload 1</div>

```mojo
def nditer(self) -> _NDIter[DataContainer[dtype].origin, dtype]
```

Returns an iterator yielding the array elements according to the memory layout of the array.

***Overload*** of the `nditer(order)` method.

<div class="prose-label">Examples</div>

```console
>>>var a = nm.random.rand[i8](2, 3, min=0, max=100)
>>>print(a)
[[      37      8       25      ]
[      25      2       57      ]]
2-D array  (2,3)  DType: int8  C-cont: True  F-cont: False  own data: True
>>>for i in a.nditer():
...    print(i, end=" ")
37 8 25 25 2 57
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `_NDIter[DataContainer[dtype].origin, dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def nditer(self, order: String) -> _NDIter[DataContainer[dtype].origin, dtype]
```

Returns an iterator yielding the array elements according to the specified order.

<div class="prose-label">Examples</div>

```console
>>>var a = nm.random.rand[i8](2, 3, min=0, max=100)
>>>print(a)
[[      37      8       25      ]
[      25      2       57      ]]
2-D array  (2,3)  DType: int8  C-cont: True  F-cont: False  own data: True
>>>for i in a.nditer():
...    print(i, end=" ")
37 8 25 25 2 57
```.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `order` (`String`) `[imm]`: The order of the array.

<div class="prose-label">Returns</div>

- `_NDIter[DataContainer[dtype].origin, dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `prod`

<div class="overload-divider">Overload 1</div>

```mojo
def prod(self) -> Scalar[dtype]
```

Computes the product of all array elements.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def prod(self, axis: Int) -> Self
```

Computes the product of array elements over a given axis.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis along which the product is performed.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `reshape`

```mojo
def reshape(self, shape: NDArrayShape, order: String = "C") -> Self
```

Returns an array of the same data with a new shape.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `shape` (`NDArrayShape`) `[imm]`: The shape of the returned array.
- `order` (`String`) `[imm]`: The order of the array -- row major `C` or column major `F`.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `resize`

```mojo
def resize(mut self, shape: NDArrayShape)
```

Changes the shape and size of the array in-place.

<div class="prose-label">Notes</div>
To return a new array, use `reshape`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `shape` (`NDArrayShape`) `[imm]`: The shape after resize.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `round`

```mojo
def round(self) -> Self
```

Rounds the elements of the array to a whole number.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `row`

```mojo
def row(self, id: Int) -> Self
```

Gets the i-th row of the matrix.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `id` (`Int`) `[imm]`: The row index.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the ndim is greater than 2.


</div>

<div class="fn-card" markdown="1">

#### `sort`

```mojo
def sort(mut self, axis: Int = Int(-1), stable: Bool = False)
```

Sorts the array in-place along the given axis using quick sort. The default axis is -1. See `sorting.sort` for more information.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `axis` (`Int`) `[imm]`: The axis along which the array is sorted. Defaults to -1.
- `stable` (`Bool`) `[imm]`: If `True`, the sort is stable. Defaults to `False`.

!!! failure "Raises"
    NumojoError: If the axis is out of bound for the given array.


</div>

<div class="fn-card" markdown="1">

#### `std`

<div class="overload-divider">Overload 1</div>

```mojo
def std[returned_dtype: DType = DType.float64](self, ddof: Int = Int(0)) -> Scalar[returned_dtype]
```

Computes the standard deviation. See `numojo.std`.

<div class="prose-label">Parameters</div>

- `returned_dtype` (`DType`): The returned data type, defaulting to `float64`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `ddof` (`Int`) `[imm]`: The delta degree of freedom.

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def std[returned_dtype: DType = DType.float64](self, axis: Int, ddof: Int = Int(0)) -> NDArray[returned_dtype]
```

Computes the standard deviation along the axis. See `numojo.std`.

<div class="prose-label">Parameters</div>

- `returned_dtype` (`DType`): The returned data type, defaulting to `float64`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis along which the mean is performed.
- `ddof` (`Int`) `[imm]`: The delta degree of freedom.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `sum`

<div class="overload-divider">Overload 1</div>

```mojo
def sum(self) -> Scalar[dtype]
```

Returns the sum of all array elements.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def sum(self, axis: Int) -> Self
```

Computes the sum of array elements over a given axis.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis along which the sum is performed.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `T`

<div class="overload-divider">Overload 1</div>

```mojo
def T(self, axes: List[Int]) -> Self
```

Transposes the array of any number of dimensions according to an arbitrary permutation of the axes.

If `axes` is not given, it is equal to flipping the axes.

Defined in `manipulation.transpose`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axes` (`List[Int]`) `[imm]`: The list of axes.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def T(self) -> Self
```

Transposes the array when `axes` is not given.

***Overload*** If `axes` is not given, it is equal to flipping the axes.
See docstring of `transpose`.

Defined in `manipulation.transpose`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `tolist`

```mojo
def tolist(self) -> List[Scalar[dtype]]
```

Converts the NDArray to a 1-D list in row-major (C) order.

This method is offset- and stride-aware, so it correctly
handles both owned arrays and non-contiguous views.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `List[Scalar[dtype]]`


</div>

<div class="fn-card" markdown="1">

#### `to_numpy`

```mojo
def to_numpy(self) -> PythonObject
```

Converts the array to a NumPy array.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `PythonObject`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `trace`

```mojo
def trace(self, offset: Int = Int(0), axis1: Int = Int(0), axis2: Int = Int(1)) -> Self
```

Computes the trace of the ndarray.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `offset` (`Int`) `[imm]`: The offset of the diagonal from the main diagonal.
- `axis1` (`Int`) `[imm]`: The first axis.
- `axis2` (`Int`) `[imm]`: The second axis.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `unsafe_ptr`

```mojo
def unsafe_ptr[mutable: Bool, //, org: Origin[mut=mutable]](ref[mutable] self) -> Pointer[Scalar[dtype], org]
```

Retrieves the pointer to the logical start of the array data.

For views with a non-zero offset, this returns a pointer to
the first element of the view, not the start of the underlying
buffer.

<div class="prose-label">Parameters</div>

- `mutable` (`Bool`)
- `org` (`Origin[mut=mutable]`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`

<div class="prose-label">Returns</div>

- `Pointer[Scalar[dtype], org]`


</div>

<div class="fn-card" markdown="1">

#### `variance`

<div class="overload-divider">Overload 1</div>

```mojo
def variance[returned_dtype: DType = DType.float64](self, ddof: Int = Int(0)) -> Scalar[returned_dtype]
```

Returns the variance of the array.

<div class="prose-label">Parameters</div>

- `returned_dtype` (`DType`): The returned data type, defaulting to `float64`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `ddof` (`Int`) `[imm]`: The delta degree of freedom.

<div class="prose-label">Returns</div>

- `Scalar[returned_dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def variance[returned_dtype: DType = DType.float64](self, axis: Int, ddof: Int = Int(0)) -> NDArray[returned_dtype]
```

Returns the variance of the array along the axis. See `numojo.variance`.

<div class="prose-label">Parameters</div>

- `returned_dtype` (`DType`): The returned data type, defaulting to `float64`.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis along which the mean is performed.
- `ddof` (`Int`) `[imm]`: The delta degree of freedom.

<div class="prose-label">Returns</div>

- `NDArray[returned_dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

#### `squeeze`

```mojo
def squeeze(mut self, axis: Int)
```

Removes (squeezes) a single dimension of size 1 from the array shape.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `axis` (`Int`) `[imm]`: The axis to squeeze. Supports negative indices.

!!! failure "Raises"
    NumojoError: If the axis is out of range.
NumojoError: If the dimension at the given axis is not of size 1.


</div>
