from __future__ import annotations

from .contract import CONTRACT, QUEUE
from .validate import assert_valid


def summary() -> dict:
    assert_valid()
    return {
        "id": CONTRACT["id"],
        "claim_cap": CONTRACT["claim_cap"],
        "shared_algebra": list(CONTRACT["shared_algebra"]),
        "sunder_method_count": len(CONTRACT["sunder_methods"]),
        "identities_distinct": CONTRACT["identities_distinct"],
        "queue": QUEUE,
        "forbidden": list(CONTRACT["forbidden_claims"]),
    }


def main() -> None:
    s = summary()
    print(f"{s['id']} cap={s['claim_cap']} algebra={s['shared_algebra']}")
    for q in s["queue"]:
        print(f"{q['id']} {q['status']} {q['name']}")


if __name__ == "__main__":
    main()
