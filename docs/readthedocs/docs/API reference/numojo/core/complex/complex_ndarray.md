# `numojo.core.complex.complex_ndarray`

Multi-dimensional arrays of complex numbers.

N-dimensional arrays of complex numbers with full indexing, slicing, and
operations. Includes lifecycle methods, operators, I/O, and iterators.

Exports
-------
- `ComplexNDArray`: Complex-valued N-dimensional array type.

Notes:
    Structure of the ComplexNDArray implementation:
    - Lifecycle methods (construction, initialization)
    - Indexing and slicing (getters, setters, dunder methods)
    - Operator overloads (arithmetic, comparison, etc.)
    - I/O, trait, and iterator dunders
    - Other methods (sorted alphabetically)

## Structs

### `ComplexNDArray`

```mojo
struct ComplexNDArray[cdtype: ComplexDType = ComplexDType.float64]
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `FloatableRaising`, `IntableRaising`, `Movable`, `Sized`, `Writable`

N-dimensional Complex array.

ComplexNDArray represents an N-dimensional array whose elements are complex numbers, supporting efficient storage, indexing, and mathematical operations. Each element consists of a real and imaginary part, stored in separate buffers.

Attributes:
    - _re: NDArray[Self.dtype]
        Buffer for real parts.
    - _im: NDArray[Self.dtype]
        Buffer for imaginary parts.
    - ndim: Int
        Number of dimensions.
    - shape: NDArrayShape
        Shape of the array.
    - size: Int
        Total number of elements.
    - strides: NDArrayStrides
        Stride information for each dimension.
    - flags: Flags
        Memory layout information.
    - print_options: PrintOptions
        Formatting options for display.

Notes:
- The array is uniquely defined by its data buffers, shape, strides, and element datatype.
- Supports both row-major (C) and column-major (F) memory order.
- Provides rich indexing, slicing, and broadcasting semantics.
- ComplexNDArray should be created using factory functions in `nomojo.routines.creation` module for convenience.

**Parameters:**

- `cdtype` (`ComplexDType`): The complex data type of the array elements (default: ComplexDType.float64).

#### Fields

- **`ndim`** (`Int`): Number of Dimensions.
- **`shape`** (`NDArrayShape`): Size and shape of ComplexNDArray.
- **`size`** (`Int`): Size of ComplexNDArray.
- **`strides`** (`NDArrayStrides`): Contains offset, strides.
- **`flags`** (`Flags`): Information about the memory layout of the array.
- **`print_options`** (`PrintOptions`): Per-instance print options (formerly global).

#### Aliases

##### `dtype`

```mojo
comptime dtype
```

**Value:** `cdtype.dtype`

Corresponding real data type.

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

###### Overload 1

```mojo
def __init__(out self, var re: NDArray[Self.dtype], var im: NDArray[Self.dtype])
```

<span class="badge badge-static">static</span>

Initialize a ComplexNDArray with given real and imaginary parts.

**Args:**

- `re` (`NDArray[Self.dtype]`) `[var]`: Real part of the complex array.
- `im` (`NDArray[Self.dtype]`) `[var]`: Imaginary part of the complex array.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def __init__(out self, shape: NDArrayShape, order: String = "C")
```

<span class="badge badge-static">static</span>

Initialize a ComplexNDArray with given shape. The memory is not filled with values.

Example:
```mojo
from numojo.prelude import *
var A = nm.ComplexNDArray[cf32](Shape(2,3,4))
```

Notes:
This constructor should not be used by users directly. Use factory functions in `numojo.routines.creation` module instead.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: Variadic shape.
- `order` (`String`) `[imm]`: Memory order C or F.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 3

```mojo
def __init__(out self, shape: List[Int], order: String = "C")
```

<span class="badge badge-static">static</span>

(Overload) Initialize a ComplexNDArray with given shape (list of integers).

Example:
```mojo
from numojo.prelude import *
var A = nm.ComplexNDArray[cf32]([2,3,4])
```

Notes:
This constructor should not be used by users directly. Use factory functions in `numojo.routines.creation` module instead.

**Args:**

- `shape` (`List[Int]`) `[imm]`: List of shape.
- `order` (`String`) `[imm]`: Memory order C or F.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 4

```mojo
def __init__(out self, shape: VariadicList[Int], order: String = "C")
```

<span class="badge badge-static">static</span>

(Overload) Initialize a ComplexNDArray with given shape (variadic list of integers).

Example:
```mojo
from numojo.prelude import *
var A = nm.ComplexNDArray[cf32](2,3,4)
```

Notes:
This constructor should not be used by users directly. Use factory functions in `numojo.routines.creation` module instead.

**Args:**

- `shape` (`VariadicList[Int]`) `[imm]`: Variadic List of shape.
- `order` (`String`) `[imm]`: Memory order C or F.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 5

```mojo
def __init__(out self, shape: List[Int], offset: Int, strides: List[Int])
```

<span class="badge badge-static">static</span>

Initialize a ComplexNDArray with a specific shape, offset, and strides.

Example:
```mojo
from numojo.prelude import *
var shape = [2, 3]
var offset = 0
var strides = [3, 1]
var arr = ComplexNDArray[cf32](shape, offset, strides)
```

Notes:
- This constructor is intended for advanced use cases requiring precise control over memory layout.
- The resulting array is uninitialized and should be filled before use.
- Both real and imaginary buffers are created with the same shape, offset, and strides.

**Args:**

- `shape` (`List[Int]`) `[imm]`: List of integers specifying the shape of the array.
- `offset` (`Int`) `[imm]`: Integer offset into the underlying buffer.
- `strides` (`List[Int]`) `[imm]`: List of integers specifying the stride for each dimension.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 6

```mojo
def __init__(out self, shape: NDArrayShape, strides: NDArrayStrides, ndim: Int, size: Int, flags: Flags)
```

<span class="badge badge-static">static</span>

Initialize a ComplexNDArray with explicit shape, strides, number of dimensions, size, and flags. This constructor creates an uninitialized ComplexNDArray with the provided properties. No compatibility checks are performed between shape, strides, ndim, size, or flags. This allows construction of arrays with arbitrary metadata, including 0-D arrays (scalars).

Notes:
- This constructor is intended for advanced or internal use cases requiring manual control.
- The resulting array is uninitialized; values must be set before use.
- No validation is performed on the consistency of the provided arguments.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: Shape of the array.
- `strides` (`NDArrayStrides`) `[imm]`: Strides for each dimension.
- `ndim` (`Int`) `[imm]`: Number of dimensions.
- `size` (`Int`) `[imm]`: Total number of elements.
- `flags` (`Flags`) `[imm]`: Memory layout flags.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 7

```mojo
def __init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

Copy copy into self.

**Args:**

- `copy` (`Self`) `[imm]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 8

```mojo
def __init__(out self, *, deinit move: Self)
```

<span class="badge badge-static">static</span>

Move other into self.

**Args:**

