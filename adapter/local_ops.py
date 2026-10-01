"""Local-definition witness for contract-only algebra names.

This module does not implement bind, unbind, similarity, register, or query.
Those names are surface-contract strings owned by other repositories.
A2: absence is checked by AST of this package only.
"""

from __future__ import annotations

import ast
from pathlib import Path

CONTRACT_ONLY_OPS = (
    "bind",
    "unbind",
    "similarity",
    "register",
    "query",
)

STATUS = "CONTRACT_ONLY_NOT_LOCAL_DEFS"


def adapter_function_defs(root: Path | None = None) -> dict[str, list[str]]:
    """Return {relative path: function def names} for adapter/*.py."""
    base = root or Path(__file__).resolve().parent
    found: dict[str, list[str]] = {}
    for path in sorted(base.glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        names = [
            node.name
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]
        found[path.name] = names
    return found


def contract_ops_defined_locally(root: Path | None = None) -> list[str]:
    """Names in CONTRACT_ONLY_OPS that appear as top-level function defs."""
    hits: list[str] = []
    for filename, names in adapter_function_defs(root).items():
        for name in names:
            if name in CONTRACT_ONLY_OPS:
                hits.append(f"{filename}:{name}")
    return hits
