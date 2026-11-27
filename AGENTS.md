# Content work rules

This repository holds canonical historical research. The engine repository owns the schema and the authoring tools. Use the contract revision pinned by the project; do not invent a local schema fork.

- Use suggested topics as research leads. Ground public chapter titles, discovery categories and historical comparisons in sources for the relevant place, period and relationship.
- Search existing identities and citations before adding records.
- Read the cited source and record the specific locator. Do not invent sources, quotations, dates or review claims.
- Separate entities, dated assertions, events, geometry, source records and assets.
- Treat language ancestry, script development, cultural transmission and political membership as distinct relationships.
- Preserve temporal and spatial uncertainty. Missing data is not evidence of absence.
- Record one canonical owner package per record. Reuse records through explicit dependencies.
- Keep IDs stable and payload paths local. Content must not contain executable JavaScript, arbitrary HTML or hidden remote resources.
- Record licensing and attribution for distributed files separately from bibliographic links.
- Keep synthetic fixtures and templates out of historical releases.
- Edit source records, not generated `published/` output. A database projection is not a second canonical history store.
- Report the validation and historical review actually performed. Never imply that schema validation establishes historical truth.

- Open tooling/index.html through HTTP to validate/export in the browser. No Node, npm or package installation is required. The toolchain is pinned by contract.lock.json and tooling.sha256.
- The default published catalogue may be an empty draft. Historical release validation still rejects an empty dataset.
- Generate published/ using the browser tool from a committed source revision. Retain prior hash-named payload files when updating a mutable branch.
