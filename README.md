# Skills SEO senior

**Neuf skills qui n'apprennent pas le SEO à ton IA. Ils lui apprennent à juger avant d'exécuter.**

[![Version](https://img.shields.io/github/v/release/agencekoeki/skills-seo-senior?label=version)](https://github.com/agencekoeki/skills-seo-senior/releases/latest)
[![Contrôle](https://github.com/agencekoeki/skills-seo-senior/actions/workflows/controle.yml/badge.svg)](https://github.com/agencekoeki/skills-seo-senior/actions/workflows/controle.yml)
[![Licence GPL 3.0](https://img.shields.io/badge/licence-GPL%203.0-blue)](LICENSE)
![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-555)
![Claude · Codex · Gemini CLI](https://img.shields.io/badge/pour-Claude%20%C2%B7%20Codex%20%C2%B7%20Gemini%20CLI-555)

> Par **Sébastien Grillot**, consultant SEO depuis 2009, fondateur de [Kōcori](https://www.kocori.co) et cofondateur de Kōeki.
> La version skills du kit PDF « 7 workflows IA d'un SEO senior ».

## Le problème que ces skills règlent

Demande un audit SEO à une IA : elle te sort tout. Les balises, les 404, les « opportunités de mots-clés ». Bien rangé, bien formaté. Et lundi matin, tu ne sais toujours pas quoi faire.

L'IA répond comme un développeur : **à la lettre**. Tu lui demandes « renomme mes URLs », elle te livre un plan de renommage. Le SEO senior, lui, demande d'abord ce qui va casser.

Ces skills ne sont pas des checklists. Chacun installe dans l'IA **une manière de penser** :

- **une question centrale**, celle qu'un senior se pose avant de toucher à quoi que ce soit ;
- **un questionnement dans un ordre précis**, parce que l'ordre change la décision ;
- **les pièges**, avec le signe qui les trahit et ce qu'ils coûtent ;
- **des garde-fous**, ce que l'IA ne doit pas faire, même si on le lui demande ;
- **des enchaînements**, vers le skill suivant quand le problème change de nature ;
- **une discipline de preuve**, qui sépare ce que l'IA **sait** (sourcé, daté) de ce qu'elle **pense** (déduit), et qui finit par une décision.

## Les neuf skills

| Skill | Tu dis | Tu obtiens |
|---|---|---|
| **seo-aiguilleur** | « regarde ce dossier », « par où je commence ? » | le bon raisonnement choisi, annoncé en une ligne |
| **seo-savoir-penser** | (s'applique tout seul dès qu'il y a un chiffre ou un audit) | ce qui est su, ce qui est supposé, ce qui manque, et une décision |
| **seo-demande-client** | « mon client veut renommer ses URLs » | ce qu'il dit, ce qu'il veut vraiment, ce qui va casser, par où entrer |
| **seo-valeur-du-trafic** | « ça vaut le coup de créer cette page ? » | chaque requête classée : clic vivant ou siphonné, intention qui rapporte ou qui informe |
| **seo-gagnabilite-serp** | « peut-on se positionner sur ce mot-clé ? » | prenable, imprenable ou prenable par un angle, et le format de page à produire |
| **seo-search-console** | « voici notre export, on a perdu du trafic » | six lectures, une page de décisions ; un script fait les calculs |
| **seo-cluster** | « quel plan de contenu sur ce thème ? » | un pilier, des satellites, une question par page, zéro cannibalisation |
| **seo-maillage-interne** | « nos pages sont mal reliées » | la carte des manques et un plan de liens ; un script lit ton crawl |
| **seo-citabilite-geo** | « les IA ne parlent pas de nous » | six leviers diagnostiqués, et un protocole de mesure honnête |

Les skills se chargent **tout seuls**, d'après ce que tu demandes. Tu n'as pas à les appeler.

## Installer

Le détail, avec le dépannage, est dans [docs/installer.md](docs/installer.md).

### Claude (claude.ai, Claude Desktop, Cowork) : par la place de marché

1. Ouvre **Personnaliser**, puis l'onglet **Plugins**.
2. **Ajouter une place de marché** › **Ajouter à partir d'un référentiel**, colle `https://github.com/agencekoeki/skills-seo-senior`, puis **Sync**.
3. Sur la ligne **SEO senior**, clique sur **Ajouter** : le plugin annonce 9 compétences.

Il faut l'exécution de code activée dans les réglages de Claude.

### Claude, par fichiers

Télécharge les `.zip` de la [dernière version](https://github.com/agencekoeki/skills-seo-senior/releases/latest) (un par skill), puis importe-les un par un dans **Personnaliser › Compétences**, sans les décompresser.

### Claude Code

```
/plugin marketplace add agencekoeki/skills-seo-senior
/plugin install seo-senior@sebastien-grillot-seo
```

### Codex (OpenAI) et Gemini CLI (Google)

Les skills suivent le standard ouvert **Agent Skills** : le même dossier fonctionne ailleurs que chez Claude.

```bash
git clone https://github.com/agencekoeki/skills-seo-senior.git
mkdir -p ~/.agents/skills && cp -r skills-seo-senior/skills/* ~/.agents/skills/
```

`~/.agents/skills/` est lu par Codex et par Gemini CLI. Avec Gemini CLI, tu peux aussi faire `gemini skills install https://github.com/agencekoeki/skills-seo-senior.git`.

### ChatGPT

Les skills existent dans ChatGPT Business, Enterprise et Edu (pas dans Plus ni Pro, à ce jour) : **Skills › Créer › Importer depuis ton ordinateur**, avec les `.zip` de la dernière version.

## Ce que ce kit ne couvre pas

Performance et Core Web Vitals, migration et plan de redirections, netlinking, E-E-A-T et sujets YMYL, mesure après le clic (GA4). Si ta demande y tombe, l'aiguilleur te le dit au lieu d'improviser une méthode.

## Le kit PDF

Les mêmes sept réflexes existent en version prompts à coller, dans le PDF « 7 workflows IA d'un SEO senior », avec une page à donner directement à ton IA. Il est distribué depuis [kocori.co](https://www.kocori.co).

## Pour une équipe

Ces neuf skills sont la version courte. La bibliothèque complète de Kōeki dépasse les vingt-cinq skills SEO, avec leurs enchaînements. Construire la même pour une agence ou une équipe, sur ses cas réels, c'est l'objet des formations de Sébastien Grillot : écris-lui sur [LinkedIn](https://www.linkedin.com/in/sebastiengrillot).

## Licence

GPL 3.0 : tu peux utiliser, modifier et redistribuer ces skills, à condition de garder la même licence et de citer l'auteur. Texte complet dans [LICENSE](LICENSE).

---

Projet indépendant. Claude est une marque d'Anthropic ; ChatGPT et Codex, d'OpenAI ; Gemini, Search Console et AI Overviews, de Google. Ce projet n'est ni affilié à ces sociétés, ni approuvé par elles.
