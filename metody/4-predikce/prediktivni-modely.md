# Prediktivní modely

**Oblast 4 · Predikce a strojové učení** · otázka oblasti: *Co nás nejspíš čeká?*  
**Krok v kruhu:** 1 Odhadni rozpětí (`/odhadni`)

## Jednou větou

**Kolik poptávky a tržeb přijde samo.** Model se z minulých dat naučí, kolik poptávky a tržeb obvykle přichází. Dostaneš výchozí čáru, od které se počítá přínos tvé práce.

## Kdy použít

- Když potřebuješ výchozí čáru: kolik přijde samo, bez tvé práce.
- Při plánování rozpočtu, kapacit a cílů.

## Kdy ne

- Když se trh právě zásadně mění a minulost neplatí.
- Když chceš dokázat příčinu. Predikce ukáže, co přijde, ne proč.

## Co potřebuješ

- Historická data (návštěvy, poptávky, tržby), ideálně aspoň dva roky.
- Co je ovlivňuje (sezóna, cena, kampaně), pokud to víš.

## Postup s AI

1. Dej AI historická data.
2. Nech ji postavit jednoduchý model s trendem a sezónností a předpověď s rozpětím.
3. Nech model otestovat na posledních měsících, které neviděl.
4. Předpověď použij jako výchozí čáru, od které měříš přínos své práce.

## Příklad z marketingu

Model ukáže, že bez nové práce přijde v březnu 8 až 10 tisíc návštěv. Když jich přijde 12 tisíc, přínos tvé práce je rozdíl proti této čáře, ne proti únoru.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Předpověď bez rozpětí je zase jen číslo z hlavy, jen z počítače.
- Čím dál do budoucnosti, tím širší rozpětí.

## Související metody

- [Časové řady](../3-mereni-dopadu/casove-rady.md): trend, sezónnost a mimořádné události
- [Detekce anomálií](../4-predikce/detekce-anomalii.md): problém uvidíš dřív než klient
- [Klasifikace](../4-predikce/klasifikace.md): šance na úspěch, třeba který článek se dostane do top 10

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Prediktivní modely.

Tady jsou moje historická data: [data]. Postav jednoduchý model s trendem a sezónností, předpověz další [počet] měsíců jako rozpětí a otestuj ho na posledních měsících, které model neviděl.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda prediktivni-modely
```
