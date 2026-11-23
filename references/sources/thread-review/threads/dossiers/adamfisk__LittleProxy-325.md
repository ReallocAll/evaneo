<!-- retrieval: {"source_ids":["public:thread:adamfisk/LittleProxy:325"],"source_type":"public","date":"2016-12-08","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="adamfisk-littleproxy-325-how-to-install-littleproxy-cert-on-android-devices"></a>
# adamfisk/LittleProxy#325: How to install littleproxy cert on Android devices? {#adamfisk-littleproxy-325-how-to-install-littleproxy-cert-on-android-devices}

Source: https://github.com/adamfisk/LittleProxy/issues/325

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Android rejected the proxy-generated HTTPS certificate. The reporter could not import the repository certificate file.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
ldn0x7dc demonstrated supplying a PKCS12 certificate source to ImpersonatingMitmManager, then installing the corresponding CA on the test device. jekh clarified BrowserMob’s MITM module works independently of the full BrowserMob Proxy; versions cited were mitm 2.1.2 with LittleProxy 1.1.0. Vincent asked status and later reported littleproxy-mitm worked for him.

## Implementation and attribution {#implementation-and-attribution}
The inline example constructs KeyStoreFileCertificateSource, passes it to rootCertificateSource and sets the bootstrap MITM manager. Example credential literals are deliberately not replicated. No project patch is linked. Certificate/key ownership and trust deployment are separate from importing a random repository artifact.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Reporter supplies a working configuration path; Vincent reports success with a related module, not necessarily the identical Charles-export setup. No security setting was changed or certificate installed during this review.

## Reusable decision and costs {#reusable-decision-and-costs}
A TLS interception library needs an explicitly selected root key/certificate and matching client trust. Reuse modular functionality independently of its larger host application; keep private key material out of recipes and reports.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2017-01-10T13:53:18Z](https://github.com/adamfisk/LittleProxy/issues/325#issuecomment-271580513).
- [ldn0x7dc · 2017-01-12T05:53:57Z](https://github.com/adamfisk/LittleProxy/issues/325#issuecomment-272082613).
- [jekh · 2017-01-12T07:10:51Z](https://github.com/adamfisk/LittleProxy/issues/325#issuecomment-272092776).
- [ldn0x7dc · 2017-01-12T10:11:48Z](https://github.com/adamfisk/LittleProxy/issues/325#issuecomment-272124615).
- [wu-vincent · 2017-01-12T10:49:43Z](https://github.com/adamfisk/LittleProxy/issues/325#issuecomment-272132793).
