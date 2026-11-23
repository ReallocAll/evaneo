<!-- retrieval: {"source_ids":["public:thread:fusesource/jansi:34"],"source_type":"public","date":"2015-05-13","topics":["concurrency","ffi","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="fusesource-jansi-34-isatty-test-on-windows-8-1-64bit"></a>
# fusesource/jansi#34: isatty test on windows 8.1 64bit {#fusesource-jansi-34-isatty-test-on-windows-8-1-64bit}

Source: https://github.com/fusesource/jansi/issues/34

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Windows 8.1 native cmd, Cygwin terminal and Emacs shell differ in isatty results and WindowsAnsiOutputStream construction, especially when piped.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Reporter proposes falling back to generic ANSI output when not a native TTY. Vincent adds a separate cmd.exe color-not-shown report after AnsiConsole.systemInstall, without an isolated reproducer. Maintainer closes old tickets years later without diagnosis.

## Implementation and attribution {#implementation-and-attribution}
Inline commands/results distinguish raw OS terminal detection from ANSI display capability; no implementation patch or confirmed resolution.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Not established that all shells share one cause. Closing stale reports is not a fix.

## Reusable decision and costs {#reusable-decision-and-costs}
Treat terminal identity, ANSI handling and redirection as separate capabilities; preserve the environment matrix before changing output wrappers.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2015-05-24T11:03:55Z](https://github.com/fusesource/jansi/issues/34#issuecomment-105001629).
- [davsclaus · 2021-10-03T18:43:02Z](https://github.com/fusesource/jansi/issues/34#issuecomment-933004302).
