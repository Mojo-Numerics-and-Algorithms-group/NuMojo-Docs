# `numojo.routines.random`

Random number generation and sampling.

Functions for creating arrays populated with random samples from various
distributions.

Exports
-------
- `seed`: Seed the global random number generator.
- `rand`, `uniform`: Uniform distribution [0, 1) (`uniform` is a
  `numpy.random`-named alias).
- `randint`: Random integers in range.
- `randn`, `normal`: Standard/general normal distribution (`normal` is a
  `numpy.random`-named alias).
- `exponential`: Exponential distribution.
- `randbool`: Random boolean values.
- `binomial`: Binomial distribution.
- `poisson`: Poisson distribution.
- `gamma`: Gamma distribution.
- `beta`: Beta distribution.
- `chisquare`: Chi-square distribution.
- `choice`: Sample elements from an array.
- `shuffle`: Shuffle an array in place along its first axis.
- `permutation`: Return a randomly permuted range or a shuffled copy of
  an array.

<div class="prose-label">Notes</div>
    Similar to numpy.random but shape is always the first argument.

## Functions


<div class="fn-card" markdown="1">

### `seed`

<div class="overload-divider">Overload 1</div>

```mojo
def seed()
```

Seed the global random number generator using a time-based value.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
nm.random.seed()
```

<div class="overload-divider">Overload 2</div>

```mojo
def seed(a: Int)
```

Seed the global random number generator with the given value, so that subsequent calls to functions in `numojo.random` are reproducible across runs.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
nm.random.seed(42)
var arr1 = nm.random.rand[nm.f64](nm.Shape(3))
nm.random.seed(42)
var arr2 = nm.random.rand[nm.f64](nm.Shape(3))
# `arr1` and `arr2` contain identical values.
```

<div class="prose-label">Args</div>

- `a` (`Int`) `[imm]`: The seed value.


</div>

<div class="fn-card" markdown="1">

### `rand`

<div class="overload-divider">Overload 1</div>

