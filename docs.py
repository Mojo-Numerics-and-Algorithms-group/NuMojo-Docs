import json
import re
import shutil
from pathlib import Path

DOCS_JSON = "docs.json"
OUT_DIR = Path("docs/readthedocs/docs/API reference")
MKDOCS_YML = Path("docs/readthedocs/mkdocs.yml")
GETTING_STARTED = Path("docs/readthedocs/docs/getting_started/install.md")
DOCS_SRC = Path("../docs")


def sanitize(text: str) -> str:
    if not text:
        return ""
    return text.strip()


def strip_todos(text: str) -> str:
    if not text:
        return text
    lines = text.splitlines()
    cleaned = []
    skip_block = False
    for line in lines:
        stripped = line.strip()
        if re.match(r"^#\s*TODO", stripped, re.IGNORECASE):
            skip_block = True
            continue
        if skip_block:
            # end the TODO block when we hit a blank line followed by non-list content
            if stripped == "":
                skip_block = False
            elif (
                stripped.startswith(("-", "*", "0123456789"[0]))
                or stripped[0:1].isdigit()
            ):
                continue
            else:
                skip_block = False
                cleaned.append(line)
            continue
        # inline TODO on its own line
        if re.match(r"^TODO\b", stripped, re.IGNORECASE):
            continue
        cleaned.append(line)
    result = "\n".join(cleaned).strip()
    # remove leading/trailing separator lines left behind
    result = re.sub(r"\n---\s*\n", "\n\n", result)
    result = re.sub(r"^---\s*\n", "", result)
    result = re.sub(r"\n---\s*$", "", result)
    return result.strip()


def render_deprecated(dep: str) -> str:
    if not dep:
        return ""
    return f'!!! warning "Deprecated"\n    {sanitize(dep)}\n\n'


def render_constraints(constraints: str) -> str:
    if not constraints:
        return ""
    return f'!!! info "Constraints"\n    {sanitize(constraints)}\n\n'


def render_parameters(params: list) -> str:
    if not params:
        return ""
    lines = ["**Parameters:**\n"]
    for p in params:
        name = p.get("name", "")
        typ = p.get("type", "")
        desc = sanitize(p.get("description", ""))
        entry = f"- `{name}`"
        if typ:
            entry += f" (`{typ}`)"
        if desc:
            entry += f": {desc}"
        lines.append(entry)
    return "\n".join(lines) + "\n\n"


def render_args(args: list) -> str:
    if not args:
        return ""
    lines = ["**Args:**\n"]
    for a in args:
        name = a.get("name", "")
        typ = a.get("type", "")
        desc = sanitize(a.get("description", ""))
        convention = a.get("convention", "")
        entry = f"- `{name}`"
        if typ:
            entry += f" (`{typ}`)"
        if convention and convention not in ("read",):
            entry += f" `[{convention}]`"
        if desc:
            entry += f": {desc}"
        lines.append(entry)
    return "\n".join(lines) + "\n\n"


def render_returns(returns) -> str:
    if not returns:
        return ""
    if isinstance(returns, dict):
        typ = returns.get("type", "")
        desc = sanitize(returns.get("description", ""))
        if not typ and not desc:
            return ""
        parts = ["**Returns:**\n"]
        entry = ""
        if typ:
            entry += f"`{typ}`"
        if desc:
            entry += (": " if entry else "") + desc
        if entry:
            parts.append(f"- {entry}")
        return "\n".join(parts) + "\n\n"
    return ""


def render_raises(raises: bool, raises_doc: str) -> str:
    if not raises:
        return ""
    doc = sanitize(raises_doc)
    if doc:
        return f'!!! failure "Raises"\n    {doc}\n\n'
    return '!!! failure "Raises"\n\n'


