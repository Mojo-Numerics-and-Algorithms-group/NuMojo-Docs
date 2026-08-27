# Quickstart

This guide gets a first NuMojo program running in a couple of minutes. See [Installation](install.md) for all the ways to add NuMojo to a project.

Runnable examples are available in `examples/` (e.g., `examples/quickstart.mojo`).

An example of n-dimensional array (`NDArray` type) goes as follows.

```mojo
import numojo as nm
from numojo.prelude import *


def main() raises:
    # Generate two 1000x1000 matrices with random float64 values
    var A = nm.random.randn(Shape(1000, 1000)) # Shape is used for all shape related operations in numojo. 
    var B = nm.random.randn(Shape(1000, 1000))

    # Generate a 3x2 matrix from string representation
    var X = nm.fromstring[f32]("[[1.1, -0.32, 1], [0.1, -3, 2.124]]")

    # Print array
    print(A)

    # Array multiplication
    var C = A @ B

    # Array inversion
    var I = nm.inv(A)

    # Array slicing
    var A_slice = A[1:3, 4:19]

    # Get scalar from array
    var A_item = A[Item(291, 141)] # Item() is used to define coordinates of an ndarray in numojo. 
    var A_item_2 = A.item(291, 141)

    # Sort and argsort along axis
    print(nm.sort(A, axis=1))
    print(nm.argsort(A, axis=0))

    # Sum along axis
    print(nm.sum(A))
    print(nm.sum(A, axis=1))

    # Solve a linear system
    print(nm.solve(A, B))
```

An example of `ComplexNDArray` is as follows:

```mojo
import numojo as nm
from numojo.prelude import *


def main() raises:
    # Create a complex scalar 5 + 5j
    # cf32 is the complex version of f32 (DType.float32) used to identify complex types in numojo.
    var complexscalar = CScalar[cf32](5) # Equivalently ComplexSIMD[cf32](5, 5)
    # Also can be define as simple as  5 + 5*`1j`!
  
    # Create complex arrays
    var A = nm.full[cf32](Shape(1000, 1000), fill_value=complexscalar)  # filled with (5+5j)
    var B = nm.ones[cf32](Shape(1000, 1000))                            # filled with (1+1j)

    # Print array
    print(A)

    # Array slicing
    var A_slice = A[1:3, 4:19]

    # Array multiplication
    var C = A * B

    # Get scalar from array
    var A_item = A[Item(291, 141)]
    # Set an element of the array
    A[item(291, 141)] = complexscalar
```

## Next steps

- Browse available functions by topic in the [User Guide](../user-guide/overview.md).
- Look up any function's full signature and docstring in the [API Reference](../API reference/numojo/index.md).
