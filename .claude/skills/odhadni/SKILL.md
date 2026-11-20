---
name: odhadni
description: Krok 1 ze 4, Odhadni rozpětí. Použij, když uživatel napíše /odhadni nebo chce vědět, kolik něco přinese, jestli se projekt vyplatí, nebo potřebuje odhad místo „čísla z hlavy“. Rozloží přínos na kroky, posbírá rozpětí a referenční třídu, spočítá Monte Carlo simulaci a výsledek zapíše do projektu. Pak navrhne /rozhodni.
---

# Krok 1: Odhadni rozpětí

Metody: odhad podle referenční třídy (`metody/1-nejistota/referencni-trida.md`), Monte Carlo simulace
(`metody/1-nejistota/monte-carlo.md`), prediktivní modely pro výchozí stav (`metody/4-predikce/prediktivni-modely.md`).
Vzor výpočtu: `priklady/pujcka-na-auto/simulace.py`.

## Postup

1. **Projekt.** Najdi projekt v `projekty/` (podle ARGUMENTS nebo poslední upravený) a přečti `zapis.md`.
   Když žádný není, zeptej se „O čem rozhoduješ?“ a založ ho jako `/start`.
2. **Co odhadujeme.** Ujasni výsledek a období (třeba „přínos v Kč za prvních 12 měsíců“) a náklady.
3. **Rozklad.** Navrhni rozklad přínosu na kroky, které se násobí (třeba hledanost × šance na top 10 × CTR ×
   proklik × konverze × hodnota konverze). Nech uživatele rozklad potvrdit nebo upravit.
4. **Referenční třída.** Zeptej se, jak dopadly podobné věci (třeba „kolik z tvých podobných stránek se dostalo
   do top 10“). Z toho je výchozí šance. Zapiš ji do sekce Referenční třída.
5. **Rozpětí.** Ke každému kroku posbírej nejméně, nejčastěji, nejvíc a zdroj. Nejvýš tři kroky najednou.
   Zeptej se i na „číslo z hlavy“, ať je s čím porovnat.
6. **Výchozí stav.** Když část výsledku přijde i bez projektu (sezóna, růst trhu), zeptej se na ni a odečti ji,
   případně použij prediktivní model.
7. **Simulace.** Napiš `projekty/<nazev>/odhad.py` (standardní knihovna, 10 000 scénářů, pevný seed) a spusť ho.
   Vypiš 10., 50. a 90. percentil, průměr, šanci, že nepokryje náklady, a porovnání s číslem z hlavy.
8. **Výstup.** Ulož `projekty/<nazev>/odhad.html` s histogramem jako vloženým SVG a tabulkou vstupů.
9. **Zápis.** Do sekce „Krok 1: Odhad“ v `zapis.md` připiš vstupy, výsledek a jednu větu pro rozhodnutí.

## Odpověď uživateli

- Výsledek jednou větou jako rozpětí: „S 80% pravděpodobností mezi X a Y, nejčastěji kolem Z.“
- Šance, že se to do roka nevrátí, a porovnání s číslem z hlavy.
- Kde je HTML.
- Další krok: **`/rozhodni`** (porovnat s jinými možnostmi a vybrat). Když je projekt jen jeden a rozhodnutí je
  ano/ne, nabídni i **`/proverit`** (co nejvíc hýbe výsledkem a co nám mohlo uniknout).
