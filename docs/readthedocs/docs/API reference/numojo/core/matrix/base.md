# `numojo.core.matrix.base`

Matrix (numojo.core.matrix)

This file implements the core 2D matrix type for the NuMojo numerical computing library. It provides efficient, flexible, and memory-safe matrix operations for scientific and engineering applications.

Features:
- `Matrix`: The primary 2D array type for owning matrix data.
- `Matrix`: Lightweight, non-owning views for fast slicing and submatrix access.
- Iterators for traversing matrix elements.
- Comprehensive dunder methods for initialization, indexing, slicing, and arithmetic.
- Utility functions for broadcasting, memory layout, and linear algebra routines.

Use this module to create, manipulate, and analyze matrices with high performance and safety guarantees.

## Structs

### `Matrix`

```mojo
struct Matrix[dtype: DType = DType.float64]
```

**Memory convention:** `memory_only`  
**Implements:** `AnyType`, `Copyable`, `ImplicitlyDestructible`, `Movable`, `Sized`, `Stringable`, `Writable`

Core implementation struct for 2D matrix operations.

`Matrix` is the single implementation backing the `Matrix` alias. It provides
the full API for 2D array manipulation with fixed dimensionality, enabling
efficient `(row, col)` access patterns and optimizations not possible with a
generic N-dimensional array.

This struct represents a specialized case of `NDArray` optimized for 2D operations.
The fixed dimensionality allows for simpler, more efficient indexing using direct
`(row, col)` access patterns rather than generic coordinate tuples. This makes it
particularly suitable for linear algebra, image processing, and other applications
where 2D structure is fundamental.

Users should typically use `Matrix[dtype]` (i.e., the `Matrix` comptime alias)
rather than instantiating `Matrix` directly.

Type Parameters:
    dtype: The data type of matrix elements (e.g., DType.float32, DType.float64).
           Default is DType.float64. This is a compile-time parameter that determines
           the size and interpretation of stored values.

Memory Layout:
    Matrices can be stored in either:
    - Row-major (C-style) layout: consecutive elements in a row are adjacent in memory
    - Column-major (Fortran-style) layout: consecutive elements in a column are adjacent

    The layout affects cache efficiency for different access patterns and is tracked
    via the `strides` and `flags` attributes.

Indexing and Slicing:
    - `mat[i, j]` - Returns scalar element at row i, column j
    - `mat[i]` - Returns a copy of row i as a new Matrix
    - `mat.get(i)` - Returns a lightweight non-owning view of row i (no copy)
    - `mat[row_slice, col_slice]` - Returns a copy of the submatrix
    - `mat.get(row_slice, col_slice)` - Returns a lightweight non-owning view of the submatrix (no copy)

    Negative indices are supported and follow Python conventions (wrap from end).

The matrix can be uniquely defined by the following features:
    1. The data buffer of all items.
    2. The shape of the matrix.
    3. The data type of the elements (compile-time known).

Attributes:
    - _buf (saved as row-majored, C-type)
    - shape
    - size (shape[0] * shape[1])
    - strides

Default constructor:
- [dtype], shape
- [dtype], data

[checklist] CORE METHODS that have been implemented:
- [x] `Matrix.any` and `mat.logic.all`
- [x] `Matrix.any` and `mat.logic.any`
- [x] `Matrix.argmax` and `mat.sorting.argmax`
- [x] `Matrix.argmin` and `mat.sorting.argmin`
- [x] `Matrix.argsort` and `mat.sorting.argsort`
- [x] `Matrix.astype`
- [x] `Matrix.cumprod` and `mat.mathematics.cumprod`
- [x] `Matrix.cumsum` and `mat.mathematics.cumsum`
- [x] `Matrix.fill` and `mat.creation.full`
- [x] `Matrix.flatten`
- [x] `Matrix.inv` and `mat.linalg.inv`
- [x] `Matrix.max` and `mat.sorting.max`
- [x] `Matrix.mean` and `mat.statistics.mean`
- [x] `Matrix.min` and `mat.sorting.min`
- [x] `Matrix.prod` and `mat.mathematics.prod`
- [x] `Matrix.reshape`
- [x] `Matrix.resize`
- [x] `Matrix.round` and `mat.mathematics.round` (TODO: Check this after next Mojo update)
- [x] `Matrix.std` and `mat.statistics.std`
- [x] `Matrix.sum` and `mat.mathematics.sum`
- [x] `Matrix.trace` and `mat.linalg.trace`
- [x] `Matrix.transpose` and `mat.linalg.transpose` (also `Matrix.T`)
- [x] `Matrix.variance` and `mat.statistics.variance` (`var` is primitive)

**Parameters:**

- `dtype` (`DType`)

#### Fields

- **`shape`** (`Tuple[Int, Int]`): Shape of Matrix.
- **`size`** (`Int`): Size of Matrix.
- **`strides`** (`Tuple[Int, Int]`): Strides of matrix.
- **`offset`** (`Int`): Offset of the first element in the data buffer.
- **`flags`** (`Flags`): Information about the memory layout of the array.

#### Aliases

##### `origin`

```mojo
comptime origin
```

**Value:** `MutExternalOrigin`

Origin of the Matrix.

##### `IteratorType`

```mojo
comptime IteratorType[is_mutable: Bool, forward: Bool]
```

**Value:** `_MatrixIter[dtype, is_mutable, forward]`

Iterator type for the Matrix.

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
__init__(out self, shape: Tuple[Int, Int], order: String = "C")
```

<span class="badge badge-static">static</span>

Initialize a new matrix with the specified shape and memory layout.

This constructor creates a matrix of the given shape without initializing
its data. The memory layout can be specified as either row-major ("C") or
column-major ("F").

Example:
```mojo
from numojo.prelude import *
var mat_c = Matrix[f32](shape=(3, 4), order="C")  # Row-major
var mat_f = Matrix[f32](shape=(3, 4), order="F")  # Column-major
```

**Args:**

- `shape` (`Tuple`): A tuple representing the dimensions of the matrix as (rows, columns).
- `order` (`String`): A string specifying the memory layout. Use "C" for row-major
       (C-style) layout or "F" for column-major (Fortran-style) layout. Defaults to "C".
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 2

```mojo
__init__(out self, var data: Self)
```

<span class="badge badge-static">static</span>

Initialize a new matrix by transferring ownership from another matrix.

This constructor creates a new matrix instance by taking ownership of the
data from an existing matrix. The source matrix (`data`) will no longer
own its data after this operation.

Notes:
- This operation is efficient as it avoids copying the data buffer.
- The source matrix (`data`) becomes invalid after the transfer and should not be used.

Example:
```mojo
from numojo.prelude import *
var mat1 = Matrix[f32](shape=(2, 3))
# ... (initialize mat1 with data) ...
var mat2 = Matrix[f32](mat1^)  # Transfer ownership from mat1 to mat2
```

**Args:**

- `data` (`Self`) `[var]`: The source matrix from which ownership of the data will be transferred.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 3

```mojo
__init__(out self, data: Self)
```

<span class="badge badge-static">static</span>

Construct a new matrix by copying from another matrix.

This initializer creates a new matrix instance by copying the data, shape and order from an existing matrix. The new matrix will have its own independent copy of the data.

**Args:**

- `data` (`Self`): The source matrix to copy from.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 4

```mojo
__init__(out self, data: NDArray[dtype])
```

<span class="badge badge-static">static</span>

Initialize a new matrix by copying data from an existing NDArray.

This constructor creates a matrix instance with the same shape, data, and
memory layout as the provided NDArray. The data is copied into a new memory buffer owned by the matrix.

Example:
```mojo
from numojo.prelude import *
var arr = NDArray[f32](Shape(2, 3))
# ... (initialize arr with data) ...
var mat = Matrix[f32](arr)  # Create a matrix from the NDArray
```

**Args:**

- `data` (`NDArray`): An NDArray instance containing the data to initialize the matrix.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the provided NDArray has more than 2 dimensions, as it cannot be represented as a matrix.

###### Overload 5

```mojo
__init__(out self, var data: DataContainer[dtype], is_view: Bool, shape: Tuple[Int, Int], strides: Tuple[Int, Int], offset: Int)
```

<span class="badge badge-static">static</span>

Initialize a Matrix as either an owning array or a non-owning view.

Notes:
Ownership is determined by the `is_view` flag and the DataContainer's reference count.
- If `is_view` is True, the Matrix is a view and does not own the data.
- If `is_view` is False and the DataContainer's reference count is 1, the Matrix owns the data.

**Args:**

- `data` (`DataContainer`) `[var]`: DataContainer holding the matrix data.
- `is_view` (`Bool`): If True, creates a non-owning view; if False, creates an owning matrix.
- `shape` (`Tuple`): Shape of the matrix as (rows, columns).
- `strides` (`Tuple`): Strides for the matrix.
- `offset` (`Int`): Offset of the first element in the data buffer.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 6

```mojo
__init__(out self, *, copy: Self)
```

<span class="badge badge-static">static</span>

Initialize a new matrix by copying data from ancopy matrix.

This method creates a deep copy of the `copy` matrix into `self`. It ensures that the copied matrix is independent of the source matrix, with its own memory allocation.

Example:
```mojo
from numojo.prelude import *
var mat1 = Matrix[f32](shape=(2, 3))
var mat2 = mat1.copy()
```

**Args:**

- `copy` (`Self`): The source matrix to copy from. Must be an owning matrix.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`

