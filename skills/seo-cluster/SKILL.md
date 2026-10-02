---
name: seo-cluster
description: Organise le contenu d'un thème en cluster (une page pilier, des satellites) pour couvrir un sujet entièrement sans que les pages se cannibalisent. Formule chaque page comme une question unique et passe le test anti-doublon contre l'existant. À charger dès qu'une demande touche un plan de contenu, un blog, un calendrier éditorial, une page pilier, des pages en série (programmatiques), des marronniers, ou quand l'utilisateur dit « on veut couvrir tout le sujet », « nos articles se font concurrence », « on a 200 pages à créer », « quel plan de contenu ». Ne pas déclencher pour choisir la cible (seo-gagnabilite-serp), ni pour les URLs, ni pour les liens internes (seo-maillage-interne).
license: GPL-3.0
---

# seo-cluster : une question, une page

**Version 1.0, octobre 2026.** Partie du kit « 7 workflows IA d'un SEO senior » de Sébastien Grillot.

## Pourquoi ce skill existe

Produire du contenu « au poids », des articles isolés empilés les uns sur les autres, ne construit aucune autorité sur un sujet. Et ça crée deux problèmes :

- **La cannibalisation.** Deux pages qui visent la même intention se volent le classement. Google ne sait pas laquelle servir : les deux plafonnent.
- **La couverture trouée.** Un thème traité par morceaux, sans logique d'ensemble, ne signale aucune expertise complète.

La logique de cluster règle les deux d'un coup : **une page pilier** qui tient le cœur du sujet, **des satellites** qui traitent chacun une facette précise et distincte. C'est aussi ce qui rend les pages en série viables plutôt que « fines », à condition que chaque page apporte une valeur propre.

## La question centrale

Devant une demande de contenu : **couvre-t-on un champ complet et sans doublon, ou empile-t-on des pages qui se cannibalisent ?**

## Le questionnement

1. **Le pilier existe-t-il ?** Un thème sans page pilier est un cluster décapité : pas de point d'ancrage, pas de tête vers laquelle les satellites pointent.
2. **Chaque satellite a-t-il une intention distincte ?** Une facette = une page = une intention. Formule chaque intention **sous forme d'une seule question**, celle que la page résout. Deux pages qui répondent à la même question, c'est une cannibalisation programmée.
3. **La couverture est-elle complète ?** Quelles facettes manquent ? Et à l'inverse, lesquelles sont hors intention ou sans valeur (la survie du clic se pose avec `seo-valeur-du-trafic`) ?
4. **À l'échelle** (pages en série, déclinaisons) : chaque page apporte-t-elle une valeur propre, ou est-ce la même page avec un mot changé ? Le volume ne rachète pas la minceur.
5. **La récurrence.** Le sujet a-t-il un cycle (saisons, marronniers, millésimes) qui justifie une déclinaison planifiée plutôt qu'un coup unique ?

## Le test anti-cannibalisation, pas à pas

1. Liste les pages **déjà en ligne** sur le thème, avec la requête principale de chacune.
2. Écris l'intention de chaque page existante et de chaque satellite proposé sous forme de **question unique**.
3. Compare les questions deux à deux. Si deux questions obtiendraient la même réponse, les deux pages sont en concurrence : **fusionner** (une page plus forte), **spécialiser** (réécrire l'une sur une facette distincte) ou **supprimer** (et rediriger).
4. Si Search Console est disponible, vérifie dans l'interface, page par page, si deux URLs se relaient sur les mêmes requêtes (`seo-search-console`, lecture 4). Sans ce couple requête × URL, la cannibalisation reste un PENSER.

## Les pièges à détecter

| Piège | Signe | Conséquence |
|---|---|---|
| **La cannibalisation** | deux pages, même question | elles se volent le classement, les deux plafonnent |
| **Le cluster sans tête** | des satellites sans page pilier | aucun point d'autorité, maillage sans centre |
| **Les pages en série trop fines** | des centaines de pages quasi identiques | pages jugées sans valeur, index gonflé pour rien |
| **La couverture trouée** | le thème traité par bouts | pas de signal d'expertise complète |
| **La surproduction** | des pages hors intention ou sans valeur | budget brûlé, dilution |
| **Le plan hors-sol** | aucune liste de l'existant | le plan doublonne ce qui est déjà en ligne |

## Ce que tu produis

- **Un tableau :** page · intention (une question) · statut (existe / à créer / à fusionner / à supprimer) · lien vers le pilier.
- **Les trous à combler** et **les excès à couper.**
- **Les trois pages à produire en premier, et pourquoi elles.**
- **Le verdict d'échelle,** si on parle de pages en série : valeur propre par page, ou condamnées à être fines.

## Quand la donnée manque

Sans la liste des pages déjà en ligne sur le thème, arrête-toi et demande-la : sans elle, tu proposes un plan qui doublonnera l'existant. Demande aussi le lecteur visé (qui, avec quel problème) : un cluster se construit autour d'une personne, pas d'un mot-clé.

## Garde-fous

- **Une intention = une page.** Non négociable.
- **Le volume ne rachète pas la minceur.** Vingt pages qui couvrent valent plus que deux cents pages fines.
- **Pas de cluster sans pilier.**
- **Tu conçois la couverture.** Tu ne décides ni des URLs ni des liens internes : ce sont deux autres chantiers (`seo-maillage-interne` pour les liens).

## Enchaînements

- Reçoit la main de `seo-gagnabilite-serp` (cible validée, il faut produire) et de `seo-valeur-du-trafic` (le contenu vaut le coup).
- Mène à `seo-maillage-interne` : relier le pilier et ses satellites.
