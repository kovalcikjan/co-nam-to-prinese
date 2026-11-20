# Doba návratnosti (payback)

**Oblast 6 · Ekonomika a byznys** · otázka oblasti: *Kdy se nám to vrátí?*  
**Krok v kruhu:** 2 Rozhodni (`/rozhodni`)  
**Ukázka z přednášky:** [Tři projekty: návratnost a riziko](../../priklady/tri-projekty/)

## Jednou větou

**Kdy se nám to vrátí.** Za kolik měsíců přínos pokryje náklady. Pro klienta nejsrozumitelnější odpověď a se simulací ji dáš jako rozpětí, ne jedno datum.

## Kdy použít

- Když klient nebo šéf chce slyšet, kdy se to vrátí.
- Když porovnáváš projekty s různým náběhem.

## Kdy ne

- Jako jediné kritérium. Rychlá návratnost neznamená nejvyšší přínos.

## Co potřebuješ

- Náklady (peníze, nebo hodiny × sazba).
- Měsíční přínos po rozjezdu a jak dlouho trvá náběh, obojí jako rozpětí.

## Postup s AI

1. Dej AI náklady, přínos a náběh v rozpětí.
2. Nech nasimulovat kumulovaný přínos minus náklady po měsících.
3. Nech spočítat, ve kterém měsíci se to nejspíš vrátí a s jakou šancí se to do roka nevrátí.
4. Komunikuj rozpětí: „nejspíš za šest měsíců, s šancí 15 %, že se do roka nevrátí“.

## Příklad z marketingu

Kalkulačka se nejspíš vrátí za šest měsíců a do roka se nevrátí jen v 15 % scénářů. Stránka „půjčka na auto“ má vyšší očekávaný přínos, ale v 60 % scénářů se do roka nevrátí.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Návratnost nevidí, co přijde po ní. Doplň ji očekávanou hodnotou.
- U SEO je náběh dlouhý a nejistý. Dej ho jako rozpětí.

## Související metody

- [Monte Carlo simulace](../1-nejistota/monte-carlo.md): spojí rozpětí jednotlivých kroků do tisíců scénářů
- [Diskontované cash flow a NPV](../6-ekonomika/npv.md): koruna za rok má menší cenu než dnes
- [Portfolio optimalizace](../5-optimalizace/portfolio.md): mix jistých malých výher a velkých sázek

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Doba návratnosti (payback).

Projekt [jaký] stojí [náklady]. Po rozjezdu přinese měsíčně [rozpětí] a náběh trvá [rozpětí měsíců]. Nasimuluj kumulovaný přínos minus náklady po měsících a řekni, kdy se to nejspíš vrátí a s jakou šancí se to do roka nevrátí.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda doba-navratnosti
```
