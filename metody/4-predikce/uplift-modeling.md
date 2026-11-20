# Uplift modeling

**Oblast 4 · Predikce a strojové učení** · otázka oblasti: *Co nás nejspíš čeká?*

## Jednou větou

**U koho kampaň opravdu něco změní.** Nehledá ty, kdo nejspíš koupí, ale ty, které kampaň ke koupi opravdu přesvědčí. Neplatíš za zákazníky, kteří by koupili i tak.

## Kdy použít

- Když cílíš kampaně, slevy nebo e-maily a nechceš platit za lidi, kteří by koupili i tak.
- Když máš data z minulého testu s kontrolní skupinou.

## Kdy ne

- Bez kontrolní skupiny. Z běžných dat se uplift spočítat nedá.

## Co potřebuješ

- Data z testu, kde část lidí kampaň dostala a část náhodně ne.
- Vlastnosti lidí (historie nákupů, zdroj, segment).

## Postup s AI

1. Dej AI data z testu s kontrolní skupinou.
2. Nech odhadnout, u kterých skupin lidí kampaň zvedá nákupy nejvíc.
3. Rozděl lidi na ty, které kampaň přesvědčí, ty, kteří koupí tak jako tak, a ty, kterým je to jedno.
4. Příště cil jen na první skupinu.

## Příklad z marketingu

Sleva 10 % zvedne nákupy hlavně u lidí, kteří nakoupili jednou před rokem. Věrní zákazníci by koupili i bez ní. Když jim slevu nepošleš, ušetříš marži.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Potřebuje dost dat. U malých testů jsou výsledky pro jednotlivé skupiny nespolehlivé.
- Je to pokročilá metoda. Začni s holdout testem.

## Související metody

- [Holdout testy (inkrementalita)](../3-mereni-dopadu/holdout-testy.md): část lidí kampaň neuvidí, rozdíl je přínos kampaně
- [Klasifikace](../4-predikce/klasifikace.md): šance na úspěch, třeba který článek se dostane do top 10
- [Experimenty a Bayesovské testování](../3-mereni-dopadu/bayesovske-testovani.md): náhodné rozdělení; pravděpodobnost místo ano, nebo ne

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Uplift modeling.

Mám data z testu [kampaně], kde náhodná část lidí kampaň nedostala: [data s vlastnostmi lidí]. Odhadni, u kterých skupin lidí kampaň nákupy opravdu zvedá, a navrhni, na koho příště cílit.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda uplift-modeling
```