- `move` (`Self`) `[deinit]`
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__deinit__`

```mojo
def __deinit__(deinit self)
```

Destroys array buffers.

**Args:**

- `self` (`Self`) `[deinit]`


</div>

<div class="fn-card" markdown="1">

##### `__bool__`

```mojo
def __bool__(self) -> Bool
```

Check if the complex array is non-zero.

For a 0-D or length-1 complex array, returns True if the complex number
is non-zero (i.e., either real or imaginary part is non-zero).

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape())  # 0-D array
A._re.unsafe_set(0, 1.0)
A._im.unsafe_set(0, 0.0)
var result = A.__bool__()  # True
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`

!!! failure "Raises"
    NumojoError: If the array is not 0-D or length-1.


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

###### Overload 1

```mojo
def __getitem__(self) -> ComplexSIMD[cdtype]
```

Gets the value of the 0-D Complex array.

Examples:
```mojo
import numojo as nm
from numojo.prelude import *
var a = nm.arange[cf32](CScalar[cf32](1))[0]
print(a[]) # gets values of the 0-D complex array.
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `ComplexSIMD[cdtype]`

!!! failure "Raises"
    NumojoError: If the array is not 0-d.

###### Overload 2

```mojo
def __getitem__(self, index: Item) -> ComplexSIMD[cdtype]
```

Get the value at the index list.

Examples:

```console
>>>import numojo as nm
>>>var A = nm.full[nm.f32](nm.Shape(2, 5), ComplexSIMD[nm.f32](1.0, 1.0))
>>>print(A[Item(1, 2)]) # gets values of the element at (1, 2).
```.

**Args:**

- `self` (`Self`) `[imm]`
- `index` (`Item`) `[imm]`: Index list.

**Returns:**

- `ComplexSIMD[cdtype]`

!!! failure "Raises"
    NumojoError: If the length of `index` does not match the number of dimensions.
NumojoError: If any of the index elements exceeds the size of the dimension of the array.

###### Overload 3

```mojo
def __getitem__(self, idx: Int) -> Self
```

Single-axis integer slice (first dimension). Returns a slice of the complex array taken at axis 0 position `idx`. Dimensionality is reduced by exactly one; a 1-D source produces a 0-D ComplexNDArray (scalar wrapper). Negative indices are supported and normalized. The result preserves the source memory order (C/F).

Notes:
Performance fast path: For C-contiguous arrays the slice for both
real and imaginary parts is copied with single `memcpy` calls.
For F-contiguous or arbitrary stride layouts, a generic
stride-based copier is used for both components. (Future: return
a non-owning view).

Example:
```mojo
import numojo as nm
from numojo.prelude import *
var a = nm.arange[cf32](CScalar[cf32](0), CScalar[cf32](12), CScalar[cf32](1)).reshape(Shape(3, 4))
print(a.shape)        # (3,4)
print(a[1].shape)     # (4,)  -- 1-D slice
print(a[-1].shape)    # (4,)  -- negative index
var b = nm.arange[cf32](CScalar[cf32](6)).reshape(nm.Shape(6))
print(b[2])           # 0-D array (scalar wrapper)
```

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: Integer index along the first (axis 0) dimension. Supports
    negative indices in [-shape[0], shape[0]).

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the array is 0-D.
NumojoError: If `idx` (after normalization) is out of bounds.

###### Overload 4

```mojo
def __getitem__(self, var *slices: Slice) -> Self
```

Retrieves a slice or sub-array from the current array using variadic slice arguments.

NOTES:
    - This method creates a new array; Views are not currently supported.
    - Negative indices and step sizes are supported as per standard slicing semantics.

Examples:
```mojo
import numojo as nm

var a = nm.arange(10).reshape(nm.Shape(2, 5))
var b = a[:, 2:4]
print(b) # Output: 2x2 sliced array corresponding to columns 2 and 3 of each row.
```

!!! info "Constraints"
    - The number of slices provided must not exceed the number of array dimensions.
- Each slice must be valid for its corresponding dimension.

**Args:**

- `self` (`Self`) `[imm]`
- `*slices` (`Slice`) `[var]`: Variadic list of `Slice` objects, one for each dimension to be sliced.

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If any slice is out of bounds for its corresponding dimension.
NumojoError: If the number of slices does not match the array's dimensions.

###### Overload 5

```mojo
def __getitem__(self, var slice_list: List[Slice]) -> Self
```

Retrieves a sub-array from the current array using a list of slice objects, enabling advanced slicing operations across multiple dimensions.

NOTES:
    - This method supports advanced slicing similar to NumPy's multi-dimensional slicing.
    - The returned array shares data with the original array if possible.

Example:
```mojo
import numojo as nm
from numojo.prelude import *
var a = nm.arange[cf32](CScalar[cf32](10.0, 10.0)).reshape(nm.Shape(2, 5))
var b = a[[Slice(0, 2, 1), Slice(2, 4, 1)]]  # Equivalent to arr[:, 2:4], returns a 2x2 sliced array.
print(b)
```

!!! info "Constraints"
    - The length of slice_list must not exceed the number of dimensions in the array.
- Each Slice in slice_list must be valid for its respective dimension.

**Args:**

- `self` (`Self`) `[imm]`
- `slice_list` (`List[Slice]`) `[var]`: List of Slice objects, where each Slice defines the start, stop, and step for the corresponding dimension.

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If slice_list is empty or contains invalid slices.

###### Overload 6

```mojo
def __getitem__(self, var *slices: Variant[Slice, Int]) -> Self
```

Get items of ComplexNDArray with a series of either slices or integers.

Examples:

```mojo
    import numojo as nm
    from numojo.prelude import *
    var a = nm.full[cf32](nm.Shape(2, 5), CScalar[cf32](1.0, 1.0))
    var b = a[1, Slice(2,4)]
    print(b)
