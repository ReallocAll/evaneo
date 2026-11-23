<!-- retrieval: {"source_ids":["public:thread:netty/netty:5893"],"source_type":"public","date":"2016-10-05","topics":["concurrency","testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="netty-netty-5893-server-stops-working-after-the-exceptioncaught-being-called"></a>
# netty/netty#5893: Server stops working after the exceptionCaught being called {#netty-netty-5893-server-stops-working-after-the-exceptioncaught-being-called}

Source: https://github.com/netty/netty/issues/5893

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
A UDP server using Netty 4.1.4.Final stopped receiving after java.net.SocketException, “Network dropped connection on reset: no further information,” from DatagramChannelImpl.receive through NioDatagramChannel.doReadMessages. The application only logged exceptionCaught; Vincent explicitly denied closing the channel there. The failure was intermittent, with no deterministic reproducer.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
normanmaurer first separated framework/version, precise exception class, and application close policy. The reporter confirmed plain SocketException rather than another IOException subtype. The maintainer linked #5899, later closed the issue as fixed. In that linked PR, the maintainer introduced a transport-specific read-error policy. nmittler asked about RuntimeException/Error; the author explicitly preferred preserving prior behavior rather than broadening this change. Scottmitch requested a unit test, but the author could not identify how to produce this platform-specific condition. Scottmitch also proposed simplifying the base predicate; this suggestion was accepted. The PR itself was closed unmerged after cherry-picks into 4.1 and 4.0, not rejected.

## Implementation and attribution {#implementation-and-attribution}
Vincent supplied the reproducer context and clarified application behavior; normanmaurer authored the fix, with nmittler and Scottmitch reviewing. Full two-file PR #5899 patch and all captured 18 review/comment records were read, plus the full two-file 4.1 cherry-pick e102a008b63d0063581ba242539f0a8d473cae00. AbstractNioMessageChannel moves close classification into protected closeOnReadError(Throwable). NioDatagramChannel overrides it to return false for SocketException, allowing subsequent datagrams. Important independent code finding: the extracted base predicate uses `this instanceof ServerChannel`, whereas the old assignment used its negation. This reverses the old ServerChannel/non-ServerChannel behavior for non-PortUnreachable IOException and contradicts the adjacent comment that server channels should remain open. The same predicate exists in the inspected 4.1 cherry-pick, so it is not merely a discarded review hunk. Do not copy that base predicate as a universally correct pattern.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
The issue is closed as fixed and a concrete 4.1 cherry-pick is verified; the PR also names a 4.0 cherry-pick, not independently inspected. No reporter retest, deterministic test, or throughput measurement is recorded. The initial linked PR body/title have a truncated opening, but its readable motivation, complete changed-file patch and full review exchange support the UDP mechanism; no missing opening text is invented. Findings describe the historical 2016 revision, not current Netty behavior.

## Reusable decision and costs {#reusable-decision-and-costs}
Exception class alone does not determine whether a transport remains usable. Separate notification from close policy and allow transport overrides; preserve other subtype semantics when extracting predicates. Review simplification requires a truth-table check, especially when a previous negation crosses a helper boundary.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [normanmaurer · 2016-10-05T10:24:40Z](https://github.com/netty/netty/issues/5893#issuecomment-251637857).
- [wu-vincent · 2016-10-05T10:43:00Z](https://github.com/netty/netty/issues/5893#issuecomment-251641316).
- [normanmaurer · 2016-10-05T10:55:42Z](https://github.com/netty/netty/issues/5893#issuecomment-251643569).
- [wu-vincent · 2016-10-05T10:57:43Z](https://github.com/netty/netty/issues/5893#issuecomment-251643924).
- [normanmaurer · 2016-10-05T11:01:17Z](https://github.com/netty/netty/issues/5893#issuecomment-251644580).
- [wu-vincent · 2016-10-05T11:01:39Z](https://github.com/netty/netty/issues/5893#issuecomment-251644644).
- [normanmaurer · 2016-10-05T11:14:27Z](https://github.com/netty/netty/issues/5893#issuecomment-251646871).
- [normanmaurer · 2016-10-06T16:15:14Z](https://github.com/netty/netty/issues/5893#issuecomment-252012159).
- [wu-vincent · 2016-10-07T05:05:27Z](https://github.com/netty/netty/issues/5893#issuecomment-252153902).
- [normanmaurer · 2016-10-10T08:37:43Z](https://github.com/netty/netty/issues/5893#issuecomment-252561670).