###### Overload 7

```mojo
__init__(out self, *, deinit take: Self)
```

<span class="badge badge-static">static</span>

Transfer ownership of resources from `other` to `self`.

This method moves the data and metadata from the `other` matrix instance
into the current instance (`self`). After the move, the `other` instance
is left in an invalid state and should not be used.

Notes:
- This operation is efficient as it avoids copying data.
- The `other` instance is deinitialized as part of this operation.

**Args:**

- `take` (`Self`) `[deinit]`: The source matrix instance whose resources will be moved.
- `self` (`Self`) `[out]`

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `__del__`

```mojo
__del__(deinit self)
```

Destructor for the matrix instance.

This method is called when the matrix instance is deinitialized. It ensures that resources owned by the matrix, such as its memory buffer, are properly released.

Notes:
- This method only frees resources if the matrix owns its data.
- The `own_data` flag determines whether the memory buffer is freed.

**Args:**

- `self` (`Self`) `[deinit]`


</div>

<div class="fn-card" markdown="1">

##### `__getitem__`

###### Overload 1

```mojo
__getitem__(self, x: Int, y: Int) -> Scalar[dtype]
```

Retrieve the scalar value at the specified row and column indices.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.ones(shape=(3, 4))
var value = mat[1, 2]  # Retrieve value at row 1, column 2
```

**Args:**

- `self` (`Self`)
- `x` (`Int`): The row index. Can be negative to index from the end.
- `y` (`Int`): The column index. Can be negative to index from the end.

**Returns:**

- `Scalar`

!!! failure "Raises"
    Error: If the provided indices are out of bounds for the matrix.

###### Overload 2

```mojo
__getitem__(self, var x: Int) -> Self
```

Retrieve a copy of the specified row in the matrix. This method creates and returns a new `Matrix` instance that contains a copy of the data from the specified row of the original matrix. The returned matrix is a row vector with a shape of (1, number_of_columns).

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.ones(shape=(3, 4))
var row_copy = mat[1]  # Get a copy of the second row
```

**Args:**

- `self` (`Self`)
- `x` (`Int`) `[var]`: The row index to retrieve. Negative indices are supported and follow Python conventions (e.g., -1 refers to the last row).

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the provided row index is out of bounds.

###### Overload 3

```mojo
__getitem__(self, x: Slice, y: Slice) -> Self
```

Retrieve a copy of the specified slice in the matrix. This method creates and returns a new `Matrix` instance that contains a copy of the data from the specified slice of the original matrix. The returned matrix will have the shape determined by the slice ranges.

Notes:
- Out of bounds indices are clamped using the shape of the matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.ones(shape=(4, 4))
var slice_copy = mat[1:3, 0:2]  # Get a copy of the submatrix
```

**Args:**

- `self` (`Self`)
- `x` (`Slice`): The row slice to retrieve. Supports Python slice syntax.
- `y` (`Slice`): The column slice to retrieve. Supports Python slice syntax.

**Returns:**

- `Self`

###### Overload 4

```mojo
__getitem__(self, x: Slice, var y: Int) -> Self
```

Retrieve a copy of a specific column slice in the matrix. This method creates and returns a new `Matrix` instance that contains a copy of the data from the specified and column slice of the original matrix. The returned matrix will have a shape determined by the row slice and a single column.

Notes:
- Negative indices for `y` are normalized to their positive equivalent.
- Out-of-bounds indices for `x` are clamped using the shape of the matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.ones(shape=(4, 4))
var column_copy = mat[0:4, 2]  # Get a copy of the third column
```

**Args:**

- `self` (`Self`)
- `x` (`Slice`): The row slice to retrieve. This defines the range of rows to include in the copy.
- `y` (`Int`) `[var]`: The column index to retrieve. This specifies the column to include in the copy.

**Returns:**

- `Self`

###### Overload 5

```mojo
__getitem__(self, var x: Int, y: Slice) -> Self
```

Retrieve a copy of a specific row slice in the matrix. This method creates and returns a new `Matrix` instance that contains a copy of the data from the specified row and column slice of the original matrix. The returned matrix will have a shape of (1, number_of_columns_in_slice).

Notes:
- Out-of-bounds indices for `y` are clamped using the shape of the matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.ones(shape=(4, 4))
var row_copy = mat[1, 0:3]  # Get a copy of the second row, columns 0 to 2
```

**Args:**

- `self` (`Self`)
- `x` (`Int`) `[var]`: The row index to retrieve. This specifies the row to include in the copy. Negative indices are supported and follow Python conventions (e.g., -1 refers to the last row).
- `y` (`Slice`): The column slice to retrieve. This defines the range of columns to include in the copy.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the provided row index `x` is out of bounds.

###### Overload 6

```mojo
__getitem__(self, indices: List[Int]) -> Self
```

Retrieve a copy of specific rows in the matrix based on the provided indices. This method creates and returns a new `Matrix` instance that contains a copy of the data from the specified rows of the original matrix. The returned matrix will have a shape of (number_of_indices, number_of_columns).

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.ones(shape=(4, 4))
var selected_rows = mat[[0, 1, 0]]  # Get a copy of the
# first and second and first rows in a new matrix with shape (3, 4)
```

**Args:**

- `self` (`Self`)
- `indices` (`List`): A list of row indices to retrieve. Each index specifies a row to include in the resulting matrix. Negative indices are supported and follow Python conventions (e.g., -1 refers to the last row).

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If any of the provided indices are out of bounds.


</div>

<div class="fn-card" markdown="1">

##### `__setitem__`

###### Overload 1

```mojo
__setitem__(mut self, x: Int, y: Int, value: Scalar[dtype])
```

Set the value at the specified row and column indices in the matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.zeros(shape=(3, 4))
mat[1, 2] = 5.0  # Set value at row 1, column 2 to 5.0
```

**Args:**

- `self` (`Self`) `[mut]`
- `x` (`Int`): The row index. Can be negative to index from the end.
- `y` (`Int`): The column index. Can be negative to index from the end.
- `value` (`Scalar`): The value to set at the specified position.

!!! failure "Raises"
    Error: If the provided indices are out of bounds for the matrix.

###### Overload 2

```mojo
__setitem__(self, var x: Int, value: Self)
```

Assign a row in the matrix at the specified index with the given matrix. This method replaces the row at the specified index `x` with the data from the provided `value` matrix. The `value` matrix must be a row vector with the same number of columns as the target matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.zeros(shape=(3, 4))
var row_vector = Matrix.ones(shape=(1, 4))
mat[1] = row_vector  # Set the second row of mat to row_vector
```

**Args:**

- `self` (`Self`)
- `x` (`Int`) `[var]`: The row index where the data will be assigned. Negative indices are
   supported and follow Python conventions (e.g., -1 refers to the last row).
- `value` (`Self`): A `Matrix` instance representing the row vector to assign.
       The `value` matrix can be in either C-contiguous or F-contiguous order.

!!! failure "Raises"
    Error: If the row index `x` is out of bounds.
Error: If the `value` matrix does not have exactly one row.
Error: If the number of columns in the `value` matrix does not match
the number of columns in the target matrix.

###### Overload 3

```mojo
__setitem__(self, x: Slice, y: Int, value: Self)
```

Assign values to a column in the matrix at the specified column index `y` and row slice `x` with the given matrix. This method replaces the values in the specified column and row slice with the data from the provided `value` matrix.

