#!/usr/bin/env python3
"""Generate docs.json from a NuMojo checkout.

`mojo doc numojo/ -o docs.json` run as a single whole-package invocation
currently fails on this codebase: `mojo doc`'s cross-file type resolution
hits a false self-type-mismatch error when `core/accelerator_ndarray.mojo`
imports `core/ndarray.mojo` at the full-package level, even though the
real compiler (`pixi run package`) builds the same code cleanly and every
top-level member of `numojo/` documents fine on its own.

This script works around that by running `mojo doc` separately on each of
`numojo/`'s top-level members (`__init__.mojo`, `prelude.mojo`, `core/`,
`routines/`) and merging the resulting JSON into the same shape a single
`mojo doc numojo/ -o docs.json` would have produced: a top-level `numojo`
package `decl` with those four as its `modules`/`packages` children. Every
byte of the merged output still comes from the real `mojo doc` tool - this
only avoids the one buggy invocation shape, it does not parse or guess at
signatures itself.

If `numojo/`'s top-level layout changes (a member added/removed/renamed),
update TOP_LEVEL_MODULES / TOP_LEVEL_PACKAGES below to match.

Usage:
    python3 gen_docs_json.py /path/to/NuMojo
    python3 gen_docs_json.py /path/to/NuMojo -o docs.json
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

# numojo/*.mojo files to document as top-level modules.
TOP_LEVEL_MODULES = ["__init__.mojo", "prelude.mojo"]
# numojo/*/ directories to document as top-level packages.
TOP_LEVEL_PACKAGES = ["core", "routines"]


def run_mojo_doc(numojo_repo: Path, rel_path: str, out_path: Path) -> dict:
    cmd = ["pixi", "run", "mojo", "doc", rel_path, "-o", str(out_path)]
    result = subprocess.run(
        cmd, cwd=numojo_repo, capture_output=True, text=True
    )
    if result.returncode != 0:
        sys.stderr.write(f"mojo doc failed for {rel_path}:\n")
        sys.stderr.write(result.stdout)
        sys.stderr.write(result.stderr)
        raise SystemExit(1)
    with open(out_path, encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "numojo_repo", type=Path, help="Path to a NuMojo checkout"
    )
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("docs.json")
    )
    args = parser.parse_args()

    numojo_repo = args.numojo_repo.resolve()
    if not (numojo_repo / "numojo").is_dir():
        parser.error(f"{numojo_repo} does not look like a NuMojo checkout")

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        module_decls = []
        for name in TOP_LEVEL_MODULES:
            print(f"Documenting numojo/{name} ...")
            out = tmp_path / f"{name}.json"
            data = run_mojo_doc(numojo_repo, f"numojo/{name}", out)
            module_decls.append(data["decl"])
            version = data.get("version")

        package_decls = []
        for name in TOP_LEVEL_PACKAGES:
            print(f"Documenting numojo/{name}/ ...")
            out = tmp_path / f"{name}.json"
            data = run_mojo_doc(numojo_repo, f"numojo/{name}", out)
            package_decls.append(data["decl"])
            version = data.get("version")

    # numojo/__init__.mojo's own decl carries the package-level docstring
    # in a normal single-shot `mojo doc numojo/` run too, so reuse it here.
    init_decl = module_decls[0]
    merged = {
        "decl": {
            "kind": "package",
            "name": "numojo",
            "description": init_decl.get("description", ""),
            "summary": init_decl.get("summary", ""),
            "modules": module_decls,
            "packages": package_decls,
        },
        "version": version,
    }

    args.output.write_text(json.dumps(merged), encoding="utf-8")
    print(f"Wrote {args.output} ({args.output.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
