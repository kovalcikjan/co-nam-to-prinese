# Rozhodovací stromy

**Oblast 2 · Rozhodování a prioritizace** · otázka oblasti: *Co udělat jako první?*

## Jednou větou

**Navazující kroky: nejdřív test, pak rozhodnutí.** Nakreslíš rozhodnutí jako větvení: co uděláš, co se může stát a co pak. Hned vidíš, jestli se vyplatí nejdřív malý test, nebo rovnou celý projekt.

## Kdy použít

- Když rozhodnutí probíhá v krocích: test, vyhodnocení, rozšíření.
- Když se ptáš, jestli nejdřív zkusit malý pilot.

## Kdy ne

- U jednoduchého ano, nebo ne bez navazujících kroků.

## Co potřebuješ

- Možné kroky a co se po každém může stát.
- Šance na jednotlivé výsledky a jejich přínos nebo náklad.

## Postup s AI

1. Popiš AI rozhodnutí a nech ji nakreslit strom: co uděláš, co se může stát, co pak.
2. Ke každé větvi doplň šanci a přínos nebo náklad.
3. Nech spočítat, která cesta má nejvyšší očekávanou hodnotu.
4. Zeptej se, kolik by stálo za to mít informaci dřív (hodnota informace).

## Příklad z marketingu

Buď napíšeš rovnou 10 článků, nebo nejdřív 2 testovací a podle výsledku dalších 8. Strom ukáže, jestli se test vyplatí: při neúspěchu ušetříš osm článků práce.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Strom rychle roste. Drž se dvou až tří kroků a hlavních větví.
- Šance ve větvích ber z dat nebo referenční třídy.

## Související metody

- [Hodnota informace (Value of Information)](../2-rozhodovani/hodnota-informace.md): kdy se vyplatí nejdřív levně ověřit
- [Očekávaná hodnota](../2-rozhodovani/ocekavana-hodnota.md): kolik to přinese, když započítáme šanci na neúspěch
- [Real options](../6-ekonomika/real-options.md): začni pilotem, pak rozšiř, nebo ukonči

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Rozhodovací stromy.

Rozhoduji se [o čem]. Nakresli rozhodovací strom (kroky, co se může stát, co pak), zeptej se mě na šance a přínosy ve větvích a spočítej, která cesta má nejvyšší očekávanou hodnotu.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda rozhodovaci-stromy
```
