# Korelace versus kauzalita

**Oblast 3 · Měření skutečného dopadu** · otázka oblasti: *Kolik z toho je naše zásluha?*

## Jednou větou

**Růst po kampani není automaticky jejím důsledkem.** Dvě věci rostou zároveň, ale jedna nemusí způsobovat druhou. Prodeje mohly vzrůst kvůli sezóně, ne kvůli kampani.

## Kdy použít

- Pokaždé, když vidíš „po kampani to vzrostlo“.
- Když reportuješ výsledky klientovi.

## Kdy ne

- Když máš čistý experiment s náhodným rozdělením. Ten příčinu řeší sám.

## Co potřebuješ

- Data před změnou a po ní.
- Seznam všeho, co se ve stejné době dělo (sezóna, update, jiné kampaně, ceny).

## Postup s AI

1. Popiš AI, co se změnilo a co jsi udělal.
2. Nech vypsat všechna jiná vysvětlení růstu.
3. U každého se zeptej, jak ho ověřit nebo vyloučit.
4. Výsledek formuluj opatrně („vzrostlo po kampani“), dokud nemáš srovnání.

## Příklad z marketingu

Po spuštění kampaně vzrostly prodeje o 30 %. Jenže byl prosinec a loni ve stejné době vzrostly o 25 %. Kampaň mohla přidat jen pár procent, ne třicet.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Sezóna, updaty vyhledávače a návrat k průměru vypadají jako úspěch.
- Čím víc metrik sleduješ, tím víc náhodných souvislostí najdeš.

## Související metody

- [Kauzální grafy (DAG)](../7-systemy/kauzalni-grafy.md): nakresli, co co ovlivňuje, než začneš měřit
- [Difference-in-Differences](../3-mereni-dopadu/difference-in-differences.md): srovnat změnu se srovnatelnou kontrolní skupinou
- [Časové řady](../3-mereni-dopadu/casove-rady.md): trend, sezónnost a mimořádné události

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Korelace versus kauzalita.

Po [co jsem udělal] se změnilo [co]. Vypiš všechna jiná možná vysvětlení té změny a ke každému napiš, jak ho ověřit nebo vyloučit.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Drž se mého konkrétního případu, ne obecných rad. Na konci jednou větou napiš, co z toho plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda korelace-vs-kauzalita
```
