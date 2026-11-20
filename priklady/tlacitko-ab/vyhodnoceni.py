#!/usr/bin/env python3
"""Example 2: Bayesian evaluation of an A/B test of a button in a loan comparison tool.

A = today's button "Zobrazit půjčku", B = new button "Porovnat nabídky". All numbers are ILLUSTRATIVE (made up for
the talk, website cleverpujcky.cz). Standard library only, fixed seed.

Run:  python3 vyhodnoceni.py
Writes vysledek.html next to this script.
"""
import html
import math
import random
from pathlib import Path

SEED = 2026 + 3
DRAWS = 20_000
A = (2400, 288)              # visits, clicks to a lender
B = (2400, 324)
VISITS_PER_MONTH = 3000      # visits of the comparison tool per month
VALUE_PER_CLICK = 0.06 * 900  # Kč per click = approval 6 % x commission 900 Kč
OUT = Path(__file__).resolve().parent / "vysledek.html"


def pct(xs, p):
    s = sorted(xs)
    k = (len(s) - 1) * p
    f, c = math.floor(k), math.ceil(k)
    return s[f] + (s[c] - s[f]) * (k - f)


def proc(x, dec=0):
    return f"{x * 100:.{dec}f}".replace(".", ",") + " %"


def kc(x):
    return f"{round(x, -1):,.0f}".replace(",", " ") + " Kč"


def classic_p_value(a, b):
    """Two-sided two-proportion z-test, the 'usual' evaluation."""
    (na, xa), (nb, xb) = a, b
    pool = (xa + xb) / (na + nb)
    z = (xb / nb - xa / na) / math.sqrt(pool * (1 - pool) * (1 / na + 1 / nb))
    return math.erfc(abs(z) / math.sqrt(2))


def posterior_draws(a, b, draws, seed):
    """Differences pB - pA from Beta(1 + clicks, 1 + misses) posteriors (uniform prior)."""
    random.seed(seed)
    (na, xa), (nb, xb) = a, b
    a_post, b_post = (1 + xa, 1 + na - xa), (1 + xb, 1 + nb - xb)
    return [random.betavariate(*b_post) - random.betavariate(*a_post) for _ in range(draws)]


def main():
    p_value = classic_p_value(A, B)
    diffs = posterior_draws(A, B, DRAWS, SEED)
    gain = [d * VISITS_PER_MONTH * VALUE_PER_CLICK for d in diffs]
    p_better = sum(d > 0 for d in diffs) / DRAWS
    g10, g50, g90, gmean = pct(gain, .1), pct(gain, .5), pct(gain, .9), sum(gain) / DRAWS
    risk = sum(max(-g, 0) for g in gain) / DRAWS  # expected monthly loss if we pick B and B is in fact worse

    print("Ilustrační čísla, cleverpujcky.cz, tlačítko ve srovnávači")
    print(f"A: {proc(A[1] / A[0], 1)} prokliků, B: {proc(B[1] / B[0], 1)} prokliků")
    print(f"Klasické vyhodnocení: p = {p_value:.2f}".replace(".", ",") + " → rozdíl není průkazný")
    print(f"Bayesovsky: B je lepší s pravděpodobností {proc(p_better, 1)}")
    print(f"Přínos B za měsíc: 80 % mezi {kc(g10)} a {kc(g90)}, průměr {kc(gmean)}")
    print(f"Když se mýlíme, riskujeme v průměru {kc(risk)} měsíčně")

    p_txt = f"{p_value:.2f}".replace(".", ",")  # computed outside the template, older Pythons need that
    OUT.write_text(f"""<!doctype html><html lang="cs"><meta charset="utf-8"><title>Tlačítko A/B: vyhodnocení</title>
<style>body{{font-family:system-ui,sans-serif;max-width:820px;margin:32px auto;padding:0 16px;color:#1a1a1a}}
.big{{font-size:28px;font-weight:700;color:#E5712C}} .note{{color:#666;font-size:14px}}</style>
<h1>Nové tlačítko: vyplatí se?</h1>
<p class="note">Ilustrační čísla vymyšlená pro přednášku. {DRAWS:,} vzorků z bayesovského rozdělení, pevný seed {SEED}.</p>
<p>A (dnes): {html.escape(proc(A[1] / A[0], 1))} · B (nové): {html.escape(proc(B[1] / B[0], 1))}<br>
Klasicky: p = {p_txt}, „rozdíl není průkazný“.</p>
<p class="big">B je lepší s pravděpodobností {proc(p_better)}</p>
<p>Přínos B za měsíc: 80 % mezi {kc(g10)} a {kc(g90)}, průměr {kc(gmean)}.<br>
Když se mýlíme, riskujeme v průměru {kc(risk)} měsíčně.</p>
<p>Rozhodnutí: nasadit B. Riziko je malé proti očekávanému přínosu.</p>
</html>""".replace(f"{DRAWS:,}", f"{DRAWS:,}".replace(",", " ")), encoding="utf-8")
    print(f"Výstup: {OUT}")


if __name__ == "__main__":
    main()
