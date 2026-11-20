# Survival analysis

**Oblast 4 · Predikce a strojové učení** · otázka oblasti: *Co nás nejspíš čeká?*

## Jednou větou

**Za jak dlouho se něco stane.** Odhaduje čas do události: za kolik měsíců se článek dostane do top 10 nebo kdy zákazník odejde. Počítá i s těmi, u kterých se to ještě nestalo.

## Kdy použít

- Když chceš vědět, za jak dlouho se něco stane: článek v top 10, odchod zákazníka, nákup leadu.
- Když se u části případů událost ještě nestala a nechceš je vyhodit.

## Kdy ne

- Když tě zajímá jen jestli, ne kdy.

## Co potřebuješ

- U každé položky datum začátku a datum události, nebo informaci, že zatím nenastala.

## Postup s AI

1. Dej AI tabulku s daty začátku a událostí.
2. Nech spočítat křivku přežití (Kaplanova-Meierova): jaký podíl ještě čeká po 1, 3 a 6 měsících.
3. Nech porovnat skupiny (třeba články na silná a slabá témata).
4. Výsledek použij jako náběh v odhadu návratnosti.

## Příklad z marketingu

Z minulých článků se polovina dostala do top 10 do čtyř měsíců, čtvrtina ani po roce. To je náběh, se kterým počítáš ve výpočtu návratnosti.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Nevyhazuj případy, u kterých se událost ještě nestala. Právě s nimi metoda umí pracovat.
- Malé skupiny dají jen hrubou křivku.

## Související metody

- [Doba návratnosti (payback)](../6-ekonomika/doba-navratnosti.md): kdy se nám to vrátí
- [Prediktivní modely](../4-predikce/prediktivni-modely.md): kolik poptávky a tržeb přijde samo
- [Klasifikace](../4-predikce/klasifikace.md): šance na úspěch, třeba který článek se dostane do top 10

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Survival analysis.

Tady je tabulka [článků nebo zákazníků] s datem začátku a datem události (nebo že zatím nenastala): [data]. Spočítej, za jak dlouho se událost obvykle stane, jako křivku s rozpětím, a porovnej skupiny [jaké].

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda survival-analysis
```
