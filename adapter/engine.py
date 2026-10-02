"""Print the locked surface contract. Does not import either VSA package."""

from __future__ import annotations

from .contract import CONTRACT, QUEUE
from .local_ops import STATUS
from .validate import validate


def summary() -> dict:
    errors = validate()
    dims = CONTRACT["dims"]
    return {
        "id": CONTRACT["id"],
        "version": CONTRACT["version"],
        "claim_cap": CONTRACT["claim_cap"],
        "shared_algebra": list(CONTRACT["shared_algebra"]),
        "sunder_method_count": len(CONTRACT["sunder_methods"]),
        "sunder_dim": dims["sunder"],
        "cleanroom_dim": dims["cleanroom"],
        "dim_mismatch": dims["equal"] is False and dims["sunder"] != dims["cleanroom"],
        "local_ops": STATUS,
        "identities_distinct": CONTRACT["identities_distinct"],
        "queue": QUEUE,
        "forbidden": list(CONTRACT["forbidden_claims"]),
        "errors": errors,
        "ok": not errors,
    }


def main() -> int:
    report = summary()
    print(
        f"{report['id']} v={report['version']} cap={report['claim_cap']} "
        f"algebra={report['shared_algebra']} "
        f"dim={report['sunder_dim']}/{report['cleanroom_dim']} "
        f"mismatch={str(report['dim_mismatch']).lower()} "
        f"local={report['local_ops']}"
    )
    for item in report["queue"]:
        print(f"{item['id']} {item['status']} {item['name']}")
    if report["errors"]:
        for err in report["errors"]:
            print(f"ERROR {err}")
        print("FAIL")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
