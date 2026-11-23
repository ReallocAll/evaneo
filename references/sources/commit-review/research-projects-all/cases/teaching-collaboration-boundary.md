<!-- retrieval: {"source_ids":["public:commit:055f3456532f68e925eb932952f55097a662fb53","public:commit:1153d60fe7940e0d40efeccf5f31468ea07f1786","public:commit:1693e233282098c38a90fe7b6aa63e78731ae3ea","public:commit:27e3d98f275b0c27798426ace626d133d0420013","public:commit:3b56171349f7380f88cfcfdea111acf54958d1d4","public:commit:43f09a1630620589bf4a02ea9d45d4b7126b079c","public:commit:48e6564db916c1f8cecd330fc7d1f3558c007778","public:commit:4ce2c2c0e90cef8bdd03f0731267a682cb4380bf","public:commit:528bcb1e788c9f77f0c9cd7f03726cc3df119a22","public:commit:54932162a614ce336a642d46e139d21a36f43ee3","public:commit:6ac38d7d09bf063ac73ea39f21e54a4cd8f08b6e","public:commit:6e30947e2c61f38672b2e4840e9c1ac8e4e3e4e4","public:commit:7966990be75eacad2d9ef67c8c4c194514140486","public:commit:798ffb98fa8d69924342fe89c406dc3b4b2ae813","public:commit:84c8bd3488e82173af635499d4b574097e829285","public:commit:868e8aa21e7aec75a4ef5cb2f04454082330f45d","public:commit:9086a448342e6f3b0756ead823d4b0ac6b9a9f08","public:commit:b28a28f8c1294587359081297442ca36fbfc58f5","public:commit:bfc0ca909600052221a482431dd57b200775e250","public:commit:fb9de80108f9e9ad58c65904ecfc69fdaf370c85"],"source_type":"public","date":"2023-11-19..2025-10-16","topics":["documentation","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="teaching-demo-readable-collaboration-history-without-invented-code-lessons"></a>
# Teaching demo: readable collaboration history without invented code lessons {#teaching-demo-readable-collaboration-history-without-invented-code-lessons}

## Scope {#scope}

All 20 reviewed commits in `tsl-imperial/cive70111_25_demo1` were read, including full messages and both parents for merges. They are README/gallery instructions, contributor recognition, conflict integration, link/description changes and deletion of an empty `.Rhistory` file. There is no C++/Python implementation change in this selected history. This history supports collaboration lessons, not inferred C++/Python implementation expertise from student application descriptions.

[Per-SHA review](../cive70111_25_demo1-review.md) provides commit-level detail. Initial public provenance: [43f09a1](https://github.com/tsl-imperial/cive70111_25_demo1/commit/43f09a1630620589bf4a02ea9d45d4b7126b079c).

## Actual contribution pattern {#actual-contribution-pattern}

The initial tutorial explains a fork/branch/edit/commit/pull-request path for adding an application to a gallery. Later changes make the entry structure explicit: participant name, application title/link and short description. This is a small but concrete reduction in submission ambiguity, supported by actual README edits. It does not show how any linked application was implemented.

The inspected commits integrate named participant entries, including Akaravin, Chanaporn, Joel, Andrew, Bilal and Zaid. Several merge commits have a tree identical to their incoming parent; these commits performed integration rather than authored those entries from scratch. Conflict-resolution commits retain multiple contributions and adjust descriptions/formatting. Other contributors remain credited in the side history. No review objection, educational outcome or interpersonal preference is invented when only a diff is present.

Two commits carry Gemini coauthor trailers: one clarifies a Sudoku description, another adjusts a trailing slash. Later integration normalizes multiple slashes including reversing the earlier change. This is direct counterevidence to treating a single accepted suggestion as a durable URL-formatting rule. The bot's participation is preserved; it is not relabelled single-author credit.

## Limits and reuse {#limits-and-reuse}

The linked deployed sites and their source were not independently examined. Gallery text is not evidence that those sites work, are secure, were built by the integration contributor, or demonstrate a C++/Python technique. The contributor image is not a verified current activity measurement. Deleting empty `.Rhistory` has no algorithmic content.

A narrowly reusable collaboration lesson is to make contribution shape explicit and inspect merge parents before assigning credit. This could assist an agent asked to organize a README contribution exercise or reconcile overlapping documentation edits. It does not establish independent C++/Python implementation expertise. These 20 commit records are not 20 independent technical lessons.
