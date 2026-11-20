# Portfolio optimalizace

**Oblast 5 · Optimalizace zdrojů** · otázka oblasti: *Jak rozdělit čas a peníze?*  
**Krok v kruhu:** 2 Rozhodni (`/rozhodni`)  
**Ukázka z přednášky:** [Tři projekty: návratnost a riziko](../../priklady/tri-projekty/)

## Jednou větou

**Mix jistých malých výher a velkých sázek.** Jako u investic: neskládáš jen nejvýnosnější projekty, ale mix, který vydělá a zároveň tě nepoloží, když jedna sázka nevyjde.

## Kdy použít

- Když skládáš plán na čtvrtletí nebo rok z víc projektů s různým rizikem.
- Když nechceš, aby jeden neúspěch zničil celé období.

## Kdy ne

- U jediného projektu.

## Co potřebuješ

- U každého projektu rozpětí přínosu (nejlépe ze simulace) a nároky.
- Kolik rizika snesete (třeba „nechceme skončit v minusu s pravděpodobností vyšší než 20 %“).

## Postup s AI

1. Dej AI simulace nebo rozpětí přínosů projektů.
2. Nech spočítat různé kombinace: očekávaný přínos a šanci na špatný výsledek.
3. Vyber kombinaci s dobrým přínosem a přijatelným rizikem.
4. Typicky: pár jistých menších výher a jedna nebo dvě velké sázky.

## Příklad z marketingu

Kalkulačka je jistá malá výhra, stránka „půjčka na auto“ velká sázka. Spolu se vejdou do 40 hodin a kalkulačka vydělává i v době, kdy auto ještě nic nepřináší nebo nevyjde.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Když projekty závisí na stejné věci (třeba na jednom updatu Googlu), rizika se nevyruší, ale sečtou.
- Riziko, které snesete, si určete předem.

## Související metody

- [Lineární a celočíselné programování](../5-optimalizace/linearni-programovani.md): co se vejde do hodin nebo rozpočtu
- [Robustní optimalizace](../5-optimalizace/robustni-optimalizace.md): plán, který vydrží chybu v odhadech
- [Očekávaná hodnota](../2-rozhodovani/ocekavana-hodnota.md): kolik to přinese, když započítáme šanci na neúspěch

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Portfolio optimalizace.

Tady jsou moje projekty s rozpětím přínosu a nároky: [data]. Spočítej různé kombinace, které se vejdou do [kapacita]: očekávaný přínos a šanci, že skončíme pod [hranice]. Doporuč kombinaci s dobrým poměrem přínosu a rizika.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda portfolio
```
