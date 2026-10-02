from adapter.contract import CONTRACT, QUEUE
from adapter.engine import main, summary
from adapter.surfaces import CLEANROOM_VSA, SHARED_ALGEBRA, SUNDER_VSA
from adapter.validate import validate


def test_valid():
    assert validate() == []


def test_sunder_surface_locked():
    assert SUNDER_VSA["path"] == "sunder/vsa.py"
    assert SUNDER_VSA["symbols"]["class"] == "VSAMemory"
    assert SUNDER_VSA["symbols"]["DEFAULT_DIM"] == 4096
    assert SUNDER_VSA["commit"].startswith("c7d4596")
    for op in SHARED_ALGEBRA:
        assert op in SUNDER_VSA["symbols"]["methods"]


def test_cleanroom_name_snapshot_not_isomorphism():
    assert CLEANROOM_VSA["type"] == "NAME_SNAPSHOT_NOT_ISOMORPHISM"
    assert CLEANROOM_VSA["prior_type"] == "TREE_PRESENT_FUNCTIONS_UNAUDITED"
    assert CLEANROOM_VSA["path"] == "core/clean_room_vsa.py"
    assert CLEANROOM_VSA["class"] == "CleanRoomVSAEngine"
    assert CLEANROOM_VSA["default_dim"] == 8192
    assert CLEANROOM_VSA["size_bytes"] == 17740
    assert CLEANROOM_VSA["prior_size_bytes"] == 16828
    assert CLEANROOM_VSA["commit"].startswith("4878918")


def test_dim_mismatch_is_the_contract():
    assert CONTRACT["dims"]["sunder"] == 4096
    assert CONTRACT["dims"]["cleanroom"] == 8192
    assert CONTRACT["dims"]["equal"] is False
    assert "default_dim_equivalence" in CONTRACT["forbidden_claims"]
    for op in SHARED_ALGEBRA:
        assert CONTRACT["mapping"][op]["equivalence"] == "NAME_ONLY"


def test_register_and_query_stay_unmapped():
    assert CONTRACT["unmapped_shared_names"] == ("register", "query")
    assert "register" not in CONTRACT["mapping"]
    assert "query" not in CONTRACT["mapping"]


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


def test_summary_and_main():
    report = summary()
    assert report["ok"] is True
    assert report["claim_cap"] == "MODULE_SURFACE"
    assert report["sunder_method_count"] == 8
    assert report["dim_mismatch"] is True
    assert report["version"] == "0.1.1"
    assert main() == 0
