#!/usr/bin/env python3
"""Example 3: where to put the next 40 hours? Three projects compared by payback, risk and value per hour.

Projects: the "půjčka na auto" page (example 1), a better loan calculator, a series of financial-literacy articles.
All numbers are ILLUSTRATIVE (made up for the talk, website cleverpujcky.cz). Standard library only, fixed seeds,
the car page reuses the exact scenarios of example 1.

Run:  python3 porovnani.py
Writes vysledek.html next to this script.
"""
import html
import math
import random
from pathlib import Path

SEED = 2026
N = 10_000
MONTHS = 24
RATE = 800  # Kč per hour of own work
CAPACITY = 40  # hours available
OUT = Path(__file__).resolve().parent / "vysledek.html"

AUTO = {  # same inputs as example 1
    "hledanost": (4000, 12000, 7000), "p_top10": 0.4, "ctr_top": (0.04, 0.20, 0.08), "ctr_out": (0.0, 0.01, 0.003),
    "proklik": (0.15, 0.35, 0.22), "schvaleni": (0.04, 0.12, 0.06), "provize": (500, 1500, 900),
    "hodiny": 25, "nabeh": (2, 8, 4),  # months until full effect
}
PROJECTS = {
    "kalkulacka": {"hodiny": 15, "p": 0.85, "mesicne": (1500, 4000, 2500), "start": 2},  # works from month 2
    "gramotnost": {"hodiny": 40, "p": 0.50, "mesicne": (1000, 6000, 2500), "nabeh": (6, 12, 9)},
}
NAMES = {"auto": "Půjčka na auto", "kalkulacka": "Kalkulačka", "gramotnost": "Finanční gramotnost"}
COLORS = {"auto": "#E5712C", "kalkulacka": "#5E8C2A", "gramotnost": "#4a4a48"}


def tri(t):
    lo, hi, mode = t
    return random.triangular(lo, hi, mode)


def pct(xs, p):
    s = sorted(xs)
    k = (len(s) - 1) * p
    f, c = math.floor(k), math.ceil(k)
    return s[f] + (s[c] - s[f]) * (k - f)


def car_yearly(n, seed):
    """Yearly benefit of the car page, identical draws to example 1."""
    random.seed(seed)
    vals = []
    for _ in range(n):
        top = random.random() < AUTO["p_top10"]
        ctr = tri(AUTO["ctr_top"]) if top else tri(AUTO["ctr_out"])
        vals.append(tri(AUTO["hledanost"]) * 12 * ctr * tri(AUTO["proklik"]) * tri(AUTO["schvaleni"]) * tri(AUTO["provize"]))
    return vals


def monthly_runs(car_vals, seed):
    """Monthly revenue of each project in every scenario."""
    random.seed(seed)
    runs = {"auto": [], "kalkulacka": [], "gramotnost": []}
    months = range(1, MONTHS + 1)
    for i in range(N):
        full, ramp = car_vals[i] / 12, tri(AUTO["nabeh"])
        runs["auto"].append([full * min(1, m / ramp) for m in months])
        k = PROJECTS["kalkulacka"]
        works, monthly = random.random() < k["p"], tri(k["mesicne"])
        runs["kalkulacka"].append([monthly if works and m >= k["start"] else 0 for m in months])
        f = PROJECTS["gramotnost"]
        works, monthly, ramp = random.random() < f["p"], tri(f["mesicne"]), tri(f["nabeh"])
        runs["gramotnost"].append([monthly * min(1, m / ramp) if works else 0 for m in months])
    return runs


