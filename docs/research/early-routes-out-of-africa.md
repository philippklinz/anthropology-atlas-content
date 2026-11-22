# Early Routes out of Africa / Frühe Wege aus Afrika

Research draft, 2026-11-22. Chapter `chapter:early-routes-out-of-africa`; owner package `package:early-dispersals`.

## Scope and learning sequence

Four selected Homo sapiens sites in the Levant and northern Arabia, within an editorial 200,000–80,000 BP viewing window. Readers compare fossils, contextual dating and changing environments. This is not an exhaustive early-dispersal inventory, a dated departure from Africa, a genealogy of modern populations, or a sequence of stops made by one group. Earlier and contested Eurasian claims such as Apidima are outside this bounded selection; Misliya is not labelled the absolute oldest Eurasian sapiens fossil. African history continues alongside this chapter.

## Chronological choices

| Evidence | Timeline representation | Source and limitation |
|---|---|---|
| Misliya-1 | Approximate instant envelope, 194–177 ka | Hershkovitz et al. (2018), pp. 456–457 and Fig. 2. Combined limits associated with the fossil, not continuous settlement or a departure date. Original four-page article consulted. |
| Skhul | Approximate synthesis envelope, 130–100 ka | Groucutt et al. (2018), Background/Discussion. Grün et al. (2005), accessible abstract, instead gives 100–135 ka under a short-burial-span assumption and allows differences between individual burials. Both are disclosed. No statistical confidence level is invented. |
| Qafzeh | Selected approximate synthesis envelope, 100–90 ka | Groucutt et al. (2018); Valladas et al. (1988) publisher abstract. Schwarcz et al. (1988), original article and Table 1, reports model-dependent ESR ages including 115 ± 15 ka and the earlier TL mean of 92 ± 5 ka. The chosen envelope is not the full site's occupation span or a universal age for every Qafzeh fossil. |
| Al Wusta | Approximate contextual envelope, 95–86 ka | Groucutt et al. (2018), abstract, Results, SI 4; this is the reported rounded combined site chronology, not a symmetric error bar or continuous occupation. |
| AW-1 direct measurement | Explained in specimen and event prose; no second duplicate timeline occurrence | The direct 87.6 ± 2.5 ka U-series result is a **minimum age**, with **2σ** specified in SI 4. Uranium uptake after burial is discussed in SI 2. It is not silently used as an exact fossil age. |

All rounded ages use the engine's fixed 1950 BP comparison convention, disclosed in both chapter texts. No radiocarbon calibration is implied. Chapter boundaries are editorial viewport endpoints. Dates concern ancient evidence, not modern excavation years.

The primary Misliya article and the Al Wusta accepted manuscript and relevant supplement were read. For Skhul only the original article's abstract was accessible; claims are limited accordingly. The Qafzeh funerary paragraph uses the excavators' 2019 abstract and avoids assigning particular rituals, beliefs, grave goods, or a universal earliest-burial label. Individual burial interpretations and detailed site chronologies remain subjects for further chapters/review.

## Geography

| Point [longitude, latitude] | Editorial accuracy | Derivation |
|---|---:|---|
| Misliya [34.97, 32.75] | 2 km | Weinstein-Evron et al. (2012), p. 203: 32°45′ N, 34°58′ E; rounded. |
| Skhul [34.97, 32.67] | 3 km | UNESCO cave-group coordinate N32 40 07 E34 58 05; a location aid for Skhul within that small property, not an excavation measurement. |
| Qafzeh [35.3, 32.7] | 15 km | Coarse orientation from Groucutt et al. Fig. 1A and Schwarcz et al. p. 733, near Nazareth. Deliberately less precise than the other Levantine points. |
| Al Wusta [39.4, 27.4] | 10 km | Groucutt et al., SI 3, OSL methods: published location used for cosmic-ray dose calculations. |

Accuracy values are editorial estimates, not surveyed errors. No migration tracks, political boundaries, palaeolake polygons, ancient coastlines or climatic distribution polygons are asserted. Today's physical basemap is explicitly identified. Overlapping Levantine points at overview scale can be selected from the timeline or separated by zooming.

## Reuse and relationships

The package depends on `package:human-origins` and reuses the canonical `taxon:homo-sapiens` and `technology:levallois-technique` records with their citation closure. The taxon summary is made independent of a particular chapter. Four attestation events connect fossils, taxon and findspots. Two dated Levallois attestations connect technology and places without treating shared technology as proof of a migration route. Explanatory dating technology is not given a prehistoric invention date.

## Local media

Both images were visually checked and are supplied locally; the reader does not load Wikimedia at runtime.

| Asset | Attribution and license | Treatment |
|---|---|---|
| `skhul-cave-view/skhul-cave.jpg` | Avishai Teicher (Avi1111), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), [source file page](https://commons.wikimedia.org/wiki/File:Skhul_Cave_(2).jpg) | Wikimedia's 1280 px derivative copied unchanged; photo dated 18 October 2016, explicitly a modern site view. |
| `skhul-v-skull-view/skhul-v.jpg` | Wapondaponda; background/rotation by UtaUtaNapishtim, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/), [source file page](https://commons.wikimedia.org/wiki/File:Skhul.JPG) | Current 549 × 570 file copied unchanged. The source does not identify original versus cast; the caption retains that uncertainty. |

Per-image rights and source URLs are recorded in asset metadata. Scientific papers are citations, not redistributed PDFs or figures. New prose is authored for the atlas. The image licenses are separate from the repository's GPL license.

## Review and validation

This is a cited editorial draft, not an independently peer-reviewed historical release. Browser validation checks the pinned contract, ownership, reference closure, dates, geometry and media. Historical uncertainty is retained rather than inferred away by passing structural checks. The committed source was compiled by the pinned browser toolkit; verification details follow.

## Export and browser verification

- Committed canonical source: `29342fc085085df37f015012b3092922cbdb265f`; 292 selected source and payload files.
- Browser export: `draft-20c8446c81c384ca3f12`, 224 records, **0 errors and 0 warnings**.
- Catalogue SHA-256: `d5e10e6c23e0b0982a0c20c229be0b549832e9e8669b364513c22df7ce00ede8`. Previous hash-named files retained.
- Published-file hashes and all pinned-toolkit checksums verified. No engine/toolkit update or package installation was required.
- Browser checks: direct chapter opening; four mapped findspots; uncertainty ranges on the BP timeline; timeline selection opens Al Wusta; DE/EN event and fossil details; local cave photograph; full skull image viewer (549 × 570) with credit; fossil-to-attestation graph; Back/Forward; chapter search by `Misliya`; scoped fossil list has exactly four new-chapter specimens.
- Combined selection with The Cradle of Humankind: chapters ordered chronologically, seven fossil/specimen entries, seven events and **one** shared Homo sapiens identity.
- Browser rendering used the engine's SVG fallback because WebGL2 is unavailable in the test environment. GPU globe rendering was not verified here.
