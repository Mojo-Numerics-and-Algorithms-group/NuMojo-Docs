# `numojo.routines.math.products`

Product reductions and cumulative products for arrays.

Computes products along axes and cumulative products for NDArrays, with
both flattened and axis-aware variants.

Exports
-------
- `prod`: Product of all elements or along an axis.
- `cumprod`: Cumulative product along an axis or flattened.

## Functions


<div class="fn-card" markdown="1">

### `prod`

#### Overload 1

```mojo
def prod[dtype: DType](A: NDArray[dtype]) -> Scalar[dtype]
```

Returns products of all items in the array.

Example:
```console
> print(A)
[[      0.1315377950668335      0.458650141954422       0.21895918250083923     ]
[      0.67886471748352051     0.93469291925430298     0.51941639184951782     ]
[      0.034572109580039978    0.52970021963119507     0.007698186207562685    ]]
2-D array  Shape: [3, 3]  DType: float32

> print(nm.prod(A))
6.1377261317829834e-07
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
def prod[dtype: DType](A: NDArray[dtype], var axis: Int) -> NDArray[dtype]
```

Returns products of array elements over a given axis.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`: NDArray.
- `axis` (`Int`) `[var]`: The axis along which the product is performed.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `cumprod`

#### Overload 1

```mojo
def cumprod[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```

Returns cumprod of all items of an array. The array is flattened before cumprod.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`: NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def cumprod[dtype: DType](A: NDArray[dtype], var axis: Int) -> NDArray[dtype]
```

Returns cumprod of array by axis.

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`: NDArray.
- `axis` (`Int`) `[var]`: Axis.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>