def render_overload(overload: dict) -> str:
    parts = []

    sig = overload.get("signature", "")
    summary = sanitize(overload.get("summary", ""))
    description = strip_todos(sanitize(overload.get("description", "")))
    deprecated = overload.get("deprecated", "")
    constraints = overload.get("constraints", "")
    params = overload.get("parameters", [])
    args = overload.get("args", [])
    returns = overload.get("returns")
    raises = overload.get("raises", False)
    raises_doc = overload.get("raisesDoc", "")

    is_static = overload.get("isStatic", False)
    is_async = overload.get("async", False)

    if sig:
        parts.append(f"```mojo\n{sig}\n```\n\n")

    badges = []
    if is_static:
        badges.append('<span class="badge badge-static">static</span>')
    if is_async:
        badges.append('<span class="badge badge-async">async</span>')
    if badges:
        parts.append(" ".join(badges) + "\n\n")

    if deprecated:
        parts.append(render_deprecated(deprecated))

    if summary:
        parts.append(f"{summary}\n\n")

    if description and description != summary:
        parts.append(f"{description}\n\n")

    if constraints:
        parts.append(render_constraints(constraints))

    if params:
        parts.append(render_parameters(params))

    if args:
        parts.append(render_args(args))

    if returns:
        parts.append(render_returns(returns))

    if raises:
        parts.append(render_raises(raises, raises_doc))

    return "".join(parts)


def render_function_group(fn: dict, level: int = 3) -> str:
    hashes = "#" * level
    name = fn.get("name", "")
    overloads = fn.get("overloads", [])

    inner = []
    inner.append(f"{hashes} `{name}`\n\n")
    if len(overloads) == 1:
        inner.append(render_overload(overloads[0]))
    else:
        for i, ol in enumerate(overloads, 1):
            inner.append(f"{'#' * (level + 1)} Overload {i}\n\n")
            inner.append(render_overload(ol))

    body = "".join(inner)
    return f'\n<div class="fn-card" markdown="1">\n\n{body}\n</div>\n'


def render_field(field: dict) -> str:
    name = field.get("name", "")
    typ = field.get("type", "")
    summary = sanitize(field.get("summary", ""))
    desc = sanitize(field.get("description", ""))
    entry = f"- **`{name}`**"
    if typ:
        entry += f" (`{typ}`)"
    if summary:
        entry += f": {summary}"
    elif desc:
        entry += f": {desc}"
    return entry


def render_alias(alias: dict, level: int = 3) -> str:
    hashes = "#" * level
    name = alias.get("name", "")
    value = alias.get("value", "")
    sig = alias.get("signature", "")
    summary = sanitize(alias.get("summary", ""))
    desc = strip_todos(sanitize(alias.get("description", "")))
    deprecated = alias.get("deprecated", "")

    parts = [f"{hashes} `{name}`\n\n"]

    if deprecated:
        parts.append(render_deprecated(deprecated))

    if sig:
        parts.append(f"```mojo\n{sig}\n```\n\n")

    if value:
        parts.append(f"**Value:** `{value}`\n\n")

    if summary:
        parts.append(f"{summary}\n\n")

    if desc and desc != summary:
        parts.append(f"{desc}\n\n")

    return "".join(parts)


def render_struct(struct: dict, level: int = 2) -> str:
    hashes = "#" * level
    name = struct.get("name", "")
    summary = sanitize(struct.get("summary", ""))
    description = strip_todos(sanitize(struct.get("description", "")))
    sig = struct.get("signature", "")
    deprecated = struct.get("deprecated", "")
    constraints = struct.get("constraints", "")
    convention = struct.get("convention", "")
    parent_traits = struct.get("parentTraits", [])
    params = struct.get("parameters", [])
    fields = struct.get("fields", [])
    aliases = struct.get("aliases", [])
    functions = struct.get("functions", [])

    parts = [f"{hashes} `{name}`\n\n"]

    if deprecated:
        parts.append(render_deprecated(deprecated))

    if sig:
        parts.append(f"```mojo\n{sig}\n```\n\n")

    meta = []
    if convention:
        meta.append(f"**Memory convention:** `{convention}`")
    if parent_traits:
        trait_names = [f"`{t.get('name', '')}`" for t in parent_traits]
        meta.append(f"**Implements:** {', '.join(trait_names)}")
    if meta:
        parts.append("  \n".join(meta) + "\n\n")

    if summary:
        parts.append(f"{summary}\n\n")

    if description and description != summary:
        parts.append(f"{description}\n\n")

    if constraints:
        parts.append(render_constraints(constraints))

    if params:
        parts.append(render_parameters(params))

    if fields:
        parts.append(f"{'#' * (level + 1)} Fields\n\n")
        for f in fields:
            parts.append(render_field(f) + "\n")
        parts.append("\n")

    if aliases:
        parts.append(f"{'#' * (level + 1)} Aliases\n\n")
        for a in aliases:
            parts.append(render_alias(a, level + 2))

    if functions:
        parts.append(f"{'#' * (level + 1)} Methods\n\n")
        for fn in functions:
            parts.append(render_function_group(fn, level + 2))

    return "".join(parts)


