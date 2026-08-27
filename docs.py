import json
import re
import shutil
from pathlib import Path

DOCS_JSON = "docs.json"
OUT_DIR = Path("docs/readthedocs/docs/API reference")
MKDOCS_YML = Path("docs/readthedocs/mkdocs.yml")
GETTING_STARTED = Path("docs/readthedocs/docs/getting_started/install.md")
# NuMojo-Docs is checked out as a sibling of the NuMojo repo
# (…/Codes/NuMojo and …/Codes/NuMojo-Docs), so the source repo is reached
# via ../NuMojo, not ../.
NUMOJO_REPO = Path("../NuMojo")
DOCS_SRC = NUMOJO_REPO / "docs"
README_SRC = NUMOJO_REPO / "README.MD"


def sanitize(text: str) -> str:
    if not text:
        return ""
    return text.strip()


# `mojo doc` derives a module's one-line `summary` by joining the first
# "sentence" of its docstring, but our module docstrings start with a
# `Title (dotted.path).` line underlined with `===`, all on separate
# source lines. Joined with spaces, that produces "Title (path).
# ===...=== First real sentence." on one line. Strip that title/underline
# prefix so only the real summary sentence renders.
MODULE_TITLE_PREFIX_RE = re.compile(r"^.{1,120}?\.\s+=+\s+")


def clean_module_summary(summary: str) -> str:
    summary = sanitize(summary)
    if not summary:
        return summary
    return MODULE_TITLE_PREFIX_RE.sub("", summary, count=1).strip()


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


# Docstring prose sometimes writes its own "Examples:" / "Notes:" /
# "References:" labels as plain text (mojo doc doesn't parse these into
# structured fields the way it does Args/Returns/Raises). Recognize the
# common spellings on their own line and turn them into a small styled
# label so they read as a distinct subsection instead of blending into
# the surrounding paragraph.
PROSE_SECTION_RE = re.compile(
    r"^(examples?|notes?|references?|further readings?)\s*:\s*$",
    re.IGNORECASE,
)
PROSE_SECTION_CANONICAL = {
    "example": "Examples",
    "examples": "Examples",
    "note": "Notes",
    "notes": "Notes",
    "reference": "References",
    "references": "References",
    "further reading": "Further Reading",
    "further readings": "Further Reading",
}


def format_prose_sections(text: str) -> str:
    if not text:
        return text
    lines = text.splitlines()
    out = []
    for line in lines:
        m = PROSE_SECTION_RE.match(line.strip())
        if m:
            label = PROSE_SECTION_CANONICAL.get(m.group(1).lower(), m.group(1).title())
            out.append(f'<div class="prose-label">{label}</div>')
        else:
            out.append(line)
    return "\n".join(out)


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
    lines = ['<div class="prose-label">Parameters</div>\n']
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
    lines = ['<div class="prose-label">Args</div>\n']
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
        parts = ['<div class="prose-label">Returns</div>\n']
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
    description = format_prose_sections(strip_todos(sanitize(overload.get("description", ""))))
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


def render_function_group(fn: dict, nested: bool = False) -> str:
    hashes = "####" if nested else "###"
    name = fn.get("name", "")
    overloads = fn.get("overloads", [])

    inner = []
    inner.append(f"{hashes} `{name}`\n\n")
    if len(overloads) == 1:
        inner.append(render_overload(overloads[0]))
    else:
        for i, ol in enumerate(overloads, 1):
            inner.append(f'<div class="overload-divider">Overload {i}</div>\n\n')
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


def render_alias(alias: dict, nested: bool = False) -> str:
    hashes = "####" if nested else "###"
    name = alias.get("name", "")
    value = alias.get("value", "")
    sig = alias.get("signature", "")
    summary = sanitize(alias.get("summary", ""))
    desc = format_prose_sections(strip_todos(sanitize(alias.get("description", ""))))
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


