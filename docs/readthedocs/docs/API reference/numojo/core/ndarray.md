# `numojo.core.ndarray`

NDArray (numojo.core.ndarray)

This module implements the core `NDArray` type, which is the fundamental data structure for multi-dimensional arrays in NuMojo.
It provides efficient storage, indexing, slicing, and basic operations on N-dimensional arrays. The `NDArray` is designed to be flexible and performant, supporting various memory layouts and data types.

SECTIONS OF THE FILE:
`NDArray` type
    1. Life cycle methods.
    2. Indexing and slicing (get and set dunders and relevant methods).
    3. Operator dunders.
    4. IO, trait, and iterator dunders.
    5. Other methods (Sorted alphabetically).

Iterators of `NDArray`:
    1. `_NDArrayIter` type
    2. `_NDAxisIter` type
    3. `_NDIter` type

## Aliases

### `IndexTypes`

```mojo
comptime IndexTypes
```

**Value:** `Variant[Int, NewAxis, EllipsisType, Slice]`

IndexTypes is used to represent the different kinds of indices that can be used for indexing and slicing operations on the NDArray.

## Structs

### `NDArray`

```mojo
struct NDArray[dtype: DType = DType.float64]
```

**Memory convention:** `memory_only`  
**Implements:** `Absable`, `AnyType`, `Copyable`, `FloatableRaising`, `ImplicitlyDestructible`, `IntableRaising`, `Movable`, `Representable`, `Sized`, `Stringable`, `Writable`

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

**Parameters:**

- `dtype` (`DType`): Type of item in NDArray. Default type is DType.float64.

#### Fields

- **`ndim`** (`Int`): Number of Dimensions.
- **`shape`** (`NDArrayShape`): Size and shape of NDArray.
- **`size`** (`Int`): Size of NDArray.
- **`strides`** (`NDArrayStrides`): Contains offset, strides.
- **`offset`** (`Int`): Offset of the first element in the data buffer.
- **`flags`** (`Flags`): Information about the memory layout of the array.
- **`print_options`** (`PrintOptions`): Per-instance print options (formerly global).

#### Aliases

##### `origin`

```mojo
comptime origin
```

**Value:** `MutExternalOrigin`

Origin of the data buffer.

##### `width`

```mojo
comptime width
```

**Value:** `simd_width_of[dtype]()`

Vector size of the data type.

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

**Value:** `False`

##### `__move_ctor_is_trivial`

```mojo
comptime __move_ctor_is_trivial
```

**Value:** `False`

##### `__copy_ctor_is_trivial`

```mojo
comptime __copy_ctor_is_trivial
```

**Value:** `False`

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
__init__(out self, shape: NDArrayShape, order: String = "C")
```

<span class="badge badge-static">static</span>

Initializes an NDArray with the given shape.

The memory is not filled with values.

Example:
```mojo
import numojo as nm
var a = nm.NDArray[nm.f32](
    nm.Shape(2, 3), order="C"
)
```

Note:
This constructor should not be used by users directly. Use factory
functions in `numojo.routines.creation` module instead.

**Args:**

- `shape` (`NDArrayShape`): The shape of the array.
- `order` (`String`): Memory order "C" or "F".
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
__init__(out self, shape: List[Int], strides: List[Int], offset: Int)
```

<span class="badge badge-static">static</span>

Initializes an NDArray with a specific shape, offset, and strides.

Notes:
- This constructor is intended for advanced use cases requiring
  precise control over memory layout.
- The resulting array is uninitialized and should be filled before
  use.

Example:
```mojo
from numojo.prelude import *
var shape = [2, 3]
var offset = 0
var strides = [3, 1]
var arr = NDArray[f32](
    shape, strides, offset
)
```

**Args:**

- `shape` (`List`): A list of integers specifying the shape of the array.
- `strides` (`List`): A list of integers specifying the stride for each
    dimension.
- `offset` (`Int`): The integer offset into the underlying buffer.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 3

```mojo
__init__(out self, shape: NDArrayShape, strides: NDArrayStrides, ndim: Int, size: Int, offset: Int, flags: Flags)
```

<span class="badge badge-static">static</span>

Initializes an NDArray with explicit shape, strides, number of dimensions, size, offset, and flags.

Creates an uninitialized NDArray with the provided properties. No
compatibility checks are performed between shape, strides, ndim, size,
offset, or flags. This allows construction of arrays with arbitrary
metadata, including 0-D arrays (scalars).

Notes:
- This constructor is intended for advanced or internal use cases
  requiring manual control.
- The resulting array is uninitialized; values must be set before
  use.
- No validation is performed on the consistency of the provided
  arguments.

**Args:**

- `shape` (`NDArrayShape`): The shape of the array.
- `strides` (`NDArrayStrides`): The strides for each dimension.
- `ndim` (`Int`): The number of dimensions.
- `size` (`Int`): The total number of elements.
- `offset` (`Int`): The offset of the first element in the data buffer.
- `flags` (`Flags`): The memory layout flags.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 4

```mojo
__init__(out self, var data: DataContainer[dtype], is_view: Bool, shape: NDArrayShape, strides: NDArrayStrides, offset: Int)
```

<span class="badge badge-static">static</span>

Initializes an NDArray as either an owning array or a non-owning view based on the provided DataContainer and the `is_view` flag.

Notes:
Ownership is determined by `is_view` and the DataContainer's reference count:
- If `is_view` is True and ref count is 1, the created NDArray will be a view and does not own the data.
- If `is_view` is False and ref count is 1, the NDArray owns the data. This is used to create deep copy of arrays.

**Args:**

- `data` (`DataContainer`) `[var]`: Reference-counted DataContainer holding array data.
- `is_view` (`Bool`): If True, creates a non-owning view; if False, owns the data i.e equivalent to deep copy.
- `shape` (`NDArrayShape`): Shape of the view.
- `strides` (`NDArrayStrides`): Strides for the view.
- `offset` (`Int`): Offset of the first element in the data buffer.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 5

```mojo
__init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

Copies `copy` into `self`.

Performs a deep copy. The new array owns its data.

**Args:**

- `copy` (`Self`): The NDArray to copy from.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 6

```mojo
__init__(out self, *, deinit take: Self)
```

<span class="badge badge-static">static</span>

Moves `take` into `self`.

**Args:**

- `take` (`Self`) `[deinit]`: The NDArray to move from.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__del__`

```mojo
__del__(deinit self)
```

Destroys all elements and frees memory.

**Args:**

- `self` (`Self`) `[deinit]`


</div>

<div class="fn-card" markdown="1">

##### `__bool__`

```mojo
__bool__(self) -> Bool
```

Returns `True` if all elements are truthy.

Examples:

```console
>>> import numojo
>>> var A = numojo.random.rand[numojo.i16](2, 2, 2)
>>> print(bool(A))
```.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`

!!! failure "Raises"
    Error: If the array is not 0-D or length-1.


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

###### Overload 1

```mojo
__getitem__(self) -> Scalar[dtype]
```

Gets the value of the 0-D array.

Examples:
```mojo
import numojo as nm
var a = nm.arange(3)[0]
print(a[])  # gets value of the 0-D array.
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"
    Error: If the array is not 0-D.