def render_trait(trait: dict, level: int = 2) -> str:
    hashes = "#" * level
    name = trait.get("name", "")
    summary = sanitize(trait.get("summary", ""))
    description = strip_todos(sanitize(trait.get("description", "")))
    deprecated = trait.get("deprecated", "")
    parent_traits = trait.get("parentTraits", [])
    fields = trait.get("fields", [])
    aliases = trait.get("aliases", [])
    functions = trait.get("functions", [])

    parts = [f"{hashes} `{name}`\n\n"]

    if deprecated:
        parts.append(render_deprecated(deprecated))

    if parent_traits:
        trait_names = [f"`{t.get('name', '')}`" for t in parent_traits]
        parts.append(f"**Extends:** {', '.join(trait_names)}\n\n")

    if summary:
        parts.append(f"{summary}\n\n")

    if description and description != summary:
        parts.append(f"{description}\n\n")

    if fields:
        parts.append(f"{'#' * (level + 1)} Fields\n\n")
        for f in fields:
            parts.append(render_field(f) + "\n")
        parts.append("\n")

    if aliases:
        parts.append(f"{'#' * (level + 1)} Aliases\n\n")
        for a in aliases:
            parts.append(render_alias(a, level + 2))

    if functions:
        parts.append(f"{'#' * (level + 1)} Methods\n\n")
        for fn in functions:
            parts.append(render_function_group(fn, level + 2))

    return "".join(parts)


def render_module(module: dict, module_path: str) -> str:
    summary = sanitize(module.get("summary", ""))
    description = strip_todos(sanitize(module.get("description", "")))
    aliases = module.get("aliases", [])
    traits = module.get("traits", [])
    structs = module.get("structs", [])
    functions = module.get("functions", [])

    parts = [f"# `{module_path}`\n\n"]

    if summary:
        parts.append(f"{summary}\n\n")

    if description and description != summary:
        parts.append(f"{description}\n\n")

    if aliases:
        parts.append("## Aliases\n\n")
        for a in aliases:
            parts.append(render_alias(a, 3))

    if traits:
        parts.append("## Traits\n\n")
        for t in traits:
            parts.append(render_trait(t, 3))

    if structs:
        parts.append("## Structs\n\n")
        for s in structs:
            parts.append(render_struct(s, 3))

    if functions:
        parts.append("## Functions\n\n")
        for fn in functions:
            parts.append(render_function_group(fn, 3))

    return "".join(parts)


def has_content(module: dict) -> bool:
    return bool(
        module.get("aliases")
        or module.get("traits")
        or module.get("structs")
        or module.get("functions")
        or sanitize(module.get("summary", ""))
        or sanitize(module.get("description", ""))
    )


