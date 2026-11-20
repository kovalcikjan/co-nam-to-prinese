# Robustní optimalizace

**Oblast 5 · Optimalizace zdrojů** · otázka oblasti: *Jak rozdělit čas a peníze?*

## Jednou větou

**Plán, který vydrží chybu v odhadech.** Nehledá plán nejlepší pro jeden odhad, ale takový, který dopadne dobře, i když se v odhadech spleteš.

## Kdy použít

- Když si nejsi jistý vstupy a špatné rozhodnutí by bolelo.
- Když nejlepší plán na papíře stojí na jednom optimistickém předpokladu.

## Kdy ne

- Když jsou vstupy dobře známé.

## Co potřebuješ

- Možné plány a scénáře vstupů (nebo simulaci).

## Postup s AI

1. Dej AI plány a scénáře nebo rozpětí vstupů.
2. Nech spočítat, jak každý plán dopadne v každém scénáři.
3. Vyber plán, který dopadne dobře i v horších scénářích (třeba podle 10. percentilu), ne jen v průměru.
4. Porovnej, kolik průměrného přínosu za tu jistotu platíš.

## Příklad z marketingu

Plán A má nejvyšší průměr, ale v pětině scénářů skončí v minusu. Plán B má průměr o 10 % nižší, ale do minusu skoro nikdy nespadne. Když si ztrátu nemůžeš dovolit, vybereš B.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Přílišná opatrnost taky stojí peníze. Hledej rovnováhu.
- Scénáře musí zahrnout i ty nepříjemné.

## Související metody

- [Portfolio optimalizace](../5-optimalizace/portfolio.md): mix jistých malých výher a velkých sázek
- [Monte Carlo simulace](../1-nejistota/monte-carlo.md): spojí rozpětí jednotlivých kroků do tisíců scénářů
- [Lineární a celočíselné programování](../5-optimalizace/linearni-programovani.md): co se vejde do hodin nebo rozpočtu

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Robustní optimalizace.

Mám tyto plány: [plány] a nejisté vstupy v rozpětí: [vstupy]. Spočítej, jak každý plán dopadne v tisících scénářů, a doporuč plán, který dopadne dobře i v horších scénářích. Řekni, kolik průměrného přínosu za to platím.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda robustni-optimalizace
```
