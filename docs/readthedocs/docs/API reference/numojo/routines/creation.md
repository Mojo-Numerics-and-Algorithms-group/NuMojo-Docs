# `numojo.routines.creation`

Functions for creating and initializing NDArray and ComplexNDArray objects.

This module provides convenient factory functions for creating arrays with various
initialization strategies (zeros, ones, empty, full, linspace, etc.) and helper
functions for array generation from Python objects and mathematical sequences.

Exports
-------
- `arange`: Evenly spaced values in interval.
- `linspace`: Values spaced linearly in interval.
- `logspace`: Values spaced logarithmically in interval.
- `zeros`: Array filled with zeros.
- `ones`: Array filled with ones.
- `full`: Array filled with constant value.
- `empty`: Uninitialized array.
- `array`: Create from Python object or scalar.

## Functions


<div class="fn-card" markdown="1">

### `arange`

#### Overload 1

```mojo
def arange[dtype: DType = DType.float64](start: Scalar[dtype], stop: Scalar[dtype], step: Scalar[dtype] = 1) -> NDArray[dtype]
```

Generate evenly spaced values within a given interval.

Examples:
```mojo
import numojo as nm

# Basic usage
var arr = nm.arange[nm.f64](0.0, 10.0, 2.0)
print(arr)  # [0.0, 2.0, 4.0, 6.0, 8.0]

# With negative step
var arr2 = nm.arange[nm.f64](10.0, 0.0, -2.0)
print(arr2)  # [10.0, 8.0, 6.0, 4.0, 2.0]
```

**Parameters:**

- `dtype` (`DType`): Datatype of the output array.

**Args:**

- `start` (`Scalar[dtype]`) `[imm]`: Start value (inclusive).
- `stop` (`Scalar[dtype]`) `[imm]`: End value (exclusive).
- `step` (`Scalar[dtype]`) `[imm]`: Step size between consecutive elements (default 1).

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def arange[dtype: DType = DType.float64](stop: Scalar[dtype]) -> NDArray[dtype]
```

Generate evenly spaced values from 0 to stop.

Overload with start=0 and step=1 for convenience.

Examples:
```mojo
import numojo as nm

var arr = nm.arange[nm.f64](5.0)
print(arr)  # [0.0, 1.0, 2.0, 3.0, 4.0]
```

**Parameters:**

- `dtype` (`DType`): Datatype of the output array.

**Args:**

- `stop` (`Scalar[dtype]`) `[imm]`: End value (exclusive).

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def arange[cdtype: ComplexDType = ComplexDType.float64](start: ComplexSIMD[cdtype], stop: ComplexSIMD[cdtype], step: ComplexSIMD[cdtype] = ComplexSIMD(SIMD(1), SIMD(1))) -> ComplexNDArray[cdtype]
```

Generate evenly spaced complex values within a given interval.

Examples:
```mojo
import numojo as nm

var start = nm.CScalar[nm.cf64](0.0, 0.0)
var stop = nm.CScalar[nm.cf64](5.0, 5.0)
var step = nm.CScalar[nm.cf64](1.0, 1.0)
var arr = nm.arange[nm.cf64](start, stop, step)
```

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `start` (`ComplexSIMD[cdtype]`) `[imm]`: Start value (inclusive).
- `stop` (`ComplexSIMD[cdtype]`) `[imm]`: End value (exclusive).
- `step` (`ComplexSIMD[cdtype]`) `[imm]`: Step size between consecutive elements (default 1+1j).

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"

#### Overload 4

```mojo
def arange[cdtype: ComplexDType = ComplexDType.float64](stop: ComplexSIMD[cdtype]) -> ComplexNDArray[cdtype]
```

Generate evenly spaced complex values from 0 to stop.

Overload with start=0+0j and step=1+1j for convenience.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `stop` (`ComplexSIMD[cdtype]`) `[imm]`: End value (exclusive).

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `linspace`

#### Overload 1

```mojo
def linspace[dtype: DType = DType.float64, parallel: Bool = False](start: Scalar[dtype], stop: Scalar[dtype], num: Int = Int(50), endpoint: Bool = True) -> NDArray[dtype] where dtype.is_floating_point()
```

Generate evenly spaced numbers over a specified interval.

Examples:
```mojo
import numojo as nm

# Basic usage
var arr = nm.linspace[nm.f64](0.0, 10.0, 5)
print(arr)  # [0.0, 2.5, 5.0, 7.5, 10.0]

# Without endpoint
var arr2 = nm.linspace[nm.f64](0.0, 10.0, 5, endpoint=False)
print(arr2)  # [0.0, 2.0, 4.0, 6.0, 8.0]

# Parallel computation for large arrays
var large = nm.linspace[nm.f64, parallel=True](0.0, 1000.0, 10000)
```