def process_node(node: dict, pkg_path: str, out_dir: Path, docs_dir: Path) -> list:
    name = node.get("name", "")
    modules = node.get("modules", [])
    packages = node.get("packages", [])

    node_dir = out_dir / name
    node_dir.mkdir(parents=True, exist_ok=True)

    nav_entries = []

    index_parts = [f"# `{pkg_path}`\n\n"]
    node_summary = sanitize(node.get("summary", ""))
    node_desc = strip_todos(sanitize(node.get("description", "")))
    if node_summary:
        index_parts.append(f"{node_summary}\n\n")
    if node_desc and node_desc != node_summary:
        index_parts.append(f"{node_desc}\n\n")

    child_rows = []

    for mod in modules:
        mod_name = mod.get("name", "")
        if mod_name == "__init__" and not has_content(mod):
            continue
        mod_display = mod_name if mod_name != "__init__" else f"{name} (init)"
        mod_path_str = f"{pkg_path}.{mod_name}"
        if has_content(mod):
            content = render_module(mod, mod_path_str)
            md_file = node_dir / f"{mod_name}.md"
            md_file.write_text(content, encoding="utf-8")
            rel = str(md_file.relative_to(docs_dir)).replace("\\", "/")
            nav_entries.append({mod_display: rel})
            child_rows.append(
                (
                    mod_display,
                    "module",
                    sanitize(mod.get("summary", "")),
                    f"[`{mod_name}`](./{mod_name}.md)",
                )
            )

    for pkg in packages:
        pkg_name = pkg.get("name", "")
        pkg_summary = sanitize(pkg.get("summary", ""))
        sub_nav = process_node(pkg, f"{pkg_path}.{pkg_name}", node_dir, docs_dir)
        nav_entries.append({pkg_name: sub_nav})
        child_rows.append(
            (pkg_name, "package", pkg_summary, f"[`{pkg_name}`](./{pkg_name}/index.md)")
        )

    if child_rows:
        index_parts.append("## Contents\n\n")
        index_parts.append("| Name | Kind | Description |\n")
        index_parts.append("|------|------|-------------|\n")
        for display, kind, summary, link in sorted(child_rows, key=lambda x: x[0]):
            index_parts.append(f"| {link} | {kind} | {summary} |\n")
        index_parts.append("\n")

    index_file = node_dir / "index.md"
    index_file.write_text("".join(index_parts), encoding="utf-8")
    rel_index = str(index_file.relative_to(docs_dir)).replace("\\", "/")
    nav_entries.insert(0, {"Overview": rel_index})

    return nav_entries


def build_nav(decl_nav: list) -> list:
    # decl_nav is the nav list for the top-level `numojo` package node.
    # We want to surface core / routines / science as their own top-level
    # API Reference tabs rather than nesting everything under one "numojo" entry.
    #
    # decl_nav structure:
    #   [{"Overview": ...}, {"__init__": ...}, {"prelude": ...},
    #    {"core": [...]}, {"routines": [...]}, {"science": [...]}]

    overview_entry = None
    top_modules = []
    sub_packages = {}

    for entry in decl_nav:
        for k, v in entry.items():
            if k == "Overview":
                overview_entry = {"Overview": v}
            elif isinstance(v, list):
                sub_packages[k] = v
            else:
                top_modules.append({k: v})

    api_ref_nav = []
    if overview_entry:
        api_ref_nav.append(overview_entry)
    api_ref_nav.extend(top_modules)

    # Add each major sub-package as its own named section
    section_labels = {
        "core": "Core",
        "routines": "Routines",
        "science": "Science",
    }
    for pkg_name, pkg_nav in sub_packages.items():
        label = section_labels.get(pkg_name, pkg_name.capitalize())
        api_ref_nav.append({label: pkg_nav})

    return [
        {"Home": "index.md"},
        {
            "Getting Started": [
                {"Quickstart": "getting_started/quickstart.md"},
                {"Installation": "getting_started/install.md"},
                {"NDArray vs Matrix": "getting_started/ndarray-vs-matrix.md"},
            ]
        },
        {
            "User Guide": [
                {
                    "Array Creation & Manipulation": "user-guide/ndarray-creation-manipulation.md"
                },
                {"Indexing": "user-guide/indexing.md"},
                {"Linear Algebra": "user-guide/linalg.md"},
                {"I/O": "user-guide/io.md"},
            ]
        },
        {
            "Developer Guide": [
                {"Architecture": "developer-guide/architecture.md"},
                {"Adding Functions": "developer-guide/adding-functions.md"},
                {"Backend Dispatch": "developer-guide/backend-dispatch.md"},
                {"NDArray Structure": "developer-guide/ndarray-basic-structure.md"},
                {"Style Guide": "developer-guide/style-guide.md"},
                {"Testing": "developer-guide/testing.md"},
            ]
        },
        {
            "Links": [
                {
                    "GitHub": "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo"
                },
                {"Discord": "https://discord.gg/NcnSH5n26F"},
                {
                    "Changelog": "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo/blob/main/docs/changelog.md"
                },
                {
                    "Roadmap": "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo/blob/main/docs/roadmap.md"
                },
                {
                    "Contributing": "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo/blob/main/CONTRIBUTING.md"
                },
            ]
        },
        {"API Reference": api_ref_nav},
    ]


