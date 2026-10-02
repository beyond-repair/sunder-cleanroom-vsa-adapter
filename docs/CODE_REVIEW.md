# Code review checklist — Q-FUNC-002

Reviewer: `python -m adapter` + pytest (deterministic). Not a live import of either VSA package.

- [x] Claim cap is MODULE_SURFACE, not runtime interop
- [x] sunder/vsa.py methods locked from tip c7d4596 (8 methods, dim=4096)
- [x] clean-room names observed on tip 4878918; type stays NAME_SNAPSHOT_NOT_ISOMORPHISM
- [x] Prior unaudited label and size 16828 kept; refreshed size is 17740
- [x] Default dims differ (4096 vs 8192) and default_dim_equivalence is forbidden
- [x] bind/unbind/similarity map as NAME_ONLY; register/query stay unmapped
- [x] No SUPERSEDES edge between identities
- [x] Queue retains Q-FUNC-003/004/005 as NOT_BUILT
- [x] No local def of bind, unbind, similarity, register, or query
- [x] Do not raise the cap to isomorphism or agent interop

Verdict: PASS under the claim contract. This is not a mind and not a shared vector space.