###### Overload 2

```mojo
__getitem__(self, index: Item) -> Scalar[dtype]
```

Gets the value at the index list.

Examples:

```console
>>>import numojo
>>>var a = numojo.arange(0, 10, 1).reshape(
...    numojo.Shape(2, 5)
...)
>>>print(a[Item(1, 2)])
```.

**Args:**

- `self` (`Self`)
- `index` (`Item`): The index list.

**Returns:**

- `Scalar`

!!! failure "Raises"
    Error: If the length of `index` does not match the number of
dimensions.
Error: If any of the index elements exceeds the size of the
dimension of the array.

###### Overload 3

```mojo
__getitem__(self, idx: Int) -> Self
```

Gets a single first-axis slice (first dimension).

Returns a slice of the array taken at the first (axis 0) position
specified by `idx`. The resulting array's dimensionality is reduced by
exactly one. If the source is 1-D, the result is a 0-D array (numojo
scalar wrapper). Negative indices are supported and are normalized
relative to the first dimension.

Notes:
Order preservation: The resulting copy preserves the source array's
memory order (C or F). Performance fast path: For C-contiguous
arrays the slice is a single contiguous block and is copied with one
`memcpy`. For F-contiguous or arbitrary strided layouts a unified
stride-based element loop is used. (Future enhancement: return a
non-owning view instead of copying.)

Example:
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

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The integer index along the first dimension. Accepts negative
    indices in the range `[-shape[0], shape[0])`.

**Returns:**

- `Self`

!!! failure "Raises"
    IndexError: If the array is 0-D (cannot slice a scalar).
IndexError: If `idx` is out of bounds after normalization.

###### Overload 4

```mojo
__getitem__(self, var *slices: Slice) -> Self
```

Retrieves a slice or sub-array from the current array using variadic slice arguments.

Notes:
- This method creates a new array; views are not currently
  supported.
- Negative indices and step sizes are supported as per standard
  slicing semantics.

Examples:
```mojo
import numojo as nm
var a = nm.arange[nm.f32](10).reshape(
    nm.Shape(2, 5)
)
var b = a[:, 2:4]
print(b)  # 2x2 sliced array
```

!!! info "Constraints"
    - The number of slices provided must not exceed the number of array
dimensions.
- Each slice must be valid for its corresponding dimension.

**Args:**

- `self` (`Self`)
- `*slices` (`Slice`) `[var]`: A variadic list of `Slice` objects, one for each dimension
    to be sliced.

**Returns:**

- `Self`

!!! failure "Raises"
    IndexError: If any slice is out of bounds for its corresponding
dimension.
ValueError: If the number of slices does not match the array's
dimensions.

###### Overload 5

```mojo
__getitem__(self, var slice_list: List[Slice], var index_type_list: List[IndexTypeInfo]) -> Self
```

Retrieves a sub-array from the current array using a list of slice objects, enabling advanced slicing operations across multiple dimensions.

Notes:
- This method supports advanced slicing similar to NumPy's
  multi-dimensional slicing.
- The returned array shares data with the original array if
  possible.

Example:
```mojo
import numojo as nm
var a = nm.arange(10).reshape(
    nm.Shape(2, 5)
)
var b = a[
    Slice(0, 2, 1), Slice(2, 4, 1)
]  # Equivalent to arr[:, 2:4].
print(b)
```

!!! info "Constraints"
    - The length of `slice_list` must not exceed the number of
dimensions in the array.
- Each `Slice` in `slice_list` must be valid for its respective
dimension.

**Args:**

- `self` (`Self`)
- `slice_list` (`List`) `[var]`: A list of `Slice` objects, where each `Slice` defines
    the start, stop, and step for the corresponding dimension.
- `index_type_list` (`List`) `[var]`: A list of `IndexTypeInfo` objects indicating the
    type of each index (slice, integer, newaxis, ellipsis).

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If `slice_list` is empty or contains invalid slices.

###### Overload 6

```mojo
__getitem__(self, *slices: Variant[Int, NewAxis, EllipsisType, Slice]) -> Self
```

Gets items of an NDArray with a series of either slices or integers.

Notes:
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
The user has to upack the 0-D array with the method`A.item(0)` to
get the corresponding number. This behavior is different from numpy
where the latter returns a number.

More examples for 1-D, 2-D, and 3-D arrays.

Examples:

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

**Args:**

- `self` (`Self`)
- `*slices` (`Variant`): A series of either `Slice` or `Int`.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the number of slices is greater than the number of
dimensions of the array.

###### Overload 7

```mojo
__getitem__(self, indices: NDArray[DType.int]) -> Self
```

Gets items from the 0-th dimension of an array by an array of indices.

If the original array is of shape `(i, j, k)` and the indices array is
of shape `(l, m, n)`, then the output array will be of shape `(l, m, n,
j, k)`.

Examples:

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

**Args:**

- `self` (`Self`)
- `indices` (`NDArray`): The array of indices.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the elements of indices are greater than the size of the
corresponding dimension of the array.

###### Overload 8

```mojo
__getitem__(self, indices: List[Int]) -> Self
```

Gets items from the 0-th dimension of an array by a list of integer indices.

Overloads `__getitem__(indices: NDArray[DType.int])`.

Examples:

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

**Args:**

- `self` (`Self`)
- `indices` (`List`): A list of `Int`.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the elements of indices are greater than the size of the
corresponding dimension of the array.

###### Overload 9

```mojo
__getitem__(self, mask: NDArray[DType.bool]) -> Self
```

Gets items from an array according to a boolean mask array.

If array shape equals mask shape, returns a flattened array of the
values where mask is `True`. If array shape does not equal mask shape,
returns items from the 0-th dimension of the array where mask is `True`.

Examples:

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

**Args:**

- `self` (`Self`)
- `mask` (`NDArray`): An NDArray with `DType.bool`.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the mask is not a 1-D array. Currently only 1-D mask
arrays are supported.

###### Overload 10

```mojo
__getitem__(self, mask: List[Bool]) -> Self
```

Gets items from the 0-th dimension of an array according to a boolean list mask.

Overloads `__getitem__(mask: NDArray[DType.bool])`.

Examples:

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

**Args:**

- `self` (`Self`)
- `mask` (`List`): A list of boolean values.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the mask is not a 1-D array. Currently only 1-D mask
arrays are supported.


</div>

<div class="fn-card" markdown="1">

##### `__setitem__`

###### Overload 1

```mojo
__setitem__(self, idx: Int, val: Self)
```

Assigns a single first-axis slice.

Replaces the sub-array at axis-0 position `idx` with `val`. The shape of
`val` must exactly match `self.shape[1:]` and its dimensionality must be
`self.ndim - 1`. Negative indices are supported. A fast contiguous
`memcpy` path is used for C-order source and destination; otherwise a
stride-based loop writes each element (works for F-order and arbitrary
layouts).

Notes:
Future work: broadcasting, zero-copy view assignment, and detection
of additional block-copy patterns in non-C-order layouts.