MKDOCS_TEMPLATE = """\
site_name: NuMojo
site_description: NuMojo — A numerics library for Mojo, inspired by NumPy.
site_author: NuMojo Contributors
docs_dir: "./docs"
repo_url: https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo
repo_name: NuMojo/NuMojo

theme:
  name: material
  logo: https://raw.githubusercontent.com/Mojo-Numerics-and-Algorithms-group/NuMojo/main/assets/numojo_logo.png
  favicon: https://raw.githubusercontent.com/Mojo-Numerics-and-Algorithms-group/NuMojo/main/assets/numojo_logo.png
  palette:
    - scheme: default
      primary: deep purple
      accent: purple
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: deep purple
      accent: purple
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.sections
    - navigation.path
    - navigation.top
    - navigation.footer
    - search.highlight
    - search.suggest
    - search.share
    - content.code.copy
    - content.code.annotate
    - toc.follow

plugins:
  - search

markdown_extensions:
  - abbr
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - toc:
      permalink: true
      toc_depth: 4
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.betterem:
      smart_enable: all
  - pymdownx.caret
  - pymdownx.details
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.keys
  - pymdownx.mark
  - pymdownx.smartsymbols
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.tilde

extra_css:
  - stylesheets/extra.css

extra_javascript:
  - javascripts/mathjax.js
  - https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js

nav:
{nav_yaml}
"""


def dict_to_yaml(obj, indent: int = 0) -> str:
    pad = "  " * indent
    if isinstance(obj, list):
        lines = []
        for item in obj:
            lines.append(dict_to_yaml(item, indent))
        return "\n".join(lines)
    if isinstance(obj, dict):
        lines = []
        for k, v in obj.items():
            safe_k = f'"{k}"' if any(c in k for c in ":{}[]|>&*!,#?-@`'\"%") else k
            if isinstance(v, list):
                lines.append(f"{pad}- {safe_k}:")
                lines.append(dict_to_yaml(v, indent + 1))
            elif isinstance(v, str):
                safe_v = f'"{v}"' if any(c in v for c in ":#{}[]|>&*!,?@`'\"") else v
                lines.append(f"{pad}- {safe_k}: {safe_v}")
            else:
                lines.append(f"{pad}- {safe_k}: {v}")
        return "\n".join(lines)
    return f"{pad}{obj}"