```

**Args:**

- `self` (`Self`) `[imm]`
- `*slices` (`Variant[Slice, Int]`) `[var]`: A series of either Slice or Int.

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the number of slices is greater than the number of dimensions of the array.

###### Overload 7

```mojo
def __getitem__(self, indices: NDArray[DType.int]) -> Self
```

Get items from 0-th dimension of a ComplexNDArray of indices. If the original array is of shape (i,j,k) and the indices array is of shape (l, m, n), then the output array will be of shape (l,m,n,j,k).

**Args:**

- `self` (`Self`) `[imm]`
- `indices` (`NDArray[DType.int]`) `[imm]`: Array of indices.

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the elements of indices are greater than size of the corresponding dimension of the array.

###### Overload 8

```mojo
def __getitem__(self, indices: List[Int]) -> Self
```

Get items from 0-th dimension of a ComplexNDArray of indices. It is an overload of `__getitem__(self, indices: NDArray[DType.int]) raises -> Self`.

**Args:**

- `self` (`Self`) `[imm]`
- `indices` (`List[Int]`) `[imm]`: A list of Int.

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the elements of indices are greater than size of the corresponding dimension of the array.

###### Overload 9

```mojo
def __getitem__(self, mask: NDArray[DType.bool]) -> Self
```

Get item from a ComplexNDArray according to a mask array. If array shape is equal to mask shape, it returns a flattened array of the values where mask is True. If array shape is not equal to mask shape, it returns items from the 0-th dimension of the array where mask is True.

**Args:**

- `self` (`Self`) `[imm]`
- `mask` (`NDArray[DType.bool]`) `[imm]`: NDArray with Dtype.bool.

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the mask is not a 1-D array (Currently we only support 1-d mask array).

###### Overload 10

```mojo
def __getitem__(self, mask: List[Bool]) -> Self
```

Get items from 0-th dimension of a ComplexNDArray according to mask.

**Args:**

- `self` (`Self`) `[imm]`
- `mask` (`List[Bool]`) `[imm]`: A list of boolean values.

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If the mask is not a 1-D array (Currently we only support 1-d mask array).


</div>

<div class="fn-card" markdown="1">

##### `__setitem__`

###### Overload 1

```mojo
def __setitem__(mut self, idx: Int, val: Self)
```

Assign a single first-axis slice. Replaces the sub-array at axis 0 position `idx` with `val`. The shape of `val` must exactly match `self.shape[1:]` and its dimensionality must be `self.ndim - 1` (or be a 0-D complex scalar when assigning into a 1-D array). Negative indices are supported. Fast path: contiguous memcpy for C-order; otherwise a stride-based generic copy is performed for both real and imaginary parts.

**Args:**

- `self` (`Self`) `[mut]`
- `idx` (`Int`) `[imm]`: Integer index along first dimension (supports negatives).
- `val` (`Self`) `[imm]`: ComplexNDArray slice data to assign.

!!! failure "Raises"
    NumojoError: If array is 0-D or idx out of bounds.
NumojoError: If `val` shape/dim mismatch with target slice.

###### Overload 2

```mojo
def __setitem__(mut self, var index: Item, val: ComplexSIMD[cdtype])
```

Sets the value at the index list.

Examples:

```mojo
import numojo as nm
from numojo.prelude import *
var A = nm.full[cf32](Shape(2, 2), CScalar[cf32](1.0))
A[Item(0, 1)] = CScalar[cf32](3.0, 4.0)
```

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`Item`) `[var]`: Index list.
- `val` (`ComplexSIMD[cdtype]`) `[imm]`: Value to set.

!!! failure "Raises"
    NumojoError: If the length of index does not match the number of dimensions.
NumojoError: If any of the indices is out of bound.

###### Overload 3

```mojo
def __setitem__(mut self, mask: NDArray[DType.bool], value: ComplexSIMD[cdtype])
```

Set the value of the array at the indices where the mask is true.

**Args:**

- `self` (`Self`) `[mut]`
- `mask` (`NDArray[DType.bool]`) `[imm]`
- `value` (`ComplexSIMD[cdtype]`) `[imm]`

!!! failure "Raises"

###### Overload 4

```mojo
def __setitem__(mut self, var *slices: Slice, *, val: Self)
```

Retreive slices of an ComplexNDArray from variadic slices.

Example:
`arr[1:3, 2:4]` returns the corresponding sliced ComplexNDArray (2 x 2).

**Args:**

- `self` (`Self`) `[mut]`
- `*slices` (`Slice`) `[var]`
- `val` (`Self`) `[imm]`

!!! failure "Raises"

###### Overload 5

```mojo
def __setitem__(mut self, slices: List[Slice], val: Self)
```

Sets the slices of an ComplexNDArray from list of slices and ComplexNDArray.

Example:
`arr[1:3, 2:4]` returns the corresponding sliced ComplexNDArray (2 x 2).

**Args:**

- `self` (`Self`) `[mut]`
- `slices` (`List[Slice]`) `[imm]`
- `val` (`Self`) `[imm]`

!!! failure "Raises"

###### Overload 6

```mojo
def __setitem__(mut self, var *slices: Variant[Slice, Int], *, val: Self)
```

Get items by a series of either slices or integers.

**Args:**

- `self` (`Self`) `[mut]`
- `*slices` (`Variant[Slice, Int]`) `[var]`
- `val` (`Self`) `[imm]`

!!! failure "Raises"

###### Overload 7

```mojo
def __setitem__(mut self, index: NDArray[DType.int], val: Self)
```

Returns the items of the ComplexNDArray from an array of indices.

Refer to `__getitem__(self, index: List[Int])`.

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`NDArray[DType.int]`) `[imm]`
- `val` (`Self`) `[imm]`

!!! failure "Raises"

###### Overload 8

```mojo
def __setitem__(mut self, mask: NDArray[DType.bool], val: Self)
```

Set the value of the ComplexNDArray at the indices where the mask is true.

**Args:**

- `self` (`Self`) `[mut]`
- `mask` (`NDArray[DType.bool]`) `[imm]`
- `val` (`Self`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__neg__`

```mojo
def __neg__(self) -> Self
```

Unary negative returns self unless boolean type.

For bolean use `__invert__`(~)

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__pos__`

```mojo
def __pos__(self) -> Self
```

Unary positive returns self unless boolean type.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__lt__`

###### Overload 1

```mojo
def __lt__(self, other: Self) -> NDArray[DType.bool]
```

NumPy-style lexicographic ordering: compare real part first, then imaginary part.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"

###### Overload 2

```mojo
def __lt__(self, other: ComplexSIMD[cdtype]) -> NDArray[DType.bool]
```

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"

###### Overload 3

```mojo
def __lt__(self, other: Scalar[Self.dtype]) -> NDArray[DType.bool]
```

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__le__`

###### Overload 1

```mojo
def __le__(self, other: Self) -> NDArray[DType.bool]
```

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"

###### Overload 2

```mojo
def __le__(self, other: ComplexSIMD[cdtype]) -> NDArray[DType.bool]
```

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"

###### Overload 3

```mojo
def __le__(self, other: Scalar[Self.dtype]) -> NDArray[DType.bool]
```

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

###### Overload 1

```mojo
def __eq__(self, other: Self) -> NDArray[DType.bool]
```

Itemwise equivalence.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"

###### Overload 2

```mojo
def __eq__(self, other: ComplexSIMD[cdtype]) -> NDArray[DType.bool]
```

Itemwise equivalence between scalar and ComplexNDArray.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

###### Overload 1

```mojo
def __ne__(self, other: Self) -> NDArray[DType.bool]
```

Itemwise non-equivalence.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"

###### Overload 2

```mojo
def __ne__(self, other: ComplexSIMD[cdtype]) -> NDArray[DType.bool]
```

Itemwise non-equivalence between scalar and ComplexNDArray.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__gt__`

###### Overload 1

```mojo
def __gt__(self, other: Self) -> NDArray[DType.bool]
```

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"

###### Overload 2

