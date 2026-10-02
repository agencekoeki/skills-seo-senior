#!/usr/bin/env python3
"""Carte des manques du maillage interne (kit « 7 workflows IA d'un SEO senior »).

Bibliothèque standard uniquement. Lit un export de liens internes : l'export
« Tous les liens entrants » (All Inlinks) de Screaming Frog, ou tout CSV avec
au moins une colonne Source et une colonne Destination (Ancre en option).

    python maillage.py liens.csv --accueil https://www.exemple.fr/
    python maillage.py liens.csv --accueil https://www.exemple.fr/ --pages sitemap.txt --cibles cibles.txt

--pages  : la liste des pages qui devraient exister (sitemap, export « Internal HTML »),
           une URL par ligne ou un CSV avec une colonne Address/URL. Sans elle, les
           orphelines ne peuvent pas être trouvées : une orpheline n'apparaît pas dans
           un export de liens, par définition.
--cibles : les pages qui doivent ranker, une URL par ligne.

Sortie : un rapport Markdown. Il montre des faits de crawl ; les décisions restent à prendre.
"""
import argparse
import collections
import csv
import io
import re
import sys
from urllib.parse import urlsplit, urlunsplit

VIDES = {"cliquez ici", "cliquez-ici", "ici", "en savoir plus", "lire la suite", "voir plus", "plus", "click here",
         "read more", "learn more", "here", "more", "découvrir", "decouvrir", "voir"}
SANS_ENJEU = re.compile(r"(mentions|legal|cgv|cgu|conditions|cookie|confidentialit|privacy|login|connexion|compte|account|panier|cart|checkout|wp-login|feed)", re.I)


def read_text(path):
    raw = open(path, "rb").read()
    for enc in ("utf-8-sig", "utf-16", "cp1252", "latin-1"):
        try:
            t = raw.decode(enc)
            if "\x00" not in t:
                return t
        except UnicodeDecodeError:
            pass
    raise SystemExit(f"Encodage illisible : {path}")


def rows_of(path):
    text = read_text(path)
    try:
        dialect = csv.Sniffer().sniff(text[:5000], delimiters=",;\t")
    except csv.Error:
        dialect = csv.excel
    return list(csv.DictReader(io.StringIO(text), dialect=dialect))


def norm(url):
    url = (url or "").strip()
    if not url:
        return ""
    p = urlsplit(url)
    path = p.path or "/"
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), path, p.query, ""))


def col(fieldnames, *cands):
    low = {f.lower().strip(): f for f in fieldnames or []}
    for c in cands:
        for k, v in low.items():
            if k == c or k.startswith(c):
                return v
    return None


def load_list(path):
    if path is None:
        return []
    text = read_text(path)
    first = text.splitlines()[0] if text.strip() else ""
    if any(sep in first for sep in (",", ";", "\t")) and not first.startswith("http"):
        rows = rows_of(path)
        c = col(rows[0].keys() if rows else [], "address", "adresse", "url", "loc", "page")
        return [norm(r[c]) for r in rows if c and r.get(c)]
    return [norm(l) for l in text.splitlines() if l.strip().startswith("http")]


