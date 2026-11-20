# Marginální analýza

**Oblast 6 · Ekonomika a byznys** · otázka oblasti: *Kdy se nám to vrátí?*

## Jednou větou

**Kolik přinese další koruna.** Neptáš se, jestli se kanál vyplácí celkově, ale kolik přinese další koruna. Prvních 10 tisíc do reklamy může vydělat hodně, dalších 10 tisíc už málo.

## Kdy použít

- Když rozhoduješ, jestli přidat nebo ubrat rozpočet v kanálu.
- Když kanál funguje, ale nevíš, jestli by fungovaly i další peníze.

## Kdy ne

- Když rozhoduješ jen o celých projektech ano, nebo ne. Pak očekávaná hodnota.

## Co potřebuješ

- Výdaje a výsledky kanálu při různých úrovních (po měsících nebo z testů).

## Postup s AI

1. Dej AI data výdajů a výsledků.
2. Nech odhadnout křivku: jak přínos roste s výdaji a kde se zplošťuje.
3. Nech spočítat, kolik přinese další koruna na dnešní úrovni.
4. Přidávej tam, kde další koruna přinese víc, než stojí.

## Příklad z marketingu

Prvních 10 tisíc měsíčně do vyhledávací reklamy přinese 40 objednávek, dalších 10 tisíc už jen 12. Celkem se kanál vyplácí, ale druhá desetitisícovka ne.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Data z běžného provozu jsou zkreslená sezónou. Nejlepší jsou výsledky z testů různých rozpočtů.
- Průměrná návratnost kanálu přeceňuje návratnost další koruny.

## Související metody

- [Marketing Mix Modeling (MMM)](../5-optimalizace/marketing-mix-modeling.md): kam dát další korunu mezi kanály
- [Customer Lifetime Value (CLV) a CAC](../6-ekonomika/clv-a-cac.md): hodnota zákazníka a náklady na jeho získání
- [Opportunity cost](../6-ekonomika/opportunity-cost.md): co neuděláme, když uděláme tohle

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Marginální analýza.

Tady jsou výdaje a výsledky kanálu [jakého] při různých rozpočtech: [data]. Odhadni, jak přínos roste s výdaji, a spočítej, kolik přinese další koruna na dnešní úrovni. Doporuč, jestli přidat, nebo ubrat.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda marginalni-analyza
```
