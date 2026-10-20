# `numojo.routines.bitwise`

Bitwise operations for integer arrays.

Element-wise bitwise operations for integer NDArrays.

Exports
-------
- `bitwise_and`, `bitwise_or`, `bitwise_xor`: Binary bitwise operations.
- `left_shift`, `right_shift`: Binary shift operations.
- `invert`: Bitwise NOT operation.

## Functions


<div class="fn-card" markdown="1">

### `bitwise_and`

```mojo
def bitwise_and[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype] where dtype.is_integral() or (dtype == DType.bool)
```

Compute the element-wise bitwise AND of two arrays.

<div class="prose-label">Examples</div>
`bitwise_and(a, b)` computes the bitwise AND of `a` and `b`.

!!! info "Constraints"
    Both arrays must have the same integral or boolean element type.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: The first input array.
- `array2` (`NDArray[dtype]`) `[imm]`: The second input array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `bitwise_or`

```mojo
def bitwise_or[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype] where dtype.is_integral() or (dtype == DType.bool)
```

Compute the element-wise bitwise OR of two arrays.

<div class="prose-label">Examples</div>
`bitwise_or(a, b)` computes the bitwise OR of `a` and `b`.

!!! info "Constraints"
    Both arrays must have the same integral or boolean element type.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: The first input array.
- `array2` (`NDArray[dtype]`) `[imm]`: The second input array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `bitwise_xor`

```mojo
def bitwise_xor[dtype: DType](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype] where dtype.is_integral() or (dtype == DType.bool)
```

Compute the element-wise bitwise XOR of two arrays.

<div class="prose-label">Examples</div>
`bitwise_xor(a, b)` computes the bitwise XOR of `a` and `b`.

!!! info "Constraints"
    Both arrays must have the same integral or boolean element type.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array1` (`NDArray[dtype]`) `[imm]`: The first input array.
- `array2` (`NDArray[dtype]`) `[imm]`: The second input array.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `left_shift`

```mojo
def left_shift[dtype: DType](array: NDArray[dtype], shift: Int) -> NDArray[dtype] where dtype.is_integral()
```

Shift each array element left by an integer number of bits.

<div class="prose-label">Examples</div>
`left_shift(a, 2)` shifts every element of `a` left by two bits.

!!! info "Constraints"
    The array must have an integral element type.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The input array.
- `shift` (`Int`) `[imm]`: The number of bits to shift each element.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `right_shift`

```mojo
def right_shift[dtype: DType](array: NDArray[dtype], shift: Int) -> NDArray[dtype] where dtype.is_integral()
```

Shift each array element right by an integer number of bits.

<div class="prose-label">Examples</div>
`right_shift(a, 2)` shifts every element of `a` right by two bits.

!!! info "Constraints"
    The array must have an integral element type.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: The input array.
- `shift` (`Int`) `[imm]`: The number of bits to shift each element.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `invert`

```mojo
def invert[dtype: DType](array: NDArray[dtype]) -> NDArray[dtype] where dtype.is_integral() or (dtype == DType.bool)
```

Element-wise invert of an array.

<div class="prose-label">Examples</div>
```mojo
from numojo.prelude import *
import numojo as nm
from numojo.routines.bitwise import invert

var arr1 = nm.array[nm.i8]([1, 2, 3], shape=[3])
var result1 = invert(arr1) # result1 is [-2, -3, -4]

var arr2 = nm.array[nm.boolean]([True, False, True], shape=[3])
var result2 = invert(arr2) # result2 is [false, true, false
```

!!! info "Constraints"
    The array must be either a boolean or integral array.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The element type.

<div class="prose-label">Args</div>

- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
