# Síťová analýza

**Oblast 7 · Modelování systémů** · otázka oblasti: *Co tím ovlivníme jinde?*

## Jednou větou

**Souvislosti témat, stránek a entit.** Stránky, témata nebo značky bereš jako body a odkazy či zmínky jako spojnice. Ukáže, co je v síti důležité a kde chybí propojení, třeba v interním prolinkování.

## Kdy použít

- U interního prolinkování webu: které stránky jsou důležité a které odříznuté.
- Když mapuješ témata, entity nebo zmínky značky a jejich souvislosti.

## Kdy ne

- Když máš pár stránek. Síť je vidět i bez výpočtu.

## Co potřebuješ

- Seznam spojení: odkud kam vede odkaz, které téma souvisí s kterým (třeba export z crawleru).

## Postup s AI

1. Dej AI seznam spojení.
2. Nech spočítat, které body jsou nejdůležitější a které osamocené.
3. Nech najít skupiny, které spolu hodně souvisí, a chybějící propojení.
4. Navrhni úpravy: kam přidat odkazy nebo obsah.

## Příklad z marketingu

Crawl ukáže, že nejdůležitější obchodní stránky dostávají méně interních odkazů než staré novinky. Přidáním odkazů z navštěvovaných článků se jejich váha ve webu zvedne.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Důležitost v síti není totéž co obchodní hodnota. Kombinuj obojí.
- Velké sítě je těžké číst z obrázku. Chtěj tabulky a seznamy.

## Související metody

- [Clustering](../4-predikce/clustering.md): skupiny klíčových slov, zákazníků a příležitostí
- [Markovovy řetězce](../7-systemy/markovovy-retezce.md): přechody zákazníků mezi stavy, třeba Markovova atribuce
- [Systémová dynamika](../7-systemy/systemova-dynamika.md): zpětné vazby v čase

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Síťová analýza.

Tady je seznam interních odkazů [nebo souvislostí témat]: [data]. Spočítej, které stránky jsou v síti nejdůležitější a které osamocené, najdi chybějící propojení a navrhni, kam přidat odkazy.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda sitova-analyza
```
