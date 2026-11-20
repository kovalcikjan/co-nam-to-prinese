# Multi-armed bandit

**Oblast 5 · Optimalizace zdrojů** · otázka oblasti: *Jak rozdělit čas a peníze?*

## Jednou větou

**Testuje a zároveň vydělává.** Na rozdíl od klasického testu posílá už během testu víc lidí k variantě, která zatím vede. Méně návštěv propálíš na horší variantě.

## Kdy použít

- Když testuješ víc variant (titulky, kreativy, nabídky) a nechceš ztrácet peníze na horších.
- U krátkých akcí, kde není čas na dlouhý test.

## Kdy ne

- Když potřebuješ přesně změřit rozdíl mezi variantami (třeba pro rozhodnutí na rok dopředu). Pak klasický test.

## Co potřebuješ

- Varianty a průběžné výsledky (zobrazení, kliky, konverze).

## Postup s AI

1. Popiš AI varianty a cíl.
2. Nech navrhnout pravidlo, jak průběžně posílat víc lidí k vedoucí variantě (třeba Thompsonův výběr).
3. Nech nasimulovat, kolik konverzí tím ušetříš proti rovnoměrnému testu.
4. Nastav to v nástroji, který to umí, nebo nech AI napsat skript.

## Příklad z marketingu

Ze čtyř předmětů e-mailu po prvních tisících odeslání jeden vede. Bandit mu posílá stále větší díl a horší předměty dostanou jen tolik, aby se ověřilo, že opravdu zaostávají.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Bandit rychleji vydělává, ale hůř měří. Na otázku „o kolik je lepší“ odpoví méně přesně.
- Když se chování lidí v čase mění (víkend, sezóna), musí s tím pravidlo počítat.

## Související metody

- [Experimenty a Bayesovské testování](../3-mereni-dopadu/bayesovske-testovani.md): náhodné rozdělení; pravděpodobnost místo ano, nebo ne
- [Holdout testy (inkrementalita)](../3-mereni-dopadu/holdout-testy.md): část lidí kampaň neuvidí, rozdíl je přínos kampaně
- [Portfolio optimalizace](../5-optimalizace/portfolio.md): mix jistých malých výher a velkých sázek

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Multi-armed bandit.

Testuji tyto varianty: [varianty] s cílem [cíl]. Navrhni pravidlo, které bude průběžně posílat víc lidí k vedoucí variantě, a nasimuluj, kolik konverzí tím ušetřím proti rovnoměrnému testu.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda multi-armed-bandit
```
