from adapter.contract import CONTRACT
from adapter.local_ops import (
    CONTRACT_ONLY_OPS,
    STATUS,
    contract_ops_defined_locally,
)


def test_contract_ops_are_not_local_defs():
    assert contract_ops_defined_locally() == []
    assert STATUS == "CONTRACT_ONLY_NOT_LOCAL_DEFS"


def test_contract_only_set_matches_bridge_gap():
    assert CONTRACT_ONLY_OPS == (
        "bind",
        "unbind",
        "similarity",
        "register",
        "query",
    )
    for op in ("bind", "unbind", "similarity"):
        assert op in CONTRACT["mapping"]
    assert "register" not in CONTRACT["mapping"]
    assert "query" not in CONTRACT["mapping"]
