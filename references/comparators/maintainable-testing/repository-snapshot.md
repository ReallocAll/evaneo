<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2026-10-30","topics":["testing","maintainability","metrics","github","repository-snapshot"],"limitations":"Git-tree path/extension heuristic, not LOC/coverage/quality. No runtime execution; only selected repos. Excluded repos are not represented."} -->
# EndstoneMC test-source footprint: pinned file and byte counts, not coverage targets {#case}

## Method {#method}

On 2026-10-30, GitHub recursive trees for these repositories' `main` branches were enumerated (no truncated trees reported). Only Git blobs whose paths are under a `test`, `tests`, `testdata`, `__tests__`, `integration_tests` directory or have recognized test naming patterns were classified as test candidates. Only files ending in Python, C/C++, Go, JavaScript/TypeScript, Rust, Java and common script/header suffixes were counted as **test code**. All other matching source-code suffixes were counted as **non-test code**. Git blob `size` is bytes, **not executable LOC, tests, assertions, branch coverage, or total maintenance cost**. Package test helpers located elsewhere, unrecognized naming styles, headers shared by tests and production, generated fixtures, and test data may be misclassified. Reproduce using each linked immutable Git tree and the algorithm above. The numbers are *descriptive*.

## Pinned snapshot {#snapshot}

| Repository and immutable Git reference | Test-code files | Test-code bytes | Other-code files | Other-code bytes | SHA |
| --- | ---: | ---: | ---: | ---: | --- |
| [`EndstoneMC/endstone`](https://github.com/EndstoneMC/endstone/tree/b4aaa87d2c5305e7d340168f824ac2e2ea722e44) | 70 | 225,847 | 1393 | 3,931,569 | `b4aaa87d2c53` |
| [`EndstoneMC/bedrock-protocol`](https://github.com/EndstoneMC/bedrock-protocol/tree/0fb448a6a9940f197e199dcea488fc4129755d48) | 259 | 935,945 | 71 | 596,556 | `0fb448a6a994` |
| [`EndstoneMC/bedrock-bench`](https://github.com/EndstoneMC/bedrock-bench/tree/65cd21b4096af1aebc5b88f8e3ba7b0244ca7bdb) | 77 | 784,165 | 91 | 884,556 | `65cd21b4096a` |
| [`EndstoneMC/client`](https://github.com/EndstoneMC/client/tree/b66cd750861e5ac5e1877e3a167e7e0ff2ffae00) | 11 | 49,675 | 66 | 174,797 | `b66cd750861e` |
| [`EndstoneMC/cpp-example-plugin`](https://github.com/EndstoneMC/cpp-example-plugin/tree/d3b19d401570b8921f125c4e9ab0d53919561bc9) | 0 | 0 | 3 | 5,906 | `d3b19d401570` |
| [`EndstoneMC/python-example-plugin`](https://github.com/EndstoneMC/python-example-plugin/tree/4d35addb2188cca2137f82dab524b4b575d5b06b) | 0 | 0 | 3 | 6,027 | `4d35addb2188` |
| [`EndstoneMC/endweave`](https://github.com/EndstoneMC/endweave/tree/d50554a3698a819ee71f25e0a88c9330f6c210d6) | 20 | 176,255 | 115 | 1,742,521 | `d50554a3698a` |

## Reading the differences {#meaning}

The Endstone core has a smaller test-source footprint relative to its total source than the protocol codec or benchmarking harness. This does **not** establish superior coverage or better design: compiler protocols require many per-message byte contracts, while server runtime internals can require live BDS checks absent from small unit suites. Example plugin repositories intentionally emphasize learning rather than providing a production regression suite. The benchmark repository's tests cannot alone validate fairness of published measurements. Files and bytes are a **review signal, not a budget, cap, or target**.

## Exclusion and caution {#limits}

Only explicitly selected repositories are in the snapshot. No inference is drawn from omitted repositories, and no excluded repository is used as a positive exemplar. The snapshot cannot detect duplicate assertions, flaky tests, test duration, quality of independent oracles, or developer-hours required for maintenance. This corpus did not clone, build or execute any repository.