```mojo
def __gt__(self, other: ComplexSIMD[cdtype]) -> NDArray[DType.bool]
```

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"

###### Overload 3

```mojo
def __gt__(self, other: Scalar[Self.dtype]) -> NDArray[DType.bool]
```

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__ge__`

###### Overload 1

```mojo
def __ge__(self, other: Self) -> NDArray[DType.bool]
```

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"

###### Overload 2

```mojo
def __ge__(self, other: ComplexSIMD[cdtype]) -> NDArray[DType.bool]
```

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"

###### Overload 3

```mojo
def __ge__(self, other: Scalar[Self.dtype]) -> NDArray[DType.bool]
```

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__add__`

###### Overload 1

```mojo
def __add__(self, other: ComplexSIMD[cdtype]) -> Self
```

Enables `ComplexNDArray + ComplexSIMD`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def __add__(self, other: Scalar[Self.dtype]) -> Self
```

Enables `ComplexNDArray + Scalar`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 3

```mojo
def __add__(self, other: Self) -> Self
```

Enables `ComplexNDArray + ComplexNDArray`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 4

```mojo
def __add__(self, other: NDArray[Self.dtype]) -> Self
```

Enables `ComplexNDArray + NDArray`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`NDArray[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__sub__`

###### Overload 1

```mojo
def __sub__(self, other: ComplexSIMD[cdtype]) -> Self
```

Enables `ComplexNDArray - ComplexSIMD`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def __sub__(self, other: Scalar[Self.dtype]) -> Self
```

Enables `ComplexNDArray - Scalar`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 3

```mojo
def __sub__(self, other: Self) -> Self
```

Enables `ComplexNDArray - ComplexNDArray`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 4

```mojo
def __sub__(self, other: NDArray[Self.dtype]) -> Self
```

Enables `ComplexNDArray - NDArray`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`NDArray[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__mul__`

###### Overload 1

```mojo
def __mul__(self, other: ComplexSIMD[cdtype]) -> Self
```

Enables `ComplexNDArray * ComplexSIMD`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def __mul__(self, other: Scalar[Self.dtype]) -> Self
```

Enables `ComplexNDArray * Scalar`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 3

```mojo
def __mul__(self, other: Self) -> Self
```

Enables `ComplexNDArray * ComplexNDArray`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 4

```mojo
def __mul__(self, other: NDArray[Self.dtype]) -> Self
```

Enables `ComplexNDArray * NDArray`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`NDArray[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__matmul__`

```mojo
def __matmul__(self, other: Self) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__truediv__`

###### Overload 1

```mojo
def __truediv__(self, other: ComplexSIMD[cdtype]) -> Self
```

Enables `ComplexNDArray / ComplexSIMD`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def __truediv__(self, other: Scalar[Self.dtype]) -> Self
```

Enables `ComplexNDArray / ComplexSIMD`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 3

```mojo
def __truediv__(self, other: Self) -> Self
```

Enables `ComplexNDArray / ComplexNDArray`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 4

```mojo
def __truediv__(self, other: NDArray[Self.dtype]) -> Self
```

Enables `ComplexNDArray / NDArray`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`NDArray[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__pow__`

###### Overload 1

```mojo
def __pow__(self, p: Int) -> Self
```

Raise complex array to integer power element-wise.

Uses De Moivre's formula for complex exponentiation:
(r * e^(i*theta))^n = r^n * e^(i*n*theta)

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(2, 2))
var B = A ** 3  # Cube each element
```

**Args:**

- `self` (`Self`) `[imm]`
- `p` (`Int`) `[imm]`: Integer exponent.

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def __pow__(self, rhs: Scalar[Self.dtype]) -> Self
```

Raise complex array to real scalar power element-wise.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(2, 2))
var B = A ** 2.5  # Raise to power 2.5
```

**Args:**

- `self` (`Self`) `[imm]`
- `rhs` (`Scalar[Self.dtype]`) `[imm]`: Real scalar exponent.

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 3

```mojo
def __pow__(self, p: Self) -> Self where ComplexNDArray[cdtype].dtype.is_floating_point()
```

Raise complex array to complex array power element-wise.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(2, 2))
var B = nm.ComplexNDArray[nm.cf64](nm.Shape(2, 2))
var C = A ** B  # Element-wise complex power
```

**Args:**

- `self` (`Self`) `[imm]`
- `p` (`Self`) `[imm]`: ComplexNDArray exponent.

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If arrays have different sizes.


</div>

<div class="fn-card" markdown="1">

##### `__radd__`

###### Overload 1

```mojo
def __radd__(mut self, other: ComplexSIMD[cdtype]) -> Self
```

Enables `ComplexSIMD + ComplexNDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def __radd__(mut self, other: Scalar[Self.dtype]) -> Self
```

Enables `Scalar + ComplexNDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 3

```mojo
def __radd__(mut self, other: NDArray[Self.dtype]) -> Self
```

Enables `NDArray + ComplexNDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`NDArray[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__rsub__`

###### Overload 1

```mojo
def __rsub__(mut self, other: ComplexSIMD[cdtype]) -> Self
```

Enables `ComplexSIMD - ComplexNDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def __rsub__(mut self, other: Scalar[Self.dtype]) -> Self
```

Enables `Scalar - ComplexNDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 3

```mojo
def __rsub__(mut self, other: NDArray[Self.dtype]) -> Self
```

Enables `NDArray - ComplexNDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`NDArray[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__rmul__`

###### Overload 1

```mojo
def __rmul__(self, other: ComplexSIMD[cdtype]) -> Self
```

