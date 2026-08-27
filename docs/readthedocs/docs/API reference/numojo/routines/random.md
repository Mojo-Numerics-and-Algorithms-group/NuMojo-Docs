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

<div class="prose-label">Notes</div>
    Similar to numpy.random but shape is always the first argument.

## Functions


<div class="fn-card" markdown="1">

### `rand`

<div class="overload-divider">Overload 1</div>

```mojo
def rand[dtype: DType = DType.float64](shape: NDArrayShape) -> NDArray[dtype]
```

Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

<div class="prose-label">Examples</div>
```mojo
from numojo import Shape
var arr = numojo.core.random.rand[numojo.i16](Shape(3,2,4))
print(arr)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def rand[dtype: DType = DType.float64](*shape: Int) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 3</div>

```mojo
def rand[dtype: DType = DType.float64](shape: List[Int]) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 4</div>

```mojo
def rand[dtype: DType = DType.float64](shape: VariadicList[Int]) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape)` Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`VariadicList[Int]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 5</div>

```mojo
def rand[dtype: DType = DType.float64](shape: NDArrayShape, min: Scalar[dtype], max: Scalar[dtype]) -> NDArray[dtype]
```

Creates an array of the given shape and populate it with random samples from a uniform distribution over [min, max). This is equivalent to `min + rand() * (max - min)`.

<div class="prose-label">Examples</div>
```mojo
from numojo import Shape
var arr = numojo.core.random.rand[numojo.i16](Shape(3,2,4), min=0, max=100)
print(arr)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `min` (`Scalar[dtype]`) `[imm]`: The minimum value of the random values.
- `max` (`Scalar[dtype]`) `[imm]`: The maximum value of the random values.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the dtype is not a floating-point type.

<div class="overload-divider">Overload 6</div>

```mojo
def rand[dtype: DType = DType.float64](*shape: Int, *, min: Scalar[dtype], max: Scalar[dtype]) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape, min, max)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [min, max). This is equivalent to `min + rand() * (max - min)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `min` (`Scalar[dtype]`) `[imm]`
- `max` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 7</div>

```mojo
def rand[dtype: DType = DType.float64](shape: List[Int], min: Scalar[dtype], max: Scalar[dtype]) -> NDArray[dtype]
```

Overloads the function `rand(shape: NDArrayShape, min, max)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [min, max). This is equivalent to `min + rand() * (max - min)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `min` (`Scalar[dtype]`) `[imm]`
- `max` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `randint`

<div class="overload-divider">Overload 1</div>

```mojo
def randint[dtype: DType = DType.int64](shape: NDArrayShape, low: Int, high: Int) -> NDArray[dtype] where dtype.is_integral()
```

Return an array of random integers from low (inclusive) to high (exclusive). Note that it is different from the built-in `random.randint()` function which returns integer in range low (inclusive) to high (inclusive).

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `low` (`Int`) `[imm]`: The minimum value of the random values.
- `high` (`Int`) `[imm]`: The maximum value of the random values.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the dtype is not a integer type.
NumojoError: If high is not greater than low.

<div class="overload-divider">Overload 2</div>

```mojo
def randint[dtype: DType = DType.int64](*shape: Int, *, low: Int, high: Int) -> NDArray[dtype] where dtype.is_integral()
```

Overloads the function `randint(shape: NDArrayShape, low, high)`. Return an array of random integers from low (inclusive) to high (exclusive). Note that it is different from the built-in `random.randint()` function which returns integer in range low (inclusive) to high (inclusive).

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `low` (`Int`) `[imm]`
- `high` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 3</div>

```mojo
def randint[dtype: DType = DType.int64](shape: NDArrayShape, high: Int) -> NDArray[dtype] where dtype.is_integral()
```

Return an array of random integers from 0 (inclusive) to high (exclusive).

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `high` (`Int`) `[imm]`: The maximum value of the random values.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If the dtype is not a integer type.
NumojoError: If high <= 0.

<div class="overload-divider">Overload 4</div>

```mojo
def randint[dtype: DType = DType.int64](*shape: Int, *, high: Int) -> NDArray[dtype] where dtype.is_integral()
```

Overloads the function `randint(shape: NDArrayShape, high)`. Return an array of random integers from 0 (inclusive) to high (exclusive).

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `high` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `randn`

