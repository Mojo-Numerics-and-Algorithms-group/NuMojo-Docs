# `numojo.routines.creation`

Creation routines (numojo.routines.creation)

Use more uniformed way of calling functions, i.e., using one specific
overload for each function. This makes maintenance easier. Example:

- `NDArray.__init__` takes in `ShapeLike` and initialize an `NDArray` container.
- `full` calls `NDArray.__init__`.
- `zeros`, `ones` calls `full`.
- Other functions calls `zeros`, `ones`, `full`.

If overloads are needed, it is better to call the default signature in other overloads. Example: `zeros(shape: NDArrayShape)`. All other overloads call this function. So it is easy for modification.

## Functions


<div class="fn-card" markdown="1">

### `arange`

#### Overload 1

```mojo
arange[dtype: DType = DType.float64](start: Scalar[dtype], stop: Scalar[dtype], step: Scalar[dtype] = 1) -> NDArray[dtype]
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

- `start` (`Scalar`): Start value (inclusive).
- `stop` (`Scalar`): End value (exclusive).
- `step` (`Scalar`): Step size between consecutive elements (default 1).

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
arange[dtype: DType = DType.float64](stop: Scalar[dtype]) -> NDArray[dtype]
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

- `stop` (`Scalar`): End value (exclusive).

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
arange[cdtype: ComplexDType = ComplexDType.float64](start: ComplexSIMD[cdtype], stop: ComplexSIMD[cdtype], step: ComplexSIMD[cdtype] = ComplexSIMD(1, 1)) -> ComplexNDArray[cdtype]
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

- `start` (`ComplexSIMD`): Start value (inclusive).
- `stop` (`ComplexSIMD`): End value (exclusive).
- `step` (`ComplexSIMD`): Step size between consecutive elements (default 1+1j).

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"

#### Overload 4

```mojo
arange[cdtype: ComplexDType = ComplexDType.float64](stop: ComplexSIMD[cdtype]) -> ComplexNDArray[cdtype]
```

Generate evenly spaced complex values from 0 to stop.

Overload with start=0+0j and step=1+1j for convenience.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `stop` (`ComplexSIMD`): End value (exclusive).

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `linspace`

#### Overload 1

```mojo
linspace[dtype: DType = DType.float64, parallel: Bool = False](start: Scalar[dtype], stop: Scalar[dtype], num: Int = 50, endpoint: Bool = True) -> NDArray[dtype] where dtype.is_floating_point()
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

- `start` (`Scalar`): Starting value of the sequence.
- `stop` (`Scalar`): End value of the sequence.
- `num` (`Int`): Number of samples to generate (default 50).
- `endpoint` (`Bool`): Whether to include `stop` in the result (default True).

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
linspace[cdtype: ComplexDType = ComplexDType.float64, parallel: Bool = False](start: ComplexSIMD[cdtype], stop: ComplexSIMD[cdtype], num: Int = 50, endpoint: Bool = True) -> ComplexNDArray[cdtype]
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

- `start` (`ComplexSIMD`): Starting complex value of the sequence.
- `stop` (`ComplexSIMD`): End complex value of the sequence.
- `num` (`Int`): Number of samples to generate (default 50).
- `endpoint` (`Bool`): Whether to include `stop` in the result (default True).

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `logspace`

#### Overload 1

```mojo
logspace[dtype: DType = DType.float64, parallel: Bool = False](start: Scalar[dtype], stop: Scalar[dtype], num: Int, endpoint: Bool = True, base: Scalar[dtype] = 10) -> NDArray[dtype] where dtype.is_floating_point()
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

- `start` (`Scalar`): Base^start is the starting value of the sequence.
- `stop` (`Scalar`): Base^stop is the final value of the sequence.
- `num` (`Int`): Number of samples to generate.
- `endpoint` (`Bool`): Whether to include base^stop in the result (default True).
- `base` (`Scalar`): The base of the logarithm (default 10.0).

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
logspace[cdtype: ComplexDType = ComplexDType.float64, parallel: Bool = False](start: ComplexSIMD[cdtype], stop: ComplexSIMD[cdtype], num: Int, endpoint: Bool = True, base: ComplexSIMD[cdtype] = ComplexSIMD(10, 10)) -> ComplexNDArray[cdtype] where cdtype.is_floating_point()
```