```mojo
def rand[dtype: DType = .float64](shape: NDArrayShape) -> NDArray[dtype] where dtype.is_floating_point()
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

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def rand[dtype: DType = .float64](*shape: Int) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `rand(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def rand[dtype: DType = .float64](shape: List[Int]) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `rand(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 4</div>

```mojo
def rand[dtype: DType = .float64](shape: VariadicList[Int]) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `rand(shape: NDArrayShape)` Creates an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`VariadicList[Int]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 5</div>

```mojo
def rand[dtype: DType = .float64](shape: NDArrayShape, min: Scalar[dtype], max: Scalar[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
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

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 6</div>

```mojo
def rand[dtype: DType = .float64](*shape: Int, *, min: Scalar[dtype], max: Scalar[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
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

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 7</div>

```mojo
def rand[dtype: DType = .float64](shape: List[Int], min: Scalar[dtype], max: Scalar[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
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

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `uniform`

<div class="overload-divider">Overload 1</div>

```mojo
def uniform[dtype: DType = .float64](shape: NDArrayShape, low: Scalar[dtype] = 0, high: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Creates an array of the given shape and populates it with random samples from a uniform distribution over [low, high).

<div class="prose-label">Notes</div>
Equivalent to `rand(shape, min=low, max=high)`, provided under
the name `numpy.random.uniform` uses.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var arr = nm.random.uniform[nm.f64](nm.Shape(3, 2), low=-1.0, high=1.0)
print(arr)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `low` (`Scalar[dtype]`) `[imm]`: The lower bound of the range (inclusive). Defaults to 0.
- `high` (`Scalar[dtype]`) `[imm]`: The upper bound of the range (exclusive). Defaults to 1.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def uniform[dtype: DType = .float64](*shape: Int, *, low: Scalar[dtype] = 0, high: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `uniform(shape: NDArrayShape, low, high)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `low` (`Scalar[dtype]`) `[imm]`
- `high` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def uniform[dtype: DType = .float64](shape: List[Int], low: Scalar[dtype] = 0, high: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `uniform(shape: NDArrayShape, low, high)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `low` (`Scalar[dtype]`) `[imm]`
- `high` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `randint`

<div class="overload-divider">Overload 1</div>

```mojo
def randint[dtype: DType = .int64](shape: NDArrayShape, low: Int, high: Int) -> NDArray[dtype] where dtype.is_integral()
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
    NumojoError: If high is not greater than low.

<div class="overload-divider">Overload 2</div>

```mojo
def randint[dtype: DType = .int64](*shape: Int, *, low: Int, high: Int) -> NDArray[dtype] where dtype.is_integral()
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

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def randint[dtype: DType = .int64](shape: NDArrayShape, high: Int) -> NDArray[dtype] where dtype.is_integral()
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
def randint[dtype: DType = .int64](*shape: Int, *, high: Int) -> NDArray[dtype] where dtype.is_integral()
```

Overloads the function `randint(shape: NDArrayShape, high)`. Return an array of random integers from 0 (inclusive) to high (exclusive).

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `high` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `randn`

<div class="overload-divider">Overload 1</div>

```mojo
def randn[dtype: DType = .float64](shape: NDArrayShape) -> NDArray[dtype]
```

Creates an array of the given shape and populate it with random samples from a standard normal distribution.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def randn[dtype: DType = .float64](*shape: Int) -> NDArray[dtype]
```

Overloads the function `randn(shape: NDArrayShape)`. Creates an array of the given shape and populate it with random samples from a standard normal distribution.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def randn[dtype: DType = .float64](shape: NDArrayShape, mean: Scalar[dtype], variance: Scalar[dtype]) -> NDArray[dtype]
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

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 4</div>

```mojo
def randn[dtype: DType = .float64](*shape: Int, *, mean: Scalar[dtype], variance: Scalar[dtype]) -> NDArray[dtype]
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

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 5</div>

```mojo
def randn[dtype: DType = .float64](shape: List[Int], mean: Scalar[dtype], variance: Scalar[dtype]) -> NDArray[dtype]
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

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `normal`

<div class="overload-divider">Overload 1</div>

```mojo
def normal[dtype: DType = .float64](shape: NDArrayShape, loc: Scalar[dtype] = 0, scale: Scalar[dtype] = 1) -> NDArray[dtype]
```

Creates an array of the given shape and populates it with random samples from a normal distribution with mean `loc` and standard deviation `scale`.

<div class="prose-label">Notes</div>
Equivalent to `randn(shape, mean=loc, variance=scale**2)`,
provided under the name `numpy.random.normal` uses.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var arr = nm.random.normal[nm.f64](nm.Shape(3, 2), loc=1.0, scale=2.0)
print(arr)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `loc` (`Scalar[dtype]`) `[imm]`: The mean of the distribution. Defaults to 0.
- `scale` (`Scalar[dtype]`) `[imm]`: The standard deviation of the distribution. Defaults to 1.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def normal[dtype: DType = .float64](*shape: Int, *, loc: Scalar[dtype] = 0, scale: Scalar[dtype] = 1) -> NDArray[dtype]
```

Overloads the function `normal(shape: NDArrayShape, loc, scale)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `loc` (`Scalar[dtype]`) `[imm]`
- `scale` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def normal[dtype: DType = .float64](shape: List[Int], loc: Scalar[dtype] = 0, scale: Scalar[dtype] = 1) -> NDArray[dtype]
```

Overloads the function `normal(shape: NDArrayShape, loc, scale)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `loc` (`Scalar[dtype]`) `[imm]`
- `scale` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `exponential`

<div class="overload-divider">Overload 1</div>

```mojo
def exponential[dtype: DType = .float64](shape: NDArrayShape, scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
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

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def exponential[dtype: DType = .float64](*shape: Int, *, scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `exponential(shape: NDArrayShape, rate)`. Creates an array of the given shape and populate it with random samples from an exponential distribution with given scale parameter.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `scale` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def exponential[dtype: DType = .float64](shape: List[Int], scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `exponential(shape: NDArrayShape, rate)`. Creates an array of the given shape and populate it with random samples from an exponential distribution with given scale parameter.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `scale` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `randbool`

<div class="overload-divider">Overload 1</div>

```mojo
def randbool(shape: NDArrayShape, p: Float64 = 0.5) -> NDArray[.bool]
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

- `NDArray[.bool]`

!!! failure "Raises"
    NumojoError: If `p` is not in the range [0.0, 1.0].

<div class="overload-divider">Overload 2</div>

```mojo
def randbool(*shape: Int, *, p: Float64 = 0.5) -> NDArray[.bool]
```

Overloads the function `randbool(shape: NDArrayShape, p)`. Creates an array of the given shape and populates it with random boolean values where each element is `True` with probability `p`.

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `p` (`Float64`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[.bool]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def randbool(shape: List[Int], p: Float64 = 0.5) -> NDArray[.bool]
```

Overloads the function `randbool(shape: NDArrayShape, p)`. Creates an array of the given shape and populates it with random boolean values where each element is `True` with probability `p`.

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `p` (`Float64`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[.bool]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `binomial`

<div class="overload-divider">Overload 1</div>

```mojo
def binomial[dtype: DType = .int64](shape: NDArrayShape, n: Int, p: Float64) -> NDArray[dtype] where dtype.is_integral()
```

Creates an array of the given shape and populates it with random samples from a binomial distribution: the number of successes in `n` independent trials, each succeeding with probability `p`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var arr = nm.random.binomial(nm.Shape(3, 2), n=10, p=0.5)
print(arr)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `n` (`Int`) `[imm]`: The number of trials.
- `p` (`Float64`) `[imm]`: The probability of success of each trial.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `n` is negative or `p` is not in [0.0, 1.0].

<div class="overload-divider">Overload 2</div>

```mojo
def binomial[dtype: DType = .int64](*shape: Int, *, n: Int, p: Float64) -> NDArray[dtype] where dtype.is_integral()
```

Overloads the function `binomial(shape: NDArrayShape, n, p)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `n` (`Int`) `[imm]`
- `p` (`Float64`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def binomial[dtype: DType = .int64](shape: List[Int], n: Int, p: Float64) -> NDArray[dtype] where dtype.is_integral()
```

Overloads the function `binomial(shape: NDArrayShape, n, p)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `n` (`Int`) `[imm]`
- `p` (`Float64`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `poisson`

<div class="overload-divider">Overload 1</div>

```mojo
def poisson[dtype: DType = .int64](shape: NDArrayShape, lam: Float64 = 1) -> NDArray[dtype] where dtype.is_integral()
```

Creates an array of the given shape and populates it with random samples from a Poisson distribution with rate parameter `lam`, using Knuth's algorithm.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var arr = nm.random.poisson(nm.Shape(3, 2), lam=4.0)
print(arr)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `lam` (`Float64`) `[imm]`: The rate (expected number of occurrences). Defaults to 1.0.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `lam` is negative.

<div class="overload-divider">Overload 2</div>

```mojo
def poisson[dtype: DType = .int64](*shape: Int, *, lam: Float64 = 1) -> NDArray[dtype] where dtype.is_integral()
```

Overloads the function `poisson(shape: NDArrayShape, lam)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `lam` (`Float64`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def poisson[dtype: DType = .int64](shape: List[Int], lam: Float64 = 1) -> NDArray[dtype] where dtype.is_integral()
```

Overloads the function `poisson(shape: NDArrayShape, lam)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `lam` (`Float64`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `gamma`

<div class="overload-divider">Overload 1</div>

```mojo
def gamma[dtype: DType = .float64](shape: NDArrayShape, k: Scalar[dtype], scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Creates an array of the given shape and populates it with random samples from a gamma distribution with shape parameter `k` (matching `numpy.random.gamma`'s `shape` parameter, renamed here to avoid clashing with the array `shape` argument) and scale parameter `scale`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var arr = nm.random.gamma[nm.f64](nm.Shape(3, 2), k=2.0, scale=2.0)
print(arr)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `k` (`Scalar[dtype]`) `[imm]`: The shape parameter of the distribution. Must be positive.
- `scale` (`Scalar[dtype]`) `[imm]`: The scale parameter of the distribution. Defaults to 1.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `k` or `scale` is not positive.

<div class="overload-divider">Overload 2</div>

```mojo
def gamma[dtype: DType = .float64](*shape: Int, *, k: Scalar[dtype], scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `gamma(shape: NDArrayShape, k, scale)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `k` (`Scalar[dtype]`) `[imm]`
- `scale` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def gamma[dtype: DType = .float64](shape: List[Int], k: Scalar[dtype], scale: Scalar[dtype] = 1) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `gamma(shape: NDArrayShape, k, scale)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `k` (`Scalar[dtype]`) `[imm]`
- `scale` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `beta`

<div class="overload-divider">Overload 1</div>

```mojo
def beta[dtype: DType = .float64](shape: NDArrayShape, a: Scalar[dtype], b: Scalar[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Creates an array of the given shape and populates it with random samples from a beta distribution with shape parameters `a` and `b`, derived from two independent gamma samples as `X / (X + Y)` with `X ~ Gamma(a, 1)` and `Y ~ Gamma(b, 1)`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var arr = nm.random.beta[nm.f64](nm.Shape(3, 2), a=2.0, b=5.0)
print(arr)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `a` (`Scalar[dtype]`) `[imm]`: The first shape parameter. Must be positive.
- `b` (`Scalar[dtype]`) `[imm]`: The second shape parameter. Must be positive.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `a` or `b` is not positive.

<div class="overload-divider">Overload 2</div>

```mojo
def beta[dtype: DType = .float64](*shape: Int, *, a: Scalar[dtype], b: Scalar[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `beta(shape: NDArrayShape, a, b)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `a` (`Scalar[dtype]`) `[imm]`
- `b` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def beta[dtype: DType = .float64](shape: List[Int], a: Scalar[dtype], b: Scalar[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `beta(shape: NDArrayShape, a, b)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `a` (`Scalar[dtype]`) `[imm]`
- `b` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `chisquare`

<div class="overload-divider">Overload 1</div>

```mojo
def chisquare[dtype: DType = .float64](shape: NDArrayShape, df: Scalar[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Creates an array of the given shape and populates it with random samples from a chi-square distribution with `df` degrees of freedom, equivalent to `Gamma(df / 2, 2)`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var arr = nm.random.chisquare[nm.f64](nm.Shape(3, 2), df=4.0)
print(arr)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the NDArray.
- `df` (`Scalar[dtype]`) `[imm]`: The degrees of freedom. Must be positive.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `df` is not positive.

<div class="overload-divider">Overload 2</div>

```mojo
def chisquare[dtype: DType = .float64](*shape: Int, *, df: Scalar[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `chisquare(shape: NDArrayShape, df)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `df` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def chisquare[dtype: DType = .float64](shape: List[Int], df: Scalar[dtype]) -> NDArray[dtype] where dtype.is_floating_point()
```

Overloads the function `chisquare(shape: NDArrayShape, df)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `df` (`Scalar[dtype]`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `shuffle`

```mojo
def shuffle[dtype: DType](mut A: NDArray[dtype])
```

Shuffle the elements of an array in place along its first axis. For a 1-D array, individual elements are shuffled. For an N-D array, whole sub-arrays along axis 0 are permuted (the array must be C-contiguous).

<div class="prose-label">Notes</div>
Matches `numpy.random.shuffle`.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var arr = nm.arange[nm.f64](6)
nm.random.shuffle(arr)
print(arr)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[mut]`: The array to shuffle in place.

!!! failure "Raises"
    NumojoError: If the array has more than one dimension and is not
C-contiguous.


</div>

<div class="fn-card" markdown="1">

### `permutation`

<div class="overload-divider">Overload 1</div>

```mojo
def permutation[dtype: DType = .int64](n: Int) -> NDArray[dtype] where dtype.is_integral()
```

Return a randomly permuted range, equivalent to shuffling `arange(n)`.

<div class="prose-label">Notes</div>
Matches `numpy.random.permutation` when called with an integer.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var arr = nm.random.permutation(5)
print(arr)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `n` (`Int`) `[imm]`: The length of the range to permute.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 2</div>

```mojo
def permutation[dtype: DType](A: NDArray[dtype]) -> NDArray[dtype]
```

Return a shuffled copy of `A` along its first axis. Unlike `shuffle`, `A` itself is not modified.

<div class="prose-label">Notes</div>
Matches `numpy.random.permutation` when called with an array.

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var arr = nm.arange[nm.f64](6)
var permuted = nm.random.permutation(arr)
print(permuted)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `A` (`NDArray[dtype]`) `[imm]`: The array to permute.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>

<div class="fn-card" markdown="1">

### `choice`

<div class="overload-divider">Overload 1</div>

```mojo
def choice[dtype: DType](shape: NDArrayShape, A: NDArray[dtype], replace: Bool = True) -> NDArray[dtype]
```

Randomly sample elements from `A` (treated as flattened), with or without replacement.

<div class="prose-label">Notes</div>
Matches `numpy.random.choice` without weights (no `p` parameter).

<div class="prose-label">Examples</div>
```mojo
import numojo as nm
var pool = nm.arange[nm.f64](10)
var sample = nm.random.choice(nm.Shape(5), pool, replace=False)
print(sample)
```

<div class="prose-label">Parameters</div>

- `dtype` (`DType`): The data type of the NDArray elements.

<div class="prose-label">Args</div>

- `shape` (`NDArrayShape`) `[imm]`: The shape of the output array.
- `A` (`NDArray[dtype]`) `[imm]`: The array to sample from.
- `replace` (`Bool`) `[imm]`: Whether sampling is with replacement. Defaults to
    `True`.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"
    NumojoError: If `A` is empty, or if `replace` is `False` and the
requested sample size exceeds `A.size`.

<div class="overload-divider">Overload 2</div>

```mojo
def choice[dtype: DType](*shape: Int, *, A: NDArray[dtype], replace: Bool = True) -> NDArray[dtype]
```

Overloads the function `choice(shape: NDArrayShape, A, replace)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `*shape` (`Int`) `[imm]`
- `A` (`NDArray[dtype]`) `[imm]`
- `replace` (`Bool`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*

<div class="overload-divider">Overload 3</div>

```mojo
def choice[dtype: DType](shape: List[Int], A: NDArray[dtype], replace: Bool = True) -> NDArray[dtype]
```

Overloads the function `choice(shape: NDArrayShape, A, replace)`.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `shape` (`List[Int]`) `[imm]`
- `A` (`NDArray[dtype]`) `[imm]`
- `replace` (`Bool`) `[imm]`

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

<div class="prose-label">Raises</div>

*Not documented in source.*


</div>
