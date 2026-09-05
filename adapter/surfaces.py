"""Locked module surfaces observed on default branches (2026-09-04/05).

A2: paths and method names taken from GitHub tree + sunder/vsa.py source.
A4: clean-room VSA methods listed as TREE_PRESENT — not AST-complete.
"""

from __future__ import annotations

SNAPSHOT_DATE = "2026-09-05"

SUNDER_VSA = {
    "repo": "sunder",
    "path": "sunder/vsa.py",
    "type": "MODULE_SURFACE",
    "symbols": {
        "DEFAULT_DIM": 4096,
        "class": "VSAMemory",
        "methods": (
            "bind",
            "unbind",
            "similarity",
            "register",
            "get",
            "query",
            "remember_file",
            "stats",
        ),
    },
    "notes": "FHRR unit-complex bind = Hadamard product; unbind = conj multiply.",
}

CLEANROOM_VSA = {
    "repo": "sovereign-clean-room",
    "path": "core/clean_room_vsa.py",
    "type": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
    "size_bytes": 16828,
    "expected_algebra": ("bind", "unbind", "similarity"),
    "notes": "FHRR / BaNEL hyperspherical core; full AST not performed in this repo.",
}

SHARED_ALGEBRA = ("bind", "unbind", "similarity")

FORBIDDEN_CLAIMS = (
    "runtime_import_of_sunder",
    "runtime_import_of_clean_room_vsa",
    "vector_isomorphism_proven",
    "agent_cross_repo_works",
    "codebook_seed_equivalence",
)