def write_extra_assets(readthedocs_dir: Path):
    css_dir = readthedocs_dir / "docs" / "stylesheets"
    css_dir.mkdir(parents=True, exist_ok=True)
    css = """\
/* Badge styles for static/async markers */
.badge {
  display: inline-block;
  padding: 0.15em 0.5em;
  border-radius: 4px;
  font-size: 0.75em;
  font-weight: 600;
  vertical-align: middle;
  margin-right: 0.3em;
}
.badge-static {
  background: var(--md-primary-fg-color);
  color: var(--md-primary-bg-color);
}
.badge-async {
  background: #7c4dff;
  color: #fff;
}

/* Tighten up API reference heading code */
.md-typeset h3 code,
.md-typeset h4 code,
.md-typeset h5 code {
  font-size: 1em;
}

/* Make code blocks slightly more compact */
.md-typeset pre > code {
  font-size: 0.85em;
}

/* Sidebar nav refinements */
.md-nav__item .md-nav__link {
  font-size: 0.8rem;
}

/* Function card: each function gets its own outlined card */
.fn-card {
  border: 1px solid var(--md-primary-fg-color--light);
  border-left: 4px solid var(--md-primary-fg-color);
  border-radius: 6px;
  padding: 1.2em 1.4em 0.8em;
  margin: 1.8em 0;
  background: var(--md-code-bg-color);
}

.fn-card > h3:first-child,
.fn-card > h4:first-child,
.fn-card > h5:first-child {
  margin-top: 0;
}
"""
    (css_dir / "extra.css").write_text(css, encoding="utf-8")

    js_dir = readthedocs_dir / "docs" / "javascripts"
    js_dir.mkdir(parents=True, exist_ok=True)
    js = """\
window.MathJax = {
  tex: {
    inlineMath: [["\\\\(", "\\\\)"]],
    displayMath: [["\\\\[", "\\\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};
"""
    (js_dir / "mathjax.js").write_text(js, encoding="utf-8")


# if possible fetch this from github docs or maybe add another file here in same directory.
INSTALL_MD = """\
# Installation

NuMojo supports multiple installation paths depending on your workflow.

## Prerequisites

- A supported platform (`osx-arm64` or `linux-64`)
- `pixi` installed
- Compatible Mojo/Modular toolchain (managed through `pixi.toml`)

---

## Method 1 — Install from source (recommended for contributors)

Use this if you want to run tests, modify source, or contribute.

### 1) Clone the repository

```bash
git clone https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo.git
cd NuMojo
```

### 2) Create environment

```bash
pixi install
```

### 3) Run validation

```bash
pixi run final
```

This runs formatting + tests.

---

## Method 2 — Use NuMojo in your own Pixi project (git dependency)

Use this when you want NuMojo directly from GitHub in another project.

Add the following to your project `pixi.toml` (adjust names as needed):

```toml
[workspace]
preview = ["pixi-build"]

[package]
name = "your_project_name"
version = "0.1.0"

[package.build]
backend = { name = "pixi-build-mojo", version = "0.*" }

[package.build.config.pkg]
name = "your_package_name"

[package.host-dependencies]
modular = ">=25.7.0,<26"

[package.build-dependencies]
modular = ">=25.7.0,<26"
numojo = { git = "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo", branch = "main" }

[package.run-dependencies]
modular = ">=25.7.0,<26"
numojo = { git = "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo", branch = "main" }

[dependencies]
modular = ">=25.7.0,<26"
numojo = { git = "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo", branch = "main" }
```

Then install:

```bash
pixi install
```

### Branch choice

- `main`: stable branch
- `pre-x.y`: active development branch (can include breaking changes)

---

## Method 3 — Install stable package from prefix.dev

Use this for reproducible, pinned setups in projects that don't need source edits.

In your `pixi.toml`:

```toml
[workspace]
channels = ["https://repo.prefix.dev/modular-community"]

[dependencies]
numojo = "=0.8.0"
```

Then:

```bash
pixi install
```

### Compatibility table

| NuMojo Version | Required Mojo Version |
| --- | --- |
| v0.8.0 | ==25.7 |
| v0.7.0 | ==25.3 |
| v0.6.1 | ==25.2 |
| v0.6.0 | ==25.2 |

---

## Method 4 — Build standalone `numojo.mojopkg`

Use this for offline or hermetic workflows.

From the NuMojo repo root:

```bash
pixi run package
```

This generates `numojo.mojopkg`. Copy it to your target project directory (or add its parent path to include dirs).

---

## Method 5 — Direct source include (no package build)

Use this for fast local iteration while editing NuMojo source.

```bash
mojo run -I "/path/to/NuMojo" your_program.mojo
```

Example:

```bash
mojo run -I "/Users/yourname/Projects/NuMojo" app.mojo
```

---

## VSCode / LSP setup

To enable autocompletion and symbol resolution for NuMojo:

1. Open VSCode settings
2. Go to `Mojo › Lsp: Include Dirs`
3. Add the absolute path to your NuMojo folder
4. Restart Mojo LSP

---

## Verify installation

Create a quick file like `check_numojo.mojo`:

```mojo
import numojo as nm
from numojo.prelude import *

fn main() raises:
    var a = nm.arange[f32](10)
    print(a)
    print(nm.sum(a))
```

Run:

```bash
mojo run -I "/path/to/NuMojo" check_numojo.mojo
```

If this runs successfully, your installation is working.

---

## Troubleshooting

### Dependency resolution issues
- Ensure your `modular` version is compatible with your selected NuMojo version.
- Recreate environment:
  ```bash
  pixi install --locked
  ```

### Package not found in editor
- Verify LSP include path points to the NuMojo root.
- Restart VSCode and Mojo LSP.

### Import works in terminal but not in editor
- Editor often uses separate language-server include paths; configure `Mojo › Lsp: Include Dirs` explicitly.
"""


