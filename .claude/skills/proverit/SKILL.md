---
name: proverit
description: Krok 3 ze 4, Hledej, co ti uniklo. Použij, když uživatel napíše /proverit nebo se ptá „co by se mohlo pokazit?“, „co nejvíc hýbe výsledkem?“, „co tím ovlivníme jinde?“. Udělá analýzu citlivosti, kauzální graf (vedlejší efekty, kanibalizace) a pre-mortem, upraví odhad a připraví plán měření. Pak navrhne /zmer po spuštění.
---

# Krok 3: Hledej, co ti uniklo

Metody: analýza citlivosti (`metody/1-nejistota/analyza-citlivosti.md`), kauzální grafy
(`metody/7-systemy/kauzalni-grafy.md`), pre-mortem (`metody/2-rozhodovani/pre-mortem.md`).

## Postup

1. **Projekt.** Přečti `projekty/<nazev>/zapis.md` a výpočty z kroků 1 a 2 (`odhad.py`, `rozhodnuti.py`).
2. **Citlivost.** Nastav vstupy na střed rozpětí a hýbej vždy jedním od 10. k 90. percentilu. Seřaď je podle vlivu
   na výsledek (tornádová tabulka). Ten nahoře je kandidát na první ověření.
3. **Co tím ovlivníme jinde.** Nakresli kauzální graf (jednoduché šipky v textu nebo Mermaid): co výsledek
   ovlivňuje a co projekt ovlivní mimo sebe (kanibalizace jiných stránek, dopad na jiné kanály, sezóna).
   Zeptej se uživatele, jestli něco chybí.
4. **Pre-mortem.** „Je rok po spuštění a projekt nevyšel. Proč?“ Deset důvodů pro tento konkrétní případ, seřazených
   podle pravděpodobnosti a dopadu. Ke třem nejhorším: jak jim předejít nebo je včas poznat.
5. **Úprava odhadu.** Když se našel efekt, který odhad nezahrnul (třeba kanibalizace), zeptej se na jeho rozpětí,
   přidej ho do `odhad.py`, spusť znovu a porovnej s původním výsledkem.
6. **Plán měření.** Domluv předem, jak se výsledek změří: metrika, kontrolní skupina (náhodná, nebo srovnatelné
   stránky), kdy vyhodnotit a co bude úspěch. Bez plánu předem se později měří špatně.
7. **Zápis.** Do sekce „Krok 3: Co nám mohlo uniknout“ připiš citlivost, graf, pre-mortem, úpravu odhadu
   a plán měření.

## Odpověď uživateli

- Co nejvíc hýbe výsledkem a jak to levně ověřit.
- Tři největší rizika a co s nimi.
- Jestli a jak se změnil odhad.
- Plán měření ve třech bodech.
- Další krok: spustit projekt a po domluvené době **`/zmer`**.
