# `numojo.science.signal`

Signal processing module (`numojo.science.signal`)

Implements signal processing utilities.

It is like `scipy.signal` in Python.

## Functions


<div class="fn-card" markdown="1">

### `convolve2d`

```mojo
convolve2d[dtype: DType, //](in1: NDArray[dtype], in2: NDArray[dtype]) -> NDArray[dtype]
```

Convolve two 2-dimensional arrays.

Currently, the mode is "valid".


Example:
```mojo
import numojo as nm
fn main() raises:
    var in1 = nm.routines.creation.fromstring("[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]")
    var in2 = nm.routines.creation.fromstring("[[1, 0], [0, -1]]")
    print(nm.science.signal.convolve2d(in1, in2))
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `in1` (`NDArray`): Input array 1.
- `in2` (`NDArray`): Input array 2. It should be of a smaller size of in1.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>
