<!-- retrieval: {"source_ids":["public:commit:4a79d98f41f6a493077eec7d1d780831e96fcdf2","public:commit:55e034e50444ded353629c2c4d985ba7fcfddc7d","public:commit:76ef1ee1cb6dcbe6e2475b37a80c371f5232a3f8","public:commit:8fe0bf0f5789eb866a1e821f9795b72b4e769fdb","public:commit:97ca89e3d58c6e8cb8eff23a64aa837fa798bf8e","public:commit:b1a5c8dacdcf1a34c266c25134ba15d6ac1e55e6","public:commit:b53033d9017299f3e7e21b2b6d17c51c06a80134","public:commit:e7a2d2417336361a605395bdb0c714cdb8076b05","public:commit:f3f99018ed2f9457982c6092b8cafe8e8042a68b"],"source_type":"public","date":"2023-11-19..2025-10-16","topics":["concurrency","ffi","build","performance","api","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="wu-vincent-dynomo-per-sha-review"></a>
# wu-vincent/DynOMo — per-SHA review {#wu-vincent-dynomo-per-sha-review}

9 reviewed commits. Commit messages and meaningful changes were reviewed; structural exceptions are explicit. No runtime validation.

## 1. refactor: consolidate environment.yml {#1-refactor-consolidate-environment-yml}

[55e034e50444ded353629c2c4d985ba7fcfddc7d](https://github.com/wu-vincent/DynOMo/commit/55e034e50444ded353629c2c4d985ba7fcfddc7d) · 2025-02-04T18:58:17Z

Replaces an exported Linux-specific Conda environment (Python3.10/older CUDA/Torch build strings) with shorter direct dependencies and Python3.12. This reduces platform-specific lock details while reducing exact reproducibility; later commits pin Torch and refill needed packages.

## 2. chore: add pre-built diff_gaussian_rasterization_w_dwv wheel {#2-chore-add-pre-built-diffgaussianrasterizationwdwv-wheel}

[97ca89e3d58c6e8cb8eff23a64aa837fa798bf8e](https://github.com/wu-vincent/DynOMo/commit/97ca89e3d58c6e8cb8eff23a64aa837fa798bf8e) · 2025-02-04T18:58:41Z

Documents environment installation and a bundled Windows CPython3.12 rasterizer wheel, fixes the depths option spelling, and adds the first binary wheel. ZIP metadata/wrapper are inspectable; native .pyd implementation remains opaque. This does not establish runtime ABI compatibility.

- Limit: Native wheel .pyd payloads receive ZIP/size/hash/metadata coverage only, no native-code disassembly or execution.

## 3. refactor: make data preparation scripts portable {#3-refactor-make-data-preparation-scripts-portable}

[b53033d9017299f3e7e21b2b6d17c51c06a80134](https://github.com/wu-vincent/DynOMo/commit/b53033d9017299f3e7e21b2b6d17c51c06a80134) · 2025-02-04T18:59:05Z

Replaces shell-heavy DAVIS download/setup with requests, pathlib, zipfile/shutil, and argument-list subprocess calls with check=True. Downloads lack timeout/checksum/atomic resume, and weight downloads lack status checks. A path to Depth-Anything is temporarily wrong and corrected later. No data/models were downloaded or preprocessors executed.

## 4. chore: freeze pytorch version in environment.yml {#4-chore-freeze-pytorch-version-in-environment-yml}

[8fe0bf0f5789eb866a1e821f9795b72b4e769fdb](https://github.com/wu-vincent/DynOMo/commit/8fe0bf0f5789eb866a1e821f9795b72b4e769fdb) · 2025-02-04T20:23:43Z

Pins Torch2.5.1/torchvision0.20.1, adds needed packages, and supplies CPython3.9–3.12 Windows wheels. Four new/replaced wheel blobs were structurally audited. Wheel metadata does not encode Torch/CUDA dependency compatibility; Python tag alone is insufficient.

- Limit: Native wheel .pyd payloads receive ZIP/size/hash/metadata coverage only, no native-code disassembly or execution.

## 5. fix: correct path handling in process_panoptic_sport.py on Windows {#5-fix-correct-path-handling-in-processpanopticsport-py-on-windows}

[b1a5c8dacdcf1a34c266c25134ba15d6ac1e55e6](https://github.com/wu-vincent/DynOMo/commit/b1a5c8dacdcf1a34c266c25134ba15d6ac1e55e6) · 2025-02-04T20:24:38Z

Normalizes Windows path separators before checking the Panoptic keep list. This matters because non-matching directories are deleted; a separator-only mismatch can otherwise remove intended views. Wrong cwd/missing list and atomic deletion are still outside this repair.

## 6. refactor: `download_panoptic` {#6-refactor-downloadpanoptic}

[e7a2d2417336361a605395bdb0c714cdb8076b05](https://github.com/wu-vincent/DynOMo/commit/e7a2d2417336361a605395bdb0c714cdb8076b05) · 2025-02-04T20:46:56Z

Ports Panoptic downloading/extraction and preprocessing to Python calls and checked subprocesses, gives explicit output names to gdown, and corrects DAVIS depth model paths. Creating annotations at the destination before shutil.move(data/data, destination) can nest the directory instead of producing the assumed layout; this is a static edge case, not a reproduction.

## 7. fix: runtime errors {#7-fix-runtime-errors}

[f3f99018ed2f9457982c6092b8cafe8e8042a68b](https://github.com/wu-vincent/DynOMo/commit/f3f99018ed2f9457982c6092b8cafe8e8042a68b) · 2025-02-05T19:44:43Z

Moves Boolean masks to CPU before indexing CPU-resident historical quaternion/background tensors, and removes unused pix_id filtering in visibility calculation. Context confirms pix_id is not returned or used downstream in that function. Existing Gaussian-ID-zero filtering, device transfer costs, and research correctness assumptions remain; no gradient/performance equivalence was measured.

## 8. refactor: replace shell commands with direct Python calls {#8-refactor-replace-shell-commands-with-direct-python-calls}

[4a79d98f41f6a493077eec7d1d780831e96fcdf2](https://github.com/wu-vincent/DynOMo/commit/4a79d98f41f6a493077eec7d1d780831e96fcdf2) · 2025-02-05T19:45:11Z

Ports iPhone download/extract/preprocess orchestration to explicit Python operations and checked subprocesses. Uses python by name and cwd-relative paths rather than sys.executable/repository-root anchoring; interpreter and partial-download failures remain relevant counterexamples.

## 9. chore: add missing dependencies in environment.yml {#9-chore-add-missing-dependencies-in-environment-yml}

[76ef1ee1cb6dcbe6e2475b37a80c371f5232a3f8](https://github.com/wu-vincent/DynOMo/commit/76ef1ee1cb6dcbe6e2475b37a80c371f5232a3f8) · 2025-02-05T19:46:35Z

Adds the fuller direct dependency set, CUDA11.8/PyTorch channel choices, matching torch-scatter instructions, and config path corrections. README names the DynOMo research authors and distinguishes paper depth sources/evaluation modes. Port/setup changes do not constitute new tracking/3D Gaussian methodology or reproduce reported 3DV results.
