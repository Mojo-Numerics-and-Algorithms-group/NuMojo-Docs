# `numojo.routines.linalg.products`

Array and vector product operations.

Functions for computing products of vectors and arrays (dot product, matrix
multiplication, cross product).

Exports
-------
- `dot`: Dot product of vectors.
- `matmul`: Matrix multiplication.
- `cross`: Cross product.
- `outer`: Outer product of two flattened arrays.
- `kron`: Kronecker product.
- `tensordot`: Sum of products over given axes.

## Functions


<div class="fn-card" markdown="1">

### `cross`

```mojo
def cross[dtype: DType = .float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Compute the cross product of two arrays.

!!! info "Constraints"
    `array1` and `array2` must be of shape (3,).

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: A array.
- `array2` (`NDArray[dtype]`) `[imm]`: A array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `dot`

```mojo
def dot[dtype: DType = .float64](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Compute the dot product of two arrays.

Parameters
    dtype: The element type.

<div class="prose-label">Examples</div>
`dot(a, b)` computes the inner product of vectors `a` and `b`.

!!! info "Constraints"
    Each input must have at most two dimensions.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: A array.
- `array2` (`NDArray[dtype]`) `[imm]`: A array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the inputs are not equal-length one-dimensional arrays.


</div>

<div class="fn-card" markdown="1">

### `matmul_tiled_unrolled_parallelized`

```mojo
def matmul_tiled_unrolled_parallelized[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Array multiplication vectorized, tiled, unrolled, and parallelized.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`
- `B` (`NDArray[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `matmul_1darray`

```mojo
def matmul_1darray[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Array multiplication for 1-d arrays (inner dot).

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`
- `B` (`NDArray[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `matmul_2darray`

```mojo
def matmul_2darray[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Array multiplication for 2-d arrays (inner dot).

Parameter:
    dtype: Data type.

Return:
    A multiplied by B.

<div class="prose-label">Notes</div>
The multiplication is vectorized and parallelized.

<div class="prose-label">References</div>
    [1] https://docs.modular.com/mojo/notebooks/Matmul.
    resultompared to the reference, we increases the size of
    the SIMD vector from the default width to 16. The purpose is to
    increase the performance via SIMD.
    This reduces the execution time by ~50 percent compared to
    `matmul_parallelized` and `matmul_tiled_unrolled_parallelized` for large
    matrices.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: First array.
- `B` (`NDArray[dtype]`) `[imm]`: Second array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    When the shape does not match.


</div>

<div class="fn-card" markdown="1">

### `matmul`

```mojo
def matmul[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Array multiplication for any dimensions.

Parameter:
    dtype: Data type.

Return:
    A multiplied by B.

<div class="prose-label">Notes</div>

When A and B are 1darray, it is equal to dot of vectors:
`(i) @ (i) -> (1)`.

When A and B are 2darray, it is equal to inner products of matrices:
`(i,j) @ (j,k) -> (i,k)`.

When A and B are more than 2d, it is equal to a stack of 2darrays:
`(i,j,k) @ (i,k,l) -> (i,j,l)` and
`(i,j,k,l) @ (i,j,l,m) -> (i,j,k,m)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: First array.
- `B` (`NDArray[dtype]`) `[imm]`: Second array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    (1) The shapes of first n-2 dimensions do not match.
(2) The shape of -2 dimension of first array does not match
the shape of -1 dimension of the second array.


</div>

<div class="fn-card" markdown="1">

### `matmul_naive`

```mojo
def matmul_naive[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Array multiplication with three nested loops.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`
- `B` (`NDArray[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `outer`

```mojo
def outer[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Compute the outer product of two arrays.

Both inputs are flattened (in C order) before the product is taken,
matching `numpy.outer`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f64](3)
var b = nm.arange[nm.f64](4)
print(nm.linalg.outer(a, b))
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: First input, treated as a flat vector of length `A.size`.
- `B` (`NDArray[dtype]`) `[imm]`: Second input, treated as a flat vector of length `B.size`.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `kron`

```mojo
def kron[dtype: DType](A: NDArray[dtype], B: NDArray[dtype]) -> NDArray[dtype]
```

Compute the Kronecker product of two arrays.

If `A` and `B` have different numbers of dimensions, the shape of the
array with fewer dimensions is padded with leading 1s, matching
`numpy.kron`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f64](6).reshape(nm.Shape(2, 3))
var b = nm.eye[nm.f64](2, 2)
print(nm.linalg.kron(a, b))
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: First input array.
- `B` (`NDArray[dtype]`) `[imm]`: Second input array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `tensordot`

<div class="overload-divider">Overload 1</div>

```mojo
def tensordot[dtype: DType](A: NDArray[dtype], B: NDArray[dtype], axes_a: List[Int], axes_b: List[Int]) -> NDArray[dtype]
```

Compute the tensor dot product along specified axes.

Sums the products of the elements of `A` and `B` over the axes given
in `axes_a` and `axes_b`. This is a generalization of `dot` and
`matmul` to arbitrary axes, matching `numpy.tensordot`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f64](60).reshape(nm.Shape(3, 4, 5))
var b = nm.arange[nm.f64](24).reshape(nm.Shape(4, 3, 2))
print(nm.linalg.tensordot(a, b, axes_a=[1, 0], axes_b=[0, 1]))
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: First input array.
- `B` (`NDArray[dtype]`) `[imm]`: Second input array.
- `axes_a` (`List[Int]`) `[imm]`: Axes of `A` to sum over. Negative values count from the
    end.
- `axes_b` (`List[Int]`) `[imm]`: Axes of `B` to sum over, paired positionally with
    `axes_a`. Negative values count from the end.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `axes_a` and `axes_b` have different lengths, or
the paired axis lengths of `A` and `B` do not match.

<div class="overload-divider">Overload 2</div>

```mojo
def tensordot[dtype: DType](A: NDArray[dtype], B: NDArray[dtype], axes: Int = Int(2)) -> NDArray[dtype]
```

(overload) Tensor dot product summing over the last `axes` axes of `A` and the first `axes` axes of `B`.

`axes=2` reproduces `matmul` for 2-D inputs; `axes=1` reproduces
`dot`-like contraction over one axis; `axes=0` reproduces the full
outer product (no summation).

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var a = nm.arange[nm.f64](60).reshape(nm.Shape(3, 4, 5))
var b = nm.arange[nm.f64](120).reshape(nm.Shape(4, 5, 6))
print(nm.linalg.tensordot(a, b, axes=2))
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: First input array.
- `B` (`NDArray[dtype]`) `[imm]`: Second input array.
- `axes` (`Int`) `[imm]`: Number of trailing/leading axes of `A`/`B` to sum over.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