Generate logarithmically spaced complex numbers over a specified interval.

The sequence starts at base^start and ends at base^stop.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array (must be floating-point).
- `parallel` (`Bool`): Whether to use parallelization for computation (default False).

**Args:**

- `start` (`ComplexSIMD`): Base^start is the starting complex value of the sequence.
- `stop` (`ComplexSIMD`): Base^stop is the final complex value of the sequence.
- `num` (`Int`): Number of samples to generate.
- `endpoint` (`Bool`): Whether to include base^stop in the result (default True).
- `base` (`ComplexSIMD`): The complex base of the logarithm (default 10+10j).

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `geomspace`

#### Overload 1

```mojo
geomspace[dtype: DType = DType.float64](start: Scalar[dtype], stop: Scalar[dtype], num: Int, endpoint: Bool = True) -> NDArray[dtype] where dtype.is_floating_point()
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

- `start` (`Scalar`): The starting value of the sequence.
- `stop` (`Scalar`): The final value of the sequence.
- `num` (`Int`): Number of samples to generate.
- `endpoint` (`Bool`): Whether to include `stop` in the result (default True).

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
geomspace[cdtype: ComplexDType = ComplexDType.float64](start: ComplexSIMD[cdtype], stop: ComplexSIMD[cdtype], num: Int, endpoint: Bool = True) -> ComplexNDArray[cdtype] where cdtype.is_floating_point()
```

Generate complex numbers spaced evenly on a log scale (geometric progression).

Notes:
This is similar to logspace, but with endpoints specified directly.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array (must be floating-point).

**Args:**

- `start` (`ComplexSIMD`): The starting complex value of the sequence.
- `stop` (`ComplexSIMD`): The final complex value of the sequence.
- `num` (`Int`): Number of samples to generate.
- `endpoint` (`Bool`): Whether to include `stop` in the result (default True).

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `empty`

#### Overload 1

```mojo
empty[dtype: DType = DType.float64](shape: NDArrayShape) -> NDArray[dtype]
```

Generate an empty NDArray of given shape with arbitrary values.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`NDArrayShape`): Shape of the NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
empty[dtype: DType = DType.float64](shape: List[Int]) -> NDArray[dtype]
```

Generate an empty NDArray from a list of integers.

Overload of `empty` that accepts a list of integers for the shape.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`List`): Shape as a list of integers.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
empty[dtype: DType = DType.float64](shape: VariadicList[Int]) -> NDArray[dtype]
```

Generate an empty NDArray from variadic integer arguments.

Overload of `empty` that accepts variadic integers for the shape.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`VariadicList`): Shape as variadic integers.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 4

```mojo
empty[cdtype: ComplexDType = ComplexDType.float64](shape: NDArrayShape) -> ComplexNDArray[cdtype]
```

Generate an empty ComplexNDArray of given shape with arbitrary values.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`NDArrayShape`): Shape of the ComplexNDArray.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"

#### Overload 5

```mojo
empty[cdtype: ComplexDType = ComplexDType.float64](shape: List[Int]) -> ComplexNDArray[cdtype]
```

Generate an empty ComplexNDArray from a list of integers.

Overload of `empty` that accepts a list of integers for the shape.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`List`): Shape as a list of integers.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"

#### Overload 6

```mojo
empty[cdtype: ComplexDType = ComplexDType.float64](shape: VariadicList[Int]) -> ComplexNDArray[cdtype]
```

Generate an empty ComplexNDArray from variadic integer arguments.

Overload of `empty` that accepts variadic integers for the shape.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`VariadicList`): Shape as variadic integers.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `empty_like`

#### Overload 1

```mojo
empty_like[dtype: DType = DType.float64](array: NDArray[dtype]) -> NDArray[dtype]
```

Generate an empty NDArray of the same shape as `array`.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `array` (`NDArray`): NDArray to be used as a reference for the shape.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
empty_like[cdtype: ComplexDType = ComplexDType.float64](array: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype]
```

Generate an empty ComplexNDArray of the same shape as `array`.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `array` (`ComplexNDArray`): ComplexNDArray to be used as a reference for the shape.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `eye`

#### Overload 1

```mojo
eye[dtype: DType = DType.float64](N: Int, M: Int) -> NDArray[dtype]
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