**Parameters:**

- `dtype` (`DType`): Datatype of the output array (must be floating-point).
- `parallel` (`Bool`): Whether to use parallelization for computation (default False).

**Args:**

- `start` (`Scalar[dtype]`) `[imm]`: Starting value of the sequence.
- `stop` (`Scalar[dtype]`) `[imm]`: End value of the sequence.
- `num` (`Int`) `[imm]`: Number of samples to generate (default 50).
- `endpoint` (`Bool`) `[imm]`: Whether to include `stop` in the result (default True).

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def linspace[cdtype: ComplexDType = ComplexDType.float64, parallel: Bool = False](start: ComplexSIMD[cdtype], stop: ComplexSIMD[cdtype], num: Int = Int(50), endpoint: Bool = True) -> ComplexNDArray[cdtype]
```

Generate evenly spaced complex numbers over a specified interval.

Examples:
```mojo
import numojo as nm

var start = nm.CScalar[nm.cf64](0.0, 0.0)
var stop = nm.CScalar[nm.cf64](10.0, 10.0)
var arr = nm.linspace[nm.cf64](start, stop, 5)
```

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array (must be floating-point).
- `parallel` (`Bool`): Whether to use parallelization for computation (default False).

**Args:**

- `start` (`ComplexSIMD[cdtype]`) `[imm]`: Starting complex value of the sequence.
- `stop` (`ComplexSIMD[cdtype]`) `[imm]`: End complex value of the sequence.
- `num` (`Int`) `[imm]`: Number of samples to generate (default 50).
- `endpoint` (`Bool`) `[imm]`: Whether to include `stop` in the result (default True).

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `logspace`

#### Overload 1

```mojo
def logspace[dtype: DType = DType.float64, parallel: Bool = False](start: Scalar[dtype], stop: Scalar[dtype], num: Int, endpoint: Bool = True, base: Scalar[dtype] = 10) -> NDArray[dtype] where dtype.is_floating_point()
```

Generate logarithmically spaced numbers over a specified interval.

The sequence starts at base^start and ends at base^stop.

Examples:
```mojo
import numojo as nm

# Logarithmic spacing from 10^0 to 10^3
var arr = nm.logspace[nm.f64](0.0, 3.0, 4)
print(arr)  # [1.0, 10.0, 100.0, 1000.0]

# Base 2 logarithmic spacing
var arr2 = nm.logspace[nm.f64](0.0, 4.0, 5, base=2.0)
print(arr2)  # [1.0, 2.0, 4.0, 8.0, 16.0]
```

**Parameters:**

- `dtype` (`DType`): Datatype of the output array (must be floating-point).
- `parallel` (`Bool`): Whether to use parallelization for computation (default False).

**Args:**

- `start` (`Scalar[dtype]`) `[imm]`: Base^start is the starting value of the sequence.
- `stop` (`Scalar[dtype]`) `[imm]`: Base^stop is the final value of the sequence.
- `num` (`Int`) `[imm]`: Number of samples to generate.
- `endpoint` (`Bool`) `[imm]`: Whether to include base^stop in the result (default True).
- `base` (`Scalar[dtype]`) `[imm]`: The base of the logarithm (default 10.0).

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def logspace[cdtype: ComplexDType = ComplexDType.float64, parallel: Bool = False](start: ComplexSIMD[cdtype], stop: ComplexSIMD[cdtype], num: Int, endpoint: Bool = True, base: ComplexSIMD[cdtype] = ComplexSIMD(SIMD(10), SIMD(10))) -> ComplexNDArray[cdtype] where cdtype.is_floating_point()
```

Generate logarithmically spaced complex numbers over a specified interval.

The sequence starts at base^start and ends at base^stop.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array (must be floating-point).
- `parallel` (`Bool`): Whether to use parallelization for computation (default False).

**Args:**

- `start` (`ComplexSIMD[cdtype]`) `[imm]`: Base^start is the starting complex value of the sequence.
- `stop` (`ComplexSIMD[cdtype]`) `[imm]`: Base^stop is the final complex value of the sequence.
- `num` (`Int`) `[imm]`: Number of samples to generate.
- `endpoint` (`Bool`) `[imm]`: Whether to include base^stop in the result (default True).
- `base` (`ComplexSIMD[cdtype]`) `[imm]`: The complex base of the logarithm (default 10+10j).

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `geomspace`

#### Overload 1

```mojo
def geomspace[dtype: DType = DType.float64](start: Scalar[dtype], stop: Scalar[dtype], num: Int, endpoint: Bool = True) -> NDArray[dtype] where dtype.is_floating_point()
```

Generate numbers spaced evenly on a log scale (geometric progression).

