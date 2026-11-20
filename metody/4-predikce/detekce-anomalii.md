# Detekce anomálií

**Oblast 4 · Predikce a strojové učení** · otázka oblasti: *Co nás nejspíš čeká?*

## Jednou větou

**Problém uvidíš dřív než klient.** Hlídá data a upozorní, když se něco chová jinak než obvykle, třeba náhlý pokles návštěv. Problém řešíš dřív, než si ho všimne klient.

## Kdy použít

- Když hlídáš víc webů, kampaní nebo metrik a nestíháš je kontrolovat ručně.
- Když chceš poznat problém (výpadek měření, pokles pozic) dřív než klient.

## Kdy ne

- Když data skáčou tak, že běžné výkyvy jsou větší než problémy, které hledáš.

## Co potřebuješ

- Pravidelný export metrik (denně nebo týdně).
- Historii, ze které je vidět, co je normální.

## Postup s AI

1. Dej AI historii metriky.
2. Nech určit normální rozpětí pro každý den nebo týden, i se sezónou.
3. Nech označit hodnoty mimo rozpětí.
4. Pro pravidelné hlídání nech napsat skript, který to dělá automaticky.

## Příklad z marketingu

Skript každé ráno porovná včerejší konverze s obvyklým rozpětím pro daný den v týdnu. Když spadnou pod něj, pošle upozornění. Rozbitý měřicí kód tak najdeš druhý den, ne na konci měsíce.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Moc citlivé hlídání otravuje falešnými poplachy a lidé ho přestanou číst.
- Anomálie není vysvětlení. Příčinu musíš najít sám.

## Související metody

- [Časové řady](../3-mereni-dopadu/casove-rady.md): trend, sezónnost a mimořádné události
- [Prediktivní modely](../4-predikce/prediktivni-modely.md): kolik poptávky a tržeb přijde samo
- [Korelace versus kauzalita](../3-mereni-dopadu/korelace-vs-kauzalita.md): růst po kampani není automaticky jejím důsledkem

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Detekce anomálií.

Tady je historie metriky [jaké]: [data]. Urči normální rozpětí pro každý den (i se sezónou), označ hodnoty mimo něj a napiš skript, který to bude kontrolovat pravidelně.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda detekce-anomalii
```
