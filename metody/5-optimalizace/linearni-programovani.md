# Lineární a celočíselné programování

**Oblast 5 · Optimalizace zdrojů** · otázka oblasti: *Jak rozdělit čas a peníze?*

## Jednou větou

**Co se vejde do hodin nebo rozpočtu.** Zadáš cíl, třeba největší přínos, a omezení, třeba 40 hodin a rozpočet. Výpočet najde nejlepší kombinaci, zvládne to i Excel Solver.

## Kdy použít

- Když vybíráš kombinaci projektů nebo rozděluješ rozpočet s pevnými omezeními (hodiny, peníze, lidé).
- Když je možností tolik, že je v hlavě neporovnáš.

## Kdy ne

- Když jsou přínosy tak nejisté, že optimalizace jednoho čísla klame. Pak přidej robustní optimalizaci.

## Co potřebuješ

- Seznam možností s přínosem a nároky (hodiny, peníze).
- Omezení: kolik hodin, jaký rozpočet, co musí být splněno.

## Postup s AI

1. Sepiš možnosti, jejich přínos a nároky.
2. Napiš AI cíl (třeba největší očekávaný přínos) a omezení.
3. Nech najít nejlepší kombinaci. U pár projektů stačí projít všechny kombinace, u větších Excel Solver nebo knihovna.
4. Nech ukázat i druhou a třetí nejlepší kombinaci a jak moc jsou horší.

## Příklad z marketingu

Máš 40 hodin a tři projekty: stránku „půjčka na auto“ (25 hodin), kalkulačku (15 hodin) a sérii článků (40 hodin). Do kapacity se vejde buď auto s kalkulačkou, nebo celá série. Výpočet porovná obě kombinace.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Výpočet je přesný, vstupy ne. Výsledek ber jako návrh.
- Zapiš všechna omezení. Co nezadáš, výpočet nebere v úvahu.

## Související metody

- [Portfolio optimalizace](../5-optimalizace/portfolio.md): mix jistých malých výher a velkých sázek
- [Robustní optimalizace](../5-optimalizace/robustni-optimalizace.md): plán, který vydrží chybu v odhadech
- [Opportunity cost](../6-ekonomika/opportunity-cost.md): co neuděláme, když uděláme tohle

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Lineární a celočíselné programování.

Mám tyto možnosti s přínosem a nároky: [tabulka]. Omezení: [hodiny, rozpočet, další]. Najdi kombinaci s nejvyšším očekávaným přínosem, která omezení splní, a ukaž i další dvě nejlepší kombinace.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda linearni-programovani
```
