---
name: seo-search-console
description: Audite une propriété Google Search Console pour en sortir des décisions, pas des constats. Vérifie d'abord que la donnée est lisible, puis fait six lectures (ce qui saigne, ce qui est à portée, la promesse SERP, la cannibalisation, l'indexation, le zéro-clic) et livre une page lisible par le client. À charger dès que l'utilisateur colle ou joint un export Search Console, dit « audite la Search Console », « on a perdu du trafic », « regarde nos positions », « pourquoi on n'est pas indexé », « beaucoup d'impressions, peu de clics », « quelles requêtes on peut aller chercher ». Ne pas déclencher pour la mesure après le clic (analytics) ni pour trier une demande client brute (seo-demande-client).
license: GPL-3.0
---

# seo-search-console : six lectures, pas quarante constats

**Version 1.0, octobre 2026.** Partie du kit « 7 workflows IA d'un SEO senior » de Sébastien Grillot.

## Pourquoi ce skill existe

Search Console est la seule source qui dise ce que Google a montré du site et ce qui a été cliqué. Elle s'arrête net au clic : ce qui se passe après relève de l'outil d'analytics.

Un audit Search Console rate presque toujours de la même façon : **quarante constats, zéro décision**. On liste les erreurs de couverture, on exporte les requêtes, on colle des captures. Et le client repart sans savoir quoi faire lundi.

L'inversion : tu ne cherches pas ce qui ne va pas. Tu cherches **ce qui va changer la trajectoire**. Six lectures suffisent. Ce qui n'entre dans aucune est du bruit documentaire.

## La question centrale

**Qu'est-ce qui va changer la trajectoire de ce site ?**

## Étape 0 : la donnée est-elle lisible ?

Non négociable. Si l'un de ces points saute, tout ce qui suit est faux, et tu le dis avant de produire quoi que ce soit.

