Carte du jeu vidéo Odyssey (Motion Twin)
Réalisée avec QGis.

Sera publiée dans le cloud de QGis, quand elle sera potable.

ici : http://qgiscloud.com/Recher/odyssey_map

# Liste des tâches #

## TODO ##

 - incrémenter le champ "identifier" lors de la création des objets.
 - pour les nombres de cartes : afficher des points d'interrogation au lieu des "-1"
 - regrouper les erreurs relevés dans twinpedia, et les corriger ou demander leur correction.
 - lister les îles incertaines pour cause de "même coordonnée". Essayer de connaître leur position précise. (Soit en demandant, soit en y allant soi-même).
 - classe générique POI.
 - possibilité d'ajouter des attributs spécifique à un POI, genre le prix pour les auberges, afin de les exporter dans la carte.
 - symbole des POI en SVG :
    * boss
    * objets de quêtes et objets divers
    * cartes
    * ruines
    * temples
    * bibliothèques
    * fontaines
    * remplisseurs de potion
    * sacs de nourriture
    * auberges
    * autels
    * PNJ (à prendre depuis help-odyssey)
    * héros
 - récupérer les POI simples depuis twinpedia, sans leurs attributs.
 - déterminer les attributs de chaque type de POI, et les parser.
 - récupérer les POI compliqués (objets divers)
 - récupérer les POI compliqués (PNJ, depuis help-odyssey)
 - placement du POI au milieu de la coordonnée.
 - Répartir correctement les POI présent sur une même coordonnée, pour qu'ils ne soient pas superposés.
 - placement du POI sur une île, quand c'est possible (une seule île possible).
 - lorsqu'il y a plusieurs îles sur une même coordonnée, les POI seront incertains. Lever les incertitudes levables à l'aide des descriptions d'île dans twinpedia.
 - Adapter le processur de répartition des POI, pour que ça marche avec les îles et les coordonnées.
 - trouver un moyen de représenter les POI incertains dans la carte (symbole grisé, ou un truc du genre).
 - noms courts et noms longs pour : mers, héros, PNJ.
 - attributs or pour les îles. Parser et afficher dans la carte.
 - fonction d'agrégation pour l'or. afficher l'or pour chaque mer (total des îles, en séparant ruines et pas-ruines)
 - apparence de la carte :
    * quel texte s'affiche à quelle échelle, et à quelle taille.
    * même symbole mais avec une couleur différente, pour les PNJ, les autels, les héros, [les boss]
 - gros carré pour faire un fond, avec le lien vers github et mon blog.
 - annoncer sur le forum de twinoid.
 - doc pour expliquer comment reconstruire la carte et la publier.
    * il faut que toutes les couches soient visibles.
    * il faut : my_scripts.map_populator.populate(True, True). Les 2 True sont importants.
 - doc sur le module qgis_recher_api
 - mini-docs d'utilisation, et remerciements dans la carte elle-même. (avec le gros carré)

## FUTURE (TODO, mais que si on est vraiment motivé) ##

 - carte mer+île en "ascii art", pour que ce soit plus facile à mettre à jour et à saisir.
 - POI des rumeurs
 - les îles incertaines dans la même coordonnée ne doivent pas se superposer. À répartir aussi.
 - trouver un screenshot plus complet de la carte globale.
 - vérif de cohérence entre les POI de twinpedia et ceux de help-odyssey.
 - vérif de cohérence entre les îles de twinpedia et les îles indiquées dans la partie "items" de help-odyssey.
 - vérif de cohérence entre la description des îles de twinpedia et tout le reste.
 - mettre les quêtes. une quête par répertoire de layer. avec un linéaire indiquant le chemin le plus court passant par tous les points de la quête. (Extraire manuellement les infos des quêtes à partir des indications du site help-odyssey)
 - possibilité de faire le plan détaillé d'une île : les chemins, les listes de monstres, ...
 - doc de conception du code.
 - tous les TODO dans le code.

## FINI ##

 - récupération des mers et des îles de twinpedia.
 - récupération des mers et des îles depuis une saisie manuelle d'un screenshot de carte globale.
 - vérif de cohérence entre ces deux sources de données.
 - création des mers et des îles dans la carte.
 - publication de la carte (à refaire manuellement à chaque mise à jour)
 - contraindre les îles incertaines dans les limites de leur mer.
 - les îles incertaines ont une taille de 1 par défaut.
 - bords en zigouigoui pour les îles et mers incertaines.
 - permettre d'indiquer directement le nom de l'île dans img_778N9.py
 - mettre l'île en incertain, si indiqué comme tel dans img_778N9.py
 - tester les intersections en excluant les bords droits et bas, car là ça fait trop d'hésitation.
 - finir de saisir les îles et mers de img_778N9.png.
 - couche "mer texte" et "île texte", utilisant la même source de donnée que "mer" et "île", mais n'affichant quel es étiquettes. Comme ça on peut cacher uniquement les étiquettes.
 - carroyage.
 - ajouter les îles et mers qui sont mentionnées dans twinpedia, mais pas dans l'image de carte.
 - texte détaillé des mers : carte et XP. (L'or, on verra plus tard).
 - apparence : hachurage des mers selon leur difficulté (nombre d'XP).