Notes:
- Out of bound slice `x` is clamped using the shape of the matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.zeros(shape=(4, 4))
var col_vector = Matrix.ones(shape=(4, 1))
mat[0:4, 2] = col_vector  # Set the third column of mat to col_vector
```

**Args:**

- `self` (`Self`)
- `x` (`Slice`): The row slice where the data will be assigned. Supports Python slice syntax (e.g., `start:stop:step`).
- `y` (`Int`): The column index where the data will be assigned. Negative indices
   are supported and follow Python conventions (e.g., -1 refers to the
   last column).
- `value` (`Self`): A `Matrix` instance representing the column vector to assign.
       The `value` matrix must have the same number of rows as the
       specified slice `x` and exactly one column.

!!! failure "Raises"
    Error: If the column index `y` is out of bounds.
Error: If the shape of the `value` matrix does not match the target
slice dimensions.

###### Overload 4

```mojo
__setitem__(self, x: Int, y: Slice, value: Self)
```

Assign values to a row in the matrix at the specified row index `x` and column slice `y` with the given matrix. This method replaces the values in the specified row and column slice with the data from the provided `value` matrix.

Notes:
- Out of bound slice `y` is clamped using the shape of the matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.zeros(shape=(4, 4))
var row_vector = Matrix.ones(shape=(1, 3))
mat[1, 0:3] = row_vector  # Set the second row, columns 0 to 2 of mat to row_vector
```

**Args:**

- `self` (`Self`)
- `x` (`Int`): The row index where the data will be assigned. Negative indices
   are supported and follow Python conventions (e.g., -1 refers to the
   last row).
- `y` (`Slice`): The column slice where the data will be assigned. Supports Python slice syntax (e.g., `start:stop:step`).
- `value` (`Self`): A `Matrix` instance representing the row vector to assign.
       The `value` matrix must have the same number of columns as the
       specified slice `y` and exactly one row.

!!! failure "Raises"
    Error: If the row index `x` is out of bounds.
Error: If the shape of the `value` matrix does not match the target
slice dimensions.

###### Overload 5

```mojo
__setitem__(self, x: Slice, y: Slice, value: Self)
```

Assign values to a submatrix of the matrix defined by row slice `x` and column slice `y` using the provided `value` matrix. This method replaces the elements in the specified row and column slices with the corresponding elements from `value`.

Notes:
- Out of bounds slices are clamped using the shape of the matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.zeros(shape=(4, 4))
var submatrix = Matrix.ones(shape=(2, 2))
mat[1:3, 1:3] = submatrix  # Set the 2x2 submatrix starting at (1,1) to ones
```

**Args:**

- `self` (`Self`)
- `x` (`Slice`): Row slice specifying which rows to assign to. Supports Python slice syntax (e.g., `start:stop:step`).
- `y` (`Slice`): Column slice specifying which columns to assign to. Supports Python slice syntax (e.g., `start:stop:step`).
- `value` (`Self`): A `Matrix` instance containing the values to assign.

!!! failure "Raises"
    Error: If the shape of `value` does not match the shape of the target slice.


</div>

<div class="fn-card" markdown="1">

##### `__lt__`

###### Overload 1

```mojo
__lt__(self, other: Self) -> Matrix[DType.bool]
```

Compare two matrices element-wise for less-than.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
var B = Matrix.ones(shape=(4, 4)) * 2
print(A < B)
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Matrix to compare with self. Must be broadcastable to self's shape.

**Returns:**

- `Matrix`

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__lt__(self, other: Scalar[dtype]) -> Matrix[DType.bool]
```

Compare each element of the matrix to a scalar for less-than.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
print(A < 2)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to compare.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__le__`

###### Overload 1

```mojo
__le__(self, other: Self) -> Matrix[DType.bool]
```

Compare two matrices element-wise for less-than-or-equal.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
var B = Matrix.ones(shape=(4, 4)) * 2
print(A <= B)
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Matrix to compare with self. Must be broadcastable to self's shape.

**Returns:**

- `Matrix`

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__le__(self, other: Scalar[dtype]) -> Matrix[DType.bool]
```

Compare each element of the matrix to a scalar for less-than-or-equal.

Example:
```mojo
from numojo.prelude import *
A = Matrix.ones(shape=(4, 4))
print(A <= 2)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to compare.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__eq__`

###### Overload 1

```mojo
__eq__(self, other: Self) -> Matrix[DType.bool]
```

Compare two matrices element-wise for equality.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
var B = Matrix.ones(shape=(4, 4))
print(A == B)
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Matrix to compare with self. Must be broadcastable to self's shape.

**Returns:**

- `Matrix`

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__eq__(self, other: Scalar[dtype]) -> Matrix[DType.bool]
```

Compare each element of the matrix to a scalar for equality.

Example:
```mojo
from numojo.prelude import *
A = Matrix.ones(shape=(4, 4))
print(A == 2)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to compare.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__ne__`

###### Overload 1

```mojo
__ne__(self, other: Self) -> Matrix[DType.bool]
```

Compare two matrices element-wise for inequality.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
var B = Matrix.ones(shape=(4, 4))
print(A != B)
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Matrix to compare with self. Must be broadcastable to self's shape.

**Returns:**

- `Matrix`

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__ne__(self, other: Scalar[dtype]) -> Matrix[DType.bool]
```

Compare each element of the matrix to a scalar for inequality.

Example:
```mojo
from numojo.prelude import *
A = Matrix.ones(shape=(4, 4))
print(A != 2)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to compare.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__gt__`

###### Overload 1

```mojo
__gt__(self, other: Self) -> Matrix[DType.bool]
```

Compare two matrices element-wise for greater-than.

Example:
```mojo
from numojo.prelude import *
A = Matrix.ones(shape=(4, 4))
B = Matrix.ones(shape=(4, 4)) * 2
print(A > B)
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Matrix to compare with self. Must be broadcastable to self's shape.

**Returns:**

- `Matrix`

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__gt__(self, other: Scalar[dtype]) -> Matrix[DType.bool]
```

Compare each element of the matrix to a scalar for greater-than.

Example:
```mojo
from numojo.prelude import *
A = Matrix.ones(shape=(4, 4))
print(A > 2)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to compare.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__ge__`

###### Overload 1

```mojo
__ge__(self, other: Self) -> Matrix[DType.bool]
```

Compare two matrices element-wise for greater-than-or-equal.

Example:
```mojo
from numojo.prelude import *
A = Matrix.ones(shape=(4, 4))
B = Matrix.ones(shape=(4, 4)) * 2
print(A >= B)
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Matrix to compare with self. Must be broadcastable to self's shape.

**Returns:**

- `Matrix`

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__ge__(self, other: Scalar[dtype]) -> Matrix[DType.bool]
```

Compare each element of the matrix to a scalar for greater-than-or-equal.

Example:
```mojo
from numojo.prelude import *
A = Matrix.ones(shape=(4, 4))
print(A >= 2)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to compare.

**Returns:**

- `Matrix`

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.


</div>

<div class="fn-card" markdown="1">

##### `__add__`

###### Overload 1

```mojo
__add__(self, other: Self) -> Self
```

Add two matrices element-wise.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
var B = Matrix.ones(shape=(4, 4))
print(A + B)
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Matrix to add to self. Must be broadcastable to self's shape.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__add__(self, other: Scalar[dtype]) -> Self
```

Add a scalar to every element of the matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
print(A + 2)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to add.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__sub__`

###### Overload 1

```mojo
__sub__(self, other: Self) -> Self
```

Subtract two matrices element-wise.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
var B = Matrix.ones(shape=(4, 4))
print(A - B)
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Matrix to subtract from self. Must be broadcastable to self's shape.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__sub__(self, other: Scalar[dtype]) -> Self
```

Subtract a scalar from every element of the matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
print(A - 2)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to subtract.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__mul__`

###### Overload 1

```mojo
__mul__(self, other: Self) -> Self
```

Multiply two matrices element-wise.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
var B = Matrix.ones(shape=(4, 4))
print(A * B)
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Matrix to multiply with self. Must be broadcastable to self's shape.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__mul__(self, other: Scalar[dtype]) -> Self
```

Multiply matrix by scalar.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
print(A * 2)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to multiply.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__matmul__`

```mojo
__matmul__(self, other: Self) -> Self
```

Matrix multiplication using the @ operator.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 3))
var B = Matrix.ones(shape=(3, 2))
print(A @ B)
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): The matrix to multiply with self.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the shapes are not compatible for matrix multiplication.


</div>

<div class="fn-card" markdown="1">

##### `__truediv__`

###### Overload 1

```mojo
__truediv__(self, other: Self) -> Self
```

Divide two matrices element-wise.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
var B = Matrix.ones(shape=(4, 4))
print(A / B)
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Matrix to divide self by. Must be broadcastable to self's shape.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__truediv__(self, other: Scalar[dtype]) -> Self
```

Divide matrix by scalar.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
print(A / 2)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to divide each element of the matrix by.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__floordiv__`

###### Overload 1

```mojo
__floordiv__(self, other: Self) -> Self
```

Floor divide two matrices element-wise.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.full[f64](shape=(4, 4), fill_value=7.0)
var B = Matrix.full[f64](shape=(4, 4), fill_value=2.0)
print(A // B)  # Element-wise floor division
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Matrix to divide by. Must be broadcastable to self's shape.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__floordiv__(self, other: Scalar[dtype]) -> Self
```

