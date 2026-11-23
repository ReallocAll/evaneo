<!-- retrieval: {"source_ids":["public:commit:f3f99018ed2f9457982c6092b8cafe8e8042a68b"],"source_type":"public","date":"2023-11-19..2025-10-16","topics":["testing","performance","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="dynomo-cpu-history-gpu-masks-and-visibility-semantics"></a>
# DynOMo: CPU history, GPU masks and visibility semantics {#dynomo-cpu-history-gpu-masks-and-visibility-semantics}

## Read scope {#read-scope}

The reviewed device-mask patch is f3f9901, [public source](https://github.com/wu-vincent/DynOMo/commit/f3f99018ed2f9457982c6092b8cafe8e8042a68b). Supporting source was read in the forward-propagation section of `src/model/dynomo.py` (lines 270–335), the complete `compute_visibility` tail of `src/model/renderer.py` (248–303), and the affected loss functions in `src/utils/losses.py` (176–244). The larger files were extracted, but their unneeded preceding implementations are not claimed as fully read.

## Device contract {#device-contract}

Historical Gaussian quaternion data is stored on CPU while a selection mask comes from the current computation. Applying the GPU Boolean mask directly to the CPU tensor crosses a device boundary at indexing. The patch makes the mask CPU-resident before selecting the historical tensor. It makes the analogous change for the background-selection mask used with stored history. This is a consistency repair between producer and consumer devices, not a new motion model.

A safe interpretation is that the selected history must be indexed using a mask on a compatible device, after which any computation-specific conversion follows. It would be wrong to generalize this into “move masks to CPU for speed.” Device copies may add transfer and synchronization costs, and alternate designs could keep history on the accelerator or transfer selected data differently. The reviewed patch contains no timing, memory study or gradient comparison choosing among those designs.

## Removal of unused work {#removal-of-unused-work}

`compute_visibility` creates a pixel-ID array, then applies a visibility-derived mask to it. The patch comments out that masking. In the examined function, the resulting pixel IDs are unused by the returned visibility calculation. Removing the operation therefore avoids an unnecessary indexing/device interaction without changing the visible return expression. This is narrower evidence than proving whole-pipeline numerical equivalence: no runtime test was performed, and external behavior such as timing/errors can differ even if the returned formula is unchanged for valid input.

The function also filters out Gaussian ID zero because zero is used in rasterizer output as an invalid entry. The source acknowledges that this discards the actual first Gaussian. This is a pre-existing approximation, not corrected by the device-mask patch. It matters to consumers who assume every valid Gaussian participates in the visibility vector.

## Upstream kernel context {#upstream-kernel-context}

Exact-SHA public rasterizer context establishes a related limitation. Its render kernel stores contributions only while a contributor index is below `MAX_CONTRIBUTERS`; the counter increases while traversing candidates, including paths that can be skipped before writing a contribution. It writes the Gaussian index into a float visibility output and contribution weight as alpha times transmittance. The read range was the render tail, not the whole rasterizer or all forward/backward kernels. Thus a downstream weighted visibility vector is derived from bounded recorded contributors and sentinel conventions, not an exhaustive geometric visibility oracle.

The Python rasterizer wrapper returns color, radii, depth, weight and visible outputs. Its backward path forwards color-output gradient to native code and does not forward the supplied depth/weight/visible gradients. The README explicitly says depth backward is unimplemented. This constrains downstream loss design; it does not by itself invalidate a method that represents supervised depth in a differentiable color-like path or uses these outputs without gradients. Whether a particular DynOMo loss takes such a route needs its own traced dataflow. No blanket “depth training is broken” claim is supported.

## Applicability and counterexamples {#applicability-and-counterexamples}

For “Boolean tensor indexing fails after moving state to CPU,” trace each tensor's storage device at production, history retention and consumption. Test CPU/GPU histories, empty masks, all-selected masks, first-frame history absence and shape agreement. For “visibility changed after a portability fix,” separate mask-device mechanics from contributor caps and sentinel loss before changing the algorithm.

For training, distinguish outputs intended for differentiable loss from diagnostic/evaluation outputs. A tensor return value alone does not establish its gradient contract. A proposed finite-difference or autograd check should isolate each intended output route and use controlled inputs. No such check, GPU execution, benchmark or reproduction was performed here.

This evidence supports careful boundary repair in one research pipeline. It does not establish a general preference for CPU storage, a faster algorithm, correct gradients for auxiliary rasterizer outputs, or ownership of the underlying dynamic tracking method.
