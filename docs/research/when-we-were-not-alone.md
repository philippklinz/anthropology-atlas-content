# When We Were Not Alone / Als wir nicht allein waren

Research draft, 2026-11-22. Chapter `chapter:when-we-were-not-alone`; owner `package:human-encounters`.

## Scope and learning sequence

Three selected stories at four Eurasian sites: immediate parental ancestry at Denisova; recent ancestry among early Homo sapiens at Bacho Kiro; individual kinship between Ranis and Zlatý kůň. The 120,000–40,000 BP viewing window overlaps the early-dispersal chapter. This is not a complete census of contemporary human groups, a single migration or a linear replacement narrative. The reader compares the strength and meaning of different genetic inferences.

## Source review

The Slon et al. (2018) original article was consulted through the Universidade de São Paulo teaching repository. Hajdinjak et al. (2021) was read as the full article through Europe PMC's fullTextXML service. Sümer et al. was read in UCL's Accelerated Article Preview, published online 12 December 2024; locators refer to its headings and numbered manuscript lines. Smith et al. (2024) was consulted in the published version hosted by Reading. Brown et al. (online 2021, journal issue 2022), especially Fig. 3b and its caption, was consulted in the author-hosted PDF. Tsanova et al. (2024), the excavating institute's Denisova page and the Czech cave administration support the orientation points.

The broader 2019 Denisova chronology is used through the explicitly attributed reproduction in Brown et al.; the chapter does not pretend that all original supplementary dating models were independently reanalysed. Published facts and models are distinguished from the atlas's explanatory synthesis. Scientific papers are linked, not redistributed.

## Dates and uncertainty

| Evidence | Representation | Meaning and limitation |
|---|---|---|
| Denisova 11 | Approximate instant envelope, 118,100–79,300 BP | Brown et al., Fig. 3b: Bayesian age model attributed to Douka et al. (2019), combining different dating evidence. No invented symmetric error bar or occupation duration. |
| Bacho Kiro / F6-620 | Approximate contextual envelope, 45,930–42,580 cal BP | Hajdinjak et al., main text: collective age envelope of early sampled individuals. Explicitly not F6-620's individual measured interval. |
| Ranis / Ranis4 | Approximate contextual envelope, 49,540–42,200 cal BP | Sümer et al., Introduction: eleven human bones collectively, 95.4% ranges. Not a direct individual date for Ranis4, nor its lifespan. |
| Zlatý kůň | Approximate point around 45,000 BP | Sümer et al., Dating Zlatý kůň: relative age inferred from shared DNA with Ranis; direct radiocarbon dating compromised by animal-derived glue. Independent molecular models yield point estimates around 47–48 ka with large uncertainty. No unsupported numerical confidence interval is fabricated. |

All deep-time values use the engine's fixed 1950 reference. Uncalibrated radiocarbon ages are not substituted for calendar ages. Chapter boundaries are editorial, not natural historical boundaries. Genetic assertion dates locate the sampled evidence: they never pretend to date conception, a migration or the earlier admixture event.

## Three kinds of genetic claim

- Denisova 11: Slon et al., nuclear and mitochondrial evidence, supports an immediate Neanderthal mother and Denisovan father. Minimum age at death is at least 13 years, not exactly 13. No Homo sapiens participation is added to this event.
- F6-620: Hajdinjak et al., Fig. 3 and main text, supports recent Neanderthal ancestry. The under-six-generations estimate is labelled as the **2021 model**, not an exact family tree or a result guaranteed under every later model. The 2024 Sümer synthesis uses different generational estimates for Bacho Kiro in its introduction; the chapter's headline deliberately uses qualitative “recent ancestors.”
- Ranis4 / Zlatý kůň: Sümer et al., Fig. 2, identifies fifth- or sixth-degree genetic kinship; Ranis4 is correctly distinguished from Ranis13, the high-coverage individual used for other comparisons. Kinship degrees here are statistical genetic categories, not legal civil-law degrees. Several pedigrees may fit. A personal meeting and an actual travelled route cannot be reconstructed from this result alone.