- `N` (`Int`): Number of rows in the matrix.
- `M` (`Int`): Number of columns in the matrix.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
eye[cdtype: ComplexDType = ComplexDType.float64](N: Int, M: Int) -> ComplexNDArray[cdtype]
```

Return a 2-D ComplexNDArray with ones on the diagonal and zeros elsewhere.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `N` (`Int`): Number of rows in the matrix.
- `M` (`Int`): Number of columns in the matrix.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `identity`

#### Overload 1

```mojo
identity[dtype: DType = DType.float64](N: Int) -> NDArray[dtype]
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

- `N` (`Int`): Size of the square matrix.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
identity[cdtype: ComplexDType = ComplexDType.float64](N: Int) -> ComplexNDArray[cdtype]
```

Generate a complex identity matrix of size N x N.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `N` (`Int`): Size of the square matrix.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `ones`

#### Overload 1

```mojo
ones[dtype: DType = DType.float64](shape: NDArrayShape) -> NDArray[dtype]
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

- `shape` (`NDArrayShape`): Shape of the NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
ones[dtype: DType = DType.float64](shape: List[Int]) -> NDArray[dtype]
```

Generate a NDArray filled with ones from a list of integers.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray.

**Args:**

- `shape` (`List`): Shape as a list of integers.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
ones[dtype: DType = DType.float64](shape: VariadicList[Int]) -> NDArray[dtype]
```

Generate a NDArray filled with ones from variadic integer arguments.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray.

**Args:**

- `shape` (`VariadicList`): Shape as variadic integers.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 4

```mojo
ones[cdtype: ComplexDType = ComplexDType.float64](shape: NDArrayShape) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray filled with ones.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`NDArrayShape`): Shape of the ComplexNDArray.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"

#### Overload 5

```mojo
ones[cdtype: ComplexDType = ComplexDType.float64](shape: List[Int]) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray filled with ones from a list of integers.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`List`): Shape as a list of integers.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"

#### Overload 6

```mojo
ones[cdtype: ComplexDType = ComplexDType.float64](shape: VariadicList[Int]) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray filled with ones from variadic integer arguments.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`VariadicList`): Shape as variadic integers.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `ones_like`

#### Overload 1

```mojo
ones_like[dtype: DType = DType.float64](array: NDArray[dtype]) -> NDArray[dtype]
```

Generate a NDArray of the same shape as `a` filled with ones.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray.

**Args:**

- `array` (`NDArray`): NDArray to be used as a reference for the shape.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
ones_like[cdtype: ComplexDType = ComplexDType.float64](array: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray of the same shape as `array` filled with ones.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `array` (`ComplexNDArray`): ComplexNDArray to be used as a reference for the shape.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `zeros`

#### Overload 1

```mojo
zeros[dtype: DType = DType.float64](shape: NDArrayShape) -> NDArray[dtype]
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

- `shape` (`NDArrayShape`): Shape of the NDArray.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
zeros[dtype: DType = DType.float64](shape: List[Int]) -> NDArray[dtype]
```

Generate a NDArray filled with zeros from a list of integers.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`List`): Shape as a list of integers.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
zeros[dtype: DType = DType.float64](shape: VariadicList[Int]) -> NDArray[dtype]
```

Generate a NDArray filled with zeros from variadic integer arguments.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`VariadicList`): Shape as variadic integers.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 4

```mojo
zeros[cdtype: ComplexDType = ComplexDType.float64](shape: NDArrayShape) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray filled with zeros.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`NDArrayShape`): Shape of the ComplexNDArray.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"

#### Overload 5

```mojo
zeros[cdtype: ComplexDType = ComplexDType.float64](shape: List[Int]) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray filled with zeros from a list of integers.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`List`): Shape as a list of integers.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"

#### Overload 6

