---
name: start
description: Začátek práce s repem. Použij, když uživatel napíše /start, neví, kde začít, nebo popisuje rozhodnutí typu „vyplatí se nám X?“, „kolik to přinese?“, „co dělat jako první?“, „fungovalo to?“. Zeptá se na rozhodnutí, vybere cestu (vedené kroky nebo jedna metoda), založí složku projektu se zápisem a navrhne další příkaz.
---

# Start: o čem rozhoduješ?

Text za příkazem (ARGUMENTS) je popis rozhodnutí, pokud ho uživatel napsal rovnou.

## Postup

1. Pokud popis chybí, zeptej se jedinou otázkou: **„O čem rozhoduješ? Stačí jedna věta.“**
2. Zařaď rozhodnutí do jedné z cest:

   | Uživatel řeší | Cesta | Další příkaz |
   |---|---|---|
   | Kolik něco přinese, jestli se to vyplatí | vedené kroky od začátku | `/odhadni` |
   | Výběr mezi víc projekty, co dělat první | odhad každého projektu, pak rozhodnutí | `/odhadni` (pak `/rozhodni`) |
   | Co by se mohlo pokazit, co tím ovlivníme jinde | kontrola plánu | `/proverit` |
   | Jestli něco fungovalo, kolik je naše zásluha | měření po spuštění | `/zmer` |
   | Chce konkrétní metodu nebo se jen rozhlédnout | katalog | `/metody` nebo `/metoda <název>` |

3. Vymysli krátký název projektu bez diakritiky a mezer (třeba `pujcka-na-auto`). Zjisti dnešní datum
   příkazem `date +%F`. Založ `projekty/<nazev>/zapis.md` podle šablony níže.
4. Odpověz krátce: co jsi pochopil (jednou větou), kterou cestu navrhuješ a proč, kde je zápis a jaký je další
   příkaz. Nic zatím nepočítej.

## Šablona zápisu

```markdown
# <Název projektu>

Založeno: <datum>

## Rozhodnutí
<jednou větou, o čem se rozhoduje a do kdy>

## Referenční třída
<jak dopadly podobné věci; doplní /odhadni a /zmer>

## Krok 1: Odhad

## Krok 2: Rozhodnutí

## Krok 3: Co nám mohlo uniknout

## Krok 4: Měření
```

Pravidla práce (rozpětí, čísla od člověka, počítá kód) jsou v `CLAUDE.md` v kořeni repa.
