# Odhad podle referenční třídy (base rate)

**Oblast 1 · Pravděpodobnost a nejistota** · otázka oblasti: *Jaké výsledky jsou možné?*  
**Krok v kruhu:** 1 Odhadni rozpětí (`/odhadni`)

## Jednou větou

**Začni tím, jak obvykle dopadly podobné projekty.** Než začneš odhadovat, podívej se, jak dopadly podobné věci, třeba tvých posledních pět stránek. Když se do top 10 dostaly dvě, začínáš na šanci 40 %, ne na pocitu.

## Kdy použít

- Než odhadneš přínos nového článku, kampaně nebo stránky.
- Když tým odhaduje z pocitu a každý říká jiné číslo.

## Kdy ne

- Když děláš něco opravdu poprvé a nemáš s čím srovnat. I pak pomůže obecná zkušenost: v Microsoftu zlepšila metriku, kterou zlepšit měla, jen třetina testovaných nápadů (Kohavi a kol., 2012).

## Co potřebuješ

- Seznam 5 až 20 podobných věcí, které už proběhly (články, kampaně, landing pages).
- U každé, jak dopadla: dostala se do top 10, kolik přinesla, za jak dlouho.

## Postup s AI

1. Popiš AI, co chceš odhadnout, a nech ji navrhnout, co je podobná věc.
2. Dej jí výsledky podobných věcí (tabulku nebo export).
3. Nech spočítat, jak často se to podařilo a jaké bylo obvyklé rozpětí.
4. Teprve potom uprav odhad podle toho, čím je tvůj případ jiný.

## Příklad z marketingu

Chceš napsat novou srovnávací stránku. Z tvých posledních pěti podobných stránek se do top 10 dostaly dvě. Výchozí šance je tedy 40 %, ne „určitě se tam dostaneme“.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Vyber opravdu podobné věci. Stránka na silné doméně se nesrovnává se stránkou na novém webu.
- Malý vzorek (třeba pět) dává jen hrubý odhad. Ber ho jako start, ne jako pravdu.

## Související metody

- [Pravděpodobnostní rozdělení](../1-nejistota/pravdepodobnostni-rozdeleni.md): rozpětí možných výsledků místo jednoho čísla
- [Kalibrace odhadů](../1-nejistota/kalibrace-odhadu.md): aby rozpětí „na 90 %“ opravdu sedělo devětkrát z deseti
- [Bayesovská statistika](../1-nejistota/bayesovska-statistika.md): zpřesní odhad, když přijdou nová data

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Odhad podle referenční třídy (base rate).

Chci odhadnout [co]. Pomoz mi najít skupinu podobných věcí, které už proběhly, a z jejich výsledků spočítej výchozí šanci a obvyklé rozpětí.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda referencni-trida
```