Examples:
```mojo
import numojo as nm

# Geometric progression from 1 to 1000
var arr = nm.geomspace[nm.f64](1.0, 1000.0, 4)
print(arr)  # [1.0, 10.0, 100.0, 1000.0]
```

Notes:
This is similar to logspace, but with endpoints specified directly.

**Parameters:**

- `dtype` (`DType`): Datatype of the output array (must be floating-point).

**Args:**

- `start` (`Scalar[dtype]`) `[imm]`: The starting value of the sequence.
- `stop` (`Scalar[dtype]`) `[imm]`: The final value of the sequence.
- `num` (`Int`) `[imm]`: Number of samples to generate.
- `endpoint` (`Bool`) `[imm]`: Whether to include `stop` in the result (default True).

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def geomspace[cdtype: ComplexDType = ComplexDType.float64](start: ComplexSIMD[cdtype], stop: ComplexSIMD[cdtype], num: Int, endpoint: Bool = True) -> ComplexNDArray[cdtype] where cdtype.is_floating_point()
```

Generate complex numbers spaced evenly on a log scale (geometric progression).

Notes:
This is similar to logspace, but with endpoints specified directly.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array (must be floating-point).

**Args:**

- `start` (`ComplexSIMD[cdtype]`) `[imm]`: The starting complex value of the sequence.
- `stop` (`ComplexSIMD[cdtype]`) `[imm]`: The final complex value of the sequence.
- `num` (`Int`) `[imm]`: Number of samples to generate.
- `endpoint` (`Bool`) `[imm]`: Whether to include `stop` in the result (default True).

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `empty`

#### Overload 1

```mojo
def empty[dtype: DType = DType.float64](shape: NDArrayShape) -> NDArray[dtype]
```

Generate an empty NDArray of given shape with arbitrary values.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: Shape of the NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def empty[dtype: DType = DType.float64](shape: List[Int]) -> NDArray[dtype]
```

Generate an empty NDArray from a list of integers.

Overload of `empty` that accepts a list of integers for the shape.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`List[Int]`) `[imm]`: Shape as a list of integers.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def empty[dtype: DType = DType.float64](shape: VariadicList[Int]) -> NDArray[dtype]
```

Generate an empty NDArray from variadic integer arguments.

Overload of `empty` that accepts variadic integers for the shape.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`VariadicList[Int]`) `[imm]`: Shape as variadic integers.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 4

```mojo
def empty[cdtype: ComplexDType = ComplexDType.float64](shape: NDArrayShape) -> ComplexNDArray[cdtype]
```

Generate an empty ComplexNDArray of given shape with arbitrary values.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: Shape of the ComplexNDArray.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"

#### Overload 5

```mojo
def empty[cdtype: ComplexDType = ComplexDType.float64](shape: List[Int]) -> ComplexNDArray[cdtype]
```

Generate an empty ComplexNDArray from a list of integers.

Overload of `empty` that accepts a list of integers for the shape.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`List[Int]`) `[imm]`: Shape as a list of integers.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"

#### Overload 6

```mojo
def empty[cdtype: ComplexDType = ComplexDType.float64](shape: VariadicList[Int]) -> ComplexNDArray[cdtype]
```

Generate an empty ComplexNDArray from variadic integer arguments.

Overload of `empty` that accepts variadic integers for the shape.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`VariadicList[Int]`) `[imm]`: Shape as variadic integers.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `empty_like`

#### Overload 1

```mojo
def empty_like[dtype: DType = DType.float64](array: NDArray[dtype]) -> NDArray[dtype]
```

Generate an empty NDArray of the same shape as `array`.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: NDArray to be used as a reference for the shape.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def empty_like[cdtype: ComplexDType = ComplexDType.float64](array: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype]
```

Generate an empty ComplexNDArray of the same shape as `array`.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `array` (`ComplexNDArray[cdtype]`) `[imm]`: ComplexNDArray to be used as a reference for the shape.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `eye`

#### Overload 1

```mojo
def eye[dtype: DType = DType.float64](N: Int, M: Int) -> NDArray[dtype]
```

Return a 2-D NDArray with ones on the diagonal and zeros elsewhere.

Examples:
```mojo
import numojo as nm

var arr = nm.eye[nm.f64](3, 4)
# [[1, 0, 0, 0],
#  [0, 1, 0, 0],
#  [0, 0, 1, 0]]
```

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `N` (`Int`) `[imm]`: Number of rows in the matrix.
- `M` (`Int`) `[imm]`: Number of columns in the matrix.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def eye[cdtype: ComplexDType = ComplexDType.float64](N: Int, M: Int) -> ComplexNDArray[cdtype]
```

Return a 2-D ComplexNDArray with ones on the diagonal and zeros elsewhere.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `N` (`Int`) `[imm]`: Number of rows in the matrix.
- `M` (`Int`) `[imm]`: Number of columns in the matrix.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `identity`

#### Overload 1

```mojo
def identity[dtype: DType = DType.float64](N: Int) -> NDArray[dtype]
```

Generate an identity matrix of size N x N.

Examples:
```mojo
import numojo as nm