def render_struct(struct: dict) -> str:
    name = struct.get("name", "")
    summary = sanitize(struct.get("summary", ""))
    description = format_prose_sections(strip_todos(sanitize(struct.get("description", ""))))
    sig = struct.get("signature", "")
    deprecated = struct.get("deprecated", "")
    constraints = struct.get("constraints", "")
    convention = struct.get("convention", "")
    parent_traits = struct.get("parentTraits", [])
    params = struct.get("parameters", [])
    fields = struct.get("fields", [])
    aliases = struct.get("aliases", [])
    functions = struct.get("functions", [])

    header = ['<span class="badge badge-kind">struct</span>\n\n']

    if deprecated:
        header.append(render_deprecated(deprecated))

    if sig:
        header.append(f"```mojo\n{sig}\n```\n\n")

    meta = []
    if convention:
        meta.append(f"**Memory convention:** `{convention}`")
    if parent_traits:
        trait_names = [f"`{t.get('name', '')}`" for t in parent_traits]
        meta.append(f"**Implements:** {', '.join(trait_names)}")
    if meta:
        header.append("  \n".join(meta) + "\n\n")

    if summary:
        header.append(f"{summary}\n\n")

    if description and description != summary:
        header.append(f"{description}\n\n")

    if constraints:
        header.append(render_constraints(constraints))

    if params:
        header.append(render_parameters(params))

    parts = [
        f"### `{name}`\n\n",
        '<div class="type-header" markdown="1">\n\n' + "".join(header) + "</div>\n\n",
    ]

    if fields:
        parts.append("#### Fields\n\n")
        for f in fields:
            parts.append(render_field(f) + "\n")
        parts.append("\n")

    if aliases:
        parts.append("#### Aliases\n\n")
        for a in aliases:
            parts.append(render_alias(a, nested=True))

    if functions:
        parts.append("#### Methods\n\n")
        for fn in functions:
            parts.append(render_function_group(fn, nested=True))

    return "".join(parts)


def render_trait(trait: dict) -> str:
    name = trait.get("name", "")
    summary = sanitize(trait.get("summary", ""))
    description = format_prose_sections(strip_todos(sanitize(trait.get("description", ""))))
    deprecated = trait.get("deprecated", "")
    parent_traits = trait.get("parentTraits", [])
    fields = trait.get("fields", [])
    aliases = trait.get("aliases", [])
    functions = trait.get("functions", [])

    header = ['<span class="badge badge-kind">trait</span>\n\n']

    if deprecated:
        header.append(render_deprecated(deprecated))

    if parent_traits:
        trait_names = [f"`{t.get('name', '')}`" for t in parent_traits]
        header.append(f"**Extends:** {', '.join(trait_names)}\n\n")

    if summary:
        header.append(f"{summary}\n\n")

    if description and description != summary:
        header.append(f"{description}\n\n")

    parts = [
        f"### `{name}`\n\n",
        '<div class="type-header" markdown="1">\n\n' + "".join(header) + "</div>\n\n",
    ]

    if fields:
        parts.append("#### Fields\n\n")
        for f in fields:
            parts.append(render_field(f) + "\n")
        parts.append("\n")

    if aliases:
        parts.append("#### Aliases\n\n")
        for a in aliases:
            parts.append(render_alias(a, nested=True))

    if functions:
        parts.append("#### Methods\n\n")
        for fn in functions:
            parts.append(render_function_group(fn, nested=True))

    return "".join(parts)


def render_module(module: dict, module_path: str) -> str:
    summary = clean_module_summary(module.get("summary", ""))
    description = format_prose_sections(strip_todos(sanitize(module.get("description", ""))))
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
            parts.append(render_alias(a))

    if traits:
        parts.append("## Traits\n\n")
        for t in traits:
            parts.append(render_trait(t))

    if structs:
        parts.append("## Structs\n\n")
        for s in structs:
            parts.append(render_struct(s))

    if functions:
        parts.append("## Functions\n\n")
        for fn in functions:
            parts.append(render_function_group(fn))

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
    node_summary = clean_module_summary(node.get("summary", ""))
    node_desc = format_prose_sections(strip_todos(sanitize(node.get("description", ""))))
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
                    clean_module_summary(mod.get("summary", "")),
                    f"[`{mod_name}`](./{mod_name}.md)",
                )
            )

    for pkg in packages:
        pkg_name = pkg.get("name", "")
        pkg_summary = clean_module_summary(pkg.get("summary", ""))
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
            ]
        },
        {
            "User Guide": [
                {"Overview": "user-guide/overview.md"},
                {"Roadmap": "user-guide/roadmap.md"},
                {"Changelog": "user-guide/changelog.md"},
            ]
        },
        {
            "Developer Guide": [
                {"Architecture": "developer-guide/architecture.md"},
                {"NDArray Structure": "developer-guide/ndarray-basic-structure.md"},
                {"Style Guide": "developer-guide/style-guide.md"},
                {"Contributing": "developer-guide/contributing.md"},
                {"Pre-PR Checks": "developer-guide/pre-pr-checks.md"},
            ]
        },
        {"API Reference": api_ref_nav},
        {
            "Links": [
                {
                    "GitHub": "https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo"
                },
                {"Discord": "https://discord.gg/NcnSH5n26F"},
            ]
        },
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
  font:
    text: Inter
    code: JetBrains Mono
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.indexes
    - navigation.top
    - navigation.footer
    - navigation.instant
    - navigation.instant.progress
    - navigation.tracking
    - search.highlight
    - search.suggest
    - search.share
    - content.code.copy
    - content.code.annotate
    - content.tooltips
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
/* Layout */
.md-grid {
  max-width: 68rem;
}