Examples:
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

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The index along the first dimension (supports negative values
    in `[-shape[0], shape[0])`).
- `val` (`Self`): The NDArray providing replacement data; shape must equal
    `self.shape[1:]`.

!!! failure "Raises"
    IndexError: Target array is 0-D or index out of bounds.
ValueError: `val.ndim != self.ndim - 1`.
ShapeError: `val.shape != self.shape[1:]`.

###### Overload 2

```mojo
__setitem__(mut self, var index: Item, val: Scalar[dtype])
```

Sets the value at the index list.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *
var A = numojo.random.rand[numojo.i16](2, 2, 2)
A[Item(0, 1, 1)] = 10
```

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`Item`) `[var]`: The index list.
- `val` (`Scalar`): The value to set.

!!! failure "Raises"
    Error: If the length of index does not match the number of
dimensions.
Error: If any of the indices is out of bound.

###### Overload 3

```mojo
__setitem__(mut self, mask: NDArray[DType.bool], value: Scalar[dtype])
```

Sets the value of the array at the indices where the mask is `True`.

Examples:

```console
>>> import numojo
>>> var A = numojo.random.rand[numojo.i16](2, 2, 2)
>>> var mask = A > 0.5
>>> A[mask] = 10
```.

**Args:**

- `self` (`Self`) `[mut]`
- `mask` (`NDArray`): The boolean mask array.
- `value` (`Scalar`): The value to set.

!!! failure "Raises"
    Error: If the mask and the array do not have the same shape.

###### Overload 4

```mojo
__setitem__(mut self, *slices: Slice, *, val: Self)
```

Sets the elements of the array at the slices with the given array.

Examples:

```console
>>> import numojo
>>> var A = numojo.random.rand[numojo.i16](2, 2, 2)
>>> A[1:3, 2:4] = numojo.random.rand[numojo.i16](2, 2)
```.

**Args:**

- `self` (`Self`) `[mut]`
- `*slices` (`Slice`): The variadic slices.
- `val` (`Self`): The NDArray to set.

!!! failure "Raises"
    Error: If the length of slices does not match the number of
dimensions.
Error: If any of the slices is out of bound.

###### Overload 5

```mojo
__setitem__(mut self, slices: List[Slice], val: Self)
```

Sets the slices of an array from a list of slices and an array.

Examples:

```console
>>> var a = nm.arange[i8](16).reshape(Shape(4, 4))
print(a)
[[      0       1       2       3       ]
 [      4       5       6       7       ]
 [      8       9       10      11      ]
 [      12      13      14      15      ]]
2-D array  Shape: [4, 4]  DType: int8  C-cont: True  F-cont: False  own data: True
>>> a[2:4, 2:4] = a[0:2, 0:2]
print(a)
[[      0       1       2       3       ]
 [      4       5       6       7       ]
 [      8       9       0       1       ]
 [      12      13      4       5       ]]
2-D array  Shape: [4, 4]  DType: int8  C-cont: True  F-cont: False  own data: True
```.

**Args:**

- `self` (`Self`) `[mut]`
- `slices` (`List`): The list of slices.
- `val` (`Self`): The value to set.

!!! failure "Raises"
    Error: If the length of slices does not match the number of
dimensions.
Error: If any of the slices is out of bound.

###### Overload 6

```mojo
__setitem__(mut self, *slices: Variant[Slice, Int], *, val: Self)
```

Sets items by a series of either slices or integers.

Examples:

```console
>>> var a = nm.arange[i8](16).reshape(Shape(4, 4))
print(a)
[[      0       1       2       3       ]
 [      4       5       6       7       ]
 [      8       9       10      11      ]
 [      12      13      14      15      ]]
2-D array  Shape: [4, 4]  DType: int8  C-cont: True  F-cont: False  own data: True
>>> a[0, Slice(2, 4)] = a[3, Slice(0, 2)]
print(a)
[[      0       1       12      13      ]
 [      4       5       6       7       ]
 [      8       9       10      11      ]
 [      12      13      14      15      ]]
2-D array  Shape: [4, 4]  DType: int8  C-cont: True  F-cont: False  own data: True
```.

**Args:**

- `self` (`Self`) `[mut]`
- `*slices` (`Variant`): The variadic slices or integers.
- `val` (`Self`): The value to set.

!!! failure "Raises"
    Error: If the length of slices does not match the number of
dimensions.
Error: If any of the slices is out of bound.

###### Overload 7

```mojo
__setitem__(mut self, index: NDArray[DType.int], val: Self)
```

Sets the items of the array from an array of indices.

Examples:

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

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`NDArray`): The array of indices.
- `val` (`Self`): The value to set.

!!! failure "Raises"

###### Overload 8

```mojo
__setitem__(mut self, mask: NDArray[DType.bool], val: Self)
```

Sets the value of the array at the indices where the mask is `True`.

Examples:

```console
>>> import numojo
>>> var A = numojo.random.rand[numojo.i16](2, 2, 2)
>>> var mask = A > 0.5
>>> A[mask] = 10
```.

**Args:**

- `self` (`Self`) `[mut]`
- `mask` (`NDArray`): The boolean mask array.
- `val` (`Self`): The value to set.

!!! failure "Raises"
    Error: If the mask and the array do not have the same shape.


</div>

<div class="fn-card" markdown="1">

##### `__neg__`

```mojo
__neg__(self) -> Self
```

Returns a negated copy of the array.

For boolean arrays, use `__invert__` (`~`).

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__pos__`

```mojo
__pos__(self) -> Self
```

Returns a positive copy of the array.

Does not accept boolean type arrays.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__invert__`

```mojo
__invert__(self) -> Self where dtype.is_integral() if dtype.is_integral() else (dtype == DType.bool)
```

Computes element-wise bitwise inversion.

Only works for boolean and integral types.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__lt__`

###### Overload 1

```mojo
__lt__(self, other: Scalar[dtype]) -> NDArray[DType.bool]
```

Computes itemwise less-than with a scalar.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): The other SIMD value to compare with.

**Returns:**

- `NDArray`

!!! failure "Raises"

###### Overload 2

```mojo
__lt__(self, other: Self) -> NDArray[DType.bool]
```

Computes itemwise less-than with an array.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The other array to compare with.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__le__`

###### Overload 1

```mojo
__le__(self, other: Scalar[dtype]) -> NDArray[DType.bool]
```

Computes itemwise less-than-or-equal-to with a scalar.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): The other SIMD value to compare with.

**Returns:**

- `NDArray`

!!! failure "Raises"

###### Overload 2

```mojo
__le__(self, other: Self) -> NDArray[DType.bool]
```

Computes itemwise less-than-or-equal-to with an array.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The other array to compare with.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

###### Overload 1

```mojo
__eq__(self, other: Self) -> NDArray[DType.bool]
```

Computes itemwise equality.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The other array to compare with.

**Returns:**

- `NDArray`

!!! failure "Raises"

###### Overload 2

```mojo
__eq__(self, other: Scalar[dtype]) -> NDArray[DType.bool]
```

Computes itemwise equality with a scalar.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): The other SIMD value to compare with.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

###### Overload 1

```mojo
__ne__(self, other: Scalar[dtype]) -> NDArray[DType.bool]
```

Computes itemwise inequality with a scalar.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): The other SIMD value to compare with.

**Returns:**

- `NDArray`

!!! failure "Raises"

###### Overload 2

```mojo
__ne__(self, other: Self) -> NDArray[DType.bool]
```

Computes itemwise inequality with an array.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The other array to compare with.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__gt__`

