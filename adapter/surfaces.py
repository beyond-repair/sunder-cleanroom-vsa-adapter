"""Locked name-only surfaces. Does not import sunder or sovereign-clean-room.

Original lock: 2026-09-05 (clean-room file present, functions unaudited).
Name pass: 2026-10-02 on the default-branch tips below. Dims differ.
"""

from __future__ import annotations

VERSION = "0.1.1"
SNAPSHOT_DATE = "2026-09-05"
OBSERVED_DATE = "2026-10-02"

SUNDER_VSA = {
    "repo": "sunder",
    "path": "sunder/vsa.py",
    "commit": "c7d4596c13b8aa0e672b40db94edc6655512b385",
    "blob_sha": "584190696218d2ccf3146c4ecfd427f92a060980",
    "type": "MODULE_SURFACE",
    "default_dim": 4096,
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
    "notes": "FHRR unit-complex bind = Hadamard product; unbind = conj multiply. Not imported here.",
}

CLEANROOM_VSA = {
    "repo": "sovereign-clean-room",
    "path": "core/clean_room_vsa.py",
    "commit": "4878918cf9f95d3c19e1890bef6d2fd6713e0a16",
    "blob_sha": "b086ae84d397415716b16cd9b36c2c15c624ad46",
    "type": "NAME_SNAPSHOT_NOT_ISOMORPHISM",
    "prior_type": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
    "size_bytes": 17740,
    "prior_size_bytes": 16828,
    "class": "CleanRoomVSAEngine",
    "default_dim": 8192,
    "expected_algebra": ("bind", "unbind", "similarity"),
    "name_only_methods": ("bind", "unbind", "similarity", "register", "query"),
    "notes": (
        "Names only, observed 2026-10-02. Not imported. "
        "DEFAULT_DIM 8192 is not sunder 4096. "
        "similarity() is not the protocol cosine-sum invertibility."
    ),
}

SHARED_ALGEBRA = ("bind", "unbind", "similarity")

# Present as names on both classes. Not in the shared mapping: this repo
# does not claim register/query mean the same thing on both sides.
UNMAPPED_SHARED_NAMES = ("register", "query")

FORBIDDEN_CLAIMS = (
    "runtime_import_of_sunder",
    "runtime_import_of_clean_room_vsa",
    "vector_isomorphism_proven",
    "agent_cross_repo_works",
    "codebook_seed_equivalence",
    "default_dim_equivalence",
)
