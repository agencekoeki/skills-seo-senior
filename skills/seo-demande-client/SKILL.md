---
name: seo-demande-client
description: Décortique une demande SEO brute (mail, ticket, capture, demande d'un client, d'un chef de projet ou d'un développeur) avant que quiconque y réponde. Sépare ce que le client DIT, ce qu'il VEUT vraiment, et ce qui va CASSER qu'il ne voit pas, puis passe six questions dans un ordre précis. À charger dès que l'utilisateur colle ou résume une demande d'un tiers, ou dit « mon client veut », « le dev propose de », « est-ce possible de renommer / migrer / restructurer », « qu'est-ce que ça touche en SEO », « décortique cette demande ». Cadre et aiguille, ne résout pas. Ne pas déclencher pour une question SEO théorique isolée.
license: GPL-3.0
---

# seo-demande-client : la demande formulée n'est jamais le besoin

**Version 1.0, octobre 2026.** Partie du kit « 7 workflows IA d'un SEO senior » de Sébastien Grillot.

## Pourquoi ce skill existe

Une demande SEO n'arrive jamais propre. Elle est **déformée par celui qui l'écrit** :

- le développeur la formule en solution (« renommer les URLs »), parce qu'il pense en tâches ;
- le chef de projet la formule en symptôme (« on a moins de trafic »), sans savoir ce qui compte ;
- le client la formule en copie d'un concurrent (« faites comme eux »), sans voir ce que ça implique.

Une IA, comme le développeur, répond à la lettre. C'est le réflexe par défaut, et c'est le piège. Le SEO senior répond à l'**intention**, et surtout au **risque que personne n'a vu**. Ce skill installe ce décalage, avant toute solution.

## Le réflexe central : trois couches, dans cet ordre

1. **Ce que le client DIT.** Sa phrase, à la lettre. Tu ne la juges pas encore.
2. **Ce qu'il VEUT vraiment.** L'enjeu sous la formulation. Souvent plus large que sa phrase, parfois plus étroit.
3. **Ce qui CASSE et qu'il ne voit pas.** La couche que presque toutes les demandes omettent, et celle qui coûte cher. **Elle n'est jamais vide.** Si tu ne trouves pas de risque, tu n'as pas assez cherché.

Si une couche te manque et que tu ne peux pas la déduire proprement, tu le dis et tu demandes. Tu ne la combles pas par un « probablement ».

## Les six questions, dans cet ordre

L'ordre n'est pas neutre. Le SEO moyen commence par la technique. Ici, on commence par la valeur : ça évite de très bien exécuter un chantier qui ne rapporte rien.

1. **Valeur.** Ce trafic existe-t-il encore, et vaut-il qu'on se batte ? Vise-t-on du trafic que l'IA ou la SERP capte déjà avant le clic ? Intention qui rapporte, ou information siphonnée ? Parfois, le meilleur conseil est de ne pas faire la demande.
2. **Nature.** Est-ce structurel (URLs, arborescence, maillage) ou cosmétique (une balise, un texte) ? Le structurel est un fort levier, durable, mais risqué. Piège fréquent : une demande cosmétique qui cache un enjeu structurel, ou l'inverse.
3. **Risque.** Qu'est-ce qui casse si on le fait ? Redirections, désindexation, perte d'autorité, duplication, cannibalisation, sitemap ou robots.txt cassés. « Ça marche en préproduction » ne veut pas dire « ça ne casse rien en production avec l'historique et l'indexation existante ».
4. **Faisabilité.** Est-ce faisable proprement sur CE CMS, sans usine à gaz ? Pas de module tiers douteux et non maintenu, pas de dépendance qui doublonne une fonction existante. Une bonne pratique infaisable proprement sur la plateforme du client n'en est pas une, ici.
5. **Alignement.** Le gain justifie-t-il l'effort et le risque ? C'est la question qui autorise à dire « non, pas maintenant » ou « oui, mais autrement ».
6. **Mesure.** Saura-t-on prouver que ça a marché ? Et la donnée actuelle est-elle lisible (périmètre de la propriété, continuité de la série, volume suffisant) ? Un chantier qu'on ne peut pas mesurer ne se défend pas, ne se reconduit pas, ne se refacture pas.

Ces six questions se généralisent à n'importe quelle demande, y compris celles que ce skill n'a jamais vues. Tu n'appliques pas des recettes : tu installes un questionnement.

## La grille de traduction (des exemples, pas des cases)

Le motif à retenir : **la demande formulée est toujours plus pauvre que le besoin, et le risque est toujours invisible pour le client.**

| Le client dit | Il veut vraiment | Ce qui casse | Skills à enchaîner |
|---|---|---|---|
| « Renommez nos URLs en /marque/produit » | une arborescence qui reflète la hiérarchie, au lieu d'identifiants techniques | le mur de redirections sur tout l'historique, et la désindexation si c'est mal séquencé | hors kit (migration), puis `seo-maillage-interne` |
| « On veut plus de trafic sur le blog » | à requalifier : quel trafic, quelle intention, quel chiffre d'affaires derrière ? | viser du trafic que l'IA capte déjà avant le clic | `seo-valeur-du-trafic`, puis `seo-gagnabilite-serp`, puis `seo-cluster` |
| « Notre concurrent est mieux placé » | savoir si la SERP est gagnable ou perdue d'avance | brûler des mois sur une SERP verrouillée | `seo-gagnabilite-serp` |
| « On a perdu du trafic » | savoir si la perte est réelle, où elle se situe, ce qui l'a causée | une « perte » qui n'est qu'un artefact de mesure (consentement, périmètre de propriété, changement de tag) | `seo-search-console` |
| « Ajoutez 200 pages produits » | couvrir un champ sans se cannibaliser | duplication et pages fines | `seo-cluster` |
| « Les IA ne parlent pas de nous », « il nous faut un llms.txt » | être la source nommée, et citée correctement | robots bloqués par accident, contenu invisible sans JavaScript, citation fausse | `seo-citabilite-geo` |

## Ce que tu produis

Court, tranché :

- **Ce que le client dit :** [une phrase]
- **Ce qu'il veut vraiment :** [l'enjeu traduit]
- **Le vrai risque :** [ce qui casse, invisible pour lui]
- **Les chantiers à ouvrir, dans l'ordre :** [liste, avec le skill de chaque chantier]
- **Par où j'entrerais :** [une décision, pas trois options]
- **Ce qu'il me manque pour trancher :** [la donnée précise à obtenir]

Un exemple complet est dans `references/cas-d-ecole.md`.

## Garde-fous

- **Le triage trie, il n'exécute pas.** Dès que tu choisis un module, écris des redirections ou rédiges un contenu, tu as quitté ce skill. Nomme le chantier, propose l'enchaînement, arrête-toi.
- **Vérifier l'existant, oui ; concevoir la solution, non.** Demander comment les anciennes URLs sont redirigées aujourd'hui fait partie du triage. Écrire le nouveau plan de redirections n'en fait pas partie.
- **Jamais répondre à la lettre.** Si tu reprends la formulation du client comme si c'était le besoin, tu fais le travail du développeur, pas le tien.
- **Le chiffre du client est un PENSER** tant qu'on n'a pas vu la donnée (`seo-savoir-penser`).
- **La couche « ce qui casse » n'est jamais vide.** Son absence est une erreur de triage.

## Enchaînements

- Précède tous les fronts du kit. C'est lui qui les nomme.
- S'empile avec `seo-savoir-penser` dès que la demande s'appuie sur un chiffre ou devient un audit.
- Si la demande sort du kit (performance, migration, netlinking, E-E-A-T), dis-le en une phrase plutôt que d'improviser une méthode.
