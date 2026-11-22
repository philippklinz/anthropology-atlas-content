# Anthropology Atlas · Content

Canonical research for the [Atlas engine](https://github.com/philippklinz/anthropology-atlas-engine). This repository currently contains authoring structure, templates and a standalone validator/compiler. **No historical research is included yet.**

## Contribute

Read `AGENTS.md` and `CONTRIBUTING.md`. Define a bounded research question, place and time in `docs/research/`. Add entities, dated assertions, sources, geometry and localized chapter text. Declare every record in an owner package and add the package ID to `dataset.json`. Templates are fictional examples, never historical evidence.

With Node.js 24 or newer:

```bash
sha256sum --check tooling.sha256
node tooling/tools/cli.js validate . --profile draft
```

`contract.lock.json` pins the engine commit and hashes every generated toolkit file. `tooling.sha256` checks that local copy before use. Update the toolkit and both manifests together from a reviewed engine revision.

No engine checkout, npm install, database or web service is needed. The empty starting dataset validates as an editorial draft; it cannot produce a release until a reviewed package and entry chapter exist.

## Publish

After source reading, real editorial review, resolved resource rights and a clean source commit:

```bash
node tooling/tools/cli.js validate . --profile release
node tooling/tools/cli.js build . --profile release --out published
```

Serve `published/` over HTTP(S), with CORS when the atlas uses another origin. For public GitHub Raw, commit generated output on a publication branch and pin the atlas to that full commit and catalogue SHA-256. The catalogue's `sourceRevision` identifies the source commit, not the later output commit. Private tokens never belong in browser configuration.

| Folder | Contents |
|---|---|
| `entities/<type>/` | Stable identities |
| `assertions/<predicate>/` | Dated, evidenced relationships |
| `events/<type>/` | Events, participants, movement |
| `geometries/` | GeoJSON and provenance |
| `sources/`, `interpretations/` | Bibliography and alternatives |
| `assets/` | Models, images, fonts, documents and rights |
| `chapters/`, `packages/` | Narrative, explicit membership and dependencies |
| `docs/research/` | Scope, findings, gaps and review evidence |
| `tooling/` | Generated pinned kit; do not edit |

The existing GNU GPL v2 `LICENSE` remains. Included resources keep their own documented terms; bibliographic links do not grant redistribution rights. Validation checks structure and consistency, not historical truth.
