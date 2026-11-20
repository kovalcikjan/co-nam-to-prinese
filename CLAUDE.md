# Pravidla pro AI v tomto repu

Repo pomáhá marketérům dělat lepší rozhodnutí: odhadnout přínos jako rozpětí, rozhodnout, co dělat první,
najít, co uniklo, a po čase výsledek změřit. Uživatel obvykle není programátor ani statistik.

## Jak mluvit

- Odpovídej jazykem uživatele, výchozí je čeština. Krátce, jasně, bez odborných zkratek. Odborný pojem
  vysvětli jednou větou, když ho použiješ poprvé.
- Ptej se postupně, nejvýš na tři věci najednou.
- Na konci každého kroku napiš jednou větou, co z výsledku plyne pro rozhodnutí, a navrhni další příkaz
  (`/odhadni`, `/rozhodni`, `/proverit`, `/zmer`, `/metoda <název>`).

## Čísla dodává člověk

- Nikdy si nevymýšlej vstupní čísla. Když chybí, zeptej se. Když uživatel neví, nabídni, jak číslo zjistit,
  nebo ho požádej o hrubý odhad.
- Odhady chtěj jako rozpětí: nejméně, nejčastěji, nejvíc. Ke každému se zeptej, odkud je (data, zkušenost, odhad).
- Vždy se zeptej na referenční třídu: jak obvykle dopadly podobné věci (stránky, kampaně, články).
- Každé číslo, které je odhad, tak označ.

## Počítá kód, ne chat

- Všechno, co se počítá, spočítej programem a spusť ho. Nepočítej v textu odpovědi.
- Preferuj Python se standardní knihovnou (`random`, `math`, `statistics`, `csv`, `json`), aby skript běžel všude.
  Když metoda potřebuje další knihovnu, řekni to a nabídni jednodušší náhradu.
- Simulace: 10 000 scénářů, pevný seed, ať jde výsledek zopakovat.
- Výsledek uváděj jako rozpětí: 10., 50. a 90. percentil, u peněz i šanci, že nepokryje náklady.
- Vzorové skripty jsou v `priklady/`. Navazuj na jejich styl.

## Kam ukládat

- Každé rozhodnutí má složku `projekty/<nazev-bez-diakritiky>/`.
- `projekty/<nazev>/zapis.md` je paměť projektu: na začátku každého kroku ho přečti, na konci do něj připiš,
  co krok zjistil (vstupy, výsledek, rozhodnutí, datum). Nic v něm nemaž, jen doplňuj.
- Skripty ukládej do složky projektu (`odhad.py`, `rozhodnuti.py`, …), výstupy jako samostatné HTML
  (`odhad.html`, …) s grafy nakreslenými jako vložené SVG, bez knihoven z internetu, aby se daly poslat dál.
- Složka `projekty/` se do gitu nenahrává (je v `.gitignore`), práce zůstane na počítači uživatele.

## Data a bezpečnost

- Když uživatel vloží citlivá nebo klientská data (jména zákazníků, e-maily, smlouvy, interní tržby klienta),
  upozorni ho a navrhni anonymizaci nebo jen agregovaná čísla.
- Nikdy nežádej hesla ani přístupy k účtům.

## Kde co je

- `metody/`: 40 metod v 7 oblastech, jeden soubor na metodu (co to je, kdy použít, co potřebuješ, postup, příklad,
  na co si dát pozor, prompt). Při práci s metodou si její soubor vždy přečti.
- `.claude/skills/`: příkazy `/start`, `/metody`, `/metoda`, `/odhadni`, `/rozhodni`, `/proverit`, `/zmer`.
- `sablony/`: šablona odhadu s rozpětím a kalibrační deník.
- `priklady/`: tři ukázky z přednášky s vymyšlenými čísly.