Enables `ComplexSIMD * ComplexNDArray`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def __rmul__(self, other: Scalar[Self.dtype]) -> Self
```

Enables `Scalar * ComplexNDArray`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 3

```mojo
def __rmul__(self, other: NDArray[Self.dtype]) -> Self
```

Enables `NDArray * ComplexNDArray`.

**Args:**

- `self` (`Self`) `[imm]`
- `other` (`NDArray[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__rtruediv__`

###### Overload 1

```mojo
def __rtruediv__(mut self, other: ComplexSIMD[cdtype]) -> Self
```

Enables `ComplexSIMD / ComplexNDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def __rtruediv__(mut self, other: Scalar[Self.dtype]) -> Self
```

Enables `Scalar / ComplexNDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 3

```mojo
def __rtruediv__(mut self, other: NDArray[Self.dtype]) -> Self
```

Enables `NDArray / ComplexNDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`NDArray[Self.dtype]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__iadd__`

###### Overload 1

```mojo
def __iadd__(mut self, other: ComplexSIMD[cdtype])
```

Enables `ComplexNDArray += ComplexSIMD`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

!!! failure "Raises"

###### Overload 2

```mojo
def __iadd__(mut self, other: Scalar[Self.dtype])
```

Enables `ComplexNDArray += Scalar`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

!!! failure "Raises"

###### Overload 3

```mojo
def __iadd__(mut self, other: Self)
```

Enables `ComplexNDArray += ComplexNDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`

!!! failure "Raises"

###### Overload 4

```mojo
def __iadd__(mut self, other: NDArray[Self.dtype])
```

Enables `ComplexNDArray += NDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`NDArray[Self.dtype]`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__isub__`

###### Overload 1

```mojo
def __isub__(mut self, other: ComplexSIMD[cdtype])
```

Enables `ComplexNDArray -= ComplexSIMD`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

!!! failure "Raises"

###### Overload 2

```mojo
def __isub__(mut self, other: Scalar[Self.dtype])
```

Enables `ComplexNDArray -= Scalar`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

!!! failure "Raises"

###### Overload 3

```mojo
def __isub__(mut self, other: Self)
```

Enables `ComplexNDArray -= ComplexNDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`

!!! failure "Raises"

###### Overload 4

```mojo
def __isub__(mut self, other: NDArray[Self.dtype])
```

Enables `ComplexNDArray -= NDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`NDArray[Self.dtype]`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__imul__`

###### Overload 1

```mojo
def __imul__(mut self, other: ComplexSIMD[cdtype])
```

Enables `ComplexNDArray *= ComplexSIMD`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

!!! failure "Raises"

###### Overload 2

```mojo
def __imul__(mut self, other: Scalar[Self.dtype])
```

Enables `ComplexNDArray *= Scalar`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

!!! failure "Raises"

###### Overload 3

```mojo
def __imul__(mut self, other: Self)
```

Enables `ComplexNDArray *= ComplexNDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`

!!! failure "Raises"

###### Overload 4

```mojo
def __imul__(mut self, other: NDArray[Self.dtype])
```

Enables `ComplexNDArray *= NDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`NDArray[Self.dtype]`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__itruediv__`

###### Overload 1

```mojo
def __itruediv__(mut self, other: ComplexSIMD[cdtype])
```

Enables `ComplexNDArray /= ComplexSIMD`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`ComplexSIMD[cdtype]`) `[imm]`

!!! failure "Raises"

###### Overload 2

```mojo
def __itruediv__(mut self, other: Scalar[Self.dtype])
```

Enables `ComplexNDArray /= Scalar`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar[Self.dtype]`) `[imm]`

!!! failure "Raises"

###### Overload 3

```mojo
def __itruediv__(mut self, other: Self)
```

Enables `ComplexNDArray /= ComplexNDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`) `[imm]`

!!! failure "Raises"

###### Overload 4

```mojo
def __itruediv__(mut self, other: NDArray[Self.dtype])
```

Enables `ComplexNDArray /= NDArray`.

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`NDArray[Self.dtype]`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__ipow__`

```mojo
def __ipow__(mut self, p: Int)
```

In-place raise to integer power.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(2, 2))
A **= 3  # Cube in place
```

**Args:**

- `self` (`Self`) `[mut]`
- `p` (`Int`) `[imm]`: Integer exponent.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `view`

```mojo
def view(mut self) -> Self
```

Create a non-owning view of the current ComplexNDArray.

Examples:
```mojo
import numojo as nm
var arr = nm.ComplexNDArray[nm.cf32](nm.Shape(3, 4))
var v = arr.view()  # Create a view into arr.
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
def normalize(self, idx: Int, dim: Int) -> Int
```

Normalize a potentially negative index to its positive equivalent within the bounds of the given dimension.

**Args:**

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: The index to normalize. Can be negative to indicate indexing
     from the end (e.g., -1 refers to the last element).
- `dim` (`Int`) `[imm]`: The size of the dimension to normalize against.

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `item`

###### Overload 1

```mojo
def item(self, var index: Int) -> ComplexSIMD[cdtype]
```

Return the scalar at the coordinates. If one index is given, get the i-th item of the complex array (not buffer). It first scans over the first row, even it is a column-major array. If more than one index is given, the length of the indices must match the number of dimensions of the array. If the ndim is 0 (0-D array), get the value as a mojo scalar.

Examples:

```console
>>> import numojo as nm
>>> var A = nm.full[nm.f32](Shape(2, 2, 2), ComplexSIMD[nm.f32](1.0, 1.0))
>>> print(A.item(10)) # returns the 10-th item of the complex array.
```.

**Args:**

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[var]`: Index of item, counted in row-major way.

**Returns:**

- `ComplexSIMD[cdtype]`

!!! failure "Raises"
    Error if array is 0-D array (numojo scalar).
Error if index is equal or larger than array size.

###### Overload 2

```mojo
def item(self, *index: Int) -> ComplexSIMD[cdtype]
```

Return the scalar at the coordinates. If one index is given, get the i-th item of the complex array (not buffer). It first scans over the first row, even it is a colume-major array. If more than one index is given, the length of the indices must match the number of dimensions of the array. For 0-D complex array (numojo scalar), return the scalar value.

Examples:

```console
>>> import numojo as nm
>>> var A = nm.full[nm.f32](Shape(2, 2, 2), ComplexSIMD[nm.f32](1.0, 1.0))
>>> print(A.item(1, 1, 1)) # returns the 10-th item of the complex array.
```.

**Args:**

- `self` (`Self`) `[imm]`
- `*index` (`Int`) `[imm]`: The coordinates of the item.

**Returns:**

- `ComplexSIMD[cdtype]`

!!! failure "Raises"
    NumojoError: If the number of indices is not equal to the number of dimensions of the array.
NumojoError: If the index is equal or larger than size of dimension.


</div>

<div class="fn-card" markdown="1">

##### `load`

###### Overload 1

```mojo
def load(self, var index: Int) -> ComplexSIMD[cdtype]
```

Safely retrieve i-th item from the underlying buffer.

`A.load(i)` differs from `A._buf.ptr[i]` due to boundary check.

Examples:

```console
>>> import numojo as nm
>>> var A = nm.full[nm.f32](Shape(2, 2, 2), ComplexSIMD[nm.f32](1.0, 1.0))
>>> print(A.load(10)) # returns the 10-th item of the complex array.
```.

**Args:**

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[var]`: Index of the item.

**Returns:**

- `ComplexSIMD[cdtype]`

!!! failure "Raises"
    Index out of bounds.

###### Overload 2

```mojo
def load[width: Int = Int(1)](self, index: Int) -> ComplexSIMD[cdtype, width]
```

Safely loads a ComplexSIMD element of size `width` at `index` from the underlying buffer.

To bypass boundary checks, use `self._buf.ptr.load` directly.

**Parameters:**

- `width` (`Int`)

