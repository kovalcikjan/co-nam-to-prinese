# Příklad 1: Kolik přinese stránka „půjčka na auto“?

Ukázka 1 z přednášky. Metoda [Monte Carlo simulace](../../metody/1-nejistota/monte-carlo.md) a
[Analýza citlivosti](../../metody/1-nejistota/analyza-citlivosti.md), krok 1 kruhu (`/odhadni`).

**Všechna čísla jsou vymyšlená** pro přednášku, na příkladu webu cleverpujcky.cz.

## Rozhodovací otázka

Vyplatí se napsat novou srovnávací stránku „půjčka na auto“? Kolik přinese za rok?

## Vstupy (rozpětí: nejméně, nejčastěji, nejvíc)

| Krok | Rozpětí |
|---|---|
| Hledanost tématu za měsíc | 4 000 až 12 000, nejčastěji 7 000 |
| Dostaneme se do top 10? | šance 40 % (z 5 podobných stránek se tam dostaly 2) |
| CTR v top 10 | 4 až 20 %, nejčastěji 8 % (mimo top 10: 0 až 1 %) |
| Proklik na partnera | 15 až 35 %, nejčastěji 22 % |
| Schválení žádosti | 4 až 12 %, nejčastěji 6 % |
| Provize za schválený úvěr | 500 až 1 500 Kč, nejčastěji 900 Kč |
| Náklady | 25 hodin × 800 Kč = 20 000 Kč |

## Postup

Roční přínos = hledanost × 12 × CTR × proklik × schválení × provize. Program 10 000krát náhodně vybere hodnotu
z každého rozpětí a spočítá přínos. Pak hýbe vždy jedním vstupem, aby ukázal, co nejvíc rozhoduje.

## Výsledek

| | |
|---|---|
| Číslo z hlavy (všechno nejčastější, stránka v top 10) | kolem 80 tisíc Kč |
| 80 % scénářů | 2,7 až 211 tisíc Kč, nejčastěji kolem 10 tisíc |
| Průměr | 71 tisíc Kč |
| Šance, že se náklady do roka nevrátí | 59 % |
| Co nejvíc hýbe výsledkem | jestli se stránka dostane do top 10 (6 až 147 tisíc) |

**Rozhodnutí:** je to velká sázka, ne jistých 80 tisíc. Nejdřív levně ověř, jestli se stránka dostane do top 10,
třeba menším testovacím článkem.

## Jak to spustit

```bash
python3 simulace.py
```

Stačí Python 3, žádné další knihovny. Vypíše výsledky a uloží `vysledek.html` s grafem.
Vstupy změníš nahoře ve skriptu v `INPUTS`.
