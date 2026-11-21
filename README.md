# A co nám to přinese?

**Metody pro lepší marketingová rozhodnutí s AI.** Podklady k přednášce *A co nám to přinese? Přesnější odhady
a lepší výsledky díky AI* (Honza Kovalčík, AI Bootcamp, 21. 11. 2026).

Když se někdo zeptá „a co nám to přinese?“, neodpovídej číslem z hlavy. Odpověz rozpětím a nech si ho spočítat AI.
Tady najdeš 40 metod ze 7 oblastí, ke každé vysvětlení pro nestatistiky a hotový prompt, a vedené kroky,
které tě provedou od odhadu po vyhodnocení.

## Prezentace

Celá přednáška jako jeden HTML soubor: [prezentace/a-co-nam-to-prinese.html](prezentace/a-co-nam-to-prinese.html).
GitHub ji ukáže jen jako kód: otevři soubor, vpravo nahoře klikni na **Download raw file** a stažený soubor
otevři v prohlížeči. Funguje bez internetu. Šipky posouvají slidy, **F** celá obrazovka, **P** pohled řečníka
s poznámkami.

## Jak začít v Claude Code (3 kroky)

1. Stáhni si repo: zelené tlačítko **Code → Download ZIP** a rozbal, nebo
   `git clone https://github.com/kovalcikjan/co-nam-to-prinese.git`.
2. Otevři složku v terminálu a spusť `claude`.
3. Napiš **`/start`** a jednou větou popiš, o čem rozhoduješ.

Claude si přečte pravidla v [CLAUDE.md](CLAUDE.md) a provede tě dál. Potřebuješ jen Python 3, žádné další knihovny.

## Bez Claude Code

Otevři kterýkoli soubor metody ve složce [metody/](metody/) a zkopíruj blok **Zkopíruj do chatu** do ChatGPT,
Clauda nebo Gemini. Hranaté závorky nahraď svými údaji. Prompt hlídá stejná pravidla jako skilly: čísla dodáváš
ty, odhady jako rozpětí, počítá se kódem.

## Vedené kroky: jeden kruh, čtyři kroky

```
  1 Odhadni rozpětí ──> 2 Rozhodni ──> 3 Hledej, co ti uniklo ──> 4 Změř a zpřesni
         ^                                                              │
         └──────────── výsledek je vstup pro příští odhad ──────────────┘
```

| Příkaz | Krok | Co udělá | Metody |
|---|---|---|---|
| `/start` | začátek | zeptá se, o čem rozhoduješ, založí projekt a navrhne cestu | |
| `/odhadni` | 1 Odhadni rozpětí | rozloží přínos na kroky, posbírá rozpětí, spočítá simulaci | referenční třída, Monte Carlo, prediktivní modely |
| `/rozhodni` | 2 Rozhodni | porovná možnosti, návratnost a riziko, co se vejde do kapacity | očekávaná hodnota, hodnota informace, portfolio, doba návratnosti |
| `/proverit` | 3 Hledej, co ti uniklo | co nejvíc hýbe výsledkem, vedlejší efekty, proč by to mohlo selhat | analýza citlivosti, kauzální grafy, pre-mortem |
| `/zmer` | 4 Změř a zpřesni | vyhodnotí výsledek, porovná s odhadem, zpřesní příští odhad | bayesovské testování, bayesovská statistika |
| `/metody` | | přehled metod, doporučí tu správnou k tvé otázce | všechny |
| `/metoda <název>` | | jedna metoda do hloubky na tvém případu, třeba `/metoda monte-carlo` | jedna |

Každý krok zapisuje do `projekty/<nazev>/zapis.md` a další krok na zápis navazuje. Složka `projekty/` se do gitu
nenahrává, tvoje práce zůstane u tebe.

## Všech 40 metod

### 1. Pravděpodobnost a nejistota: *Jaké výsledky jsou možné?*

| Metoda | Jednou větou | Krok | Ukázka |
|---|---|---|---|
| [Odhad podle referenční třídy (base rate)](metody/1-nejistota/referencni-trida.md) | začni tím, jak obvykle dopadly podobné projekty | `/odhadni` |  |
| [Pravděpodobnostní rozdělení](metody/1-nejistota/pravdepodobnostni-rozdeleni.md) | rozpětí možných výsledků místo jednoho čísla |  |  |
| [Kalibrace odhadů](metody/1-nejistota/kalibrace-odhadu.md) | aby rozpětí „na 90 %“ opravdu sedělo devětkrát z deseti |  |  |
| [Monte Carlo simulace](metody/1-nejistota/monte-carlo.md) | spojí rozpětí jednotlivých kroků do tisíců scénářů | `/odhadni` | [ano](priklady/pujcka-na-auto/) |
| [Analýza citlivosti](metody/1-nejistota/analyza-citlivosti.md) | který předpoklad nejvíc hýbe výsledkem | `/proverit` | [ano](priklady/pujcka-na-auto/) |
| [Bayesovská statistika](metody/1-nejistota/bayesovska-statistika.md) | zpřesní odhad, když přijdou nová data | `/zmer` |  |

