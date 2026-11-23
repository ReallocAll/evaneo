<!-- retrieval: {"source_ids":["public:commit:02c31fd8863c1cce37aa3ff6e334e81097e48377","public:commit:117d8780bb1603c446cd4141cec6e59d9391f037","public:commit:173bf02fa2e5f7b0cba6014b140b73e7e7bc8a80","public:commit:1a47a108e8a3a84690ce151986e64ad9c46d5168","public:commit:1a5f721b4b15b783faf8f8cd540dad57c4c8962b","public:commit:6d88f1e65629d8008e3cfe06b219f4c703e445da","public:commit:8c7e4c21155b2f333a9ce47283f235f462f82f50","public:commit:b8b2e1441a36c14ecb22614a1b42038820217c8e","public:commit:d6281a3b1c51f477bb0f97497173b82385c70754","public:commit:e51990bbf51fb600a31ef8df74a15f7fe790c09c"],"source_type":"public","date":"2025-03-12..2025-03-26","topics":["ffi","testing","build","api","documentation","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="papi03-packaging-is-part-of-an-api-contract"></a>
# Packaging is part of an API contract {#papi03-packaging-is-part-of-an-api-contract}

## What changed {#what-changed}

The initial PAPI distribution has a native plugin and a Python wrapper. `d6281a3b` builds native Linux/Windows binaries separately from CPython 3.9–3.13 wheels. After the implementation becomes a Python-backed service, `e51990bb` removes the native plugin job; `1a5f721b` installs the C++ public headers into the wheel. A C++ caller can therefore obtain its interface from the same distribution that supplies the provider. README `02c31fd8` explicitly says the plugin is unreleased and directs users to CI artifacts and the header inside the wheel.

`117d8780` changes scikit-build-core to scikit-build-core-conan and adds a Conan CMakeToolchain/CMakeDeps layout. `8c7e4c21` sets the Conan generator to Ninja. The exact motivation for the backend change is not recorded beyond the commit subjects. The dependency is temporarily `main` during service development, then `173bf02f` pins Endstone v0.7.0. Locally that tag resolves to `db676bf032f2e959a37e0c0d039dd9ae1ffd9bb3`.

## Claims versus evidence {#claims-versus-evidence}

The wheel matrix is a requested build surface, not a successful CI result. Native jobs earlier use Clang15 while Linux wheel configuration installs Clang/libc++16 in an Endstone manylinux image. The selected history has no automated behavior test invocation and scikit-build explicitly disables BUILD_TESTING. No workflow, compiler or dependency installer was run in this review.

`1a47a108` lowers declared Python support from >=3.10 to >=3.9. The final plugin still uses structural pattern matching; a static AST parse with Python3.9 grammar rejects it. This check parses source without importing or executing it. `chars_replacer.py` also evaluates a `Player | None` annotation without future annotations, an additional compatibility concern. The lowered metadata and cp39 wheel matrix do not prove Python3.9 runtime compatibility. README context still says Python3.10+, so documentation, metadata and code disagree.

The native binding sources are excluded from source distributions by `sdist.exclude = ["endstone_papi/*.cpp"]`, despite CMake requiring that file to build the extension. This is a static source-distribution completeness risk; no sdist was built here to determine backend behavior. Wheel packaging and sdist installability must be checked separately.

## Proportionate evidence treatment {#proportionate-evidence-treatment}

- Root scaffold is an exact copied tree, not a new design.
- `b8b2e144` is quote/blank-line formatting only.
- `c3a4289e` has equal Python ASTs and inspected C++ formatting-only changes; it does not earn independent functional credit.
- The added screenshot was opened. It depicts a populated join message, but lacks platform/version/test procedure and cannot establish broad compatibility.
- Version pins, artifact names and README edits have small but explicit dispositions rather than disappearing from the ledger.

## Reusable lesson and boundary {#reusable-lesson-and-boundary}

When a plugin is consumed in two languages, review installation paths, extension initialization symbol, stub imports, header distribution, runtime API version, source-distribution contents and supported interpreter syntax as one contract. The useful pattern here is shipping a shared interface with its provider and updating examples along the migration. The counterexample is treating a metadata downgrade as working support. Do not turn this sequence into a preference for Conan, Ninja or any one binding framework without the stated constraints.

## Evidence {#evidence}

[Per-commit source index](../repositories/papi-source-index.md) covers the selected history. Public sources include [packaging changes](https://github.com/EndstoneMC/papi/commit/1a5f721b4b15b783faf8f8cd540dad57c4c8962b) and [Python version metadata](https://github.com/EndstoneMC/papi/commit/1a47a108e8a3a84690ce151986e64ad9c46d5168). The grammar, AST, wheel and screenshot observations above are static-review findings; local check outputs are not distributed.
