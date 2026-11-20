# Vícekriteriální rozhodování

**Oblast 2 · Rozhodování a prioritizace** · otázka oblasti: *Co udělat jako první?*

## Jednou větou

**Když nejde jen o peníze.** Stanovíš si pár kritérií, třeba přínos, riziko, pracnost a dopad na značku, a dáš jim váhy. Projekty pak porovnáš podle všech najednou.

## Kdy použít

- Když rozhodnutí nestojí jen na penězích: značka, riziko, pracnost, strategie.
- Když se tým neshodne, protože každý hodnotí podle jiného kritéria.

## Kdy ne

- Když jde opravdu jen o peníze. Pak stačí očekávaná hodnota.

## Co potřebuješ

- Tři až pět kritérií a jejich váhy (kolik které znamená).
- Hodnocení každé možnosti podle každého kritéria.

## Postup s AI

1. Nech AI pomoct vybrat tři až pět kritérií, která opravdu rozhodují.
2. Dohodněte váhy dřív, než uvidíte výsledky.
3. Ohodnoťte každou možnost a nech AI spočítat vážené skóre.
4. Nech AI ukázat, jak by se pořadí změnilo při jiných vahách.

## Příklad z marketingu

Vybíráš mezi třemi kampaněmi. Kritéria: přínos (40 %), riziko pro značku (30 %), pracnost (20 %), soulad se strategií (10 %). Vítěz podle váženého skóre nemusí být kampaň s nejvyšším přínosem.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Váhy určují výsledek. Stanov je předem, jinak si je nevědomky upravíš podle oblíbené možnosti.
- Kritéria se nemají překrývat, jinak jedno počítáš dvakrát.

## Související metody

- [Očekávaná hodnota](../2-rozhodovani/ocekavana-hodnota.md): kolik to přinese, když započítáme šanci na neúspěch
- [Portfolio optimalizace](../5-optimalizace/portfolio.md): mix jistých malých výher a velkých sázek
- [Pre-mortem](../2-rozhodovani/pre-mortem.md): představ si, že projekt selhal, a zeptej se proč

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Vícekriteriální rozhodování.

Rozhoduji mezi [možnosti]. Pomoz mi vybrat tři až pět kritérií a jejich váhy, pak se mě zeptej na hodnocení každé možnosti, spočítej vážené skóre a ukaž, jak se pořadí změní při jiných vahách.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda vicekriterialni-rozhodovani
```
