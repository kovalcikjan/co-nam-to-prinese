# Marketing Mix Modeling (MMM)

**Oblast 5 · Optimalizace zdrojů** · otázka oblasti: *Jak rozdělit čas a peníze?*

## Jednou větou

**Kam dát další korunu mezi kanály.** Model z historie výdajů a prodejů odhadne, kolik přinesl který kanál a kde už další koruna skoro nic nepřidá. Obejde se bez cookies.

## Kdy použít

- Když rozděluješ rozpočet mezi víc kanálů (PPC, sociální sítě, TV, rádio, e-mail).
- Když nemůžeš sledovat jednotlivé lidi (cookies, offline kanály).

## Kdy ne

- Když máš krátkou historii nebo skoro neměnné výdaje. Model pak nemá z čeho se učit.

## Co potřebuješ

- Týdenní výdaje na každý kanál a prodeje, obvykle za dlouhé období (třeba dva roky).
- Další vlivy: sezóna, ceny, akce, konkurence.

## Postup s AI

1. Dej AI týdenní data výdajů a prodejů.
2. Nech postavit model, který odhadne přínos každého kanálu a jak klesá s dalšími penězi.
3. Nech spočítat, kam přesunout rozpočet, aby přinesl víc.
4. Doporučení ověř testem (třeba na části regionů), než přesuneš všechno.

## Příklad z marketingu

Model ukáže, že PPC na značku je nasycené a další koruna přinese málo, zatímco video ještě roste. Přesunem části rozpočtu z PPC do videa by se při stejných nákladech mohly zvednout prodeje.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Výsledky modelu jsou citlivé na předpoklady. Ověřuj je experimenty.
- Je to pokročilá metoda. Pro malé rozpočty stačí marginální analýza po kanálech.

## Související metody

- [Marginální analýza](../6-ekonomika/marginalni-analyza.md): kolik přinese další koruna
- [Holdout testy (inkrementalita)](../3-mereni-dopadu/holdout-testy.md): část lidí kampaň neuvidí, rozdíl je přínos kampaně
- [Časové řady](../3-mereni-dopadu/casove-rady.md): trend, sezónnost a mimořádné události

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Marketing Mix Modeling (MMM).

Tady jsou týdenní výdaje po kanálech a prodeje za [období]: [data]. Postav jednoduchý model marketingového mixu, odhadni přínos každého kanálu a jak klesá s dalšími penězi a doporuč, jak přesunout rozpočet. Řekni, co by šlo ověřit testem.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda marketing-mix-modeling
```
