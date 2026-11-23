<!-- retrieval: {"source_ids":["public:thread:Karumi/Dexter:107"],"source_type":"public","date":"2017-01-16","topics":["testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="karumi-dexter-107-caused-by-java-lang-nullpointerexception-attempt-to-invoke-virtual-method-void-com-karumi-dexter-dexterinstance-"></a>
# Karumi/Dexter #107: Caused by java.lang.NullPointerException: Attempt to invoke virtual method 'void com.karumi.dexter.DexterInstance.onActivityReady(android.app.Activity)' on a null object reference {#karumi-dexter-107-caused-by-java-lang-nullpointerexception-attempt-to-invoke-virtual-method-void-com-karumi-dexter-dexterinstance-}

Source: https://github.com/Karumi/Dexter/issues/107

## Evidence and attribution {#evidence-and-attribution}

Primary author: cioraneanu. Created 2017-01-16T13:23:12Z; recorded state closed; merged not applicable.

## Permission activity recreation: concrete reproduction, then later regressions {#permission-activity-recreation-concrete-reproduction-then-later-regressions}
cioraneanu reports Dexter3.0.0 null DexterInstance from permission activity creation; several users confirm only crash telemetry. xoex associates it with revoking permissions in Android settings and returning, even on3.0.1. Wu first says same here, then hypothesizes activity recycling and gives finishing the requesting activity immediately as his observed trigger. These are contribution-level observations, not authorship of the eventual fix.
Serchinastico reproduces settings/revoke/return and releases3.0.2 null guarding absent Dexter instance; it avoids the crash when the library has no request state to resume. No claim that lost permission workflow is reconstructed. Later4.1.0 reports fail during activity destruction and4.2 during permission result Activity.finish on null, so a single creation guard is not comprehensive lifecycle correctness. Full traces/comments read; no library patch linked or inspected. This is a separate mature-project case, not Endstone implementation evidence.

## Code and verification boundary {#code-and-verification-boundary}

No associated patch is supplied in this thread. Lifecycle reasoning and release claims are scoped to the captured discussion; Dexter implementation not independently audited. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/Karumi/Dexter/issues/107
- https://github.com/Karumi/Dexter/issues/107#issuecomment-274538844
- https://github.com/Karumi/Dexter/issues/107#issuecomment-275850400
- https://github.com/Karumi/Dexter/issues/107#issuecomment-276064864
- https://github.com/Karumi/Dexter/issues/107#issuecomment-276070405
- https://github.com/Karumi/Dexter/issues/107#issuecomment-276071816
- https://github.com/Karumi/Dexter/issues/107#issuecomment-276073978
- https://github.com/Karumi/Dexter/issues/107#issuecomment-276079396
- https://github.com/Karumi/Dexter/issues/107#issuecomment-276086946
- https://github.com/Karumi/Dexter/issues/107#issuecomment-276088873
- https://github.com/Karumi/Dexter/issues/107#issuecomment-276134234
- https://github.com/Karumi/Dexter/issues/107#issuecomment-276268823
- https://github.com/Karumi/Dexter/issues/107#issuecomment-276292347
- https://github.com/Karumi/Dexter/issues/107#issuecomment-276299951
- https://github.com/Karumi/Dexter/issues/107#issuecomment-276668634
- https://github.com/Karumi/Dexter/issues/107#issuecomment-276709690
- https://github.com/Karumi/Dexter/issues/107#issuecomment-345286100
- https://github.com/Karumi/Dexter/issues/107#issuecomment-350445232
- https://github.com/Karumi/Dexter/issues/107#issuecomment-354088303