.md-typeset {
  line-height: 1.65;
}

.md-typeset h1 {
  font-weight: 700;
  margin-bottom: 1em;
}

.md-typeset h2 {
  font-weight: 600;
  margin-top: 1.8em;
  padding-top: 0.4em;
  border-top: 1px solid var(--md-default-fg-color--lightest);
}

.md-typeset h2:first-child {
  border-top: none;
  padding-top: 0;
}

/* Badges */
.badge {
  display: inline-block;
  padding: 0.1em 0.55em;
  border-radius: 4px;
  font-size: 0.7em;
  font-weight: 600;
  letter-spacing: 0.02em;
  text-transform: uppercase;
  vertical-align: middle;
  margin-right: 0.4em;
}
.badge-static {
  background: var(--md-default-fg-color--lightest);
  color: var(--md-default-fg-color--light);
}
.badge-async {
  background: var(--md-primary-fg-color--light);
  color: var(--md-primary-bg-color);
}
.badge-kind {
  background: var(--md-primary-fg-color);
  color: var(--md-primary-bg-color);
}

/* API reference headings & code */
.md-typeset h3 code,
.md-typeset h4 code,
.md-typeset h5 code {
  font-size: 0.95em;
  background: none;
  padding: 0;
}

.md-typeset pre > code {
  font-size: 0.82em;
  line-height: 1.55;
}

.md-typeset code {
  border-radius: 4px;
}

/* Sidebar navigation */
.md-nav__item .md-nav__link {
  font-size: 0.78rem;
}

.md-nav__title {
  font-weight: 700;
}

.md-nav--secondary .md-nav__link {
  font-size: 0.72rem;
}

/* Struct/trait header: sits under the ### name, no box (structs can have
   dozens of methods, so a full enclosing card would grow huge). */
.type-header {
  border-left: 3px solid var(--md-primary-fg-color);
  padding: 0.2em 0 0.2em 1em;
  margin: 0.6em 0 1.4em;
}

.type-header > *:first-child {
  margin-top: 0;
}

.type-header > *:last-child {
  margin-bottom: 0;
}

/* Function/method card */
.fn-card {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-left: 3px solid var(--md-primary-fg-color);
  border-radius: 8px;
  padding: 1.1em 1.4em 0.9em;
  margin: 1.6em 0;
  background: var(--md-code-bg-color);
}

.fn-card > h3:first-child,
.fn-card > h4:first-child {
  margin-top: 0;
}

.fn-card + .fn-card {
  margin-top: 1.6em;
}

/* Overload divider: a labeled break between overloads in one fn-card */
.overload-divider {
  display: block;
  font-size: 0.72em;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--md-default-fg-color--light);
  border-top: 1px solid var(--md-default-fg-color--lightest);
  padding-top: 0.8em;
  margin-top: 1.2em;
}

/* Prose sub-section label (Examples/Notes/References inside a docstring
   body that mojo doc leaves as plain text rather than a structured field) */
.prose-label {
  display: block;
  font-size: 0.72em;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--md-primary-fg-color);
  margin-top: 1.4em;
  margin-bottom: 0.5em;
}

/* Buttons */
.md-typeset .md-button {
  border-radius: 6px;
  font-weight: 600;
}

