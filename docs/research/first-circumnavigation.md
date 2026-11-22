# First circumnavigation, 1519–1522

Research scope: one voyage, with selected stations and the conflict on Mactan. This is a usable historical sample, not a complete expedition database or a global history. Sources were consulted on 22 November 2026 by the AI research/implementation assistant. All records remain **draft**; there has been no independent specialist or human historical review.

## What is included

The original sample had 48 records: 15 entities (4 people, 9 places, one ship and one historically bounded community), 12 events, one dated assertion, 10 geometries, 8 sources, one chapter and one package. The voyage still uses those historical identities. Rio Bay, the Cape of Good Hope, their two geometries, the Elkano itinerary and USNO calendar source now have a single owner in `package:maritime-shared`, reused by the additional voyage packages without changing their IDs. German and English chapter text and entity descriptions are maintained separately. No synthetic record is selected by dataset.json.

The chapter starts with the entire voyage period. The main route is a schematic itinerary, not the location of one ship on the selected date. Events supply dated points; setting a single year filters those points. Participation in an event does not imply participation for its entire duration: Magellan died during the expedition. Lapulapu's personal presence in the fighting is expressly uncertain.

## Source reading

The canonical source records contain URLs, access dates and bibliographic limitations. Every historical record has locators rather than bare links.

- UNESCO: title and introductory paragraphs of the documentary-register entry, for the expedition's scope and completion.
- Fundación Elkano: the institutional exhibition's itinerary paragraphs, for selected stations and their conventional dates.
- Museo Naval: preparation, voyage, Magellan's death, arrival at Tidore and return sections. The exhibition's Cape Verde date conflicts with the Elkano itinerary; no Cape Verde dated event is published here.
- Pigafetta: opening/departure and closing/return passages of the 1874 Stanley translation, read through Wikisource. This is a participant's narrative in a later translation, not direct consultation of a manuscript. No extended quotation is distributed.
- NHCP: registry entry and text of the 1951 Lapulapu memorial marker, a commemorative source, not an eyewitness account or a geodetic survey.
- Ybiernas and Chua / National Quincentennial Committee: indexed full-text version of “Battle of Mactan Beyond Textbooks”, particularly “The Showdown in Mactan”, including the explicit uncertainty about Lapulapu's presence. Direct access returned HTTP 403. Interpretations in unrelated sections are not imported wholesale.
- Archivo General de Indias: indexed full text of its description of a contemporary copy of Elcano's letter, identifying the return at Sanlúcar. Direct access returned HTTP 429. The original letter and facsimile were not inspected.
- US Naval Observatory: calendar notes, solely for the technical normalization method.

## Dates and geometry

Day labels preserve the conventional Julian expedition chronology under time.original. Between March 1500 and February 1700 the proleptic Gregorian date is ten days later. That arithmetic is used in earliest/latest; the reader sees the original label, and the calculation date is available in Details. This conversion does not resolve voyage clock discrepancies or establish a modern local civil date at Pacific stations. No finer timing than the consulted chronology is claimed.

The nine points are manually authored, rounded to 0.1 degree and explicitly schematic, with unknown historical positional accuracy. They orient the reader to a city, island, bay, strait or cape; they do not identify surveyed historical harbour positions or a precise battlefield. Modern countries in the place summaries are orientation aids, not political assignments in 1521.

The route is original line work based on the selected itinerary. Extra vertices only shape the ocean crossings and are not historical observations. The Pacific crossing is split at ±180 degrees. The path omits stops and simplifies passages, especially within island groups. It must not be used for distances, sailing speeds or archaeological location. No external map, portrait, manuscript or 3D model is copied. Distributed text and original geometry use the repository's existing GPL-2.0 license; linked publications retain their own rights.

## Deliberate limits

No invented political boundaries, reconstructed ship model, language genealogy or ethnic map is added merely to fill a menu category. Mactan's defenders are a specific group associated with the event, not a timeless homogeneous people. No claim that the expedition first established the Earth's spherical shape is made.

The authoring validator verifies structure, references, geometry and ownership. It does not establish historical truth. Remaining review work includes independent checking of dates, broader scholarship on local perspectives, and greater cartographic precision where warranted.
