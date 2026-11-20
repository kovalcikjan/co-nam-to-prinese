# Pravděpodobnostní rozdělení

**Oblast 1 · Pravděpodobnost a nejistota** · otázka oblasti: *Jaké výsledky jsou možné?*

## Jednou větou

**Rozpětí možných výsledků místo jednoho čísla.** Místo „přinese to 80 tisíc“ řekneš „spíš 20 až 120 tisíc, nejčastěji kolem 50“. Rozpětí přizná, co nevíš, a ukáže riziko.

## Kdy použít

- Kdykoli někdo chce slyšet, kolik to přinese.
- Když potřebuješ ukázat riziko, ne jen potenciál.

## Kdy ne

- Když je výsledek opravdu jistý (pevná cena, smlouva). Tam stačí číslo.

## Co potřebuješ

- Ke každému neznámému číslu tři hodnoty: nejméně, nejčastěji, nejvíc.
- Odkud ta čísla máš (data, zkušenost, odhad).

## Postup s AI

1. Řekni AI, co odhaduješ, a nech ji rozložit výsledek na pár neznámých.
2. Ke každé neznámé dej tři hodnoty: nejméně, nejčastěji, nejvíc.
3. Nech AI nakreslit, jak rozdělení vypadá, a říct, s jakou pravděpodobností padne výsledek do které části.
4. Výsledek komunikuj jako rozpětí: „s 80% pravděpodobností mezi X a Y, nejčastěji Z“.

## Příklad z marketingu

Místo „kampaň přinese 300 poptávek“ řekneš „nejspíš 200 až 400, nejčastěji kolem 280, pod 150 to spadne jen výjimečně“. Klient hned vidí, s čím počítat.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Rozpětí z hlavy bývají moc úzká. Zkontroluj je kalibrací.
- Nejčastější hodnota není totéž co průměr. U nesouměrných rozdělení se liší hodně.

## Související metody

- [Kalibrace odhadů](../1-nejistota/kalibrace-odhadu.md): aby rozpětí „na 90 %“ opravdu sedělo devětkrát z deseti
- [Monte Carlo simulace](../1-nejistota/monte-carlo.md): spojí rozpětí jednotlivých kroků do tisíců scénářů
- [Odhad podle referenční třídy (base rate)](../1-nejistota/referencni-trida.md): začni tím, jak obvykle dopadly podobné projekty

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Pravděpodobnostní rozdělení.

Chci odhadnout [co]. Pomoz mi vyjádřit odhad jako rozdělení: zeptej se na nejnižší, nejčastější a nejvyšší hodnotu každého neznámého čísla a ukaž, jak pravděpodobné jsou různé výsledky.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda pravdepodobnostni-rozdeleni
```
