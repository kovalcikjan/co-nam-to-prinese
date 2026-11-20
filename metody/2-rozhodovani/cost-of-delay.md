# Cost of Delay

**Oblast 2 · Rozhodování a prioritizace** · otázka oblasti: *Co udělat jako první?*

## Jednou větou

**Co nás stojí každý týden odkladu; s pracností dává pořadí.** Spočítej, o kolik peněz přicházíš každý týden, kdy věc není hotová. Vyděl to pracností a dostaneš pořadí: nejdřív to, co rychle zastaví největší ztrátu.

## Kdy použít

- Když máš víc věcí rozdělaných a nevíš, co dokončit dřív.
- U oprav a vylepšení, kde každý týden bez nich stojí peníze (rozbitý formulář, sezónní kampaň).

## Kdy ne

- Když odklad nic nestojí, třeba u obsahu, který není vázaný na sezónu.

## Co potřebuješ

- U každé věci, kolik peněz týdně ztrácíš, dokud není hotová.
- Kolik práce to zabere.

## Postup s AI

1. Ke každé položce odhadni ztrátu za týden odkladu (jako rozpětí).
2. Odhadni pracnost.
3. Nech AI vydělit ztrátu za týden pracností a seřadit od nejvyššího čísla.
4. Nahoře je to, co za málo práce zastaví největší ztrátu.

## Příklad z marketingu

Rozbitý formulář stojí 20 tisíc týdně a oprava zabere dva dny. Nová kampaň by přinesla 30 tisíc týdně, ale zabere tři týdny. Oprava jde první, i když kampaň vypadá větší.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Sezónní věci mají ztrátu, která po termínu skočí, ne roste rovnoměrně. Řekni to AI.
- Ztrátu za týden je těžké odhadnout. Dej ji jako rozpětí.

## Související metody

- [Očekávaná hodnota](../2-rozhodovani/ocekavana-hodnota.md): kolik to přinese, když započítáme šanci na neúspěch
- [Opportunity cost](../6-ekonomika/opportunity-cost.md): co neuděláme, když uděláme tohle
- [Lineární a celočíselné programování](../5-optimalizace/linearni-programovani.md): co se vejde do hodin nebo rozpočtu

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Cost of Delay.

Tady je seznam rozdělaných úkolů: [úkoly]. U každého se mě zeptej, kolik peněz týdně stojí, že není hotový, a kolik práce zabere. Pak je seřaď podle ztráty za týden dělené pracností.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda cost-of-delay
```