**Args:**

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[imm]`: Index of the item.

**Returns:**

- `ComplexSIMD[cdtype, width]`

!!! failure "Raises"
    Index out of boundary.

###### Overload 3

```mojo
def load[width: Int = Int(1)](self, *indices: Int) -> ComplexSIMD[cdtype, width]
```

Safely loads a ComplexSIMD element of size `width` at given variadic indices from the underlying buffer.

To bypass boundary checks, use `self._buf.ptr.load` directly.

Examples:

```console
>>> import numojo as nm
>>> var A = nm.full[nm.f32](Shape(2, 2, 2), ComplexSIMD[nm.f32](1.0, 1.0))
>>> print(A.load(0, 1, 1))
```.

**Parameters:**

- `width` (`Int`)

**Args:**

- `self` (`Self`) `[imm]`
- `*indices` (`Int`) `[imm]`: Variadic indices.

**Returns:**

- `ComplexSIMD[cdtype, width]`

!!! failure "Raises"
    NumojoError: If the length of indices does not match the number of dimensions.
NumojoError: If any of the indices is out of bound.


</div>

<div class="fn-card" markdown="1">

##### `__int__`

```mojo
def __int__(self) -> Int
```

Gets `Int` representation of the complex array's real part.

Only 0-D arrays or length-1 arrays can be converted to scalars.
The imaginary part is discarded.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape())  # 0-D array
A._re.unsafe_set(0, 42.7)
A._im.unsafe_set(0, 3.14)
print(A.__int__())  # 42 (only real part)
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`

!!! failure "Raises"
    NumojoError: If the array is not 0-D or length-1.


</div>

<div class="fn-card" markdown="1">

##### `__float__`

```mojo
def __float__(self) -> Float64
```

Gets `Float64` representation of the complex array's magnitude.

Only 0-D arrays or length-1 arrays can be converted to scalars.
Returns the magnitude (absolute value) of the complex number.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape())  # 0-D array
A._re.unsafe_set(0, 3.0)
A._im.unsafe_set(0, 4.0)
print(A.__float__())  # 5.0 (magnitude)
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Float64`

!!! failure "Raises"
    NumojoError: If the array is not 0-D or length-1.


</div>

<div class="fn-card" markdown="1">

##### `__abs__`

```mojo
def __abs__(self) -> NDArray[Self.dtype]
```

Compute the magnitude (absolute value) of each complex element.

Returns an NDArray of real values containing the magnitude of each
complex number: sqrt(re^2 + im^2).

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(2, 2))
# Fill with some values
var mag = A.__abs__()  # Returns NDArray[f64] with magnitudes
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `NDArray[Self.dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
def __str__(self) -> String
```

Enables String(array).

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `write_to`

```mojo
def write_to[W: Writer](self, mut writer: W)
```

Writes the array to a writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`: The writer to write the array to.


</div>

<div class="fn-card" markdown="1">

##### `write_repr_to`

```mojo
def write_repr_to[W: Writer](self, mut writer: W)
```

Write the string representation to a writer.

**Parameters:**

- `W` (`Writer`): The writer type.

**Args:**

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`: The writer to write to.


</div>

<div class="fn-card" markdown="1">

##### `__repr__`

```mojo
def __repr__(self) -> String
```

Compute the "official" string representation of ComplexNDArray. An example is: ``` def main() raises:     var A = ComplexNDArray[f32](List[ComplexSIMD[f32]](14,97,-59,-4,112,), shape=List[Int](5,))     print(repr(A)) ``` It prints what can be used to construct the array itself: ```console     ComplexNDArray[f32](List[ComplexSIMD[f32]](14,97,-59,-4,112,), shape=List[Int](5,)) ```.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `__len__`

```mojo
def __len__(self) -> Int
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `store`

###### Overload 1

```mojo
def store[width: Int = Int(1)](mut self, index: Int, val: ComplexSIMD[cdtype])
```

Safely stores SIMD element of size `width` at `index` of the underlying buffer.

To bypass boundary checks, use `self._buf.ptr.store` directly.

**Parameters:**

- `width` (`Int`)

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`Int`) `[imm]`
- `val` (`ComplexSIMD[cdtype]`) `[imm]`

!!! failure "Raises"
    Index out of boundary.

###### Overload 2

```mojo
def store[width: Int = Int(1)](mut self, *indices: Int, *, val: ComplexSIMD[cdtype])
```

Safely stores SIMD element of size `width` at given variadic indices of the underlying buffer.

To bypass boundary checks, use `self._buf.ptr.store` directly.

**Parameters:**

- `width` (`Int`)

**Args:**

- `self` (`Self`) `[mut]`
- `*indices` (`Int`) `[imm]`
- `val` (`ComplexSIMD[cdtype]`) `[imm]`

!!! failure "Raises"
    Index out of boundary.


</div>

<div class="fn-card" markdown="1">

##### `reshape`

```mojo
def reshape(self, shape: NDArrayShape, order: String = "C") -> Self
```

Returns an array of the same data with a new shape.

**Args:**

- `self` (`Self`) `[imm]`
- `shape` (`NDArrayShape`) `[imm]`: Shape of returned array.
- `order` (`String`) `[imm]`: Order of the array - Row major `C` or Column major `F`.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `itemset`

###### Overload 1

```mojo
def itemset(mut self, index: Int, item: ComplexSIMD[cdtype])
```

Sets the scalar at the given coordinate.

Examples:

```
import numojo as nm
def main() raises:
    var A = nm.zeros[nm.cf16](nm.Shape(3, 3))
    print(A)
    A.itemset(5, nm.ComplexSIMD[nm.f16](1.0, 2.0))
    print(A)
```
```console
[[      (0.0, 0.0)    (0.0, 0.0)    (0.0, 0.0)    ]
[      (0.0, 0.0)    (0.0, 0.0)    (0.0, 0.0)    ]
[      (0.0, 0.0)    (0.0, 0.0)    (0.0, 0.0)    ]]
2-D array  Shape: [3, 3]  DType: complex16
[[      (0.0, 0.0)    (0.0, 0.0)    (0.0, 0.0)    ]
[      (0.0, 0.0)    (0.0, 0.0)    (1.0, 2.0)    ]
[      (0.0, 0.0)    (0.0, 0.0)    (0.0, 0.0)    ]]
2-D array  Shape: [3, 3]  DType: complex16
```.

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`Int`) `[imm]`: The linear index of the i-th item of the whole array.
- `item` (`ComplexSIMD[cdtype]`) `[imm]`: The complex scalar to be set.

!!! failure "Raises"
    NumojoError: If the index is out of bounds.
NumojoError: If the length of index does not match the number of
dimensions.

###### Overload 2

```mojo
def itemset(mut self, var indices: List[Int], item: ComplexSIMD[cdtype])
```

Sets the scalar at the given coordinates.

Notes:
This is similar to `numpy.ndarray.itemset`. The difference is that
we take `List[Int]`, but NumPy takes a tuple.

Examples:

