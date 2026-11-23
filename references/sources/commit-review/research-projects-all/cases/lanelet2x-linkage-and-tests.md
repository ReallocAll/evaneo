<!-- retrieval: {"source_ids":["public:commit:21674a16b150f80d92546989c37cc618e1b7a199","public:commit:24082b2faa9b1b945b64ee67b3c770f94073ec14","public:commit:7b3e7803faec7eaace96a568ba99f37c5673b3ea","public:commit:7cd5e3d1de2e7abb26ca02f344a24001057c2dde","public:commit:9a0296bcc405db769d80f01b977ef027c3c91347","public:commit:cdc4d6109a7cb2dda10f20af32bda013a5ad6e78","public:commit:fb3a3f6200da4b00665a9f22f3668ee39379b173"],"source_type":"public","date":"2023-11-19..2025-10-16","topics":["testing","build","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="lanelet2x-static-registries-compiler-repairs-and-test-invariants"></a>
# Lanelet2x: static registries, compiler repairs and test invariants {#lanelet2x-static-registries-compiler-repairs-and-test-invariants}

## The substantial implementation change {#the-substantial-implementation-change}

9a0296b moves built-in registrations from implementation translation units to the translation unit containing the corresponding factory. This affects regulatory elements, binary/OSM parsers and writers, German traffic rules, and validators. The algorithms themselves are not rewritten. [Public commit](https://github.com/wu-vincent/lanelet2x/commit/9a0296bcc405db769d80f01b977ef027c3c91347).

A static archive is selected by symbol needs rather than by a requirement to run every object file's namespace-scope constructor. A consumer calling a factory can therefore omit a separate implementation object whose only apparent effect is self-registration. In the new layout, referencing the factory pulls in an object containing registrations, and those registrations create references to the built-in implementations. This is a linkage-reachability solution to a runtime registry problem. The supporting final context was read in RegulatoryElement.cpp, IO Factory.cpp, TrafficRulesFactory.cpp, and ValidatorFactory.cpp.

The factories use function-local singleton instances and map lookups. Missing parser/writer/traffic rules produce explicit exceptions. This contextual behavior explains why a link may succeed yet using a factory fails at runtime. Singleton implementation and registry semantics predate the fork's relocation and must retain upstream credit.

## Scope and counterexamples {#scope-and-counterexamples}

The fix is bounded to enumerated built-ins. It does not make arbitrary third-party static plugins discoverable, solve every global initialization ordering problem, or prove behavior under all LTO/dead-stripping options. It also centralizes knowledge of built-in implementations in the factories, increasing coupling and potentially pulling in more code. Explicit registration functions, generated registration lists, whole-archive linking, or a dynamic plugin mechanism are alternative designs; none is observed as a discussed/rejected alternative in these commits. They are analytical comparisons only.

The same commit expands CI to static and shared modes. That is evidence that linkage mode became an explicit tested dimension in configuration. It is not proof that those jobs passed. An offline proposed check would link a minimal consumer that calls only factory creation and enumerate/instantiate each expected built-in without directly referencing the concrete class. A test that directly names all classes can accidentally force archive extraction and hide the defect.

## Portable test setup can preserve syntax while changing semantics {#portable-test-setup-can-preserve-syntax-while-changing-semantics}

Several smaller repairs expose the importance of the original invariant:

1. cdc4d61 replaces `mkdtemp` with a literal `lanelet2_io_test.XXXXXX` path and `create_directory` if absent. 24082b2 applies a similar pattern to routing. `XXXXXX` is now ordinary filename text; it is no longer expanded by `mkdtemp`. Two simultaneous runs can reuse the same path and interfere, especially with identical file names or cleanup. This is a source-derived counterexample; no parallel test was run.
2. Map fixtures move through relative-path adjustments, build-tree copying and finally `PKG_DIR`-based source-root lookup. Tests depend on an explicit data-location contract, not just executable availability. The final static-library change removes some copy dependencies after adding direct source paths.
3. The routing fixture moves from namespace static state to an inline static class member for MSVC, then to a function-local static for the restored C++14 baseline. fb3a3f6 briefly leaves an incorrect declaration; 21674a1 supplies the reference initialization. The full sequence matters more than the word “fix” in a single title.
4. Compiler-directed changes guard GCC pragmas, add an explicit string include, qualify names that have different lookup ambiguity, and relocate constexpr values into lambdas. They are repairs at compiler/language boundaries; geometry algorithms are unchanged.

## Coverage and cleanup are not correctness proof {#coverage-and-cleanup-are-not-correctness-proof}

7b3e780 adds GCC coverage flags and LCOV upload after CTest. The 747-line CodeCoverage helper's full text was read. Its header credits Lars Bilke and a sequence of collaborators; no original authorship by the fork is assigned to that module, and no exact external revision match was asserted. The fork integration enables it when tests are not string-OFF and compiler is GNU, while CI switches that job to Debug. The helper warns that optimized builds can mislead coverage interpretation; a separate badge does not establish a percentage or successful upload.

Python CLI cleanup in 7cd5e3d adds main guards and converts `iteritems` to `items`, but an error print still adds integer `args.has_id` to a string. This is a useful reminder to inspect failure branches after broad cleanup. It is not evidence that the author knowingly ignored an issue.

## Reuse rule {#reuse-rule}

For “factory is empty only in a static build,” follow linker reachability before changing the registry data structure. For “portable tests are flaky,” inspect uniqueness, file ownership, data locations and cleanup, not just whether a platform-specific API was replaced. Preserve a matrix of relevant modes and test the externally observable contract. Do not infer unmeasured performance, numerical equivalence, or an author's universal style from these repairs.
