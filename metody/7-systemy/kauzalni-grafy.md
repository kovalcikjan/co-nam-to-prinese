# Kauzální grafy (DAG)

**Oblast 7 · Modelování systémů** · otázka oblasti: *Co tím ovlivníme jinde?*  
**Krok v kruhu:** 3 Hledej, co ti uniklo (`/proverit`)

## Jednou větou

**Nakresli, co co ovlivňuje, než začneš měřit.** Šipkami nakreslíš, co podle tebe co ovlivňuje: sezóna prodeje, kampaň návštěvy, cena konverze. Hned vidíš, co musíš při měření zohlednit.

## Kdy použít

- Než začneš měřit dopad, abys věděl, co všechno výsledek ovlivňuje.
- Když se tým neshodne, co je příčina a co důsledek.

## Kdy ne

- Jako důkaz. Graf zachycuje, co si myslíš, a data ho mají ověřit.

## Co potřebuješ

- Výsledek, který tě zajímá, a vše, co ho podle tebe ovlivňuje.

## Postup s AI

1. Řekni AI, jaký výsledek sleduješ a co měníš.
2. Nech nakreslit graf: co ovlivňuje co, šipkami.
3. Doplň, co AI neví (vaše sezóna, jiné kampaně, ceny).
4. Nech říct, na co musíš při měření dát pozor: společné příčiny, které vyrábějí falešné souvislosti.

## Příklad z marketingu

Sezóna zvedá hledanost i prodeje. Když v sezóně spustíš kampaň, graf ukáže, že bez srovnání se sezónou připíšeš kampani i to, co udělala sezóna. A nová stránka může brát návštěvy stávajícím stránkám (kanibalizace).

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Graf je jen tak dobrý jako tvoje znalost. Nech AI navrhnout i vazby, na které jsi nepomyslel.
- Šipky mají směr. Ujasni si, co je příčina.

## Související metody

- [Korelace versus kauzalita](../3-mereni-dopadu/korelace-vs-kauzalita.md): růst po kampani není automaticky jejím důsledkem
- [Systémová dynamika](../7-systemy/systemova-dynamika.md): zpětné vazby v čase
- [Pre-mortem](../2-rozhodovani/pre-mortem.md): představ si, že projekt selhal, a zeptej se proč

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Kauzální grafy (DAG).

Sleduji [výsledek] a měním [co]. Nakresli kauzální graf: co všechno výsledek ovlivňuje a jak spolu věci souvisí. Pak řekni, na co si mám při měření dát pozor, abych dopad nepřecenil.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Drž se mého konkrétního případu, ne obecných rad. Na konci jednou větou napiš, co z toho plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda kauzalni-grafy
```
