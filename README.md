# Anthropology Atlas Content

Independent historical content for the [Anthropology Atlas engine](https://github.com/philippklinz/anthropology-atlas-engine).

The first historical sample covers **the first circumnavigation, 1519–1522**: 4 people, 9 places, 12 events, the Victoria, the defenders of Mactan, and 8 sources. The chapter is available in German and English. All records are honestly marked as a **research draft**, with cited sources and explicitly schematic geography. See [research scope and limits](docs/research/first-circumnavigation.md).

`published/catalog.json` serves this sample to the atlas. Synthetic fixtures remain in the engine’s test area and are not part of this historical package.

## Use as a content source

The engine defaults to this public repository, branch `main`, path `published/catalog.json`. A clone can also be served by any HTTP(S) server; put its catalogue URL in the engine's central `atlas.config.json`. Different origins require CORS. No MariaDB, Node.js, npm or package installation is needed.

## Authoring without a toolchain

1. Edit canonical source records and commit them. `dataset.json` selects the packages to publish.
2. Open **`tooling/index.html`** through a web server. The same tool is available as `authoring.html` in the engine.
3. Select this content folder or a ZIP containing it. Choose `draft`, `release` or `fixture` and validate.
4. For export, enter the full Git commit of those selected source data (`git rev-parse HEAD`) and download `published.zip`.
5. Extract into `published/` and commit the generated catalogue and files. Retain existing hashed files in `published/files/` when updating a branch so concurrent readers can finish loading their previous catalogue.

All processing runs in the browser; selected files are not uploaded. The tool cannot attest your Git revision or host symlink metadata: verify the selected data match the commit, and do not use symlink payloads. Validation checks structure and semantics, not historical truth. A historical `release` rejects an empty or synthetic dataset.

## Canonical layout

- `entities/<type-plural>/`: one identity per JSON file.
- `assertions/<predicate>/`: dated, cited relationships.
- `events/<type>/`: events, journeys and participants.
- `geometries/{points,lines,areas}/<slug>/`: metadata and GeoJSON payload.
- `sources/`, `interpretations/`: citations and alternative interpretations.
- `assets/{models,images,fonts,documents}/<slug>/`: media and rights.
- `chapters/<slug>/`: chapter metadata and localized Markdown.
- `packages/<slug>/manifest.json`: explicit ownership and dependencies.
- `templates/`: drafting examples, excluded from publication.
- `tooling/`: fixed standalone browser tools and schemas from the engine.
- `published/`: browser-consumable output; source remains authoritative.

`contract.lock.json` and `tooling.sha256` identify and verify the delivered toolkit. Toolkit updates are deliberate maintainer commits. The repository retains its existing GNU GPL v2 LICENSE; distributed media and third-party components retain their separately documented rights.
