# Clustering

**Oblast 4 · Predikce a strojové učení** · otázka oblasti: *Co nás nejspíš čeká?*

## Jednou větou

**Skupiny klíčových slov, zákazníků a příležitostí.** Algoritmus sám najde skupiny podobných věcí, aniž bys je předem určoval. Třeba témata klíčových slov nebo typy zákazníků podle chování.

## Kdy použít

- Když máš stovky klíčových slov, zákazníků nebo produktů a chceš v nich najít skupiny.
- Na začátku obsahové strategie nebo segmentace.

## Kdy ne

- Když skupiny už znáš a jen do nich řadíš. Pak je to klasifikace.

## Co potřebuješ

- Seznam položek s vlastnostmi (klíčová slova s hledaností, zákazníci s chováním).

## Postup s AI

1. Dej AI seznam položek.
2. Nech je seskupit (podle významu slov, podle chování zákazníků).
3. Nech každou skupinu pojmenovat a popsat jednou větou.
4. Zkontroluj, jestli skupiny dávají smysl, a uprav jejich počet.

## Příklad z marketingu

Dva tisíce klíčových slov o půjčkách se rozpadnou do skupin jako „půjčka na auto“, „půjčka na bydlení“ nebo „refinancování“. Každá skupina je kandidát na jednu stránku.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Algoritmus vždy nějaké skupiny najde, i když v datech nejsou. Kontroluj je selským rozumem.
- Počet skupin volíš ty. Zkus víc variant.

## Související metody

- [Klasifikace](../4-predikce/klasifikace.md): šance na úspěch, třeba který článek se dostane do top 10
- [Síťová analýza](../7-systemy/sitova-analyza.md): souvislosti témat, stránek a entit
- [Prediktivní modely](../4-predikce/prediktivni-modely.md): kolik poptávky a tržeb přijde samo

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Clustering.

Tady je seznam [klíčových slov nebo zákazníků] s vlastnostmi: [data]. Seskup je do smysluplných skupin, každou pojmenuj a popiš jednou větou a navrhni, co s každou skupinou dělat.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda clustering
```
