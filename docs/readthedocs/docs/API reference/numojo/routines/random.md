# `numojo.routines.random`

Random number generation and sampling.

Functions for creating arrays populated with random samples from various
distributions.

Exports
-------
- `rand`: Uniform distribution [0, 1).
- `randint`: Random integers in range.
- `randn`: Standard normal distribution.
- `exponential`: Exponential distribution.
- `randbool`: Random boolean values.

Notes:
    Similar to numpy.random but shape is always the first argument.

## Functions


<div class="fn-card" markdown="1">

### `rand`

#### Overload 1

```mojo
def rand[dtype: DType = DType.float64](shape: NDArrayShape) -> NDArray[dtype]
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

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def rand[dtype: DType = DType.float64](*shape: Int) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `*shape` (`Int`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def rand[dtype: DType = DType.float64](shape: List[Int]) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `shape` (`List[Int]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 4

```mojo
def rand[dtype: DType = DType.float64](shape: VariadicList[Int]) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape)` Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `shape` (`VariadicList[Int]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 5

```mojo
def rand[dtype: DType = DType.float64](shape: NDArrayShape, min: Scalar[dtype], max: Scalar[dtype]) -> NDArray[dtype]
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

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `min` (`Scalar[dtype]`) `[imm]`: The minimum value of the random values.
- `max` (`Scalar[dtype]`) `[imm]`: The maximum value of the random values.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the dtype is not a floating-point type.

#### Overload 6

```mojo
def rand[dtype: DType = DType.float64](*shape: Int, *, min: Scalar[dtype], max: Scalar[dtype]) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape, min, max)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [min, max). This is equivalent to `min + rand() * (max - min)`.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `*shape` (`Int`) `[imm]`
- `min` (`Scalar[dtype]`) `[imm]`
- `max` (`Scalar[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 7

```mojo
def rand[dtype: DType = DType.float64](shape: List[Int], min: Scalar[dtype], max: Scalar[dtype]) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape, min, max)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [min, max). This is equivalent to `min + rand() * (max - min)`.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `shape` (`List[Int]`) `[imm]`
- `min` (`Scalar[dtype]`) `[imm]`
- `max` (`Scalar[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `randint`

#### Overload 1

```mojo
def randint[dtype: DType = DType.int64](shape: NDArrayShape, low: Int, high: Int) -> NDArray[dtype] where dtype.is_integral()
```

Return an array of random integers from low (inclusive) to high (exclusive). Note that it is different from the built-in `random.randint()` function which returns integer in range low (inclusive) to high (inclusive).

**Parameters:**

- `dtype` (`DType`): The data type of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `low` (`Int`) `[imm]`: The minimum value of the random values.
- `high` (`Int`) `[imm]`: The maximum value of the random values.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the dtype is not a integer type.
NumojoError: If high is not greater than low.

#### Overload 2

```mojo
def randint[dtype: DType = DType.int64](*shape: Int, *, low: Int, high: Int) -> NDArray[dtype] where dtype.is_integral()
```

Overloads the function `randint(shape: NDArrayShape, low, high)`. Return an array of random integers from low (inclusive) to high (exclusive). Note that it is different from the built-in `random.randint()` function which returns integer in range low (inclusive) to high (inclusive).

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `*shape` (`Int`) `[imm]`
- `low` (`Int`) `[imm]`
- `high` (`Int`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def randint[dtype: DType = DType.int64](shape: NDArrayShape, high: Int) -> NDArray[dtype] where dtype.is_integral()
```

Return an array of random integers from 0 (inclusive) to high (exclusive).

**Parameters:**

- `dtype` (`DType`): The data type of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `high` (`Int`) `[imm]`: The maximum value of the random values.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the dtype is not a integer type.
NumojoError: If high <= 0.

#### Overload 4

```mojo
def randint[dtype: DType = DType.int64](*shape: Int, *, high: Int) -> NDArray[dtype] where dtype.is_integral()
```

Overloads the function `randint(shape: NDArrayShape, high)`. Return an array of random integers from 0 (inclusive) to high (exclusive).

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `*shape` (`Int`) `[imm]`
- `high` (`Int`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `randn`

#### Overload 1

```mojo
def randn[dtype: DType = DType.float64](shape: NDArrayShape) -> NDArray[dtype]
```

Creates an array of the given shape and populate it with random samples from a standard normal distribution.

**Parameters:**

- `dtype` (`DType`): The data type of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def randn[dtype: DType = DType.float64](*shape: Int) -> NDArray[dtype]
```

Overloads the function `randn(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a standard normal distribution.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `*shape` (`Int`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def randn[dtype: DType = DType.float64](shape: NDArrayShape, mean: Scalar[dtype], variance: Scalar[dtype]) -> NDArray[dtype]
```

Creates an array of the given shape and populate it with random samples from a normal distribution with given mean and variance.

**Parameters:**

- `dtype` (`DType`): The data type of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `mean` (`Scalar[dtype]`) `[imm]`: The mean value of the random values.
- `variance` (`Scalar[dtype]`) `[imm]`: The variance of the random values.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 4

```mojo
def randn[dtype: DType = DType.float64](*shape: Int, *, mean: Scalar[dtype], variance: Scalar[dtype]) -> NDArray[dtype]
```

Overloads the function `randn(shape: NDArrayShape, mean, variance)`. Creates an array of the given shape and populate it with random samples from a normal distribution with given mean and variance.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `*shape` (`Int`) `[imm]`
- `mean` (`Scalar[dtype]`) `[imm]`
- `variance` (`Scalar[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 5

```mojo
def randn[dtype: DType = DType.float64](shape: List[Int], mean: Scalar[dtype], variance: Scalar[dtype]) -> NDArray[dtype]
```

Overloads the function `randn(shape: NDArrayShape, mean, variance)`. Creates an array of the given shape and populate it with random samples from a normal distribution with given mean and variance.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `shape` (`List[Int]`) `[imm]`
- `mean` (`Scalar[dtype]`) `[imm]`
- `variance` (`Scalar[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `exponential`

#### Overload 1

```mojo
def exponential[dtype: DType = DType.float64](shape: NDArrayShape, scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
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

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `scale` (`Scalar[dtype]`) `[imm]`: The scale parameter of the exponential distribution (lambda).

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def exponential[dtype: DType = DType.float64](*shape: Int, *, scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `exponential(shape: NDArrayShape, rate)`. Creates an array of the given shape and populate it with random samples from an exponential distribution with given scale parameter.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `*shape` (`Int`) `[imm]`
- `scale` (`Scalar[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def exponential[dtype: DType = DType.float64](shape: List[Int], scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `exponential(shape: NDArrayShape, rate)`. Creates an array of the given shape and populate it with random samples from an exponential distribution with given scale parameter.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `shape` (`List[Int]`) `[imm]`
- `scale` (`Scalar[dtype]`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `randbool`

#### Overload 1

```mojo
def randbool(shape: NDArrayShape, p: Float64 = 0.5) -> NDArray[DType.bool]
```

Creates an array of the given shape and populates it with random boolean values where each element is `True` with probability `p` and `False` with probability `1 - p`.

Example:
```py
var arr = numojo.random.randbool(Shape(3, 4))
var biased = numojo.random.randbool(Shape(10, 10), p=0.8)
```

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `p` (`Float64`) `[imm]`: Probability of `True` for each element. Must be in [0.0, 1.0].
   Defaults to 0.5.

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"
    NumojoError: If `p` is not in the range [0.0, 1.0].

#### Overload 2

```mojo
def randbool(*shape: Int, *, p: Float64 = 0.5) -> NDArray[DType.bool]
```

Overloads the function `randbool(shape: NDArrayShape, p)`. Creates an array of the given shape and populates it with random boolean values where each element is `True` with probability `p`.

**Args:**

- `*shape` (`Int`) `[imm]`
- `p` (`Float64`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"

#### Overload 3

```mojo
def randbool(shape: List[Int], p: Float64 = 0.5) -> NDArray[DType.bool]
```

Overloads the function `randbool(shape: NDArrayShape, p)`. Creates an array of the given shape and populates it with random boolean values where each element is `True` with probability `p`.

**Args:**

- `shape` (`List[Int]`) `[imm]`
- `p` (`Float64`) `[imm]`

**Returns:**

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>
