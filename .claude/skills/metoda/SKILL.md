---
name: metoda
description: Jedna konkrétní metoda do hloubky na případu uživatele, třeba /metoda monte-carlo nebo /metoda bayesovske-testovani. Použij, když uživatel napíše /metoda s názvem metody nebo chce jednu metodu vysvětlit, vyzkoušet a spočítat na svých datech. Vysvětlí ji na jeho případu, posbírá vstupy, spočítá kódem a uloží výstup.
---

# Metoda: jedna metoda na tvém případu

Text za příkazem (ARGUMENTS) je název metody (třeba `monte-carlo`), případně i popis situace.

## 1. Najdi metodu

- Hledej soubor `metody/*/<název>.md`. Když přesná shoda není, hledej podle názvu i obsahu (bez ohledu na
  diakritiku a velikost písmen) a nabídni nejvýš tři nejbližší.
- Když název chybí, zeptej se, kterou metodu chce, nebo nabídni `/metody`.
- Soubor metody celý přečti. Postup, upozornění a příklad z něj jsou závazné.

## 2. Vysvětli na jeho případu

- Když uživatel ještě nepopsal situaci, zeptej se jednou otázkou, na čem chce metodu použít.
- Ve třech až pěti větách vysvětli, co metoda udělá právě s jeho případem a co z ní vyjde. Bez vzorců.
- Pokud existuje projekt v `projekty/` k tomuto rozhodnutí, přečti jeho `zapis.md` a navaž na něj. Jinak
  nabídni založení projektu (stejně jako `/start`).

## 3. Posbírej vstupy

- Ptej se podle sekce „Co potřebuješ“, nejvýš na tři věci najednou.
- Čísla jen od uživatele, odhady jako rozpětí (nejméně, nejčastěji, nejvíc), u každého odkud je.
- Šablona pro rozpětí: `sablony/odhad-rozpeti.md`.

## 4. Spočítej a ulož

- U metod, které počítají: napiš skript (Python, standardní knihovna, pevný seed), ulož ho do složky projektu
  a spusť. Vzor: `priklady/`.
- Výsledek jako rozpětí (10., 50. a 90. percentil), u peněz i šanci, že nepokryje náklady.
- Ulož samostatné HTML s výsledkem a grafem (vložené SVG) do složky projektu.
- U metod bez výpočtu (pre-mortem, kauzální graf, korelace a kauzalita) vytvoř strukturovaný výstup
  (seznam, tabulku nebo graf šipek) a ulož ho do zápisu.

## 5. Zapiš a navrhni další krok

- Do `projekty/<nazev>/zapis.md` připiš: metoda, vstupy, výsledek, jedna věta pro rozhodnutí, datum.
- Odpověz: výsledek jako rozpětí, jedna věta pro rozhodnutí, kde je HTML, a další příkaz. Další krok vyber podle
  sekce „Související metody“ nebo podle kruhu: `/odhadni` → `/rozhodni` → `/proverit` → `/zmer`.