def write_getting_started():
    GETTING_STARTED.parent.mkdir(parents=True, exist_ok=True)
    GETTING_STARTED.write_text(INSTALL_MD, encoding="utf-8")


def copy_docs_pages(docs_dir: Path):
    mapping = {
        DOCS_SRC / "getting-started" / "quickstart.md": docs_dir
        / "getting_started"
        / "quickstart.md",
        DOCS_SRC / "getting-started" / "ndarray-vs-matrix.md": docs_dir
        / "getting_started"
        / "ndarray-vs-matrix.md",
        DOCS_SRC / "user-guide" / "ndarray-creation-manipulation.md": docs_dir
        / "user-guide"
        / "ndarray-creation-manipulation.md",
        DOCS_SRC / "user-guide" / "indexing.md": docs_dir
        / "user-guide"
        / "indexing.md",
        DOCS_SRC / "user-guide" / "linalg.md": docs_dir / "user-guide" / "linalg.md",
        DOCS_SRC / "user-guide" / "io.md": docs_dir / "user-guide" / "io.md",
        DOCS_SRC / "developer-guide" / "architecture.md": docs_dir
        / "developer-guide"
        / "architecture.md",
        DOCS_SRC / "developer-guide" / "adding-functions.md": docs_dir
        / "developer-guide"
        / "adding-functions.md",
        DOCS_SRC / "developer-guide" / "backend-dispatch.md": docs_dir
        / "developer-guide"
        / "backend-dispatch.md",
        DOCS_SRC / "developer-guide" / "ndarray-basic-structure.md": docs_dir
        / "developer-guide"
        / "ndarray-basic-structure.md",
        DOCS_SRC / "developer-guide" / "style-guide.md": docs_dir
        / "developer-guide"
        / "style-guide.md",
        DOCS_SRC / "developer-guide" / "testing.md": docs_dir
        / "developer-guide"
        / "testing.md",
    }
    for src, dst in mapping.items():
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
            print(f"  copied {src.name} -> {dst}")
        else:
            print(f"  WARNING: source not found: {src}")


