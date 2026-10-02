#!/usr/bin/env python3
"""Lectures 0 à 3 d'un export Search Console (kit « 7 workflows IA d'un SEO senior »).

Bibliothèque standard uniquement. Lit un export CSV de l'onglet Requêtes ou Pages,
en français ou en anglais, avec ou sans la comparaison de périodes.

    python gsc_lectures.py export.csv
    python gsc_lectures.py export.csv --total-impressions 184000 --min-clics 50 --top 20

Sortie : un rapport Markdown. Le script sort des lignes, pas des décisions :
les causes proposées sont des hypothèses (PENSER) à confirmer.
"""
import argparse
import csv
import io
import re
import statistics
import sys

PREVIOUS = ("previous", "précédent", "precedent", "précédente", "avant", "prior")


def read_text(path):
    raw = open(path, "rb").read()
    for enc in ("utf-8-sig", "utf-16", "cp1252", "latin-1"):
        try:
            text = raw.decode(enc)
            if "\x00" in text:
                continue
            return text
        except UnicodeDecodeError:
            continue
    raise SystemExit("Encodage illisible : réexporte le fichier en CSV.")


def sniff_rows(text):
    sample = text[:5000]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
    except csv.Error:
        dialect = csv.excel
    return [r for r in csv.reader(io.StringIO(text), dialect) if any(c.strip() for c in r)]


def metric_of(header):
    h = header.lower()
    if "clic" in h or "click" in h:
        return "clics"
    if "impression" in h:
        return "impressions"
    if "ctr" in h:
        return "ctr"
    if "position" in h:
        return "position"
    return None


def to_number(value, metric):
    v = (value or "").strip().replace(" ", "").replace("\xa0", "").replace(" ", "").replace("%", "")
    if v in ("", "-", "\u2014"):
        return None
    if "," in v and "." in v:
        v = v.replace(",", "") if v.rfind(".") > v.rfind(",") else v.replace(".", "").replace(",", ".")
    elif "," in v:
        if metric in ("clics", "impressions") and re.fullmatch(r"\d{1,3}(,\d{3})+", v):
            v = v.replace(",", "")
        else:
            v = v.replace(",", ".")
    try:
        return float(v)
    except ValueError:
        return None


def load(path):
    rows = sniff_rows(read_text(path))
    if len(rows) < 2:
        raise SystemExit("Fichier vide ou sans ligne de données.")
    header, data = rows[0], rows[1:]
    cols = {}
    for i, h in enumerate(header[1:], start=1):
        m = metric_of(h)
        if not m:
            continue
        period = "prev" if any(p in h.lower() for p in PREVIOUS) else "cur"
        cols.setdefault((m, period), i)
    if ("clics", "cur") not in cols:
        raise SystemExit("Colonne des clics introuvable. En-têtes lus : " + " | ".join(header))
    out = []
    for r in data:
        if not r or not r[0].strip():
            continue
        item = {"cle": r[0].strip()}
        for (m, p), i in cols.items():
            item[f"{m}_{p}"] = to_number(r[i], m) if i < len(r) else None
        if item.get("ctr_cur") is None and item.get("clics_cur") is not None and item.get("impressions_cur"):
            item["ctr_cur"] = 100 * item["clics_cur"] / item["impressions_cur"]
        elif item.get("ctr_cur") is not None and item["ctr_cur"] <= 1 and (item.get("clics_cur") or 0) > 0:
            # CTR exporté en fraction (0,032) plutôt qu'en pourcentage
            if item.get("impressions_cur") and abs(100 * item["clics_cur"] / item["impressions_cur"] - 100 * item["ctr_cur"]) < 1:
                item["ctr_cur"] *= 100
        out.append(item)
    return header, cols, out


def fmt(x, d=0):
    if x is None:
        return "?"
    return f"{x:,.{d}f}".replace(",", " ").replace(".", ",")


