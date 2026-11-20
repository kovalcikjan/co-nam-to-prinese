---
name: zmer
description: Krok 4 ze 4, Změř a zpřesni. Použij, když uživatel napíše /zmer nebo se ptá „fungovalo to?“, „kolik je naše zásluha?“, „vyhodnoť test“, „je B lepší?“. Vyhodnotí výsledek bayesovsky (A/B test, kontrolní skupina), porovná ho s původním odhadem, zapíše kalibraci a zpřesní referenční třídu pro příští odhad. Pak navrhne /odhadni pro další projekt.
---

# Krok 4: Změř a zpřesni

Metody: experimenty a Bayesovské testování (`metody/3-mereni-dopadu/bayesovske-testovani.md`), Bayesovská
statistika (`metody/1-nejistota/bayesovska-statistika.md`). Když náhodné rozdělení nebylo:
difference-in-differences (`metody/3-mereni-dopadu/difference-in-differences.md`) nebo CausalImpact
(`metody/3-mereni-dopadu/causalimpact.md`). Vzor výpočtu: `priklady/tlacitko-ab/vyhodnoceni.py`.

## Postup

1. **Projekt.** Přečti `projekty/<nazev>/zapis.md`, hlavně odhad z kroku 1 a plán měření z kroku 3.
   Když projekt v `projekty/` není, zeptej se, co se měří, a založ ho.
2. **Data.** Zeptej se na skutečné výsledky: u testu návštěvy a konverze každé varianty, jinak data upravené
   a srovnávací skupiny před změnou a po ní. Upozorni, když jde o citlivá data.
3. **Vyhodnocení.** Napiš a spusť `projekty/<nazev>/mereni.py`:
   - A/B test nebo kontrolní skupina: bayesovsky (Beta rozdělení), pravděpodobnost, že varianta pomohla,
     přínos v Kč jako rozpětí a riziko, když se mýlíme. Pro srovnání i klasické p.
   - Bez náhodného rozdělení: rozdíl změn proti srovnatelné skupině, s kontrolou, že se před změnou vyvíjely podobně.
4. **Porovnání s odhadem.** Padl skutečný výsledek do rozpětí z kroku 1? Zapiš to do kalibračního deníku
   (`sablony/kalibracni-denik.md` jako vzor, deník v projektu).
5. **Zpřesnění.** Aktualizuj referenční třídu (třeba ze „2 z 5 stránek v top 10“ na „3 z 6“) a napiš, jak se tím
   posune výchozí šance pro příští odhad.
6. **Výstup a zápis.** Ulož `projekty/<nazev>/mereni.html` a do sekce „Krok 4: Měření“ připiš výsledek, kalibraci
   a novou referenční třídu.

## Odpověď uživateli

- Výsledek jednou větou: „B je lepší s pravděpodobností X %, přinese Y až Z Kč měsíčně, riziko W Kč.“
- Jestli se odhad trefil do rozpětí a co to říká o příštích odhadech.
- Nová referenční třída.
- Další krok: **`/odhadni`** pro další projekt. Začíná teď z lepšího bodu. Tím se kruh uzavírá.