var I = nm.identity[nm.f64](3)
# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]
```

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `N` (`Int`) `[imm]`: Size of the square matrix.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def identity[cdtype: ComplexDType = ComplexDType.float64](N: Int) -> ComplexNDArray[cdtype]
```

Generate a complex identity matrix of size N x N.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `N` (`Int`) `[imm]`: Size of the square matrix.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `ones`

#### Overload 1

```mojo
def ones[dtype: DType = DType.float64](shape: NDArrayShape) -> NDArray[dtype]
```

Generate a NDArray filled with ones.

Examples:
```mojo
import numojo as nm

var arr = nm.ones[nm.f64](nm.Shape(2, 3))
# [[1, 1, 1],
#  [1, 1, 1]]
```

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: Shape of the NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def ones[dtype: DType = DType.float64](shape: List[Int]) -> NDArray[dtype]
```

Generate a NDArray filled with ones from a list of integers.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray.

**Args:**

- `shape` (`List[Int]`) `[imm]`: Shape as a list of integers.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def ones[dtype: DType = DType.float64](shape: VariadicList[Int]) -> NDArray[dtype]
```

Generate a NDArray filled with ones from variadic integer arguments.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray.

**Args:**

- `shape` (`VariadicList[Int]`) `[imm]`: Shape as variadic integers.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 4

```mojo
def ones[cdtype: ComplexDType = ComplexDType.float64](shape: NDArrayShape) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray filled with ones.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: Shape of the ComplexNDArray.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"

#### Overload 5

```mojo
def ones[cdtype: ComplexDType = ComplexDType.float64](shape: List[Int]) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray filled with ones from a list of integers.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`List[Int]`) `[imm]`: Shape as a list of integers.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"

#### Overload 6

```mojo
def ones[cdtype: ComplexDType = ComplexDType.float64](shape: VariadicList[Int]) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray filled with ones from variadic integer arguments.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`VariadicList[Int]`) `[imm]`: Shape as variadic integers.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `ones_like`

#### Overload 1

```mojo
def ones_like[dtype: DType = DType.float64](array: NDArray[dtype]) -> NDArray[dtype]
```

Generate a NDArray of the same shape as `a` filled with ones.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: NDArray to be used as a reference for the shape.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def ones_like[cdtype: ComplexDType = ComplexDType.float64](array: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray of the same shape as `array` filled with ones.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `array` (`ComplexNDArray[cdtype]`) `[imm]`: ComplexNDArray to be used as a reference for the shape.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `zeros`

#### Overload 1

```mojo
def zeros[dtype: DType = DType.float64](shape: NDArrayShape) -> NDArray[dtype]
```

Generate a NDArray filled with zeros.

Examples:
```mojo
import numojo as nm

var arr = nm.zeros[nm.f64](nm.Shape(2, 3))
# [[0, 0, 0],
#  [0, 0, 0]]
```

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: Shape of the NDArray.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def zeros[dtype: DType = DType.float64](shape: List[Int]) -> NDArray[dtype]
```

Generate a NDArray filled with zeros from a list of integers.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`List[Int]`) `[imm]`: Shape as a list of integers.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def zeros[dtype: DType = DType.float64](shape: VariadicList[Int]) -> NDArray[dtype]
```

Generate a NDArray filled with zeros from variadic integer arguments.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`VariadicList[Int]`) `[imm]`: Shape as variadic integers.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 4

```mojo
def zeros[cdtype: ComplexDType = ComplexDType.float64](shape: NDArrayShape) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray filled with zeros.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: Shape of the ComplexNDArray.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"

#### Overload 5

```mojo
def zeros[cdtype: ComplexDType = ComplexDType.float64](shape: List[Int]) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray filled with zeros from a list of integers.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`List[Int]`) `[imm]`: Shape as a list of integers.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"

#### Overload 6

```mojo
def zeros[cdtype: ComplexDType = ComplexDType.float64](shape: VariadicList[Int]) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray filled with zeros from variadic integer arguments.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`VariadicList[Int]`) `[imm]`: Shape as variadic integers.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `zeros_like`

#### Overload 1

```mojo
def zeros_like[dtype: DType = DType.float64](array: NDArray[dtype]) -> NDArray[dtype]
```