### 2. Rozhodování a prioritizace: *Co udělat jako první?*

| Metoda | Jednou větou | Krok | Ukázka |
|---|---|---|---|
| [Očekávaná hodnota](metody/2-rozhodovani/ocekavana-hodnota.md) | kolik to přinese, když započítáme šanci na neúspěch | `/rozhodni` | [ano](priklady/tri-projekty/) |
| [Cost of Delay](metody/2-rozhodovani/cost-of-delay.md) | co nás stojí každý týden odkladu; s pracností dává pořadí |  |  |
| [Vícekriteriální rozhodování](metody/2-rozhodovani/vicekriterialni-rozhodovani.md) | když nejde jen o peníze |  |  |
| [Rozhodovací stromy](metody/2-rozhodovani/rozhodovaci-stromy.md) | navazující kroky: nejdřív test, pak rozhodnutí |  |  |
| [Hodnota informace (Value of Information)](metody/2-rozhodovani/hodnota-informace.md) | kdy se vyplatí nejdřív levně ověřit | `/rozhodni` |  |
| [Pre-mortem](metody/2-rozhodovani/pre-mortem.md) | představ si, že projekt selhal, a zeptej se proč | `/proverit` |  |

### 3. Měření skutečného dopadu: *Kolik z toho je naše zásluha?*

| Metoda | Jednou větou | Krok | Ukázka |
|---|---|---|---|
| [Korelace versus kauzalita](metody/3-mereni-dopadu/korelace-vs-kauzalita.md) | růst po kampani není automaticky jejím důsledkem |  |  |
| [Experimenty a Bayesovské testování](metody/3-mereni-dopadu/bayesovske-testovani.md) | náhodné rozdělení; pravděpodobnost místo ano, nebo ne | `/zmer` | [ano](priklady/tlacitko-ab/) |
| [Holdout testy (inkrementalita)](metody/3-mereni-dopadu/holdout-testy.md) | část lidí kampaň neuvidí, rozdíl je přínos kampaně |  |  |
| [Difference-in-Differences](metody/3-mereni-dopadu/difference-in-differences.md) | srovnat změnu se srovnatelnou kontrolní skupinou |  |  |
| [Časové řady](metody/3-mereni-dopadu/casove-rady.md) | trend, sezónnost a mimořádné události |  |  |
| [CausalImpact](metody/3-mereni-dopadu/causalimpact.md) | když kontrolní skupina chybí, model ji poskládá z jiných řad |  |  |

### 4. Predikce a strojové učení: *Co nás nejspíš čeká?*

| Metoda | Jednou větou | Krok | Ukázka |
|---|---|---|---|
| [Prediktivní modely](metody/4-predikce/prediktivni-modely.md) | kolik poptávky a tržeb přijde samo | `/odhadni` |  |
| [Klasifikace](metody/4-predikce/klasifikace.md) | šance na úspěch, třeba který článek se dostane do top 10 |  |  |
| [Uplift modeling](metody/4-predikce/uplift-modeling.md) | u koho kampaň opravdu něco změní |  |  |
| [Clustering](metody/4-predikce/clustering.md) | skupiny klíčových slov, zákazníků a příležitostí |  |  |
| [Survival analysis](metody/4-predikce/survival-analysis.md) | za jak dlouho se něco stane |  |  |
| [Detekce anomálií](metody/4-predikce/detekce-anomalii.md) | problém uvidíš dřív než klient |  |  |

### 5. Optimalizace zdrojů: *Jak rozdělit čas a peníze?*

| Metoda | Jednou větou | Krok | Ukázka |
|---|---|---|---|
| [Lineární a celočíselné programování](metody/5-optimalizace/linearni-programovani.md) | co se vejde do hodin nebo rozpočtu |  |  |
| [Portfolio optimalizace](metody/5-optimalizace/portfolio.md) | mix jistých malých výher a velkých sázek | `/rozhodni` | [ano](priklady/tri-projekty/) |
| [Robustní optimalizace](metody/5-optimalizace/robustni-optimalizace.md) | plán, který vydrží chybu v odhadech |  |  |
| [Marketing Mix Modeling (MMM)](metody/5-optimalizace/marketing-mix-modeling.md) | kam dát další korunu mezi kanály |  |  |
| [Multi-armed bandit](metody/5-optimalizace/multi-armed-bandit.md) | testuje a zároveň vydělává |  |  |

