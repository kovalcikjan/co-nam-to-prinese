---
name: metody
description: Přehled všech 40 metod ze 7 oblastí a výběr té správné. Použij, když uživatel napíše /metody, chce vidět, jaké metody existují, nebo se ptá „jakou metodu na to použít?“, „jak to spočítat?“, „čím to změřit?“. S otázkou za příkazem doporučí jednu až tři metody a řekne, jak je spustit.
---

# Metody: přehled a výběr

Text za příkazem (ARGUMENTS) je otázka nebo situace uživatele. Může chybět.

## Bez otázky: přehled

Vypiš sedm oblastí, ke každé otázku oblasti a názvy metod (bez dlouhých popisů). Zdroj je tabulka v `README.md`
a soubory v `metody/`. Na konci nabídni: „Napiš, o čem rozhoduješ, a doporučím metodu. Nebo rovnou
`/metoda <název>`.“

| Oblast | Otázka | Složka |
|---|---|---|
| 1 Pravděpodobnost a nejistota | Jaké výsledky jsou možné? | `metody/1-nejistota/` |
| 2 Rozhodování a prioritizace | Co udělat jako první? | `metody/2-rozhodovani/` |
| 3 Měření skutečného dopadu | Kolik z toho je naše zásluha? | `metody/3-mereni-dopadu/` |
| 4 Predikce a strojové učení | Co nás nejspíš čeká? | `metody/4-predikce/` |
| 5 Optimalizace zdrojů | Jak rozdělit čas a peníze? | `metody/5-optimalizace/` |
| 6 Ekonomika a byznys | Kdy se nám to vrátí? | `metody/6-ekonomika/` |
| 7 Modelování systémů | Co tím ovlivníme jinde? | `metody/7-systemy/` |

## S otázkou: doporučení

1. Najdi oblast, na jejíž otázku se uživatel ptá. Když jich je víc, vezmi nejvýš dvě.
2. Přečti soubory metod z té oblasti (sekce „Kdy použít“ a „Kdy ne“) a vyber jednu až tři, které sedí.
3. Ke každé napiš jednou větou, proč sedí na jeho případ, a co od něj bude potřebovat (sekce „Co potřebuješ“).
4. Doporuč jednu jako první a napiš příkaz: `/metoda <název-souboru-bez-.md>`. Když jde o celé rozhodnutí
   (odhad, výběr, kontrola, měření), nabídni místo toho vedené kroky od `/start`.
5. Nic nepočítej, jen doporuč.
