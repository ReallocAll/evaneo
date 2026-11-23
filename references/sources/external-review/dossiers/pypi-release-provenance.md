<!-- retrieval: {"source_ids":["public:external:pypi-build-backend"],"source_type":"public","topics":["testing","build","api","documentation","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="scikit-build-core-conan-0-9-1-release-provenance-and-build-boundary"></a>

# scikit-build-core-conan 0.9.1: release provenance and build boundary {#scikit-build-core-conan-0-9-1-release-provenance-and-build-boundary}


## Release source and scope {#what-was-actually-read}

The [PyPI release page](https://pypi.org/project/scikit-build-core-conan/0.9.1/) returned HTTP 200 with a client-challenge document, not the project body. No challenge was solved. PyPI's ordinary public [versioned JSON endpoint](https://pypi.org/pypi/scikit-build-core-conan/0.9.1/json) supplied the release description, dependency constraints and both distribution records. Author/contact metadata were excluded from the retained JSON.

Both listed distributions were downloaded without installation or execution. SHA-256 digests were independently computed and matched the official release metadata. Both public provenance documents' in-toto statements were decoded; their subject filenames and digests match the downloaded files. Selected public certificate identity extensions were decoded with the existing OpenSSL tool. The [workflow at the attested commit](https://github.com/wu-vincent/scikit-build-core-conan/blob/d45118e5d9a51d7e45a439eacd7c61f83b2f7ec9/.github/workflows/release.yml) supports the workflow observations below. The public release metadata, linked provenance records and pinned workflow identify the sources for these observations.

**Verification boundary:** digest agreement and parsed publisher identity are established. Cryptographic signature verification, certificate-chain/transparency verification, rebuild reproducibility, dependency installation, and package runtime correctness were not performed. The wheel/sdist contents were acquired for integrity comparison, not certified as a full package implementation review in this external occurrence. Repository/commit analysis is a separate corpus scope.

## Release interface and dependency model {#release-interface-and-dependency-model}

The release description presents a Conan 2 integration layer around scikit-build-core for Python extensions with native dependencies. The advertised flow finds a root `conanfile.py` or `conanfile.txt`, resolves/builds dependencies through Conan, configures a CMake toolchain, then builds the extension. The selected PEP 517 backend is `scikit_build_core_conan.build`; the description says users need not separately list scikit-build-core because the plugin requires it.

The published 0.9.1 metadata requires Python 3.10 or later, Conan ≥2.20.0, scikit-build-core ≥0.11.0, Ruff ≥0.14.14, and Tomli below Python 3.11. Ruff is in ordinary release requirements, not only the test extra. Test extras include build, pytest, pytest-subprocess, pytest-xdist, cattrs, setuptools, virtualenv and wheel. These are the constraints of this specific release, not a statement that 0.9.1 remains the newest release or that all environments satisfying lower bounds are tested.

Configuration exposes separate host, build and combined contexts for profiles, options, settings and conf. This is important for cross-compilation: the tool running during a build and the library consumed by the target do not necessarily share an architecture or compiler. Local recipes provide a development path outside a remote index. Remote selection, cache-only resolution, update behavior, source-build patterns and deployers are separate controls. Lockfile input/output, partial-lock acceptance and cleanup are documented; “lockfile support” alone does not prove all toolchains, sources and environment inputs are reproducible.

Options may be provided through `pyproject.toml` or frontend configuration settings. Overrides reuse scikit-build-core's conditional system; the example uses `if.platform-system`. This connects to the separately reviewed upstream [PR #739](https://github.com/scikit-build/scikit-build-core/pull/739), but does not imply that Wu authored the entire upstream override system. The description names Endstone as a consumer and announces a future rename at 1.0; both are release-documentation claims, not independent adoption or current-roadmap verification.

## Provenance chain and workflow mechanics {#provenance-chain-and-workflow-mechanics}

The release uploaded a universal Python wheel (8,886 bytes) and source archive (15,905 bytes) on 2026-01-30. Their SHA-256 values are:

- Wheel: `f89573c4031d746515dcf6712c11a8bb7467c4ab88c2ed1d1f346623e50aeff7`.
- Source archive: `6d9f0c43d45ff26a2d055970c46d4b0806890989dddef4c01438d1febb4565b5`.

The [wheel provenance](https://pypi.org/integrity/scikit-build-core-conan/0.9.1/scikit_build_core_conan-0.9.1-py3-none-any.whl/provenance) and [source provenance](https://pypi.org/integrity/scikit-build-core-conan/0.9.1/scikit_build_core_conan-0.9.1.tar.gz/provenance) name the GitHub publisher `wu-vincent/scikit-build-core-conan`, workflow `release.yml`, environment `pypi`. The decoded certificate identifies `.github/workflows/release.yml@refs/heads/main`, commit `d45118e5d9a51d7e45a439eacd7c61f83b2f7ec9`, a `workflow_dispatch` trigger and GitHub-hosted execution, with [run 21518108509, attempt 1](https://github.com/wu-vincent/scikit-build-core-conan/actions/runs/21518108509/attempts/1). Parsing these fields is not a substitute for validating the signed envelope.

The [pinned workflow](https://github.com/wu-vincent/scikit-build-core-conan/blob/d45118e5d9a51d7e45a439eacd7c61f83b2f7ec9/.github/workflows/release.yml) has two jobs:

1. `dist` checks out full history, reads `project.version` from TOML, builds distributions with `pipx run build`, and uploads the distribution artifact.
2. `deploy` depends on `dist`, uses the `pypi` environment, requests `id-token: write` and `contents: write`, downloads the artifact, invokes PyPA's publish action, and creates a GitHub release tagged from the extracted version with generated notes and distribution files.

The job separation makes the built artifact the publishing boundary. The explicit environment and short-lived identity permission explain the identity recorded in provenance; no embedded long-lived publishing credential is visible in this workflow. The workflow itself has no test step, but this does not establish that the repository lacks separate CI. Its actions use major/release tags rather than immutable action SHAs, so pinning the repository commit does not independently freeze every external action implementation. No release, workflow, or permission change was triggered during this review.

## Separately attributed supply-chain reference {#separately-attributed-supply-chain-reference}

The official [PyPI Integrity API](https://docs.pypi.org/api/integrity/) explains how provenance is attached to an exact project/version/filename. [PyPI's consuming-attestations guide](https://docs.pypi.org/attestations/consuming-attestations/) describes verification beyond decoding. The [publish-attestation specification](https://docs.pypi.org/attestations/publish/v1/) establishes publisher-to-artifact identity/integrity semantics, not trustworthiness of the artifact's code. These are PyPI ecosystem mechanisms, not original mechanisms attributed to the package author.

Portable decision: distinguish release ownership evidence, byte integrity, authenticated provenance, reproducible construction, and behavior validation. Each needs its own evidence; a green result for one does not establish the others.