INDEX_MD = """\
---
hide:
  - navigation
  - toc
---

# NuMojo

<p style="font-size:1.2em">
A library for numerical computing in <strong>Mojo 🔥</strong>. Inspired by NumPy.
</p>

<div style="margin: 1.5em 0; display:flex; gap:0.7em; flex-wrap:wrap;">
<a href="getting_started/quickstart/" class="md-button md-button--primary">Quickstart →</a>
<a href="getting_started/install/" class="md-button">Installation</a>
<a href="API reference/numojo/" class="md-button">API Reference</a>
<a href="https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo" class="md-button">GitHub</a>
<a href="https://discord.gg/NcnSH5n26F" class="md-button">Discord</a>
</div>

---

## What is NuMojo?

NuMojo provides fast, vectorized numerical routines for Mojo — the same role NumPy and SciPy play in
the Python ecosystem, but built from the ground up to exploit Mojo's native SIMD, parallelism, and
(future) GPU acceleration.

**NuMojo is not** a machine learning library and will never include back-propagation.

---

## Core types

| Type | Description |
|------|-------------|
| `NDArray` | General-purpose N-dimensional array for tensors, grids, batches |
| `Matrix` | Dedicated 2-D array optimized for linear-algebra workflows |
| `ComplexNDArray` | N-dimensional array of complex numbers |

---

## Highlights

=== "NDArray"

    ```mojo
    import numojo as nm
    from numojo.prelude import *

    fn main() raises:
        var A = nm.random.randn(Shape(1000, 1000))
        var B = nm.random.randn(Shape(1000, 1000))
        var C = A @ B
        var I = nm.inv(A)
        var s = A[1:3, 4:19]
        print(nm.sum(A))
    ```

=== "Matrix"

    ```mojo
    from numojo import Matrix
    import numojo as nm

    fn main() raises:
        var A = Matrix.rand(shape=(1000, 1000))
        var B = Matrix.rand(shape=(1000, 1))
        var x = nm.solve(A, B)
        print(x)
    ```

=== "ComplexNDArray"

    ```mojo
    import numojo as nm
    from numojo.prelude import *

    fn main() raises:
        var z = CScalar[cf32](5)
        var A = nm.full[cf32](Shape(4, 4), fill_value=z)
        var B = nm.ones[cf32](Shape(4, 4))
        print(A * B)
    ```

---

## Routines at a glance

- **Creation** — `zeros`, `ones`, `arange`, `linspace`, `fromstring`, `random`, …
- **Manipulation** — `reshape`, `transpose`, `flip`, `broadcast_to`, …
- **Math** — `sin`, `cos`, `exp`, `log`, `sqrt`, arithmetic, rounding, …
- **Linear algebra** — `matmul`, `inv`, `solve`, `lstsq`, `det`, `norm`, decompositions, …
- **Logic** — `all`, `any`, comparison, logical ops, …
- **Statistics** — `mean`, `std`, `var`, `sum`, `prod`, `min`, `max`, …
- **Sorting & searching** — `sort`, `argsort`, `argmin`, `argmax`, …
- **I/O** — file read/write, formatting, …

---

## Installation

The fastest way to get started:

```toml
[workspace]
channels = ["https://repo.prefix.dev/modular-community"]

[dependencies]
numojo = "=0.8.0"
```

```bash
pixi install
```

See the [full installation guide](getting_started/install.md) for all methods.

---

## Version compatibility

| NuMojo | Mojo |
|--------|------|
| v0.8.0 | ==25.7 |
| v0.7.0 | ==25.3 |
| v0.6.1 | ==25.2 |

---

## License

Apache 2.0 with LLVM Exceptions.
See [LICENSE](https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo/blob/main/LICENSE).

## Contributors

[![Contributors](https://contrib.rocks/image?repo=Mojo-Numerics-and-Algorithms-group/NuMojo)](https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo/graphs/contributors)
"""


def generate():
    with open(DOCS_JSON, encoding="utf-8") as f:
        data = json.load(f)

    decl = data["decl"]

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    docs_dir = MKDOCS_YML.parent / "docs"
    print(f"Generating API reference into {OUT_DIR}/")
    decl_nav = process_node(decl, "numojo", OUT_DIR, docs_dir)

    write_getting_started()
    print(f"Updated {GETTING_STARTED}")

    copy_docs_pages(docs_dir)

    index_path = docs_dir / "index.md"
    index_path.write_text(INDEX_MD, encoding="utf-8")
    print(f"Updated {index_path}")

    readthedocs_dir = MKDOCS_YML.parent
    write_extra_assets(readthedocs_dir)

    nav = build_nav(decl_nav)
    nav_yaml = dict_to_yaml(nav, indent=1)
    mkdocs_content = MKDOCS_TEMPLATE.format(nav_yaml=nav_yaml)
    MKDOCS_YML.write_text(mkdocs_content, encoding="utf-8")
    print(f"Updated {MKDOCS_YML}")
    print("Done.")


if __name__ == "__main__":
    generate()
