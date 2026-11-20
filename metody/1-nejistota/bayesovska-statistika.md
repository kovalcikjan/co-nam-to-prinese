# Bayesovská statistika

**Oblast 1 · Pravděpodobnost a nejistota** · otázka oblasti: *Jaké výsledky jsou možné?*  
**Krok v kruhu:** 4 Změř a zpřesni (`/zmer`)

## Jednou větou

**Zpřesní odhad, když přijdou nová data.** Začneš s tím, co víš dnes, a každá nová data odhad posunou. Po měsíci máš přesnější číslo a nezačínáš od nuly.

## Kdy použít

- Když máš výchozí odhad a postupně přicházejí data (týdny kampaně, první měsíce stránky).
- Když chceš místo „průkazné ano, nebo ne“ slyšet, s jakou pravděpodobností.

## Kdy ne

- Když máš obrovské množství dat. Tam vyjde podobně jako klasická statistika.

## Co potřebuješ

- Výchozí odhad (třeba z referenční třídy) a jak moc sis jím jistý.
- Nová data: kolik pokusů a kolik úspěchů, nebo naměřené hodnoty.

## Postup s AI

1. Řekni AI, jaký byl tvůj výchozí odhad a jak moc sis jím byl jistý.
2. Dej jí nová data.
3. Nech spočítat aktualizovaný odhad jako rozpětí a ukázat, jak se posunul.
4. Opakuj s každými dalšími daty. Nový odhad je výchozí pro příště.

## Příklad z marketingu

Čekal jsi, že se do top 10 dostanou 2 z 5 stránek. Další stránka se tam dostala, takže máš 3 z 6. Odhad šance pro příští stránku se posune nahoru, ale opatrně, protože vzorek je pořád malý.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Výchozí odhad ovlivní výsledek hlavně u malých dat. Napiš ho poctivě a předem, ne až podle výsledku.
- Pravděpodobnost 90 % není jistota. Jednou z deseti to dopadne jinak.

## Související metody

- [Odhad podle referenční třídy (base rate)](../1-nejistota/referencni-trida.md): začni tím, jak obvykle dopadly podobné projekty
- [Experimenty a Bayesovské testování](../3-mereni-dopadu/bayesovske-testovani.md): náhodné rozdělení; pravděpodobnost místo ano, nebo ne
- [Kalibrace odhadů](../1-nejistota/kalibrace-odhadu.md): aby rozpětí „na 90 %“ opravdu sedělo devětkrát z deseti

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Bayesovská statistika.

Můj výchozí odhad byl [co, s jakou jistotou]. Teď mám nová data: [data]. Spočítej bayesovsky aktualizovaný odhad jako rozpětí a vysvětli, jak a proč se posunul.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda bayesovska-statistika
```
