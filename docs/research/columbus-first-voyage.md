# Columbus's first Atlantic voyage, 1492–1493

This bounded chapter follows the first voyage outward and selected Niña return stations. It is not all four voyages or a general history of the Americas. Sources were consulted by the AI research/implementation assistant on 22 November 2026. Records remain **draft**, without independent specialist or human review.

## Scope

The package owns 44 records: 4 people, 3 ships, one historically bounded Lucayan community, 8 places, 11 events (journey and 10 stations), 9 geometries, 5 sources, one 3D asset, a chapter and its package manifest. It depends on `package:maritime-shared` for the calendar reference. The community represents the people encountered at Guanahani in 1492, not a timeless homogeneous category.

## Source reading and perspective

- The NVCC educational transcription of Markham's 1893 translation: departure on 3 August, departure from Gomera on 6 September, 11–15 October landfall/encounters, 28 October Cuba, 5–6 December Hispaniola, 25 December wreck and salvage, 2 January La Navidad/Guacanagarí, 16 January return departure, 18 February Azores, 4 March Tagus shelter and 15 March return. The 14–15 October passages record taking islanders and attempts to escape; these are not presented as voluntary participation. The text represents expedition claims and intentions, not an independent Indigenous account.
- William F. Keegan's Florida Museum discussion of the landfall debate: competing island identifications, archaeology and the loss/transmission of the original log. Guanahani is not equated with one modern island in this dataset.
- Library of Congress, Columbus and the Taíno: the inhabited Caribbean setting and the expedition's account. Its reproduced illustrations are not copied.
- US Naval Observatory calendar explanation, reused from the shared package: technical Gregorian/Julian normalization only.

Columbus's original log is lost; the surviving account is mediated by Las Casas and later translation. Editorial introductions and translated primary text are distinguished. The appended letter on the NVCC page is a different translation; dates here are based on the journal entries. No extended quotation is distributed.

## Dates and geographical uncertainty

Conventional voyage dates are Julian. In 1492–1493 the proleptic Gregorian calculation date is nine days later. `time.original` retains the original label and conversion note. This arithmetic does not resolve shipboard day-count questions. The 5–6 December Hispaniola event preserves the sighting/approach distinction as an interval.

All points are manually authored, rounded orientation aids. Guanahani is a **regional placeholder in the Bahamas**, explicitly not a selected candidate island or a measured landfall. The Santa María wreck uses a broad northern Hispaniola marker, not a claimed wreck site. Other coast and harbour markers are schematic too. Modern country names aid orientation without assigning modern borders to 1492.

The original line drawing selects outward and return stations; vessels separated, and the return is not a common track for all three ships. Additional ocean vertices are visual interpolation, not historical observations. No archaeological map, portrait or third-party ship model is copied. The project-supplied 3D reconstruction is described below. Original project content uses GPL-2.0; linked publications retain their own rights.

## Checks and limits

Browser validation checks schema, references, package closure, dates and geometry. It cannot settle the landfall debate or verify historical truth. Independent review, broader Caribbean scholarship, more local perspectives and more precise geography remain work for a later editorial pass. Claims of possession, captivity and colonization are included in the chapter instead of treating the Caribbean as previously empty land.

## Santa María reconstruction, added 23 November 2026

The project supplied `santa_maria.glb`, a Blender export representing the ship on the 1492 voyage. It is linked to the existing `artifact:santa-maria` rather than creating a second ship identity, and is a direct chapter focus item. The model, its record and both additional bibliographic records belong to this package. German and English descriptions explain what the visitor can inspect and distinguish reconstruction from a documented original.

The GLB metadata identifies the transmitted journal, Powerhouse catalogue H4306 and Fundación Nao Victoria’s 2018 reconstruction documentation as references. The journal’s 25 December entry was re-read, together with the museum’s Description/History and the foundation’s launch report. The journal supports the voyage and wreck context. The other references describe later reconstructions; they do not establish the original ship’s precise form. The model itself labels its chosen 21.4 m hull length and 7.4 m beam as interpretive. No original plans or securely identified wreck were used, according to its metadata. Its referenced authoring note `quellen.md` was not part of the supplied file and was not reviewed.

All seven texture images are embedded. The supplied metadata identifies original procedural wood and linen textures and a hand-drawn banner, with no third-party photographs. The asset follows the project’s GPL-2.0 content licence. No reference-site images are copied. Only `scenes[0].extras.initialView` was added to the supplied GLB to give a useful starting view; all mesh and embedded-image bytes remain unchanged.

The model is approximately 17.9 MiB with 524,288 triangles. This exceeds the initial recommended per-exhibit budgets (10 MiB / 250,000 triangles); it is retained as supplied rather than silently reducing its detail. It is fetched only when the visitor opens the model. The source and hashed publication payload remain together in this content repository. Browser validation and interactive rendering checks cover technical integration, not an independent historical review of the reconstruction.
