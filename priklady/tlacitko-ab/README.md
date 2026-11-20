# Příklad 2: Vyplatí se nové tlačítko?

Ukázka 3 z přednášky. Metoda [Experimenty a Bayesovské testování](../../metody/3-mereni-dopadu/bayesovske-testovani.md),
krok 4 kruhu (`/zmer`).

**Všechna čísla jsou vymyšlená** pro přednášku, na příkladu webu cleverpujcky.cz.

## Rozhodovací otázka

Ve srovnávači půjček testujeme tlačítko. A je dnešní „Zobrazit půjčku“, B nové „Porovnat nabídky“.
Nasadit B? A co to přinese?

## Vstupy

| | Návštěvy | Prokliky na partnera | Míra prokliku |
|---|---|---|---|
| A (dnes) | 2 400 | 288 | 12,0 % |
| B (nové) | 2 400 | 324 | 13,5 % |

Srovnávač má 3 000 návštěv měsíčně, proklik má hodnotu 54 Kč (schválení 6 % × provize 900 Kč).

## Postup

1. Klasické vyhodnocení (test dvou podílů) pro srovnání.
2. Bayesovské vyhodnocení: z počtů prokliků se spočítá rozdělení skutečné míry prokliku obou variant
   (Beta rozdělení) a z 20 000 vzorků pravděpodobnost, že je B lepší.
3. Rozdíl se převede na Kč za měsíc a spočítá se, kolik riskujeme, když zvolíme B a mýlíme se.

## Výsledek

| | |
|---|---|
| Klasicky | p = 0,12, „rozdíl není průkazný“, tedy zase „uvidíme“ |
| Bayesovsky | B je lepší s pravděpodobností 94 % |
| Přínos B za měsíc (80 % scénářů) | 440 až 4 410 Kč, průměr 2 440 Kč |
| Riziko, když se mýlíme | v průměru 40 Kč měsíčně |

**Rozhodnutí:** nasadit B. Riziko je malé proti očekávanému přínosu.

## Jak to spustit

```bash
python3 vyhodnoceni.py
```

Stačí Python 3, žádné další knihovny. Vypíše výsledky a uloží `vysledek.html`. Svá čísla doplníš nahoře
ve skriptu (`A`, `B`, `VISITS_PER_MONTH`, `VALUE_PER_CLICK`).
