# `numojo.core.traits.backend`

Computational backend trait definitions.

Defines traits for different computation backends to standardize how
array operations are implemented.

Exports
-------
- `Backend`: Base trait for computational backends.

## Traits

### `Backend`

**Extends:** `AnyType`, `Deinitable`

A trait that defines backends for calculations in the rest of the library.

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
def __init__(out self)
```

<span class="badge badge-static">static</span>

Initialize the backend.

**Args:**

- `self` (`_Self`) `[out]`

**Returns:**

- `_Self`


</div>

<div class="fn-card" markdown="1">

##### `math_func_fma`

###### Overload 1

```mojo
def math_func_fma[dtype: DType](self, array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[dtype]
```

Apply a SIMD level fuse multipy add function of three variables and one return to a NDArray.

!!! info "Constraints"
    Both arrays must have the same shape

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `self` (`_Self`) `[imm]`
- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array3` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"
    If shapes are missmatched or there is a access error.

###### Overload 2

```mojo
def math_func_fma[dtype: DType](self, array1: NDArray[dtype], array2: NDArray[dtype], simd: Scalar[dtype]) -> NDArray[dtype]
```

Apply a SIMD level fuse multipy add function of three variables and one return to a NDArray.

!!! info "Constraints"
    Both arrays must have the same shape

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `self` (`_Self`) `[imm]`
- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `simd` (`Scalar[dtype]`) `[imm]`: A SIMD[dtype,1] value to be added.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `math_func_1_array_in_one_array_out`

```mojo
def math_func_1_array_in_one_array_out[dtype: DType, func: def[type: DType, simd_w: Int](SIMD[type, simd_w]) -> SIMD[type, simd_w]](self, array: NDArray[dtype]) -> NDArray[dtype]
```

Apply a SIMD function of one variable and one return to a NDArray.

**Parameters:**

- `dtype` (`DType`): The element type.
- `func` (`def[type: DType, simd_w: Int](SIMD[type, simd_w]) -> SIMD[type, simd_w]`): The SIMD function to to apply.

**Args:**

- `self` (`_Self`) `[imm]`
- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `math_func_2_array_in_one_array_out`

```mojo
def math_func_2_array_in_one_array_out[dtype: DType, func: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[type, simd_w]](self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Apply a SIMD function of two variable and one return to a NDArray.

!!! info "Constraints"
    Both arrays must have the same shape

**Parameters:**

- `dtype` (`DType`): The element type.
- `func` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[type, simd_w]`): The SIMD function to to apply.

**Args:**

- `self` (`_Self`) `[imm]`
- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `math_func_1_array_1_scalar_in_one_array_out`

```mojo
def math_func_1_array_1_scalar_in_one_array_out[dtype: DType, func: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[type, simd_w]](self, array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Apply a SIMD function of two variable and one return to a NDArray.

!!! info "Constraints"
    Both arrays must have the same shape

**Parameters:**

- `dtype` (`DType`): The element type.
- `func` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[type, simd_w]`): The SIMD function to to apply.

**Args:**

- `self` (`_Self`) `[imm]`
- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: A Scalars.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `math_func_1_scalar_1_array_in_one_array_out`

```mojo
def math_func_1_scalar_1_array_in_one_array_out[dtype: DType, func: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[type, simd_w]](self, scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Apply a SIMD function of two variable and one return to a NDArray.

!!! info "Constraints"
    Both arrays must have the same shape

**Parameters:**

- `dtype` (`DType`): The element type.
- `func` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[type, simd_w]`): The SIMD function to to apply.

**Args:**

- `self` (`_Self`) `[imm]`
- `scalar` (`Scalar[dtype]`) `[imm]`: A Scalars.
- `array` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `math_func_compare_2_arrays`

```mojo
def math_func_compare_2_arrays[dtype: DType, func: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[DType.bool, simd_w]](self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

Apply a SIMD comparision function of two variable.

!!! info "Constraints"
    Both arrays must have the same shape.

**Parameters:**

- `dtype` (`DType`): The element type.
- `func` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[DType.bool, simd_w]`): The SIMD comparision function to to apply.

**Args:**

- `self` (`_Self`) `[imm]`
- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `array2` (`NDArray[dtype]`) `[imm]`: A NDArray.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `math_func_compare_array_and_scalar`

```mojo
def math_func_compare_array_and_scalar[dtype: DType, func: def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[DType.bool, simd_w]](self, array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

Apply a SIMD comparision function of two variable.

!!! info "Constraints"
    Both arrays must have the same shape.

**Parameters:**

- `dtype` (`DType`): The element type.
- `func` (`def[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[DType.bool, simd_w]`): The SIMD comparision function to to apply.

**Args:**

- `self` (`_Self`) `[imm]`
- `array1` (`NDArray[dtype]`) `[imm]`: A NDArray.
- `scalar` (`Scalar[dtype]`) `[imm]`: A scalar.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `math_func_is`

```mojo
def math_func_is[dtype: DType, func: def[type: DType, simd_w: Int](SIMD[type, simd_w]) -> SIMD[DType.bool, simd_w]](self, array: NDArray[dtype]) -> NDArray[DType.bool]
```

**Parameters:**

- `dtype` (`DType`)
- `func` (`def[type: DType, simd_w: Int](SIMD[type, simd_w]) -> SIMD[DType.bool, simd_w]`)

**Args:**

- `self` (`_Self`) `[imm]`
- `array` (`NDArray[dtype]`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>