###### Overload 1

```mojo
__gt__(self, other: Scalar[dtype]) -> NDArray[DType.bool]
```

Computes itemwise greater-than with a scalar.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): The other SIMD value to compare with.

**Returns:**

- `NDArray`

!!! failure "Raises"

###### Overload 2

```mojo
__gt__(self, other: Self) -> NDArray[DType.bool]
```

Computes itemwise greater-than with an array.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The other array to compare with.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__ge__`

###### Overload 1

```mojo
__ge__(self, other: Scalar[dtype]) -> NDArray[DType.bool]
```

Computes itemwise greater-than-or-equal-to with a scalar.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): The other SIMD value to compare with.

**Returns:**

- `NDArray`

!!! failure "Raises"

###### Overload 2

```mojo
__ge__(self, other: Self) -> NDArray[DType.bool]
```

Computes itemwise greater-than-or-equal-to with an array.

**Args:**

- `self` (`Self`)
- `other` (`Self`): The other array to compare with.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__add__`

###### Overload 1

```mojo
__add__(self, other: Scalar[dtype]) -> Self
```

Enables `array + scalar`.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`)

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
__add__(self, other: Self) -> Self
```

Enables `array + array`.

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__sub__`

###### Overload 1

```mojo
__sub__(self, other: Scalar[dtype]) -> Self
```

Enables `array - scalar`.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`)

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
__sub__(self, other: Self) -> Self
```

Enables `array - array`.

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__mul__`

###### Overload 1

```mojo
__mul__(self, other: Scalar[dtype]) -> Self
```

Enables `array * scalar`.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`)

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
__mul__(self, other: Self) -> Self
```

Enables `array * array`.

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__matmul__`

```mojo
__matmul__(self, other: Self) -> Self
```

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__truediv__`

###### Overload 1

```mojo
__truediv__(self, other: Scalar[dtype]) -> Self
```

Enables `array / scalar`.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`)

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
__truediv__(self, other: Self) -> Self
```

Enables `array / array`.

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__floordiv__`

###### Overload 1

```mojo
__floordiv__(self, other: Scalar[dtype]) -> Self
```

Enables `array // scalar`.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`)

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
__floordiv__(self, other: Self) -> Self
```

Enables `array // array`.

**Args:**

- `self` (`Self`)
- `other` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__mod__`

###### Overload 1

```mojo
__mod__(mut self, other: Scalar[dtype]) -> Self
```

Enables `array % scalar`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`)

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
__mod__(mut self, other: Self) -> Self
```

Enables `array % array`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__pow__`

###### Overload 1

```mojo
__pow__(self, p: Int) -> Self
```

**Args:**

- `self` (`Self`)
- `p` (`Int`)

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
__pow__(self, rhs: Scalar[dtype]) -> Self
```

Computes element-wise power of items.

**Args:**

- `self` (`Self`)
- `rhs` (`Scalar`)

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 3

```mojo
__pow__(self, p: Self) -> Self
```

**Args:**

- `self` (`Self`)
- `p` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__radd__`

```mojo
__radd__(mut self, other: Scalar[dtype]) -> Self
```

Enables `scalar + array`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__rsub__`

```mojo
__rsub__(mut self, other: Scalar[dtype]) -> Self
```

Enables `scalar - array`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__rmul__`

```mojo
__rmul__(mut self, other: Scalar[dtype]) -> Self
```

Enables `scalar * array`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__rtruediv__`

```mojo
__rtruediv__(self, s: Scalar[dtype]) -> Self
```

Enables `scalar / array`.

**Args:**

- `self` (`Self`)
- `s` (`Scalar`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__rfloordiv__`

```mojo
__rfloordiv__(self, other: Scalar[dtype]) -> Self
```

Enables `scalar // array`.

**Args:**

- `self` (`Self`)
- `other` (`Scalar`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__rmod__`

```mojo
__rmod__(mut self, other: Scalar[dtype]) -> Self
```

Enables `scalar % array`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__iadd__`

###### Overload 1

```mojo
__iadd__(mut self, other: Scalar[dtype])
```

Enables `array += scalar`. View-safe: modifies buffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`)

!!! failure "Raises"

###### Overload 2

```mojo
__iadd__(mut self, other: Self)
```

Enables `array += array`. View-safe: modifies buffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`)

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__isub__`

###### Overload 1

```mojo
__isub__(mut self, other: Scalar[dtype])
```

Enables `array -= scalar`. View-safe: modifies buffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`)

!!! failure "Raises"

###### Overload 2

```mojo
__isub__(mut self, other: Self)
```

Enables `array -= array`. View-safe: modifies buffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`)

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__imul__`

###### Overload 1

```mojo
__imul__(mut self, other: Scalar[dtype])
```

Enables `array *= scalar`. View-safe: modifies buffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`)

!!! failure "Raises"

###### Overload 2

```mojo
__imul__(mut self, other: Self)
```

Enables `array *= array`. View-safe: modifies buffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`)

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__itruediv__`

###### Overload 1

```mojo
__itruediv__(mut self, s: Scalar[dtype])
```

Enables `array /= scalar`. View-safe: modifies buffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `s` (`Scalar`)

!!! failure "Raises"

###### Overload 2

```mojo
__itruediv__(mut self, other: Self)
```

Enables `array /= array`. View-safe: modifies buffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`)

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__ifloordiv__`

###### Overload 1

```mojo
__ifloordiv__(mut self, s: Scalar[dtype])
```

Enables `array //= scalar`. View-safe: modifies buffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `s` (`Scalar`)

!!! failure "Raises"

###### Overload 2

```mojo
__ifloordiv__(mut self, other: Self)
```

Enables `array //= array`. View-safe: modifies buffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`)

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__imod__`

###### Overload 1

```mojo
__imod__(mut self, other: Scalar[dtype])
```

Enables `array %= scalar`. View-safe: modifies buffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`)

!!! failure "Raises"

###### Overload 2

```mojo
__imod__(mut self, other: Self)
```

Enables `array %= array`. View-safe: modifies buffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`)

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__ipow__`

```mojo
__ipow__(mut self, p: Int)
```

Enables `array **= int`. View-safe: modifies buffer in-place.

**Args:**

- `self` (`Self`) `[mut]`
- `p` (`Int`)

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `deep_copy`

```mojo
deep_copy(self) -> Self
```

Create a deep copy of the NDArray.

Example:
```mojo
import numojo as nm
var arr = nm.ones[nm.f32](nm.Shape(2, 3))
var arr_copy = arr.deep_copy()
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `view`

```mojo
view(mut self) -> Self
```

Create a non-owning view of the current NDArray.

Example:
```mojo
import numojo as nm
var arr = nm.NDArray[nm.f32](nm.Shape(3, 4))
var v = arr.view()  # Create a view into arr
```

