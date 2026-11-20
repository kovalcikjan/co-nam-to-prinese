# Markovovy řetězce

**Oblast 7 · Modelování systémů** · otázka oblasti: *Co tím ovlivníme jinde?*

## Jednou větou

**Přechody zákazníků mezi stavy, třeba Markovova atribuce.** Popíšou, jak zákazník přechází mezi kroky, třeba z reklamy na web a do košíku. Markovova atribuce spočítá, kolik konverzí by zmizelo bez jednoho kanálu.

## Kdy použít

- Když chceš vědět, kolik který kanál přispívá ke konverzím, když lidé přicházejí víckrát různými cestami.
- Když modeluješ přechody zákazníků mezi stavy (nový, aktivní, spící, odešel).

## Kdy ne

- Když máš data jen o posledním kliknutí. Potřebuješ celé cesty.

## Co potřebuješ

- Cesty zákazníků: posloupnosti kanálů nebo stavů a jestli konvertovali.

## Postup s AI

1. Dej AI export cest (třeba z analytiky).
2. Nech spočítat pravděpodobnosti přechodů mezi kroky.
3. Pro atribuci nech spočítat, kolik konverzí by zmizelo, kdyby kanál chyběl.
4. Porovnej to s atribucí podle posledního kliknutí.

## Příklad z marketingu

Podle posledního kliknutí dělá všechno PPC na značku. Markovova atribuce ukáže, že bez obsahových článků by zmizela velká část konverzí, protože lidé značku poprvé poznali v nich.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Atribuce není experiment. Ukazuje podíl na cestách, ne jistý příčinný efekt.
- Data o cestách bývají neúplná (různá zařízení, odmítnuté cookies).

## Související metody

- [Kauzální grafy (DAG)](../7-systemy/kauzalni-grafy.md): nakresli, co co ovlivňuje, než začneš měřit
- [Holdout testy (inkrementalita)](../3-mereni-dopadu/holdout-testy.md): část lidí kampaň neuvidí, rozdíl je přínos kampaně
- [Síťová analýza](../7-systemy/sitova-analyza.md): souvislosti témat, stránek a entit

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Markovovy řetězce.

Tady je export cest zákazníků (posloupnosti kanálů a jestli konvertovali): [data]. Spočítej Markovovu atribuci, tedy kolik konverzí by zmizelo bez každého kanálu, a porovnej to s atribucí podle posledního kliknutí.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda markovovy-retezce
```
