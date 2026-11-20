# Časové řady

**Oblast 3 · Měření skutečného dopadu** · otázka oblasti: *Kolik z toho je naše zásluha?*

## Jednou větou

**Trend, sezónnost a mimořádné události.** Rozložíš data v čase na dlouhodobý trend, pravidelné výkyvy během roku a jednorázové události. Teprve pak vidíš, co je opravdu nové.

## Kdy použít

- Když potřebuješ vědět, co je sezóna a co skutečná změna.
- Před každým srovnáním před a po.

## Kdy ne

- Když máš data kratší než jeden celý cyklus (u roční sezóny aspoň rok).

## Co potřebuješ

- Data v čase, ideálně týdenní nebo denní, aspoň rok nebo dva.
- Seznam známých událostí (kampaně, updaty, výpadky).

## Postup s AI

1. Dej AI export dat v čase.
2. Nech je rozložit na trend, sezónnost a zbytek.
3. Nech označit neobvyklé výkyvy a porovnej je se seznamem událostí.
4. Teprve zbytek po odečtení trendu a sezóny ukazuje, co je opravdu nové.

## Příklad z marketingu

Návštěvnost blogu v lednu spadla o 20 %. Rozklad ukáže, že stejný pokles je každý leden. Žádný problém, jen sezóna.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Svátky se každý rok posouvají (Velikonoce). Řekni to AI.
- Jednorázová událost v datech zkreslí sezónnost, pokud ji neoznačíš.

## Související metody

- [Prediktivní modely](../4-predikce/prediktivni-modely.md): kolik poptávky a tržeb přijde samo
- [Detekce anomálií](../4-predikce/detekce-anomalii.md): problém uvidíš dřív než klient
- [CausalImpact](../3-mereni-dopadu/causalimpact.md): když kontrolní skupina chybí, model ji poskládá z jiných řad

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Časové řady.

Tady jsou moje data v čase: [export]. Rozlož je na trend, sezónnost a zbytek, označ neobvyklé výkyvy a řekni, co je skutečná změna a co jen sezóna.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda casove-rady
```