**Args:**

- `self` (`Self`) `[mut]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `normalize`

```mojo
normalize(self, idx: Int, dim: Int) -> Int
```

Normalizes a potentially negative index to its positive equivalent within the bounds of the given dimension.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The index to normalize. Can be negative to indicate indexing
    from the end (e.g., -1 refers to the last element).
- `dim` (`Int`): The size of the dimension to normalize against.

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `item`

###### Overload 1

```mojo
item(self, var index: Int) -> Scalar[dtype]
```

Returns the scalar at the given linear index.

If one index is given, gets the i-th item of the array (not buffer). It
first scans over the first row, even if it is a column-major array. If
more than one index is given, the length of the indices must match the
number of dimensions of the array. If the ndim is 0 (0-D array), gets
the value as a Mojo scalar.

Examples:

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

**Args:**

- `self` (`Self`)
- `index` (`Int`) `[var]`: The index of the item, counted in row-major order.

**Returns:**

- `Scalar`

!!! failure "Raises"
    Error: If the array is a 0-D array.
Error: If index is equal to or larger than the array size.

###### Overload 2

```mojo
item(self, *index: Int) -> Scalar[dtype]
```

Returns the scalar at the given coordinates.

If one index is given, gets the i-th item of the array (not buffer). It
first scans over the first row, even if it is a column-major array. If
more than one index is given, the length of the indices must match the
number of dimensions of the array. For 0-D array (numojo scalar),
returns the scalar value.

Examples:

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

**Args:**

- `self` (`Self`)
- `*index` (`Int`): The coordinates of the item.

**Returns:**

- `Scalar`

!!! failure "Raises"
    Error: If the number of indices is not equal to the number of
dimensions of the array.
Error: If the index is equal to or larger than the size of the
dimension.


</div>

<div class="fn-card" markdown="1">

##### `unsafe_load`

```mojo
unsafe_load[width: Int = 1](self, var index: Int) -> SIMD[dtype, width]
```

Unsafely retrieves the i-th item from the underlying buffer as a SIMD element of size `width`.

This method does not perform boundary checks. Use the `load` method for
safe retrieval.

**Parameters:**

- `width` (`Int`)

**Args:**

- `self` (`Self`)
- `index` (`Int`) `[var]`: The index of the item.

**Returns:**

- `SIMD`


</div>

<div class="fn-card" markdown="1">

##### `load`

###### Overload 1

```mojo
load(self, var index: Int) -> Scalar[dtype]
```

Safely retrieves the i-th item from the underlying buffer.

`A.load(i)` differs from `A._buf.ptr[i]` due to boundary check.

Examples:

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

**Args:**

- `self` (`Self`)
- `index` (`Int`) `[var]`: The index of the item.

**Returns:**

- `Scalar`

!!! failure "Raises"
    Error: If the index is out of bounds.

###### Overload 2

```mojo
load[width: Int = 1](self, var index: Int) -> SIMD[dtype, __result__.width]
```

Safely loads a SIMD element of size `width` at `index` from the underlying buffer.

To bypass boundary checks, use `self._buf.ptr.load` directly.

**Parameters:**

- `width` (`Int`)

**Args:**

- `self` (`Self`)
- `index` (`Int`) `[var]`: The index of the item.

**Returns:**

- `SIMD`

!!! failure "Raises"
    Error: If the index is out of boundary.

###### Overload 3

```mojo
load[width: Int = 1](self, *indices: Int) -> SIMD[dtype, __result__.width]
```

Safely loads a SIMD element of size `width` at given variadic indices from the underlying buffer.

To bypass boundary checks, use `self._buf.ptr.load` directly.

Examples:

```console
>>> import numojo
>>> var A = numojo.random.randn[numojo.f16](2, 2, 2)
>>> print(A.load(0, 1, 1))
```.

**Parameters:**

- `width` (`Int`)

**Args:**

- `self` (`Self`)
- `*indices` (`Int`): The variadic indices.

**Returns:**

- `SIMD`

!!! failure "Raises"
    Error: If the length of indices does not match the number of
dimensions.
Error: If any of the indices is out of bound.


</div>

<div class="fn-card" markdown="1">

##### `itemset`

###### Overload 1

```mojo
itemset(mut self, index: Int, item: Scalar[dtype])
```

Sets the scalar at the given coordinate.

Examples:

```
import numojo as nm
fn main() raises:
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

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`Int`): The coordinates of the item. It is the index of the
    i-th item of the whole array.
- `item` (`Scalar`): The scalar to be set.

!!! failure "Raises"
    Error: If the index is out of bound.
Error: If the length of index does not match the number of
dimensions.

###### Overload 2

```mojo
itemset(mut self, var indices: List[Int], item: Scalar[dtype])
```

Sets the scalar at the given coordinates.

Notes:
This is similar to `numpy.ndarray.itemset`. The difference is that
we take `List[Int]`, but NumPy takes a tuple.

Examples:

```
import numojo as nm
fn main() raises:
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

**Args:**

- `self` (`Self`) `[mut]`
- `indices` (`List`) `[var]`: The coordinates of the item.
- `item` (`Scalar`): The scalar to be set.

!!! failure "Raises"
    Error: If the index is out of bound.
Error: If the length of index does not match the number of
dimensions.


</div>

<div class="fn-card" markdown="1">

##### `unsafe_store`

```mojo
unsafe_store[width: Int = 1](mut self, index: Int, val: SIMD[dtype, val.width])
```

Unsafely stores a SIMD element to the i-th item of the underlying buffer.

`A.unsafe_store(i, a)` is equivalent to `A._buf.ptr.store(i, a)`. It
does not perform boundary check and is faster than `store`.

**Parameters:**

- `width` (`Int`)

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`Int`): The index of the item.
- `val` (`SIMD`): The value to store.


</div>

<div class="fn-card" markdown="1">

##### `store`

###### Overload 1

```mojo
store(self, var index: Int, val: Scalar[dtype])
```

Safely stores a scalar to the i-th item of the underlying buffer.

`A.store(i, a)` differs from `A._buf.ptr[i] = a` due to boundary check.

Examples:

```console
> array.store(15, val = 100)
```
Sets the item of index 15 of the array's data buffer to 100. Note that
it does not check against C-order or F-order.

**Args:**

- `self` (`Self`)
- `index` (`Int`) `[var]`: The index of the item.
- `val` (`Scalar`): The value to store.

!!! failure "Raises"
    Error: If the index is out of boundary.

###### Overload 2

```mojo
store[width: Int](mut self, index: Int, val: SIMD[dtype, val.width])
```

Safely stores a SIMD element of size `width` at `index` of the underlying buffer.

To bypass boundary checks, use `self._buf.ptr.store` directly.

Examples:

```console
> array.store(15, val = 100)
```
sets the item of index 15 of the array's data buffer to 100.

**Parameters:**

- `width` (`Int`)

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`Int`): The index of the item.
- `val` (`SIMD`): The value to store.

!!! failure "Raises"
    Error: If the index is out of boundary.

###### Overload 3

```mojo
store[width: Int = 1](mut self, *indices: Int, *, val: SIMD[dtype, val.width])
```

Safely stores a SIMD element of size `width` at given variadic indices of the underlying buffer.

To bypass boundary checks, use `self._buf.ptr.store` directly.

Examples:

```console
>>> import numojo
>>> var A = numojo.random.rand[numojo.i16](2, 2, 2)
>>> A.store(0, 1, 1, val=100)
```.

**Parameters:**

- `width` (`Int`)

**Args:**

- `self` (`Self`) `[mut]`
- `*indices` (`Int`): The variadic indices.
- `val` (`SIMD`): The value to store.

!!! failure "Raises"
    Error: If the index is out of boundary.


</div>

<div class="fn-card" markdown="1">

##### `__int__`

```mojo
__int__(self) -> Int
```

Gets `Int` representation of the array.

Only 0-D arrays or length-1 arrays can be converted to scalars.

Examples:

```console
> var A = NDArray[dtype](6, random=True)
> print(Int(A))

