# NuMojo Architecture Guide

This document explains how NuMojo is organized, what each layer is responsible for, and how to add or change code without creating API or maintenance debt.

## Goals of the architecture

- Keep the **public API simple and stable**.
- Keep implementation details (execution strategy, backend choices) **internal**.
- Minimize duplication across `NDArray` and `Matrix` code paths.
- Make onboarding easier by clearly defining where code should live.

---

## High-level architecture

NuMojo is currently evolving toward a layered structure:

1. **Core layer** (`numojo/core`)
2. **Routines layer** (`numojo/routines`, top-level `numojo`)
4. **Tests + docs + examples** (`tests`, `docs`, `examples`)

---

## Layer 1: Core (`numojo/core`)

Core contains foundational data types and low-level mechanics.

### Core responsibilities

- Data containers:
  - `NDArray`
  - `Matrix`
  - `ComplexNDArray`
  - `ComplexSIMD`
- Shape/stride/layout mechanics:
  - shape and stride structs
  - layout flags and contiguity checks
- Indexing primitives:
  - `Item`
  - slice/index traversal utilities
- Memory ownership and storage:
  - data container
  - reference counting
  - host/device abstractions
  - DLPack conversion utilities
- Base error types and shared aliases

### Core should NOT contain

- High-level user workflow docs/examples
- Topic-level numerical routines exposed as user namespaces (`math`, `linalg`, `statistics`, etc.)
- API ergonomics that belong in routines/top-level exports

---

## Layer 2: Routines + public API (`numojo/routines`, `numojo/__init__.mojo`)

Routines provide NumPy-like functional APIs grouped by domain:

- `creation`
- `manipulation`
- `math`
- `linalg`
- `logic`
- `statistics`
- `io`
- `sorting`, `searching`, `indexing`, `random`, etc.

Top-level `numojo/__init__.mojo` exposes a curated, user-friendly import surface.

### Design rules for this layer

1. Public function names should be clear and consistent with NumPy-like expectations where possible.
2. Public APIs should avoid leaking backend/internal plumbing.
3. Routine modules should delegate shared execution patterns to internal helpers instead of repeating loops in every function.

---

## Execution model and backend strategy

NuMojo currently uses vectorized helpers and backend-style abstractions in several routines. The recommended direction is:

- Public functions remain simple:
  - example: `sin(x)`
- Internal execution chooses strategy:
  - vectorized CPU path
  - future GPU path

A practical long-term pattern is an internal execution engine with methods like:

- `apply_unary[dtype, fn](x)`
- `apply_binary[dtype, fn](x, y)`

This keeps backend decisions centralized and avoids passing backend parameters through user-facing signatures.

---

## Data model summary

At a conceptual level, `NDArray` wraps:

- data buffer
- shape
- strides
- offset
- flags / metadata

`Matrix` is a dedicated 2D container with matrix-specific semantics and methods.

Key principles:

- Views share underlying data and metadata relationships safely.
- Copies should be explicit when ownership separation is required.
- Shape/stride correctness is part of core correctness.

For detailed memory/reference behavior, see:
- `developer-guide/ndarray-basic-structure.md`

---

## API exposure strategy

Current public access patterns include:

- top-level convenience:
  - `numojo.sin`, `numojo.sum`, `numojo.solve`, etc.
- namespace access:
  - `numojo.linalg.solve`
  - `numojo.random.randn`

Recommended governance:

- Keep top-level exports curated and stable.
- Avoid duplicate re-export chains where possible.
- Treat top-level imports as a compatibility contract.

---

## Architectural pain points (known)

These are active cleanup targets and should guide new contributions:

1. Inconsistent naming in some public symbols.
2. Backend/internal execution details exposed in some public signatures.
3. Export duplication across multiple `__init__` modules.
4. Stale docs/examples in some parts of the documentation set.
5. Inconsistent Error handling (we prefer to use internal `NumojoError`).

When contributing, prefer patterns that reduce these issues.

---

## Contribution rules to preserve architecture

Before opening a PR, verify:

1. **Placement**
   - Did you put code in the correct layer?
2. **Reuse**
   - Are you reusing shared helpers instead of duplicating loops/logic whenever possible?
3. **API cleanliness**
   - Did internal mechanics leak into public function signatures?
4. **Consistency**
   - Naming, error style, and behavior match existing conventions?
5. **Coverage**
   - Tests added/updated in the appropriate test module?
6. **Docs**
   - Relevant docs updated if user-facing behavior changed?

---

## Related docs

- `docs/README.md`
- `docs/developer-guide/adding-functions.md`
- `docs/developer-guide/backend-dispatch.md`
- `docs/developer-guide/testing.md`
- `docs/developer-guide/style-guide.md`
- `docs/roadmap.md`
- `docs/features.md`
