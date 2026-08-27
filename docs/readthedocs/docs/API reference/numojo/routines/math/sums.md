# `numojo.routines.math.sums`

Sum reductions and cumulative sums for arrays.

Computes sum reductions along axes and cumulative sums for NDArrays, with
both flattened and axis-aware variants.

Exports
-------
- `sum`: Sum of all elements or along an axis.
- `cumsum`: Cumulative sum along an axis or flattened.

## Functions


<div class="fn-card" markdown="1">

### `sum`

<div class="overload-divider">Overload 1</div>

```mojo
def sum[dtype: DType](A: NDArray[dtype]) -> Scalar[dtype]
```

Returns sum of all items in the array.

<div class="prose-label">Examples</div>
```console
> print(A)
[[      0.1315377950668335      0.458650141954422       0.21895918250083923     ]
 [      0.67886471748352051     0.93469291925430298     0.51941639184951782     ]
 [      0.034572109580039978    0.52970021963119507     0.007698186207562685    ]]
2-D array  Shape: [3, 3]  DType: float32
> print(nm.sum(A))
3.5140917301177979
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: NDArray.

<div class="prose-label">Returns</div>

- `Scalar[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def sum[dtype: DType](A: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Returns sums of array elements over a given axis.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var A = nm.random.randn(100, 100)
print(nm.sum(A, axis=0))
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: NDArray.
- `axis` (`Int`) `[imm]`: The axis along which the sum is performed.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound.
NumojoError: If the number of dimensions is 1.


</div>

<div class="fn-card" markdown="1">

### `cumsum`

<div class="overload-divider">Overload 1</div>

```mojo
def cumsum[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```

Returns cumsum of all items of an array. The array is flattened before cumsum.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def cumsum[dtype: DType](A: NDArray[dtype], var axis: Int) -> NDArray[dtype]
```

Returns cumsum of array by axis.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: NDArray.
- `axis` (`Int`) `[var]`: Axis.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>
