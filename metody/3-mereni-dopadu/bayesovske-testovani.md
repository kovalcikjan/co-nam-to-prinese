# Experimenty a Bayesovské testování

**Oblast 3 · Měření skutečného dopadu** · otázka oblasti: *Kolik z toho je naše zásluha?*  
**Krok v kruhu:** 4 Změř a zpřesni (`/zmer`)  
**Ukázka z přednášky:** [Tlačítko A/B: bayesovské vyhodnocení](../../priklady/tlacitko-ab/)

## Jednou větou

**Náhodné rozdělení; pravděpodobnost místo ano, nebo ne.** Lidi náhodně rozdělíš na dvě skupiny a každé ukážeš jinou variantu. Bayesovské vyhodnocení řekne, s jakou pravděpodobností je která lepší.

## Kdy použít

- Když můžeš návštěvníky náhodně rozdělit na dvě skupiny (A/B test).
- Když klasické vyhodnocení skončí „rozdíl není průkazný“ a ty stejně musíš rozhodnout.

## Kdy ne

- Když návštěvníky rozdělit nejde (změna celého webu). Pak difference-in-differences nebo CausalImpact.

## Co potřebuješ

- Počet návštěv a konverzí (třeba prokliků) v každé variantě.
- Kolik má jedna konverze hodnotu, pokud chceš výsledek v korunách.

## Postup s AI

1. Dej AI počty návštěv a konverzí obou variant.
2. Nech spočítat bayesovsky, s jakou pravděpodobností je B lepší.
3. Nech převést rozdíl na peníze za měsíc, jako rozpětí.
4. Zeptej se, kolik riskuješ, když zvolíš B a mýlíš se.
5. Rozhodni podle pravděpodobnosti a rizika, ne jen podle hranice 5 %.

## Příklad z marketingu

Tlačítko A mělo 12,0 % prokliků, B 13,5 %. Klasicky p = 0,12, tedy „není průkazné“. Bayesovsky je B lepší s pravděpodobností 94 % a přinese 440 až 4 410 Kč měsíčně, riziko je kolem 40 Kč.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Test neukončuj ve chvíli, kdy se ti výsledek hodí. Délku si urči předem.
- U malých dat hraje roli výchozí předpoklad. Napiš ho předem.

## Související metody

- [Bayesovská statistika](../1-nejistota/bayesovska-statistika.md): zpřesní odhad, když přijdou nová data
- [Holdout testy (inkrementalita)](../3-mereni-dopadu/holdout-testy.md): část lidí kampaň neuvidí, rozdíl je přínos kampaně
- [Multi-armed bandit](../5-optimalizace/multi-armed-bandit.md): testuje a zároveň vydělává

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Experimenty a Bayesovské testování.

Mám A/B test: varianta A [návštěvy, konverze], varianta B [návštěvy, konverze]. Jedna konverze má hodnotu [Kč] a měsíčně je [počet] návštěv. Vyhodnoť to bayesovsky: s jakou pravděpodobností je B lepší, kolik přinese za měsíc jako rozpětí a kolik riskuji, když zvolím B a mýlím se.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda bayesovske-testovani
```
