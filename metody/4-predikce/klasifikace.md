# Klasifikace

**Oblast 4 · Predikce a strojové učení** · otázka oblasti: *Co nás nejspíš čeká?*

## Jednou větou

**Šance na úspěch, třeba který článek se dostane do top 10.** Model zařadí každou položku do skupiny a řekne, s jakou pravděpodobností. Třeba: tenhle článek má šanci 60 % na top 10, tenhle jen 15 %.

## Kdy použít

- Když chceš odhadnout šanci na úspěch u mnoha položek najednou (články, leady, produkty).
- Když chceš vědět, které vlastnosti úspěch provázejí.

## Kdy ne

- Když máš málo příkladů úspěchu i neúspěchu (desítky, ne stovky).

## Co potřebuješ

- Tabulku minulých položek s vlastnostmi (délka, téma, hledanost, síla domény) a výsledkem (uspěl, neuspěl).
- Nové položky, pro které chceš šanci.

## Postup s AI

1. Dej AI tabulku minulých položek s výsledkem.
2. Nech postavit jednoduchý model (třeba logistickou regresi) a ověřit ho na části dat, kterou neviděl.
3. Nech spočítat šanci pro nové položky.
4. Šance použij jako vstup do očekávané hodnoty.

## Příklad z marketingu

Z 200 minulých článků model zjistí, co mají společné ty v top 10. U plánovaných článků pak řekne: tenhle má šanci 60 %, tenhle 15 %. Přednost dostanou ty s vyšší šancí a vyšším přínosem.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Model najde souvislosti, ne příčiny. Délka článku může souviset s úspěchem jen proto, že dlouhé články píšeš na silná témata.
- Ověřuj na datech, která model neviděl, jinak přecení svou přesnost.

## Související metody

- [Očekávaná hodnota](../2-rozhodovani/ocekavana-hodnota.md): kolik to přinese, když započítáme šanci na neúspěch
- [Clustering](../4-predikce/clustering.md): skupiny klíčových slov, zákazníků a příležitostí
- [Odhad podle referenční třídy (base rate)](../1-nejistota/referencni-trida.md): začni tím, jak obvykle dopadly podobné projekty

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Klasifikace.

Tady je tabulka minulých [položek] s vlastnostmi a výsledkem: [data]. Postav jednoduchý model, ověř ho na části dat, kterou neviděl, a spočítej šanci na úspěch pro tyto nové položky: [data].

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda klasifikace
```
