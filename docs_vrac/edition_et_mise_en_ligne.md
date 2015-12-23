# Mettre en ligne sa propre version de la carte #

TODO :ce  bla-bla n'est pas très détaillé. Work in progress.

## Reconstruire la carte ##

La carte est réalisée avec le logiciel QGis 2.6.1-Brighton.

Ce repository contient un script en python permettant de reconstruir entièrement la carte, à partir de données présentes dans des fichiers textes.

Avant de lancer le script, il faut s'assurer que tous les layers sont visibles. Sinon, on risque d'obtenir un message d'erreur de ce type dans la console :

    File "C:/Recher/projets/git/Odyssey-Map/carte_offline\my_scripts\map_populator.py", line 66, in _layer_of_poi
        return recher_api.layers[layer_name]
    KeyError: u'lieu__ruines'


Pour lancer le script la première fois, ouvrir une console python dans QGIS.

    import main
    main.main()

Le script peut être modifié pendant que QGIS est ouvert, les modifications seront prises en compte. Pour relancer le script les fois suivantes, utiliser les commandes :

    reload(main)
    main.main()

Le fichier `main.py` se trouve dans le même répertoire que la carte QGIS. Les autres fichiers de code sont dans le répertoire `my_scripts`.


## Publier la carte ##

 - Installer QGIS Cloud plugin.
 - Ouvrir les options de QGIS Cloud. Menu - Extension - Cloud - Cloud Settings.
 - se connecter avec son login et mot de passe de QGIS.
 - onglet "Account". Sélectionner la database.
 - bouton "Delete database". (C'est long, et des fois ça se bloque tout seul. Faut redémarrer QGIS)
 - onglet "Upload Data". bouton Refresh layers.
 - les couches s'affichent. (pas forcément bien rangées mais c'est pas grave)
 - cocher "replace local layers in project"
 - bouton "upload data" tout en bas de la fenêtre de QGIS Cloud. (super long)
 - indiquer "enregistrer sous" si on le demande. Rechoisir le même fichier de carte. (Faut faire une sauvegarde avant de la carte offline)
 - éviter de se déplacer dans la carte.
 - onglet "Services", bouton "Publish map".
 - L'échelle initiale sera pas la même. Pas la peine d'essayer de faire un truc pil poil. Ça dépend de trucs complètement ésotérique tel que la taille de l'écran ou autre.
 - on peut changer des infos dans la configuration de la carte, et refaire "Publish map". Si on change des infos dans les données, il faut tout recommencer. (Désolé, pas de meilleure solution).


## Visualiser la carte ##

http://qgiscloud.com/Recher/odyssey_map

http://m.qgiscloud.com/Recher/odyssey_map