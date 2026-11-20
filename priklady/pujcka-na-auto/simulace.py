#!/usr/bin/env python3
"""Example 1: Monte Carlo estimate of the yearly benefit of a new comparison page "půjčka na auto".

All inputs are ILLUSTRATIVE (made up for the talk, website cleverpujcky.cz). Standard library only, fixed seed,
so every run prints the same numbers.

Run:  python3 simulace.py
Writes vysledek.html next to this script (open it in a browser).
"""
import html
import math
import random
from pathlib import Path

SEED = 2026
N = 10_000          # number of simulated scenarios
RATE = 800          # Kč per hour of own work
HOURS = 25          # hours to build the page
OUT = Path(__file__).resolve().parent / "vysledek.html"

# Each step as a triangular range: (lowest, highest, most likely)
INPUTS = {
    "hledanost": (4000, 12000, 7000),   # searches per month for the topic
    "p_top10": 0.4,                      # reference class: 2 of 5 similar pages reached the top 10
    "ctr_top": (0.04, 0.20, 0.08),       # CTR when the page is in the top 10
    "ctr_out": (0.0, 0.01, 0.003),       # CTR when it is not
    "proklik": (0.15, 0.35, 0.22),       # visit -> click to a lender
    "schvaleni": (0.04, 0.12, 0.06),     # click -> approved loan
    "provize": (500, 1500, 900),         # Kč per approved loan
}
SENSITIVITY = (("hledanost", "Hledanost"), ("ctr_top", "CTR v top 10"), ("proklik", "Proklik na partnera"),
               ("schvaleni", "Schválení žádosti"), ("provize", "Provize"))


def tri(t):
    lo, hi, mode = t
    return random.triangular(lo, hi, mode)


def q_tri(u, t):
    """Quantile u of a triangular distribution (lo, hi, mode)."""
    a, b, c = t
    fc = (c - a) / (b - a)
    return a + math.sqrt(u * (b - a) * (c - a)) if u < fc else b - math.sqrt((1 - u) * (b - a) * (b - c))


def pct(xs, p):
    s = sorted(xs)
    k = (len(s) - 1) * p
    f, c = math.floor(k), math.ceil(k)
    return s[f] + (s[c] - s[f]) * (k - f)


def yearly(h, ctr, pk, sch, prov):
    return h * 12 * ctr * pk * sch * prov


def simulate(inputs, n, seed):
    """Yearly benefit in Kč for n random scenarios (same draw order as the talk's demo script)."""
    random.seed(seed)
    vals = []
    for _ in range(n):
        top = random.random() < inputs["p_top10"]
        ctr = tri(inputs["ctr_top"]) if top else tri(inputs["ctr_out"])
        vals.append(yearly(tri(inputs["hledanost"]), ctr, tri(inputs["proklik"]), tri(inputs["schvaleni"]),
                           tri(inputs["provize"])))
    return vals


def sensitivity(inputs):
    """Expected yearly value with every input at its median, moving one input to its 10th and 90th percentile."""
    med = {k: q_tri(.5, inputs[k]) for k in ("hledanost", "ctr_top", "ctr_out", "proklik", "schvaleni", "provize")}

    def ev(p=inputs["p_top10"], **over):
        m = {**med, **over}
        return m["hledanost"] * 12 * m["proklik"] * m["schvaleni"] * m["provize"] * (p * m["ctr_top"] + (1 - p) * m["ctr_out"])

    rows = [("Dostaneme se do top 10? (ne / ano)", ev(p=0), ev(p=1))]
    rows += [(name, ev(**{k: q_tri(.1, inputs[k])}), ev(**{k: q_tri(.9, inputs[k])})) for k, name in SENSITIVITY]
    return ev(), sorted(rows, key=lambda r: r[2] - r[1], reverse=True)


def proc(x, dec=0):
    return f"{x * 100:.{dec}f}".replace(".", ",") + " %"


def tis(x):
    return f"{x / 1000:,.1f}".replace(",", " ").replace(".", ",") + " tis. Kč"


