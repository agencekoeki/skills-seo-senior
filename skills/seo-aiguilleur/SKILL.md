---
name: seo-aiguilleur
description: Point d'entrée des skills SEO senior. Lit une demande de référencement (SEO, GEO, Search Console, mots-clés, contenu, maillage, citations par les IA, mail ou ticket de client) et choisit le raisonnement à appliquer avant toute réponse. À charger dès qu'une conversation touche le référencement et qu'aucun skill plus précis n'est actif, ou quand l'utilisateur dit « par où je commence », « c'est quoi le vrai problème ici », « aide-moi sur ce dossier SEO », « regarde ce que m'envoie mon client ». Ne traite pas le fond lui-même : il aiguille, puis s'efface.
license: GPL-3.0
---

# seo-aiguilleur : choisir le raisonnement avant de dérouler la réponse

**Version 1.0, octobre 2026.** Partie du kit « 7 workflows IA d'un SEO senior » de Sébastien Grillot.

## Pourquoi ce skill existe

Une demande SEO arrive rarement avec son étiquette. « On a perdu du trafic » peut cacher un problème de mesure, une SERP qui a changé, une page désindexée ou une refonte mal faite. Si tu réponds directement, tu choisis un diagnostic au hasard et tu le déroules avec assurance. C'est le pire des scénarios : une réponse bien écrite, sur le mauvais problème.

L'aiguilleur fait une seule chose, et elle passe avant tout le reste : **il choisit le bon raisonnement avant que tu en déroules un.**

## Le protocole, en quatre temps

1. **Qualifier la forme de la demande.**
   - Une demande brute venue d'un tiers (mail, ticket, capture, « mon client veut », « le dev propose ») : `seo-demande-client` d'abord, toujours. Elle traduit avant d'agir.
   - Une question précise : le skill du front concerné (carte ci-dessous).
   - Une donnée jointe (export Search Console, crawl, SERP collée) : le skill qui sait lire cette donnée.
2. **Choisir deux skills au maximum.** Au-delà, les consignes se contredisent et le contexte se noie. Les autres, tu les nommes pour plus tard.
3. **Empiler `seo-savoir-penser`** dès qu'il y a un chiffre, un audit, un livrable pour un client, ou une affirmation sur ce que fait Google ou une IA.
4. **Annoncer en une ligne, puis t'effacer.** « J'applique seo-search-console, parce que tu m'as joint un export et que la question est une baisse de trafic. » L'utilisateur peut corriger l'aiguillage tout de suite. Ensuite, c'est le skill choisi qui guide.

## La carte

| Ce que tu entends ou reçois | Skill | Pas pour |
|---|---|---|
| Un mail, un ticket, la demande d'un client ou d'un dev, « est-ce possible de… » | `seo-demande-client` | une question théorique isolée |
| « Plus de trafic », « ça vaut le coup de créer cette page ? », des impressions sans clics, « les AI Overviews nous piquent nos clics » | `seo-valeur-du-trafic` | savoir si la SERP est prenable |
| « Peut-on se positionner sur [requête] ? », choix de mots-clés, « notre concurrent est mieux placé », « pourquoi on ne monte pas » | `seo-gagnabilite-serp` | décider si le trafic vaut le coup |
| Un export ou un accès Search Console, une baisse de trafic, des positions, de l'indexation | `seo-search-console` | ce qui se passe après le clic (analytics) |
| Un plan de contenu, un blog, une page pilier, des articles qui se concurrencent, des pages en série | `seo-cluster` | les URLs, les liens |
| Liens internes, pages orphelines, profondeur de clic, ancres | `seo-maillage-interne` | les liens venus d'autres sites |
| « Comment être cité par ChatGPT », Perplexity, AI Overviews, llms.txt, « les IA ne parlent pas de nous » | `seo-citabilite-geo` | l'accès technique des robots (à traiter, mais hors kit) |
| Tout ce qui demande de distinguer ce qu'on sait de ce qu'on suppose | `seo-savoir-penser` | s'empile sur tous les autres |

## Les parcours qui reviennent

| Situation | Ordre |
|---|---|
| « On a perdu du trafic » | `seo-search-console` (en commençant par la lisibilité de la donnée), puis `seo-valeur-du-trafic` si les impressions tiennent et que les clics fondent |
| « Il nous faut plus de trafic », « on lance un blog » | `seo-valeur-du-trafic`, puis `seo-gagnabilite-serp`, puis `seo-cluster`, puis `seo-maillage-interne` |
| « Les IA ne nous citent pas » | `seo-valeur-du-trafic` (le clic est-il mort ?), puis `seo-citabilite-geo` |
| « Notre concurrent nous passe devant » | `seo-gagnabilite-serp`, puis `seo-cluster` |
| « Renommez nos URLs », « on refait le site » | `seo-demande-client` ; la migration elle-même est hors kit (voir plus bas) |

Un parcours se **propose**, il ne se lance pas d'office. À la fin d'un skill, tu dis lequel vient ensuite et pourquoi, et l'utilisateur décide.

## Hors carte

Ce kit couvre sept fronts. Il ne couvre pas : la performance et les Core Web Vitals, la migration et le plan de redirections, le netlinking, l'E-E-A-T et les sujets YMYL (santé, finance, droit), la mesure après le clic (GA4). Si la demande y tombe :

- dis-le en une phrase (« ce kit n'a pas de méthode pour ça ») ;
- applique quand même `seo-savoir-penser` ;
- ne fais pas semblant d'avoir une méthode que tu n'as pas.

Une refonte ou un renommage d'URLs mérite au minimum de nommer le risque (redirections, désindexation, perte d'autorité) et de conseiller un plan de redirections validé avant la mise en ligne.

## Si un skill nommé ici n'est pas installé

Dans Codex, Gemini ou ChatGPT, ou avec une installation partielle, il se peut qu'un skill manque. Dis-le, puis applique au moins sa question centrale :

| Skill | Sa question centrale |
|---|---|
| `seo-savoir-penser` | Ce que j'affirme, je le sais ou je le pense ? |
| `seo-demande-client` | Qu'est-ce qu'il dit, qu'est-ce qu'il veut vraiment, qu'est-ce qui va casser ? |
| `seo-valeur-du-trafic` | Ce clic existe-t-il encore, et rapporte-t-il ? |
| `seo-gagnabilite-serp` | Qui occupe cette SERP, et a-t-on le poids pour s'y asseoir ? |
| `seo-search-console` | Qu'est-ce qui va changer la trajectoire de ce site ? |
| `seo-cluster` | Deux pages répondent-elles à la même question ? |
| `seo-maillage-interne` | Chaque page reçoit-elle du lien des bonnes voisines ? |
| `seo-citabilite-geo` | Si l'IA nous cite, est-ce sous notre nom, et correctement ? |

## Garde-fous

- **L'aiguilleur route, il ne répond pas.** Dès que tu commences à diagnostiquer, tu as quitté ce skill : charge le front.
- **Dans le doute entre deux skills, `seo-demande-client`.** Traduire coûte une minute ; se tromper de problème coûte des semaines.
- **Toujours annoncer l'aiguillage**, en une ligne.
- **Jamais de skill inventé.** Si rien ne couvre le sujet, dis-le.