```mojo
zeros[cdtype: ComplexDType = ComplexDType.float64](shape: VariadicList[Int]) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray filled with zeros from variadic integer arguments.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`VariadicList`): Shape as variadic integers.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `zeros_like`

#### Overload 1

```mojo
zeros_like[dtype: DType = DType.float64](array: NDArray[dtype]) -> NDArray[dtype]
```

Generate a NDArray of the same shape as `array` filled with zeros.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `array` (`NDArray`): NDArray to be used as a reference for the shape.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
zeros_like[cdtype: ComplexDType = ComplexDType.float64](array: ComplexNDArray[cdtype]) -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray of the same shape as `array` filled with zeros.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `array` (`ComplexNDArray`): ComplexNDArray to be used as a reference for the shape.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `full`

#### Overload 1

```mojo
full[dtype: DType = DType.float64](shape: NDArrayShape, fill_value: Scalar[dtype], order: String = "C") -> NDArray[dtype]
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

- `shape` (`NDArrayShape`): Shape of the array.
- `fill_value` (`Scalar`): Value to fill all elements with.
- `order` (`String`): Memory layout order ('C' for row-major or 'F' for column-major).

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
full[dtype: DType = DType.float64](shape: List[Int], fill_value: Scalar[dtype], order: String = "C") -> NDArray[dtype]
```

Create a NDArray filled with a specified value from a list of integers.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`List`): Shape as a list of integers.
- `fill_value` (`Scalar`): Value to fill all elements with.
- `order` (`String`): Memory layout order ('C' or 'F').

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
full[dtype: DType = DType.float64](shape: VariadicList[Int], fill_value: Scalar[dtype], order: String = "C") -> NDArray[dtype]
```

Create a NDArray filled with a specified value from variadic integer arguments.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `shape` (`VariadicList`): Shape as variadic integers.
- `fill_value` (`Scalar`): Value to fill all elements with.
- `order` (`String`): Memory layout order ('C' or 'F').

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 4

```mojo
full[cdtype: ComplexDType = ComplexDType.float64](shape: NDArrayShape, fill_value: ComplexSIMD[cdtype], order: String = "C") -> ComplexNDArray[cdtype]
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

- `shape` (`NDArrayShape`): Shape of the ComplexNDArray.
- `fill_value` (`ComplexSIMD`): Complex value to fill all elements with.
- `order` (`String`): Memory layout order ('C' for row-major or 'F' for column-major).

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"

#### Overload 5

```mojo
full[cdtype: ComplexDType = ComplexDType.float64](shape: List[Int], fill_value: ComplexSIMD[cdtype], order: String = "C") -> ComplexNDArray[cdtype]
```

Create a ComplexNDArray filled with a specified value from a list of integers.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`List`): Shape as a list of integers.
- `fill_value` (`ComplexSIMD`): Complex value to fill all elements with.
- `order` (`String`): Memory layout order ('C' or 'F').

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"

#### Overload 6

```mojo
full[cdtype: ComplexDType = ComplexDType.float64](shape: VariadicList[Int], fill_value: ComplexSIMD[cdtype], order: String = "C") -> ComplexNDArray[cdtype]
```

Create a ComplexNDArray filled with a specified value from variadic integer arguments.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `shape` (`VariadicList`): Shape as variadic integers.
- `fill_value` (`ComplexSIMD`): Complex value to fill all elements with.
- `order` (`String`): Memory layout order ('C' or 'F').

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `full_like`

#### Overload 1

```mojo
full_like[dtype: DType = DType.float64](array: NDArray[dtype], fill_value: Scalar[dtype], order: String = "C") -> NDArray[dtype]
```

Generate a NDArray of the same shape as `array` filled with `fill_value`.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `array` (`NDArray`): NDArray to be used as a reference for the shape.
- `fill_value` (`Scalar`): Value to fill the NDArray with.
- `order` (`String`): Memory layout order ('C' or 'F').

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
full_like[cdtype: ComplexDType = ComplexDType.float64](array: ComplexNDArray[cdtype], fill_value: ComplexSIMD[cdtype], order: String = "C") -> ComplexNDArray[cdtype]
```

Generate a ComplexNDArray of the same shape as `array` filled with `fill_value`.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `array` (`ComplexNDArray`): ComplexNDArray to be used as a reference for the shape.
- `fill_value` (`ComplexSIMD`): Complex value to fill the ComplexNDArray with.
- `order` (`String`): Memory layout order ('C' or 'F').

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `diag`

