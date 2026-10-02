# Installer les skills SEO senior

## Avant tout

- **Claude :** l'exécution de code activée dans les réglages (sans elle, les compétences apparaissent grisées ; dans une organisation, c'est le propriétaire du compte qui l'active).
- **Les scripts** (`seo-search-console`, `seo-maillage-interne`) n'ont besoin que de Python 3, sans bibliothèque supplémentaire. Sans exécution de code, les skills fonctionnent quand même : l'IA fait les calculs à la main.

## 1. Claude Desktop, claude.ai, Cowork : par la place de marché (recommandé)

1. Ouvre **Personnaliser**, puis l'onglet **Plugins**. Pas l'onglet des connecteurs : son bouton d'ajout demande l'adresse d'un serveur MCP.
2. Clique sur **Ajouter** (ou **+**), puis **Ajouter une place de marché** › **Ajouter à partir d'un référentiel**, colle `https://github.com/agencekoeki/skills-seo-senior`, puis **Sync**.
3. Sur la ligne **SEO senior**, clique sur **Ajouter** : le plugin doit annoncer 9 compétences.

Les intitulés des menus changent d'une version de l'application à l'autre. Si tu ne trouves pas le menu, passe par les fichiers : le résultat est le même, seules les mises à jour se font à la main.

## 2. claude.ai, par fichiers

1. Télécharge les neuf `.zip` de la [dernière version](https://github.com/agencekoeki/skills-seo-senior/releases/latest). Pas les archives « Source code » : c'est le dépôt entier.
2. Dans **Personnaliser › Compétences**, importe-les un par un, sans les décompresser.
3. À chaque nouvelle version, supprime les anciens et importe les nouveaux.

## 3. Claude Code

```
/plugin marketplace add agencekoeki/skills-seo-senior
/plugin install seo-senior@sebastien-grillot-seo
```

Les skills apparaissent avec le préfixe du plugin dans le menu « / » (par exemple `seo-senior:seo-search-console`) : c'est normal.

## 4. Codex et Gemini CLI

```bash
git clone https://github.com/agencekoeki/skills-seo-senior.git
mkdir -p ~/.agents/skills && cp -r skills-seo-senior/skills/* ~/.agents/skills/
```

- **Codex** lit `~/.agents/skills/` (et `.agents/skills/` dans un projet). Redémarre Codex si un skill n'apparaît pas.
- **Gemini CLI** lit `~/.agents/skills/` et `~/.gemini/skills/`. Il sait aussi installer depuis le dépôt : `gemini skills install https://github.com/agencekoeki/skills-seo-senior.git`.

## 5. ChatGPT

Les skills sont proposés dans ChatGPT Business, Enterprise, Edu et Healthcare, selon les réglages de l'espace de travail. **Skills › Créer › Importer depuis ton ordinateur**, avec les `.zip` de la dernière version. Pas disponible à ce jour dans ChatGPT Plus ni Pro.

## Premier pas

Demande simplement ce que tu veux faire : « voici l'export Search Console de mon client, on a perdu du trafic », ou « mon client veut renommer ses URLs, tu en penses quoi ? ». L'aiguilleur choisit le skill et l'annonce en une ligne.

## Dépannage

| Ce que tu vois | Ce que ça veut dire | Quoi faire |
|---|---|---|
| les compétences sont grisées | l'exécution de code est désactivée | l'activer dans les réglages |
| les skills portent un préfixe dans le menu « / » | ils sont installés en plugin | c'est normal |
| un skill ne se déclenche pas | la demande ne ressemble pas à sa description | nomme-le : « applique seo-cluster » |
| le script refuse l'export | en-têtes inattendus | il affiche les en-têtes lus ; réexporte en CSV depuis l'interface |

## Mettre à jour

- **Place de marché :** dans Claude Desktop et sur claude.ai, par la synchronisation de la place de marché. Dans Claude Code : `claude plugin marketplace update sebastien-grillot-seo`, puis `claude plugin update seo-senior@sebastien-grillot-seo`.
- **Fichiers :** réimporte les `.zip` de la [dernière version](https://github.com/agencekoeki/skills-seo-senior/releases/latest).
- **Codex, Gemini CLI :** `git pull` dans le dépôt cloné, puis recopie le dossier `skills/`.
