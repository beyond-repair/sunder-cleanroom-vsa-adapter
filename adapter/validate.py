from __future__ import annotations

from .contract import CONTRACT, QUEUE
from .surfaces import SHARED_ALGEBRA, SUNDER_VSA


def validate() -> list[str]:
    errors: list[str] = []
    if CONTRACT["claim_cap"] != "MODULE_SURFACE":
        errors.append("claim_cap drift")
    if CONTRACT["supersedes"] is not None:
        errors.append("must not claim SUPERSEDES")
    for op in SHARED_ALGEBRA:
        if op not in SUNDER_VSA["symbols"]["methods"]:
            errors.append(f"sunder missing {op}")
        if op not in CONTRACT["mapping"]:
            errors.append(f"mapping missing {op}")
    statuses = [q["status"] for q in QUEUE]
    if "THIS_REPO" not in statuses:
        errors.append("queue missing THIS_REPO")
    if "NOT_BUILT" not in statuses:
        errors.append("queue collapsed; remaining items lost")
    if "runtime_import_of_sunder" not in CONTRACT["forbidden_claims"]:
        errors.append("forbidden-claim registry incomplete")
    return errors


def assert_valid() -> None:
    errs = validate()
    if errs:
        raise AssertionError(errs)
