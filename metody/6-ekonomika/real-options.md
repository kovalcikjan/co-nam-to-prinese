# Real options

**Oblast 6 · Ekonomika a byznys** · otázka oblasti: *Kdy se nám to vrátí?*

## Jednou větou

**Začni pilotem, pak rozšiř, nebo ukonči.** Hodnotu má i možnost rozhodnout se později. Malý pilot ti koupí právo projekt rozšířit, když vyjde, nebo ho levně ukončit, když ne.

## Kdy použít

- Když jde projekt rozdělit na malý začátek a pozdější rozšíření.
- Když je nejistota velká, ale brzy se zmenší (po prvních datech).

## Kdy ne

- Když se musíš rozhodnout naráz a nejde to vrátit.

## Co potřebuješ

- Náklady pilotu a plné verze.
- Co se z pilotu dozvíš a jak to změní odhad.

## Postup s AI

1. Popiš AI projekt a možné etapy.
2. Nech porovnat dvě cesty: všechno hned, nebo pilot a pak rozhodnutí.
3. Nech spočítat očekávanou hodnotu obou cest, včetně možnosti po pilotu skončit.
4. Když má cesta s pilotem vyšší hodnotu, začni pilotem a předem si urči, podle čeho rozšíříš.

## Příklad z marketingu

Místo 30 stránek o půjčkách napíšeš nejdřív tři. Když se do tří měsíců dostanou do top 20, dopíšeš zbytek. Když ne, ušetřil jsi 27 stránek práce a víš proč.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Pilot musí být opravdu informativní. Malý vzorek může mást.
- Kritéria pro rozšíření stanov předem.

## Související metody

- [Hodnota informace (Value of Information)](../2-rozhodovani/hodnota-informace.md): kdy se vyplatí nejdřív levně ověřit
- [Rozhodovací stromy](../2-rozhodovani/rozhodovaci-stromy.md): navazující kroky: nejdřív test, pak rozhodnutí
- [Diskontované cash flow a NPV](../6-ekonomika/npv.md): koruna za rok má menší cenu než dnes

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Real options.

Zvažuji [projekt]. Můžu začít malým pilotem za [náklady] a pak rozšířit za [náklady]. Porovnej očekávanou hodnotu cesty „všechno hned“ a „pilot, pak rozhodnutí“ a navrhni kritéria, podle kterých po pilotu rozšířím, nebo skončím.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda real-options
```
