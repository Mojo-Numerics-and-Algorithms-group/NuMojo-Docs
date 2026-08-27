# `numojo.routines.linalg.norms`

Determinant and trace computation for 2-D arrays.

Exports
-------
- `det`: Determinant via LUP decomposition.
- `trace`: Sum of the diagonal elements.

## Functions


<div class="fn-card" markdown="1">

### `det`

```mojo
def det[dtype: DType](A: NDArray[dtype]) -> Scalar[dtype]
```

Find the determinant of A using LUP decomposition.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `A` (`NDArray[dtype]`) `[imm]`

**Returns:**

- `Scalar[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `trace`

```mojo
def trace[dtype: DType](array: NDArray[dtype], offset: Int = Int(0), axis1: Int = Int(0), axis2: Int = Int(1)) -> NDArray[dtype]
```

Computes the trace of a ndarray.

**Parameters:**

- `dtype` (`DType`): Data type of the array.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `offset` (`Int`) `[imm]`: Offset of the diagonal from the main diagonal.
- `axis1` (`Int`) `[imm]`: First axis.
- `axis2` (`Int`) `[imm]`: Second axis.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>
