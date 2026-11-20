# Analýza citlivosti

**Oblast 1 · Pravděpodobnost a nejistota** · otázka oblasti: *Jaké výsledky jsou možné?*  
**Krok v kruhu:** 3 Hledej, co ti uniklo (`/proverit`)  
**Ukázka z přednášky:** [Půjčka na auto: Monte Carlo](../../priklady/pujcka-na-auto/)

## Jednou větou

**Který předpoklad nejvíc hýbe výsledkem.** Měníš jeden předpoklad po druhém a sleduješ, jak moc se pohne výsledek. Ten, který hýbe nejvíc, ověř jako první.

## Kdy použít

- Po každém odhadu, abys věděl, co ověřit jako první.
- Když se tým hádá, který předpoklad je důležitý.

## Kdy ne

- Když máš jen jeden vstup.

## Co potřebuješ

- Hotový výpočet nebo simulaci se vstupy v rozpětí.

## Postup s AI

1. Nech AI nastavit všechny vstupy na střed rozpětí.
2. Pak hýbej vždy jedním vstupem od spodní k horní hranici a sleduj, jak se změní výsledek.
3. Nech seřadit vstupy podle toho, jak moc výsledkem hýbou, a nakreslit tornádový graf.
4. Ten nahoře ověř jako první, ideálně levným testem.

## Příklad z marketingu

U stránky „půjčka na auto“ nejvíc rozhoduje, jestli se dostane do top 10: očekávaná hodnota se pohne mezi 6 a 147 tisíci ročně. Ostatní předpoklady hýbou výsledkem jen o desítky tisíc. Nejdřív se tedy ověřuje pozice.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Hýbání jedním vstupem nevidí, když se dva vstupy pohnou spolu.
- Důležitost závisí na šířce rozpětí. Vstup může jen vypadat nedůležitě, protože jsi jeho rozpětí odhadl příliš sebejistě.

## Související metody

- [Monte Carlo simulace](../1-nejistota/monte-carlo.md): spojí rozpětí jednotlivých kroků do tisíců scénářů
- [Hodnota informace (Value of Information)](../2-rozhodovani/hodnota-informace.md): kdy se vyplatí nejdřív levně ověřit
- [Rozhodovací stromy](../2-rozhodovani/rozhodovaci-stromy.md): navazující kroky: nejdřív test, pak rozhodnutí

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Analýza citlivosti.

Tady je můj výpočet se vstupy v rozpětí: [výpočet]. Udělej analýzu citlivosti: nastav vstupy na střed, hýbej vždy jedním od spodní k horní hranici, seřaď je podle vlivu na výsledek a řekni, který mám ověřit jako první.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda analyza-citlivosti
```
