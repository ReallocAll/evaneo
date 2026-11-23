<!-- retrieval: {"source_ids":["public:commit:4a79d98f41f6a493077eec7d1d780831e96fcdf2","public:commit:55e034e50444ded353629c2c4d985ba7fcfddc7d","public:commit:76ef1ee1cb6dcbe6e2475b37a80c371f5232a3f8","public:commit:8fe0bf0f5789eb866a1e821f9795b72b4e769fdb","public:commit:97ca89e3d58c6e8cb8eff23a64aa837fa798bf8e","public:commit:b1a5c8dacdcf1a34c266c25134ba15d6ac1e55e6","public:commit:b53033d9017299f3e7e21b2b6d17c51c06a80134","public:commit:e7a2d2417336361a605395bdb0c714cdb8076b05","public:commit:f3f99018ed2f9457982c6092b8cafe8e8042a68b"],"source_type":"public","date":"2023-11-19..2025-10-16","topics":["testing","build","api","documentation","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="dynomo-portable-setup-without-claiming-experiment-reproduction"></a>
# DynOMo: portable setup without claiming experiment reproduction {#dynomo-portable-setup-without-claiming-experiment-reproduction}

## Attribution and problem {#attribution-and-problem}

Nine reviewed commits from 2025 modify dependencies, installation guidance, bundled native wheels, download/preprocessing orchestration and a focused tensor-device issue. The final README identifies the DynOMo research authors: Jenny Seidenschwarz, Qunjie Zhou, Bardienus Pieter Duisterhof, Deva Ramanan and Laura Leal-Taixé. These setup and portability changes are distinct from their dynamic Gaussian tracking method and 3DV 2025 research results. See [all nine per-SHA records](../DynOMo-review.md) and [final public commit](https://github.com/wu-vincent/DynOMo/commit/76ef1ee1cb6dcbe6e2475b37a80c371f5232a3f8).

## Environment evolution {#environment-evolution}

The first environment patch removes a detailed exported Linux environment with older Python/Torch/CUDA build strings and replaces it with a shorter direct-dependency list targeting Python3.12. This reduces platform-specific pins and incidental transitive details. It simultaneously stops specifying the old exact environment: fewer pins do not establish equivalent numerical or runtime behavior. Subsequent commits pin Torch2.5.1/torchvision0.20.1, add dependencies such as natsort, and finally add a fuller set including CUDA11.8-related requirements and matching torch-scatter installation instructions.

The README adds Windows wheel installation. New/replaced wheel files target CPython3.9–3.12. All five introduced binary artifacts were opened as ZIP data only: filenames, member sizes/hashes, WHEEL/METADATA and the common Python wrapper were inspected. The `.pyd` payloads were not executed, imported, disassembled, or compared for machine-code semantics. The package metadata contains no Requires-Dist constraint expressing the Torch/CUDA compatibility contract. A Python tag and `win_amd64` tag therefore do not establish compatibility with an arbitrary installed Torch/CUDA stack. Wheel audit retains exact evidence.

## Download and preprocessing boundary {#download-and-preprocessing-boundary}

The DAVIS, Panoptic Sport and iPhone changes replace shell command strings with Python filesystem/archive/download operations and subprocess argument lists. `subprocess.run(..., check=True)` surfaces nonzero preprocessing exits instead of silently continuing a shell sequence. Explicit output filenames improve predictability for gdown operations. Path separators are normalized before checking Panoptic's keep list, which matters because non-kept directories are removed.

These are meaningful portability improvements, but they preserve or introduce other assumptions:

- Paths are relative to the current working directory. Several subprocesses invoke `python` by name rather than the running interpreter's `sys.executable`.
- The DAVIS depth command temporarily points at `data/Depth-Anything`; a later commit fixes it to the repository-relative model location. This is a concrete revision, not evidence that the first port was already complete.
- Downloads are not uniformly timeout/status/checksum/atomic-write protected. The helper's `raise_for_status` does not cover every separately downloaded model-weight path. A check for one existing weight file is not a transaction covering an expected pair of files.
- ZIP extraction has no explicit archive-resource budget in these changes. A network interruption, unexpected archive shape or insufficient disk space can leave a partial destination.
- Creating `panoptic_sport/annotations` before `shutil.move(data/data, panoptic_sport)` means the destination already exists. Standard move semantics can place the source under `panoptic_sport/data`; downstream assumptions should be checked against that layout. This is a static counterexample, not a claimed observed defect in an executed download.
- Separator normalization fixes an exact false-negative keep-list comparison. It does not establish that the correct root, scene list or dataset version was selected before destructive cleanup.

No datasets, model weights or external tools were downloaded/executed during this review. Descriptions of the script's intended network/filesystem operations are source analysis only.

## Experiment inputs are part of the method {#experiment-inputs-are-part-of-the-method}

The README distinguishes paper-used depth inputs for Panoptic Sport and iPhone from generic depth estimation options. It also describes an evaluation option selecting the best Gaussian using ground truth. That “best” setting has oracle information and cannot be mixed with an ordinary estimated association setting when comparing results. A successful environment install would still leave depth-source, camera, sequence, model checkpoint, mask and evaluation-setting questions open.

The recorded dependency changes do not include a controlled before/after accuracy, runtime, memory or reproducibility study. No claim is made that the port preserves all original numerical behavior, reaches paper metrics, or improves performance. The appropriate outcome is “source-level setup and compatibility work reviewed.”

## Reuse and test design {#reuse-and-test-design}

Use this case for a Python research repo that must work across shells/operating systems, a downloader that succeeds partially, or a model port whose environment no longer matches the paper. Keep orchestration separate from numerical method credit. Define a manifest of expected archive paths, model identities and hashes, preserve partial-download state intentionally, and anchor subprocesses to an explicit interpreter/root. Before destructive selection, compare normalized paths against a validated manifest and test a missing/empty keep-list case.

Proposed offline fixtures can exercise path handling and staged-directory logic without contacting the data hosts or running models. Actual numerical validation would separately compare matched inputs, seeds, precision, dependency stack and evaluation options. These are suggested future checks, not work performed or permission to install/run upstream code.
