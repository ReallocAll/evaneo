<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2026-03-23","topics":["testing","maintainability","complexity","review","onboarding","examples","scope"],"limitations":"Static review of linked primary sources and bundled historical analyses; upstream tests were not executed. Historical claims and code changes are distinguished from proven runtime outcomes."} -->
# Official Endstone starter plugins: omit demos unrelated to the teaching contract {#case}

## Two independent template simplifications {#changes}

The historical comparison in [initialization-lessons.md](../../sources/commit-review/plugin-examples-all/initialization-lessons.md) traces March 2026 changes to both official starter repositories. The [C++ template reset de2cf164](https://github.com/EndstoneMC/cpp-example-plugin/commit/de2cf164f859aa955de351b47e790ba82231498e) removed advanced Fibonacci/whoami/server-load demonstrations, keeping a narrower hello/broadcast and player lifecycle entry path. The [Python template reset 383c855c](https://github.com/EndstoneMC/python-example-plugin/commit/383c855c22919483e578f1e335d1469801acbb60) removed the separate executor, scheduling and permission-attachment demonstrations to emphasize basic lifecycle/config/events. Some demonstrations were later selectively restored after identifying a teaching need.

## Judgment {#reading}

A starter repository has a different risk profile from a production library: maintainable onboarding means showing the minimum complete use case and one clear extension route, not exhaustively demonstrating the framework. Tests and workflow setup should not dominate a learning template merely to showcase infrastructure.

## Limit {#limits}

These commits are *educational scope reductions*, not evidence that production plugins should omit scheduler or permission tests. Other build and docs changes in the same resets may have increased overall repository complexity.