Generate a NDArray of the same shape as `array` filled with zeros.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: NDArray to be used as a reference for the shape.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def zeros_like[cdtype: ComplexDType = ComplexDType.float64](array: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray of the same shape as `array` filled with zeros.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `array` (`ComplexNDArray[cdtype]`) `[imm]`: ComplexNDArray to be used as a reference for the shape.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `full`

#### Overload 1

```mojo
def full[dtype: DType = DType.float64](shape: NDArrayShape, fill_value: Scalar[dtype], order: String = "C") -> NDArray[dtype]
```

Create a NDArray filled with a specified value.

Examples:
```mojo
import numojo as nm

var arr = nm.full[nm.f64](nm.Shape(2, 3), fill_value=7.0)
# [[7, 7, 7],
#  [7, 7, 7]]
```

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: Shape of the array.
- `fill_value` (`Scalar[dtype]`) `[imm]`: Value to fill all elements with.
- `order` (`String`) `[imm]`: Memory layout order ('C' for row-major or 'F' for column-major).

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def full[dtype: DType = DType.float64](shape: List[Int], fill_value: Scalar[dtype], order: String = "C") -> NDArray[dtype]
```

Create a NDArray filled with a specified value from a list of integers.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`List[Int]`) `[imm]`: Shape as a list of integers.
- `fill_value` (`Scalar[dtype]`) `[imm]`: Value to fill all elements with.
- `order` (`String`) `[imm]`: Memory layout order ('C' or 'F').

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def full[dtype: DType = DType.float64](shape: VariadicList[Int], fill_value: Scalar[dtype], order: String = "C") -> NDArray[dtype]
```

Create a NDArray filled with a specified value from variadic integer arguments.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`VariadicList[Int]`) `[imm]`: Shape as variadic integers.
- `fill_value` (`Scalar[dtype]`) `[imm]`: Value to fill all elements with.
- `order` (`String`) `[imm]`: Memory layout order ('C' or 'F').

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 4

```mojo
def full[cdtype: ComplexDType = ComplexDType.float64](shape: NDArrayShape, fill_value: ComplexSIMD[cdtype], order: String = "C") -> ComplexNDArray[cdtype]
```

Create a ComplexNDArray filled with a specified complex value.

Examples:
```mojo
import numojo as nm

var val = nm.CScalar[nm.cf64](3.0, 4.0)
var arr = nm.full[nm.cf64](nm.Shape(2, 2), fill_value=val)
```

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`NDArrayShape`) `[imm]`: Shape of the ComplexNDArray.
- `fill_value` (`ComplexSIMD[cdtype]`) `[imm]`: Complex value to fill all elements with.
- `order` (`String`) `[imm]`: Memory layout order ('C' for row-major or 'F' for column-major).

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"

#### Overload 5

```mojo
def full[cdtype: ComplexDType = ComplexDType.float64](shape: List[Int], fill_value: ComplexSIMD[cdtype], order: String = "C") -> ComplexNDArray[cdtype]
```

Create a ComplexNDArray filled with a specified value from a list of integers.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`List[Int]`) `[imm]`: Shape as a list of integers.
- `fill_value` (`ComplexSIMD[cdtype]`) `[imm]`: Complex value to fill all elements with.
- `order` (`String`) `[imm]`: Memory layout order ('C' or 'F').

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"

#### Overload 6

```mojo
def full[cdtype: ComplexDType = ComplexDType.float64](shape: VariadicList[Int], fill_value: ComplexSIMD[cdtype], order: String = "C") -> ComplexNDArray[cdtype]
```

Create a ComplexNDArray filled with a specified value from variadic integer arguments.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`VariadicList[Int]`) `[imm]`: Shape as variadic integers.
- `fill_value` (`ComplexSIMD[cdtype]`) `[imm]`: Complex value to fill all elements with.
- `order` (`String`) `[imm]`: Memory layout order ('C' or 'F').

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `full_like`

#### Overload 1

```mojo
def full_like[dtype: DType = DType.float64](array: NDArray[dtype], fill_value: Scalar[dtype], order: String = "C") -> NDArray[dtype]
```

Generate a NDArray of the same shape as `array` filled with `fill_value`.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `array` (`NDArray[dtype]`) `[imm]`: NDArray to be used as a reference for the shape.
- `fill_value` (`Scalar[dtype]`) `[imm]`: Value to fill the NDArray with.
- `order` (`String`) `[imm]`: Memory layout order ('C' or 'F').

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def full_like[cdtype: ComplexDType = ComplexDType.float64](array: ComplexNDArray[cdtype], fill_value: ComplexSIMD[cdtype], order: String = "C") -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray of the same shape as `array` filled with `fill_value`.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `array` (`ComplexNDArray[cdtype]`) `[imm]`: ComplexNDArray to be used as a reference for the shape.
- `fill_value` (`ComplexSIMD[cdtype]`) `[imm]`: Complex value to fill the ComplexNDArray with.
- `order` (`String`) `[imm]`: Memory layout order ('C' or 'F').

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `diag`

