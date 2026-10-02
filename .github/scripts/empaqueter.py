#!/usr/bin/env python3
"""Fabrique un .zip par skill (dossier du skill à la racine, licence jointe) et les notes de version.

    python3 .github/scripts/empaqueter.py dist
"""
import pathlib
import re
import sys
import zipfile

RACINE = pathlib.Path(__file__).resolve().parents[2]
DEPOT = "https://github.com/agencekoeki/skills-seo-senior"
IGNORES = {"__pycache__", ".DS_Store"}


def main():
    sortie = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    sortie.mkdir(parents=True, exist_ok=True)
    skills = sorted(p.name for p in (RACINE / "skills").iterdir() if (p / "SKILL.md").exists())
    if not skills:
        sys.exit("BLOQUANT  aucun skill trouvé")
    for nom in skills:
        dossier = RACINE / "skills" / nom
        chemin = sortie / f"{nom}.zip"
        with zipfile.ZipFile(chemin, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(dossier.rglob("*")):
                if f.is_file() and not IGNORES & set(f.parts):
                    z.write(f, pathlib.Path(nom) / f.relative_to(dossier))
            z.write(RACINE / "LICENSE", pathlib.Path(nom) / "LICENSE")
        print(f"OK        {nom}.zip")
    journal = (RACINE / "CHANGELOG.md").read_text(encoding="utf-8")
    entree = re.search(r"^## .*?(?=\n## |\Z)", journal, re.M | re.S)
    liens = "\n".join(f"- {n} : [.zip]({DEPOT}/releases/latest/download/{n}.zip)" for n in skills)
    (sortie / "notes.md").write_text(
        (entree.group(0).strip() if entree else "Voir le journal des versions.")
        + "\n\n## Installer par fichiers\n\nImporte chaque .zip dans Personnaliser › Compétences (claude.ai), sans le décompresser.\n\n"
        + liens + "\n",
        encoding="utf-8",
    )
    print("OK        notes.md")


if __name__ == "__main__":
    main()
