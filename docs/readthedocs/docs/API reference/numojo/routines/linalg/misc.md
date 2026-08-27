# `numojo.routines.linalg.misc`

Miscellaneous linear algebra operations.

Additional linear algebra utilities (diagonals, symmetry checks).

Exports
-------
- `det`: Determinant.
- `inv`: Matrix inverse.
- `trace`: Matrix trace.

## Functions


<div class="fn-card" markdown="1">

### `diagonal`

```mojo
def diagonal[dtype: DType](a: NDArray[dtype], offset: Int = Int(0), axis1: Int = Int(0), axis2: Int = Int(1)) -> NDArray[dtype]
```

Returns specific diagonals.

For 2-D arrays (the default `axis1=0, axis2=1` case), returns the 1-D
diagonal at the given `offset`. For N-D arrays, `axis1` and `axis2` are
treated as the two axes that define the 2-D sub-arrays whose diagonals
are extracted; the result has the two diagonalized axes removed and
replaced by a new last axis holding the diagonal values. The result shape is
`a.shape[axes not in {axis1, axis2}] + (diagonal_length,)`, where the
surviving axes keep their original relative order.

Examples:
```mojo
import numojo as nm

var a = nm.arange[nm.i32](60).reshape(nm.Shape(3, 4, 5))
# axis1=0, axis2=1 (default): result shape (5, 3) -- min(3,4)=3
print(nm.linalg.diagonal(a, axis1=0, axis2=1))
```
.

**Parameters:**

- `dtype` (`DType`): Data type of the array.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: An NDArray.
- `offset` (`Int`) `[imm]`: Offset of the diagonal from the main diagonal.
- `axis1` (`Int`) `[imm]`: First axis of the 2-D sub-arrays from which the diagonals
    should be taken. Defaults to 0.
- `axis2` (`Int`) `[imm]`: Second axis of the 2-D sub-arrays from which the diagonals
    should be taken. Defaults to 1.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the array has fewer than 2 dimensions.
NumojoError: If `axis1` or `axis2` is out of bounds, or `axis1 == axis2`.
NumojoError: If the offset is beyond the shape of the array.


</div>
