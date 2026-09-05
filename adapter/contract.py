"""Deterministic mapping. Does not execute foreign packages."""

from __future__ import annotations

from .surfaces import (
    CLEANROOM_VSA,
    FORBIDDEN_CLAIMS,
    SHARED_ALGEBRA,
    SNAPSHOT_DATE,
    SUNDER_VSA,
)

SURFACES = {
    "sunder": SUNDER_VSA,
    "sovereign-clean-room": CLEANROOM_VSA,
}

CONTRACT = {
    "id": "Q-FUNC-002",
    "name": "sunder-cleanroom-vsa-adapter",
    "snapshot_date": SNAPSHOT_DATE,
    "claim_cap": "MODULE_SURFACE",
    "shared_algebra": SHARED_ALGEBRA,
    "sunder_methods": SUNDER_VSA["symbols"]["methods"],
    "mapping": {
        "bind": {"sunder": "VSAMemory.bind", "cleanroom": "expected bind (unaudited AST)"},
        "unbind": {"sunder": "VSAMemory.unbind", "cleanroom": "expected unbind (unaudited AST)"},
        "similarity": {
            "sunder": "VSAMemory.similarity",
            "cleanroom": "expected similarity (unaudited AST)",
        },
    },
    "identities_distinct": True,
    "supersedes": None,
    "forbidden_claims": FORBIDDEN_CLAIMS,
}

QUEUE = [
    {
        "id": "Q-FUNC-002",
        "name": "sunder-cleanroom-vsa-adapter",
        "status": "THIS_REPO",
        "reason": "Wire a claim-capped surface map; do not import either tree.",
    },
    {
        "id": "Q-FUNC-003",
        "name": "seem-identity-unifier",
        "status": "NOT_BUILT",
        "reason": "Three SEEM microservice identities; no SUPERSEDES proof.",
    },
    {
        "id": "Q-FUNC-004",
        "name": "os-constitution-merge",
        "status": "NOT_BUILT",
        "reason": "Sovereign-OS / SovereignOS / LegionOS / RealityOS unmerged.",
    },
    {
        "id": "Q-FUNC-005",
        "name": "workforce-lineage-graph",
        "status": "NOT_BUILT",
        "reason": "Digital Double variants lack typed SUPERSEDES edges.",
    },
]