#### Overload 1

```mojo
def diag[dtype: DType = DType.float64](v: NDArray[dtype], k: Int = Int(0)) -> NDArray[dtype]
```

Extract a diagonal or construct a diagonal NDArray.

Examples:
```mojo
import numojo as nm

# Create diagonal matrix from 1-D array
var v = nm.arange[nm.f64](3.0)
var diag_mat = nm.diag[nm.f64](v)
# [[0, 0, 0],
#  [0, 1, 0],
#  [0, 0, 2]]

# Extract diagonal from 2-D array
var mat = nm.ones[nm.f64](nm.Shape(3, 3))
var d = nm.diag[nm.f64](mat)
# [1, 1, 1]
```

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `v` (`NDArray[dtype]`) `[imm]`: If 1-D, creates a 2-D array with v on the diagonal. If 2-D, extracts the diagonal.
- `k` (`Int`) `[imm]`: Diagonal offset (0 for main diagonal, positive for upper, negative for lower).

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def diag[cdtype: ComplexDType = ComplexDType.float64](v: ComplexNDArray[cdtype], k: Int = Int(0)) -> ComplexNDArray[cdtype]
```

Extract a diagonal or construct a diagonal ComplexNDArray.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `v` (`ComplexNDArray[cdtype]`) `[imm]`: If 1-D, creates a 2-D array with v on the diagonal. If 2-D, extracts the diagonal.
- `k` (`Int`) `[imm]`: Diagonal offset (0 for main diagonal, positive for upper, negative for lower).

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `diagflat`

#### Overload 1

```mojo
def diagflat[dtype: DType = DType.float64](v: NDArray[dtype], k: Int = Int(0)) -> NDArray[dtype]
```

Create a 2-D array with the flattened input as the diagonal.

Examples:
```mojo
import numojo as nm

var v = nm.arange[nm.f64](4.0).reshape(nm.Shape(2, 2))  # 2x2 array
var d = nm.diagflat[nm.f64](v)  # Flattens to [0,1,2,3] then creates diagonal
# [[0, 0, 0, 0],
#  [0, 1, 0, 0],
#  [0, 0, 2, 0],
#  [0, 0, 0, 3]]
```

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `v` (`NDArray[dtype]`) `[imm]`: NDArray to be flattened and used as the diagonal (any shape).
- `k` (`Int`) `[imm]`: Diagonal offset (0 for main diagonal, positive for upper, negative for lower).

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def diagflat[cdtype: ComplexDType = ComplexDType.float64](v: ComplexNDArray[cdtype], k: Int = Int(0)) -> ComplexNDArray[cdtype]
```

Create a 2-D complex array with the flattened input as the diagonal.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `v` (`ComplexNDArray[cdtype]`) `[imm]`: ComplexNDArray to be flattened and used as the diagonal (any shape).
- `k` (`Int`) `[imm]`: Diagonal offset (0 for main diagonal, positive for upper, negative for lower).

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `tri`

#### Overload 1

```mojo
def tri[dtype: DType = DType.float64](N: Int, M: Int, k: Int = Int(0)) -> NDArray[dtype]
```

Generate a lower triangular matrix.

Creates an array with ones on and below the k-th diagonal, zeros elsewhere.

Examples:
```mojo
import numojo as nm

# Lower triangular matrix
var L = nm.tri[nm.f64](3, 3)
# [[1, 0, 0],
#  [1, 1, 0],
#  [1, 1, 1]]

# With offset
var L2 = nm.tri[nm.f64](3, 3, k=1)
# [[1, 1, 0],
#  [1, 1, 1],
#  [1, 1, 1]]
```

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `N` (`Int`) `[imm]`: Number of rows in the matrix.
- `M` (`Int`) `[imm]`: Number of columns in the matrix.
- `k` (`Int`) `[imm]`: Diagonal offset (0 for main diagonal, positive shifts right, negative shifts left).

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def tri[cdtype: ComplexDType = ComplexDType.float64](N: Int, M: Int, k: Int = Int(0)) -> ComplexNDArray[cdtype]
```

Generate a lower triangular complex matrix.

Creates a complex array with ones on and below the k-th diagonal, zeros elsewhere.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `N` (`Int`) `[imm]`: Number of rows in the matrix.
- `M` (`Int`) `[imm]`: Number of columns in the matrix.
- `k` (`Int`) `[imm]`: Diagonal offset (0 for main diagonal, positive shifts right, negative shifts left).

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `tril`

#### Overload 1

```mojo
def tril[dtype: DType = DType.float64](m: NDArray[dtype], k: Int = Int(0)) -> NDArray[dtype]
```

Zero out elements above the k-th diagonal.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `m` (`NDArray[dtype]`) `[imm]`: NDArray to be zeroed out.
- `k` (`Int`) `[imm]`: Diagonal offset.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def tril[cdtype: ComplexDType = ComplexDType.float64](m: ComplexNDArray[cdtype], k: Int = Int(0)) -> ComplexNDArray[cdtype]
```