Floor divide matrix by scalar.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.full[f64](shape=(4, 4), fill_value=7.0)
print(A // 2)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to divide each element by.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__mod__`

###### Overload 1

```mojo
__mod__(self, other: Self) -> Self
```

Compute element-wise modulo of two matrices.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.full[f64](shape=(4, 4), fill_value=7.0)
var B = Matrix.full[f64](shape=(4, 4), fill_value=3.0)
print(A % B)  # Element-wise modulo
```

**Args:**

- `self` (`Self`)
- `other` (`Self`): Matrix to compute modulo with. Must be broadcastable to self's shape.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__mod__(self, other: Scalar[dtype]) -> Self
```

Compute element-wise modulo of matrix with scalar.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.full[f64](shape=(4, 4), fill_value=7.0)
print(A % 3)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to compute modulo with.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__pow__`

```mojo
__pow__(self, rhs: Scalar[dtype]) -> Self
```

Raise each element of the matrix to the power of `rhs`.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
print(A ** 2)
```

**Args:**

- `self` (`Self`)
- `rhs` (`Scalar`): The scalar exponent to which each element of the matrix will be raised.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__radd__`

```mojo
__radd__(self, other: Scalar[dtype]) -> Self
```

Add a matrix to a scalar (right-hand side).

Example:
```mojo
from numojo.prelude import *
A = Matrix.ones(shape=(4, 4))
print(2 + A)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to add.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__rsub__`

```mojo
__rsub__(self, other: Scalar[dtype]) -> Self
```

Subtract a matrix from a scalar (right-hand side).

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
print(2 - A)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to subtract from.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__rmul__`

```mojo
__rmul__(self, other: Scalar[dtype]) -> Self
```

Multiply scalar by matrix (right-hand side).

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
print(2 * A)
```

**Args:**

- `self` (`Self`)
- `other` (`Scalar`): Scalar value to multiply.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `__iadd__`

###### Overload 1

```mojo
__iadd__(mut self, other: Self)
```

Add another matrix to this matrix in-place.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
var B = Matrix.ones(shape=(4, 4))
A += B  # A is modified in-place
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`): Matrix to add. Must be broadcastable to self's shape.

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__iadd__(mut self, other: Scalar[dtype])
```

Add a scalar to this matrix in-place.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
A += 2  # A is modified in-place
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`): Scalar value to add to each element.


</div>

<div class="fn-card" markdown="1">

##### `__isub__`

###### Overload 1

```mojo
__isub__(mut self, other: Self)
```

Subtract another matrix from this matrix in-place.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
var B = Matrix.ones(shape=(4, 4))
A -= B  # A is modified in-place
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`): Matrix to subtract. Must be broadcastable to self's shape.

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__isub__(mut self, other: Scalar[dtype])
```

Subtract a scalar from this matrix in-place.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
A -= 2  # A is modified in-place
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`): Scalar value to subtract from each element.


</div>

<div class="fn-card" markdown="1">

##### `__imul__`

###### Overload 1

```mojo
__imul__(mut self, other: Self)
```

Multiply this matrix by another matrix element-wise in-place.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
var B = Matrix.full(shape=(4, 4), fill_value=2)
A *= B  # A is modified in-place
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`): Matrix to multiply with. Must be broadcastable to self's shape.

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__imul__(mut self, other: Scalar[dtype])
```

Multiply this matrix by a scalar in-place.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
A *= 2  # A is modified in-place
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`): Scalar value to multiply each element by.


</div>

<div class="fn-card" markdown="1">

##### `__itruediv__`

###### Overload 1

```mojo
__itruediv__(mut self, other: Self)
```

Divide this matrix by another matrix element-wise in-place.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
var B = Matrix.full(shape=(4, 4), fill_value=2)
A /= B  # A is modified in-place
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`): Matrix to divide by. Must be broadcastable to self's shape.

!!! failure "Raises"
    Error: If the shapes are not compatible for broadcasting.

###### Overload 2

```mojo
__itruediv__(mut self, other: Scalar[dtype])
```

Divide this matrix by a scalar in-place.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones(shape=(4, 4))
A /= 2  # A is modified in-place
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`): Scalar value to divide each element by.


</div>

<div class="fn-card" markdown="1">

##### `__ifloordiv__`

###### Overload 1

```mojo
__ifloordiv__(mut self, other: Self)
```

Floor divide this matrix by another matrix element-wise in-place.

Example:
```mojo
from numojo.prelude import *
from numojo.prelude import *
var A = Matrix.full[f64](shape=(4, 4), fill_value=7.0)
var B = Matrix.full[f64](shape=(4, 4), fill_value=2.0)
A //= B  # A is modified in-place
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`): Matrix to divide by. Must be same shape as self.

!!! failure "Raises"
    Error: If the shapes do not match.

###### Overload 2

```mojo
__ifloordiv__(mut self, other: Scalar[dtype])
```

Floor divide this matrix by a scalar in-place.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.full[f64](shape=(4, 4), fill_value=7.0)
A //= 2  # A is modified in-place
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`): Scalar value to divide each element by.


</div>

<div class="fn-card" markdown="1">

##### `__imod__`

###### Overload 1

```mojo
__imod__(mut self, other: Self)
```

Compute element-wise modulo with another matrix in-place.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.full[f64](shape=(4, 4), fill_value=7.0)
var B = Matrix.full[f64](shape=(4, 4), fill_value=3.0)
A %= B  # A is modified in-place
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Self`): Matrix to compute modulo with. Must be same shape as self.

!!! failure "Raises"
    Error: If the shapes do not match.

###### Overload 2

```mojo
__imod__(mut self, other: Scalar[dtype])
```

Compute element-wise modulo with a scalar in-place.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.full[f64](shape=(4, 4), fill_value=7.0)
A %= 3  # A is modified in-place
```

**Args:**

- `self` (`Self`) `[mut]`
- `other` (`Scalar`): Scalar value to compute modulo with.


</div>

<div class="fn-card" markdown="1">

##### `deep_copy`

```mojo
deep_copy(self) -> Self
```

Returns a deep copy of the matrix.

The new matrix has its own independent data buffer, shape, and strides.

Example:
```mojo
import numojo as nm
var mat1 = nm.Matrix[nm.f32](shape=(2, 3))
var mat2 = mat1.deep_copy()
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `view`

```mojo
view(mut self) -> Self
```

Returns a non-owning view of the current matrix.

The view shares the underlying data buffer with the original matrix and does not allocate new memory.

Example:
```mojo
import numojo as nm
var mat = nm.Matrix[nm.f32](shape=(3, 4))
var mat_view = mat.view()
```

**Args:**

- `self` (`Self`) `[mut]`

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `validate_and_normalize`

```mojo
validate_and_normalize(self, x: Int, y: Int) -> Tuple[Int, Int]
```

Validate and normalize the provided row and column indices.

This method checks if the given indices are within the bounds of the matrix shape.
If an index is negative, it is normalized to its positive equivalent.

**Args:**

- `self` (`Self`)
- `x` (`Int`): The row index. Can be negative to index from the end.
- `y` (`Int`): The column index. Can be negative to index from the end.

**Returns:**

- `Tuple`

!!! failure "Raises"
    Error: If any of the provided indices are out of bounds for the matrix.


</div>

<div class="fn-card" markdown="1">

##### `get`

###### Overload 1

```mojo
get(mut self, var x: Int) -> Self
```

Retrieve a view of the specified row in the matrix. This method returns a non-owning `Matrix` that references the data of the specified row in the original matrix. The view does not allocate new memory and directly points to the existing data buffer of the matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.ones(shape=(3, 4))
var row_view = mat.get(1)  # Get a view of the second row
```

**Args:**

- `self` (`Self`) `[mut]`
- `x` (`Int`) `[var]`: The row index to retrieve. Negative indices are supported and follow Python conventions (e.g., -1 refers to the last row).

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the provided row index is out of bounds.

###### Overload 2

```mojo
get(mut self, x: Slice, y: Slice) -> Self
```

Retrieve a view of the specified slice in the matrix.

This method returns a non-owning `Matrix` that references the data of the specified row in the original matrix. The view does not allocate new memory and directly points to the existing data buffer of the matrix.

Notes:
- Out of bounds indices are clamped using the shape of the matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.ones(shape=(4, 4))
var slice_view = mat.get(Slice(1, 3), Slice(0, 2))  # Get a view of the submatrix
```

**Args:**

- `self` (`Self`) `[mut]`
- `x` (`Slice`): The row slice to retrieve.
- `y` (`Slice`): The column slice to retrieve.

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 3

```mojo
get(mut self, x: Slice, var y: Int) -> Self
```

Retrieve a view of a specific column slice in the matrix. This method returns a non-owning `Matrix` that references the data of the specified column slice in the original matrix. The view does not allocate new memory and directly points to the existing data buffer of the matrix.