Unhandled exception caught during execution: Only 0-D arrays or length-1 arrays can be converted to scalars
mojo: error: execution exited with a non-zero result: 1

> var B = NDArray[dtype](1, 1, random=True)
> print(Int(B))
14
```.

**Args:**

- `self` (`Self`)

**Returns:**

- `Int`

!!! failure "Raises"
    Error: If the array is not 0-D or length-1.


</div>

<div class="fn-card" markdown="1">

##### `__float__`

```mojo
__float__(self) -> Float64
```

Gets `Float64` representation of the array.

Only 0-D arrays or length-1 arrays can be converted to scalars.

**Args:**

- `self` (`Self`)

**Returns:**

- `Float64`

!!! failure "Raises"
    Error: If the array is not 0-D or length-1.


</div>

<div class="fn-card" markdown="1">

##### `__abs__`

```mojo
__abs__(self) -> Self
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
__str__(self) -> String
```

Returns the string representation of the array.

Enables `String(array)`.

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `write_to`

```mojo
write_to[W: Writer](self, mut writer: W)
```

Writes the array to a writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`: The writer to write the array to.


</div>

<div class="fn-card" markdown="1">

##### `__repr__`

```mojo
__repr__(self) -> String
```

Computes the "official" string representation of the NDArray.

You can construct the array using this representation.

Examples:

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

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `__len__`

```mojo
__len__(self) -> Int
```

Returns the length of the 0-th dimension.

**Args:**

- `self` (`Self`)

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `__iter__`

```mojo
__iter__(self) -> _NDArrayIter[origin_of(self), dtype]
```

Iterates over elements of the NDArray and returns sub-arrays as views.

Examples:

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

**Args:**

- `self` (`Self`)

**Returns:**

- `_NDArrayIter`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__reversed__`

```mojo
__reversed__(self) -> _NDArrayIter[origin_of(self), dtype, False]
```

Iterates backwards over elements of the NDArray, returning copied values.

**Args:**

- `self` (`Self`)

**Returns:**

- `_NDArrayIter`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `all`

```mojo
all(self) -> Bool where (dtype == DType.bool) if (dtype == DType.bool)._mlir_value else dtype.is_integral()
```

Returns `True` if all elements are truthy.

This method is offset and stride-aware via `contiguous()`.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`

!!! failure "Raises"
    Error: If the array elements are not Boolean or Integer.


</div>

<div class="fn-card" markdown="1">

##### `any`

```mojo
any(self) -> Bool where (dtype == DType.bool) if (dtype == DType.bool)._mlir_value else dtype.is_integral()
```

Returns `True` if any element is truthy.

This method is offset- and stride-aware via `contiguous()`.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`

!!! failure "Raises"
    Error: If the array elements are not Boolean or Integer.


</div>

<div class="fn-card" markdown="1">

##### `argmax`

###### Overload 1

```mojo
argmax(self) -> Scalar[DType.int]
```

Returns the indices of the maximum values along an axis. When no axis is specified, the array is flattened. See `numojo.argmax()` for more details.

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
argmax(self, axis: Int) -> NDArray[DType.int]
```

Returns the indices of the maximum values along an axis. See `numojo.argmax()` for more details.

**Args:**

- `self` (`Self`)
- `axis` (`Int`)

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `argmin`

###### Overload 1

```mojo
argmin(self) -> Scalar[DType.int]
```

Returns the indices of the minimum values along an axis. When no axis is specified, the array is flattened. See `numojo.argmin()` for more details.

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
argmin(self, axis: Int) -> NDArray[DType.int]
```

Returns the indices of the minimum values along an axis. See `numojo.argmin()` for more details.

**Args:**

- `self` (`Self`)
- `axis` (`Int`)

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `argsort`

###### Overload 1

```mojo
argsort(mut self) -> NDArray[DType.int]
```

Sorts the NDArray and returns the sorted indices. See `numojo.argsort()` for more details.

**Args:**

- `self` (`Self`) `[mut]`

**Returns:**

- `NDArray`

!!! failure "Raises"

###### Overload 2

```mojo
argsort(mut self, axis: Int) -> NDArray[DType.int]
```

Sorts the NDArray and returns the sorted indices. See `numojo.argsort()` for more details.

**Args:**

- `self` (`Self`) `[mut]`
- `axis` (`Int`)

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `astype`

```mojo
astype[target: DType](self) -> NDArray[target]
```

Converts the type of the array.

**Parameters:**

- `target` (`DType`): The target data type.

**Args:**

- `self` (`Self`)

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `clip`

```mojo
clip(self, a_min: Scalar[dtype], a_max: Scalar[dtype]) -> Self
```

Limits the values in an array between `[a_min, a_max]`.

If `a_min` is greater than `a_max`, the value is equal to `a_max`. See
`numojo.clip()` for more details.

**Args:**

- `self` (`Self`)
- `a_min` (`Scalar`): The minimum value.
- `a_max` (`Scalar`): The maximum value.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `compress`

###### Overload 1

```mojo
compress(self, condition: NDArray[DType.bool], axis: Int) -> Self
```

Returns selected slices of an array along a given axis.

If no axis is provided, the array is flattened before use.

**Args:**

- `self` (`Self`)
- `condition` (`NDArray`): A 1-D array of booleans that selects which entries to
    return. If length of condition is less than the size of the
    array along the given axis, then output is filled to the length
    of the condition with `False`.
- `axis` (`Int`): The axis along which to take slices.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the axis is out of bound for the given array.
Error: If the condition is not a 1-D array.
Error: If the condition length is out of bound for the given axis.
Error: If the condition contains no `True` values.

###### Overload 2

```mojo
compress(self, condition: NDArray[DType.bool]) -> Self
```

Returns selected slices of an array along a given axis.

If no axis is provided, the array is flattened before use. This is a
function ***OVERLOAD***.

**Args:**

- `self` (`Self`)
- `condition` (`NDArray`): A 1-D array of booleans that selects which entries to
    return. If length of condition is less than the size of the
    array along the given axis, then output is filled to the length
    of the condition with `False`.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the condition is not a 1-D array.
Error: If the condition length is out of bound for the given axis.
Error: If the condition contains no `True` values.


</div>

<div class="fn-card" markdown="1">

##### `contiguous`

```mojo
contiguous(self) -> Self
```

Returns a new C-contiguous array owning a copy of the data.

Always creates a new owned array, even if the source is already
C-contiguous. This ensures consistent behavior: the caller can
always assume the result is independent of the source.

For the already-contiguous fast path, data is copied with a single
`memcpy`. For non-contiguous views, a stride-aware element-by-element
copy is performed.

Example:
```mojo
import numojo as nm
var a = nm.arange[nm.f32](24).reshape(nm.Shape(2, 3, 4))
var v = a[0:2:1, 0:3:2]  # non-contiguous view
var c = v.contiguous()    # new C-contiguous owned copy
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `col`

