# `numojo.core.layout.ndshape`

Array shape representation and operations.

Represents array dimensions with efficient storage, shape transformations
(permute, reverse), and dimension access.

Exports
-------
- `NDArrayShape`: Shape container for N-dimensional arrays.

<div class="prose-label">Notes</div>
    - The number of elements in the shape must be positive.
    - All elements of the shape must be non-negative.
    - Dimension values are validated upon creation.

## Structs

### `NDArrayShape`

<div class="type-header" markdown="1">

<span class="badge badge-kind">struct</span>

```mojo
struct NDArrayShape
```

**Memory convention:** `register_passable`  
**Implements:** `AnyType`, `Copyable`, `Deinitable`, `Equatable`, `ImplicitlyCopyable`, `Movable`, `RegisterPassable`, `Sized`, `Writable`

Represents the shape (dimensions) of an NDArray.

The data buffer is a series of `Int` values in memory. Dimensions and values are validated
upon creation to ensure they are non-negative.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm

# Create shape with variadic arguments
var shape1 = nm.Shape(2, 3, 4)
print(shape1)  # Shape: (2, 3, 4)

# Create shape from list
var shape2 = nm.Shape([5, 6, 7])
print(shape2)  # Shape: (5, 6, 7)
```

</div>

#### Fields

- **`ndim`** (`Int`): Number of dimensions of array. It must be larger than 0.

#### Aliases

#### `element_type`

```mojo
comptime element_type
```

**Value:** `DType.int`

The data type of the NDArrayShape elements.

#### Methods


<div class="fn-card" markdown="1">

#### `__init__`

<div class="overload-divider">Overload 1</div>

```mojo
def __init__() -> Self
```

<span class="badge badge-static">static</span>

Initializes an empty NDArrayShape.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 2</div>

```mojo
def __init__(var buf: IndexBuffer) -> Self
```

<span class="badge badge-static">static</span>

Initializes the NDArrayShape from an IndexBuffer.

<div class="prose-label">Args</div>

- `buf` (`IndexBuffer`) `[var]`: The IndexBuffer to initialize from.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 3</div>

```mojo
def __init__(out self, *shape: Int)
```

<span class="badge badge-static">static</span>

Initializes the NDArrayShape with variable shape dimensions.

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`: Variable number of integers representing the shape dimensions.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If any shape dimension is negative.

<div class="overload-divider">Overload 4</div>

```mojo
def __init__(out self, shape: List[Int])
```

<span class="badge badge-static">static</span>

Initializes the NDArrayShape with a list of shape dimensions.

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`: A list of integers representing the shape dimensions.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the number of dimensions is not positive.
NumojoError: If any shape dimension is negative.

<div class="overload-divider">Overload 5</div>

```mojo
def __init__(out self, shape: VariadicList[Int])
```

<span class="badge badge-static">static</span>

Initializes the NDArrayShape with a list of shape dimensions.

<div class="prose-label">Args</div>

- `shape` (`VariadicList[Int]`) `[imm]`: A variadic list of integers representing the shape dimensions.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the number of dimensions is not positive.
NumojoError: If any shape dimension is negative.

<div class="overload-divider">Overload 6</div>

```mojo
def __init__(shape: Self) -> Self
```

<span class="badge badge-static">static</span>

Initializes the NDArrayShape from another NDArrayShape. A deep copy of the data buffer is conducted.

<div class="prose-label">Args</div>

- `shape` (`Self`) `[imm]`: Another NDArrayShape to initialize from.

<div class="prose-label">Returns</div>

- `Self`

<div class="overload-divider">Overload 7</div>

```mojo
def __init__(out self, *, ndim: Int, initialized: Bool)
```

<span class="badge badge-static">static</span>

Construct NDArrayShape with number of dimensions. This method is useful when you want to create a shape with given ndim without knowing the shape values. `ndim == 0` is allowed in this method for 0darray (numojo scalar).

<div class="prose-label">Notes</div>
After creating the shape with uninitialized values,
you must set the values before using it! Otherwise, it may lead to undefined behavior.

<div class="prose-label">Args</div>

- `ndim` (`Int`) `[imm]`: Number of dimensions.
- `initialized` (`Bool`) `[imm]`: Whether the shape is initialized.
    If yes, the values will be set to 1.
    If no, the values will be uninitialized.
- `self` (`Self`) `[out]`

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the number of dimensions is negative.

<div class="overload-divider">Overload 8</div>

```mojo
def __init__(*, copy: Self) -> Self
```

<span class="badge badge-static">static</span>

Initializes the NDArrayShape from ancopy NDArrayShape. A deep copy of the data buffer is conducted.

<div class="prose-label">Args</div>

- `copy` (`Self`) `[imm]`: Ancopy NDArrayShape to initialize from.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `__getitem__`

<div class="overload-divider">Overload 1</div>

```mojo
def __getitem__(self, index: Int) -> Int
```

Gets shape dimension at specified index.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[imm]`: Index to get the shape.

