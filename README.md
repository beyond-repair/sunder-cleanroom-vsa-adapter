# sunder-cleanroom-vsa-adapter

Claim-capped **surface contract** between:

- `sunder/vsa.py` (`VSAMemory`: bind, unbind, similarity, register, query)
- `sovereign-clean-room/core/clean_room_vsa.py` (FHRR / BaNEL VSA core; tree present, functions not fully audited here)

This repository closes queue item **Q-FUNC-002** from `adl-function-census`.

## Claim contract

| Claimed | Not claimed |
|---|---|
| Both trees exist on default branch as of 2026-09-04/05 | Runtime import of either package |
| Shared algebraic surface: bind, unbind, similarity, register/query | Vector-space isomorphism of implementations |
| Deterministic adapter mapping + tests | Working autonomous agent across repos |
| Distinct identities (no SUPERSEDES) | Equivalence of codebook seeds or dim |

Claim cap of this repo: **MODULE_SURFACE**.

## Run

```bash
pip install -r requirements.txt
python -m adapter.engine
python -m pytest -q
```

## Related

- `sunder`, `sovereign-clean-room`
- `adl-function-census` Q-FUNC-002
- `adl-capability-matrix` Q-003 (broader SEEM-sunder bridge — still queued)
- `ADL-Governance`, `forge-aegis`
