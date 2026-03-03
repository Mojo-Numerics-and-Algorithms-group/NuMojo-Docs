# `numojo.core.traits.backend`

## Traits

### `Backend`

**Extends:** `AnyType`, `ImplicitlyDestructible`

A trait that defines backends for calculations in the rest of the library.

#### Aliases

##### `__del__is_trivial`

```mojo
comptime __del__is_trivial
```

A flag (often compiler generated) to indicate whether the implementation of `__del__` is trivial.

The implementation of `__del__` is considered to be trivial if:
- The struct has a compiler-generated trivial destructor and all its fields
  have a trivial `__del__` method.

In practice, it means that the `__del__` can be considered as no-op.

#### Methods


<div class="fn-card" markdown="1">

##### `__init__`

```mojo
__init__(out self: _Self)
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
math_func_fma[dtype: DType](self: _Self, array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[dtype]
```

Apply a SIMD level fuse multipy add function of three variables and one return to a NDArray.

!!! info "Constraints"
    Both arrays must have the same shape

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `self` (`_Self`)
- `array1` (`NDArray`): A NDArray.
- `array2` (`NDArray`): A NDArray.
- `array3` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"
    If shapes are missmatched or there is a access error.

###### Overload 2

```mojo
math_func_fma[dtype: DType](self: _Self, array1: NDArray[dtype], array2: NDArray[dtype], simd: Scalar[dtype]) -> NDArray[dtype]
```

Apply a SIMD level fuse multipy add function of three variables and one return to a NDArray.

!!! info "Constraints"
    Both arrays must have the same shape

**Parameters:**

- `dtype` (`DType`): The element type.

**Args:**

- `self` (`_Self`)
- `array1` (`NDArray`): A NDArray.
- `array2` (`NDArray`): A NDArray.
- `simd` (`Scalar`): A SIMD[dtype,1] value to be added.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `math_func_1_array_in_one_array_out`

```mojo
math_func_1_array_in_one_array_out[dtype: DType, func: fn[type: DType, simd_w: Int](SIMD[type, simd_w]) -> SIMD[type, simd_w]](self: _Self, array: NDArray[dtype]) -> NDArray[dtype]
```

Apply a SIMD function of one variable and one return to a NDArray.

**Parameters:**

- `dtype` (`DType`): The element type.
- `func` (`fn[type: DType, simd_w: Int](SIMD[type, simd_w]) -> SIMD[type, simd_w]`): The SIMD function to to apply.

**Args:**

- `self` (`_Self`)
- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `math_func_2_array_in_one_array_out`

```mojo
math_func_2_array_in_one_array_out[dtype: DType, func: fn[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[type, simd_w]](self: _Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```

Apply a SIMD function of two variable and one return to a NDArray.

!!! info "Constraints"
    Both arrays must have the same shape

**Parameters:**

- `dtype` (`DType`): The element type.
- `func` (`fn[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[type, simd_w]`): The SIMD function to to apply.

**Args:**

- `self` (`_Self`)
- `array1` (`NDArray`): A NDArray.
- `array2` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `math_func_1_array_1_scalar_in_one_array_out`

```mojo
math_func_1_array_1_scalar_in_one_array_out[dtype: DType, func: fn[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[type, simd_w]](self: _Self, array: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[dtype]
```

Apply a SIMD function of two variable and one return to a NDArray.

!!! info "Constraints"
    Both arrays must have the same shape

**Parameters:**

- `dtype` (`DType`): The element type.
- `func` (`fn[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[type, simd_w]`): The SIMD function to to apply.

**Args:**

- `self` (`_Self`)
- `array` (`NDArray`): A NDArray.
- `scalar` (`Scalar`): A Scalars.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `math_func_1_scalar_1_array_in_one_array_out`

```mojo
math_func_1_scalar_1_array_in_one_array_out[dtype: DType, func: fn[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[type, simd_w]](self: _Self, scalar: Scalar[dtype], array: NDArray[dtype]) -> NDArray[dtype]
```

Apply a SIMD function of two variable and one return to a NDArray.

!!! info "Constraints"
    Both arrays must have the same shape

**Parameters:**

- `dtype` (`DType`): The element type.
- `func` (`fn[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[type, simd_w]`): The SIMD function to to apply.

**Args:**

- `self` (`_Self`)
- `scalar` (`Scalar`): A Scalars.
- `array` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `math_func_compare_2_arrays`

```mojo
math_func_compare_2_arrays[dtype: DType, func: fn[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[DType.bool, simd_w]](self: _Self, array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[DType.bool]
```

Apply a SIMD comparision function of two variable.

!!! info "Constraints"
    Both arrays must have the same shape.

**Parameters:**

- `dtype` (`DType`): The element type.
- `func` (`fn[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[DType.bool, simd_w]`): The SIMD comparision function to to apply.

**Args:**

- `self` (`_Self`)
- `array1` (`NDArray`): A NDArray.
- `array2` (`NDArray`): A NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `math_func_compare_array_and_scalar`

```mojo
math_func_compare_array_and_scalar[dtype: DType, func: fn[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[DType.bool, simd_w]](self: _Self, array1: NDArray[dtype], scalar: Scalar[dtype]) -> NDArray[DType.bool]
```

Apply a SIMD comparision function of two variable.

!!! info "Constraints"
    Both arrays must have the same shape.

**Parameters:**

- `dtype` (`DType`): The element type.
- `func` (`fn[type: DType, simd_w: Int](SIMD[type, simd_w], SIMD[type, simd_w]) -> SIMD[DType.bool, simd_w]`): The SIMD comparision function to to apply.

**Args:**

- `self` (`_Self`)
- `array1` (`NDArray`): A NDArray.
- `scalar` (`Scalar`): A scalar.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

##### `math_func_is`

```mojo
math_func_is[dtype: DType, func: fn[type: DType, simd_w: Int](SIMD[type, simd_w]) -> SIMD[DType.bool, simd_w]](self: _Self, array: NDArray[dtype]) -> NDArray[DType.bool]
```

**Parameters:**

- `dtype` (`DType`)
- `func` (`fn[type: DType, simd_w: Int](SIMD[type, simd_w]) -> SIMD[DType.bool, simd_w]`)

**Args:**

- `self` (`_Self`)
- `array` (`NDArray`)

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>