<div class="overload-divider">Overload 1</div>

```mojo
def randn[dtype: DType = DType.float64](shape: NDArrayShape) -> NDArray[dtype]
```

Creates an array of the given shape and populate it with random samples from a standard normal distribution.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def randn[dtype: DType = DType.float64](*shape: Int) -> NDArray[dtype]
```

Overloads the function `randn(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a standard normal distribution.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 3</div>

```mojo
def randn[dtype: DType = DType.float64](shape: NDArrayShape, mean: Scalar[dtype], variance: Scalar[dtype]) -> NDArray[dtype]
```

Creates an array of the given shape and populate it with random samples from a normal distribution with given mean and variance.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `mean` (`Scalar[dtype]`) `[imm]`: The mean value of the random values.
- `variance` (`Scalar[dtype]`) `[imm]`: The variance of the random values.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 4</div>

```mojo
def randn[dtype: DType = DType.float64](*shape: Int, *, mean: Scalar[dtype], variance: Scalar[dtype]) -> NDArray[dtype]
```

Overloads the function `randn(shape: NDArrayShape, mean, variance)`. Creates an array of the given shape and populate it with random samples from a normal distribution with given mean and variance.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `mean` (`Scalar[dtype]`) `[imm]`
- `variance` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 5</div>

```mojo
def randn[dtype: DType = DType.float64](shape: List[Int], mean: Scalar[dtype], variance: Scalar[dtype]) -> NDArray[dtype]
```

Overloads the function `randn(shape: NDArrayShape, mean, variance)`. Creates an array of the given shape and populate it with random samples from a normal distribution with given mean and variance.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `mean` (`Scalar[dtype]`) `[imm]`
- `variance` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `exponential`

<div class="overload-divider">Overload 1</div>

```mojo
def exponential[dtype: DType = DType.float64](shape: NDArrayShape, scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Creates an array of the given shape and populate it with random samples from an exponential distribution with given scale parameter.

<div class="prose-label">Examples</div>
```py
var arr = numojo.random.exponential(Shape(3, 2, 4), 2.0)
print(arr)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `scale` (`Scalar[dtype]`) `[imm]`: The scale parameter of the exponential distribution (lambda).

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 2</div>

```mojo
def exponential[dtype: DType = DType.float64](*shape: Int, *, scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `exponential(shape: NDArrayShape, rate)`. Creates an array of the given shape and populate it with random samples from an exponential distribution with given scale parameter.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `scale` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"

<div class="overload-divider">Overload 3</div>

```mojo
def exponential[dtype: DType = DType.float64](shape: List[Int], scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `exponential(shape: NDArrayShape, rate)`. Creates an array of the given shape and populate it with random samples from an exponential distribution with given scale parameter.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `scale` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `randbool`

<div class="overload-divider">Overload 1</div>

```mojo
def randbool(shape: NDArrayShape, p: Float64 = 0.5) -> NDArray[DType.bool]
```

Creates an array of the given shape and populates it with random boolean values where each element is `True` with probability `p` and `False` with probability `1 - p`.

<div class="prose-label">Examples</div>
```py
var arr = numojo.random.randbool(Shape(3, 4))
var biased = numojo.random.randbool(Shape(10, 10), p=0.8)
```

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `p` (`Float64`) `[imm]`: Probability of `True` for each element. Must be in [0.0, 1.0].
   Defaults to 0.5.

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"
    NumojoError: If `p` is not in the range [0.0, 1.0].

<div class="overload-divider">Overload 2</div>

```mojo
def randbool(*shape: Int, *, p: Float64 = 0.5) -> NDArray[DType.bool]
```

Overloads the function `randbool(shape: NDArrayShape, p)`. Creates an array of the given shape and populates it with random boolean values where each element is `True` with probability `p`.

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `p` (`Float64`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"

<div class="overload-divider">Overload 3</div>

```mojo
def randbool(shape: List[Int], p: Float64 = 0.5) -> NDArray[DType.bool]
```

Overloads the function `randbool(shape: NDArrayShape, p)`. Creates an array of the given shape and populates it with random boolean values where each element is `True` with probability `p`.

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `p` (`Float64`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[DType.bool]`

!!! failure "Raises"


</div>