Notes:
- Out-of-bounds indices for `x` are clamped using the shape of the matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.ones(shape=(4, 4))
var column_view = mat.get(Slice(0, 4), 2)  # Get a view of the third column
```

**Args:**

- `self` (`Self`) `[mut]`
- `x` (`Slice`): The row slice to retrieve. This defines the range of rows to include in the view.
- `y` (`Int`) `[var]`: The column index to retrieve. This specifies the column to include in the view.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the provided column index `y` is out of bounds.

###### Overload 4

```mojo
get(mut self, var x: Int, y: Slice) -> Self
```

Retrieve a view of a specific row slice in the matrix. This method returns a non-owning `Matrix` that references the data of the specified row slice in the original matrix. The view does not allocate new memory and directly points to the existing data buffer of the matrix.

Notes:
- Out-of-bounds indices for `y` are clamped using the shape of the matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.ones(shape=(4, 4))
var row_view = mat.get(1, Slice(0, 3))  # Get a view of the second row, columns 0 to 2
```

**Args:**

- `self` (`Self`) `[mut]`
- `x` (`Int`) `[var]`: The row index to retrieve. This specifies the row to include in the view. Negative indices are supported and follow Python conventions (e.g., -1 refers to the last row).
- `y` (`Slice`): The column slice to retrieve. This defines the range of columns to include in the view.

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the provided row index `x` is out of bounds.


</div>

<div class="fn-card" markdown="1">

##### `load`

```mojo
load[width: Int = 1](self, idx: Int) -> SIMD[dtype, __result__.width]
```

Load a SIMD element from the matrix at the specified linear index.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.ones(shape=(4, 4))
var simd_element = mat.load[4](2)  # Load a SIMD element of width 4 from index 2
```

**Parameters:**

- `width` (`Int`): The width of the SIMD element to load. Defaults to 1.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The linear index of the element to load. Negative indices are supported and follow Python conventions.

**Returns:**

- `SIMD`

!!! failure "Raises"
    Error: If the provided index is out of bounds.


</div>

<div class="fn-card" markdown="1">

##### `set`

###### Overload 1

```mojo
set(self, var x: Int, value: Self)
```

Assign a row in the matrix at the specified index with the given matrix. This method replaces the row at the specified index `x` with the data from the provided `value` matrix. The `value` matrix must be a row vector with the same number of columns as the target matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.zeros(shape=(3, 4))
var row_vector = Matrix.ones(shape=(1, 4))
mat.set(1, row_vector)  # Set the second row of mat to row_vector

var view = row_vector.view() # create a view of row_vector
mat.set(2, view)  # Set the third row of mat to the view
```

**Args:**

- `self` (`Self`)
- `x` (`Int`) `[var]`: The row index where the data will be assigned. Negative indices are
   supported and follow Python conventions (e.g., -1 refers to the last row).
- `value` (`Self`): A `Matrix` instance representing the row vector to assign.
       The `value` matrix can be in either C-contiguous or F-contiguous order.

!!! failure "Raises"
    Error: If the row index `x` is out of bounds.
Error: If the `value` matrix does not have exactly one row.
Error: If the number of columns in the `value` matrix does not match
the number of columns in the target matrix.

###### Overload 2

```mojo
set(self, x: Slice, y: Int, value: Self)
```

Assign values to a column in the matrix at the specified column index `y` and row slice `x` with the given matrix. This method replaces the values in the specified column and row slice with the data from the provided `value` matrix.

Notes:
- Out of bound slice `x` is clamped using the shape of the matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.zeros(shape=(4, 4))
var col_vector = Matrix.ones(shape=(4, 1))
mat.set(Slice(0, 4), 2, col_vector)  # Set the third column of mat to col_vector

var view = col_vector.view() # create a view of col_vector
mat.set(Slice(0, 4), 3, view)  # Set the fourth column of mat to the view
```

**Args:**

- `self` (`Self`)
- `x` (`Slice`): The row slice where the data will be assigned. Supports Python slice syntax (e.g., `start:stop:step`).
- `y` (`Int`): The column index where the data will be assigned. Negative indices
   are supported and follow Python conventions (e.g., -1 refers to the
   last column).
- `value` (`Self`): A `Matrix` instance representing the column vector to assign.
       The `value` matrix must have the same number of rows as the
       specified slice `x` and exactly one column.

!!! failure "Raises"
    Error: If the column index `y` is out of bounds.
Error: If the shape of the `value` matrix does not match the target
slice dimensions.

###### Overload 3

```mojo
set(self, x: Int, y: Slice, value: Self)
```

Assign values to a row in the matrix at the specified row index `x` and column slice `y` with the given matrix. This method replaces the values in the specified row and column slice with the data from the provided `value` matrix.

Notes:
- Out of bound slice `y` is clamped using the shape of the matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.zeros(shape=(4, 4))
var row_vector = Matrix.ones(shape=(1, 3))
mat.set(1, Slice(0, 3), row_vector)  # Set the second row, columns 0 to 2 of mat to row_vector

var view = row_vector.view() # create a view of row_vector
mat.set(2, Slice(0, 3), view)  # Set the third row, columns 0 to 2 of mat to the view
```

**Args:**

- `self` (`Self`)
- `x` (`Int`): The row index where the data will be assigned. Negative indices
   are supported and follow Python conventions (e.g., -1 refers to the
   last row).
- `y` (`Slice`): The column slice where the data will be assigned. Supports Python slice syntax (e.g., `start:stop:step`).
- `value` (`Self`): A `Matrix` instance representing the row vector to assign.
       The `value` matrix must have the same number of columns as the
       specified slice `y` and exactly one row.

!!! failure "Raises"
    Error: If the row index `x` is out of bounds.
Error: If the shape of the `value` matrix does not match the target
slice dimensions.

###### Overload 4

```mojo
set(self, x: Slice, y: Slice, value: Self)
```

Assign values to a submatrix of the matrix defined by row slice `x` and column slice `y` using the provided `value` matrix. This method replaces the elements in the specified row and column slices with the corresponding elements from `value`.

Notes:
- Out of bounds slices are clamped using the shape of the matrix.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.zeros(shape=(4, 4))
var submatrix = Matrix.ones(shape=(2, 2))
mat.set(Slice(1, 3), Slice(1, 3), submatrix)  # Set the 2x2 submatrix starting at (1,1) to ones

var view = submatrix.view() # create a view of submatrix
mat.set(Slice(2, 4), Slice(2, 4), view
)  # Set the 2x2 submatrix starting at (2,2) to the view
```

**Args:**

- `self` (`Self`)
- `x` (`Slice`): Row slice specifying which rows to assign to. Supports Python slice syntax (e.g., `start:stop:step`).
- `y` (`Slice`): Column slice specifying which columns to assign to. Supports Python slice syntax (e.g., `start:stop:step`).
- `value` (`Self`): A `Matrix` instance containing the values to assign.

!!! failure "Raises"
    Error: If the shape of `value` does not match the shape of the target slice.


</div>

<div class="fn-card" markdown="1">

##### `store`

```mojo
store[width: Int = 1](self, idx: Int, val: SIMD[dtype, val.width])
```

Store a SIMD element into the matrix at the specified linear index.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.ones(shape=(4, 4))
var simd_element = SIMD[f64, 4](2.0, 2.0, 2.0, 2.0)
mat.store[4](2, simd_element)  # Store a SIMD element of width 4 at index 2
```

**Parameters:**

- `width` (`Int`): The width of the SIMD element to store. Defaults to 1.

**Args:**

- `self` (`Self`)
- `idx` (`Int`): The linear index where the element will be stored. Negative indices are supported and follow Python conventions.
- `val` (`SIMD`): The SIMD element to store at the given index.

!!! failure "Raises"
    Error: If the provided index is out of bounds.


</div>

<div class="fn-card" markdown="1">

##### `__iter__`

```mojo
__iter__(ref self) -> _MatrixIter[dtype, True]
```

Returns an iterator over the rows of the Matrix. Each iteration yields a Matrix representing a single row.

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.rand((4, 4))
for row in mat:
    print(row)  # Each row is a Matrix
```

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_MatrixIter`


</div>

<div class="fn-card" markdown="1">

##### `__len__`

```mojo
__len__(self) -> Int
```

Return the number of rows in the matrix (length of the first dimension).

Example:
```mojo
from numojo.prelude import *
var mat = Matrix.rand((4, 4))
print(len(mat))  # Outputs: 4
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Int`


</div>

<div class="fn-card" markdown="1">

##### `__reversed__`

```mojo
__reversed__(ref self) -> _MatrixIter[dtype, True, False]
```

Return an iterator that traverses the matrix rows in reverse order.

