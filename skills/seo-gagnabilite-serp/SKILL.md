---
name: seo-gagnabilite-serp
description: Avant de viser un mot-clé, lit la SERP réelle pour décider si elle est gagnable pour CE site, quelle intention Google y récompense, et par quel angle entrer si la requête de face est fermée. À charger dès qu'une demande touche le choix de mots-clés, la difficulté d'une requête, l'analyse concurrentielle sur une requête, ou quand l'utilisateur dit « on veut se positionner sur [mot-clé] », « notre concurrent est mieux placé », « pourquoi on ne monte pas », « c'est un mot-clé difficile ? », « on fait une page produit ou un article pour ça ? ». Ne pas déclencher pour savoir si le clic existe encore (seo-valeur-du-trafic) ni pour organiser la couverture d'un thème (seo-cluster).
license: GPL-3.0
---

# seo-gagnabilite-serp : regarde qui est à table avant de t'asseoir

**Version 1.0, octobre 2026.** Partie du kit « 7 workflows IA d'un SEO senior » de Sébastien Grillot.

## Pourquoi ce skill existe

Un mot-clé n'est pas une cible. C'est un **terrain déjà occupé** : il a des tenants, une intention que Google a déjà tranchée, et un format de résultats. Deux erreurs classiques coûtent des mois :

- **Viser trop haut.** Se battre sur une requête tenue par des marketplaces, des encyclopédies ou de gros médias, avec un site qui n'a pas le poids pour rivaliser. On y met des mois, on n'atteint jamais la première page.
- **Se tromper d'intention.** Créer une page produit là où Google classe des guides, ou l'inverse. Google a déjà décidé quel **type** de page il récompense sur cette requête. Se battre contre ça, c'est perdre.

Le score de difficulté d'un outil est un indice. **La vérité est dans le top 10 réel.** Et la SERP contient déjà la réponse aux deux questions qui comptent : peut-on la prendre, et avec quel format ?

## La question centrale

Devant une requête cible : **qui occupe déjà cette SERP, quelle intention Google y récompense, et a-t-on le poids pour rivaliser ? Ou brûle-t-on du budget ?**

## Ce qu'on lit dans une SERP

1. **L'intention récompensée.** Quels **types** de pages Google classe-t-il en tête : fiches produit (transactionnel), guides (informationnel), comparatifs (commercial), pages de marque (navigationnel) ? Ce que Google classe, c'est l'intention qu'il a tranchée. On aligne son format dessus.
2. **Les occupants et leur poids.** Des géants hors de portée, ou des acteurs de ton niveau ? La difficulté réelle se lit dans **qui** ranke, pas dans un score.
3. **Volume contre faisabilité.** Un gros volume verrouillé vaut moins qu'un volume moyen accessible. On ne confond jamais l'attractivité (le volume) avec la faisabilité (qui occupe).
4. **Les features.** Pack local, images, vidéos, extrait optimisé, AI Overview, panneau : combien d'espace et de clics mangent-elles avant le premier résultat organique ? Une SERP saturée laisse peu de clic, même en première position (recoupe `seo-valeur-du-trafic`).
5. **L'angle d'entrée.** Si la requête de face est fermée, existe-t-il une longue traîne ou une intention voisine, plus spécifique, accessible, qui amène le même client ?

Le protocole de lecture détaillé, résultat par résultat, est dans `references/lire-une-serp.md`.

## Les pièges à détecter

| Piège | Signe | Conséquence |
|---|---|---|
| **Le mot-clé verrouillé** | top 10 tenu par des marketplaces, des encyclopédies, des gros médias | des mois d'effort, jamais la première page |
| **L'erreur d'intention** | une page produit là où Google classe des guides | la page ne rankera pas, mauvais format |
| **Le volume comme boussole** | on vise le plus gros volume sans regarder qui l'occupe | on vise l'inatteignable |
| **Ignorer les features** | premier en organique sous un mur de features | position gagnée, clics captés avant |
| **Le front unique** | on s'acharne sur la requête de face | on rate la traîne accessible qui convertit autant |
| **Le verdict sans SERP** | une difficulté « estimée » sans top 10 observé | un PENSER présenté comme un SAVOIR |

## Ce que tu produis

- **Le verdict :** prenable / imprenable pour ce site / prenable par un angle.
- **Le format de page à produire :** celui que Google récompense, pas celui que le client voulait.
- **La cible ajustée,** si la requête de face est fermée.
- **Ce qui est SAVOIR** (vu dans la SERP collée, avec sa date) **et ce qui est PENSER** (le poids supposé du site, par exemple).

## Quand la donnée manque

**Pas de top 10 réel, pas de verdict.** Demande les dix URLs du jour avec le type de chaque page, le pays et la langue. Demande aussi ce que l'utilisateur sait du poids de son site (ancienneté, notoriété, liens). Sans ces éléments, tu peux décrire la méthode, pas trancher.

## Garde-fous

- **La difficulté se lit dans qui occupe, pas dans un chiffre.**
- **On aligne le format sur l'intention que Google a tranchée.** On ne se bat pas contre elle.
- **Un « non, imprenable » net vaut mieux qu'un « on peut essayer » mou** qui coûtera des mois.
- **Tu tranches la cible, tu ne rédiges pas le contenu.** La production, c'est `seo-cluster`.
- **Une SERP se date.** Celle d'hier n'est pas celle d'aujourd'hui, et elle change selon le pays, la langue et l'appareil.

## Enchaînements

- Reçoit la main de `seo-valeur-du-trafic` (le clic est vivant : est-il prenable ?) et de `seo-demande-client`.
- Mène à `seo-cluster` une fois la cible et l'intention validées.
