# Testing Guide for Developers

This guide explains how testing works in NuMojo and how to add/maintain tests with consistent quality.

## Goals

NuMojo tests should:

- validate numerical correctness against trusted references (primarily NumPy),
- catch regressions quickly,
- be easy for new contributors to run and extend,
- keep behavior consistent across modules (`core`, `routines`, `science`).

---

## Test layout

Current test structure:

- `tests/core/*` — core containers, indexing, shape/stride behavior, matrix/core semantics
- `tests/routines/*` — user-facing functional routines (math, linalg, io, sorting, etc.)
- `tests/science/*` — higher-level scientific modules
- `tests/utils_for_test.mojo` — helper assertions and NumPy comparison utilities

Keep new tests in the correct bucket. If a test spans layers, place it where the user-facing behavior is asserted.

---

## Running tests locally

From repo root:

```/dev/null/terminal.sh#L1-4
pixi run test
pixi run test_core
pixi run test_routines
pixi run test_science
```

Run one file directly:

```/dev/null/terminal.sh#L1-1
pixi run mojo run -I tests/ tests/routines/test_math.mojo
```

Or use the helper task:

```/dev/null/terminal.sh#L1-1
pixi run run-test TEST_FILE=tests/routines/test_math.mojo
```

Before opening a PR, run:

```/dev/null/terminal.sh#L1-1
pixi run final
```

`final` runs formatting and full tests.

---

## Test entrypoint pattern

Every test file should expose test functions and have the standard discovery runner:

```/dev/null/example_test_file.mojo#L1-8
from testing.testing import TestSuite

def test_example():
    pass

def main():
    TestSuite.discover_tests[__functions_in_module()]().run()
```

Use `def test_*` naming so discovery picks tests automatically.

---

## Assertion strategy

Use explicit assertions with clear failure messages. Prefer one conceptual assertion per check block.

### Numerical array checks

Use helpers from `tests/utils_for_test.mojo`:

- `check(...)` for exact equality against NumPy
- `check_with_dtype(...)` for values + dtype agreement
- `check_is_close(...)` for approximate float checks
- `check_values_close(...)` for scalar tolerance checks

Example pattern:

```/dev/null/example_check.mojo#L1-14
from python import Python
import numojo as nm
from utils_for_test import check_is_close

def test_sin_basic() raises:
    var np = Python.import_module("numpy")
    var a = nm.linspace[f32](0, 3.14159, 20)
    var got = nm.sin(a)
    var exp = np.sin(a.to_numpy())

    check_is_close(got, exp, "sin should match numpy within tolerance")
```

---

## What to test for every new function

When adding a new API function, include tests for:

1. **Happy path**
   - standard shape(s)
   - common dtype(s)
2. **Edge cases**
   - small sizes (`0`, `1`)
   - degenerate shape when meaningful
   - negative axis handling where applicable
3. **Error behavior**
   - invalid shapes
   - out-of-bounds axis
   - unsupported dtype
4. **Layout sensitivity**
   - contiguous and non-contiguous/view-like paths where relevant
5. **Parity**
   - compare behavior against NumPy equivalent (or clearly documented intentional deviation)

---

## Error tests

For invalid inputs, assert that errors are raised and messages are meaningful.

```/dev/null/example_error_test.mojo#L1-12
from testing import assert_raises
import numojo as nm
from numojo.prelude import *

def test_sum_invalid_axis_raises():
    var a = nm.arange[f32](6).reshape(Shape(2, 3))
    assert_raises[Error](
        fn() raises:
            _ = nm.sum(a, axis=10)
    )
```

If exact message matching is brittle, at least assert the error type and key context.

---

## Tolerance guidance

Use strict tolerances where possible:

- `f64`: tighter (`1e-8` to `1e-12` depending on op)
- `f32`: moderate (`1e-4` to `1e-6`)
- complex/math-heavy transforms: choose practical tolerance and document why

Avoid very loose tolerances unless truly necessary. If a loose tolerance is required, add a short rationale in the test message.

---

## Determinism guidance

For random-based tests:

- prefer fixed inputs over random where possible,
- if randomness is needed, use deterministic generation patterns or compare invariant properties,
- avoid flaky tests caused by unstable random assumptions.

---

## Performance-sensitive tests

Unit tests should prioritize correctness, not microbenchmarking.

For performance checks:

- keep benchmark-style code in `benchmark/`,
- avoid strict timing assertions in CI tests,
- if needed, test algorithmic behavior (e.g., output shape, monotonicity, complexity-safe constraints) rather than elapsed time.

---

## CI expectations

CI runs tests by category and expects:

- formatting clean,
- all test scripts pass,
- no dependency on local-only files/paths.

Before opening a PR:

1. `pixi run format`
2. `pixi run test`
3. verify your new tests are discovered and executed

---

## Common mistakes to avoid

- adding tests without `def main()` discovery runner,
- writing tests that depend on local machine state,
- comparing floats with exact equality when approximation is required,
- skipping negative/error cases,
- adding huge tests that are slow without necessity,
- placing tests in the wrong test directory.

---

## Recommended checklist for PR authors

- [ ] Added tests for new behavior
- [ ] Added tests for invalid/error path
- [ ] Compared against NumPy reference when applicable
- [ ] Covered at least one edge case
- [ ] Ran `pixi run final`
- [ ] Ensured test file follows discovery pattern

---

## Future improvements (tracked as follow-up work)

- add dedicated matrix comparison helpers (`check_matrix`, `check_matrix_is_close`),
- make tolerance configurable in helper functions,
- improve diagnostics for failed comparisons (shape/dtype diff summary),
- add a lightweight testing FAQ for common contributor issues.