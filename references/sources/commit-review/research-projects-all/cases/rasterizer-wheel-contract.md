<!-- retrieval: {"source_ids":["public:commit:4f11a843c09fe9988719c7211795ccf8d50858b3","public:commit:720936a2d70853a90104056a559c711eb8adcd21","public:commit:8772764934357eecdc0e53115c7c2d18082cc4a5","public:commit:a56756f62d18340432617353b928bfc62801d9d6","public:commit:d7cc8357a091cd57681d2a7521a14ec2cfcf59af"],"source_type":"public","date":"2023-11-19..2025-10-16","topics":["ffi","testing","build","performance","documentation","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="cuda-rasterizer-wheels-build-matrix-abi-and-numerical-boundaries"></a>
# CUDA rasterizer wheels: build matrix, ABI and numerical boundaries {#cuda-rasterizer-wheels-build-matrix-abi-and-numerical-boundaries}

## Wheel workflow changes {#what-the-target-changed}

All five reviewed commits in `wu-vincent/diff-gaussian-rasterization-w-depth-vis-weights` change the wheel workflow. They do not modify CUDA kernels, the C++ binding or Python autograd implementation. [Chronological review](../diff-gaussian-rasterization-w-depth-vis-weights-review.md), [initial commit](https://github.com/wu-vincent/diff-gaussian-rasterization-w-depth-vis-weights/commit/720936a2d70853a90104056a559c711eb8adcd21), and [final pin](https://github.com/wu-vincent/diff-gaussian-rasterization-w-depth-vis-weights/commit/d7cc8357a091cd57681d2a7521a14ec2cfcf59af).

The initial workflow targets Linux/Windows and multiple Python versions, but uses an undefined CUDA matrix field and an unquoted `3.10` value. A following commit supplies CUDA11.8 and quotes Python3.9–3.12, sets specific older runner images, adds CUDA components and architecture flags, repairs Linux wheels, and uploads artifacts. A later small commit adds Thrust. The final commit pins Torch2.5.1 and torchvision0.20.1, matching the DynOMo environment changes.

The first workflow contains an install/import smoke step; the restructuring removes it. Therefore the later matrix is not stronger runtime evidence merely because it builds more artifacts. No Actions run logs or successful installation/import results were reviewed.

## Build and runtime dependency contract {#build-and-runtime-dependency-contract}

Exact-SHA setup.py defines a Torch `CUDAExtension`, compiling rasterizer implementation, forward/backward CUDA, rasterize_points.cu and ext.cpp with the GLM include directory. The binding exposes rasterize, backward and mark-visible functions with pybind. The submodule file identifies GLM under third_party. The workflow checkout does not request recursive submodules. That creates a source-availability question to test; no build failure is asserted from configuration alone.

Linux repair excludes `libtorch_python.so`, `libc10.so` and `libtorch_cpu.so`, so those dependencies are intentionally external to the repaired wheel. Python version, platform, Torch build/version, CUDA toolkit/runtime, compiler ABI and hardware code/virtual-code targets are distinct dimensions. Artifact names encode only some of them. An architecture list ending in 8.6+PTX is a recorded compilation choice, not proof of support or performance on every accelerator.

DynOMo contains five new/replaced Windows wheel blobs, all with an identical Python wrapper and separate native payload hashes. Wrapper contents match the exact-SHA public source after newline normalization; this establishes wrapper identity, not the provenance or equivalence of compiled native code. Metadata records distribution name/version0.0.0 and tags but no Torch/CUDA Requires-Dist. Do not assume the wheel can safely substitute for another Torch version just because pip accepts the Python/platform tag.

The DynOMo gitlink points to `497b84f4d895954feed9ac54fa3443427ec7a48e`, the parent of the first reviewed rasterizer workflow commit. The relevant README, setup, binding, GLM configuration, forward kernel and Python wrapper blobs are unchanged through the final reviewed revision. Comparison of the public Git blobs supports that source-revision relationship, so the contextual limits also apply to the revision referenced by DynOMo. This still does not verify which source/compiler configuration produced each native wheel.

## Algorithm credit and depth semantics {#algorithm-credit-and-depth-semantics}

The exact-SHA README identifies the base Graphdeco/Inria rasterizer and attributes the depth extension to Jonathon Luiten. It cites the 3D Gaussian Splatting authors Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler and George Drettakis. The code header retains a non-commercial research/evaluation license notice. This review reports the notice, not a legal determination about a proposed use. Wheel-CI edits do not create ownership of these algorithms.

The render-tail source was read at forward.cu lines 260–500; the full file is also preserved with independently matching Git blob hash, but earlier preprocessing is not claimed read. Per pixel, transmittance starts at one; alpha is capped at0.99, tiny alpha is skipped, and very low transmittance ends accumulation. Median depth is set from the Gaussian at the crossing below0.5, with a default15 if no crossing occurs. The code uses strict comparisons, so edge equality should not be silently treated as a proven exact median convention. Its own comment calls the fallback a hack. Weight/visibility records are contributor-capped.

The wrapper exposes mutually exclusive SH/precomputed-color input routes and scale+rotation/precomputed-covariance routes, using empty tensors as absence sentinels. It returns auxiliary depth/weight/visibility outputs but its backward forwards only color-output gradient. The README explicitly states that depth backward has not been implemented. Auxiliary output availability is therefore different from differentiable training support.

## Evidence acquisition and remaining limits {#evidence-acquisition-and-remaining-limits}

Public exact-SHA setup, wrapper, README, extension, GLM and forward-source blobs were checked independently. The complete-file hash comparisons and the narrower excerpts used for interpretation support different claims. No source was executed; compiled wheel provenance remains unverified.

No source-level attribution for every historic visibility extension is established beyond the README/header and the verified fact that all five changes are limited to build workflows. The native binaries were inspected structurally, not executed or reverse engineered. No throughput, accuracy, gradient correctness or wheel ABI claim is made.

## Reuse {#reuse}

Use this case for “package a Torch CUDA extension,” “pip installs but import fails,” or “can I train from this depth output.” Specify and test a coherent ABI matrix, verify submodule availability, retain import/native smoke checks after build refactors, and inspect autograd dataflow before promising differentiability. A successful build artifact and a research README each answer a different question. Neither substitutes for a controlled numerical or deployment test.