Zero out elements above the k-th diagonal.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `m` (`ComplexNDArray[cdtype]`) `[imm]`: ComplexNDArray to be zeroed out.
- `k` (`Int`) `[imm]`: Diagonal offset.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `triu`

#### Overload 1

```mojo
def triu[dtype: DType = DType.float64](m: NDArray[dtype], k: Int = Int(0)) -> NDArray[dtype]
```

Zero out elements below the k-th diagonal.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `m` (`NDArray[dtype]`) `[imm]`: NDArray to be zeroed out.
- `k` (`Int`) `[imm]`: Diagonal offset.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def triu[cdtype: ComplexDType = ComplexDType.float64](m: ComplexNDArray[cdtype], k: Int = Int(0)) -> ComplexNDArray[cdtype]
```

Zero out elements below the k-th diagonal.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `m` (`ComplexNDArray[cdtype]`) `[imm]`: ComplexNDArray to be zeroed out.
- `k` (`Int`) `[imm]`: Diagonal offset.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `vander`

#### Overload 1

```mojo
def vander[dtype: DType = DType.float64](x: NDArray[dtype], N: Optional[Int] = None, increasing: Bool = False) -> NDArray[dtype]
```

Generate a Vandermonde matrix.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `x` (`NDArray[dtype]`) `[imm]`: 1-D input array.
- `N` (`Optional[Int]`) `[imm]`: Number of columns in the output. If N is not specified, a square array is returned.
- `increasing` (`Bool`) `[imm]`: Order of the powers of the columns. If True, the powers increase from left to right, if False (the default) they are reversed.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def vander[cdtype: ComplexDType = ComplexDType.float64](x: ComplexNDArray[cdtype], N: Optional[Int] = None, increasing: Bool = False) -> ComplexNDArray[cdtype]
```

Generate a Complex Vandermonde matrix.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `x` (`ComplexNDArray[cdtype]`) `[imm]`: 1-D input array.
- `N` (`Optional[Int]`) `[imm]`: Number of columns in the output. If N is not specified, a square array is returned.
- `increasing` (`Bool`) `[imm]`: Order of the powers of the columns. If True, the powers increase from left to right, if False (the default) they are reversed.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `astype`

#### Overload 1

```mojo
def astype[dtype: DType, //, target: DType](a: NDArray[dtype]) -> NDArray[target]
```

Cast an NDArray to a different dtype.

**Parameters:**

- `dtype` (`DType`): Data type of the input array, always inferred.
- `target` (`DType`): Data type to cast the NDArray to.

**Args:**

- `a` (`NDArray[dtype]`) `[imm]`: NDArray to be casted.

**Returns:**

- `NDArray[target]`

!!! failure "Raises"

#### Overload 2

```mojo
def astype[cdtype: ComplexDType, //, target: ComplexDType](a: ComplexNDArray[cdtype]) -> ComplexNDArray[target]
```

Cast a ComplexNDArray to a different dtype.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the input array.
- `target` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `a` (`ComplexNDArray[cdtype]`) `[imm]`: ComplexNDArray to be casted.

**Returns:**

- `ComplexNDArray[target]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `fromstring`

```mojo
def fromstring[dtype: DType = DType.float64](text: String, order: String = "C") -> NDArray[dtype]
```

NDArray initialization from string representation of an ndarray. The shape can be inferred from the string representation. The literals will be casted to the dtype of the NDArray.

Note:
StringLiteral is also allowed as input as it is coerced to String type
before it is passed into the function.

Example:
```
import numojo as nm

def main() raises:
    var A = nm.fromstring[DType.int8]("[[[1,2],[3,4]],[[5,6],[7,8]]]")
    var B = nm.fromstring[DType.float16]("[[1,2,3,4],[5,6,7,8]]")
    var C = nm.fromstring[DType.float32]("[0.1, -2.3, 41.5, 19.29145, -199]")
    var D = nm.fromstring[DType.int32]("[0.1, -2.3, 41.5, 19.29145, -199]")

    print(A)
    print(B)
    print(C)
    print(D)
```

The output goes as follows. Note that the numbers are automatically
casted to the dtype of the NDArray.

```console
[[[     1       2       ]
 [     3       4       ]]
 [[     5       6       ]
 [     7       8       ]]]
3-D array  Shape: [2, 2, 2]  DType: int8

[[      1.0     2.0     3.0     4.0     ]
 [      5.0     6.0     7.0     8.0     ]]