def histogram_svg(vals, marks, width=760, height=260, top=250_000, step=10_000):
    bins = top // step + 1
    counts = [0] * bins
    for v in vals:
        counts[min(int(v // step), bins - 1)] += 1
    cmax = max(counts)
    bw = width / bins
    bars = "".join(f'<rect x="{i * bw + 1:.1f}" y="{height - 30 - (height - 50) * c / cmax:.1f}" width="{bw - 2:.1f}" '
                   f'height="{(height - 50) * c / cmax:.1f}" fill="#E5712C" opacity=".85"/>' for i, c in enumerate(counts))
    lines = "".join(f'<line x1="{width * min(x, top) / (top + step):.1f}" y1="14" x2="{width * min(x, top) / (top + step):.1f}" '
                    f'y2="{height - 30}" stroke="#202020" stroke-dasharray="4 4"/><text x="{width * min(x, top) / (top + step) + 4:.1f}" '
                    f'y="12" font-size="12">{html.escape(t)}</text>' for x, t in marks)
    ticks = "".join(f'<text x="{width * t / (top + step):.1f}" y="{height - 10}" font-size="11" text-anchor="middle">'
                    f'{t // 1000}</text>' for t in range(0, top, 50_000))
    return (f'<svg viewBox="0 0 {width} {height}" width="100%" role="img" aria-label="Rozdělení ročního přínosu">'
            f'{bars}{lines}{ticks}<text x="{width}" y="{height - 10}" font-size="11" text-anchor="end">tis. Kč za rok</text></svg>')


def main():
    vals = simulate(INPUTS, N, SEED)
    cost = HOURS * RATE
    guess = yearly(INPUTS["hledanost"][2], INPUTS["ctr_top"][2], INPUTS["proklik"][2], INPUTS["schvaleni"][2],
                   INPUTS["provize"][2])
    p10, p50, p90, mean = pct(vals, .1), pct(vals, .5), pct(vals, .9), sum(vals) / N
    below_cost = sum(v < cost for v in vals) / N
    base, sens = sensitivity(INPUTS)

    print("Ilustrační čísla, cleverpujcky.cz, stránka „půjčka na auto“")
    print(f"Číslo z hlavy (vše nejčastější a stránka v top 10): {tis(guess)}")
    print(f"10 000 scénářů: P10 {tis(p10)}, P50 {tis(p50)}, P90 {tis(p90)}, průměr {tis(mean)}")
    print(f"Náklady {tis(cost)}, šance, že se do roka nevrátí: {proc(below_cost, 1)}")
    print("Citlivost (očekávaná hodnota při 10. a 90. percentilu vstupu):")
    for name, lo, hi in sens:
        print(f"  {name}: {tis(lo)} až {tis(hi)}")

    n_txt = f"{N:,}".replace(",", " ")
    rows = "".join(f"<tr><td>{html.escape(n)}</td><td>{tis(lo)}</td><td>{tis(hi)}</td></tr>" for n, lo, hi in sens)
    OUT.write_text(f"""<!doctype html><html lang="cs"><meta charset="utf-8"><title>Půjčka na auto: simulace přínosu</title>
<style>body{{font-family:system-ui,sans-serif;max-width:820px;margin:32px auto;padding:0 16px;color:#1a1a1a}}
td,th{{padding:4px 10px;border-bottom:1px solid #eee;text-align:left}} .note{{color:#666;font-size:14px}}</style>
<h1>Půjčka na auto: kolik přinese za rok?</h1>
<p class="note">Ilustrační čísla vymyšlená pro přednášku. {n_txt} simulovaných scénářů, pevný seed {SEED}.</p>
<p><b>80 % scénářů: {tis(p10)} až {tis(p90)}</b>, nejčastěji kolem {tis(p50)}, průměr {tis(mean)}.<br>
Číslo z hlavy: {tis(guess)}. Šance, že se náklady {tis(cost)} do roka nevrátí: {proc(below_cost)}.</p>
{histogram_svg(vals, [(guess, "číslo z hlavy"), (cost, "náklady")])}
<h2>Co nejvíc hýbe výsledkem</h2><table><tr><th>Předpoklad</th><th>nízko</th><th>vysoko</th></tr>{rows}</table>
<p>Rozhodnutí: nejvíc záleží na tom, jestli se stránka dostane do top 10. Ověř to nejdřív levně, třeba menším testovacím článkem.</p>
</html>""", encoding="utf-8")
    print(f"Výstup: {OUT}")


if __name__ == "__main__":
    main()
