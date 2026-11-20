# Holdout testy (inkrementalita)

**Oblast 3 · Měření skutečného dopadu** · otázka oblasti: *Kolik z toho je naše zásluha?*

## Jednou větou

**Část lidí kampaň neuvidí, rozdíl je přínos kampaně.** Malé skupině lidí kampaň schválně nezobrazíš. Co navíc nakoupili ti, kdo ji viděli, je skutečný přínos kampaně, ne to, co by koupili i tak.

## Kdy použít

- U kampaní, kde nevíš, jestli by lidé nekoupili i bez nich (remarketing, e-maily, PPC na značku).
- Když platforma hlásí skvělé výsledky a ty chceš vědět, kolik je opravdu navíc.

## Kdy ne

- Když je skupina tak malá, že rozdíl neuvidíš. Pak test prodluž nebo skupinu zvětši.

## Co potřebuješ

- Možnost schválně vynechat náhodnou část lidí (třeba 10 % seznamu).
- Konverze obou skupin za stejné období.

## Postup s AI

1. Náhodně odděl kontrolní skupinu, která kampaň neuvidí.
2. Po skončení dej AI konverze obou skupin.
3. Nech spočítat rozdíl a jeho nejistotu, třeba bayesovsky.
4. Přínos navíc porovnej s náklady kampaně.

## Příklad z marketingu

Remarketing hlásí 500 objednávek. Kontrolní skupina, která reklamu neviděla, nakupovala skoro stejně často. Navíc tedy remarketing přinesl jen zlomek z hlášených 500.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Kontrolní skupina musí být náhodná, ne „ti, na které nezbyl rozpočet“.
- Vynechání stojí trochu tržeb. Je to cena za pravdivé číslo.

## Související metody

- [Experimenty a Bayesovské testování](../3-mereni-dopadu/bayesovske-testovani.md): náhodné rozdělení; pravděpodobnost místo ano, nebo ne
- [Uplift modeling](../4-predikce/uplift-modeling.md): u koho kampaň opravdu něco změní
- [Korelace versus kauzalita](../3-mereni-dopadu/korelace-vs-kauzalita.md): růst po kampani není automaticky jejím důsledkem

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Holdout testy (inkrementalita).

Pustil jsem kampaň [jakou]. Náhodná kontrolní skupina ji neviděla. Výsledky: kampaň [lidé, konverze], kontrola [lidé, konverze]. Spočítej přínos navíc jako rozpětí a porovnej ho s náklady [Kč].

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda holdout-testy
```