| À vérifier | Pourquoi ça peut tout invalider |
|---|---|
| **Type de propriété** : domaine (`exemple.fr`) ou préfixe d'URL (`https://www.exemple.fr/`) | le préfixe ignore les autres sous-domaines et l'autre protocole. Deux propriétés « du même site » aux totaux différents, c'est la fausse alerte la plus fréquente |
| **Plusieurs propriétés en parallèle** | on compare sans le savoir deux périmètres |
| **Fenêtre de seize mois** | au-delà, il n'y a plus rien : un comparatif sur deux ans est impossible |
| **Données provisoires** | les derniers jours bougent encore : ne jamais diagnostiquer sur les trois derniers jours |
| **Anomalies déclarées par Google** | une chute peut venir d'un incident de collecte, pas du site : vérifier la page des anomalies avant d'accuser une mise en production |
| **Plafond de 1 000 lignes** dans l'interface | l'export est la tête de courbe, pas un échantillon : la longue traîne est invisible (API ou export BigQuery si l'enjeu le mérite) |

## Les six lectures

### 1. Ce qui saigne
Compare les 28 derniers jours à la période précédente, **au niveau des URLs**. Retiens ce qui pesait au moins une cinquantaine de clics et perd au moins 25 %. Le reste est du bruit.

Trois causes à départager avant de conclure, parce qu'elles appellent des actions opposées : **une baisse de position**, **une captation par une réponse générative**, **la saisonnalité**. Conclure sans avoir tranché, c'est prescrire au hasard. À position égale, une chute de clics désigne la SERP, pas le site.

### 2. Ce qui est à portée
Les requêtes en positions 8 à 20 avec de la demande. C'est le meilleur rapport effort-gain du SEO : la page existe, Google la connaît, il manque un cran.

Le piège : trier par impressions. Trie par **valeur business**. Une requête à 3 000 impressions sans intention d'achat vaut moins qu'une requête à 200 impressions transactionnelle.

### 3. La promesse SERP
Les lignes dont le CTR est très en dessous de ce que **ce site** obtient à cette position. Pas d'une courbe théorique publiée ailleurs : les courbes génériques ne valent rien hors de leur secteur et produisent des faux positifs à la chaîne.

Deux diagnostics possibles, et il faut choisir : la promesse est mauvaise (title et description à retravailler), ou **le clic n'est plus l'issue de cette SERP**. Le second ne se répare pas avec un title : il bascule vers `seo-valeur-du-trafic`.

### 4. La cannibalisation
Une requête dont l'URL positionnée alterne dans le temps, ou deux URLs sur le même groupe de requêtes.

**Les exports standard ne permettent pas de la voir** : les onglets Requêtes et Pages sont séparés, il n'existe aucun couple requête × URL. Pour l'établir : filtrer page par page dans l'interface, ou passer par l'API. N'affirme jamais une cannibalisation à partir des deux exports séparés : c'est un PENSER déguisé en SAVOIR. Une fois établie, l'arbitrage (fusionner, spécialiser, réécrire) appartient à `seo-cluster` et `seo-maillage-interne`.

### 5. L'indexation
Le rapport Pages, les non indexées, **triées par motif**. Le motif est tout : « Explorée, actuellement non indexée » (Google a vu et jugé que ça ne valait pas la peine) ne se traite pas comme « Bloquée par le fichier robots.txt » (on s'est tiré une balle dans le pied), ni comme « Autre page avec balise canonique correcte » (c'est normal, n'y touche pas). Compter les pages non indexées sans les trier par motif ne produit aucune décision.

### 6. Le zéro-clic
La lecture qui distingue un audit de 2026 d'un audit de 2019 : des impressions qui montent pendant que les clics stagnent ou baissent.

Search Console déploie depuis juin 2026 un rapport séparé pour l'IA générative (AI Overviews, AI Mode) : **impressions seulement**, sans clics, sans CTR, sans requêtes, et pas encore sur toutes les propriétés. Son absence n'est pas un résultat. Ne calcule jamais un CTR qui mélange impressions Web et impressions IA générative. Détails et date dans `references/sources.md`.

## Le script

`scripts/gsc_lectures.py` fait l'étape 0 et les lectures 1 à 3 sur un export CSV de l'onglet Requêtes ou Pages, en français ou en anglais. Bibliothèque standard de Python, rien à installer.

```bash
python scripts/gsc_lectures.py export.csv
python scripts/gsc_lectures.py export.csv --total-impressions 184000 --min-clics 50 --top 20
```

Pour la lecture 1, l'export doit être fait avec « Comparer » activé (28 jours contre la période précédente). `--total-impressions` prend le total lu en haut du rapport Performance : le script calcule la part d'impressions que l'export ne montre pas.

Exécute-le si tu peux exécuter du code : c'est plus rapide, reproductible, et sans erreur de tableur. Sinon, fais les mêmes calculs à la main. **Le script sort des lignes, pas des décisions** : ses « pistes » sont des PENSER à confirmer.

## Ce que tu produis (une page, lisible par le client)

- **Ce que je peux affirmer :** périmètre, période, volume, et ce que l'export ne couvre pas.
- **Ce qui saigne :** avec la cause tranchée, ou la donnée qui manque pour la trancher.
- **Ce qui est à portée :** trié par valeur business.
- **Ce qui est déjà perdu :** les impressions qui ne deviendront pas des clics. Ne pas chercher à les récupérer.
- **Ce qui est cassé :** l'indexation, par motif.
- **Par où j'entrerais :** une décision, pas trois options.

Un audit Search Console qui ne tient pas en une page n'a pas été trié.

## Garde-fous

- **Le volume avant le pourcentage.** Une page qui passe de 12 à 8 clics n'a rien perdu.
- **Une baisse de clics n'est pas une baisse de positions.** Vérifie la position avant de conclure.
- **Jamais de cannibalisation sans couple requête × URL.**
- **Absence de donnée n'est pas donnée à zéro** : rapport en déploiement, propriété récente, requêtes anonymisées.
- **Tu audites une source, tu n'exécutes pas.** Dès qu'il faut concevoir la correction (arborescence, redirections, contenu, liens), passe la main au skill concerné.

## Enchaînements

- Mène à `seo-valeur-du-trafic` (l'impression vaut-elle qu'on se batte ?), `seo-gagnabilite-serp` (la SERP est-elle gagnable ?), `seo-cluster` et `seo-maillage-interne` (consolider après une cannibalisation).
- S'empile avec `seo-savoir-penser` : chaque affirmation porte sa source et sa période.
