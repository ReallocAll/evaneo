<!-- retrieval: {"source_ids":["public:external:paper-routing"],"source_type":"public","topics":["testing","performance","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="walking-school-bus-routing-explicit-objectives-and-bounded-optimization"></a>

# Walking-school-bus routing: explicit objectives and bounded optimization {#walking-school-bus-routing-explicit-objectives-and-bounded-optimization}


## Provenance, attribution and actual scope {#provenance-attribution-and-actual-scope}

[Published paper, DOI 10.1002/mcda.1803](https://doi.org/10.1002/mcda.1803): Judith Y. T. Wang, Zhengyu Wu, Yating Kang, Edward Brown, Mengfan Wen, Christopher Rushton and Matthias Ehrgott, *Journal of Multi-Criteria Decision Analysis* 30(3–4), 109–131 (2023). The [White Rose record](https://eprints.whiterose.ac.uk/id/eprint/198393/) links the open CC BY 4.0 published PDF. Table 1 and Table 2 were visually checked because rotated extraction and threshold details matter. Other diagrams/maps were reviewed through captions and surrounding text, not comprehensively image-audited; the cited studies are not independently reviewed here.

The acknowledgments credit Dr Jon Pearce with providing the multi-objective shortest-path computer program.

## Problem and boundaries {#problem-and-boundaries}

Shortest travel time alone misses pollutant exposure, safety and enjoyment. The authors formulate a walking network and three additive objectives, then enumerate nondominated routes rather than force one unexplained weighted total. The practical decision-maker can trade marginal time against dose and walkability.

This is optimization *between preselected stops in a predetermined sequence*. It does not jointly optimize stop placement, sequence, volunteer assignment, or timetables. The case-study stops are chosen so most local homes fall within roughly 100 m (1–2 minutes) of one. Stop location, stop sequencing and driver scheduling are explicitly future research. Outcomes are modeled routes, not a trial proving adoption or health improvement.

## Representation before optimization {#representation-before-optimization}

Busy roads have separate sidewalk links on each side; intersections have crossing links with waiting time. Quiet residential roads can use a single link when side distinctions are immaterial. Site visits add footpaths missing from the map. This level of representation permits side-dependent pollution and explicit crossing choices. It is more important than choosing an optimizer over an oversimplified road-centerline graph.

The authors deliberately distinguish walking-link properties from crossing-link properties. Sidewalk width, buffers, traffic, lighting, surface, trees and parking characterize walking segments; crossings receive their own scoring, and nearby lighting etc. are represented on adjacent segments. This avoids silently double-counting the same road feature across different link types.

## Objective construction and assumptions {#objective-construction-and-assumptions}

1. Walking time: segment length divided by a fixed 1.29 m/s walking speed. Crossing time adds expected waiting. For signal cycles, expected wait is red-time squared divided by twice the full signal-cycle time. This is an expectation under an implicit arrival model, not a guaranteed bound or a stochastic simulation.
2. Pollutant dose: concentration × time × breathing rate, summed over walking and crossing links. The case uses 36 L/min breathing rate and calibrated Bradford Council pollution estimates at a 1 m × 1 m grid. Concentration along a link is weighted by length through each grid cell. Both NO2 and PM2.5 were modeled, but published route results show PM2.5.
3. Unwalkability: each feature receives 0/1/2 for good/medium/bad; weighted segment scores are accumulated with segment length. The sign convention makes all three objectives minimizations. The word “walkability” in result tables therefore denotes a cost: lower is better.

Table 1's weights are counts of mentions in reviewed literature: traffic speed 10, buffer 9, traffic volume 8, sidewalk width 8, surface condition 7, on-street parking 6, lighting 4, trees 4. These are explicit heuristic weights, not fitted causal effect sizes or measured community preferences. Planners can choose survey-derived alternatives.

Table 2 uses concrete and qualitative bins. One reproducibility issue is a literal gap in sidewalk-width thresholds: medium is 1.5–2.05 m and good starts at 2.20 m, leaving 2.05–2.20 m unspecified; this is visible in the PDF, not merely extraction corruption. Other qualitative bins need an assessment rubric to make independent observers agree. The case describes signalized crossings as bad, with link score 2; the general formulation also describes crossings as equivalent to bad walking links. Implementers should resolve normalization/units before reproducing the numeric score.

## Algorithm and compositional route construction {#algorithm-and-compositional-route-construction}

Each arc carries a three-component cost vector. A route is efficient when no alternative is at least as good in all components and strictly better in one. The paper employs a three-objective label-correcting extension of Bellman-style shortest paths. Efficient-path sets can be exponentially large in the worst case; favorable practical counts cited in other work are not a complexity guarantee.

For a stop sequence, compute efficient subroutes for each adjacent stop pair, combine candidate subroutes, then eliminate dominated whole routes. The case has five unique OD pairs shared across three lines, so the decomposition reuses intermediate work. Additivity is essential to this composition. Dynamic congestion, fatigue, synchronized crossing arrivals, capacity, prohibited repeated segments or nonlinear dose responses would need explicit extra state or constraints before this decomposition could safely be reused.

## Concrete case and results {#concrete-case-and-results}

The Bradford school case distinguishes the busy main roads, a constrained traffic island, quieter residential streets and green footpaths. Three chosen lines have 1, 3 and 4 efficient route options respectively. Line A's footpath route is simultaneously best for all objectives, a useful counterexample to assuming every multiobjective task must expose a trade-off.

For line B, shortest time is 661.77 s with dose 3.645 μg; the minimum-dose option takes 664.93 s for 3.639 μg; the best walkability route takes 711.32 s with dose 3.883 μg. Thus a “safer/more comfortable” modeled path can increase exposure because it takes longer, even when it avoids some road frontage. For the expanded line C, the quickest option takes 864.62 s versus line B's 661.77 s: +202.85 s, about 3.38 minutes, to serve an additional stop. Its four route options occupy only about 5.37 s of travel-time spread, while changing the other objectives. The reported numerical differences are model outputs, not measured intervention effects or statistically distinguished estimates.

## Limitations and reusable engineering checks {#limitations-and-reusable-engineering-checks}

- Input precision matters: a fine-grained optimizer does not rescue coarse, stale or unavailable concentration data. The Council data were licensed and cannot be redistributed by the authors; independent numerical reproduction is blocked without suitable data.
- Fixed speed, fixed breathing rate, average signal waits and a static pollution map simplify real variability. Sensitivity analysis of these constants and measurement error is not reported.
- “Safety” is a composite perceived-safety/comfort score. It is not a calibrated crash probability or evidence that a route is safe for a particular child.
- No public program source, runtime benchmark, solver test suite, or performance scaling experiment is supplied in the paper. No code was run in this review.
- Separate optimization scope from downstream decisions: route selection, budget, staffing and demand coverage remain decisions for the planner. Do not claim the paper solves the complete operational problem.
- Portable use: before tuning an algorithm, make units, link semantics, additive assumptions and unresolved bins explicit; keep a Pareto set when stakeholder objectives genuinely conflict; retain data provenance and test dominance filtering with counterexamples. These are analyst-derived application checks grounded in the paper's identified gaps.