```mojo
col(self, id: Int) -> Self
```

Gets the i-th column of the matrix.

**Args:**

- `self` (`Self`)
- `id` (`Int`): The column index.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `cumprod`

###### Overload 1

```mojo
cumprod(self) -> Self
```

Returns the cumulative product of all items of an array. The array is flattened before computation.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
cumprod(self, axis: Int) -> Self
```

Returns the cumulative product of the array along the given axis.

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `cumsum`

###### Overload 1

```mojo
cumsum(self) -> Self
```

Returns the cumulative sum of all items of an array. The array is flattened before computation.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
cumsum(self, axis: Int) -> Self
```

Returns the cumulative sum of the array along the given axis.

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `diagonal`

```mojo
diagonal(self, offset: Int = 0) -> Self
```

Returns specific diagonals.

Currently supports only 2D arrays.

**Args:**

- `self` (`Self`)
- `offset` (`Int`): The offset of the diagonal from the main diagonal.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the array is not 2D.
Error: If the offset is beyond the shape of the array.


</div>

<div class="fn-card" markdown="1">

##### `fill`

```mojo
fill(mut self, val: Scalar[dtype])
```

Fills all items of the array with the given value.

This method is offset- and stride-aware, so it correctly fills
both owned arrays and non-contiguous views.

**Args:**

- `self` (`Self`) `[mut]`
- `val` (`Scalar`): The value to fill.


</div>

<div class="fn-card" markdown="1">

##### `flatten`

```mojo
flatten(self, order: String = "C") -> Self
```

Returns a copy of the array collapsed into one dimension.

**Args:**

- `self` (`Self`)
- `order` (`String`): The order of the array.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `is_c_contiguous`

```mojo
is_c_contiguous(self) -> Bool
```

Checks if the array is strictly C-contiguous (dense row-major).

A C-contiguous array has strides that exactly match a dense row-major
layout with no padding: `stride[-1] == 1` and each preceding stride
equals the product of the subsequent dimension sizes.

Computed from the current strides and shape (not cached flags),
so the result is always up-to-date.

Example:
```mojo
import numojo as nm
var a = nm.arange[nm.f32](12).reshape(nm.Shape(3, 4))
print(a.is_c_contiguous())  # True
var v = a[0:3:1, 0:4:2]    # stride = (4, 2) → not C-contiguous
print(v.is_c_contiguous())  # False
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_f_contiguous`

```mojo
is_f_contiguous(self) -> Bool
```

Checks if the array is strictly F-contiguous (dense column-major).

An F-contiguous array has strides that exactly match a dense
Fortran-style layout with no padding: `stride[0] == 1` and each
subsequent stride equals the product of the preceding dimension sizes.

Computed from the current strides and shape (not cached flags).

Example:
```mojo
import numojo as nm
var a = nm.arange[nm.f32](12).reshape(
    nm.Shape(3, 4), order="F"
)
print(a.is_f_contiguous())  # True
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_row_contiguous`

```mojo
is_row_contiguous(self) -> Bool
```

Checks if elements within each row (last axis) are contiguous.

This is a relaxation of C-contiguous: only the innermost (last)
stride must be 1. Higher dimensions may have gaps (padding
between rows).

Hierarchy: `is_c_contiguous() → is_row_contiguous()` (but not
vice versa).

Example:
```mojo
import numojo as nm
var a = nm.arange[nm.f32](20).reshape(nm.Shape(4, 5))
print(a.is_row_contiguous())  # True (C-contiguous → row-contiguous)
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_col_contiguous`

```mojo
is_col_contiguous(self) -> Bool
```

Checks if elements within each column (first axis) are contiguous.

This is a relaxation of F-contiguous: only the outermost (first)
stride must be 1. Higher dimensions may have gaps (padding
between columns).

Hierarchy: `is_f_contiguous() → is_col_contiguous()` (but not
vice versa).

Example:
```mojo
import numojo as nm
var a = nm.arange[nm.f32](12).reshape(
    nm.Shape(3, 4), order="F"
)
print(a.is_col_contiguous())  # True
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `iter_along_axis`

```mojo
iter_along_axis[forward: Bool = True](self, axis: Int, order: String = "C") -> _NDAxisIter[dtype, forward]
```

Returns an iterator yielding 1-D array slices along the given axis.

Examples:

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

**Parameters:**

- `forward` (`Bool`): If `True`, iterates from the beginning to the end. If
    `False`, iterates from the end to the beginning.

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis by which the iteration is performed.
- `order` (`String`): The order to traverse the array.

**Returns:**

- `_NDAxisIter`

!!! failure "Raises"
    Error: If the axis is out of bound for the given array.


</div>

<div class="fn-card" markdown="1">

##### `iter_over_dimension`

```mojo
iter_over_dimension[forward: Bool = True](self, dimension: Int) -> _NDArrayIter[origin_of(self), dtype, forward]
```

Returns an iterator yielding `ndim-1` arrays over the given dimension.

**Parameters:**

- `forward` (`Bool`): If `True`, iterates from the beginning to the end. If
    `False`, iterates from the end to the beginning.

**Args:**

- `self` (`Self`)
- `dimension` (`Int`): The dimension by which the iteration is performed.

**Returns:**

- `_NDArrayIter`

!!! failure "Raises"
    Error: If the axis is out of bound for the given array.


</div>

<div class="fn-card" markdown="1">

##### `max`

###### Overload 1

```mojo
max(self) -> Scalar[dtype]
```

Finds the max value of an array.

When no axis is given, the array is flattened before sorting.

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
max(self, axis: Int) -> Self
```

Finds the max value of an array along the axis. The number of dimensions will be reduced by 1.

When no axis is given, the array is flattened before sorting.

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which the max is performed.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `mean`

###### Overload 1

```mojo
mean[returned_dtype: DType = DType.float64](self) -> Scalar[returned_dtype]
```

Computes the mean of the array.

**Parameters:**

- `returned_dtype` (`DType`)

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
mean[returned_dtype: DType = DType.float64](self, axis: Int) -> NDArray[returned_dtype]
```

Computes the mean of array elements over a given axis.

**Parameters:**

- `returned_dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which the mean is performed.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `median`

###### Overload 1

```mojo
median[returned_dtype: DType = DType.float64](self) -> Scalar[returned_dtype]
```

Computes the median of the array.

**Parameters:**

