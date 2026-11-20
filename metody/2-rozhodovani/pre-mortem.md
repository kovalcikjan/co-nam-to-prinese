# Pre-mortem

**Oblast 2 · Rozhodování a prioritizace** · otázka oblasti: *Co udělat jako první?*  
**Krok v kruhu:** 3 Hledej, co ti uniklo (`/proverit`)

## Jednou větou

**Představ si, že projekt selhal, a zeptej se proč.** Představ si, že je rok po spuštění a projekt nevyšel. Sepiš všechny důvody proč. S AI to zabere pět minut a odhalí rizika, která jinak přehlédneš.

## Kdy použít

- Před každým větším projektem nebo kampaní.
- Když je tým nadšený a nikdo nechce mluvit o rizicích.

## Kdy ne

- Až po spuštění. Pak už je to rozbor, ne prevence.

## Co potřebuješ

- Popis projektu: cíl, plán, termín.
- Pět minut a ochotu představit si neúspěch.

## Postup s AI

1. Řekni AI: „Je rok po spuštění a projekt nevyšel. Proč?“
2. Nech vypsat deset důvodů a doplň vlastní.
3. Seřaďte je podle pravděpodobnosti a dopadu.
4. U tří nejhorších vymysli, jak jim předejít nebo je včas poznat.

## Příklad z marketingu

Nová srovnávací stránka nevyšla. Důvody: Google ji neindexoval, partner zrušil affiliate program, AI odpovědi ve vyhledávači snížily prokliky, stránka brala návštěvy jiné stránce na webu. Dva z nich jde hlídat hned od začátku.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- AI vymyslí obecná rizika. Nech ji ptát se na tvůj konkrétní případ.
- Cílem není projekt zabít, ale najít, co hlídat.

## Související metody

- [Kauzální grafy (DAG)](../7-systemy/kauzalni-grafy.md): nakresli, co co ovlivňuje, než začneš měřit
- [Analýza citlivosti](../1-nejistota/analyza-citlivosti.md): který předpoklad nejvíc hýbe výsledkem
- [Vícekriteriální rozhodování](../2-rozhodovani/vicekriterialni-rozhodovani.md): když nejde jen o peníze

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Pre-mortem.

Plánuji [projekt]. Představ si, že je rok po spuštění a projekt nevyšel. Vypiš deset nejpravděpodobnějších důvodů pro můj konkrétní případ, seřaď je podle pravděpodobnosti a dopadu a ke třem nejhorším navrhni, jak jim předejít nebo je včas poznat.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Drž se mého konkrétního případu, ne obecných rad. Na konci jednou větou napiš, co z toho plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda pre-mortem
```
