# Difference-in-Differences

**Oblast 3 · Měření skutečného dopadu** · otázka oblasti: *Kolik z toho je naše zásluha?*

## Jednou větou

**Srovnat změnu se srovnatelnou kontrolní skupinou.** Porovnáš, jak se změnily stránky, které jsi upravil, a podobné stránky, na které jsi nesáhl. Co zasáhlo obě skupiny, třeba sezóna, se odečte samo.

## Kdy použít

- Když jsi změnil jen část stránek, kategorií nebo regionů a ostatní nechal.
- Když nejde dělat A/B test, ale máš srovnatelnou skupinu.

## Kdy ne

- Když se skupiny vyvíjely odlišně už před změnou. Pak srovnání klame.

## Co potřebuješ

- Data upravené a neupravené skupiny před změnou a po ní (třeba týdenní kliky ze Search Console).
- Datum změny.

## Postup s AI

1. Vyber srovnatelnou skupinu, na kterou jsi nesáhl (stejný typ stránek, podobná návštěvnost).
2. Dej AI data obou skupin před změnou a po ní.
3. Nech zkontrolovat, jestli se před změnou vyvíjely podobně.
4. Nech spočítat rozdíl změn a jeho nejistotu.

## Příklad z marketingu

Přepsal jsi 20 recenzí poskytovatelů a 37 nechal být. Upravené vzrostly o 40 %, neupravené o 25 %, protože přišla sezóna. Tvůj efekt je zhruba rozdíl mezi nimi, ne celých 40 %.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Skupiny se nesmí ovlivňovat navzájem (interní odkazy, kanibalizace).
- Nevybírej k úpravě jen nejlepší stránky. Pak srovnáváš nesrovnatelné.

## Související metody

- [Časové řady](../3-mereni-dopadu/casove-rady.md): trend, sezónnost a mimořádné události
- [CausalImpact](../3-mereni-dopadu/causalimpact.md): když kontrolní skupina chybí, model ji poskládá z jiných řad
- [Korelace versus kauzalita](../3-mereni-dopadu/korelace-vs-kauzalita.md): růst po kampani není automaticky jejím důsledkem

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Difference-in-Differences.

Změnil jsem [co] u skupiny [A], skupinu [B] jsem nechal. Tady jsou data obou skupin před změnou a po ní: [data]. Zkontroluj, jestli se před změnou vyvíjely podobně, a spočítej efekt metodou difference-in-differences jako rozpětí.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda difference-in-differences
```