**Args:**

- `self` (`Self`) `[ref]`

**Returns:**

- `_MatrixIter`


</div>

<div class="fn-card" markdown="1">

##### `__str__`

```mojo
__str__(self) -> String
```

Return a string representation of the matrix.

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

Write the string representation of the matrix to a writer.

**Parameters:**

- `W` (`Writer`)

**Args:**

- `self` (`Self`)
- `writer` (`W`) `[mut]`: The writer to output the matrix string to.


</div>

<div class="fn-card" markdown="1">

##### `all`

###### Overload 1

```mojo
all(self) -> Scalar[dtype]
```

Returns True if all elements of the matrix evaluate to True.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist([Float64(1), 1, 1, 1, 1], (5, 1))
print(A.all())  # Outputs: True
var B = Matrix.fromlist([Float64(1), 0, 2, 3, 4], (5, 1))
print(B.all())  # Outputs: False
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

###### Overload 2

```mojo
all(self, axis: Int) -> Self
```

Returns a matrix indicating whether all elements along the specified axis evaluate to True.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist(
   [Float64(1), 1, 1, 0, 1, 3], (2, 3)
)
print(A.all(axis=0))  # Outputs: [[0, 1, 1]]
print(A.all(axis=1))  # Outputs: [[1], [0]]
```

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which to perform the test.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `any`

###### Overload 1

```mojo
any(self) -> Scalar[dtype]
```

Returns True if any element of the matrix evaluates to True.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist([Float64(0), 0, 0, 0, 0], (5, 1))
print(A.any())  # Outputs: False
var B = Matrix.fromlist([Float64(0), 2, 0, 0, 0], (5, 1))
print(B.any())  # Outputs: True
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

###### Overload 2

```mojo
any(self, axis: Int) -> Self
```

Returns a matrix indicating whether any element along the specified axis evaluates to True.

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which to perform the test.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `argmax`

###### Overload 1

```mojo
argmax(self) -> Scalar[DType.int]
```

Returns the index of the maximum element in the flattened matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist([Float64(1), 3, 2, 5, 4], (5, 1))
print(A.argmax())  # Outputs: 3
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
argmax(self, axis: Int) -> Matrix[DType.int]
```

Returns the indices of the maximum elements along the specified axis.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist([Float64(1), 3, 2, 5, 4, 6], (2, 3))
print(A.argmax(axis=0))  # Outputs: [[1, 1, 1]]
print(A.argmax(axis=1))  # Outputs: [[1], [2]]
```

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which to find the maximum.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `argmin`

###### Overload 1

```mojo
argmin(self) -> Scalar[DType.int]
```

Returns the index of the minimum element in the flattened matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist([Float64(3), 1, 4, 2, 5], (5, 1))
print(A.argmin())  # Outputs: 1
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
argmin(self, axis: Int) -> Matrix[DType.int]
```

Returns the indices of the minimum elements along the specified axis.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist([Float64(3), 1, 4, 2, 5, 0], (2, 3))
print(A.argmin(axis=0))  # Outputs: [[1, 1, 1]]
print(A.argmin(axis=1))  # Outputs: [[1], [2]]
```

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which to find the minimum.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `argsort`

###### Overload 1

```mojo
argsort(self) -> Matrix[DType.int]
```

Returns the indices that would sort the flattened matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist([Float64(3), 1, 4, 2], (4, 1))
print(A.argsort())  # Outputs: [[1, 3, 0, 2]]
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Matrix`

!!! failure "Raises"

###### Overload 2

```mojo
argsort(self, axis: Int) -> Matrix[DType.int]
```

Returns the indices that would sort the matrix along the specified axis.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist([Float64(3), 1, 4, 2, 5, 0], (2, 3))
print(A.argsort(axis=0))  # Outputs: [[1, 1, 1], [0, 0, 0]]
print(A.argsort(axis=1))  # Outputs: [[1, 3, 0], [2, 0, 1]]
```

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which to sort.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `astype`

```mojo
astype[asdtype: DType](self) -> Matrix[asdtype]
```

Returns a copy of the matrix cast to the specified data type.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist([Float32(1.5), 2.5, 3.5], (3, 1))
var B = A.astype[i8]()
print(B)  # Outputs a Matrix[i8] with values [[1], [2], [3]]
```

**Parameters:**

- `asdtype` (`DType`): The target data type to cast to.

**Args:**

- `self` (`Self`)

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

##### `cumprod`

###### Overload 1

```mojo
cumprod(self) -> Self
```

Compute the cumulative product of all elements in the matrix, flattened into a single dimension.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(100, 100))
print(A.cumprod())
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
cumprod(self, axis: Int) -> Self
```

Compute the cumulative product of elements along a specified axis.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(100, 100))
print(A.cumprod(axis=0))
print(A.cumprod(axis=1))
```

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which to compute the cumulative product (0 for rows, 1 for columns).

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

Compute the cumulative sum of all elements in the matrix, flattened into a single dimension.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(100, 100))
print(A.cumsum())
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"

###### Overload 2

```mojo
cumsum(self, axis: Int) -> Self
```

Compute the cumulative sum of elements along a specified axis.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(100, 100))
print(A.cumsum(axis=0))
print(A.cumsum(axis=1))
```

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which to compute the cumulative sum (0 for rows, 1 for columns).

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `fill`

```mojo
fill(self, fill_value: Scalar[dtype])
```

Fill the matrix with the specified value. This method sets every element of the matrix to `fill_value`.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand((3, 3))
A.fill(5)
print(A)
```

See also: `Matrix.full`

**Args:**

- `self` (`Self`)
- `fill_value` (`Scalar`): The value to assign to every element of the matrix.


</div>

<div class="fn-card" markdown="1">

##### `flatten`

```mojo
flatten(self) -> Self
```

Return a flattened copy of the matrix. This method returns a new matrix containing all elements of the original matrix in a single row (shape (1, size)), preserving the order.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand((2, 3))
print(A.flatten())
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `inv`

```mojo
inv(self) -> Self
```

Compute the inverse of the matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand((3, 3))
print(A.inv())
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the matrix is not square or not invertible.


</div>

<div class="fn-card" markdown="1">

##### `order`

```mojo
order(self) -> String
```

Return the memory layout order of the matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand((3, 3), order="F")
print(A.order())  # "F"
```

**Args:**

- `self` (`Self`)

**Returns:**

- `String`


</div>

<div class="fn-card" markdown="1">

##### `is_c_contiguous`

```mojo
is_c_contiguous(self) -> Bool
```

Checks if the matrix is strictly C-contiguous (dense row-major).

For a 2-D matrix this means `strides == (shape[1], 1)`.

Computed from the current strides and shape (not cached flags),
so the result is always up-to-date.

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

Checks if the matrix is strictly F-contiguous (dense column-major).

For a 2-D matrix this means `strides == (1, shape[0])`.

Computed from the current strides and shape (not cached flags).

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

Checks if elements within each row are contiguous.

This is a relaxation of C-contiguous: only `stride[1] == 1`.
Rows may have padding between them.

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

Checks if elements within each column are contiguous.

This is a relaxation of F-contiguous: only `stride[0] == 1`.
Columns may have padding between them.

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `contiguous`

```mojo
contiguous(self) -> Self
```

Returns a new C-contiguous matrix owning a copy of the data.

Always creates a new owned matrix, even if the source is already
C-contiguous. This ensures consistent behavior.

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `max`

###### Overload 1

```mojo
max(self) -> Scalar[dtype]
```

Return the maximum element in the matrix.

The matrix is flattened before finding the maximum.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand((3, 3))
print(A.max())
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
max(self, axis: Int) -> Self
```

Return the maximum values along the specified axis.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand((3, 3))
print(A.max(axis=0))  # Max of each column
print(A.max(axis=1))  # Max of each row
```

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which to compute the maximum (0 for rows, 1 for columns).

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

Compute the arithmetic mean of all elements in the matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(100, 100))
print(A.mean())
```

**Parameters:**

- `returned_dtype` (`DType`)

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
mean[returned_dtype: DType = DType.float64](self, axis: Int) -> Matrix[returned_dtype]
```

Compute the arithmetic mean along the specified axis.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(100, 100))
print(A.mean(axis=0))
print(A.mean(axis=1))
```

**Parameters:**

- `returned_dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which to compute the mean (0 for rows, 1 for columns).

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `min`

###### Overload 1

```mojo
min(self) -> Scalar[dtype]
```

Return the minimum element in the matrix.

The matrix is flattened before finding the minimum.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand((3, 3))
print(A.min())
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
min(self, axis: Int) -> Self
```