```
import numojo as nm
def main() raises:
    var A = nm.zeros[nm.cf16](nm.Shape(3, 3))
    print(A)
    A.itemset(nm.List(1, 1), nm.ComplexSIMD[nm.f16](1.0, 2.0))
    print(A)
```
```console
[[      (0.0, 0.0)    (0.0, 0.0)    (0.0, 0.0)    ]
[      (0.0, 0.0)    (0.0, 0.0)    (0.0, 0.0)    ]
[      (0.0, 0.0)    (0.0, 0.0)    (0.0, 0.0)    ]]
2-D array  Shape: [3, 3]  DType: complex16
[[      (0.0, 0.0)    (0.0, 0.0)    (0.0, 0.0)    ]
[      (0.0, 0.0)    (1.0, 2.0)    (0.0, 0.0)    ]
[      (0.0, 0.0)    (0.0, 0.0)    (0.0, 0.0)    ]]
2-D array  Shape: [3, 3]  DType: complex16
```.

**Args:**

- `self` (`Self`) `[mut]`
- `indices` (`List[Int]`) `[var]`: The coordinates of the item.
- `item` (`ComplexSIMD[cdtype]`) `[imm]`: The complex scalar to be set.

!!! failure "Raises"
    NumojoError: If the index is out of bounds.
NumojoError: If the length of index does not match the number of
dimensions.


</div>

<div class="fn-card" markdown="1">

##### `conj`

```mojo
def conj(self) -> Self
```

Return the complex conjugate of the ComplexNDArray.

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `to_ndarray`

```mojo
def to_ndarray(self, type: String = "re") -> NDArray[Self.dtype]
```

**Args:**

- `self` (`Self`) `[imm]`
- `type` (`String`) `[imm]`

**Returns:**

- `NDArray[Self.dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `squeeze`

```mojo
def squeeze(mut self, axis: Int)
```

Remove (squeeze) a single dimension of size 1 from the array shape.

**Args:**

- `self` (`Self`) `[mut]`
- `axis` (`Int`) `[imm]`: The axis to squeeze. Supports negative indices.

!!! failure "Raises"
    NumojoError: If the axis is out of range.
NumojoError: If the dimension at the given axis is not of size 1.


</div>

<div class="fn-card" markdown="1">

##### `all`

```mojo
def all(self) -> Bool
```

Check if all complex elements are non-zero.

A complex number is considered "true" if either its real or imaginary
part is non-zero.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 3))
# Fill with non-zero values
var result = A.all()  # True if all non-zero
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `any`

```mojo
def any(self) -> Bool
```

Check if any complex element is non-zero.

A complex number is considered "true" if either its real or imaginary
part is non-zero.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 3))
# Fill with some values
var result = A.any()  # True if any non-zero
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `sum`

###### Overload 1

```mojo
def sum(self) -> ComplexSIMD[cdtype]
```

Sum of all complex array elements.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 3))
var total = A.sum()  # Sum of all elements
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `ComplexSIMD[cdtype]`

!!! failure "Raises"

###### Overload 2

```mojo
def sum(self, axis: Int) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `prod`

###### Overload 1

```mojo
def prod(self) -> ComplexSIMD[cdtype]
```

Product of all complex array elements.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 3))
var product = A.prod()  # Product of all elements
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `ComplexSIMD[cdtype]`

!!! failure "Raises"

###### Overload 2

```mojo
def prod(self, axis: Int) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `mean`

###### Overload 1

```mojo
def mean(self) -> ComplexSIMD[cdtype]
```

Mean (average) of all complex array elements.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 3))
var average = A.mean()  # Mean of all elements
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `ComplexSIMD[cdtype]`

!!! failure "Raises"

###### Overload 2

```mojo
def mean(self, axis: Int) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `max`

###### Overload 1

```mojo
def max(self) -> ComplexSIMD[cdtype]
```

Find the complex element with maximum magnitude.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 3))
var max_elem = A.max()  # Element with largest magnitude
```

Notes:
Returns the element with maximum |z| = sqrt(re^2 + im^2).

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `ComplexSIMD[cdtype]`

!!! failure "Raises"

###### Overload 2

```mojo
def max(self, axis: Int) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `min`

###### Overload 1

```mojo
def min(self) -> ComplexSIMD[cdtype]
```

Find the complex element with minimum magnitude.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 3))
var min_elem = A.min()  # Element with smallest magnitude
```

Notes:
Returns the element with minimum |z| = sqrt(re^2 + im^2).

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `ComplexSIMD[cdtype]`

!!! failure "Raises"

###### Overload 2

```mojo
def min(self, axis: Int) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `argmax`

###### Overload 1

```mojo
def argmax(self) -> Int
```

Return the index of the element with maximum magnitude.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 3))
var idx = A.argmax()  # Index of element with largest magnitude
```

Notes:
Compares by magnitude: |z| = sqrt(re^2 + im^2).

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`

!!! failure "Raises"

###### Overload 2

```mojo
def argmax(self, axis: Int) -> NDArray[DType.int]
```

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`

**Returns:**

- `NDArray[DType.int]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `argmin`

###### Overload 1

```mojo
def argmin(self) -> Int
```

Return the index of the element with minimum magnitude.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 3))
var idx = A.argmin()  # Index of element with smallest magnitude
```

Notes:
Compares by magnitude: |z| = sqrt(re^2 + im^2).

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`

!!! failure "Raises"

###### Overload 2

```mojo
def argmin(self, axis: Int) -> NDArray[DType.int]
```

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`

**Returns:**

- `NDArray[DType.int]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `cumsum`

###### Overload 1

```mojo
def cumsum(self) -> Self
```

Cumulative sum of complex array elements.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(5))
var cumulative = A.cumsum()
```

Notes:
For array [a, b, c, d], returns [a, a+b, a+b+c, a+b+c+d].

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def cumsum(self, axis: Int) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `cumprod`

###### Overload 1

```mojo
def cumprod(self) -> Self
```

Cumulative product of complex array elements.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(5))
var cumulative = A.cumprod()
```

Notes:
For array [a, b, c, d], returns [a, a*b, a*b*c, a*b*c*d].

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def cumprod(self, axis: Int) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `flatten`

```mojo
def flatten(self, order: String = "C") -> Self
```

Return a copy of the array collapsed into one dimension.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 4))
var flat = A.flatten()  # Shape(12)
```

**Args:**

- `self` (`Self`) `[imm]`
- `order` (`String`) `[imm]`: Order of flattening - 'C' for row-major or 'F' for column-major.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `fill`

```mojo
def fill(mut self, val: ComplexSIMD[cdtype])
```

Fill all items of array with a complex value.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 3))
A.fill(nm.ComplexSIMD[nm.cf64](1.0, 2.0))  # Fill with 1+2i
```

**Args:**

- `self` (`Self`) `[mut]`
- `val` (`ComplexSIMD[cdtype]`) `[imm]`: Complex value to fill the array with.


</div>

<div class="fn-card" markdown="1">

##### `row`

```mojo
def row(self, id: Int) -> Self
```

