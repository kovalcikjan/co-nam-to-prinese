---
name: rozhodni
description: Krok 2 ze 4, Rozhodni. Použij, když uživatel napíše /rozhodni nebo vybírá mezi víc projekty, ptá se „co dělat jako první?“, „co se vejde do kapacity?“, „kdy se nám to vrátí?“. Spočítá očekávanou hodnotu na hodinu, návratnost a riziko, najde nejlepší kombinaci do kapacity a řekne, co nejdřív levně ověřit. Pak navrhne /proverit.
---

# Krok 2: Rozhodni

Metody: očekávaná hodnota (`metody/2-rozhodovani/ocekavana-hodnota.md`), hodnota informace
(`metody/2-rozhodovani/hodnota-informace.md`), portfolio optimalizace (`metody/5-optimalizace/portfolio.md`),
doba návratnosti (`metody/6-ekonomika/doba-navratnosti.md`). Vzor výpočtu: `priklady/tri-projekty/porovnani.py`.

## Postup

1. **Projekt.** Přečti `projekty/<nazev>/zapis.md`. Když chybí odhad z kroku 1, nabídni `/odhadni`.
2. **Možnosti.** Zjisti, s čím se projekt porovnává (další projekty, „nedělat nic“), kolik má každý hodin
   nebo peněz a jaká je kapacita (třeba 40 hodin měsíčně). U možností bez odhadu stačí rychlé rozpětí
   (měsíční přínos, šance, že zabere, náběh), ale zeptej se na ně uživatele.
3. **Výpočet.** Napiš a spusť `projekty/<nazev>/rozhodnuti.py` (standardní knihovna, pevný seed). U každé možnosti:
   - očekávaný přínos za 24 měsíců minus náklady a přínos na hodinu práce,
   - šance, že se do roka nevrátí, a ve kterém měsíci se nejspíš vrátí,
   - u kombinací, které se vejdou do kapacity: očekávaný přínos a šance na špatný výsledek.
4. **Hodnota informace.** Najdi předpoklad s největší nejistotou (z kroku 1 nebo podle rozptylu) a navrhni levný
   test, který ho ověří dřív, než se utratí celé náklady. Porovnej cenu testu s tím, o co jde.
5. **Výstup.** Ulož `projekty/<nazev>/rozhodnuti.html` (tabulka možností, graf návratnosti v čase jako vložené SVG).
6. **Zápis.** Do sekce „Krok 2: Rozhodnutí“ připiš výsledky, doporučenou kombinaci a co ověřit nejdřív.

## Odpověď uživateli

- Doporučení jednou větou (třeba „Do 40 hodin: kalkulačka a stránka o autě, u stránky nejdřív levně ověř top 10.“).
- Krátká tabulka: možnost, přínos na hodinu, šance, že se do roka nevrátí, návratnost.
- Kde je HTML.
- Další krok: **`/proverit`** (co nám mohlo uniknout, než se do toho pustíme).
