# Příklad 3: Do čeho dát příštích 40 hodin?

Ukázka 6 z přednášky. Metody [Doba návratnosti](../../metody/6-ekonomika/doba-navratnosti.md),
[Očekávaná hodnota](../../metody/2-rozhodovani/ocekavana-hodnota.md) a
[Portfolio optimalizace](../../metody/5-optimalizace/portfolio.md), krok 2 kruhu (`/rozhodni`).

**Všechna čísla jsou vymyšlená** pro přednášku, na příkladu webu cleverpujcky.cz.

## Rozhodovací otázka

Máme 40 hodin. Kam je dát: do stránky „půjčka na auto“, do lepší kalkulačky, nebo do série článků
z finanční gramotnosti?

## Vstupy

| Projekt | Hodiny (× 800 Kč) | Šance, že zabere | Přínos po rozjezdu | Náběh |
|---|---|---|---|---|
| Půjčka na auto | 25 h (20 000 Kč) | 40 % na top 10 | z [příkladu 1](../pujcka-na-auto/) | 2 až 8 měsíců |
| Kalkulačka | 15 h (12 000 Kč) | 85 % | 1 500 až 4 000 Kč měsíčně | od 2. měsíce |
| Finanční gramotnost | 40 h (32 000 Kč) | 50 % | 1 000 až 6 000 Kč měsíčně | 6 až 12 měsíců |

## Postup

Stejná simulace jako v příkladu 1, jen pro tři projekty a po měsících na dva roky dopředu. U každého
scénáře se sčítá přínos minus náklady a hledá se měsíc, kdy se projekt vrátí.

## Výsledek

| Projekt | Očekávaně na hodinu | Nevrátí se do roka | Návratnost (medián) |
|---|---|---|---|
| Půjčka na auto | 4 400 Kč | 60 % scénářů | ve víc než polovině scénářů ne do 2 let |
| Kalkulačka | 2 700 Kč | 15 % scénářů | 6. měsíc |
| Finanční gramotnost | 0 Kč | 89 % scénářů | ve víc než polovině scénářů ne do 2 let |

**Rozhodnutí:** kalkulačka je jistá malá výhra, auto velká sázka s nejvyšším očekávaným přínosem. Do 40 hodin
se vejdou obě. U auta nejdřív levně ověř, jestli se stránka dostane do top 10. Simulace nepočítá
s kanibalizací jiných stránek, to řeší krok 3 (`/proverit`).

## Jak to spustit

```bash
python3 porovnani.py
```

Stačí Python 3, žádné další knihovny. Vypíše výsledky a uloží `vysledek.html` s grafem návratnosti v čase.
Vstupy změníš nahoře ve skriptu (`AUTO`, `PROJECTS`, `RATE`, `CAPACITY`).
