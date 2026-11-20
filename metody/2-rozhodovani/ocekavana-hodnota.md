# Očekávaná hodnota

**Oblast 2 · Rozhodování a prioritizace** · otázka oblasti: *Co udělat jako první?*  
**Krok v kruhu:** 2 Rozhodni (`/rozhodni`)  
**Ukázka z přednášky:** [Tři projekty: návratnost a riziko](../../priklady/tri-projekty/)

## Jednou větou

**Kolik to přinese, když započítáme šanci na neúspěch.** Vynásobíš možný přínos šancí, že to vyjde. Projekt za 100 tisíc s šancí 20 % má očekávanou hodnotu 20 tisíc, jistých 30 tisíc je tedy lepší volba.

## Kdy použít

- Když porovnáváš projekty s různou šancí na úspěch.
- Když máš sklon vybírat to, co může přinést nejvíc, bez ohledu na šanci.

## Kdy ne

- Když by neúspěch firmu vážně poškodil. Pak řeš i riziko, ne jen průměr (portfolio).

## Co potřebuješ

- U každého projektu možný přínos (nejlépe jako rozpětí) a šanci, že vyjde.
- Pracnost v hodinách, pokud chceš přínos na hodinu.

## Postup s AI

1. Sepiš projekty, u každého přínos, šanci na úspěch a pracnost.
2. Nech AI spočítat očekávanou hodnotu (přínos × šance) a přínos na hodinu práce.
3. Nech je seřadit a porovnat s pořadím, které jste měli podle pocitu.
4. U projektů s velkým rozdílem se zeptej, který předpoklad by pořadí otočil.

## Příklad z marketingu

Ze tří projektů na webu vychází nejvýš stránka „půjčka na auto“ (kolem 4 400 Kč na hodinu práce), kalkulačka kolem 2 700 Kč na hodinu a série článků se v těchto číslech nevyplatí.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Průměr nevidí riziko. Dva projekty se stejnou očekávanou hodnotou můžou mít úplně jinou šanci na nulu.
- Šanci na úspěch ber z referenční třídy, ne z nadšení.

## Související metody

- [Hodnota informace (Value of Information)](../2-rozhodovani/hodnota-informace.md): kdy se vyplatí nejdřív levně ověřit
- [Portfolio optimalizace](../5-optimalizace/portfolio.md): mix jistých malých výher a velkých sázek
- [Odhad podle referenční třídy (base rate)](../1-nejistota/referencni-trida.md): začni tím, jak obvykle dopadly podobné projekty

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Očekávaná hodnota.

Tady jsou moje projekty s možným přínosem, šancí na úspěch a pracností: [tabulka]. Spočítej očekávanou hodnotu a přínos na hodinu práce, seřaď je a řekni, který předpoklad by pořadí nejvíc změnil.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda ocekavana-hodnota
```
