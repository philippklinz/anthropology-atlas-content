# Anthropology Atlas Content

Independent historical content for the [Anthropology Atlas engine](https://github.com/philippklinz/anthropology-atlas-engine).

Fifteen historical chapters are available in German and English:

- [The Cradle of Humankind: early Homo sapiens in Africa](docs/research/cradle-of-humankind.md), including fossil evidence, stone tools and explicit dating uncertainty.
- [Early Routes out of Africa: Misliya, Skhul, Qafzeh and Al Wusta](docs/research/early-routes-out-of-africa.md), with fossil evidence, environmental context and explicit dating limits.
- [When We Were Not Alone: Denisova, Bacho Kiro, Ranis and Zlatý kůň](docs/research/when-we-were-not-alone.md), comparing parentage, earlier ancestry and individual kinship through ancient DNA.
- [Traces of Our Thoughts: signs, images and music](docs/research/traces-of-our-thoughts.md), comparing four findsites, minimum ages, image interpretation and early flutes.
- [Across Seas and Land Bridges: Sahul, Beringia and White Sands](docs/research/seas-and-land-bridges.md), with independent findsites, selectable route hypotheses and dated schematic land connections.
- [A Day of Making a Living](docs/research/day-of-making-a-living.md), comparing charred remains, food processing tools and isotope evidence.
- [Inventing with Stone, Wood and Fibres](docs/research/materials-and-invention.md), on composite tools and early pottery.
- [Growing Up, Caring and Saying Goodbye](docs/research/growing-up-and-caring.md), on childhood, possible social support and burial.
- [Connected Across Long Distances](docs/research/connections-across-distances.md), comparing bead styles, material origins and manufacture.
- [Living at the Edge of the Ice](docs/research/life-at-the-ice-edge.md), on the structures at Kostenki 11, Ohalo II and Kharaneh IV.
- [The Americas: Many Paths, Many Environments](docs/research/many-american-landscapes.md), on Paisley, Page-Ladson and Arroyo Seco 2.
- [As the Ice Retreats](docs/research/as-the-ice-retreats.md), comparing fishing images, a coral archive and stone buildings.
- [Columbus's first Atlantic voyage, 1492–1493](docs/research/columbus-first-voyage.md), including inhabited Caribbean societies and the disputed identification of Guanahani.
- [The first circumnavigation, 1519–1522](docs/research/first-circumnavigation.md).
- [Darwin and the second Beagle voyage, 1831–1836](docs/research/darwin-beagle.md), including his four Galápagos island stays.

The dataset contains 530 records: 167 entities, 87 events, 29 assertions, 79 geometries, 112 sources, 24 images, one interpretation group, fifteen chapters and sixteen packages. All records remain **research drafts**. The chapter notes document sources, map precision and outstanding interpretations.

`published/catalog.json` serves these chapters to the atlas. Synthetic fixtures remain in the engine’s test area. Reused Rio Bay and Cape of Good Hope identities, their geometries and two supporting sources have one canonical owner in `package:maritime-shared`; voyage packages declare explicit dependencies on it. The early-dispersal package reuses Homo sapiens and Levallois identities through its explicit dependency on `package:human-origins`. The human-encounters package depends on the same owner for Homo sapiens and introduces cited genetic relationships between individual specimens and biological lineages.

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

## Chapter discovery

All fifteen chapters define explicit `recordIds` membership and bilingual discovery summaries, periods, regions and topics. Membership is independent of package ownership. The engine opens a searchable overview, supports multiple chapter selection, and scopes the atlas and directory to that selection. Ohalo II appears in the food and shelter chapters with a single canonical place record. The twelve early chapters share the **Palaeolithic** filter. See [chapter discovery](docs/research/chapter-discovery.md), [the chapter plan](docs/planning/palaeolithic.md) and [the expansion notes](docs/research/palaeolithic-expansion.md).
