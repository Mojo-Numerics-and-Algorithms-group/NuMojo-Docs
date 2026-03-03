# `numojo.routines.random`

Random (numojo.routines.random)

Creates array of the given shape and populate it with random samples from
a certain distribution.

This module is similar to `numpy.random`. However, in this module, the shape is
always appearing as the first argument.

## Functions


<div class="fn-card" markdown="1">

### `rand`

#### Overload 1

```mojo
rand[dtype: DType = DType.float64](shape: NDArrayShape) -> NDArray[dtype]
```

Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

Example:
```mojo
from numojo import Shape
var arr = numojo.core.random.rand[numojo.i16](Shape(3,2,4))
print(arr)
```

**Parameters:**

- `dtype` (`DType`): The data type of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`): The shape of the NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
rand[dtype: DType = DType.float64](*shape: Int) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `*shape` (`Int`)

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
rand[dtype: DType = DType.float64](shape: List[Int]) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `shape` (`List`)

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 4

```mojo
rand[dtype: DType = DType.float64](shape: VariadicList[Int]) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape)` Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `shape` (`VariadicList`)

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 5

```mojo
rand[dtype: DType = DType.float64](shape: NDArrayShape, min: Scalar[dtype], max: Scalar[dtype]) -> NDArray[dtype]
```

Creates an array of the given shape and populate it with random samples from a uniform distribution over [min, max). This is equivalent to `min + rand() * (max - min)`.

Example:
```mojo
from numojo import Shape
var arr = numojo.core.random.rand[numojo.i16](Shape(3,2,4), min=0, max=100)
print(arr)
```

**Parameters:**

- `dtype` (`DType`): The data type of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`): The shape of the NDArray.
- `min` (`Scalar`): The minimum value of the random values.
- `max` (`Scalar`): The maximum value of the random values.

**Returns:**

- `NDArray`

!!! failure "Raises"
    Error: If the dtype is not a floating-point type.

#### Overload 6

```mojo
rand[dtype: DType = DType.float64](*shape: Int, *, min: Scalar[dtype], max: Scalar[dtype]) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape, min, max)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [min, max). This is equivalent to `min + rand() * (max - min)`.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `*shape` (`Int`)
- `min` (`Scalar`)
- `max` (`Scalar`)

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 7

```mojo
rand[dtype: DType = DType.float64](shape: List[Int], min: Scalar[dtype], max: Scalar[dtype]) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape, min, max)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [min, max). This is equivalent to `min + rand() * (max - min)`.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `shape` (`List`)
- `min` (`Scalar`)
- `max` (`Scalar`)

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `randint`

#### Overload 1

```mojo
randint[dtype: DType = DType.int64](shape: NDArrayShape, low: Int, high: Int) -> NDArray[dtype] where dtype.is_integral()
```

Return an array of random integers from low (inclusive) to high (exclusive). Note that it is different from the built-in `random.randint()` function which returns integer in range low (inclusive) to high (inclusive).

**Parameters:**

- `dtype` (`DType`): The data type of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`): The shape of the NDArray.
- `low` (`Int`): The minimum value of the random values.
- `high` (`Int`): The maximum value of the random values.

**Returns:**

- `NDArray`

!!! failure "Raises"
    Error: If the dtype is not a integer type.
Error: If high is not greater than low.

#### Overload 2

```mojo
randint[dtype: DType = DType.int64](*shape: Int, *, low: Int, high: Int) -> NDArray[dtype] where dtype.is_integral()
```

Overloads the function `randint(shape: NDArrayShape, low, high)`. Return an array of random integers from low (inclusive) to high (exclusive). Note that it is different from the built-in `random.randint()` function which returns integer in range low (inclusive) to high (inclusive).

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `*shape` (`Int`)
- `low` (`Int`)
- `high` (`Int`)

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
randint[dtype: DType = DType.int64](shape: NDArrayShape, high: Int) -> NDArray[dtype] where dtype.is_integral()
```

Return an array of random integers from 0 (inclusive) to high (exclusive).

**Parameters:**

- `dtype` (`DType`): The data type of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`): The shape of the NDArray.
- `high` (`Int`): The maximum value of the random values.

**Returns:**

- `NDArray`

!!! failure "Raises"
    Error: If the dtype is not a integer type.
Error: If high <= 0.

#### Overload 4

```mojo
randint[dtype: DType = DType.int64](*shape: Int, *, high: Int) -> NDArray[dtype] where dtype.is_integral()
```

Overloads the function `randint(shape: NDArrayShape, high)`. Return an array of random integers from 0 (inclusive) to high (exclusive).

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `*shape` (`Int`)
- `high` (`Int`)

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `randn`

#### Overload 1

```mojo
randn[dtype: DType = DType.float64](shape: NDArrayShape) -> NDArray[dtype]
```

Creates an array of the given shape and populate it with random samples from a standard normal distribution.

**Parameters:**

- `dtype` (`DType`): The data type of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`): The shape of the NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
randn[dtype: DType = DType.float64](*shape: Int) -> NDArray[dtype]
```

Overloads the function `randn(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a standard normal distribution.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `*shape` (`Int`)

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
randn[dtype: DType = DType.float64](shape: NDArrayShape, mean: Scalar[dtype], variance: Scalar[dtype]) -> NDArray[dtype]
```

Creates an array of the given shape and populate it with random samples from a normal distribution with given mean and variance.

**Parameters:**

- `dtype` (`DType`): The data type of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`): The shape of the NDArray.
- `mean` (`Scalar`): The mean value of the random values.
- `variance` (`Scalar`): The variance of the random values.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 4

```mojo
randn[dtype: DType = DType.float64](*shape: Int, *, mean: Scalar[dtype], variance: Scalar[dtype]) -> NDArray[dtype]
```

Overloads the function `randn(shape: NDArrayShape, mean, variance)`. Creates an array of the given shape and populate it with random samples from a normal distribution with given mean and variance.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `*shape` (`Int`)
- `mean` (`Scalar`)
- `variance` (`Scalar`)

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 5

```mojo
randn[dtype: DType = DType.float64](shape: List[Int], mean: Scalar[dtype], variance: Scalar[dtype]) -> NDArray[dtype]
```

Overloads the function `randn(shape: NDArrayShape, mean, variance)`. Creates an array of the given shape and populate it with random samples from a normal distribution with given mean and variance.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `shape` (`List`)
- `mean` (`Scalar`)
- `variance` (`Scalar`)

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `exponential`

#### Overload 1

```mojo
exponential[dtype: DType = DType.float64](shape: NDArrayShape, scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Creates an array of the given shape and populate it with random samples from an exponential distribution with given scale parameter.

Example:
```py
var arr = numojo.random.exponential(Shape(3, 2, 4), 2.0)
print(arr)
```

**Parameters:**

- `dtype` (`DType`): The data type of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`): The shape of the NDArray.
- `scale` (`Scalar`): The scale parameter of the exponential distribution (lambda).

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
exponential[dtype: DType = DType.float64](*shape: Int, *, scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `exponential(shape: NDArrayShape, rate)`. Creates an array of the given shape and populate it with random samples from an exponential distribution with given scale parameter.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `*shape` (`Int`)
- `scale` (`Scalar`)

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
exponential[dtype: DType = DType.float64](shape: List[Int], scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `exponential(shape: NDArrayShape, rate)`. Creates an array of the given shape and populate it with random samples from an exponential distribution with given scale parameter.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `shape` (`List`)
- `scale` (`Scalar`)

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>