The engine's dedicated `has-genetic-ancestry-from` and symmetric `genetically-related-to` predicates carry explicit notes and supporting locators. The specimen endpoints each represent one sampled individual. Denisovans and Neanderthals are biological lineages, not modern peoples, cultures or language groups. No transitive genetic inference is generated. Ancient-DNA methodology is explained as modern research, not a prehistoric invention. The shared Homo sapiens identity retains its canonical owner in `package:human-origins`.

## Geography

| Point [longitude, latitude] | Editorial accuracy | Derivation |
|---|---:|---|
| Denisova [84.68, 51.4] | 2 km | IAET institutional description, nearby research-station coordinate 51º23′48″N 84º40′35″E, rounded to the cave area. |
| Bacho Kiro [25.43, 42.947] | 1 km | Tsanova et al., Background / Fig. 1, 42°56′48″N 25°25′49″E. |
| Ranis [11.565, 50.663] | 1 km | Smith et al., reporting-summary research location 50°39′45.3″N 11°33′53.5″E. |
| Zlatý kůň / Koněprusy [14.069, 49.916] | 1 km | Czech cave administration, GPS 49°54′58″N 14°04′08″E; visitor-site orientation, not the exact skull findspot. |

Accuracy values are editorial estimates, not surveyed statistical errors. Today's countries orient the reader; no ancient borders or ethnic territories are implied. The kinship relationship remains in the network, with no invented route line across the map. Western sites may overlap at the Eurasian overview scale; zooming and the timeline provide separate selection.

## Local media

Both supplied images were visually checked. Images are served with the content, without runtime Wikimedia requests.

| Asset | Rights | Treatment |
|---|---|---|
| `denisova-entrance` | Xenochka, CC BY-SA 4.0; [source](https://commons.wikimedia.org/wiki/File:%D0%A2%D0%B0%D0%B8%D0%BD%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F_%D0%BF%D0%B5%D1%89%D0%B5%D1%80%D0%B0.jpg), [license](https://creativecommons.org/licenses/by-sa/4.0/) | Wikimedia 1280 px derivative copied unchanged; 14 August 2013. Modern entrance, no landscape reconstruction. |
| `bacho-kiro-view` | Nenko Lazarov, CC BY 2.5; [source](https://commons.wikimedia.org/wiki/File:Bacho_Kiro_Cave.jpg), [license](https://creativecommons.org/licenses/by/2.5/) | Current 1024 × 768 original copied unchanged, including existing credit. Modern illuminated interior; EXIF date 4 June 2006. |

Media retain their own rights independently of the repository's GPL license. No fabricated portrait or fossil reconstruction is presented as historical evidence.

## Publication and review

All 40 new records remain research drafts. Structural validation is not independent historical peer review. The toolkit is deliberately pinned to engine commit `c2f02195e1b9f550f598e39b9b12a03d5458cc6c`, compiler `0.1.0-dev.7`, adding typed genetic relationships without an npm/Node toolchain. Browser export and verification results are recorded after source commit and compilation.

## Export and browser verification

- Committed canonical source: `e82c3993418d6d73be7efa7bb4c702457c1d2685`; ZIP made with `git archive` from that commit (340 selected source and payload files).
- Browser export: `draft-bf7cd701bf7265e53458`, 264 records, **0 errors and 0 warnings**; compiler `0.1.0-dev.7`.
- Catalogue SHA-256: `680677cef9b39b463c8d307be917902170575ae7704cf0267f3dbad5852383dc`. All catalogued file sizes and hashes verified; previously committed hashed payloads retained.
- Browser checks: direct chapter opening; four visible findsite markers; selected Denisova event highlighted; BP uncertainty ranges; the Denisova ancestry graph; cited Ranis4–Zlatý kůň relationship; visible relationship explanations in DE and EN; chapter overview text in both languages; local full-image viewer (Bacho Kiro, 1024 × 768); working image license links; Back/Forward; discovery search for `Ranis` returns this chapter.
- Scoped navigation: four fossil individuals, four events and four places in this chapter. Combined with the two previous human-origins chapters: chronological menu order, eleven fossils and eleven events, and exactly one shared Homo sapiens identity carrying all three chapter badges.
- Engine browser regression suite: 39/39 passed for the genetics extension. The reader's assertion-note display and CC license links were additionally checked in-browser; static checks passed. No Node/npm installation or build step was introduced.
- Browser rendering used the SVG fallback because WebGL2 is unavailable in the test environment. GPU globe rendering was not verified here.
