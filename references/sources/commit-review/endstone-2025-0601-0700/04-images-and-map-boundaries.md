<!-- retrieval: {"source_ids":["public:commit:31c92f4d48b1da9891dde91556660b17c81852d0","public:commit:5678bb1bdda4f644288c998d1bc43d65de8d3361","public:commit:5fe2d909a55bb79ad8eb09f1f3932ee8358458ef","public:commit:602cdbda7a17eba0ce46b51fdd547ba8c0afc62a","public:commit:8a55b824be4f78be8d4d58d53706a24892961d0c","public:commit:abb16c16420aafd72c370bb063f6dc6915cf70cf","public:commit:b624b8d57e280e0a66db0b62f50c643e0af7acca","public:commit:d0288c884b8a88c3ea771aa660c2af19e519e2d7","public:commit:fe2b6b2cfe2844b72b0f7ceaccb5a8cee5492df8","public:commit:feb3eb2338ef77aba7410c83f34fd99c60399afe"],"source_type":"public","date":"2025-05-22..2025-05-23","topics":["lifetime","ffi","testing","api","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Owning pixels, Python conversion and unfinished map surfaces {#owning-pixels-python-conversion-and-unfinished-map-surfaces}


## From wrapper classes to values {#from-wrapper-classes-to-values}

658–660 introduce Color, owning RGBA Image, Skin's image fields and abstract map interfaces. Image stores row-major pixels; construction and pixel access rely on dimension/index preconditions. fromBuffer checks positive dimensions and exact byte count, but signed multiplication is not independently overflow-checked. The public abstraction does not itself establish hostile-input safety.

The Python surface goes through a short-lived class-based stage.661 binds every Color channel to red and binds Skin's skin image to cape data.662 repairs the image binding and renames fields to id/image/cape_image.663 adapts login decoding but supplies skin dimensions to cape image parsing even after reading cape dimensions. This is an observed static mismatch; whether a particular client cape is rejected depends on its sizes and native data. No login-path test accompanies it.

665 replaces Image's Python class with a NumPy uint8 RGBA caster. The conversion force-casts/contiguizes arrays, validates the shape through fromBuffer, copies into C++ storage and explicitly copies back to an owning NumPy result. That copy cost buys independence from a temporary C++ buffer.666 replaces Color's class with a3/4-element sequence input and RGBA tuple output, removing the faulty class bindings rather than patching their getters. Temporary exports are cleaned up with the caster migration.

## Test scope and limits {#test-scope-and-limits}

665 adapts skin tests to the new fields/casters and reduces four cases to three by removing redundant separate initialization coverage. With-cape, without-cape value checks and invalid-shape TypeError coverage remain. This is a cost/coverage tradeoff, not automatically a defect. Those tests do not cover native login's cape dimensions, signed-size overflow, map ownership or channel binding from the removed class. No tests were executed here.

## Map contracts are declarations, not a working renderer {#map-contracts-are-declarations-not-a-working-renderer}

The map API describes128×128 canvas layers, nullopt revealing a lower layer, contextual per-player rendering, scale, center, dimension, locking, tracking and renderer management. The interface deliberately exposes abstractions before a native implementation.667 supplies inline renderer defaults, a Python trampoline and public stubs, but no native map retrieval/rendering integration in this slice.

At700 two Python binding expressions still conflict with the public names: remove_renderer binds addRenderer, and locked binds unlimited-tracking getters/setters. isContextual is not exposed. Renderer references are borrowed with no explicit keep_alive declaration. These are source-level API/lifetime boundaries, not an executed end-user failure report. The staged map headers also briefly precede their implementation/includes, so individual commits are not claimed to compile independently.

Use this chain for evaluating copy-versus-borrow decisions, coordinating C++/Python/stub migrations, choosing bounded tests for changed contracts and avoiding claims that an abstract API is complete runtime support. Complete meaningful diffs and test edits are retained per SHA below; no removal of a redundant test is used as a proxy for decreased overall quality.

## Per-commit decisions and revisions {#per-commit-decisions-and-revisions}

<a id="commit-658"></a>
### Commit 658 {#commit-658}

[8a55b824be4f](https://github.com/EndstoneMC/endstone/commit/8a55b824be4f78be8d4d58d53706a24892961d0c) · 2025-05-22T00:11:24Z · feat: add `endstone::Color` for RGBA color

Adds immutable-facing four-uint8 Color value with RGBA getters/default opaque black. Numeric range enforced by parameter type conversion, not explicit domain validation; no tests.


<a id="commit-659"></a>
### Commit 659 {#commit-659}

[5678bb1bdda4](https://github.com/EndstoneMC/endstone/commit/5678bb1bdda4f644288c998d1bc43d65de8d3361) · 2025-05-22T00:11:37Z · feat: add `endstone::Image`

Adds owning row-major RGBA Image with unchecked signed dimension multiplication and unchecked documented-in-range pixel access. Skin replaces ImageData with Image and removes default constructor; umbrella includes forthcoming map headers before660 adds them, so staged dependency. No input safety/test claim.


<a id="commit-660"></a>
### Commit 660 {#commit-660}

[602cdbda7a17](https://github.com/EndstoneMC/endstone/commit/602cdbda7a17eba0ce46b51fdd547ba8c0afc62a) · 2025-05-22T00:11:50Z · feat: add `MapView`, `MapRenderer` and `MapCanvas`

Introduces abstract MapView/MapCanvas and renderer API:128x128 pixel layers, nullopt reveals base, contextual renderer perplayer, map scale/center/dimension/lock/tracking and renderer management. No native implementation. Renderer ctor/isContextual/initialize declared until667. Closest spelledCloset, setWorld acceptsDimension; later name repair. Interfaces express intended behavior only.


<a id="commit-661"></a>
### Commit 661 {#commit-661}

[feb3eb2338ef](https://github.com/EndstoneMC/endstone/commit/feb3eb2338ef77aba7410c83f34fd99c60399afe) · 2025-05-22T00:49:56Z · feat: add python binding for `Color` and `Image`

Initial Color/Image Python classes and Skin migration; fromBuffer validates positive dimensions/exact byte length but multiplication remainsint. Cape optional exposed nullablepointer. Interim bugs: skin_data boundCapeData, everyColor channelgetter boundRed, from_buffer arg annotations incomplete. Subsequent662/663/665/666 revise these rather than treating temporary API as final.


<a id="commit-662"></a>
### Commit 662 {#commit-662}

[d0288c884b8a](https://github.com/EndstoneMC/endstone/commit/d0288c884b8a88c3ea771aa660c2af19e519e2d7) · 2025-05-22T01:02:11Z · refactor: name methods in `Skin` class

Renames Skin to id/image/cape_image and corresponding C++ accessors; skin image now correctly bindsgetImage, repairing661. Reference return policy borrows containedimage, later665 caster returnsownedcopy.


<a id="commit-663"></a>
### Commit 663 {#commit-663}

[abb16c16420a](https://github.com/EndstoneMC/endstone/commit/abb16c16420aafd72c370bb063f6dc6915cf70cf) · 2025-05-22T12:50:51Z · feat: update python bindings

Adapts player login skin decoding to validatedImage and nullable unique-ownedSkin. Invalid skin logs/returns; cape parse mistakenly uses skin_width/height despite reading cape dimensions, so legitimate different-sized capes may be discarded. Updates Python bytes constructor/stub and Color names but retainsRed copy-paste bindings. Command symbolindex explicitcast and Detours gitlink reverses609 to b2bf32a; submodule contents outside scope.


<a id="commit-664"></a>
### Commit 664 {#commit-664}

[fe2b6b2cfe28](https://github.com/EndstoneMC/endstone/commit/fe2b6b2cfe2844b72b0f7ceaccb5a8cee5492df8) · 2025-05-22T12:52:29Z · feat: add Color and Image to endstone.util exports

Exports Color/Image from endstone.util, later666 reverses exports after caster migration. No independent lesson.


<a id="commit-665"></a>
### Commit 665 {#commit-665}

[5fe2d909a55b](https://github.com/EndstoneMC/endstone/commit/5fe2d909a55bb79ad8eb09f1f3932ee8358458ef) · 2025-05-22T14:54:12Z · feat: add type caster for `endstone::Image`

Replaces Python Image class with NumPy uint8 RGBA caster: force-casts contiguous array, validatesH/W/4shape throughfromBuffer, copies intoC++ and explicitly copies back toownedNumPy result, trading copycost for detached lifetime. Skin remains NumPy-facing with renamedfields. Adapts3skin tests, removes redundant separate initialization case while keeping with/withoutcape values and invalidshape(TypeError) coverage. Adds no native login/cape-dimension or overflow tests. Export temporarily staleuntil666. Header include-cycle cleanup.


<a id="commit-666"></a>
### Commit 666 {#commit-666}

[31c92f4d48b1](https://github.com/EndstoneMC/endstone/commit/31c92f4d48b1da9891dde91556660b17c81852d0) · 2025-05-22T15:14:55Z · feat: add type caster for `endstone::Color`

Replaces faulty Color class bindings with3/4element sequence→Color(defaultalpha255) and Color→RGBAtuple caster, removesColor/Imageexports andclasses. Broad sequence check anduint8 conversion errors, no component-specifictests. This eliminates interimallRedbindings ratherthanfixingtheclassAPI.


<a id="commit-667"></a>
### Commit 667 {#commit-667}

[b624b8d57e28](https://github.com/EndstoneMC/endstone/commit/b624b8d57e280e0a66db0b62f50c643e0af7acca) · 2025-05-23T16:29:27Z · feat: add python binding for the Map API

MapPythonbinding/trampoline and facade/stubs/buildentry; renderer constructor/isContextual/initialize now inline and setWorld renamedsetDimension. AbstractAPIonly, no map retrieval/native renderer implementation. Staticcopy-paste mismatches: remove_renderer bindsaddRenderer; locked bindsunlimitedtrackingget/set; isContextual not exposed. Renderer add borrowsreference with no keepalive declaration. Detours pointerbackea6c4ae; unexamined submodulecontents. No runtime/tests.