/* Tables */
.md-typeset table:not([class]) {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 6px;
  overflow: hidden;
}

.md-typeset table:not([class]) th {
  background: var(--md-default-fg-color--lightest);
  font-weight: 600;
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



def extract_readme_section(readme_text: str, heading: str) -> str:
    """Return the body of a top-level (##) section from README.MD, up to
    (but not including) the next top-level heading. `heading` is matched
    exactly against the text after '## '.
    """
    lines = readme_text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == f"## {heading}":
            start = i + 1
            break
    if start is None:
        raise ValueError(f"README.MD has no '## {heading}' section")
    end = len(lines)
    for i in range(start, len(lines)):
        if lines[i].startswith("## "):
            end = i
            break
    body = "\n".join(lines[start:end]).strip("\n")
    # README examples use `def main() raises:`, matching current Mojo syntax
    # already, so no rewriting needed there. Demote any `### ` headings by
    # one level isn't necessary since README already starts sections at ###.
    return body


def write_getting_started():
    GETTING_STARTED.parent.mkdir(parents=True, exist_ok=True)
    readme_text = README_SRC.read_text(encoding="utf-8")

    usage = extract_readme_section(readme_text, "Usage")
    quickstart_md = (
        "# Quickstart\n\n"
        "This guide gets a first NuMojo program running in a couple of "
        "minutes. See [Installation](install.md) for all the ways to add "
        "NuMojo to a project.\n\n"
        f"{usage}\n\n"
        "## Next steps\n\n"
        "- Browse available functions by topic in the "
        "[User Guide](../user-guide/overview.md).\n"
        "- Look up any function's full signature and docstring in the "
        "[API Reference](../API reference/numojo/index.md).\n"
    )
    (GETTING_STARTED.parent / "quickstart.md").write_text(
        quickstart_md, encoding="utf-8"
    )

    installation = extract_readme_section(readme_text, "Installation")
    install_md = f"# Installation\n\n{installation}\n"
    GETTING_STARTED.write_text(install_md, encoding="utf-8")


def copy_docs_pages(docs_dir: Path):
    mapping = {
        DOCS_SRC / "developer-guide" / "architecture.md": docs_dir
        / "developer-guide"
        / "architecture.md",
        DOCS_SRC / "developer-guide" / "ndarray-basic-structure.md": docs_dir
        / "developer-guide"
        / "ndarray-basic-structure.md",
        DOCS_SRC / "developer-guide" / "style-guide.md": docs_dir
        / "developer-guide"
        / "style-guide.md",
        DOCS_SRC / "developer-guide" / "contributing.md": docs_dir
        / "developer-guide"
        / "contributing.md",
        DOCS_SRC / "developer-guide" / "pre-pr-checks.md": docs_dir
        / "developer-guide"
        / "pre-pr-checks.md",
        DOCS_SRC / "user-guide" / "features.md": docs_dir
        / "user-guide"
        / "overview.md",
        DOCS_SRC / "user-guide" / "roadmap.md": docs_dir
        / "user-guide"
        / "roadmap.md",
        DOCS_SRC / "user-guide" / "changelog.md": docs_dir
        / "user-guide"
        / "changelog.md",
    }
    # Links in the source docs are relative to their location in the NuMojo
    # repo; rewrite the ones that don't resolve from the docs site.
    link_rewrites = {
        DOCS_SRC
        / "user-guide"
        / "features.md": [
            (
                "[here](../../numojo/__init__.mojo)",
                "[here](https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo/blob/main/numojo/__init__.mojo)",
            ),
            (
                "see `roadmap.md`",
                "see the [Roadmap](../user-guide/roadmap.md)",
            ),
        ],
    }

    for src, dst in mapping.items():
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            text = src.read_text(encoding="utf-8")
            for old, new in link_rewrites.get(src, []):
                text = text.replace(old, new)
            dst.write_text(text, encoding="utf-8")
            print(f"  copied {src.name} -> {dst}")
        else:
            print(f"  WARNING: source not found: {src}")


INDEX_MD = """\
---
hide:
  - navigation
  - toc
---

<div style="text-align:center; margin-top: 1em;">
<img src="https://raw.githubusercontent.com/Mojo-Numerics-and-Algorithms-group/NuMojo/main/assets/numojo_logo_360x360.png" alt="NuMojo logo" width="160">

<h1 style="border:none; margin:0.4em 0 0;">NuMojo</h1>

<p style="font-size:1.2em">
A library for numerical computing in <strong>Mojo 🔥</strong>, similar to NumPy in Python.
</p>
</div>

<div style="margin: 1.5em 0; display:flex; gap:0.7em; flex-wrap:wrap; justify-content:center;">
<a href="getting_started/quickstart/" class="md-button md-button--primary">Quickstart →</a>
<a href="getting_started/install/" class="md-button">Installation</a>
<a href="API reference/numojo/" class="md-button">API Reference</a>
<a href="https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo" class="md-button">GitHub</a>
<a href="https://discord.gg/NcnSH5n26F" class="md-button">Discord</a>
</div>

---

## What is NuMojo?

NuMojo aims to encompass the extensive numerics capabilities found in NumPy. We seek to harness the
full potential of Mojo, including vectorization, parallelization, and GPU acceleration — currently,
NuMojo extends most (if not all) standard library math functions to support array inputs.

Our vision for NuMojo is to serve as a familiar and essential building block for other Mojo libraries
needing fast math operations, without the additional weight of a machine learning back-propagation
system.

---

## Why NuMojo

- **Native to Mojo.** NuMojo's `NDArray` is a Mojo-native SIMD-backed type, not a binding around
  NumPy or MAX's tensor types, so it compiles into your program with no Python interop overhead.
- **NumPy-familiar API.** Slicing, broadcasting, `@` for matrix multiplication, and function names
  mirror NumPy where it makes sense, so existing intuition carries over.
- **Built for Mojo's strengths.** Vectorization and parallelism are used throughout the routines,
  with GPU and other accelerator support (`AcceleratorNDArray`) landing as Mojo's own device support
  matures.

---

## Core types

| Type | Description |
|------|-------------|
| `NDArray` | General-purpose N-dimensional array for tensors, grids, batches |
| `ComplexNDArray` | N-dimensional array of complex numbers |

---

## Highlights

=== "NDArray"

    ```mojo
    import numojo as nm
    from numojo.prelude import *

    def main() raises:
        var A = nm.random.randn(Shape(1000, 1000))
        var B = nm.random.randn(Shape(1000, 1000))
        var C = A @ B
        var I = nm.inv(A)
        var s = A[1:3, 4:19]
        print(nm.sum(A))
        print(nm.solve(A, B))
    ```

=== "ComplexNDArray"

    ```mojo
    import numojo as nm
    from numojo.prelude import *

    def main() raises:
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
- **Linear algebra** — `matmul`, `inv`, `solve`, `det`, `trace`, `lu_decomposition`, …
- **Logic** — `all`, `any`, comparison, logical ops, …
- **Statistics** — `mean`, `std`, `var`, `sum`, `prod`, `min`, `max`, …
- **Sorting & searching** — `sort`, `argsort`, `argmin`, `argmax`, …
- **I/O** — file read/write, formatting, …

See the [User Guide](user-guide/overview.md) for the full list linked to the [API Reference](API reference/numojo/index.md).

---

## Installation

The fastest way to get started, for a pinned stable release:

```toml
[workspace]
channels = ["https://repo.prefix.dev/modular-community"]

[dependencies]
numojo = "=0.10.0"
```

```bash
pixi install
```

See the [full installation guide](getting_started/install.md) for all methods,
including tracking the latest development branch.

---

## Version compatibility

| NuMojo | Mojo |
|--------|------|
| v0.10.0 | ==1.0.0 |
| v0.9.0 | ==26.2 |
| v0.8.0 | ==25.7 |
| v0.7.0 | ==25.3 |
| v0.6.1 | ==25.2 |

---

## Learn more

- [Roadmap](user-guide/roadmap.md) — planned work and long-term direction.
- [Changelog](user-guide/changelog.md) — released changes by version.
- [Contributing](developer-guide/contributing.md) — how to get involved.

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

    # Clear previously generated getting-started/user-guide/developer-guide
    # pages so pages removed from the source docs don't linger as orphans.
    for stale_dir in ("getting_started", "user-guide", "developer-guide"):
        stale_path = docs_dir / stale_dir
        if stale_path.exists():
            shutil.rmtree(stale_path)

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
