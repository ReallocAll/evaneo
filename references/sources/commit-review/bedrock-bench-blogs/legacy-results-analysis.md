<!-- retrieval: {"source_ids":["public:commit:0a49c6914171a3d325adfca5bc50cf612ea4cb8e","public:commit:655e3e486185341520890621f65d9b69a9b6067d","public:commit:f1d4ef7430a3178564950a282780a28fff77cc00"],"source_type":"public","date":"2026-10-12","topics":["concurrency","testing","performance","diagnosis","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="legacy-result-contents-18-file-review"></a>
# Legacy result contents: 18-file review {#legacy-result-contents-18-file-review}

<a id="coverage-and-provenance"></a>
## Coverage and provenance {#coverage-and-provenance}

All 18 result files added under `published/legacy-0.11.14/results/` by f1d4ef7430a3178564950a282780a28fff77cc00 are substantively reviewed: nine JSON objects, three Markdown comparisons and six Windows console summaries. Full prose and JSON structures/values were read. Three long chaos transcripts received complete line classification, all nonrepetitive setup/summary/warning/error-family reading and structured verification of every monitor sample and repetitive action/event family. This is explicit generated-data reduction, not a claim that every repeated bot name was independently interpreted. No upstream code, binary or analysis program was executed.

A prior static comparison mapped every published file to its original Git blob and path in the initial import (ordinal 0) and ordinal 2. All 18 originals at those trees match their legacy blobs at ordinal 7. Seventeen published copies are identical Git blobs; chaos-after-win is the declared UTF-16→UTF-8/LF conversion, normalized-content identical. That historical comparison also reported matching declared SHA-256 values; those values have not been independently recalculated for this Skill. These are reused occurrences of experiments, not independent replications. Authorship of the containing documentation/import does not establish who personally conducted each experiment; preserve the files as project-reported measurements.

The lost raw run directories and incompletely retained steady bot source/hash prevent re-analysis or precise reproduction. Windows final's DLL prefix85262df56bbd64e4 and chaos's ed43d5e170ccb982 are different prerelease builds behind a 0.11.13 version banner. Linux steady uses dev10; chaos uses dev4. The vanilla JSON's wheel field denotes the environment, not an Endstone implementation under test. The release label0.11.14 must never replace these identities.

## Windows steady outputs {#windows-steady-outputs}

`begin-01113.out`: 100 players occupy100 cells with max1/cell, worst offset107 blocks. Settle329.3s; join median3.78/p905.48; historical view t90 median189.03/p90208.97/max456.94, n100, measured from60-second bot lines. Whole steady TPS11.23166 differs from median5-second TPS11.28 (min10.41, n19). MC_SERVER996ms/s; DevTools701ms/s persists. Earlier idle DevTools683 and loading774 show real overhead. Profiler window/whole loading differ: storm_prof19.24TPS, storm_full11.75TPS. During settle, repeated teleports and55 airborne nudges modify loading. Server exits0, reported errors0.

`final-100.out`: same100-cell layout, worst offset92.3; settle300.5s; t90 median80.54/p90206.77/max419.63, n100. Median steady20TPS, min19.85,n18; whole steady20.00112; main857ms/s (about42.85 CPUms/tick). DevTools0. First60s streaming threads all seven near759–769ms/s; whole load averages171–181 each, a different window. Steady private4857.4MiB, WS4094.2; loading private4808.1, idle1118.5. One reteleport and no airborne nudges. No logged errors, exit0. Improved median view loading does not erase the p90≈207-second tail.

`vanilla-100.out`: settle326.9s; t90 median191.47/p90247.13/max451.9,n100; steady median9.4/min4.96,n18 versus whole-window9.23733TPS. Main971ms/s divided by whole TPS gives≈105.12 CPUms/tick, whereas dividing median9.4 yields103.30; the comparison sheet's103.3 and blog≈105 reflect different denominators. No DevTools. Private4063/WS4051.5 steady. Airborne58 nudges appear twice. Eight logged ERROR lines are the startup NetherNet transport banner despite successful bot joins, illustrating why raw severity counts require categorization. `_interim.md` says0 vanilla errors and `_ref_check.md`2, whereas this console says8; scopes/filters are not recoverable enough to silently reconcile them.

## Linux steady JSON {#linux-steady-json}

All three report100 joined, no failed/dropped/dead bots,100 occupied cells, no foreign process list, completed=true, exit0, crashed=false. Server CPU mask0–15, bots16–27. PYPI0.11.13: steady median9.49/window9.45/min15s9.1, main1000ms/s/105.85ms per tick; load median9.4/window10.03/min15s0.95; settle302s. Vanilla:9.48/9.46/9.11, main1000/105.72; loading8.87/9.32/0.92; settle301s. Dev10 wake0:20/20/20, main930/46.5; loading19.96/18.72/7.95; settle302s.

Their t90 median/p90/max are192.231/208.809/385.302,194.197/208.621/391.627 and130.486/242.552/388.036 seconds respectively. The faster dev10 median coexists with a worse p90 than either comparator: do not summarize as uniform latency improvement. Chunk medians97 in all; means99.58/102.98/102.9, minimum69/77/69. PYPI bot uniq_total9952 differs from99.58×100=9958, a six-chunk internal discrepancy; preserve rather than repair. Vanilla10298 and dev1010290 align with means. RSS steady4059/3955/4539MiB; settle-only peaks4004/3922/4506 can legitimately be lower than later steady memory because phases differ. Process steady cores1.11/1.09/1.09, load2.2/2.18/2.48. Wake0 load workers seven>100ms/s, sum1501; steady none>100,sum71. Its errors/warnings0 are reported, not independent correctness validation.

## Linux chaos JSON {#linux-chaos-json}

All four last900s and report no crash, zero exit, zero verification lines and null verification cleanliness. Empty verification details mean no behavior-equivalence evidence. Regime TPS medians for randomtickspeed0/1/3/100/1000:

| File | all/normal/high monitor median | Regime medians | Applied/queued changes |
|---|---|---|---|
| chaos-after-r2 |19.1/19.3/10.78|19.45/19.28/19.28/15.49/2.85|29/30|
| chaos-after |15.01/17.16/5.77|18.04/16.01/17.02/11.52/2.6|30/30|
| chaos-pypi01113 |7.49/10.15/3.37|11.85/9.21/11.04/5.67/1.88|30/30|
| chaos-vanilla |12.7/14.84/4.73|13.61/14.84/15.79/9.56/2.53|30/30|

Each89 monitor samples, with different regime occupancy. The dev4 rerun spends116/384/168/113/119s per regime; contaminated dev4 spends143/316/134/146/161; PYPI totals901s from rounded bins; vanilla totals900. A global median therefore is not a fixed-workload comparison. PYPI five-second all/normal/high7.64/10.53/3.58 differs from monitor medians; vanilla12.36/14.49/4.11 likewise. R2 changes waypoint dialect from boolean true/false to everyone/off: its improvement is not a clean machine-contention-only rerun. R2 error/command-feedback counts3/1274 versus589/573, PYPI0/1490, vanilla0/3371. Error-free engine logging still coexists with failed commands.

Dev4 process cores are null, not zero; PYPI3.58 and vanilla3.33. RSS start/end/peak: r25396/4932/5423, first5380/4664/5454, PYPI4820/5180/5180, vanilla4649/5057/5057MiB. Threads23/23,23/23,51/51,19/19. Different command/action, disconnect and reconnect outcomes remain in the complete parsed JSON audit. These short chaos windows support an observed survival statement, not long-run leak freedom or equivalent correctness.

## Windows chaos transcripts: structured verification {#windows-chaos-transcripts-structured-verification}

Each has exactly60 monitor observations t=10…600s,20 explicit “no verify lines yet” messages and no steady phase (n0/null, not0TPS). The complete numeric monitor ranges and medians are not reproduced here; a prior static inspection reported that every cumulative event field is monotone. All20 action families are accounted for: blocks, churn/churn_one, cleanup, dimensions, far teleports, flash leaves, gamemode, kick, kill, randomtickspeed, stack/unstack, summon, tickingarea add/remove, view disconnect, waypoints on/off and weather. All four gamemodes, three dimensions, five randomtick regimes and three weathers appear. Locatorbar uses invalid true/false dialect here too. Repeated actor identifiers and coordinates are workload samples, not individual human information.

| Run | median/min monitor TPS | whole-window TPS | online min/median/final | max backlog | skipped actions | errors/command feedback |
|---|---|---|---|---|---|---|
| PYPI01113 |2.925/0.46|3.7021|25/72.5/36|223|171|108/522|
| after |17.2/1.08|12.7390|38/58/50|185|55|585/965|
| vanilla |4.485/0.68|5.9784|43/78/50|222|116|75/819|

294/515/410 CHAOS action lines differ substantially, even before skipped_backlog171/55/116 and list_status59/58/59. Online population collapses, making declining memory an especially weak leak argument. Main medians992.5/926/989ms/s, max1044/1017/1049 reflect sampling quantization, not literal extra physical cores for one thread. Private start→end4944→4236.2,4828→3210.1,4048.4→3578.4MiB. Linear rates in the summaries are not simply endpoint differences: after handles634→641 yet slope−29.37/hour. Preserve rate semantics as reported; don't “correct” their sign from endpoints.

All report crash=false and server exit0, but there are12/11/19 `on_event failed: ValueError('I/O operation on closed file.')` messages around shutdown despite empty harness_errors. The after run explicitly warns of foreign loadbot processes at idle, load, settled and end. This is direct contamination evidence, not a speculation from the blog. Error families include null-context teleport/fill/setblock/summon/loot, failed summons, block placement, selector misses, transport banner and vanilla unknown status command. Displayed ERRLINE examples repeat earlier errors and are only excerpts; their frequency is not the total failure count. Total log_errors632/1550/896 uses a broader scope than chaos error_lines.

Final rejoin failures260/195/155 and giveups52/39/23; read failures12/26/10. Final not_respawned lists contain3/2/2 bots even when aggregate deaths equal respawns, so aggregate count equality is insufficient per-identity correctness. Last after monitor DIMDONE83 becomes84 in summary, showing snapshot timing, not a reason to rewrite the monitor. t90 outputs n72/76/80 with medians380.88/143.04/297.38 are affected by chaos survival and historical accumulated chunks; they are not the steady100-bot view-loading benchmark.

## LeviLamina and cross-server evidence {#levilamina-and-cross-server-evidence}

`_interim.md` compares Levi optimized10.27TPS, contaminated Levi10.61, Endstone20, vanilla9.4. Main CPU1004/991/857/971ms/s; equivalent CPUms/tick97.8/93.4/42.9/103.3. Median view latency192/256.1/80.5/191.5s. First-minute worker sums2755/3547/5348/2543ms/s and active workers4/7,7/7,7/7,4/7. Foreign Minecraft process2784ms/s during contaminated loading, and differing Edge/lghub/System use, preclude treating all rows as clean controlled replicates. `_ref_check.md` cross-checks two references but does not supply independent runs.

Levi optimized chaos lasts601s, no crash, exit0. Queued normal-randomtick median1.4TPS versus actually executed normal9.42 (five-second series); monitor counterparts1.38 versus9.5. Only6 executed changes for7 queued;427s at1000. Global monitor1.23/five-second1.25 median is dominated by actual high load. Skipped backlog187, command errors475, summary error lines38, four unrespawned bots,295 rejoin failures and59 giveups undermine “same nominal commands” equivalence. Its eight chaos-specific errors are invalid locatorbar tokens; other severity counts include startup transport banner and a CrashLogger-enabled message. Missing validator output remains missing.

`custom-servers/comparison.md` juxtaposes six incomparable contexts: Endstone dev reference, PMMP nolimit, fresh PNX, pregenerated PNX, Dragonfly and pregenerated Nukkit. Steady medians19.99/4.62/1.34/4.25/19.99/20; loading minima18.61/1.54/0.69/1.66/14.57/0.69. Pregen PNX raises TPS but uses7.39 steady cores versus3.67 fresh; private≈17GiB, not a free improvement. Dragonfly no native tick-thread CPU metric and zero join quantiles are not evidence of zero cost. Fresh PNX never filled the requested view (16 unique chunks); DF461/PMMP456/Nukkit480 differ drastically from Endstone103. Settle capped runs and inconsistent memory endpoints prevent one ranking. No-crash observations coexist with errors, omitted actions and15 DF killed bots never respawned.

`endstone-ref.json` has median view latency132/p90256,n99 and final minimum unique0, not the final release's80.54-second median. First-five-minute chaos median2.02 differs from full10-minute17.2; this JSON's reported end memory3488WS/4280.7private also differs from the full chaos-after console's2468.2/3210.1. Keep these as distinct summary scopes/artifacts even though many action/error totals align. Do not merge their endpoints or call them identical reruns.

## Reusable conclusions {#reusable-conclusions}

Store binary, bot and scenario identity; retain actual command-application timing and completion, phase-specific windows, sample denominators and tails; make contamination and missing verification fatal to claims that require them. Record survival separately from correctness, and throughput separately from workload completed. Preserve historical published numbers while making their narrower evidential scope explicit. All figures here are archive observations, not a new experiment or current product ranking.
