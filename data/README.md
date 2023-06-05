# Collated Game Data

Contains search phrases to find in text & associated game data & image asset keys. Search phrases should be lowercase and should only contain characters in the `ALLOWLIST` (character search whitelist) as defined in [CONFIG.py](../CONFIG.py).

To reduce OCR (image-to-text) errors, keep the `ALLOWLIST` as small as possible (e.g. quotes `"` are not needed. `"They" Too Were Once Flawless` can be searched using the phrase `too were once flawless`).

The search phrases do not need to match the entire text, it just has to be unique enough to identify the location/character/domain.

Image asset keys have the same names as image files in [Image Assets](../Image%20Assets/), but are all lowercase, do not contain the file extension and spaces are replaced with underscores. E.g. [Image Assets/Char Kirara.png](../Image%20Assets/Characters/Char%20Kirara.png) has the image asset key `char_kirara`. These have to be manually updated by the discord app owner [@euwbah](https://github.com/euwbah).

## [Characters](characters.csv)

```csv
lowercase search phrase, character image asset, character display name
kaveh,                   char_kaveh,            Kaveh
```

Character image assets are located in [Image Assets/Characters](../Image%20Assets/Characters/).

## [Domains/Trounce weekly bosses](domains.csv)

```csv
lowercase search phrase, domain name,                        domain type, location image asset
obsession,               Tower of Abject Pride | Obsession,  forgery,     domain_forgery_sumeru
```

Domain image assets are located in [Image Assets/Domains](../Image%20Assets/Domains/).

> ⚠️ This list is incomplete. In need of contributions for one-time domains.
>
> 🟠 The `domain type` values must match the strings in the function `DomainType.from_str()`
> 
> 🟠 Weekly bosses in Trounce Domains are listed here as well.

## [Locations/Points of interest](locations.csv)

```csv
lowercase search phrase, location name, subarea name, country name, location emblem image asset
wuwang hill,             Wuwang Hill,   Bishui Plain, Liyue,        emblem_liyue
```

Location emblem image assets are in [Image Assets/Location Emblem](../Image%20Assets/Location%20Emblem/).

This list includes locations, subareas, points of interest, and search text pertaining to specific areas like `chubby` or `tubby` for detecting teapot, `prince` and `cat's tail` for detecting cat's tail, etc...

> ⚠️ This list is incomplete. (Missing certain points of interest that are not considered subareas (e.g. Treasures Street)).
>
> ⚠️ It is currently assumed that **commas are not part of location names**. If this changes in the future, the map teleport location text detection search will need to work differently (it truncates everything after the first comma to omit the area from the location search, otherwise all subareas in mondstadt will register as the subarea mondstadt city)
> 
> 🟠 Some location emblems/entries are for limited-time events, which can be deleted once no longer used.
>
> 🟠 Location search phrase should be as short as possible while maintaining uniqueness.
> For long location names, use the middle part of the location name as the search phrase.

## [World bosses](bosses.csv)

```csv
lowercase search phrase, boss name,        boss image asset
aeonblight drake,        Aeonblight Drake, boss_aeonblight_drake
```

> 🟠 NOTE: This list does not include Trounce Domains, those go under domains.
>    Only add world bosses into this list.
>
> 🟠 Andrius is considered a world boss, since there's no domain text to scan to identify the boss fight action.