Return the minimum values along the specified axis.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand((3, 3))
print(A.min(axis=0))  # Min of each column
print(A.min(axis=1))  # Min of each row
```

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which to compute the minimum (0 for rows, 1 for columns).

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `prod`

###### Overload 1

```mojo
prod(self) -> Scalar[dtype]
```

Compute the product of all elements in the matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(100, 100))
print(A.prod())
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

###### Overload 2

```mojo
prod(self, axis: Int) -> Self
```

Compute the product of elements along the specified axis.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(100, 100))
print(A.prod(axis=0))
print(A.prod(axis=1))
```

**Args:**

- `self` (`Self`)
- `axis` (`Int`): The axis along which to compute the product (0 for rows, 1 for columns).

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `reshape`

```mojo
reshape(self, shape: Tuple[Int, Int], order: String = "C") -> Self
```

Return a new matrix with the specified shape containing the same data.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(4, 4))
var B = A.reshape((2, 8))
print(B)
```

**Args:**

- `self` (`Self`)
- `shape` (`Tuple`): Tuple of (rows, columns) specifying the new shape.
- `order` (`String`): Memory layout order of the new matrix. "C" for C-contiguous, "F" for F-contiguous. Default is "C".

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the total number of elements does not match the original matrix size.


</div>

<div class="fn-card" markdown="1">

##### `resize`

```mojo
resize(mut self, shape: Tuple[Int, Int])
```

Change the shape and size of the matrix in-place.

Notes:
- If the new shape is larger, the matrix is reallocated and new elements are zero-initialized.
- If the new shape is smaller, the matrix shape and strides are updated without reallocating memory.
- Only allowed for matrices with own_data=True.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(2, 3))
A.resize((4, 5))
print(A)
```

**Args:**

- `self` (`Self`) `[mut]`
- `shape` (`Tuple`): Tuple of (rows, columns) specifying the new shape.

!!! failure "Raises"
    Error: If the new shape requires more elements than the current matrix can hold and memory allocation fails.


</div>

<div class="fn-card" markdown="1">

##### `round`

```mojo
round(self, decimals: Int) -> Self
```

Round each element of the matrix to the specified number of decimals.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist([Float64(1.12345), 2.67891, 3.14159], (3, 1))
var B = A.round(2)
print(B)  # Outputs a Matrix[Float64] with values [[1.12], [2.68], [3.14]]
```

**Args:**

- `self` (`Self`)
- `decimals` (`Int`): Number of decimal places to round to.

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `std`

###### Overload 1

```mojo
std[returned_dtype: DType = DType.float64](self, ddof: Int = 0) -> Scalar[returned_dtype]
```

Compute the standard deviation of all elements in the matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(100, 100))
print(A.std())
```

**Parameters:**

- `returned_dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `ddof` (`Int`): Delta degrees of freedom. The divisor used in calculations is N - ddof, where N is the number of elements.

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
std[returned_dtype: DType = DType.float64](self, axis: Int, ddof: Int = 0) -> Matrix[returned_dtype]
```

Compute the standard deviation along the specified axis.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(100, 100))
print(A.std(axis=0))
print(A.std(axis=1))
```

**Parameters:**

- `returned_dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `axis` (`Int`): Axis along which to compute the standard deviation (0 for rows, 1 for columns).
- `ddof` (`Int`): Delta degrees of freedom. The divisor used in calculations is N - ddof, where N is the number of elements along the axis.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `sum`

###### Overload 1

```mojo
sum(self) -> Scalar[dtype]
```

Compute the sum of all elements in the matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(100, 100))
print(A.sum())
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

###### Overload 2

```mojo
sum(self, axis: Int) -> Self
```

Compute the sum of elements along the specified axis.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(100, 100))
print(A.sum(axis=0))
print(A.sum(axis=1))
```

**Args:**

- `self` (`Self`)
- `axis` (`Int`): Axis along which to sum (0 for rows, 1 for columns).

**Returns:**

- `Self`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `trace`

```mojo
trace(self) -> Scalar[dtype]
```

Compute the trace of the matrix (sum of diagonal elements).

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist(
    [Float64(1), 2, 3, 4, 5, 6, 7, 8, 9], (3, 3)
)
print(A.trace())  # Outputs: 15.0
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Scalar`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `issymmetric`

```mojo
issymmetric(self) -> Bool
```

Check if the matrix is symmetric (equal to its transpose).

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist([Float64(1), 2, 2, 1], (2, 2))
print(A.issymmetric())  # Outputs: True
var B = Matrix.fromlist([Float64(1), 2, 3, 4], (2, 2))
print(B.issymmetric())  # Outputs: False
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Bool`


</div>

<div class="fn-card" markdown="1">

##### `transpose`

```mojo
transpose(self) -> Self
```

Return the transpose of the matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist([Float64(1), 2, 3, 4], (2, 2))
print(A.transpose())  # Outputs: [[1, 3], [2, 4]]
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `reorder_layout`

```mojo
reorder_layout(self) -> Self
```

Reorder the memory layout of the matrix to match its current order ("C" or "F"). This method returns a new matrix with the same data but stored in the requested memory layout. Only allowed for matrices with own_data=True.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand((3, 3), order="F")
var B = A.reorder_layout()
print(B.order())  # Outputs: "F"
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`

!!! failure "Raises"
    Error: If the matrix does not have its own data.


</div>

<div class="fn-card" markdown="1">

##### `T`

```mojo
T(self) -> Self
```

Return the transpose of the matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromlist([Float64(1), 2, 3, 4], (2, 2))
print(A.T())  # Outputs: [[1, 3], [2, 4]]
```

**Args:**

- `self` (`Self`)

**Returns:**

- `Self`


</div>

<div class="fn-card" markdown="1">

##### `variance`

###### Overload 1

```mojo
variance[returned_dtype: DType = DType.float64](self, ddof: Int = 0) -> Scalar[returned_dtype]
```

Compute the variance of all elements in the matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(100, 100))
print(A.variance())
```

**Parameters:**

- `returned_dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `ddof` (`Int`): Delta degrees of freedom. The divisor used in calculations is N - ddof, where N is the number of elements.

**Returns:**

- `Scalar`

!!! failure "Raises"

###### Overload 2

```mojo
variance[returned_dtype: DType = DType.float64](self, axis: Int, ddof: Int = 0) -> Matrix[returned_dtype]
```

Compute the variance along the specified axis.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand(shape=(100, 100))
print(A.variance(axis=0))
print(A.variance(axis=1))
```

**Parameters:**

- `returned_dtype` (`DType`)

**Args:**

- `self` (`Self`)
- `axis` (`Int`): Axis along which to compute the variance (0 for rows, 1 for columns).
- `ddof` (`Int`): Delta degrees of freedom. The divisor used in calculations is N - ddof, where N is the number of elements along the axis.

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `to_ndarray`

```mojo
to_ndarray(self) -> NDArray[dtype]
```

Create `NDArray` from `Matrix`.

Returns a new NDArray with the same shape and data as the Matrix.
The buffer is copied, so changes to the NDArray do not affect the original Matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand((3, 3))
var ndarray_A = A.to_ndarray()
print(ndarray_A)
```

**Args:**

- `self` (`Self`)

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `to_numpy`

```mojo
to_numpy(self) -> PythonObject
```

Convert the Matrix to a NumPy ndarray.

Notes:
- The returned NumPy array is a copy of the Matrix data.
- The dtype and memory order are matched as closely as possible.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand((3, 3))
var np_A = A.to_numpy()
print(np_A)
```

**Args:**

- `self` (`Self`)

**Returns:**

- `PythonObject`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `full`

```mojo
full[datatype: DType = DType.float64](shape: Tuple[Int, Int], fill_value: Scalar[datatype] = 0, order: String = "C") -> Matrix[datatype]
```

<span class="badge badge-static">static</span>

Create a matrix of the specified shape, filled with the given value.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.full[f32](shape=(10, 10), fill_value=100)
```

**Parameters:**

- `datatype` (`DType`)

**Args:**

- `shape` (`Tuple`): Tuple specifying the matrix dimensions (rows, columns).
- `fill_value` (`Scalar`): Value to fill every element of the matrix.
- `order` (`String`): Memory layout order, "C" (row-major) or "F" (column-major).

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

##### `zeros`

```mojo
zeros[datatype: DType = DType.float64](shape: Tuple[Int, Int], order: String = "C") -> Matrix[datatype]
```

<span class="badge badge-static">static</span>

Create a matrix of the specified shape, filled with zeros.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.zeros[i32](shape=(10, 10))
```

**Parameters:**

- `datatype` (`DType`)

**Args:**

- `shape` (`Tuple`): Tuple specifying the matrix dimensions (rows, columns).
- `order` (`String`): Memory layout order, "C" (row-major) or "F" (column-major).

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

##### `ones`