#### Overload 1

```mojo
diag[dtype: DType = DType.float64](v: NDArray[dtype], k: Int = 0) -> NDArray[dtype]
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

- `v` (`NDArray`): If 1-D, creates a 2-D array with v on the diagonal. If 2-D, extracts the diagonal.
- `k` (`Int`): Diagonal offset (0 for main diagonal, positive for upper, negative for lower).

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
diag[cdtype: ComplexDType = ComplexDType.float64](v: ComplexNDArray[cdtype], k: Int = 0) -> ComplexNDArray[cdtype]
```

Extract a diagonal or construct a diagonal ComplexNDArray.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `v` (`ComplexNDArray`): If 1-D, creates a 2-D array with v on the diagonal. If 2-D, extracts the diagonal.
- `k` (`Int`): Diagonal offset (0 for main diagonal, positive for upper, negative for lower).

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `diagflat`

#### Overload 1

```mojo
diagflat[dtype: DType = DType.float64](v: NDArray[dtype], k: Int = 0) -> NDArray[dtype]
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

- `v` (`NDArray`): NDArray to be flattened and used as the diagonal (any shape).
- `k` (`Int`): Diagonal offset (0 for main diagonal, positive for upper, negative for lower).

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
diagflat[cdtype: ComplexDType = ComplexDType.float64](v: ComplexNDArray[cdtype], k: Int = 0) -> ComplexNDArray[cdtype]
```

Create a 2-D complex array with the flattened input as the diagonal.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `v` (`ComplexNDArray`): ComplexNDArray to be flattened and used as the diagonal (any shape).
- `k` (`Int`): Diagonal offset (0 for main diagonal, positive for upper, negative for lower).

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `tri`

#### Overload 1

```mojo
tri[dtype: DType = DType.float64](N: Int, M: Int, k: Int = 0) -> NDArray[dtype]
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

- `N` (`Int`): Number of rows in the matrix.
- `M` (`Int`): Number of columns in the matrix.
- `k` (`Int`): Diagonal offset (0 for main diagonal, positive shifts right, negative shifts left).

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
tri[cdtype: ComplexDType = ComplexDType.float64](N: Int, M: Int, k: Int = 0) -> ComplexNDArray[cdtype]
```

Generate a lower triangular complex matrix.

Creates a complex array with ones on and below the k-th diagonal, zeros elsewhere.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `N` (`Int`): Number of rows in the matrix.
- `M` (`Int`): Number of columns in the matrix.
- `k` (`Int`): Diagonal offset (0 for main diagonal, positive shifts right, negative shifts left).

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `tril`

#### Overload 1

```mojo
tril[dtype: DType = DType.float64](m: NDArray[dtype], k: Int = 0) -> NDArray[dtype]
```

Zero out elements above the k-th diagonal.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `m` (`NDArray`): NDArray to be zeroed out.
- `k` (`Int`): Diagonal offset.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
tril[cdtype: ComplexDType = ComplexDType.float64](m: ComplexNDArray[cdtype], k: Int = 0) -> ComplexNDArray[cdtype]
```

Zero out elements above the k-th diagonal.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `m` (`ComplexNDArray`): ComplexNDArray to be zeroed out.
- `k` (`Int`): Diagonal offset.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `triu`

#### Overload 1

```mojo
triu[dtype: DType = DType.float64](m: NDArray[dtype], k: Int = 0) -> NDArray[dtype]
```

Zero out elements below the k-th diagonal.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `m` (`NDArray`): NDArray to be zeroed out.
- `k` (`Int`): Diagonal offset.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
triu[cdtype: ComplexDType = ComplexDType.float64](m: ComplexNDArray[cdtype], k: Int = 0) -> ComplexNDArray[cdtype]
```

Zero out elements below the k-th diagonal.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `m` (`ComplexNDArray`): ComplexNDArray to be zeroed out.
- `k` (`Int`): Diagonal offset.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `vander`

#### Overload 1

```mojo
vander[dtype: DType = DType.float64](x: NDArray[dtype], N: Optional[Int] = None, increasing: Bool = False) -> NDArray[dtype]
```

Generate a Vandermonde matrix.

**Parameters:**

