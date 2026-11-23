<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2026-07-11","topics":["testing","maintainability","complexity","review","protocol","compiler","scope"],"limitations":"Static review of linked primary sources and bundled historical analyses; upstream tests were not executed. Historical claims and code changes are distinguished from proven runtime outcomes."} -->
# Bedrock protocol compiler: cut an over-general initial scaffold to the actual consumer {#case}

## Immediate reduction {#changes}

Maintainer wu-vincent initially imported a broad protocol compiler in [8a871ab8](https://github.com/EndstoneMC/bedrock-protocol/commit/8a871ab833476c6a6fd0a623945a2af3f6c94c24) (38 files; 6,004 additions). The first concrete consumer exercised only the `AttributeLayerSync` closure, but the parser also carried speculative nested enums, predicates, maps, bitsets, redeclaration and special serialization machinery, including unsupported or incomplete combinations.

The immediate [rewrite 3ddd4d80](https://github.com/EndstoneMC/bedrock-protocol/commit/3ddd4d80092450b68787de8f3743dda9a82d0871) changed 15 files, **+796/−3,032 lines**, removing broad unneeded support and adopting a narrower protoc-like field generator. The commit reports a compiler shrink from roughly 4,500 to 2,300 lines and passing historical golden/downstream tests. Bundled per-commit analyses independently inspected the diffs, but did not run those tests.

## Judgment and counterexample {#reading}

Build the smallest sound implementation for known consumers, rather than implementing an assumed future language ecosystem. Historical support for some removed features was later reintroduced when concrete packet demand appeared: this is **not** evidence that all removed functionality was useless forever. A generic extension becomes justified when a real consumer needs it.

## Limits {#limits}

The scaffold was a broad starting point, not a proven fully working general compiler. Removing unsupported branches can reduce test matrix growth, but the diff alone does not measure defect rate. Further detailed analyses are available at [0001-8a871ab83347.md](../../sources/commit-review/bedrock-protocol-0001-0076/dossiers/0001-8a871ab83347.md) and [0002-3ddd4d800924.md](../../sources/commit-review/bedrock-protocol-0001-0076/dossiers/0002-3ddd4d800924.md).
