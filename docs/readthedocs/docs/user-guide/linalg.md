# Linear Algebra in NuMojo

This guide covers practical linear algebra workflows in NuMojo using `Matrix` and `NDArray`.

## When to use `Matrix` vs `NDArray`

- Use `Matrix` when your data is always 2D and your workflow is matrix-focused.
- Use `NDArray` for general n-dimensional data, and switch to matrix operations when needed.

For purely linear-algebra-heavy code, `Matrix` is usually the clearest choice.

---

## Imports

```/dev/null/example.mojo#L1-3
import numojo as nm
from numojo import Matrix
from numojo.prelude import *
```

---

## 1) Matrix multiplication

Use the `@` operator for matrix multiplication.

```/dev/null/example.mojo#L1-11
import numojo as nm
from numojo import Matrix

fn main() raises:
    var A = Matrix.rand(shape=(3, 3))
    var B = Matrix.rand(shape=(3, 3))
    var C = A @ B

    print("A:")
    print(A)
    print("B:")
    print(B)
    print("C = A @ B:")
    print(C)
```

### Notes
- `A @ B` requires compatible shapes (`A.cols == B.rows`).
- For element-wise multiply, use routine APIs (for arrays) rather than `@`.

---

## 2) Solve linear systems (`Ax = b`)

Use `nm.solve(A, b)` to solve linear systems.

```/dev/null/example.mojo#L1-12
import numojo as nm
from numojo import Matrix

fn main() raises:
    var A = Matrix.rand(shape=(4, 4))
    var b = Matrix.rand(shape=(4, 1))

    var x = nm.solve(A, b)

    print("A:")
    print(A)
    print("b:")
    print(b)
    print("x (solution):")
    print(x)
```

### Notes
- `A` should be square and non-singular for a unique solution.
- If your system is ill-conditioned, use least-squares (`nm.lstsq`) as needed.

---

## 3) Matrix inverse

Use `A.inv()` for matrix inverse.

```/dev/null/example.mojo#L1-10
from numojo import Matrix

fn main() raises:
    var A = Matrix.rand(shape=(3, 3))
    var A_inv = A.inv()

    print("A:")
    print(A)
    print("A_inv:")
    print(A_inv)
    print("A @ A_inv:")
    print(A @ A_inv)
```

### Recommendation
Prefer solving systems (`solve`) over explicitly computing inverses when possible:
- Better numerical stability
- Usually better performance

---

## 4) Least squares

Use `nm.lstsq(A, b)` for overdetermined systems.

```/dev/null/example.mojo#L1-12
import numojo as nm
from numojo import Matrix

fn main() raises:
    var A = Matrix.rand(shape=(6, 3))   # more rows than columns
    var b = Matrix.rand(shape=(6, 1))

    var x = nm.lstsq(A, b)

    print("A shape:", A.shape)
    print("b shape:", b.shape)
    print("x (least-squares solution) shape:", x.shape)
    print(x)
```

---

## 5) Determinant and trace

Use the linear algebra routines for scalar matrix properties.

```/dev/null/example.mojo#L1-12
import numojo as nm
from numojo import Matrix

fn main() raises:
    var A = Matrix.rand(shape=(4, 4))

    var d = nm.det(A)
    var t = nm.trace(A)

    print("A:")
    print(A)
    print("det(A):", d)
    print("trace(A):", t)
```

---

## 6) Decompositions

NuMojo provides decomposition routines in the linalg namespace (availability can vary by version).

Common patterns include:
- LU decomposition
- QR decomposition
- Eigen-related routines

Check current exports in:
- `docs/features.md`
- `numojo/routines/linalg/__init__.mojo`

---

## 7) Working with `NDArray` in linalg flows

If your data starts as `NDArray`, keep tensor operations in `NDArray` and move into matrix workflows when shape semantics are clearly 2D.

```/dev/null/example.mojo#L1-13
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var x = nm.random.randn(Shape(3, 3))
    var y = nm.random.randn(Shape(3, 3))

    var z = x @ y
    print("x:")
    print(x)
    print("y:")
    print(y)
    print("z = x @ y:")
    print(z)
```

---

## 8) Common shape pitfalls

### Matrix multiplication mismatch
- Invalid: `(m, n) @ (p, q)` when `n != p`

### Solve mismatch
- `solve(A, b)` expects `A` as square `(n, n)`
- `b` should align in leading dimension (`n`, or `(n, k)`)

### Axis assumptions
- Most matrix-specific operations assume 2D semantics.

---

## 9) Numerical stability tips

- Prefer `solve(A, b)` over `inv(A) @ b`.
- Prefer least squares for inconsistent/overdetermined systems.
- Be cautious with near-singular matrices from random generation.
- Validate residuals when needed:
  - compute `r = A @ x - b`
  - inspect norm-like aggregate metrics (`sum(abs(r))`, etc.) if available.

---

## 10) Quick recipe reference

- Multiply matrices: `A @ B`
- Inverse: `A.inv()`
- Solve system: `nm.solve(A, b)`
- Least squares: `nm.lstsq(A, b)`
- Determinant: `nm.det(A)`
- Trace: `nm.trace(A)`

---

## Next steps

- For array basics: `docs/user-guide/ndarray-creation-manipulation.md`
- For indexing and slicing: `docs/user-guide/indexing.md`
- For install/setup: `docs/getting-started/installation.md`
- For design internals: `docs/developer-guide/architecture.md`
