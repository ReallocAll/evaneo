<!-- retrieval: {"source_ids":["public:commit:4f11a843c09fe9988719c7211795ccf8d50858b3","public:commit:720936a2d70853a90104056a559c711eb8adcd21","public:commit:8772764934357eecdc0e53115c7c2d18082cc4a5","public:commit:a56756f62d18340432617353b928bfc62801d9d6","public:commit:d7cc8357a091cd57681d2a7521a14ec2cfcf59af"],"source_type":"public","date":"2023-11-19..2025-10-16","topics":["build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="wu-vincent-diff-gaussian-rasterization-w-depth-vis-weights-per-sha-review"></a>
# wu-vincent/diff-gaussian-rasterization-w-depth-vis-weights — per-SHA review {#wu-vincent-diff-gaussian-rasterization-w-depth-vis-weights-per-sha-review}

5 reviewed commits. Commit messages and meaningful changes were reviewed; structural exceptions are explicit. No runtime validation.

## 1. ci: add build.yml {#1-ci-add-build-yml}

[720936a2d70853a90104056a559c711eb8adcd21](https://github.com/wu-vincent/diff-gaussian-rasterization-w-depth-vis-weights/commit/720936a2d70853a90104056a559c711eb8adcd21) · 2025-02-04T14:39:45Z

Introduces Ubuntu/Windows wheel CI, Python matrix, CUDA setup and an import smoke command. Initial unquoted 3.10 risks YAML numeric interpretation and CUDA version references an undefined matrix field; both are revised next. No kernel or autograd implementation changed.

## 2. ci: update build.yml {#2-ci-update-build-yml}

[8772764934357eecdc0e53115c7c2d18082cc4a5](https://github.com/wu-vincent/diff-gaussian-rasterization-w-depth-vis-weights/commit/8772764934357eecdc0e53115c7c2d18082cc4a5) · 2025-02-04T15:49:08Z

Quotes CPython3.9–3.12, sets CUDA11.8, older OS runners, architecture list, wheel repair and artifact upload. Auditwheel excludes Torch shared libraries, leaving the PyTorch runtime external. Removes the previous install/import smoke step. Workflow lacks recursive checkout while setup includes GLM submodule headers; build success is not established.

## 3. ci: update build.yml {#3-ci-update-build-yml}

[4f11a843c09fe9988719c7211795ccf8d50858b3](https://github.com/wu-vincent/diff-gaussian-rasterization-w-depth-vis-weights/commit/4f11a843c09fe9988719c7211795ccf8d50858b3) · 2025-02-04T15:50:03Z

Removes pip cache configuration from setup-python. No stated reason and no independent algorithm or performance lesson.

## 4. ci: update build.yml {#4-ci-update-build-yml}

[a56756f62d18340432617353b928bfc62801d9d6](https://github.com/wu-vincent/diff-gaussian-rasterization-w-depth-vis-weights/commit/a56756f62d18340432617353b928bfc62801d9d6) · 2025-02-04T15:51:07Z

Adds the CUDA thrust component to setup. A build dependency completion, not a rasterization/numerical change.

## 5. ci: update build.yml {#5-ci-update-build-yml}

[d7cc8357a091cd57681d2a7521a14ec2cfcf59af](https://github.com/wu-vincent/diff-gaussian-rasterization-w-depth-vis-weights/commit/d7cc8357a091cd57681d2a7521a14ec2cfcf59af) · 2025-02-04T19:58:38Z

Pins Torch2.5.1/torchvision0.20.1, aligned with DynOMo environment work. All five reviewed commits are workflow-only. Public exact-SHA context identifies Inria rasterization and Jonathon Luiten depth extension; depth backward is absent, depth fallback is 15, and contributor-bounded visibility is not a universal differentiable-depth contract.
