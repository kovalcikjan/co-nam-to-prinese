# CausalImpact

**Oblast 3 · Měření skutečného dopadu** · otázka oblasti: *Kolik z toho je naše zásluha?*

## Jednou větou

**Když kontrolní skupina chybí, model ji poskládá z jiných řad.** Model z dat, která tvoje změna neovlivnila, odhadne, jak by to vypadalo bez ní. Rozdíl proti skutečnosti je tvůj efekt.

## Kdy použít

- Když jsi změnil celý web nebo celou kampaň a kontrolní skupina není.
- Když máš jiná data, která změna neovlivnila (jiný trh, hledanost oboru).

## Kdy ne

- Když se i srovnávací data změnila kvůli tvému zásahu.
- Když máš krátkou historii před změnou.

## Co potřebuješ

- Dlouhou řadu dat před změnou a po ní.
- Jednu nebo víc srovnávacích řad, které změna neovlivnila, ale normálně se hýbou podobně.

## Postup s AI

1. Dej AI svou řadu a srovnávací řady.
2. Nech ji napsat skript s open-source knihovnou CausalImpact nebo podobným modelem.
3. Model odhadne, jak by to vypadalo bez změny.
4. Rozdíl proti skutečnosti je tvůj efekt, i s rozpětím.

## Příklad z marketingu

Změnil jsi strukturu celého e-shopu. Srovnávací řadou je hledanost oboru a návštěvnost podobného webu bez změny. Model ukáže, kolik návštěv navíc nová struktura přinesla.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Výsledek stojí a padá na srovnávacích řadách. Když se chovají jinak, efekt je špatně.
- Je to statistický model, ne experiment. Ber výsledek jako dobrý odhad, ne jako důkaz.

## Související metody

- [Časové řady](../3-mereni-dopadu/casove-rady.md): trend, sezónnost a mimořádné události
- [Difference-in-Differences](../3-mereni-dopadu/difference-in-differences.md): srovnat změnu se srovnatelnou kontrolní skupinou
- [Prediktivní modely](../4-predikce/prediktivni-modely.md): kolik poptávky a tržeb přijde samo

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou CausalImpact.

Změnil jsem [co] k datu [datum] a kontrolní skupinu nemám. Mám tato data před změnou a po ní: [data] a srovnávací řady, které změna neovlivnila: [data]. Odhadni, jak by to vypadalo bez změny, a spočítej efekt jako rozpětí.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda causalimpact
```