def table(head, lines):
    s = "| " + " | ".join(head) + " |\n|" + "---|" * len(head) + "\n"
    return s + "".join("| " + " | ".join(str(x) for x in l) + " |\n" for l in lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("liens")
    ap.add_argument("--accueil", help="URL de la page d'accueil, pour calculer la profondeur de clic")
    ap.add_argument("--pages", help="liste des pages qui devraient exister (pour trouver les orphelines)")
    ap.add_argument("--cibles", help="pages qui doivent ranker")
    ap.add_argument("--top", type=int, default=15)
    a = ap.parse_args()

    rows = rows_of(a.liens)
    if not rows:
        raise SystemExit("Export de liens vide.")
    f = rows[0].keys()
    c_src, c_dst = col(f, "source", "from", "origine"), col(f, "destination", "to", "cible", "target url")
    c_anc, c_type = col(f, "anchor", "ancre", "texte d'ancre"), col(f, "type")
    c_follow, c_pos = col(f, "follow"), col(f, "link position", "position du lien")
    if not c_src or not c_dst:
        raise SystemExit("Colonnes Source et Destination introuvables. En-têtes lus : " + " | ".join(f))

    edges, anchors, positions = set(), collections.defaultdict(list), collections.defaultdict(collections.Counter)
    ignores = collections.Counter()
    hosts = collections.Counter(urlsplit(norm(r[c_src])).netloc for r in rows if r.get(c_src))
    host = hosts.most_common(1)[0][0] if hosts else ""
    for r in rows:
        s, d = norm(r.get(c_src)), norm(r.get(c_dst))
        if not s or not d or s == d:
            continue
        if c_type and r.get(c_type) and r[c_type].strip().lower() not in ("hyperlink", "lien hypertexte", "ahref", "a"):
            ignores["autre type que lien"] += 1
            continue
        if c_follow and str(r.get(c_follow, "")).strip().lower() in ("false", "faux", "nofollow", "0"):
            ignores["nofollow"] += 1
            continue
        if urlsplit(d).netloc != host:
            continue
        edges.add((s, d))
        anchors[d].append((r.get(c_anc) or "").strip().lower() if c_anc else "")
        if c_pos and r.get(c_pos):
            positions[d][r[c_pos].strip()] += 1

    inlinks = collections.Counter(d for _, d in edges)
    graph = collections.defaultdict(set)
    for s, d in edges:
        graph[s].add(d)

    depth = {}
    if a.accueil:
        start = norm(a.accueil)
        depth[start] = 0
        queue = collections.deque([start])
        while queue:
            u = queue.popleft()
            for v in graph.get(u, ()):
                if v not in depth:
                    depth[v] = depth[u] + 1
                    queue.append(v)

    pages = load_list(a.pages)
    cibles = load_list(a.cibles)
    known = set(pages) | set(inlinks) | {s for s, _ in edges}

    print("# Carte du maillage interne\n")
    print("## Ce que cet export permet d'affirmer\n")
    print(f"- {len(edges)} liens internes uniques (source → destination) vers {len(inlinks)} pages, domaine `{host}`.")
    if ignores:
        print("- Écartés : " + ", ".join(f"{n} {k}" for k, n in ignores.items()) + ".")
    if not a.pages:
        print("- **Pas de liste de pages (`--pages`) : les orphelines ne peuvent pas être trouvées.** Une page que rien ne lie n'apparaît pas dans un export de liens.")
    if not a.accueil:
        print("- Pas d'URL d'accueil (`--accueil`) : la profondeur de clic n'est pas calculée.")
    print()

    if pages:
        orph = [p for p in pages if inlinks.get(p, 0) == 0 and p != norm(a.accueil or "")]
        print(f"## Orphelines ({len(orph)} sur {len(pages)} pages listées)\n")
        print("\n".join(f"- {p}" for p in orph[: a.top * 2]) or "Aucune.")
        print("\nUne orpheline se rattache, ou s'assume comme volontairement isolée. Elle ne se laisse pas par oubli.\n")

    if depth:
        deep = sorted((d, p) for p, d in depth.items() if d >= 4)
        unreached = [p for p in known if p not in depth and p != norm(a.accueil)]
        print(f"## Profondeur de clic depuis l'accueil\n")
        hist = collections.Counter(min(d, 6) for d in depth.values())
        print("Pages par profondeur : " + ", ".join(f"{'6 et plus' if k == 6 else k} : {n}" for k, n in sorted(hist.items())) + ".")
        if deep:
            print(f"\n{len(deep)} pages à 4 clics ou plus. Les plus profondes :\n")
            print(table(["Page", "Profondeur"], [[p, d] for d, p in deep[-a.top:][::-1]]))
        if unreached:
            print(f"{len(unreached)} pages connues ne sont pas atteignables en suivant les liens depuis l'accueil.\n")

    if cibles:
        print("## Les pages qui doivent ranker\n")
        lines = []
        for p in cibles:
            an = [x for x in anchors.get(p, []) if x]
            top_share = ""
            if an:
                mc, n = collections.Counter(an).most_common(1)[0]
                top_share = f"« {mc} » {round(100 * n / len(an))} %"
            vides = sum(1 for x in an if x in VIDES)
            pos = positions.get(p, {})
            contenu = sum(n for k, n in pos.items() if k.lower() in ("content", "contenu")) if pos else "?"
            signal = []
            if inlinks.get(p, 0) == 0:
                signal.append("aucun lien")
            if p in depth and depth[p] >= 4:
                signal.append("trop profonde")
            if pos and isinstance(contenu, int) and contenu < 3:
                signal.append("peu de liens en contenu")
            if an and collections.Counter(an).most_common(1)[0][1] / len(an) > 0.6 and len(an) >= 5:
                signal.append("ancre répétée")
            if vides:
                signal.append(f"{vides} ancre(s) vide(s)")
            lines.append([p, inlinks.get(p, 0), contenu, depth.get(p, "?"), len(set(an)), top_share, ", ".join(signal) or "ok"])
        print(table(["Page cible", "Pages qui la lient", "Liens en contenu", "Profondeur", "Ancres distinctes", "Ancre dominante", "Signaux"], lines))

    print("## Où va l'autorité interne\n")
    top = inlinks.most_common(a.top)
    print(table(["Page", "Pages qui la lient", "Sans enjeu ?"], [[p, n, "oui" if SANS_ENJEU.search(p) else ""] for p, n in top]))
    print("Les pages qui reçoivent le plus de liens sont souvent celles des menus. Si des pages sans enjeu sont en tête et que les cibles sont loin derrière, l'autorité fuit.\n")
    print("---\nCe rapport montre des faits de crawl. Le plan de liens (depuis quelle page, vers quelle page, avec quelle ancre) se décide avec SKILL.md.")


if __name__ == "__main__":
    main()
