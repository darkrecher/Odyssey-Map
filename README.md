Carte du jeu vidéo Odyssey (Motion Twin)
Réalisée avec QGis.

Sera publiée dans le cloud de QGis, quand elle sera potable.

ici : http://qgiscloud.com/Recher/odyssey_map

# Liste des tâches #

## TODO ##

 - ajouter les îles et mers qui sont mentionnées dans twinpedia, mais pas dans l'image de carte.
 - finir de saisir les îles et mers de img_778N9.png.
 - lister les îles incertaines pour cause de "même coordonnée". Essayer de connaître leur position précise.
 - classe générique POI (avec attributs spécifique, genre le prix pour les auberges).
 - symbole des POI :
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
 - récupérer les POI simples depuis twinpedia.
 - récupérer les POI compliqués (objets divers)
 - récupérer les POI compliqués (PNJ, depuis help-odyssey)
 - placement du POI sur une île, ou un plein milieu d'une coordonnée quand on ne sait pas où il est.
 - répartition de tous les POI d'une île / d'une coordonnée, pour les représenter non superposés.
 - trouver un moyen de représenter les POI incertains dans la carte (symbole grisé, ou un truc du genre).
 - noms courts et noms longs pour : îles, mers, héros, PNJ.
 - fonction d'agrégation pour l'or.
 - apparence de la carte :
    * quels textes s'affichent à quelle échelle.
    * hachurage des îles selon leur difficulté.
    * même symbole mais avec une couleur différente, pour les PNJ, les autels, les héros, [les boss]
 - carroyage.
 - gros carré pour faire un fond, avec le lien vers github et mon blog.
 - publier.
 - annoncer sur le forum de twinoid.
 - doc pour expliquer comment reconstruire la carte et la publier.
 - doc sur le module qgis_recher_api
 - mini-docs d'utilisation, et remerciements dans la carte elle-même.

## FUTURE (TODO, mais que si on est vraiment motivé) ##

 - POI des rumeurs
 - les îles incertaines dans la même coordonnée ne doivent pas se superposer.
 - trouver un screenshot plus complet de la carte globale.
 - vérif de cohérence entre les POI de twinpedia et ceux de help-odyssey.
 - vérif de cohérence entre les îles de twinpedia et les îles indiquées dans la partie "items" de help-odyssey.
 - vérif de cohérence entre la description des îles de twinpedia et tout le reste.
 - mettre les quêtes. une quête par répertoire de layer. avec un linéaire indiquant le chemin le plus court passant par tous les points de la quête. (Extraire manuellement les infos des quêtes à partir des indications du site help-odyssey)
 - possibilité de faire le plan détaillé d'une île : les chemins, les listes de monstres, ...
 - doc de conception du code.

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