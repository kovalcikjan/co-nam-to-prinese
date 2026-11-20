# Opportunity cost

**Oblast 6 · Ekonomika a byznys** · otázka oblasti: *Kdy se nám to vrátí?*

## Jednou větou

**Co neuděláme, když uděláme tohle.** Každá hodina na jednom projektu chybí jinde. Skutečná cena projektu je i přínos nejlepší alternativy, kterou kvůli němu neuděláš.

## Kdy použít

- Když hodnotíš projekt samotný a vychází dobře.
- Když máš omezenou kapacitu týmu.

## Kdy ne

- Když kapacita není omezená a projekty si nekonkurují.

## Co potřebuješ

- Seznam alternativ, které by šly dělat místo toho.
- Jejich odhadovaný přínos (stačí hrubě).

## Postup s AI

1. Popiš AI projekt a jeho přínos.
2. Nech vypsat, co jiného by šlo za stejné hodiny nebo peníze udělat.
3. Odhadni přínos nejlepší alternativy.
4. Projekt se vyplatí, jen když porazí nejlepší alternativu, ne nulu.

## Příklad z marketingu

Redesign blogu přinese odhadem 20 tisíc. Za stejných 60 hodin by šlo napsat 10 článků s očekávaným přínosem 50 tisíc. Redesign tedy ve skutečnosti stojí 30 tisíc, i když sám o sobě vydělává.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Alternativy mají taky nejistotu. Porovnávej rozpětí, ne jen čísla.
- Nejlepší alternativa nemusí být vidět. Nech AI navrhnout i ty, na které nemyslíš.

## Související metody

- [Očekávaná hodnota](../2-rozhodovani/ocekavana-hodnota.md): kolik to přinese, když započítáme šanci na neúspěch
- [Lineární a celočíselné programování](../5-optimalizace/linearni-programovani.md): co se vejde do hodin nebo rozpočtu
- [Cost of Delay](../2-rozhodovani/cost-of-delay.md): co nás stojí každý týden odkladu; s pracností dává pořadí

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Opportunity cost.

Zvažuji [projekt] s přínosem [odhad] za [hodiny nebo peníze]. Vypiš, co jiného by šlo za stejné zdroje udělat, pomoz mi odhadnout přínos nejlepší alternativy a řekni, jestli ji projekt porazí.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda opportunity-cost
```