- `returned_dtype` (`DType`)

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
median[returned_dtype: DType = DType.float64](self, axis: Int) -> NDArray[returned_dtype]
```

Computes the median of array elements over a given axis.

**Parameters:**

- `returned_dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which the median is performed.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `min`

###### Overload 1

```mojo
min(self) -> Scalar[dtype]
```

Finds the min value of an array.

When no axis is given, the array is flattened before sorting.

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
min(self, axis: Int) -> Self
```

Finds the min value of an array along the axis. The number of dimensions will be reduced by 1.

When no axis is given, the array is flattened before sorting.

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which the min is performed.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `nditer`

###### Overload 1

```mojo
nditer(self) -> _NDIter[origin_of(self), dtype]
```

Returns an iterator yielding the array elements according to the memory layout of the array.

***Overload*** of the `nditer(order)` method.

Examples:

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

**Args:**

- `self` (`Self`)

**Returns:**

- `_NDIter`

!!! failure "Raises"

###### Overload 2

```mojo
nditer(self, order: String) -> _NDIter[origin_of(self), dtype]
```

Returns an iterator yielding the array elements according to the specified order.

Examples:

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

**Args:**

- `self` (`Self`)
- `order` (`String`): The order of the array.

**Returns:**

- `_NDIter`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `prod`

###### Overload 1

```mojo
prod(self) -> Scalar[dtype]
```

Computes the product of all array elements.

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
prod(self, axis: Int) -> Self
```

Computes the product of array elements over a given axis.

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which the product is performed.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `reshape`

```mojo
reshape(self, shape: NDArrayShape, order: String = "C") -> Self
```

Returns an array of the same data with a new shape.

**Args:**

- `self` (`Self`)
- `shape` (`NDArrayShape`): The shape of the returned array.
- `order` (`String`): The order of the array -- row major `C` or column major `F`.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `resize`

```mojo
resize(mut self, shape: NDArrayShape)
```

Changes the shape and size of the array in-place.

Notes:
To return a new array, use `reshape`.

**Args:**

- `self` (`Self`) `[mut]`
- `shape` (`NDArrayShape`): The shape after resize.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `round`

```mojo
round(self) -> Self
```

Rounds the elements of the array to a whole number.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `row`

```mojo
row(self, id: Int) -> Self
```

Gets the i-th row of the matrix.

**Args:**

- `self` (`Self`)
- `id` (`Int`): The row index.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the ndim is greater than 2.


</div>

<div class="fn-card" markdown="1">

##### `sort`

```mojo
sort(mut self, axis: Int = -1, stable: Bool = False)
```

Sorts the array in-place along the given axis using quick sort. The default axis is -1. See `numojo.sorting.sort` for more information.

**Args:**

- `self` (`Self`) `[mut]`
- `axis` (`Int`): The axis along which the array is sorted. Defaults to -1.
- `stable` (`Bool`): If `True`, the sort is stable. Defaults to `False`.

!!! failure "Raises"
    Error: If the axis is out of bound for the given array.


</div>

<div class="fn-card" markdown="1">

##### `std`

###### Overload 1

```mojo
std[returned_dtype: DType = DType.float64](self, ddof: Int = 0) -> Scalar[returned_dtype]
```

Computes the standard deviation. See `numojo.std`.

**Parameters:**

- `returned_dtype` (`DType`): The returned data type, defaulting to `float64`.

**Args:**

- `self` (`Self`)
- `ddof` (`Int`): The delta degree of freedom.

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
std[returned_dtype: DType = DType.float64](self, axis: Int, ddof: Int = 0) -> NDArray[returned_dtype]
```

Computes the standard deviation along the axis. See `numojo.std`.

**Parameters:**

- `returned_dtype` (`DType`): The returned data type, defaulting to `float64`.

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which the mean is performed.
- `ddof` (`Int`): The delta degree of freedom.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `sum`

###### Overload 1

```mojo
sum(self) -> Scalar[dtype]
```

Returns the sum of all array elements.

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
sum(self, axis: Int) -> Self
```

Computes the sum of array elements over a given axis.

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which the sum is performed.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `T`

###### Overload 1

```mojo
T(self, axes: List[Int]) -> Self
```

Transposes the array of any number of dimensions according to an arbitrary permutation of the axes.

If `axes` is not given, it is equal to flipping the axes.

Defined in `numojo.routines.manipulation.transpose`.

**Args:**

- `self` (`Self`)
- `axes` (`List`): The list of axes.

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
T(self) -> Self
```

Transposes the array when `axes` is not given.

***Overload*** If `axes` is not given, it is equal to flipping the axes.
See docstring of `transpose`.

Defined in `numojo.routines.manipulation.transpose`.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `tolist`

```mojo
tolist(self) -> List[Scalar[dtype]]
```

Converts the NDArray to a 1-D list in row-major (C) order.

This method is offset- and stride-aware, so it correctly
handles both owned arrays and non-contiguous views.

**Args:**

- `self` (`Self`)

**Returns:**

- `List`


</div>

<div class="fn-card" markdown="1">

##### `to_numpy`

```mojo
to_numpy(self) -> PythonObject
```

Converts the array to a NumPy array.

**Args:**

- `self` (`Self`)

**Returns:**

- `PythonObject`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `trace`

```mojo
trace(self, offset: Int = 0, axis1: Int = 0, axis2: Int = 1) -> Self
```

Computes the trace of the ndarray.

**Args:**

- `self` (`Self`)
- `offset` (`Int`): The offset of the diagonal from the main diagonal.
- `axis1` (`Int`): The first axis.
- `axis2` (`Int`): The second axis.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `unsafe_ptr`

```mojo
unsafe_ptr(ref self) -> UnsafePointer[Scalar[dtype], MutAnyOrigin]
```

Retrieves the pointer to the logical start of the array data.

For views with a non-zero offset, this returns a pointer to
the first element of the view, not the start of the underlying
buffer.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `UnsafePointer`


</div>

<div class="fn-card" markdown="1">

##### `variance`

###### Overload 1

```mojo
variance[returned_dtype: DType = DType.float64](self, ddof: Int = 0) -> Scalar[returned_dtype]
```

Returns the variance of the array.

**Parameters:**

- `returned_dtype` (`DType`): The returned data type, defaulting to `float64`.

**Args:**

- `self` (`Self`)
- `ddof` (`Int`): The delta degree of freedom.

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
variance[returned_dtype: DType = DType.float64](self, axis: Int, ddof: Int = 0) -> NDArray[returned_dtype]
```

Returns the variance of the array along the axis. See `numojo.variance`.

**Parameters:**

- `returned_dtype` (`DType`): The returned data type, defaulting to `float64`.

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which the mean is performed.
- `ddof` (`Int`): The delta degree of freedom.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `squeeze`

```mojo
squeeze(mut self, axis: Int)
```

Removes (squeezes) a single dimension of size 1 from the array shape.

**Args:**

- `self` (`Self`) `[mut]`
- `axis` (`Int`): The axis to squeeze. Supports negative indices.

!!! failure "Raises"
    IndexError: If the axis is out of range.
ShapeError: If the dimension at the given axis is not of size 1.


</div>
