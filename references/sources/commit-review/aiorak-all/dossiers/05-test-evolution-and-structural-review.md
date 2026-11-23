<!-- retrieval: {"source_ids":["public:commit:02518a3c358b1b35bb14d1c7df56583750bde3f4","public:commit:03a7726369f34e97f27d784dfe527c1f7b586d1e","public:commit:0473a92d9d3a8fc5a7678b1899561612a801227c","public:commit:1078d7dbe490219f0b28b2d858fb2353b3918b83","public:commit:1647e1fbd8c1df12a183e63f8dd20e1a27f8116e","public:commit:1677a238e022d4880a95ee2012e6c4439b8d0ab8","public:commit:172c5b0a34c908df2d9a227ad5f71a499d9c413d","public:commit:2134ab6df587a48bb7a9df96d7382253fc5c60a8","public:commit:25456e7f42be8dfd47d68846104add4e585e503a","public:commit:2961f488270fd02b1c356ef3cc3dbe975399f8b0","public:commit:50aec9bb903521392fd9018b18717426b98115a0","public:commit:862190c1e17dfc86cd674fe07ec688176c6474ff","public:commit:89db6e3ec40f8cfa0b555b18c10e293f1b6029d0","public:commit:8d5e18e56b169a588d603acb88dedeaf7cd44339","public:commit:9c132d11bf6e20b9e0a934cab6f2ac5dbf72f1ba","public:commit:a83e4b876d6a9ff3c2a1f13e57f227b51e9582c6","public:commit:b16084f41d35b2cbaa5b87d5d20fc70387d19d5f","public:commit:bff4439e9b3c3c4a5293dea7f632492d7cd77b25","public:commit:c8d0df3af20b13d3d520c1ae718a6e0256f8a2fd","public:commit:d3edff38b025138bd293429a1e7647810a50a767","public:commit:de96971f365ac781cbd33aeaa382764f39ec96b8","public:commit:f834416e171bd5fbc2e0f558146c925b33cb55d5","public:commit:fd290406d2a6d3763a54748c5c166d5369722470"],"source_type":"public","date":"2023-12-11..2026-03-17","topics":["testing","build","performance","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="test-evolution-bulk-verification-and-oracle-strength"></a>
# Test evolution, bulk verification and oracle strength {#test-evolution-bulk-verification-and-oracle-strength}

## Initial breadth and limits {#initial-breadth-and-limits}

[051 · d3edff38b025](../commits/051-d3edff38b025.md) adds unit tests, loopback client/server integration, large packets, ordering, connection churn and throughput scenarios. This is substantial test investment. It is not independent interoperability evidence: the client/server share the same implementation, and paired encoders/decoders can agree on incorrect wire values. Some stress cases catch broad exceptions or accept weak count conditions. The later byte-order repair [058 · 25456e7f42be](../commits/058-25456e7f42be.md) is a concrete counterexample to equating broad coverage with external correctness.

[053 · 02518a3c358b](../commits/053-02518a3c358b.md) updates tests for handlers and streams rather than Event polling. [054 · 8d5e18e56b16](../commits/054-8d5e18e56b16.md) adds graceful-close scenarios. The old bodies and causal parents were read alongside the replacement additions. The linked public commits and bundled notes provide the inspectable source; the working blob-comparison inventory is not distributed with the Skill. These are meaningful API/test changes, not proof of equivalence from similar names.

## First major consolidation changes what is asserted {#first-major-consolidation-changes-what-is-asserted}

[055 · de96971f365a](../commits/055-de96971f365a.md) consolidates tests into C++ sample-inspired scenario groups and adds pytest-xdist. Complete additions and old ancestor bodies were examined, with removed paths independently verified. Several changes strengthen coverage: 32 channels with 50 messages and varied padding, reliable/ordered size exploration, and an eight-peer fanout scenario. Others weaken the oracle:

- The large 5 MB transfer checks length rather than the earlier cryptographic content digest. Same-length corruption becomes less observable.
- The throughput scenario changes from a minimum-rate assertion to paced sending around 100 packets per second for three seconds with 400-byte data and printed observations. It no longer asserts the old 500 KB/s floor.
- Randomized stress catches broad errors, so surviving the loop need not mean every intended operation succeeded.
- Timeout markers in this configuration are registered marker metadata; without an enforcing plugin they are not evidence that pytest will interrupt a hung test.

These are costs and tradeoffs, not necessarily mistakes. Lower-flakiness scenarios may be reasonable, but the commit text does not authorize inventing that motive. Retain the observable oracle changes and distinguish them from an explicit rationale.

[056 · 0473a92d9d3a](../commits/056-0473a92d9d3a.md) adjusts Windows abrupt-close handling and waits for both established and pending maps to clear before reconnecting. Its message reports platform failures; this review has not independently reproduced them. [057 · c8d0df3af20b](../commits/057-c8d0df3af20b.md) removes a now-unused helper.

## Coverage-oriented additions {#coverage-oriented-additions}

[092 · 172c5b0a34c9](../commits/092-172c5b0a34c9.md) adds unit branch cases, mocked transport/platform paths and loopback scenarios. Some assert exact frame/state outcomes; others mainly execute a line. A test named for duplicate/noise ping still performs normal ping rather than inducing those conditions. Message-reported coverage rises from 89% to 98%, but no coverage run was performed here.

[094 · 1677a238e022](../commits/094-1677a238e022.md) adds malformed OCR/ping raw UDP, optional parameters, context/properties, GUID duplication, broadcast exclusion and handler failure. Observing no reply does not establish that an event-loop callback did not raise internally. The handler-log scenario does not inspect caplog despite its name. Capacity tests do not exhaust pending OCR2 allocation. These limits matter when interpreting both the percentage and the names.

<a id="the-8-033-line-reorganization-reviewed-through-structure-and-deltas"></a>
## The 8,033-line reorganization: reviewed through structure and deltas {#the-8-033-line-reorganization-reviewed-through-structure-and-deltas}

[095 · b16084f41d35](../commits/095-b16084f41d35.md) says it consolidates 28 test modules into 13, removes duplicates and maintains 98% coverage with 267 tests instead of 277. The large patch is not falsely credited as 8,033 lines of fresh logic. The static review used the complete before/after test trees:

1. All changed paths and before/after blob SHA-256 values were recorded.
2. AST comparison preserves function arguments, decorators and executable nodes. It normalizes only the function's own name and standalone string-expression nodes, including docstrings. Normalization is not a claim that discarded documentation is irrelevant; documentation and module context were read separately.
3. There are 314 function/method definitions before and 293 after when nested function bodies are part of their enclosing AST. Of the 293 new definitions, 174 match an old normalized AST exactly. All 119 unmatched new residuals were manually read against their nearest old function. All old functions not covered by exact identity were examined against the before/after source trees; the working AST mapping and removed-function listing are not bundled.
4. All module-level imports, fixtures/globals and pytest marks were read. The 252 new or changed standalone string expressions/docstrings were also enumerated and read; descriptions are treated as claims, especially the stale culling descriptions. Class bases, decorators, attributes and parametrization context were checked separately. The two parameterizations are preserved: three burst sizes and seven message-size strides.
5. Static `test_` definitions count 269 before and 259 after. Adding the parameterization expansions gives 277 and 267, consistent with the message. This is source arithmetic, not actual pytest collection or a measured coverage result.
6. The test-module claim excludes supporting Python files: the whole tests tree has 30 Python modules before and 15 after, including package/helper files.

This verification supports comprehensive review of moved/changed content; it does not establish behavior preservation. The residuals reveal material changes:

- The eight-peer test still records per-sender/per-receiver sequences but now asserts only total delivery of 5,600 messages. It removes explicit no-self-delivery, per-pair count of 100, and strictly increasing per-pair sequence assertions. A correct total can coexist with misdistribution or ordering failure.
- Abrupt-disconnect cleanup still waits for maps with a timeout and asserts zero peers, but removes a final exact zero-pending-connections assertion.
- Cross-simultaneous-connect removes exact server peer-count checks. Cross-cycle testing loses explicit server-received-payload assertions, although echo checks still remain.
- Reliable/unreliable throughput scenarios lose per-packet length checks and printed rates. The ordered scenario retains size/order checks.
- Receive-window testing loses one additional below-base assertion.
- The combined stress module receives a module-level slow marker, affecting selection by `-m 'not slow'`.
- A zero-data-length frame test is improved by padding enough to reach the intended branch. A separate minimum-size test and a datagram-history-eviction case are added.
- Some removed definitions are genuine duplicate helpers or overlapping simple context/repr/ping/close cases; those do not count as independent lost capabilities.

Consequently the phrase “coverage maintained” must stay attributed. Even if independently confirmed numerically, coverage percentage would not imply the removed properties were preserved. The [095 public commit](https://github.com/wu-vincent/aiorak/commit/b16084f41d35b2cbaa5b87d5d20fc70387d19d5f) and its parent are the available primary evidence for rechecking these changes. The working AST mapping, residual text and removed-function listing are not distributed, so the static-review counts above are not independently rerunnable from this Skill.

## Formatting bulk was also verified, not guessed {#formatting-bulk-was-also-verified-not-guessed}

[062 · f834416e171b](../commits/062-f834416e171b.md) changes 31 files. Full-module AST comparison after removing standalone string-expression nodes shows 21 unchanged executable ASTs. The ten residuals are unused/reordered imports or a constant f-string simplification, and all residuals were read. Python imports can have side effects in general, so this is described as local cleanup with inspected residuals, not an unrestricted proof that import reordering never changes semantics.

## Final testing limits and next verification targets {#final-testing-limits-and-next-verification-targets}

[096 · 1647e1fbd8c1](../commits/096-1647e1fbd8c1.md) introduces new resource bounds and stricter types/CI but changes no test file. Two stale unreliable-culling tests remain despite dead-code removal: one checks only that sending emptied the queue, and the mixed-entry case has no outcome assertion. No upstream test, benchmark, mypy, Ruff, build, package install or CI workflow was run. Assertions about platform success, throughput, all tests passing or exact coverage remain source claims unless separately supported.

For future behavior-preserving refactors, inventory properties rather than just test names: content identity, ordering, per-peer distribution, resource disposal, saturation admission and failure signals. Hashes/AST matching are excellent tools for proving which bodies moved; they are insufficient to show that fixtures, scheduling, markers, decorators, imports and removed assertions preserve the same contract. That synthesis is grounded in the observable deltas here.
