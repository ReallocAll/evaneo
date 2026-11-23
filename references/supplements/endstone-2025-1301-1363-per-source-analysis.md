<!-- retrieval: {"source_ids":["public:commit:04382f6c1f157046339225ab6de16204e13d6763","public:commit:06ce8871e4ce49b09079845f097f839e23a094e5","public:commit:0b41fe71d2921b915480e5cefd607d56204ae313","public:commit:0d0c48ebbed993642ae800cb12db5c182e9a2c2d","public:commit:15ed7ff932eb79239933e368e40cfc0a9d5d3e21","public:commit:1608ef01e8c8a89abddf3151d39ccbc39e032801","public:commit:1841a88a5fda378e8524b97a277b4d182ed06871","public:commit:2597eeca495d0d4d94f0e600974aca1b1d84b3ad","public:commit:28ba71750246e378d0f583cb0a365f9c4b27d542","public:commit:2b1d39150120d90b9fccf3a331e4402122feca57","public:commit:2e9873f0a61452f18127360655bc976896a58231","public:commit:32860a1c09628326b28812bb6fe0d134f84f6a49","public:commit:38b262298ac192ba1a81250d4f39737e88cb50d8","public:commit:38bfc6c53df32792d1ec798ab61ae8254272c762","public:commit:39ce1ba35ea97ff336b9eff838e2dde6e5d84c7e","public:commit:3e81975a9b69da1870039c5b10a568f4f940fe34","public:commit:400184c491022c25f53cdd563989dbb0f06d7d08","public:commit:42f5b9d1196591139d33345e555c68397d71d0e6","public:commit:4524abbb91e61b00af509e7d1c2daa782f718458","public:commit:469c32717bf0113089c16db2bd220c15eff6489c","public:commit:4816aef277f86290cef18daf14aeee2d0904bca4","public:commit:577e472c2b6e399ca346cf4b0564162875f5c6af","public:commit:57b966951a4a124042b59905607fdd72d9d64a4b","public:commit:5aa11cc6a93c9f8c78813b00335dcf19af066b41","public:commit:641d0eec3c26c9a246ac072e33967e31ecda4207","public:commit:6c0e04b0a9c6cb531aa921161ec3fadef69649dc","public:commit:6e4b448c5533405c1e60d4751862472c76a2f335","public:commit:70cfe379eacc9214c29737b082acdd121ddeb505","public:commit:70ec2e3e11bf5c2c5375d1587a7680e33e844853","public:commit:71371baf85ad4dd260d3fd0ec6217c057427eea7","public:commit:73b97731312275fd488176f4c12ad55b6384fb14","public:commit:7f01cf0102ede5d1d780277078e7f8fd0387453e","public:commit:81d3ee0391bdae8e80b719db999b110c14e9ac7b","public:commit:823dc2388a832cca92462f7f8af189c7b201edd9","public:commit:85ff264f0c5b7cb883dca3f24e2772b2e73fb28c","public:commit:8b0babbe7dae604a1e84d8fb90aa5c431233c172","public:commit:91064e5fa25c4416f5f8782d7ba6004251a723bf","public:commit:911c1fef6bf1539d06c2b69f545cdaaa1111e10b","public:commit:92569ca1b2eda7acc2972022fc6ab260c0233fad","public:commit:937c70a5ac804567576ce3a5fbe6ecbaf2f66804","public:commit:96ee3a8d37421e697db0f30b31362c6e23822a12","public:commit:989771ee0388376e7d2d428360361f94ef82bf63","public:commit:9b5a77bb8e86d38cb7517e2c65fc9880356d3688","public:commit:a78b39c147581fc31aa88e2bd95f80b1d9d730c7","public:commit:a87b940e1d79d1cc5d677f0fe529d51e0a218e05","public:commit:b16ec4a30715f6c40c2b886ea520c9fd96e96d12","public:commit:b209f49ab18ba0e97d64e98bce40d5b877a28260","public:commit:b5fb6c8c55533a845417eb5c8fe85e70154a3dd4","public:commit:c7a25f0e6accd03a3a6964c7f643d4fcfcc77d0d","public:commit:ca42dc07c3da9bc55719e2143361cdb2c0afdb76","public:commit:d24e5f10ce3ab6a0315e7d313350d03799009a2f","public:commit:d379fa5dfef0046faa8983fd55e67d1a4b1d00c0","public:commit:da9b2316c79829f93579d15afdad095af7d57118","public:commit:dc6d78e0f2d48ffcb88fda15e53ddfd50a2fae85","public:commit:dd7736a5ff03deb59dde5653a1ecf909c5b25f2e","public:commit:e1db80635f8e0731595139b27fedae237db05e70","public:commit:e248c66f39d4fe184ef7f1eb539b9977e89ae39c","public:commit:ef36db7c2b6460580fa5d88ce63473a0d5b4e4d0","public:commit:f0cbdedc05d40ff10742ac3f1191c7098d50bd48","public:commit:f454f49adbad2448e66c3cafe497dd191fc38a74","public:commit:f66147f0c00e7575ca573d819131e7a7ade8a37d","public:commit:f6751f87e4411563c51d2bc8c165ca4fdbe6d376","public:commit:fce3b8e4b280df7cf2f6b0b3c483861c8bc0b73b"],"source_type":"public","date":"2025-11-15..2025-12-14","topics":["ffi","diagnosis","documentation","review","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Additional per-source analysis and source qualifications {#additional-per-source-causal-analysis}

These supplemental notes record commit-specific engineering observations and evidence limits alongside the main source analyses. Public commit links identify the inspected revisions; no runtime result is independently verified here. A repeated review-scope qualification describes a limit of the analysis, not necessarily a change made by every listed commit.

<a id="commit-641d0eec3c26c9a246ac072e33967e31ecda4207"></a>
## feat: implement `Actor::_setDimensionTransitionComponent` {#commit-641d0eec3c26c9a246ac072e33967e31ecda4207}

### Provenance {#commit-641d0eec3c26c9a246ac072e33967e31ecda4207-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/641d0eec3c26c9a246ac072e33967e31ecda4207

Source date: 2025-11-16T19:44:00Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-ca42dc07c3da9bc55719e2143361cdb2c0afdb76"></a>
## fix: add missing exports {#commit-ca42dc07c3da9bc55719e2143361cdb2c0afdb76}

### Provenance {#commit-ca42dc07c3da9bc55719e2143361cdb2c0afdb76-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/ca42dc07c3da9bc55719e2143361cdb2c0afdb76

Source date: 2025-11-16T20:21:34Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-d379fa5dfef0046faa8983fd55e67d1a4b1d00c0"></a>
## chore: update BDS to v1.21.123.2 {#commit-d379fa5dfef0046faa8983fd55e67d1a4b1d00c0}

### Provenance {#commit-d379fa5dfef0046faa8983fd55e67d1a4b1d00c0-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/d379fa5dfef0046faa8983fd55e67d1a4b1d00c0

Source date: 2025-11-17T16:41:27Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-937c70a5ac804567576ce3a5fbe6ecbaf2f66804"></a>
## Merge remote-tracking branch 'origin/v0.10' into v0.10 {#commit-937c70a5ac804567576ce3a5fbe6ecbaf2f66804}

### Provenance {#commit-937c70a5ac804567576ce3a5fbe6ecbaf2f66804-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/937c70a5ac804567576ce3a5fbe6ecbaf2f66804

Source date: 2025-11-17T16:46:56Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-8b0babbe7dae604a1e84d8fb90aa5c431233c172"></a>
## fix: resolve compilation errors {#commit-8b0babbe7dae604a1e84d8fb90aa5c431233c172}

### Provenance {#commit-8b0babbe7dae604a1e84d8fb90aa5c431233c172-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/8b0babbe7dae604a1e84d8fb90aa5c431233c172

Source date: 2025-11-15T03:11:54Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-da9b2316c79829f93579d15afdad095af7d57118"></a>
## fix: patch a vulnerability caused by improperly sized certificate chains {#commit-da9b2316c79829f93579d15afdad095af7d57118}

### Provenance {#commit-da9b2316c79829f93579d15afdad095af7d57118-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/da9b2316c79829f93579d15afdad095af7d57118

Source date: 2025-11-17T20:22:17Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-2e9873f0a61452f18127360655bc976896a58231"></a>
## fix: add input size validation in `UnverifiedCertificate::fromString` {#commit-2e9873f0a61452f18127360655bc976896a58231}

### Provenance {#commit-2e9873f0a61452f18127360655bc976896a58231-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/2e9873f0a61452f18127360655bc976896a58231

Source date: 2025-11-17T20:56:28Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-9b5a77bb8e86d38cb7517e2c65fc9880356d3688"></a>
## feat: add `StringByteInput` {#commit-9b5a77bb8e86d38cb7517e2c65fc9880356d3688}

### Provenance {#commit-9b5a77bb8e86d38cb7517e2c65fc9880356d3688-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/9b5a77bb8e86d38cb7517e2c65fc9880356d3688

Source date: 2025-11-17T23:17:04Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-73b97731312275fd488176f4c12ad55b6384fb14"></a>
## feat: add `readNamedCompoundTag` and `readOrGetEmpty` methods to `NbtIo` {#commit-73b97731312275fd488176f4c12ad55b6384fb14}

### Provenance {#commit-73b97731312275fd488176f4c12ad55b6384fb14-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/73b97731312275fd488176f4c12ad55b6384fb14

Source date: 2025-11-18T00:08:34Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-81d3ee0391bdae8e80b719db999b110c14e9ac7b"></a>
## fix: resolve a vulnerability in item deserialisation that can cause the server to hang {#commit-81d3ee0391bdae8e80b719db999b110c14e9ac7b}

### Provenance {#commit-81d3ee0391bdae8e80b719db999b110c14e9ac7b-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/81d3ee0391bdae8e80b719db999b110c14e9ac7b

Source date: 2025-11-18T00:33:05Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-f6751f87e4411563c51d2bc8c165ca4fdbe6d376"></a>
## feat: implement `ItemStackBase::_loadBlocksForCanPlaceOnCanDestroy` {#commit-f6751f87e4411563c51d2bc8c165ca4fdbe6d376}

### Provenance {#commit-f6751f87e4411563c51d2bc8c165ca4fdbe6d376-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/f6751f87e4411563c51d2bc8c165ca4fdbe6d376

Source date: 2025-11-18T00:56:32Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-dc6d78e0f2d48ffcb88fda15e53ddfd50a2fae85"></a>
## feat: update symbols.toml {#commit-dc6d78e0f2d48ffcb88fda15e53ddfd50a2fae85}

### Provenance {#commit-dc6d78e0f2d48ffcb88fda15e53ddfd50a2fae85-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/dc6d78e0f2d48ffcb88fda15e53ddfd50a2fae85

Source date: 2025-11-18T01:14:00Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-b5fb6c8c55533a845417eb5c8fe85e70154a3dd4"></a>
## fix: correct the implementation of `CompoundTag::load` and `ListTag::load` {#commit-b5fb6c8c55533a845417eb5c8fe85e70154a3dd4}

### Provenance {#commit-b5fb6c8c55533a845417eb5c8fe85e70154a3dd4-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/b5fb6c8c55533a845417eb5c8fe85e70154a3dd4

Source date: 2025-11-18T01:49:59Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-dd7736a5ff03deb59dde5653a1ecf909c5b25f2e"></a>
## chore: bump version to 0.10.12 {#commit-dd7736a5ff03deb59dde5653a1ecf909c5b25f2e}

### Provenance {#commit-dd7736a5ff03deb59dde5653a1ecf909c5b25f2e-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/dd7736a5ff03deb59dde5653a1ecf909c5b25f2e

Source date: 2025-11-18T01:57:53Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-911c1fef6bf1539d06c2b69f545cdaaa1111e10b"></a>
## Merge remote-tracking branch 'origin/v0.10' {#commit-911c1fef6bf1539d06c2b69f545cdaaa1111e10b}

### Provenance {#commit-911c1fef6bf1539d06c2b69f545cdaaa1111e10b-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/911c1fef6bf1539d06c2b69f545cdaaa1111e10b

Source date: 2025-11-18T13:25:58Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-1841a88a5fda378e8524b97a277b4d182ed06871"></a>
## feat: update symbols.toml {#commit-1841a88a5fda378e8524b97a277b4d182ed06871}

### Provenance {#commit-1841a88a5fda378e8524b97a277b4d182ed06871-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/1841a88a5fda378e8524b97a277b4d182ed06871

Source date: 2025-11-18T13:32:45Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-6c0e04b0a9c6cb531aa921161ec3fadef69649dc"></a>
## fix: resolve a dimension-related crash {#commit-6c0e04b0a9c6cb531aa921161ec3fadef69649dc}

### Provenance {#commit-6c0e04b0a9c6cb531aa921161ec3fadef69649dc-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/6c0e04b0a9c6cb531aa921161ec3fadef69649dc

Source date: 2025-11-18T13:50:53Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-ef36db7c2b6460580fa5d88ce63473a0d5b4e4d0"></a>
## chore: bump version to 0.10.13 {#commit-ef36db7c2b6460580fa5d88ce63473a0d5b4e4d0}

### Provenance {#commit-ef36db7c2b6460580fa5d88ce63473a0d5b4e4d0-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/ef36db7c2b6460580fa5d88ce63473a0d5b4e4d0

Source date: 2025-11-18T14:36:46Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-f454f49adbad2448e66c3cafe497dd191fc38a74"></a>
## fix: prevent packet spam from disconnected clients {#commit-f454f49adbad2448e66c3cafe497dd191fc38a74}

### Provenance {#commit-f454f49adbad2448e66c3cafe497dd191fc38a74-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/f454f49adbad2448e66c3cafe497dd191fc38a74

Source date: 2025-11-18T19:47:05Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-15ed7ff932eb79239933e368e40cfc0a9d5d3e21"></a>
## feat: enable packet rate limiting by default {#commit-15ed7ff932eb79239933e368e40cfc0a9d5d3e21}

### Provenance {#commit-15ed7ff932eb79239933e368e40cfc0a9d5d3e21-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/15ed7ff932eb79239933e368e40cfc0a9d5d3e21

Source date: 2025-11-18T19:47:21Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-91064e5fa25c4416f5f8782d7ba6004251a723bf"></a>
## chore: bump version to 0.10.14 {#commit-91064e5fa25c4416f5f8782d7ba6004251a723bf}

### Provenance {#commit-91064e5fa25c4416f5f8782d7ba6004251a723bf-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/91064e5fa25c4416f5f8782d7ba6004251a723bf

Source date: 2025-11-18T22:46:15Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-85ff264f0c5b7cb883dca3f24e2772b2e73fb28c"></a>
## feat: enable RakNet connection frequency limiting {#commit-85ff264f0c5b7cb883dca3f24e2772b2e73fb28c}

### Provenance {#commit-85ff264f0c5b7cb883dca3f24e2772b2e73fb28c-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/85ff264f0c5b7cb883dca3f24e2772b2e73fb28c

Source date: 2025-11-18T22:59:50Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-96ee3a8d37421e697db0f30b31362c6e23822a12"></a>
## refactor: clean up codes {#commit-96ee3a8d37421e697db0f30b31362c6e23822a12}

### Provenance {#commit-96ee3a8d37421e697db0f30b31362c6e23822a12-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/96ee3a8d37421e697db0f30b31362c6e23822a12

Source date: 2025-11-18T23:09:26Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-989771ee0388376e7d2d428360361f94ef82bf63"></a>
## Merge remote-tracking branch 'origin/v0.10' {#commit-989771ee0388376e7d2d428360361f94ef82bf63}

### Provenance {#commit-989771ee0388376e7d2d428360361f94ef82bf63-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/989771ee0388376e7d2d428360361f94ef82bf63

Source date: 2025-11-18T23:12:06Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-c7a25f0e6accd03a3a6964c7f643d4fcfcc77d0d"></a>
## feat: add support for v1.21.124.2 {#commit-c7a25f0e6accd03a3a6964c7f643d4fcfcc77d0d}

### Provenance {#commit-c7a25f0e6accd03a3a6964c7f643d4fcfcc77d0d-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/c7a25f0e6accd03a3a6964c7f643d4fcfcc77d0d

Source date: 2025-11-21T17:59:31Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-06ce8871e4ce49b09079845f097f839e23a094e5"></a>
## fix: ensure the connection is probably closed {#commit-06ce8871e4ce49b09079845f097f839e23a094e5}

### Provenance {#commit-06ce8871e4ce49b09079845f097f839e23a094e5-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/06ce8871e4ce49b09079845f097f839e23a094e5

Source date: 2025-11-21T18:41:42Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-28ba71750246e378d0f583cb0a365f9c4b27d542"></a>
## docs: update README.md and CHANGELOG.md {#commit-28ba71750246e378d0f583cb0a365f9c4b27d542}

### Provenance {#commit-28ba71750246e378d0f583cb0a365f9c4b27d542-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/28ba71750246e378d0f583cb0a365f9c4b27d542

Source date: 2025-11-21T18:44:19Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-04382f6c1f157046339225ab6de16204e13d6763"></a>
## refactor: improve connection logics {#commit-04382f6c1f157046339225ab6de16204e13d6763}

### Provenance {#commit-04382f6c1f157046339225ab6de16204e13d6763-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/04382f6c1f157046339225ab6de16204e13d6763

Source date: 2025-11-21T19:09:34Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-a87b940e1d79d1cc5d677f0fe529d51e0a218e05"></a>
## fix: enforce proper connection closure {#commit-a87b940e1d79d1cc5d677f0fe529d51e0a218e05}

### Provenance {#commit-a87b940e1d79d1cc5d677f0fe529d51e0a218e05-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/a87b940e1d79d1cc5d677f0fe529d51e0a218e05

Source date: 2025-11-21T19:51:19Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-0d0c48ebbed993642ae800cb12db5c182e9a2c2d"></a>
## chore: bump version to v0.10.15 {#commit-0d0c48ebbed993642ae800cb12db5c182e9a2c2d}

### Provenance {#commit-0d0c48ebbed993642ae800cb12db5c182e9a2c2d-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/0d0c48ebbed993642ae800cb12db5c182e9a2c2d

Source date: 2025-11-21T20:18:14Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-6e4b448c5533405c1e60d4751862472c76a2f335"></a>
## fix: resolve a crash in `NetworkSystem::closeConnection` {#commit-6e4b448c5533405c1e60d4751862472c76a2f335}

### Provenance {#commit-6e4b448c5533405c1e60d4751862472c76a2f335-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/6e4b448c5533405c1e60d4751862472c76a2f335

Source date: 2025-11-22T00:41:40Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-4816aef277f86290cef18daf14aeee2d0904bca4"></a>
## refactor: rename AttributeModifier operations {#commit-4816aef277f86290cef18daf14aeee2d0904bca4}

### Provenance {#commit-4816aef277f86290cef18daf14aeee2d0904bca4-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/4816aef277f86290cef18daf14aeee2d0904bca4

Source date: 2025-11-24T21:57:49Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-42f5b9d1196591139d33345e555c68397d71d0e6"></a>
## refactor: update `ItemStack.type` property return type to `ItemType` {#commit-42f5b9d1196591139d33345e555c68397d71d0e6}

### Provenance {#commit-42f5b9d1196591139d33345e555c68397d71d0e6-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/42f5b9d1196591139d33345e555c68397d71d0e6

Source date: 2025-11-24T22:11:32Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-7f01cf0102ede5d1d780277078e7f8fd0387453e"></a>
## feat: add setter for `Mob.max_health` property {#commit-7f01cf0102ede5d1d780277078e7f8fd0387453e}

### Provenance {#commit-7f01cf0102ede5d1d780277078e7f8fd0387453e-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/7f01cf0102ede5d1d780277078e7f8fd0387453e

Source date: 2025-11-24T22:31:30Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-823dc2388a832cca92462f7f8af189c7b201edd9"></a>
## Merge remote-tracking branch 'origin/main' {#commit-823dc2388a832cca92462f7f8af189c7b201edd9}

### Provenance {#commit-823dc2388a832cca92462f7f8af189c7b201edd9-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/823dc2388a832cca92462f7f8af189c7b201edd9

Source date: 2025-11-24T22:32:55Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-469c32717bf0113089c16db2bd220c15eff6489c"></a>
## Merge remote-tracking branch 'origin/v0.10' {#commit-469c32717bf0113089c16db2bd220c15eff6489c}

### Provenance {#commit-469c32717bf0113089c16db2bd220c15eff6489c-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/469c32717bf0113089c16db2bd220c15eff6489c

Source date: 2025-11-24T22:33:46Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-e1db80635f8e0731595139b27fedae237db05e70"></a>
## chore: update symbol to 1.21.124 {#commit-e1db80635f8e0731595139b27fedae237db05e70}

### Provenance {#commit-e1db80635f8e0731595139b27fedae237db05e70-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/e1db80635f8e0731595139b27fedae237db05e70

Source date: 2025-11-25T16:43:06Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-5aa11cc6a93c9f8c78813b00335dcf19af066b41"></a>
## refactor: update `ItemStack` and enchantment handling logic for type and ID consistency {#commit-5aa11cc6a93c9f8c78813b00335dcf19af066b41}

### Provenance {#commit-5aa11cc6a93c9f8c78813b00335dcf19af066b41-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/5aa11cc6a93c9f8c78813b00335dcf19af066b41

Source date: 2025-11-25T17:09:40Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-2597eeca495d0d4d94f0e600974aca1b1d84b3ad"></a>
## refactor: simplify registry binding logic with `type_list` {#commit-2597eeca495d0d4d94f0e600974aca1b1d84b3ad}

### Provenance {#commit-2597eeca495d0d4d94f0e600974aca1b1d84b3ad-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/2597eeca495d0d4d94f0e600974aca1b1d84b3ad

Source date: 2025-11-25T17:29:19Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-4524abbb91e61b00af509e7d1c2daa782f718458"></a>
## refactor: replace `Result<void>` with `void` in `setProgress` and add `Preconditions` utility {#commit-4524abbb91e61b00af509e7d1c2daa782f718458}

### Provenance {#commit-4524abbb91e61b00af509e7d1c2daa782f718458-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/4524abbb91e61b00af509e7d1c2daa782f718458

Source date: 2025-11-25T18:37:54Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-577e472c2b6e399ca346cf4b0564162875f5c6af"></a>
## chore: remove `.gitmodules` file {#commit-577e472c2b6e399ca346cf4b0564162875f5c6af}

### Provenance {#commit-577e472c2b6e399ca346cf4b0564162875f5c6af-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/577e472c2b6e399ca346cf4b0564162875f5c6af

Source date: 2025-11-25T19:01:46Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-a78b39c147581fc31aa88e2bd95f80b1d9d730c7"></a>
## chore: move contributing guide to docs directory {#commit-a78b39c147581fc31aa88e2bd95f80b1d9d730c7}

### Provenance {#commit-a78b39c147581fc31aa88e2bd95f80b1d9d730c7-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/a78b39c147581fc31aa88e2bd95f80b1d9d730c7

Source date: 2025-11-25T19:02:25Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-3e81975a9b69da1870039c5b10a568f4f940fe34"></a>
## refactor: replace `Result<Color>` with `Color` {#commit-3e81975a9b69da1870039c5b10a568f4f940fe34}

### Provenance {#commit-3e81975a9b69da1870039c5b10a568f4f940fe34-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/3e81975a9b69da1870039c5b10a568f4f940fe34

Source date: 2025-11-25T19:30:08Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-b16ec4a30715f6c40c2b886ea520c9fd96e96d12"></a>
## refactor: update `remove_attachment` method to return a boolean {#commit-b16ec4a30715f6c40c2b886ea520c9fd96e96d12}

### Provenance {#commit-b16ec4a30715f6c40c2b886ea520c9fd96e96d12-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/b16ec4a30715f6c40c2b886ea520c9fd96e96d12

Source date: 2025-11-25T19:41:12Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-400184c491022c25f53cdd563989dbb0f06d7d08"></a>
## refactor: replace `Result<void>` with `void` in `setHealth` and `setMaxHealth`, add `Preconditions` validation {#commit-400184c491022c25f53cdd563989dbb0f06d7d08}

### Provenance {#commit-400184c491022c25f53cdd563989dbb0f06d7d08-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/400184c491022c25f53cdd563989dbb0f06d7d08

Source date: 2025-11-25T19:50:55Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-70cfe379eacc9214c29737b082acdd121ddeb505"></a>
## refactor: replace `Result<float>` with `float` in `distanceSquared`, add `Preconditions` validation {#commit-70cfe379eacc9214c29737b082acdd121ddeb505}

### Provenance {#commit-70cfe379eacc9214c29737b082acdd121ddeb505-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/70cfe379eacc9214c29737b082acdd121ddeb505

Source date: 2025-11-25T19:52:12Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-0b41fe71d2921b915480e5cefd607d56204ae313"></a>
## refactor: replace `Result<float>` with `float` in `distance` {#commit-0b41fe71d2921b915480e5cefd607d56204ae313}

### Provenance {#commit-0b41fe71d2921b915480e5cefd607d56204ae313-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/0b41fe71d2921b915480e5cefd607d56204ae313

Source date: 2025-11-25T19:52:36Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-f66147f0c00e7575ca573d819131e7a7ade8a37d"></a>
## refactor: replace `Result<T>` with `T` in `Objective` and `Score`, add `Preconditions` validation {#commit-f66147f0c00e7575ca573d819131e7a7ade8a37d}

### Provenance {#commit-f66147f0c00e7575ca573d819131e7a7ade8a37d-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/f66147f0c00e7575ca573d819131e7a7ade8a37d

Source date: 2025-11-25T20:32:35Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-1608ef01e8c8a89abddf3151d39ccbc39e032801"></a>
## refactor: replace `Result<Objective>` with `Objective`, add `Preconditions` validation {#commit-1608ef01e8c8a89abddf3151d39ccbc39e032801}

### Provenance {#commit-1608ef01e8c8a89abddf3151d39ccbc39e032801-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/1608ef01e8c8a89abddf3151d39ccbc39e032801

Source date: 2025-11-25T21:20:21Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-32860a1c09628326b28812bb6fe0d134f84f6a49"></a>
## refactor: replace `Result` with `Preconditions` validation {#commit-32860a1c09628326b28812bb6fe0d134f84f6a49}

### Provenance {#commit-32860a1c09628326b28812bb6fe0d134f84f6a49-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/32860a1c09628326b28812bb6fe0d134f84f6a49

Source date: 2025-11-25T23:28:07Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-38b262298ac192ba1a81250d4f39737e88cb50d8"></a>
## refactor: replace `Result` with `Preconditions` validation {#commit-38b262298ac192ba1a81250d4f39737e88cb50d8}

### Provenance {#commit-38b262298ac192ba1a81250d4f39737e88cb50d8-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/38b262298ac192ba1a81250d4f39737e88cb50d8

Source date: 2025-11-25T23:34:47Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-39ce1ba35ea97ff336b9eff838e2dde6e5d84c7e"></a>
## refactor: replace `Result` with `Preconditions` validation {#commit-39ce1ba35ea97ff336b9eff838e2dde6e5d84c7e}

### Provenance {#commit-39ce1ba35ea97ff336b9eff838e2dde6e5d84c7e-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/39ce1ba35ea97ff336b9eff838e2dde6e5d84c7e

Source date: 2025-11-25T23:38:56Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-d24e5f10ce3ab6a0315e7d313350d03799009a2f"></a>
## [feature] add 1.21.130 support {#commit-d24e5f10ce3ab6a0315e7d313350d03799009a2f}

### Provenance {#commit-d24e5f10ce3ab6a0315e7d313350d03799009a2f-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/d24e5f10ce3ab6a0315e7d313350d03799009a2f

Source date: 2025-12-11T00:00:30Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-fce3b8e4b280df7cf2f6b0b3c483861c8bc0b73b"></a>
## docs: update README.md and CHANGELOG.md {#commit-fce3b8e4b280df7cf2f6b0b3c483861c8bc0b73b}

### Provenance {#commit-fce3b8e4b280df7cf2f6b0b3c483861c8bc0b73b-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/fce3b8e4b280df7cf2f6b0b3c483861c8bc0b73b

Source date: 2025-12-11T00:05:46Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-57b966951a4a124042b59905607fdd72d9d64a4b"></a>
## fix: resolve a crash caused by missing damage cause {#commit-57b966951a4a124042b59905607fdd72d9d64a4b}

### Provenance {#commit-57b966951a4a124042b59905607fdd72d9d64a4b-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/57b966951a4a124042b59905607fdd72d9d64a4b

Source date: 2025-12-11T17:51:05Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-f0cbdedc05d40ff10742ac3f1191c7098d50bd48"></a>
## refactor: suppress additional low-priority logs for `System` log area {#commit-f0cbdedc05d40ff10742ac3f1191c7098d50bd48}

### Provenance {#commit-f0cbdedc05d40ff10742ac3f1191c7098d50bd48-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/f0cbdedc05d40ff10742ac3f1191c7098d50bd48

Source date: 2025-12-11T19:08:06Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-e248c66f39d4fe184ef7f1eb539b9977e89ae39c"></a>
## fix: correct the symbols for `ItemStackBase::_loadBlocksForCanPlaceOnCanDestroy` {#commit-e248c66f39d4fe184ef7f1eb539b9977e89ae39c}

### Provenance {#commit-e248c66f39d4fe184ef7f1eb539b9977e89ae39c-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/e248c66f39d4fe184ef7f1eb539b9977e89ae39c

Source date: 2025-12-11T19:19:38Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-70ec2e3e11bf5c2c5375d1587a7680e33e844853"></a>
## docs: update CHANGELOG.md {#commit-70ec2e3e11bf5c2c5375d1587a7680e33e844853}

### Provenance {#commit-70ec2e3e11bf5c2c5375d1587a7680e33e844853-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/70ec2e3e11bf5c2c5375d1587a7680e33e844853

Source date: 2025-12-11T19:40:25Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-38bfc6c53df32792d1ec798ab61ae8254272c762"></a>
## feat: add `UnverifiedCertificate::fromString` hook with JSON validation logic {#commit-38bfc6c53df32792d1ec798ab61ae8254272c762}

### Provenance {#commit-38bfc6c53df32792d1ec798ab61ae8254272c762-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/38bfc6c53df32792d1ec798ab61ae8254272c762

Source date: 2025-12-14T17:36:50Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-92569ca1b2eda7acc2972022fc6ab260c0233fad"></a>
## fix: add `Certificate::validate` hook to fix a null pointer-related crash (blame mojang) {#commit-92569ca1b2eda7acc2972022fc6ab260c0233fad}

### Provenance {#commit-92569ca1b2eda7acc2972022fc6ab260c0233fad-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/92569ca1b2eda7acc2972022fc6ab260c0233fad

Source date: 2025-12-14T17:58:26Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-b209f49ab18ba0e97d64e98bce40d5b877a28260"></a>
## fix: ensure the fix works on Linux {#commit-b209f49ab18ba0e97d64e98bce40d5b877a28260}

### Provenance {#commit-b209f49ab18ba0e97d64e98bce40d5b877a28260-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/b209f49ab18ba0e97d64e98bce40d5b877a28260

Source date: 2025-12-14T18:20:12Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-71371baf85ad4dd260d3fd0ec6217c057427eea7"></a>
## chore: bump version to 0.10.18 {#commit-71371baf85ad4dd260d3fd0ec6217c057427eea7}

### Provenance {#commit-71371baf85ad4dd260d3fd0ec6217c057427eea7-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/71371baf85ad4dd260d3fd0ec6217c057427eea7

Source date: 2025-12-14T18:23:11Z

Limits: Main1352 and stable1363 are distinct endpoints.


<a id="commit-2b1d39150120d90b9fccf3a331e4402122feca57"></a>
## refactor: remove unused `validate_ptr` helper function in `certificate.cpp` {#commit-2b1d39150120d90b9fccf3a331e4402122feca57}

### Provenance {#commit-2b1d39150120d90b9fccf3a331e4402122feca57-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/2b1d39150120d90b9fccf3a331e4402122feca57

Source date: 2025-12-14T18:27:22Z

Limits: Main1352 and stable1363 are distinct endpoints.
