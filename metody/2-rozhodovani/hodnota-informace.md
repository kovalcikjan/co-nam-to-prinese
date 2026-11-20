# Hodnota informace (Value of Information)

**Oblast 2 · Rozhodování a prioritizace** · otázka oblasti: *Co udělat jako první?*  
**Krok v kruhu:** 2 Rozhodni (`/rozhodni`)

## Jednou větou

**Kdy se vyplatí nejdřív levně ověřit.** Kolik by stálo za to znát odpověď dřív, než se rozhodneš. Když je test levnější než možná chyba, nejdřív testuj.

## Kdy použít

- Když nevíš klíčový předpoklad a rozhodnutí je drahé.
- Po analýze citlivosti: víš, co nejvíc hýbe výsledkem, a ptáš se, jestli to nejdřív ověřit.

## Kdy ne

- Když je rozhodnutí levné a vratné. Pak je rychlejší to zkusit.

## Co potřebuješ

- Rozhodnutí a jeho možné výsledky.
- Nejistý předpoklad, který chceš ověřit, a kolik by test stál.

## Postup s AI

1. Řekni AI, o čem rozhoduješ a který předpoklad je nejistý.
2. Nech spočítat očekávaný výsledek, když se rozhodneš hned, a když budeš předpoklad znát.
3. Rozdíl je hodnota informace. Porovnej ji s cenou testu.
4. Když je test levnější, nejdřív testuj.

## Příklad z marketingu

Stránka „půjčka na auto“ přinese buď skoro nic, nebo hodně, podle toho, jestli se dostane do top 10. Menší testovací článek za tři hodiny ukáže, jestli máš na pozici šanci. To je levné proti 25 hodinám práce na celé stránce.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Test nemusí dát úplnou odpověď. Počítej s tím, že informace bude jen částečná.
- Hodnota informace je nejvyšší u nejistých a drahých rozhodnutí. U jistých se testovat nevyplatí.

## Související metody

- [Analýza citlivosti](../1-nejistota/analyza-citlivosti.md): který předpoklad nejvíc hýbe výsledkem
- [Rozhodovací stromy](../2-rozhodovani/rozhodovaci-stromy.md): navazující kroky: nejdřív test, pak rozhodnutí
- [Real options](../6-ekonomika/real-options.md): začni pilotem, pak rozšiř, nebo ukonči

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Hodnota informace (Value of Information).

Rozhoduji se [o čem]. Nejistý je hlavně předpoklad [jaký]. Spočítej, kolik by stálo za to ho znát dřív, než se rozhodnu, a porovnej to s cenou testu [částka nebo hodiny].

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda hodnota-informace
```
