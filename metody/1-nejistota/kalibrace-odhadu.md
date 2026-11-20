# Kalibrace odhadů

**Oblast 1 · Pravděpodobnost a nejistota** · otázka oblasti: *Jaké výsledky jsou možné?*

## Jednou větou

**Aby rozpětí „na 90 %“ opravdu sedělo devětkrát z deseti.** Zapisuj si odhady s rozpětím a po čase je porovnej se skutečností. Když se trefuješ jen v polovině případů, dávej širší rozpětí.

## Kdy použít

- Když pravidelně odhaduješ přínosy, termíny nebo rozpočty a chceš se trefovat častěji.
- Když tým dává rozpětí, ale nikdo nekontroluje, jestli sedí.

## Kdy ne

- U jednorázového odhadu. Kalibrace potřebuje víc odhadů a čas.

## Co potřebuješ

- Deník odhadů: co jsi odhadl, jaké rozpětí, jak moc sis byl jistý. Šablona je v [sablony/kalibracni-denik.md](../../sablony/kalibracni-denik.md).
- Po čase skutečný výsledek.

## Postup s AI

1. Každý odhad zapiš jako rozpětí s jistotou, třeba „na 90 % mezi X a Y“.
2. Po skončení dopiš skutečnost.
3. Po 10 až 20 odhadech dej deník AI a nech spočítat, kolik skutečností padlo do rozpětí.
4. Když je to výrazně méně než devět z deseti, rozšiř rozpětí. Když skoro vždy, můžeš je zúžit.

## Příklad z marketingu

Za čtvrtletí jsi odhadl přínos 12 článků s rozpětím „na 90 %“. Do rozpětí se trefilo jen 6. Tvoje rozpětí jsou tedy moc úzká a příště je dáš zhruba dvakrát širší.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Lidé bývají přehnaně sebejistí. Studenti, kteří odhadovali, kdy dopíšou práci, „když se všechno pokazí“, ten termín dodrželi jen v 48,7 % případů (Buehler, Griffin, Ross, 1994).
- Vyhodnocuj poctivě i odhady, které nevyšly. Bez nich kalibrace nefunguje.

## Související metody

- [Pravděpodobnostní rozdělení](../1-nejistota/pravdepodobnostni-rozdeleni.md): rozpětí možných výsledků místo jednoho čísla
- [Odhad podle referenční třídy (base rate)](../1-nejistota/referencni-trida.md): začni tím, jak obvykle dopadly podobné projekty
- [Bayesovská statistika](../1-nejistota/bayesovska-statistika.md): zpřesní odhad, když přijdou nová data

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Kalibrace odhadů.

Tady je můj deník odhadů s rozpětím a skutečnými výsledky: [deník]. Spočítej, jak často se skutečnost trefila do rozpětí, a řekni, jestli mám rozpětí rozšířit, nebo zúžit.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda kalibrace-odhadu
```