```mojo
ones[datatype: DType = DType.float64](shape: Tuple[Int, Int], order: String = "C") -> Matrix[datatype]
```

<span class="badge badge-static">static</span>

Create a matrix of the specified shape, filled with ones.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.ones[f64](shape=(10, 10))
```

**Parameters:**

- `datatype` (`DType`)

**Args:**

- `shape` (`Tuple`): Tuple specifying the matrix dimensions (rows, columns).
- `order` (`String`): Memory layout order, "C" (row-major) or "F" (column-major).

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

##### `identity`

```mojo
identity[datatype: DType = DType.float64](len: Int, order: String = "C") -> Matrix[datatype]
```

<span class="badge badge-static">static</span>

Create an identity matrix of the given size.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.identity[f16](12)
print(A)
```

**Parameters:**

- `datatype` (`DType`)

**Args:**

- `len` (`Int`): Size of the identity matrix (number of rows and columns).
- `order` (`String`): Memory layout order, "C" (row-major) or "F" (column-major).

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

##### `rand`

```mojo
rand[datatype: DType = DType.float64](shape: Tuple[Int, Int], order: String = "C") -> Matrix[datatype]
```

<span class="badge badge-static">static</span>

Create a matrix of the specified shape, filled with random values uniformly distributed between 0 and 1.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand[f64]((12, 12))
```

**Parameters:**

- `datatype` (`DType`)

**Args:**

- `shape` (`Tuple`): Tuple specifying the matrix dimensions (rows, columns).
- `order` (`String`): Memory layout order, "C" (row-major) or "F" (column-major).

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

##### `empty`

```mojo
empty[datatype: DType = DType.float64](shape: Tuple[Int, Int], order: String = "C") -> Matrix[datatype]
```

<span class="badge badge-static">static</span>

Create a matrix of the specified shape without initializing its values. This is faster than zeros() when you plan to immediately overwrite all values.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.empty[f64]((10, 10))
# Fill A with your own values
```

Warning:
The matrix values are undefined. Always initialize before reading.

**Parameters:**

- `datatype` (`DType`)

**Args:**

- `shape` (`Tuple`): Tuple specifying the matrix dimensions (rows, columns).
- `order` (`String`): Memory layout order, "C" (row-major) or "F" (column-major).

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

##### `arange`

```mojo
arange[datatype: DType = DType.float64](start: Scalar[datatype], stop: Scalar[datatype], step: Scalar[datatype] = 1, order: String = "C") -> Matrix[datatype]
```

<span class="badge badge-static">static</span>

Create a matrix with evenly spaced values within a given interval as a row vector.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.arange[f64](0, 10, 2)  # [0, 2, 4, 6, 8]
```

**Parameters:**

- `datatype` (`DType`)

**Args:**

- `start` (`Scalar`): Start of the interval (inclusive).
- `stop` (`Scalar`): End of the interval (exclusive).
- `step` (`Scalar`): Spacing between values.
- `order` (`String`): Memory layout order, "C" (row-major) or "F" (column-major).

**Returns:**

- `Matrix`

!!! failure "Raises"
    Error: If step is zero or has wrong sign for the interval.


</div>

<div class="fn-card" markdown="1">

##### `linspace`

```mojo
linspace[datatype: DType = DType.float64](start: Scalar[datatype], stop: Scalar[datatype], num: Int = 50, order: String = "C") -> Matrix[datatype]
```

<span class="badge badge-static">static</span>

Create a matrix with evenly spaced values over a specified interval as a row vector.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.linspace[f64](0, 10, 5)  # [0, 2.5, 5, 7.5, 10]
```

**Parameters:**

- `datatype` (`DType`)

**Args:**

- `start` (`Scalar`): Start of the interval (inclusive).
- `stop` (`Scalar`): End of the interval (inclusive).
- `num` (`Int`): Number of values to generate.
- `order` (`String`): Memory layout order, "C" (row-major) or "F" (column-major).

**Returns:**

- `Matrix`

!!! failure "Raises"
    Error: If num is less than 2.


</div>

<div class="fn-card" markdown="1">

##### `diag`

```mojo
diag[datatype: DType = DType.float64](diagonal: Matrix[datatype], order: String = "C") -> Matrix[datatype]
```

<span class="badge badge-static">static</span>

Create a diagonal matrix from a vector or extract diagonal from a matrix.

Example:
```mojo
from numojo.prelude import *
var vec = Matrix.fromlist[f64]([Float64(1), 2, 3], (1, 3))
var diag_mat = Matrix.diag(vec)  # 3x3 diagonal matrix
```

**Parameters:**

- `datatype` (`DType`)

**Args:**

- `diagonal` (`Matrix`): Row or column vector to use as diagonal, or a matrix to extract diagonal from.
- `order` (`String`): Memory layout order, "C" (row-major) or "F" (column-major).

**Returns:**

- `Matrix`

!!! failure "Raises"
    Error: If input is not a vector or matrix.


</div>

<div class="fn-card" markdown="1">

##### `zeros_like`

```mojo
zeros_like[datatype: DType = DType.float64](other: Matrix[datatype]) -> Matrix[datatype]
```

<span class="badge badge-static">static</span>

Create a matrix of zeros with the same shape as the given matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand[f64]((3, 4))
var B = Matrix.zeros_like(A)  # 3x4 matrix of zeros
```

**Parameters:**

- `datatype` (`DType`)

**Args:**

- `other` (`Matrix`): Matrix whose shape to copy.

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

##### `ones_like`

```mojo
ones_like[datatype: DType = DType.float64](other: Matrix[datatype]) -> Matrix[datatype]
```

<span class="badge badge-static">static</span>

Create a matrix of ones with the same shape as the given matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand[f64]((3, 4))
var B = Matrix.ones_like(A)  # 3x4 matrix of ones
```

**Parameters:**

- `datatype` (`DType`)

**Args:**

- `other` (`Matrix`): Matrix whose shape to copy.

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

##### `empty_like`

```mojo
empty_like[datatype: DType = DType.float64](other: Matrix[datatype]) -> Matrix[datatype]
```

<span class="badge badge-static">static</span>

Create an uninitialized matrix with the same shape as the given matrix.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.rand[f64]((3, 4))
var B = Matrix.empty_like(A)  # 3x4 uninitialized matrix
```

Warning:
The matrix values are undefined. Always initialize before reading.

**Parameters:**

- `datatype` (`DType`)

**Args:**

- `other` (`Matrix`): Matrix whose shape to copy.

**Returns:**

- `Matrix`


</div>

<div class="fn-card" markdown="1">

##### `fromlist`

```mojo
fromlist[datatype: DType = DType.float64](object: List[Scalar[datatype]], shape: Tuple[Int, Int] = Tuple(VariadicPack(0, 0)), order: String = "C") -> Matrix[datatype]
```

<span class="badge badge-static">static</span>

Create a matrix from a 1-dimensional list and reshape to the given shape.

Example:
```mojo
from numojo.prelude import *
var a = Matrix.fromlist([Float64(1), 2, 3, 4, 5], (5, 1))
print(a)
```

**Parameters:**

- `datatype` (`DType`)

**Args:**

- `object` (`List`): List of values to populate the matrix.
- `shape` (`Tuple`): Tuple specifying the matrix dimensions (rows, columns). If not provided, creates a row vector.
- `order` (`String`): Memory layout order, "C" (row-major) or "F" (column-major).

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `fromstring`

```mojo
fromstring[datatype: DType = DType.float64](text: String, shape: Tuple[Int, Int] = Tuple(VariadicPack(0, 0)), order: String = "C") -> Matrix[datatype]
```

<span class="badge badge-static">static</span>

Create a Matrix from a string representation of its elements.

The input string should contain numbers separated by commas, right brackets, or whitespace. Digits, underscores, decimal points, and minus signs are treated as part of numbers. If no shape is provided, the returned matrix will be a row vector.

Example:
```mojo
from numojo.prelude import *
var A = Matrix.fromstring[f32]("1 2 .3 4 5 6.5 7 1_323.12 9 10, 11.12, 12 13 14 15 16", (4, 4))
print(A)
```

Output:
```
[[1.0   2.0     0.30000001192092896     4.0]
[5.0   6.5     7.0     1323.1199951171875]
[9.0   10.0    11.119999885559082      12.0]
[13.0  14.0    15.0    16.0]]
Size: 4x4  datatype: float32
```

**Parameters:**

- `datatype` (`DType`)

**Args:**

- `text` (`String`): String containing the matrix elements.
- `shape` (`Tuple`): Tuple specifying the matrix dimensions (rows, columns). If not provided, creates a row vector.
- `order` (`String`): Memory layout order, "C" (row-major) or "F" (column-major).

**Returns:**

- `Matrix`

!!! failure "Raises"


</div>