Get the ith row of the matrix.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 4))
var first_row = A.row(0)  # Get first row
```

**Args:**

- `self` (`Self`) `[imm]`
- `id` (`Int`) `[imm]`: The row index.

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If ndim is greater than 2.


</div>

<div class="fn-card" markdown="1">

##### `col`

```mojo
def col(self, id: Int) -> Self
```

Get the ith column of the matrix.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 4))
var first_col = A.col(0)  # Get first column
```

**Args:**

- `self` (`Self`) `[imm]`
- `id` (`Int`) `[imm]`: The column index.

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If ndim is greater than 2.


</div>

<div class="fn-card" markdown="1">

##### `clip`

```mojo
def clip(self, a_min: Scalar[Self.dtype], a_max: Scalar[Self.dtype]) -> Self
```

Limit the magnitudes of complex values between [a_min, a_max].

Elements with magnitude less than a_min are scaled to have magnitude a_min.
Elements with magnitude greater than a_max are scaled to have magnitude a_max.
The phase (angle) of each complex number is preserved.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(10))
var clipped = A.clip(1.0, 5.0)  # Clip magnitudes to [1, 5]
```

Notes:
Clips by magnitude while preserving phase angle.

**Args:**

- `self` (`Self`) `[imm]`
- `a_min` (`Scalar[Self.dtype]`) `[imm]`: The minimum magnitude.
- `a_max` (`Scalar[Self.dtype]`) `[imm]`: The maximum magnitude.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `round`

```mojo
def round(self) -> Self
```

Round the real and imaginary parts of each element to the nearest integer.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(10))
# A contains e.g. 1.7+2.3i
var rounded = A.round()  # Returns 2.0+2.0i
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `T`

###### Overload 1

```mojo
def T(self) -> Self
```

Transpose the complex array (reverse all axes).

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 4))
var A_T = A.T()  # Shape(4, 3)
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def T(self, axes: List[Int]) -> Self
```

Transpose the complex array according to the given axes permutation.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(2, 3, 4))
var A_T = A.T([2, 0, 1])  # Shape(4, 2, 3)
```

**Args:**

- `self` (`Self`) `[imm]`
- `axes` (`List[Int]`) `[imm]`: Permutation of axes (e.g., [1, 0, 2]).

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `diagonal`

```mojo
def diagonal(self, offset: Int = Int(0)) -> Self
```

Extract the diagonal from a 2D complex array.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(4, 4))
var diag = A.diagonal()      # Main diagonal
var upper = A.diagonal(1)    # First upper diagonal
```

**Args:**

- `self` (`Self`) `[imm]`
- `offset` (`Int`) `[imm]`: Offset from the main diagonal (0 for main diagonal).

**Returns:**

- `Self`

!!! failure "Raises"
    NumojoError: If array is not 2D.


</div>

<div class="fn-card" markdown="1">

##### `trace`

```mojo
def trace(self) -> ComplexSIMD[cdtype]
```

Return the sum of the diagonal elements (trace of the matrix).

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 3))
var tr = A.trace()  # Sum of diagonal elements
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `ComplexSIMD[cdtype]`

!!! failure "Raises"
    NumojoError: If array is not 2D.


</div>

<div class="fn-card" markdown="1">

##### `tolist`

```mojo
def tolist(self) -> List[ComplexSIMD[cdtype]]
```

Convert the complex array to a List of complex scalars.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(2, 3))
var elements = A.tolist()  # List of 6 complex numbers
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `List[ComplexSIMD[cdtype]]`


</div>

<div class="fn-card" markdown="1">

##### `astype`

```mojo
def astype[target: ComplexDType](self) -> ComplexNDArray[target]
```

Casts this complex array to another complex dtype.

**Parameters:**

- `target` (`ComplexDType`)

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `ComplexNDArray[target]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `compress`

###### Overload 1

```mojo
def compress(self, condition: NDArray[DType.bool], axis: Int) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`
- `condition` (`NDArray[DType.bool]`) `[imm]`
- `axis` (`Int`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
def compress(self, condition: NDArray[DType.bool]) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`
- `condition` (`NDArray[DType.bool]`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `contiguous`

```mojo
def contiguous(self) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `is_c_contiguous`

```mojo
def is_c_contiguous(self) -> Bool
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_f_contiguous`

```mojo
def is_f_contiguous(self) -> Bool
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_row_contiguous`

```mojo
def is_row_contiguous(self) -> Bool
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `is_col_contiguous`

```mojo
def is_col_contiguous(self) -> Bool
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `unsafe_load`

```mojo
def unsafe_load[width: Int = Int(1)](self, index: Int) -> ComplexSIMD[cdtype, width]
```

**Parameters:**

- `width` (`Int`)

**Args:**

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[imm]`

**Returns:**

- `ComplexSIMD[cdtype, width]`


</div>

<div class="fn-card" markdown="1">

##### `unsafe_store`

```mojo
def unsafe_store[width: Int = Int(1)](mut self, index: Int, val: ComplexSIMD[cdtype, width])
```

**Parameters:**

- `width` (`Int`)

**Args:**

- `self` (`Self`) `[mut]`
- `index` (`Int`) `[imm]`
- `val` (`ComplexSIMD[cdtype, width]`) `[imm]`


</div>

<div class="fn-card" markdown="1">

##### `to_numpy`

```mojo
def to_numpy(self) -> PythonObject
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `PythonObject`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `argsort`

###### Overload 1

```mojo
def argsort(self) -> NDArray[DType.int]
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `NDArray[DType.int]`

!!! failure "Raises"

###### Overload 2

```mojo
def argsort(self, axis: Int) -> NDArray[DType.int]
```

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`

**Returns:**

- `NDArray[DType.int]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `sort`

```mojo
def sort(mut self, axis: Int = Int(-1), stable: Bool = False)
```

**Args:**

- `self` (`Self`) `[mut]`
- `axis` (`Int`) `[imm]`
- `stable` (`Bool`) `[imm]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `median`

###### Overload 1

```mojo
def median(self) -> ComplexSIMD[cdtype]
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `ComplexSIMD[cdtype]`

!!! failure "Raises"

###### Overload 2

```mojo
def median(self, axis: Int) -> Self
```

**Args:**

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `num_elements`

```mojo
def num_elements(self) -> Int
```

Return the total number of elements in the array.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(3, 4, 5))
print(A.num_elements())  # 60
```

**Args:**

- `self` (`Self`) `[imm]`

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `resize`

```mojo
def resize(mut self, shape: NDArrayShape)
```

Change shape and size of array in-place.

If the new shape requires more elements, they are filled with zero.
If the new shape requires fewer elements, the array is truncated.

Examples:
```mojo
import numojo as nm
var A = nm.ComplexNDArray[nm.cf64](nm.Shape(2, 3))
A.resize(nm.Shape(3, 4))  # Now 3x4, filled with zeros as needed
```

Notes:
This modifies the array in-place. To get a reshaped copy, use reshape().

**Args:**

- `self` (`Self`) `[mut]`
- `shape` (`NDArrayShape`) `[imm]`: The new shape for the array.

!!! failure "Raises"


</div>
