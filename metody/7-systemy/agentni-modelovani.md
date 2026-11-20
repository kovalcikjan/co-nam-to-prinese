# Agentní modelování (agent-based modeling)

**Oblast 7 · Modelování systémů** · otázka oblasti: *Co tím ovlivníme jinde?*

## Jednou větou

**Simulace mnoha zákazníků najednou.** Nasimuluješ tisíce zákazníků s jednoduchými pravidly a sleduješ, co udělají dohromady. „Syntetičtí zákazníci“ z AI ale skutečná data nenahradí.

## Kdy použít

- Když výsledek vzniká z chování mnoha lidí, kteří se navzájem ovlivňují (doporučení, šíření, fronty).
- Když chceš zkusit „co kdyby“ bez nasazení naostro.

## Kdy ne

- Jako náhradu skutečných dat o zákaznících. Syntetičtí zákazníci z AI můžou přinést nápady, ne skutečné chování.

## Co potřebuješ

- Jednoduchá pravidla chování (kdy člověk nakoupí, komu to řekne).
- Hrubé odhady parametrů, ideálně z dat.

## Postup s AI

1. Popiš AI chování zákazníků jednoduchými pravidly.
2. Nech napsat simulaci tisíců zákazníků.
3. Nech spustit scénáře (třeba s doporučovacím programem a bez něj).
4. Výsledky ověř na skutečných datech nebo malým testem.

## Příklad z marketingu

Simulace 10 000 zákazníků ukáže, jestli doporučovací program s odměnou 200 Kč rozjede šíření, nebo jen zaplatí lidem, kteří by značku doporučili i tak.

*Čísla jsou vymyšlená pro ilustraci.*

## Na co si dát pozor

- Pravidla si vymýšlíš ty. Výsledek je jen tak dobrý jako ona.
- Výsledky ber jako hypotézy k ověření, ne jako předpověď.

## Související metody

- [Systémová dynamika](../7-systemy/systemova-dynamika.md): zpětné vazby v čase
- [Monte Carlo simulace](../1-nejistota/monte-carlo.md): spojí rozpětí jednotlivých kroků do tisíců scénářů
- [Uplift modeling](../4-predikce/uplift-modeling.md): u koho kampaň opravdu něco změní

## Zkopíruj do chatu

Funguje v ChatGPT, Claude i Gemini. Hranaté závorky nahraď svými údaji. Nevkládej citlivá ani klientská data.

```text
Pomoz mi s metodou Agentní modelování (agent-based modeling).

Chci nasimulovat [situaci]. Pomoz mi popsat chování zákazníků jednoduchými pravidly, napiš simulaci tisíců zákazníků a porovnej scénáře [A] a [B]. Upozorni mě, co z výsledku je jen hypotéza.

Moje situace: [popiš svůj případ]

Pravidla: Ptej se mě postupně, nejvýš na tři věci najednou. Žádná čísla si nevymýšlej, odhady chci jako rozpětí (nejméně, nejčastěji, nejvíc). Počítej programem, ne z hlavy. Výsledek ukaž jako rozpětí (10., 50. a 90. percentil) a jednou větou napiš, co z něj plyne pro rozhodnutí. Piš srozumitelně, bez zkratek.
```

## V Claude Code

```text
/metoda agentni-modelovani
```
