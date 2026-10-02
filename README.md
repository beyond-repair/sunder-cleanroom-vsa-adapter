<div align="center">

[![Lifecycle](https://img.shields.io/badge/●_RESEARCH-a855f7?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/Claim_≤1-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)

```
LIFECYCLE   RESEARCH
CLAIM       ≤1
NOT CLAIMED thrust · energy extraction · AGI · production autonomy · runtime VSA interop
```

</div>

---

# sunder-cleanroom-vsa-adapter

Claim-capped **name-only surface contract** (v0.1.1) between:

- `sunder` `sunder/vsa.py` — class `VSAMemory`, `DEFAULT_DIM = 4096` (locked at `c7d4596`)
- `sovereign-clean-room` `core/clean_room_vsa.py` — class `CleanRoomVSAEngine`, `DEFAULT_DIM = 8192` (names locked at `4878918`)

This repository closes queue item **Q-FUNC-002** from `adl-function-census`.

It does **not** import either package, bind vectors, or prove the algebras match. The useful fact in the contract is the mismatch: the shared names `bind`, `unbind`, and `similarity` are mapped as `NAME_ONLY`, and the default dimensions are **4096 ≠ 8192**. `register` and `query` appear as names on both classes and stay **unmapped**.

## Claim contract

| Claimed | Not claimed |
|---|---|
| Locked paths, classes, and method names on the commits above | Runtime import of either package |
| Shared names bind, unbind, similarity as NAME_ONLY | Local implementations of those names |
| Default dims differ (4096 vs 8192) | Vector-space isomorphism or equal codebook seeds |
| register/query exist on both and are not in the mapping | Those operations mean the same thing |
| Deterministic checker (`python -m adapter`) | A mind, an autonomous coder, or a cross-repo agent |

Claim cap: **MODULE_SURFACE**.

`adapter/local_ops.py` treats `bind`, `unbind`, `similarity`, `register`, and `query` as contract-only strings. Tests fail if any of those names is added as a top-level function in `adapter/`.

The 2026-09-05 lock called the clean-room file `TREE_PRESENT_FUNCTIONS_UNAUDITED` at 16828 bytes. The 2026-10-02 name pass records class and algebra names at 17740 bytes and does not delete that prior label.

## Install and run

Python 3.11+. From a fresh clone of the default branch:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m adapter
python -m pytest -q
```

`python -m adapter` (same as `python -m adapter.engine`) prints the contract and `OK`, then exits 0. A drifted contract prints `FAIL` and exits 1.

No configuration file. Nothing here talks to the network.

## Related

- `sunder`, `sovereign-clean-room` (not dependencies of this package)
- `adl-function-census` Q-FUNC-002
- `adl-capability-matrix` Q-003 (broader SEEM-sunder bridge — still queued)
- `ADL-Governance`, `forge-aegis`

---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

Governing source: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>
