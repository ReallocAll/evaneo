<!-- retrieval: {"source_ids":["public:external:paper-consynth"],"source_type":"public","topics":["testing","performance","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="consynth-coauthored-simulation-synthetic-data-and-evaluation-boundaries"></a>

# ConSynth: coauthored simulation, synthetic data, and evaluation boundaries {#consynth-coauthored-simulation-synthetic-data-and-evaluation-boundaries}

Authors: Zhengyu Wu, Yuxiang Feng, Yiannis Demiris, Panagiotis Angeloudis.

## Provenance and source notes {#provenance-and-reading}

- Paper: *Development of a Digital Twin-Based Simulation System and a Novel Synthetic Video Dataset for Enhancing Computer Vision in Construction Site Safety*, EC3 2024, DOI [10.35490/EC3.2024.195](https://doi.org/10.35490/EC3.2024.195).
- The original `ec-3.org/publications/conferences/EC32024/papers/EC32024_195.pdf` path returns 404. The [current publisher page](https://ec-3.org/publication/EC32024_195/) explicitly links [the moved published PDF](https://ec-3.org/wp-content/uploads/2025/10/EC32024_195.pdf). The [Imperial institutional record](https://spiral.imperial.ac.uk/entities/publication/38446ba9-f90e-4a78-bdcb-01da0ada6ce6) independently confirms the title, authors, DOI, published version, and CC BY-NC-ND 4.0 license.
- The paper's extracted text covers methods, tables, results, limitations, acknowledgments and bibliography. The metric equation and training/dataset text on PDF page 6 were visually checked; other figures were reviewed through captions and surrounding text, not comprehensively image-audited. The cited studies are not independently reviewed here.
- The linked published PDF is the primary source. No experiments, simulator, dataset, training, or model weights were run.

## Problem, alternatives and system decomposition {#problem-alternatives-and-system-decomposition}

The paper targets the annotation cost and domain mismatch in construction-site object detection. It contrasts crop-and-paste imagery, which can mismatch illumination and perspective, and manually authored scenes, which omit site detail. Its alternative is a site-specific digital twin, behavioral simulation, randomized visual conditions, and automatic annotations. That choice costs surveying and environment creation; it is not a zero-cost replacement for real validation data.

The environment comes from weekly UAV images reconstructed with structure-from-motion in Bentley ContextCapture. The captured site has insufficient background for shallow camera angles. Rather than extend the costly scan to the whole surrounding landscape, the authors georegister the local reconstruction and combine it with Google Earth's more static distant scene, removing the overlapping region. This is a layered-fidelity construction: spend high fidelity where change matters and use a separate low-refresh background. The paper does not establish rights for an unrelated user to redistribute those background assets.

A Lanelet2 vector map represents the site's logistics plan. Vehicle lanes, intersections and pedestrian paths have explicit tags. Vehicles spawn outside intersections with minimum spacing and a maximum count; pedestrians have a separate spacing/count constraint. Pedestrian-lane intersections with vehicle lanes become crossings. Intersection lanes are clustered with a stated k-nearest-neighbor method to create intersection controllers; the paper does not specify enough parameters to reproduce this clustering exactly. Vehicles randomly select connected lanes. The intersection controller admits waiting vehicles and then grants pedestrian crossings a timed `walkable` phase. This is rule-based movement control, not evidence of a learned navigation policy or a quantitatively validated human-behavior model.

## Visual diversity and annotation implementation {#visual-diversity-and-annotation-implementation}

Weather sampling assigns probabilities to clear sky (0.20), ordinary clouds (0.10), partial clouds (0.10), fog (0.20), light rain (0.10), thunderstorms (0.10), and overcast (0.20); daylight/night are 0.75/0.25. Camera placement first chooses a lane point, then an elevated center and hemisphere position, rejects occluded views with ray tracing, points the camera toward the center, and randomizes intrinsic/extrinsic parameters. This avoids wasting most examples on empty background while retaining viewpoint diversity. Numerical bounds for camera height/radius and several movement parameters are symbolic rather than supplied constants.

Unreal Engine 5 renders RGB, masks and other buffers. A C++ annotation component records agent and camera transforms, coordinates, rotations and 3D box dimensions. Instance IDs are represented by distinct mask colors; OpenCV extracts polygons and enclosing 2D rectangles. Important implementation questions left open include partial-visibility box conventions, anti-aliased mask colors, deterministic seeds, synchronization across camera/agent snapshots, and annotation unit tests. These are review questions, not defects demonstrated by the paper.

The dataset contains 200 sequences of 120 frames at 12 fps, hence 24,000 frames at 1920×1080. It has three categories: workers (237,215 instances), dump trucks (106,929), mixer trucks (31,800). The authors classify 63%/24%/13% as small/medium/large after proportionally scaling their COCO-derived thresholds. They offer annotations for several tasks, but the experiments evaluate object detection; support for tracking, depth or behavior analysis is not evidence of measured success on those tasks.

## Evaluation, measured results and what they do not show {#evaluation-measured-results-and-what-they-do-not-show}

YOLOv8 is trained for 100 epochs on four RTX 4090 24 GB GPUs, batch size 16, SGD, initial learning rate 0.002 and final learning-rate factor 0.01, with 640×640 model inputs. The real train/validation sets combine MOCS and ACID (24,233/5,219 images); synthetic train/validation has 19,200/4,800 frames. The paper does not clearly specify whether the latter split is sequence-disjoint, leaving correlated-frame leakage an unresolved audit question.

The independent target-site set is selected from 500,000 captured images: 10,000 sampled candidates, then 100 selected for embedding diversity using ImageNet-pretrained MobileNetv2, manually labeled and reviewed. This favors diversity but is a small, selected site-specific evaluation population, not an unbiased multi-site field deployment sample.

Table 2's reported all-class metric is 69.3 for real-trained/real-validation, 56.4 for synthetic/synthetic, 9.3 for real/synthetic, and 5.7 for synthetic/real. Mixing datasets yields 67.8 on real and 50.8 on synthetic validation. On the target-site set, real-only yields 9.9, synthetic-only 4.2, and mixed 11.2. The often-highlighted dump-truck improvement is 6.4→9.0 on that target site: +2.6 points, approximately +40.6% relative. It is not a universal 40-point gain. Synthetic-only improves dump trucks there (6.4→7.7) while sharply reducing worker and mixer-truck scores; aggregate synthetic-only performance is worse.

The paper calls the metric mAP but prints `TP/(TP+FP)` as its defining equation, which is precision, not average precision integrated over recall and averaged across classes. This was verified visually on page 6. The text does not resolve the IoU protocol or whether the equation is merely a writing error. Preserve the paper's label as a *reported metric*, do not claim an independently validated mAP protocol.

Real-data ablation uses 100 through 12,800 real examples plus synthetic data. On real validation, 12,800 real examples produce 66.7 against the mixed full-data 67.8; 6,400 yield 62.9. The text refers to a real-only baseline of 69.0 while Table 2 says 69.3. The broad “75% less data with comparable performance” wording therefore depends on the target-site comparison and tolerance for lower real-domain scores. The paper has no confidence intervals, multiple random-seed variance, or causal isolation of scene fidelity versus weather randomization.

## Failure modes, next checks and portable use {#failure-modes-next-checks-and-portable-use}

- Domain gap remains in both directions despite photorealism. Site matching may explain target-site improvement more directly than general robustness.
- Small distant objects and occluded workers remain difficult; downsizing can erase their features. SAHI and broader assets are proposed future work, not completed results.
- Only three categories and one reconstructed site were demonstrated. No safety outcome reduction or production reliability result is measured.
- The paper's promised repository, [tsl-imperial/ConSynth](https://github.com/tsl-imperial/ConSynth), returned 404 on this review. This is an explicit reproducibility blocker; no private or removed repository was accessed.
- Applicable engineering lesson: decompose simulation into geometry, motion, observation, annotation and validation, then evaluate within-domain, cross-domain and actual-target behavior separately. Preserve negative transfer and absolute metric levels alongside relative gains.
- Before adoption: define the metric exactly, split by sequence/site, audit render/annotation synchronization, document seeds and parameters, test minority/occluded classes, and quantify survey/render/training costs. Those are analyst recommendations grounded in the gaps, not claimed personal preferences of Wu.
