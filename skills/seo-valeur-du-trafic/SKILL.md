---
name: seo-valeur-du-trafic
description: Avant de chercher à ranker, décide si le trafic visé arrive encore sur le site ou si l'IA et la SERP le captent avant le clic, puis s'il rapporte. Grille de valeur « survie du clic × intention ». À charger dès qu'une demande vise « plus de trafic », « plus de visibilité », la création d'une page ou d'un article, un blog, une liste de mots-clés, ou quand l'utilisateur dit « ça vaut le coup de créer cette page ? », « on a des impressions mais pas de clics », « les AI Overviews nous piquent nos clics », « faut-il encore faire du contenu informationnel ». Ne pas déclencher pour savoir si une SERP est prenable (seo-gagnabilite-serp) ni pour être cité par une IA (seo-citabilite-geo).
license: GPL-3.0
---

# seo-valeur-du-trafic : on se bat pour quoi, au juste ?

**Version 1.0, octobre 2026.** Partie du kit « 7 workflows IA d'un SEO senior » de Sébastien Grillot.

## Pourquoi ce skill existe

Le SEO moyen commence par « comment ranker ». Ce skill commence par une question volontairement contre-intuitive : **ce trafic existe-t-il encore, et vaut-il d'être capté ?**

Une part croissante des recherches ne débouche plus sur une visite. La réponse est servie dans la page de résultats : extrait optimisé, panneau, AI Overview, AI Mode. L'internaute lit et repart. Sur une partie du trafic informationnel, le clic est structurellement mort : on peut être premier et ne recevoir personne.

Décider **si un contenu mérite d'exister** est donc devenu une décision SEO à part entière, en amont de toute optimisation. Créer une page qu'une IA résumera sans jamais envoyer de visite, c'est produire de la matière gratuite pour un moteur, pas de la valeur pour le client.

## La question centrale

Devant toute demande de trafic ou de contenu : **ce trafic arrive-t-il encore sur le site, ou l'IA et la SERP le captent-elles avant le clic ?**

Puis, immédiatement : **et s'il arrive, convertit-il ?** Un trafic qui arrive et ne fait rien ne vaut pas mieux qu'un trafic mort.

## La grille de valeur

Chaque requête visée se classe sur deux axes : le clic survit-il, et l'intention rapporte-t-elle ?

| | Le clic survit | Le clic est siphonné |
|---|---|---|
| **Intention qui rapporte** (transactionnelle, commerciale) | **Cibler.** Le clic existe et il convertit : c'est là que va le budget. | **Surveiller.** Un comparateur ou un panneau peut capter quand même. |
| **Intention qui informe** | **À condition de.** Nourrir la notoriété, le maillage, ou être la source citée. | **Éviter.** Tu écris pour l'IA, pas pour toi. |

Le réflexe : pousser vers le coin « cibler », se méfier du coin « éviter ». « acheter porte-vélo Fiamma » garde son clic et vend. « qu'est-ce qu'un porte-vélo » est de plus en plus résumé par l'IA, et ne vend rien.

## Les quatre questions de valeur

1. **Survie du clic.** Sur cette requête, la SERP sert-elle déjà la réponse ? Quel clic reste-t-il à prendre ? **Sans la SERP réelle du jour sous les yeux, la réponse est « inconnu ».**
2. **Intention.** Transactionnelle, commerciale, ou purement informationnelle ? Ce que la requête dit de l'étape où en est la personne.
3. **Rôle stratégique.** Si le clic est mort, le contenu sert-il à autre chose de mesurable : notoriété, maillage interne, être la source citée par les IA (`seo-citabilite-geo`) ? Sinon, pourquoi le créer ?
4. **Coût d'opportunité.** Ce budget, investi sur du trafic vivant, rapporterait quoi ? Créer une page morte, c'est ne pas créer une page vivante.

## Comment lire la survie du clic

Sur la SERP du jour, note ce qui se trouve **avant** le premier résultat organique : AI Overview, extrait optimisé, pack local, carrousel produits, vidéos, « Autres questions posées ». Plus la réponse est complète au-dessus de la ligne de flottaison, plus le clic est fragile.

Dans Search Console, le signe caractéristique : des impressions qui montent ou tiennent, des clics qui stagnent ou baissent, à position à peu près stable. La position n'a pas bougé ; c'est la page de résultats qui a changé. Les chiffres de référence sont dans `references/sources.md`.

## Les pièges à détecter

| Piège | Signe | Conséquence |
|---|---|---|
| **Chasser le volume mort** | on vise un gros volume informationnel | impressions élevées, visites nulles |
| **Confondre impressions et valeur** | « on est bien positionné » sur des requêtes siphonnées | indicateur flatteur, zéro chiffre d'affaires |
| **Le contenu-cadeau à l'IA** | on produit ce que l'AI Overview résumera | on nourrit le moteur, pas le client |
| **Ignorer l'intention** | du trafic qui arrive et repart | on célèbre des visites qui ne font rien |
| **Présumer que le clic survit** | aucune SERP observée | toute la stratégie repose sur une hypothèse |

## Ce que tu produis

- **Un tableau :** requête · clic (vivant / siphonné / inconnu) · intention · verdict (cibler / à condition de / ne pas créer).
- **Une phrase :** où je mets le budget en premier.
- **La suite :** si le clic est vivant mais qu'on ignore si la SERP est prenable, `seo-gagnabilite-serp`. Si le clic est mort mais qu'on veut exister sur le sujet, `seo-citabilite-geo`.

## Garde-fous

- **Le volume de recherche n'est pas la valeur.** Un petit volume vivant et transactionnel vaut plus qu'un gros volume mort.
- **Ne valide jamais un contenu sans avoir posé la survie du clic.** L'oublier, c'est faire du SEO d'avant 2023.
- **« Ne crée pas cette page » est une recommandation légitime.** Tu n'es pas là pour justifier du contenu, tu es là pour protéger le budget.
- **Tu décides si ça vaut le coup, pas comment le prendre.** La gagnabilité de la SERP, c'est `seo-gagnabilite-serp` ; la production, `seo-cluster`.
- **Les chiffres d'études se datent** (`seo-savoir-penser`). Ceux de ce skill sont datés dans `references/sources.md`.

## Enchaînements

- Souvent appelé par `seo-demande-client` sur toute demande de trafic ou de contenu.
- Mène à `seo-gagnabilite-serp` (prendre un clic vivant), `seo-citabilite-geo` (exister sans clic), `seo-cluster` (produire).
