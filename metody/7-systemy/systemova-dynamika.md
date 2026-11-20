# Systémová dynamika

**Oblast 7 · Modelování systémů** · otázka oblasti: *Co tím ovlivníme jinde?*

## Jednou větou

**Zpětné vazby v čase.** Modeluje smyčky, které se samy posilují nebo brzdí: víc obsahu, víc odkazů, vyšší autorita, víc návštěv. Nebo časté slevy naučí lidi čekat na další slevu.

## Kdy použít

- Když výsledek závisí na smyčkách, které se v čase posilují nebo brzdí.
- Když krátkodobé zlepšení může dlouhodobě škodit (slevy, agresivní reklama).

## Kdy ne

- Když jde o jednorázový efekt bez zpětné vazby.

## Co potřebuješ

- Popis hlavních veličin (zákazníci, obsah, autorita, rozpočet) a jak se navzájem ovlivňují.
- Hrubé odhady rychlostí (kolik zákazníků měsíčně přijde a odejde).

## Postup s AI

1. Popiš AI systém a nech nakreslit smyčky: co co posiluje a co brzdí.
2. Doplň hrubé odhady rychlostí.
3. Nech napsat jednoduchou simulaci na jeden až tři roky.
4. Porovnej strategie: co udělá krátkodobá akce za rok.

## Příklad z marketingu

Časté slevy zvednou prodeje v měsíci akce, ale naučí zákazníky čekat. Simulace na dva roky ukáže, jestli průměrná marže klesá a mimo akce se prodává míň.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Model je zjednodušení. Používej ho na porovnání strategií, ne na přesná čísla.
- Rychlosti a zpoždění dej jako rozpětí.

## Související metody

- [Kauzální grafy (DAG)](../7-systemy/kauzalni-grafy.md): nakresli, co co ovlivňuje, než začneš měřit
- [Agentní modelování (agent-based modeling)](../7-systemy/agentni-modelovani.md): simulace mnoha zákazníků najednou
- [Prediktivní modely](../4-predikce/prediktivni-modely.md): kolik poptávky a tržeb přijde samo

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Systémová dynamika.

Tady jsou hlavní veličiny a vazby v mém systému: [popis]. Nakresli, co co posiluje a brzdí, zeptej se mě na hrubé rychlosti a nasimuluj vývoj na [období] pro strategie [A] a [B].

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda systemova-dynamika
```
