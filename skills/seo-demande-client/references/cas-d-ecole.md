# Cas d'école : « on a perdu 30 %, renommez nos URLs »

*Cas fictif, construit pour l'exemple. Il montre le niveau attendu, pas un modèle à recopier.*

## La demande reçue

> « Bonjour, depuis la refonte du site on a perdu 30 % de trafic. Notre développeur propose de renommer toutes les URLs produits en /marque/produit, comme notre concurrent. Vous pouvez valider ? »
> Un e-commerce d'accessoires, environ 1 200 produits.

## La réponse attendue

**Ce que le client dit :** il a perdu 30 % de trafic depuis la refonte et veut renommer toutes les URLs produits en /marque/produit.

**Ce qu'il veut vraiment :** retrouver le trafic d'avant la refonte, et surtout les ventes qui allaient avec. Le renommage est une solution déjà choisie, pas son besoin. PENSER : rien dans son message ne relie la perte à la forme des URLs.

**Le vrai risque :** une deuxième migration posée sur une première qu'on n'a pas comprise.
- Si la refonte a déjà changé les URLs, les anciennes pages et leurs liens externes passeraient par deux redirections successives, et Google relirait le catalogue une deuxième fois. PENSER, à vérifier par un crawl des anciennes URLs.
- Si la refonte n'a pas changé les URLs, la cause est ailleurs, et on crée une migration qui n'existait pas.
- Dans les deux cas, on empile deux changements : on ne saura plus jamais lequel a coûté quoi. La mesure est cassée.
- Le « 30 % » est un PENSER tant qu'on n'a pas vu la donnée. Une refonte change souvent le tag de mesure ou le bandeau de consentement : une partie de la « perte » peut n'exister que dans l'outil.

**Les chantiers à ouvrir, dans l'ordre :**
1. Valeur et mesure : la perte est-elle réelle, sur quelles pages, ces pages vendaient-elles ? Comparer les clics Search Console avant et après la refonte (`seo-search-console`), puis les rapprocher des données de vente.
2. Risque : crawler la liste des anciennes URLs. Pour chacune : redirection vers l'équivalent exact, erreur 404, ou renvoi vers l'accueil ?
3. Faisabilité et alignement : seulement ensuite, juger le passage en /marque/produit. Faisable proprement sur ce CMS ? Le gain vaut-il une nouvelle vague de redirections ? PENSER : le gain d'une URL plus lisible est faible face à ce risque.
4. Mesure : poser une base de référence avant de toucher à quoi que ce soit.

**Par où j'entrerais :** on gèle le renommage. J'entre par le diagnostic de la perte, page par page, dans Search Console.

**Ce qu'il me manque pour trancher :** la date de mise en ligne de la refonte ; si les URLs ont changé à ce moment-là et comment elles ont été redirigées ; d'où sort le 30 % (Search Console ou outil d'analytics, sur quelles périodes) ; le CMS.

## Ce qui rend cette réponse bonne

- Elle ne valide ni ne refuse le renommage : elle le **gèle** en attendant la preuve.
- La couche « ce qui casse » contient un risque que le client n'a pas vu (la double migration et la mesure cassée).
- Le chiffre du client reste un PENSER.
- La décision est unique, et la donnée manquante est précise.
