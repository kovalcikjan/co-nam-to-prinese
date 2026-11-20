# Customer Lifetime Value (CLV) a CAC

**Oblast 6 · Ekonomika a byznys** · otázka oblasti: *Kdy se nám to vrátí?*

## Jednou větou

**Hodnota zákazníka a náklady na jeho získání.** CLV je, kolik ti zákazník přinese za celou dobu, CAC je, kolik stojí ho získat. Když je CAC vyšší než CLV, každý nový zákazník tě stojí peníze.

## Kdy použít

- Když rozhoduješ, kolik můžeš zaplatit za nového zákazníka.
- Když porovnáváš kanály, které přivádějí různě hodnotné zákazníky.

## Kdy ne

- U jednorázových nákupů bez opakování. Tam stačí marže z jedné objednávky.

## Co potřebuješ

- Marži na objednávku, jak často zákazníci nakupují a jak dlouho zůstávají.
- Náklady na získání: výdaje kanálu a počet nových zákazníků z něj.

## Postup s AI

1. Dej AI data o objednávkách a nákladech kanálů.
2. Nech spočítat CLV (marže za celou dobu vztahu) a CAC po kanálech, jako rozpětí.
3. Nech porovnat CLV a CAC u každého kanálu.
4. Kanály, kde CAC převyšuje CLV, uprav nebo omez.

## Příklad z marketingu

Zákazník z newsletteru nakupuje třikrát ročně, zákazník ze slevového portálu jednou. Při stejném CAC je newsletter mnohem výhodnější, i když první objednávka vypadá stejně.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Počítej s marží, ne s tržbou.
- U nových firem je délka vztahu odhad. Dej ji jako rozpětí.

## Související metody

- [Marginální analýza](../6-ekonomika/marginalni-analyza.md): kolik přinese další koruna
- [Diskontované cash flow a NPV](../6-ekonomika/npv.md): koruna za rok má menší cenu než dnes
- [Doba návratnosti (payback)](../6-ekonomika/doba-navratnosti.md): kdy se nám to vrátí

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Customer Lifetime Value (CLV) a CAC.

Tady jsou data o objednávkách zákazníků a nákladech kanálů: [data]. Spočítej CLV (z marže) a CAC po kanálech jako rozpětí, porovnej je a řekni, které kanály se vyplácejí a které ne.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda clv-a-cac
```