- `dtype` (`DType`): Datatype of the NDArray elements.

**Args:**

- `x` (`NDArray`): 1-D input array.
- `N` (`Optional`): Number of columns in the output. If N is not specified, a square array is returned.
- `increasing` (`Bool`): Order of the powers of the columns. If True, the powers increase from left to right, if False (the default) they are reversed.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
vander[cdtype: ComplexDType = ComplexDType.float64](x: ComplexNDArray[cdtype], N: Optional[Int] = None, increasing: Bool = False) -> ComplexNDArray[cdtype]
```

Generate a Complex Vandermonde matrix.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `x` (`ComplexNDArray`): 1-D input array.
- `N` (`Optional`): Number of columns in the output. If N is not specified, a square array is returned.
- `increasing` (`Bool`): Order of the powers of the columns. If True, the powers increase from left to right, if False (the default) they are reversed.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `astype`

#### Overload 1

```mojo
astype[dtype: DType, //, target: DType](a: NDArray[dtype]) -> NDArray[target]
```

Cast an NDArray to a different dtype.

**Parameters:**

- `dtype` (`DType`): Data type of the input array, always inferred.
- `target` (`DType`): Data type to cast the NDArray to.

**Args:**

- `a` (`NDArray`): NDArray to be casted.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
astype[cdtype: ComplexDType, //, target: ComplexDType](a: ComplexNDArray[cdtype]) -> ComplexNDArray[target]
```

Cast a ComplexNDArray to a different dtype.

**Parameters:**

- `cdtype` (`ComplexDType`): Complex datatype of the input array.
- `target` (`ComplexDType`): Complex datatype of the output array.

**Args:**

- `a` (`ComplexNDArray`): ComplexNDArray to be casted.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `fromstring`

```mojo
fromstring[dtype: DType = DType.float64](text: String, order: String = "C") -> NDArray[dtype]
```

NDArray initialization from string representation of an ndarray. The shape can be inferred from the string representation. The literals will be casted to the dtype of the NDArray.

Note:
StringLiteral is also allowed as input as it is coerced to String type
before it is passed into the function.

Example:
```
import numojo as nm

fn main() raises:
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

- `text` (`String`): String representation of an ndarray.
- `order` (`String`): Memory order C or F.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `array`

#### Overload 1

```mojo
array[dtype: DType = DType.float64](text: String, order: String = "C") -> NDArray[dtype]
```

This reload is an comptime of `fromstring`.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `text` (`String`)
- `order` (`String`)

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 2

```mojo
array[dtype: DType = DType.float64](data: List[Scalar[dtype]], shape: List[Int], order: String = "C") -> NDArray[dtype]
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

- `data` (`List`): List of data.
- `shape` (`List`): List of shape.
- `order` (`String`): Memory order C or F.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 3

```mojo
array[cdtype: ComplexDType = ComplexDType.float64](data: List[ComplexSIMD[cdtype]], shape: List[Int], order: String = "C") -> ComplexNDArray[cdtype]
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

- `data` (`List`): List of complex data.
- `shape` (`List`): List of shape.
- `order` (`String`): Memory order C or F.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"

#### Overload 4

```mojo
array[dtype: DType = DType.float64](data: PythonObject, order: String = "C") -> NDArray[dtype]
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

- `data` (`PythonObject`): A Numpy array (PythonObject).
- `order` (`String`): Memory order C or F.

**Returns:**

- `NDArray`

!!! failure "Raises"

#### Overload 5

```mojo
array[cdtype: ComplexDType = ComplexDType.float64](real: PythonObject, imag: PythonObject, order: String = "C") -> ComplexNDArray[cdtype]
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

- `real` (`PythonObject`): A Numpy array (PythonObject).
- `imag` (`PythonObject`): A Numpy array (PythonObject).
- `order` (`String`): Memory order C or F.

**Returns:**

- `ComplexNDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `meshgrid`

```mojo
meshgrid[dtype: DType = DType.float64, indexing: String = "xy"](*arrays: NDArray[dtype]) -> List[NDArray[dtype]]
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

- `*arrays` (`NDArray`): 1-D input arrays representing the coordinates of a grid.

**Returns:**

- `List`

!!! failure "Raises"


</div>