def table(head, lines):
    s = "| " + " | ".join(head) + " |\n|" + "---|" * len(head) + "\n"
    for l in lines:
        s += "| " + " | ".join(l) + " |\n"
    return s


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--total-impressions", type=float, help="total lu en haut du rapport Performance")
    ap.add_argument("--min-clics", type=float, default=50, help="clics minimum sur la période précédente (lecture 1)")
    ap.add_argument("--baisse", type=float, default=25, help="baisse minimum en %% (lecture 1)")
    ap.add_argument("--min-impressions", type=float, default=100, help="impressions minimum (lectures 2 et 3)")
    ap.add_argument("--top", type=int, default=20)
    a = ap.parse_args()

    header, cols, rows = load(a.csv)
    compare = ("clics", "prev") in cols
    tot_clics = sum(r.get("clics_cur") or 0 for r in rows)
    tot_impr = sum(r.get("impressions_cur") or 0 for r in rows)

    print("# Lectures Search Console (0 à 3)\n")
    print("## 0. Ce que cet export permet d'affirmer\n")
    print(f"- Fichier : `{a.csv}`, {len(rows)} lignes, première colonne « {header[0]} ».")
    print(f"- Comparaison de périodes : {'oui' if compare else 'non (la lecture 1 est impossible : réexporter avec « Comparer » activé)'}.")
    if len(rows) >= 1000:
        print("- **Plafond de 1 000 lignes atteint** : c'est la tête de courbe, pas un échantillon. La longue traîne est invisible ici (API ou export BigQuery si l'enjeu le mérite).")
    print(f"- Dans le fichier : {fmt(tot_clics)} clics, {fmt(tot_impr)} impressions sur la période en cours.")
    if a.total_impressions:
        part = 100 * tot_impr / a.total_impressions if a.total_impressions else 0
        print(f"- Le fichier couvre {fmt(part, 1)} % des impressions du rapport. Le reste est anonymisé ou au-delà du plafond.")
    print("- À vérifier dans l'interface, que ce fichier ne dit pas : type de propriété (domaine ou préfixe d'URL), derniers jours provisoires, anomalies de données déclarées par Google.\n")

    if compare:
        print(f"## 1. Ce qui saigne (au moins {fmt(a.min_clics)} clics avant, baisse d'au moins {fmt(a.baisse)} %)\n")
        bleed = []
        for r in rows:
            p, c = r.get("clics_prev"), r.get("clics_cur")
            if p is None or c is None or p < a.min_clics:
                continue
            delta = 100 * (c - p) / p
            if delta > -a.baisse:
                continue
            pp, pc = r.get("position_prev"), r.get("position_cur")
            ip, ic = r.get("impressions_prev"), r.get("impressions_cur")
            if pp is not None and pc is not None and pc - pp >= 2:
                piste = "position perdue"
            elif ip and ic is not None and (ic - ip) / ip <= -0.2:
                piste = "demande en baisse (saison ?)"
            elif pp is not None and pc is not None:
                piste = "position quasi stable : SERP changée ou clic capté ?"
            else:
                piste = "à trancher"
            bleed.append((p - c, [r["cle"], fmt(p), fmt(c), fmt(delta) + " %", f"{fmt(pp, 1)} → {fmt(pc, 1)}", piste]))
        bleed.sort(key=lambda x: -x[0])
        if bleed:
            print(table(["Élément", "Clics avant", "Clics maintenant", "Écart", "Position", "Piste (PENSER)"], [b[1] for b in bleed[: a.top]]))
            print("Les pistes sont des hypothèses. Une baisse de clics à position égale désigne la SERP, pas le site.\n")
        else:
            print("Rien ne dépasse les seuils.\n")

    print(f"## 2. Ce qui est à portée (positions 8 à 20, au moins {fmt(a.min_impressions)} impressions)\n")
    reach = [r for r in rows if r.get("position_cur") is not None and 8 <= r["position_cur"] <= 20 and (r.get("impressions_cur") or 0) >= a.min_impressions]
    reach.sort(key=lambda r: -(r.get("impressions_cur") or 0))
    if reach:
        print(table(["Élément", "Position", "Impressions", "Clics", "Valeur business (à remplir)"], [[r["cle"], fmt(r["position_cur"], 1), fmt(r.get("impressions_cur")), fmt(r.get("clics_cur")), ""] for r in reach[: a.top]]))
        print("Ce tri par impressions est provisoire : retrie par valeur business avant de décider.\n")
    else:
        print("Aucune ligne dans cette zone, ou pas de colonne Position.\n")

    print("## 3. La promesse SERP (CTR très en dessous de la courbe de CE site)\n")
    buckets = {}
    for r in rows:
        pos, ctr, imp = r.get("position_cur"), r.get("ctr_cur"), r.get("impressions_cur") or 0
        if pos is None or ctr is None or imp < a.min_impressions or pos > 20:
            continue
        buckets.setdefault(max(1, round(pos)), []).append(ctr)
    curve = {b: statistics.median(v) for b, v in buckets.items() if len(v) >= 5}
    if not curve:
        print("Pas assez de lignes pour dessiner la courbe du site (au moins 5 par position). Lecture impossible sur cet export.\n")
    else:
        print("Courbe du site (CTR médian par position arrondie) : " + ", ".join(f"pos {b} : {fmt(curve[b], 1)} %" for b in sorted(curve)) + "\n")
        weak = []
        for r in rows:
            pos, ctr, imp = r.get("position_cur"), r.get("ctr_cur"), r.get("impressions_cur") or 0
            if pos is None or ctr is None or imp < a.min_impressions:
                continue
            b = max(1, round(pos))
            if b in curve and curve[b] > 0 and ctr < 0.5 * curve[b]:
                weak.append((imp, [r["cle"], fmt(pos, 1), fmt(ctr, 1) + " %", fmt(curve[b], 1) + " %", fmt(imp)]))
        weak.sort(key=lambda x: -x[0])
        if weak:
            print(table(["Élément", "Position", "CTR", "CTR médian du site à cette position", "Impressions"], [w[1] for w in weak[: a.top]]))
            print("Deux diagnostics possibles, à trancher ligne par ligne : la promesse est mauvaise (title et description), ou le clic n'est plus l'issue de cette SERP (voir seo-valeur-du-trafic).\n")
        else:
            print("Aucune ligne sous la moitié de la courbe du site.\n")

    print("---\nLectures 4 à 6 (cannibalisation, indexation, zéro-clic) : elles demandent l'interface ou d'autres exports, voir SKILL.md.")


if __name__ == "__main__":
    main()
