# Odyssey-Map #

Carte du jeu vidéo Odyssey, de la Motion Twin.

Consultable dans le cloud de QGIS :
http://qgiscloud.com/Recher/odyssey_map


## Copies d'écran ##

![screenshot map Odyssey vue globale](https://raw.githubusercontent.com/darkrecher/Odyssey-Map/master/docs_vrac/screenshot_001.png)

![screenshot map Odyssey vue détaillée](https://raw.githubusercontent.com/darkrecher/Odyssey-Map/master/docs_vrac/screenshot_002.png)

![screenshot map Odyssey examiner objet](https://raw.githubusercontent.com/darkrecher/Odyssey-Map/master/docs_vrac/screenshot_003.png)


## Afficher l'aide utilisateur ##

L'aide est intégrée dans la carte.

Sur le côté gauche se trouve la liste des layers. Cochez la case "texte__aide". Le manuel s'affichera par-dessus la carte. Décochez la case pour revenir à un affichage normal.

![screenshot map Odyssey afficher aide](https://raw.githubusercontent.com/darkrecher/Odyssey-Map/master/docs_vrac/afficher_aide.png)


## État actuel du projet ##

Il reste beaucoup d'infos à ajouter, à corriger, à vérifier, à corréler, etc.

Je n'ai pas prévu de retravailler dessus avant juillet 2015. En attendant, vous pouvez forker ce repository et créer votre propre carte à partir de celle-ci. Il faut juste se familiariser un peu avec QGIS et le langage python.


## Modifier et publier sa propre carte ##

TODO : partie à détailler. Il y a un début de documentation ici :

https://github.com/darkrecher/Odyssey-Map/blob/master/docs_vrac/edition_et_mise_en_ligne.md


## Crédits ##

### La carte ###

Créée par Réchèr.

La configuration de la carte, son apparence, le code source permettant de la générer et cette documentation sont sous une double licence : Art Libre ou Creative Commons CC-BY-SA (au choix).

Mon compte twinoid : http://twinoid.com/user/12910

Mon blog : http://recher.wordpress.com

Ce repository : https://github.com/darkrecher/Odyssey-Map

Les dons en crypto-monnaies diverses sont acceptés :
 - Bitcoin (BTC) : 12wF4PWLeVAoaU1ozD1cnQprSiKr6dYW1G
 - Litecoin (LTC) : LQfceQahHPwXS9ByKF8NtdT4TJeQoDWTaF
 - Dogecoin (Ð) : DKQUVP7on5K6stnLffKp3mHJor3nzYTLnS
 - Next (NXT) : 12693681966999686910

Vous pouvez faire un don sans dépenser d'argent. Allez sur ce lien (attention, c'est de la pub).
http://cur.lv/yns
Attendez quelques secondes, que le bouton "Skip ad" apparaisse en haut à droite, puis cliquez dessus.

### Le jeu Odyssey ###

Créé par la Motion Twin :
http://odyssey.muxxu.com/

Les informations du jeu (images, personnages, ...) sont sous licence copyright et appartiennent à la Motion Twin.


### Le recensement des données du jeu ###

Les données permettant de réaliser cette carte ont été collectées par les joueurs. Un grand merci aux sites et aux joueurs suivants :

Twinpedia :
http://www.twinpedia.com/muxxu/odyssey

Help-Odyssey :
http://muxxu.com/g/help-odyssey

Carte des auberges, faite par 3l3ktr0 :
http://muxxu.com/g/help-odyssey?page=37633


## Tâches restantes ##

### Priorité haute ###

 - Il y a toute la carte des îles et des mers ici : http://twd.io/e/xNdF0w/436
 - Afficher des points d'interrogation au lieu de "-1" lorsque le nombre de carte d'une mer est inconnu.
 - Incrémenter le champ "identifier" lors de la création des objets.
 - Regrouper les erreurs relevées dans Twinpedia, les corriger ou demander leur correction.
 - Lister les îles incertaines pour cause de "même coordonnée". Essayer de connaître leur position précise. (Soit en demandant, soit en y allant soi-même).
 - Dessiner les symboles des POI (Point Of Interests) au format SVG :
    * boss
    * objets de quêtes et objets divers
    * cartes
    * ruines
    * bibliothèques
    * fontaines
    * remplisseurs de potion
    * sacs de nourriture
    * auberges
    * autels
    * PNJ
    * héros
 - Déterminer les attributs de chaque type de POI, et les parser.
 - Récupérer les POI simples : boss, cartes, autels, héros.
 - Récupérer les POI compliqués : objets divers, PNJ (depuis help-odyssey).
 - Répartir correctement les POI présent sur une même coordonnée, pour qu'ils ne soient pas superposés.
 - Placer les POI sur leur île, quand c'est possible et qu'il n'ya pas d'ambigüité (une seule île sur la coordonnée).
 - Trouver un moyen de représenter les POI incertains (symbole grisé, ou un truc du genre).
 - Supprimer les incertitudes des POI à l'aide des descriptions d'île de Twinpedia.
 - Adapter la répartition des POI dans une zone, pour que ça marche avec les îles et les coordonnées incertaines.
 - Noms courts et noms longs pour : héros, PNJ.
 - Ajouter l'attribut "or" pour les îles. Le parser et l'afficher dans la carte.
 - Afficher l'or de chaque mer (égal au total des îles, en séparant ruines et pas-ruines).
 - Mettre un symbole avec une couleur variable pour : PNJ, autels, héros, [boss].
 - Terminer la doc expliquant comment reconstruire la carte et la publier.
 - Écrire les docstrings du module qgis_recher_api.
 - Enlever les bavure des screenshots.
 - Expliquer le "Object Identification = Active Layer" dans l'aide utilisateur. Sinon, on examine les infos de l'objet "texte__lien" et pas des objets en-dessous.

### Priorité basse ###

À ne faire que si la motivation est grande.

 - Gérer une carte des mers et des îles en "ascii art", parsée par le script, afin que les mers et les îles soient plus facile à mettre à jour et à saisir.
 - Ajouter les POI des rumeurs, avec leur texte.
 - Répartir les îles incertaines qui sont situées sur une même coordonnée.
 - Trouver une carte globale plus complète, pour cartographier d'autres mers et îles.
 - Faire des vérifs de cohérence entre les POI de Twinpedia et ceux de help-odyssey.
 - Faire des vérifs de cohérence entre les îles de Twinpedia et les îles indiquées dans la partie "items" de help-odyssey.
 - Faire des vérifs de cohérence entre la description des îles de Twinpedia et tout le reste.
 - Ajouter les quêtes, sous forme d'un objet linéaire indiquant le chemin le plus court passant par tous les points de la quête. Il faudra extraire manuellement les infos des quêtes à partir des indications du site Help-odyssey.
 - Coder la fonction de génération de plan détaillé d'une île : avec les chemins, les listes de monstres, ....
 - Écrire la doc de conception du code.
 - Régler tous les TODO présents dans le code.

### Tâches terminées ###

https://github.com/darkrecher/Odyssey-Map/blob/master/docs_vrac/taches_realisees.md