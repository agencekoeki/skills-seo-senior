---
name: seo-citabilite-geo
description: Diagnostic GEO. Pour qu'un moteur génératif (AI Overviews, AI Mode, ChatGPT, Perplexity, Copilot, Claude) cite une page, sous le bon nom et correctement. Formule de travail : être cité = ranker sur les sous-requêtes + être extractible + être attribuable. À charger dès qu'une demande vise la visibilité dans les réponses des IA, ou quand l'utilisateur dit « comment être cité par ChatGPT », « apparaître dans Perplexity ou les AI Overviews », « les IA ne parlent pas de nous », « faut-il un llms.txt », « GEO », « AEO ». Ne pas déclencher pour décider si le trafic vaut le coup (seo-valeur-du-trafic).
license: GPL-3.0
---

# seo-citabilite-geo : cité, oui, mais sous ton nom et correctement

**Version 1.0, octobre 2026.** Partie du kit « 7 workflows IA d'un SEO senior » de Sébastien Grillot.

## Pourquoi ce skill existe

Un moteur génératif synthétise une réponse et cite, ou non, ses sources. Deux erreurs symétriques coûtent cher :

- **Croire que le GEO est un autre métier que le SEO.** Google l'écrit noir sur blanc : de son point de vue, optimiser pour la recherche générative, c'est encore du SEO. Vendre un « GEO » déconnecté du référencement, c'est vendre des recettes qui ne se répliquent pas.
- **Croire que bien ranker suffit.** L'IA éclate la question en sous-requêtes, puis choisit ce qu'elle cite. Les citations des AI Overviews ne viennent plus majoritairement du top 10 de la requête tapée.

Ce skill tient les deux bouts. Les sources et leurs dates sont dans `references/sources.md`.

## La formule de travail

**Être cité = ranker sur les sous-requêtes + être extractible + être attribuable.**

- **Ranker sur les sous-requêtes :** la page est indexée, éligible à l'extrait, et bien classée sur les questions que le modèle se pose à lui-même pour répondre, pas seulement sur la requête d'origine.
- **Être extractible :** des affirmations nettes, autonomes, présentes dans le HTML sans dépendre du JavaScript.
- **Être attribuable :** des énoncés datés, chiffrés, sourcés, sous un nom d'entité stable (marque, auteur), pour être cité, et cité juste.

Puis la question qui compte pour la marque : **sous quel nom, et avec quelle exactitude ?** Une citation anonyme ne construit rien ; une citation fausse détruit.

## Les six leviers du diagnostic

1. **Éligibilité.** La page est-elle indexée et autorisée en extrait (pas de `nosnippet` sur les pages stratégiques) ? Les robots de recherche des assistants (OAI-SearchBot, PerplexityBot, Claude-SearchBot) sont-ils bloqués par le robots.txt ou par le pare-feu, par accident ?
2. **Sous-requêtes.** Quelles questions l'IA se pose-t-elle pour répondre ? La page y répond-elle, et ranke-t-elle dessus ?
3. **Extractibilité.** Les affirmations clés sont-elles nettes, autonomes, dans le HTML initial ? Google dit ne pas avoir besoin d'un découpage spécial ; des sections claires aident d'autres assistants.
4. **Attribuabilité.** Chiffres datés, méthode visible, source citée, nom de marque et d'auteur identiques partout ?
5. **Autorité tierce.** Qui parle de la marque ailleurs, de façon indépendante (presse, institutions, vidéos, comparateurs) ? Ce que les autres disent pèse plus que ce qu'on dit de soi.
6. **Exactitude en sortie.** Quand la marque est citée, l'est-elle correctement ? Ça se vérifie par un panel de questions, rejoué et daté.

## Le protocole de mesure : trois grandeurs, séparées

- **Les citations :** les rapports IA de Search Console (impressions seulement, déploiement progressif), les rapports équivalents de Bing.
- **Les clics :** les visites venues des assistants, repérées par leur référent ou leurs paramètres de suivi (par exemple `utm_source=chatgpt.com`).
- **Les mentions :** un panel de vingt à trente vraies questions de clients, posées aux assistants à date fixe, avec captures. Les réponses varient d'une exécution à l'autre : on compare des tendances, pas une capture isolée.

Ne mélange jamais les trois. Une citation n'est pas un clic, et une mention n'est pas une citation.

## Les pièges à détecter

| Piège | Signe | Conséquence |
|---|---|---|
| **Le GEO hors-sol** | des réécritures « magiques » sans travail de classement | recettes non répliquées, client déçu |
| **Top 10 égale citation** | « on est premier, donc on sera cité » | on rate les sous-requêtes |
| **llms.txt ou miroir Markdown comme levier Google** | un plan GEO centré sur des fichiers pour IA | aucun effet chez Google, qui dit ne pas en avoir besoin ; un miroir indexé devient un doublon |
| **L'achat de mentions** | une campagne de « mentions » sans valeur éditoriale | Google dit ne pas en tenir le compte espéré ; risque d'image |
| **Citation égale trafic** | « nombre de citations » vendu comme indicateur business | le lien cité est très peu cliqué |
| **Citation égale vérité** | « ChatGPT nous cite, donc c'est juste » | les assistants se trompent souvent sur leurs sources |
| **L'entité floue** | nom de marque ou d'auteur variable selon les pages | citation anonyme, ou attribuée à quelqu'un d'autre |
| **Le blocage accidentel** | un pare-feu ou un robots.txt qui écarte les robots de recherche des assistants | invisible, sans erreur visible |
| **Google-Extended mal compris** | on le bloque pour « sortir des AI Overviews » | il ne touche pas l'inclusion dans la recherche Google |

## Ce que tu produis

- **Le diagnostic :** oui ou non pour chacun des six leviers, avec la preuve, et sous quel nom la marque est citée aujourd'hui.
- **Les leviers prioritaires,** en P0, P1, P2 : ce qui manque pour passer de « noyé » à « cité nommément et correctement ».
- **Le protocole de mesure,** avec les trois grandeurs séparées.

## Quand la donnée manque

Demande : l'URL de la page, le nom exact de la marque et de l'auteur, cinq à dix vraies questions que les clients posent aux assistants, et des captures datées de ce que les assistants répondent aujourd'hui. Sans captures, le diagnostic « exactitude » est un PENSER.

## Garde-fous

- **Le GEO ne se vend pas contre le SEO.** Chez Google, même index et même classement ; la différence tient à la sous-requête et à la sélection finale. Si tu te surprends à promettre une recette sans travail de classement, tu as glissé.
- **Aucune promesse de citation.** Les réponses sont instables et les moteurs opaques. On retire des obstacles et on augmente des probabilités ; on ne garantit rien.
- **Toute affirmation sur « comment les IA choisissent leurs sources » est un PENSER,** sauf documentation d'éditeur ou étude publiée, datée (`seo-savoir-penser`).
- **Viser l'attribution juste, pas le volume de mentions.**
- **Santé, finance, droit :** l'exigence monte d'un cran ; l'exactitude de la citation compte plus que sa fréquence.

## Enchaînements

- Reçoit la main de `seo-valeur-du-trafic` (le clic est mort : exister comme source).
- Mène à `seo-gagnabilite-serp` (ranker sur les sous-requêtes) et à `seo-cluster` (couvrir les questions que l'IA se pose).
- L'accès technique des robots, le rendu JavaScript et l'analyse des journaux serveur sont hors de ce kit : nomme-les, ne les improvise pas.