2-D array  Shape: [2, 4]  DType: float16

[       0.10000000149011612     2.2999999523162842      41.5    19.291450500488281      199.0   ]
1-D array  Shape: [5]  DType: float32

[       0       2       41      19      199     ]
1-D array  Shape: [5]  DType: int32
```

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `text` (`String`) `[imm]`: String representation of an ndarray.
- `order` (`String`) `[imm]`: Memory order C or F.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `array`

#### Overload 1

```mojo
def array[dtype: DType = DType.float64](text: String, order: String = "C") -> NDArray[dtype]
```

This reload is an comptime of `fromstring`.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `text` (`String`) `[imm]`
- `order` (`String`) `[imm]`

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 2

```mojo
def array[dtype: DType = DType.float64](data: List[Scalar[dtype]], shape: List[Int], order: String = "C") -> NDArray[dtype]
```

Array creation with given data, shape and order.

Example:
```mojo
import numojo as nm
from numojo.prelude import *
var arr = nm.array[f16](data=[Scalar[f16](1), 2, 3, 4], shape=[2, 2])
```

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `data` (`List[Scalar[dtype]]`) `[imm]`: List of data.
- `shape` (`List[Int]`) `[imm]`: List of shape.
- `order` (`String`) `[imm]`: Memory order C or F.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 3

```mojo
def array[cdtype: ComplexDType = ComplexDType.float64](data: List[ComplexSIMD[cdtype]], shape: List[Int], order: String = "C") -> ComplexNDArray[cdtype]
```

Array creation with given data, shape and order.

Example:
```mojo
import numojo as nm
from numojo.prelude import *
var array = nm.array[cf64](
    data=[CScalar[cf64](1, 1),
    CScalar[cf64](2, 2),
    CScalar[cf64](3, 3),
    CScalar[cf64](4, 4)],
    shape=[2, 2],
)
```

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the ComplexNDArray elements.

**Args:**

- `data` (`List[ComplexSIMD[cdtype]]`) `[imm]`: List of complex data.
- `shape` (`List[Int]`) `[imm]`: List of shape.
- `order` (`String`) `[imm]`: Memory order C or F.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"

#### Overload 4

```mojo
def array[dtype: DType = DType.float64](data: PythonObject, order: String = "C") -> NDArray[dtype]
```

Array creation with given data, shape and order.

Example:
```mojo
import numojo as nm
from numojo.prelude import *
from python import Python
var np = Python.import_module("numpy")
var np_arr = np.array(Python.list(1, 2, 3, 4))
A = nm.array[f16](data=np_arr, order="C")
```

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `data` (`PythonObject`) `[imm]`: A Numpy array (PythonObject).
- `order` (`String`) `[imm]`: Memory order C or F.

**Returns:**

- `NDArray[dtype]`

!!! failure "Raises"

#### Overload 5

```mojo
def array[cdtype: ComplexDType = ComplexDType.float64](real: PythonObject, imag: PythonObject, order: String = "C") -> ComplexNDArray[cdtype]
```

Array creation with given real and imaginary data, shape and order.

Example:
```mojo
import numojo as nm
from numojo.prelude import *
from python import Python

var np = Python.import_module("numpy")
var np_arr = np.array(Python.list(1, 2, 3, 4))
A = nm.array[cf32](real=np_arr, imag=np_arr, order="C")
```

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the NDArray elements.

**Args:**

- `real` (`PythonObject`) `[imm]`: A Numpy array (PythonObject).
- `imag` (`PythonObject`) `[imm]`: A Numpy array (PythonObject).
- `order` (`String`) `[imm]`: Memory order C or F.

**Returns:**

- `ComplexNDArray[cdtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `meshgrid`

```mojo
def meshgrid[dtype: DType = DType.float64, indexing: String = "xy"](*arrays: NDArray[dtype]) -> List[NDArray[dtype]]
```

Generate coordinate matrices from coordinate vectors.

Examples:
```mojo
from numojo.routines.creation import meshgrid, arange
from numojo.prelude import *

var x = arange[f64](3.0)  # [0, 1, 2]
var y = arange[f64](2.0)  # [0, 1]
var grids = meshgrid[f64, indexing="xy"](x, y)
# grids[0]: [[0, 1, 2],
#            [0, 1, 2]]
# grids[1]: [[0, 0, 0],
#            [1, 1, 1]]
```

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.
- `indexing` (`String`): Cartesian ('xy', default) or matrix ('ij') indexing of output.

**Args:**

- `*arrays` (`NDArray[dtype]`) `[imm]`: 1-D input arrays representing the coordinates of a grid.

**Returns:**

- `List[NDArray[dtype]]`

!!! failure "Raises"


</div>