### 6. Ekonomika a byznys: *Kdy se nám to vrátí?*

| Metoda | Jednou větou | Krok | Ukázka |
|---|---|---|---|
| [Customer Lifetime Value (CLV) a CAC](metody/6-ekonomika/clv-a-cac.md) | hodnota zákazníka a náklady na jeho získání |  |  |
| [Marginální analýza](metody/6-ekonomika/marginalni-analyza.md) | kolik přinese další koruna |  |  |
| [Opportunity cost](metody/6-ekonomika/opportunity-cost.md) | co neuděláme, když uděláme tohle |  |  |
| [Doba návratnosti (payback)](metody/6-ekonomika/doba-navratnosti.md) | kdy se nám to vrátí | `/rozhodni` | [ano](priklady/tri-projekty/) |
| [Diskontované cash flow a NPV](metody/6-ekonomika/npv.md) | koruna za rok má menší cenu než dnes |  |  |
| [Real options](metody/6-ekonomika/real-options.md) | začni pilotem, pak rozšiř, nebo ukonči |  |  |

### 7. Modelování systémů: *Co tím ovlivníme jinde?*

| Metoda | Jednou větou | Krok | Ukázka |
|---|---|---|---|
| [Kauzální grafy (DAG)](metody/7-systemy/kauzalni-grafy.md) | nakresli, co co ovlivňuje, než začneš měřit | `/proverit` |  |
| [Markovovy řetězce](metody/7-systemy/markovovy-retezce.md) | přechody zákazníků mezi stavy, třeba Markovova atribuce |  |  |
| [Síťová analýza](metody/7-systemy/sitova-analyza.md) | souvislosti témat, stránek a entit |  |  |
| [Systémová dynamika](metody/7-systemy/systemova-dynamika.md) | zpětné vazby v čase |  |  |
| [Agentní modelování (agent-based modeling)](metody/7-systemy/agentni-modelovani.md) | simulace mnoha zákazníků najednou |  |  |

## Příklady z přednášky

| Příklad | Otázka | Metoda |
|---|---|---|
| [Půjčka na auto](priklady/pujcka-na-auto/) | Kolik přinese nová stránka za rok? | Monte Carlo, analýza citlivosti |
| [Tlačítko A/B](priklady/tlacitko-ab/) | Vyplatí se nové tlačítko? | bayesovské testování |
| [Tři projekty](priklady/tri-projekty/) | Do čeho dát příštích 40 hodin? | doba návratnosti, očekávaná hodnota, portfolio |

Každý příklad má popis a skript, který spustíš příkazem `python3 <skript>.py`. **Všechna čísla v příkladech
jsou vymyšlená** pro přednášku, na příkladu webu cleverpujcky.cz.

## Šablony

- [Odhad s rozpětím](sablony/odhad-rozpeti.md): tabulka kroků s hodnotami nejméně, nejčastěji, nejvíc
- [Kalibrační deník](sablony/kalibracni-denik.md): odhady proti skutečnosti, ať se trefuješ častěji

## Data a bezpečnost

- Do AI nevkládej citlivá a klientská data: jména a e-maily zákazníků, smlouvy, přístupy, interní čísla klienta
  bez jeho souhlasu. Anonymizuj, nebo použij jen souhrnná čísla.
- Ověř si, jestli tvoje firma nemá pravidla, který AI nástroj smíš na pracovní data používat.
- Výsledky jsou odhady. Jsou jen tak dobré jako čísla, která do nich dáš.

## Zdroje čísel z přednášky

- Kohavi, Deng, Frasca, Longbotham, Walker, Xu (2012): *Trustworthy Online Controlled Experiments: Five Puzzling
  Outcomes Explained*, KDD 2012. V Microsoftu zlepšila metriku, kterou zlepšit měla, jen třetina testovaných nápadů.
- Kohavi, Longbotham (2023): *Online Controlled Experiments and A/B Tests*, Encyclopedia of Machine Learning
  and Data Science, Springer.
- Buehler, Griffin, Ross (1994): *Exploring the „Planning Fallacy“*, Journal of Personality and Social Psychology
  67(3), s. 366–381.