def summarize(name, runs):
    hours = AUTO["hodiny"] if name == "auto" else PROJECTS[name]["hodiny"]
    cost = hours * RATE
    cum_runs, payback = [], []
    for run in runs:
        acc, cum, pb = -cost, [], None
        for m, v in enumerate(run, 1):
            acc += v
            cum.append(acc)
            if pb is None and acc >= 0:
                pb = m
        cum_runs.append(cum)
        payback.append(pb)
    band = [(pct([c[m] for c in cum_runs], .1), pct([c[m] for c in cum_runs], .5), pct([c[m] for c in cum_runs], .9))
            for m in range(MONTHS)]
    paid = sorted(p for p in payback if p is not None)
    ev = sum(c[-1] for c in cum_runs) / N
    return {"hodiny": hours, "naklady": cost, "nevrati_do_roka": sum(p is None or p > 12 for p in payback) / N,
            "navratnost_median": paid[N // 2] if len(paid) > N // 2 else None, "ev_24m": ev, "ev_za_hodinu": ev / hours,
            "band": band}


def kc(x):
    return f"{round(x, -2) + 0.0:,.0f}".replace(",", " ") + " Kč"  # + 0.0 turns -0.0 into 0.0


def proc(x):
    return f"{x * 100:.0f} %"


def fan_svg(res, width=760, height=300, ymin=-40_000, ymax=120_000):
    xs = lambda m: 50 + (width - 60) * m / MONTHS  # noqa: E731
    ys = lambda v: 20 + (height - 50) * (ymax - min(max(v, ymin), ymax)) / (ymax - ymin)  # noqa: E731
    out = [f'<line x1="50" y1="{ys(0):.1f}" x2="{width - 10}" y2="{ys(0):.1f}" stroke="#202020"/>',
           f'<line x1="{xs(12):.1f}" y1="20" x2="{xs(12):.1f}" y2="{height - 30}" stroke="#999" stroke-dasharray="4 4"/>',
           f'<text x="{xs(12) + 4:.1f}" y="32" font-size="11">rok</text>']
    for v in range(ymin, ymax + 1, 40_000):
        out.append(f'<text x="44" y="{ys(v) + 4:.1f}" font-size="11" text-anchor="end">{v // 1000}</text>')
    for m in (0, 6, 12, 18, 24):
        out.append(f'<text x="{xs(m):.1f}" y="{height - 10}" font-size="11" text-anchor="middle">{m}</text>')
    for name, r in res.items():
        pts = [(0, -r["naklady"], -r["naklady"], -r["naklady"])] + [(m + 1, *b) for m, b in enumerate(r["band"])]
        band = " ".join(f"{xs(m):.1f},{ys(hi):.1f}" for m, lo, md, hi in pts) + " " + " ".join(
            f"{xs(m):.1f},{ys(lo):.1f}" for m, lo, md, hi in reversed(pts))
        med = " ".join(f"{xs(m):.1f},{ys(md):.1f}" for m, lo, md, hi in pts)
        out.append(f'<polygon points="{band}" fill="{COLORS[name]}" opacity=".14"/>'
                   f'<polyline points="{med}" fill="none" stroke="{COLORS[name]}" stroke-width="3"/>')
    return (f'<svg viewBox="0 0 {width} {height}" width="100%" role="img" aria-label="Kumulovaný přínos minus náklady">'
            f'{"".join(out)}</svg>')


def main():
    runs = monthly_runs(car_yearly(N, SEED), SEED + 6)
    res = {name: summarize(name, r) for name, r in runs.items()}

    print("Ilustrační čísla, cleverpujcky.cz, 40 hodin práce")
    for name, r in res.items():
        med = f"{r['navratnost_median']}. měsíc" if r["navratnost_median"] else "nevrátí se do 2 let"
        print(f"{NAMES[name]}: {r['hodiny']} h, náklady {kc(r['naklady'])}, nevrátí se do roka v {proc(r['nevrati_do_roka'])} "
              f"scénářů, návratnost nejspíš: {med}, očekávaný přínos {kc(r['ev_za_hodinu'])} na hodinu")
    print(f"Do {CAPACITY} hodin se vejde auto + kalkulačka (25 + 15 h), nebo celá finanční gramotnost (40 h).")

    rows = "".join(
        f"<tr><td style='color:{COLORS[n]}'><b>{html.escape(NAMES[n])}</b></td><td>{r['hodiny']} h</td>"
        f"<td>{proc(r['nevrati_do_roka'])}</td><td>{r['navratnost_median'] or 'nevrátí se do 2 let'}</td>"
        f"<td>{kc(r['ev_za_hodinu'])}</td></tr>" for n, r in res.items())
    OUT.write_text(f"""<!doctype html><html lang="cs"><meta charset="utf-8"><title>Tři projekty: kdy se vrátí</title>
<style>body{{font-family:system-ui,sans-serif;max-width:820px;margin:32px auto;padding:0 16px;color:#1a1a1a}}
td,th{{padding:4px 10px;border-bottom:1px solid #eee;text-align:left}} .note{{color:#666;font-size:14px}}</style>
<h1>Do čeho dát příštích {CAPACITY} hodin?</h1>
<p class="note">Ilustrační čísla vymyšlená pro přednášku. Čára je medián, pásmo 80 % scénářů, osa v tisících Kč, měsíce 0 až 24.</p>
{fan_svg(res)}
<table><tr><th>Projekt</th><th>Hodiny</th><th>Nevrátí se do roka</th><th>Návratnost (medián, měsíc)</th><th>Očekávaně na hodinu</th></tr>{rows}</table>
<p>Rozhodnutí: kalkulačka je jistá malá výhra, auto velká sázka. Do 40 hodin se vejdou obě. U auta nejdřív levně ověř, jestli se stránka dostane do top 10.</p>
</html>""", encoding="utf-8")
    print(f"Výstup: {OUT}")


if __name__ == "__main__":
    main()
