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

#### Overload 1

```mojo
def sum[dtype: DType](A: NDArray[dtype]) -> Scalar[dtype]
```

Returns sum of all items in the array.

Example:
```console
> print(A)
[[      0.1315377950668335      0.458650141954422       0.21895918250083923     ]
 [      0.67886471748352051     0.93469291925430298     0.51941639184951782     ]
 [      0.034572109580039978    0.52970021963119507     0.007698186207562685    ]]
2-D array  Shape: [3, 3]  DType: float32
> print(nm.sum(A))
3.5140917301177979
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`: NDArray.

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def sum[dtype: DType](A: NDArray[dtype], axis: Int) -> NDArray[dtype]
```

Returns sums of array elements over a given axis.

Example:
```mojo
import numojo as nm
var A = nm.random.randn(100, 100)
print(nm.sum(A, axis=0))
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`: NDArray.
- `axis` (`Int`) `[imm]`: The axis along which the sum is performed.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the axis is out of bound.
NumojoError: If the number of dimensions is 1.


</div>

<div class="fn-card" markdown="1">

### `cumsum`

#### Overload 1

```mojo
def cumsum[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```

Returns cumsum of all items of an array. The array is flattened before cumsum.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`: NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def cumsum[dtype: DType](A: NDArray[dtype], var axis: Int) -> NDArray[dtype]
```

Returns cumsum of array by axis.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`: NDArray.
- `axis` (`Int`) `[var]`: Axis.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>
