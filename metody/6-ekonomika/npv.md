# Diskontované cash flow a NPV

**Oblast 6 · Ekonomika a byznys** · otázka oblasti: *Kdy se nám to vrátí?*

## Jednou větou

**Koruna za rok má menší cenu než dnes.** Peníze, které přijdou později, mají menší hodnotu, protože na ně čekáš a nesou riziko. NPV převede budoucí přínosy na dnešní koruny, aby šly projekty férově porovnat.

## Kdy použít

- Když porovnáváš projekty, jejichž přínosy přicházejí v různé době (SEO za rok, PPC hned).
- U větších investic na víc let.

## Kdy ne

- U krátkých akcí na pár měsíců. Rozdíl bude zanedbatelný.

## Co potřebuješ

- Náklady a přínosy po měsících nebo letech.
- Diskontní sazbu: jaký výnos by peníze měly jinde (třeba 10 % ročně). Dohodni ji s financemi.

## Postup s AI

1. Dej AI tok nákladů a přínosů v čase.
2. Nech převést budoucí přínosy na dnešní koruny podle diskontní sazby.
3. Sečti je, to je NPV. Kladné NPV znamená, že projekt vydělá víc než alternativa s danou sazbou.
4. Nech porovnat projekty podle NPV a ukázat, jak se pořadí mění při jiné sazbě.

## Příklad z marketingu

SEO projekt přinese 100 tisíc, ale až za rok a půl. PPC kampaň 80 tisíc hned. Při sazbě 10 % ročně má SEO dnes hodnotu kolem 87 tisíc, při 20 % jen kolem 76 tisíc a vyhraje PPC.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Sazba je předpoklad. Ukaž výsledek pro víc sazeb.
- NPV z jednoho čísla zase skrývá nejistotu. Kombinuj ji se simulací.

## Související metody

- [Doba návratnosti (payback)](../6-ekonomika/doba-navratnosti.md): kdy se nám to vrátí
- [Real options](../6-ekonomika/real-options.md): začni pilotem, pak rozšiř, nebo ukonči
- [Customer Lifetime Value (CLV) a CAC](../6-ekonomika/clv-a-cac.md): hodnota zákazníka a náklady na jeho získání

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Diskontované cash flow a NPV.

Tady jsou náklady a přínosy projektů po měsících: [data]. Spočítej NPV při diskontní sazbě [sazba] ročně, porovnej projekty a ukaž, jak se pořadí mění při jiné sazbě.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda npv
```
