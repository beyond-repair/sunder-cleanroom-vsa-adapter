from __future__ import annotations

from .contract import CONTRACT, QUEUE
from .local_ops import contract_ops_defined_locally
from .surfaces import CLEANROOM_VSA, SHARED_ALGEBRA, SUNDER_VSA


def validate() -> list[str]:
    errors: list[str] = []
    if CONTRACT["claim_cap"] != "MODULE_SURFACE":
        errors.append("claim_cap drift")
    if CONTRACT["version"] != "0.1.1":
        errors.append("version drift")
    if CONTRACT["supersedes"] is not None:
        errors.append("must not claim SUPERSEDES")
    if CONTRACT["dims"]["sunder"] != 4096 or SUNDER_VSA["default_dim"] != 4096:
        errors.append("sunder dim drift")
    if CONTRACT["dims"]["cleanroom"] != 8192 or CLEANROOM_VSA["default_dim"] != 8192:
        errors.append("cleanroom dim drift")
    if CONTRACT["dims"]["equal"] is not False:
        errors.append("dim mismatch witness collapsed")
    if CONTRACT["dims"]["sunder"] == CONTRACT["dims"]["cleanroom"]:
        errors.append("dims unexpectedly equal")
    if CLEANROOM_VSA["type"] != "NAME_SNAPSHOT_NOT_ISOMORPHISM":
        errors.append("cleanroom type overclaim")
    if CLEANROOM_VSA["prior_type"] != "TREE_PRESENT_FUNCTIONS_UNAUDITED":
        errors.append("prior unaudited type erased")
    if CLEANROOM_VSA["size_bytes"] == CLEANROOM_VSA["prior_size_bytes"]:
        errors.append("size refresh not recorded")
    if CLEANROOM_VSA["class"] != "CleanRoomVSAEngine":
        errors.append("cleanroom class drift")
    for op in SHARED_ALGEBRA:
        if op not in SUNDER_VSA["symbols"]["methods"]:
            errors.append(f"sunder missing {op}")
        if op not in CLEANROOM_VSA["name_only_methods"]:
            errors.append(f"cleanroom name missing {op}")
        entry = CONTRACT["mapping"].get(op)
        if not isinstance(entry, dict):
            errors.append(f"mapping missing {op}")
            continue
        if entry.get("equivalence") != "NAME_ONLY":
            errors.append(f"{op} equivalence overclaim")
    for name in CONTRACT["unmapped_shared_names"]:
        if name in CONTRACT["mapping"]:
            errors.append(f"{name} must stay unmapped")
        if name not in CLEANROOM_VSA["name_only_methods"]:
            errors.append(f"unmapped name {name} not observed")
    if contract_ops_defined_locally():
        errors.append("contract ops implemented locally")
    statuses = [q["status"] for q in QUEUE]
    if "THIS_REPO" not in statuses:
        errors.append("queue missing THIS_REPO")
    if "NOT_BUILT" not in statuses:
        errors.append("queue collapsed; remaining items lost")
    forbidden = CONTRACT["forbidden_claims"]
    for claim in (
        "runtime_import_of_sunder",
        "vector_isomorphism_proven",
        "default_dim_equivalence",
    ):
        if claim not in forbidden:
            errors.append(f"forbidden-claim registry incomplete: {claim}")
    return errors


def assert_valid() -> None:
    errs = validate()
    if errs:
        raise AssertionError(errs)
