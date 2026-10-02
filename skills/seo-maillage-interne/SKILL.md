---
name: seo-maillage-interne
description: Conçoit le maillage interne (les liens entre les pages d'un site, pas la structure des URLs) pour concentrer l'autorité sur les pages qui doivent ranker. Repère les orphelines, les fuites, la profondeur de clic et les ancres, à partir d'un crawl réel, puis livre un plan de liens. À charger dès qu'une demande touche les liens internes, le cocon sémantique, les pages orphelines, la profondeur de clic, les ancres, ou quand l'utilisateur dit « nos pages sont mal reliées », « comment faire circuler le jus », « relie ce cluster », ou joint un export de crawl. Ne pas déclencher pour l'arborescence des URLs ni pour les liens venus d'autres sites (netlinking).
license: GPL-3.0
---

# seo-maillage-interne : les tendons, pas le squelette

**Version 1.0, octobre 2026.** Partie du kit « 7 workflows IA d'un SEO senior » de Sébastien Grillot.

## Pourquoi ce skill existe

L'arborescence dit **où vivent** les pages. Le maillage dit **comment l'autorité circule** entre elles, et comment le crawl les découvre. Ce sont deux compétences, et c'est le piège de ce sujet : on peut avoir une arborescence parfaite et un maillage catastrophique. Une page peut être rangée à la bonne adresse et n'être liée par rien.

Un maillage négligé produit trois effets :

- **des pages orphelines**, qu'aucune page interne ne lie : quasi invisibles au crawl comme à l'internaute, même si elles existent dans le sitemap ;
- **de l'autorité qui stagne ou qui fuit** : elle s'accumule sur l'accueil et ne redescend pas vers les pages qui doivent ranker, ou se disperse vers des pages sans enjeu ;
- **une profondeur excessive** : des pages importantes à quatre ou cinq clics de l'accueil, que les moteurs explorent peu et jugent mineures.

Le cocon sémantique en est la forme aboutie : un réseau de liens qui suit la logique thématique (le pilier et ses satellites se lient entre eux), et qui concentre la pertinence sur les pages cibles.

## La distinction qui passe avant tout

**Structure n'est pas maillage.** Avant tout diagnostic, vérifie qu'on ne confond pas « l'URL est bien rangée » (arborescence) avec « la page est bien reliée à ses voisines » (maillage). Si tu te surprends à parler d'URLs et de silos, tu es dans l'arborescence : ce n'est pas la question de ce skill.

## La question centrale

**Chaque page reçoit-elle du lien depuis les bonnes pages, et en envoie-t-elle vers les bonnes ? Ou est-elle isolée ?**

## Le questionnement

1. **Les orphelines.** Quelles pages ne reçoivent aucun lien interne ? Elles se rattachent, ou s'assument comme volontairement isolées.
2. **La circulation.** L'autorité descend-elle de l'accueil et des pages fortes vers les pages qui doivent ranker, ou stagne-t-elle en haut, ou fuit-elle vers des pages sans enjeu (mentions légales, conditions de vente, connexion) ?
3. **La cohérence thématique.** Les liens suivent-ils les clusters (pilier et satellites, voisins d'un même thème) ? Un lien cohérent transmet un signal ; un lien au hasard dilue.
4. **La profondeur.** Les pages cibles sont-elles à peu de clics de l'accueil, ou enfouies ?
5. **Les ancres.** Les textes de liens sont-ils descriptifs et variés (ils disent de quoi parle la page liée), ou identiques partout, ou vides (« cliquez ici », « en savoir plus ») ?

Ces cinq questions se tranchent **dans un crawl**, pas à l'intuition.

## Le script

`scripts/maillage.py` lit l'export « All Inlinks » de Screaming Frog (ou tout CSV avec Source, Destination et Ancre) et sort la carte des manques : orphelines, profondeur de clic, état de chaque page cible, et pages qui captent le plus de liens. Bibliothèque standard de Python, rien à installer.

```bash
python scripts/maillage.py liens.csv --accueil https://www.exemple.fr/ --pages sitemap.txt --cibles cibles.txt
```

Sans `--pages` (le sitemap, ou la liste des pages qui devraient exister), les orphelines sont introuvables : par définition, une page que rien ne lie n'apparaît pas dans un export de liens. Le script le dit, et toi aussi.

Exécute-le si tu peux exécuter du code ; sinon, lis l'export à la main avec les mêmes questions. **Le script montre des faits de crawl, il ne décide pas.**

## Les pièges à détecter

| Piège | Signe | Conséquence |
|---|---|---|
| **Les orphelines** | aucune page interne ne les lie | invisibles au crawl et à l'internaute |
| **L'autorité qui stagne en haut** | tout pointe vers l'accueil, rien ne redescend | les cibles manquent d'autorité interne |
| **La fuite vers l'inutile** | les pages sans enjeu reçoivent le plus de liens | autorité dispersée |
| **Le maillage anti-cluster** | des liens qui ignorent la logique thématique | signal brouillé, pas de cocon |
| **La profondeur excessive** | des cibles à 4 clics ou plus | peu explorées, jugées mineures |
| **Les ancres sur-optimisées ou vides** | la même ancre exacte partout, ou « cliquez ici » | signal suspect, ou nul |
| **Les liens de menu pris pour du maillage** | toutes les pages lient les mêmes catégories via le menu | les liens dans le contenu, ceux qui portent le sens, manquent |

## Ce que tu produis

- **La carte des manques :** orphelines, cibles sous-liées, fuites, profondeur.
- **Le plan de liens :** un tableau d'actions, quinze lignes au maximum, triées par impact sur les pages cibles.

| Depuis quelle page | Vers quelle page | Ancre proposée | Pourquoi |
|---|---|---|---|
| un satellite du cluster | le pilier | une ancre qui décrit le pilier | remonter l'autorité vers la tête |

- **Les renvois :** si les pages à relier n'existent pas encore, `seo-cluster`. Si le problème vient de l'arborescence, dis-le : c'est hors de ce kit.

## Quand la donnée manque

Sans export de crawl, tu peux expliquer la méthode, pas établir la carte. Demande : l'export des liens internes (source, destination, ancre, et si possible la position du lien), la liste des pages qui devraient exister, la liste des pages cibles, et l'URL de l'accueil.

## Garde-fous

- **Les orphelines se prouvent par le crawl**, pas par l'intuition.
- **Un lien a un sens, ou n'a pas lieu d'être.** Le maillage suit la logique thématique ; un lien décoratif dilue plus qu'il n'aide.
- **Liens internes uniquement.** Le netlinking est un autre chantier.
- **Tu conçois les liens, pas la structure.** Ne propose pas de renommer des URLs pour régler un problème de liens.

## Enchaînements

- Reçoit la main de `seo-cluster` (pilier et satellites définis, il faut les relier) et de `seo-search-console` (une cannibalisation à arbitrer).
- S'empile avec `seo-savoir-penser` : « la page est bien maillée » se prouve par le crawl.