<div class="prose-label">Returns</div>

- `Int`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def __getitem__(self, slice_index: Slice) -> Self
```

Return a sliced view of the dimension tuple as a new NDArrayShape.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `slice_index` (`Slice`) `[imm]`: Slice object defining the sub-buffer.

<div class="prose-label">Returns</div>

- `Self`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `__setitem__`

```mojo
def __setitem__(mut self, index: Int, val: Int)
```

Sets shape at specified index.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `index` (`Int`) `[imm]`: Index to set the shape.
- `val` (`Int`) `[imm]`: Value to set at the given index.

!!! failure "Raises"
    NumojoError: Index out of bound.


</div>

<div class="fn-card" markdown="1">

#### `__eq__`

```mojo
def __eq__(self, other: Self) -> Bool
```

Checks if two shapes have identical dimensions and values.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The shape to compare with.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__ne__`

```mojo
def __ne__(self, other: Self) -> Bool
```

Checks if two shapes have identical dimensions and values.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The shape to compare with.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `__contains__`

```mojo
def __contains__(self, val: Int) -> Bool
```

Check if the NDArrayShape contains the given value.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `val` (`Int`) `[imm]`: Value to check for.

<div class="prose-label">Returns</div>

- `Bool`


</div>

<div class="fn-card" markdown="1">

#### `load`

```mojo
def load[width: Int = Int(1)](self, idx: Int) -> SIMD[DType.int, width]
```

Load a SIMD vector from the Shape at the specified index.

<div class="prose-label">Parameters</div>

- `width` (`Int`): The width of the SIMD vector.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: The starting index to load from.

<div class="prose-label">Returns</div>

- `SIMD[DType.int, width]`

!!! failure "Raises"
    NumojoError: If the load exceeds the bounds of the Shape.


</div>

<div class="fn-card" markdown="1">

#### `store`

```mojo
def store[width: Int = Int(1)](self, idx: Int, value: SIMD[DType.int, width])
```

Store a SIMD vector into the Shape at the specified index.

<div class="prose-label">Parameters</div>

- `width` (`Int`): The width of the SIMD vector.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: The starting index to store to.
- `value` (`SIMD[DType.int, width]`) `[imm]`: The SIMD vector to store.

!!! failure "Raises"
    NumojoError: If the store exceeds the bounds of the Shape.


</div>

<div class="fn-card" markdown="1">

#### `unsafe_load`

```mojo
def unsafe_load[width: Int = Int(1)](self, idx: Int) -> SIMD[DType.int, width]
```

Unsafely load a SIMD vector from the Shape at the specified index.

<div class="prose-label">Parameters</div>

- `width` (`Int`): The width of the SIMD vector.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: The starting index to load from.

<div class="prose-label">Returns</div>

- `SIMD[DType.int, width]`


</div>

<div class="fn-card" markdown="1">

#### `unsafe_store`

```mojo
def unsafe_store[width: Int = Int(1)](self, idx: Int, value: SIMD[DType.int, width])
```

Unsafely store a SIMD vector into the Shape at the specified index.

<div class="prose-label">Parameters</div>

- `width` (`Int`): The width of the SIMD vector.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`: The starting index to store to.
- `value` (`SIMD[DType.int, width]`) `[imm]`: The SIMD vector to store.


</div>

<div class="fn-card" markdown="1">

#### `unsafe_get`

```mojo
def unsafe_get(self, idx: Int) -> Int
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `idx` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `unsafe_set`

```mojo
def unsafe_set(mut self, idx: Int, value: Int)
```

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`
- `idx` (`Int`) `[imm]`
- `value` (`Int`) `[imm]`


</div>

<div class="fn-card" markdown="1">

#### `row_major`

```mojo
def row_major(self) -> NDArrayStrides
```

Create row-major (C-style) strides from a shape.

Row-major means the last dimension has stride 1 and strides increase
going backwards through dimensions.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArrayStrides`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `col_major`

```mojo
def col_major(self) -> NDArrayStrides
```

Create column-major (Fortran-style) strides from a shape.

Column-major means the first dimension has stride 1 and strides increase
going forward through dimensions.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArrayStrides`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `reverse`

```mojo
def reverse(self) -> Self
```

Return a new shape with dimensions reversed.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `permute`

```mojo
def permute(self, axes: List[Int]) -> Self
```

Return a new shape with axes reordered.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axes` (`List[Int]`) `[imm]`: New axis order. Must contain each axis exactly once.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If axes length doesn't match ndim or contains invalid/duplicate axes.


