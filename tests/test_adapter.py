from adapter.contract import CONTRACT, QUEUE
from adapter.engine import summary
from adapter.surfaces import CLEANROOM_VSA, SHARED_ALGEBRA, SUNDER_VSA
from adapter.validate import validate


def test_valid():
    assert validate() == []


def test_sunder_surface_locked():
    assert SUNDER_VSA["path"] == "sunder/vsa.py"
    assert SUNDER_VSA["symbols"]["class"] == "VSAMemory"
    assert SUNDER_VSA["symbols"]["DEFAULT_DIM"] == 4096
    for op in SHARED_ALGEBRA:
        assert op in SUNDER_VSA["symbols"]["methods"]


def test_cleanroom_not_overclaimed():
    assert CLEANROOM_VSA["type"] == "TREE_PRESENT_FUNCTIONS_UNAUDITED"
    assert CLEANROOM_VSA["path"] == "core/clean_room_vsa.py"


def test_no_supersedes():
    assert CONTRACT["supersedes"] is None
    assert CONTRACT["identities_distinct"] is True


def test_queue_preserves_unbuilt():
    this = [q for q in QUEUE if q["status"] == "THIS_REPO"]
    rest = [q for q in QUEUE if q["status"] == "NOT_BUILT"]
    assert len(this) == 1
    assert this[0]["id"] == "Q-FUNC-002"
    assert len(rest) >= 3


def test_forbidden_runtime_import_claim():
    assert "runtime_import_of_sunder" in CONTRACT["forbidden_claims"]
    assert "vector_isomorphism_proven" in CONTRACT["forbidden_claims"]


def test_summary():
    s = summary()
    assert s["claim_cap"] == "MODULE_SURFACE"
    assert s["sunder_method_count"] == 8
