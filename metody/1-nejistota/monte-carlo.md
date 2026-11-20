# Monte Carlo simulace

**Oblast 1 · Pravděpodobnost a nejistota** · otázka oblasti: *Jaké výsledky jsou možné?*  
**Krok v kruhu:** 1 Odhadni rozpětí (`/odhadni`)  
**Ukázka z přednášky:** [Půjčka na auto: Monte Carlo](../../priklady/pujcka-na-auto/)

## Jednou větou

**Spojí rozpětí jednotlivých kroků do tisíců scénářů.** Počítač tisíckrát náhodně vybere hodnotu z každého rozpětí a pokaždé spočítá výsledek. Z tisíců výsledků vidíš, co je pravděpodobné a co jen možné.

## Kdy použít

- Když výsledek závisí na několika krocích za sebou a každý je nejistý (návštěvy, konverze, objednávka).
- Když chceš vědět nejen průměr, ale i šanci, že se projekt nevrátí.

## Kdy ne

- Když máš jediné neznámé číslo. Tam stačí rozdělení.
- Když nemáš o vstupech ani hrubou představu. Simulace z vymyšlených čísel dá vymyšlený výsledek.

## Co potřebuješ

- Rozklad výsledku na kroky, které se násobí nebo sčítají.
- Ke každému kroku rozpětí: nejméně, nejčastěji, nejvíc.
- Náklady, pokud chceš vědět, jestli se to vrátí.

## Postup s AI

1. Popiš AI, co chceš spočítat, a nech ji navrhnout kroky.
2. Ke každému kroku dodej rozpětí a referenční třídu (jak dopadly podobné věci).
3. Nech AI napsat krátký program, který spočítá 10 000 scénářů, a spustit ho.
4. Chtěj výsledek jako rozpětí (10., 50. a 90. percentil), průměr a šanci, že nepokryje náklady.
5. Nech si ukázat graf rozdělení a zeptej se, co nejvíc hýbe výsledkem (analýza citlivosti).

## Příklad z marketingu

Stránka „půjčka na auto“: hledanost × šance na top 10 × CTR × proklik × schválení × provize. Z hlavy 80 tisíc ročně. Simulace ukázala, že polovina scénářů skončí pod 10 tisíci a v 59 % scénářů se náklady do roka nevrátí.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Výsledek je jen tak dobrý jako rozpětí na vstupu.
- Počítat má program, ne chat. Jazykový model v textu počítá nespolehlivě.
- Když jsou kroky na sobě závislé (vyšší pozice zvedne CTR i proklik), řekni to AI. Jinak simulace rozptyl podcení.

## Související metody

- [Pravděpodobnostní rozdělení](../1-nejistota/pravdepodobnostni-rozdeleni.md): rozpětí možných výsledků místo jednoho čísla
- [Analýza citlivosti](../1-nejistota/analyza-citlivosti.md): který předpoklad nejvíc hýbe výsledkem
- [Doba návratnosti (payback)](../6-ekonomika/doba-navratnosti.md): kdy se nám to vrátí

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Monte Carlo simulace.

Chci odhadnout [co]. Rozlož výsledek na kroky, ke každému se mě zeptej na rozpětí (nejméně, nejčastěji, nejvíc) a napiš program, který spočítá 10 000 scénářů. Ukaž 10., 50. a 90. percentil, průměr a šanci, že výsledek nepokryje náklady [částka].

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda monte-carlo
```