</div>

<div class="fn-card" markdown="1">

#### `broadcast`

```mojo
def broadcast(self, other: Self) -> Self
```

Compute the broadcast result shape of `self` and `other`, following NumPy broadcasting rules.

Shapes are aligned from the trailing dimension. Two dimensions are
compatible when they are equal, or when one of them is 1. Missing
leading dimensions are treated as size 1.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `other` (`Self`) `[imm]`: The other shape to broadcast against.

<div class="prose-label">Returns</div>

- `Self`

!!! failure "Raises"
    NumojoError: If the shapes are not broadcast-compatible.


</div>

<div class="fn-card" markdown="1">

#### `join`

```mojo
def join(self, *shapes: Self) -> Self
```

Join multiple shapes into a single shape.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `*shapes` (`Self`) `[imm]`: Variable number of NDArrayShape objects.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `swapaxes`

```mojo
def swapaxes(self, axis1: Int, axis2: Int) -> Self
```

Returns a new shape with the given axes swapped.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis1` (`Int`) `[imm]`: The first axis to swap.
- `axis2` (`Int`) `[imm]`: The second axis to swap.

<div class="prose-label">Returns</div>

- `Self`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `extend`

```mojo
def extend(self, *values: Int) -> Self
```

Extend the shape by sizes of extended dimensions.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `*values` (`Int`) `[imm]`: Sizes of extended dimensions.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `flip`

```mojo
def flip(mut self)
```

Flip the items in-place.

<div class="prose-label">Args</div>

- `self` (`Self`) `[mut]`


</div>

<div class="fn-card" markdown="1">

#### `flipped`

```mojo
def flipped(self) -> Self
```

Returns a new shape by flipping the items.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `move_axis_to_end`

```mojo
def move_axis_to_end(self, axis: Int) -> Self
```

Returns a new shape by moving the value of axis to the end.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis (index) to move.

<div class="prose-label">Returns</div>

- `Self`


</div>

<div class="fn-card" markdown="1">

#### `pop`

```mojo
def pop(self, axis: Int) -> Self
```

Drops the item at the given axis (index).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `axis` (`Int`) `[imm]`: The axis (index) to drop.

<div class="prose-label">Returns</div>

- `Self`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

#### `rank`

```mojo
def rank(self) -> Int
```

Returns the number of dimensions of the shape.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `size`

```mojo
def size(self) -> Int
```

Returns the total number of elements in the array.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `sum`

```mojo
def sum(self) -> Int
```

Compute the sum of all elements in NDArrayShape.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `product`

```mojo
def product(self) -> Int
```

Compute the product of all elements in the IndexBuffer.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `__len__`

```mojo
def __len__(self) -> Int
```

Gets number of elements in the shape. It equals the number of dimensions of the array.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `__repr__`

```mojo
def __repr__(self) -> String
```

Returns a string of the shape of the array.

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

#### `__str__`

```mojo
def __str__(self) -> String
```

Returns a string of the shape of the array.

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

Writes the shape representation to a writer.

<div class="prose-label">Parameters</div>

- `W` (`Writer`)

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `writer` (`W`) `[mut]`


</div>

<div class="fn-card" markdown="1">

#### `tolist`

```mojo
def tolist(self) -> List[Int]
```

Convert the shape to a list of integers.

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`

<div class="prose-label">Returns</div>

- `List[Int]`


</div>

<div class="fn-card" markdown="1">

#### `normalize_index`

```mojo
def normalize_index(self, index: Int) -> Int
```

Normalizes the given index to be within the valid range [0, ndim).

<div class="prose-label">Args</div>

- `self` (`Self`) `[imm]`
- `index` (`Int`) `[imm]`: The index to normalize.

<div class="prose-label">Returns</div>

- `Int`


</div>

<div class="fn-card" markdown="1">

#### `__iter__`

```mojo
def __iter__(ref self) -> _ShapeIter[origin_of(self)]
```

Iterate over elements of the NDArrayShape, returning copied values.

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`

<div class="prose-label">Returns</div>

- `_ShapeIter[origin_of(self)]`


</div>

<div class="fn-card" markdown="1">

#### `__reversed__`

```mojo
def __reversed__(ref self) -> _ShapeIter[origin_of(self), False]
```

Iterate over elements of the NDArrayShape in reverse order, returning copied values.

<div class="prose-label">Args</div>

- `self` (`Self`) `[ref]`

<div class="prose-label">Returns</div>

- `_ShapeIter[origin_of(self), False]`


</div>
