# Question posée sur IndexError

http://indexerror.net/976/m%C3%A9thode-pas-trop-sale-pour-recharger-tous-modules-programme

Auteur : recher. Date : 2015-03-07.

## Méthode pas trop sale pour recharger tous les modules d'un programme 

Je suis en train de bosser sur un script dans QGIS (un SIG avec une console python intégrée). J'aimerais bien ne pas avoir à redémarrer tout QGIS à chaque fois que je veux tester la moindre modif effectuée dans un module.

Il faut donc que j'utilise la fonction reload(module). Mais je n'ai pas trouvé de meilleure solution que d'en mettre partout.

Pour chaque import fait dans chacun de mes modules, je dois ajouter un reload.

Ce code

    from .repertoire_1 import module_1

devient

    from .repertoire_1 import module_1
    reload(module_1)

Et ce code

    from .module_2 import fonction_A

devient :

    from . import module_2
    reload(module_2)
    fonction_A = module_2.fonction_A

Pour lancer mon script dans la console QGIS, je tape :

    reload(main)
    main.fonction_main()

Est-ce qu'il n'y a pas une solution plus élégante que d'indiquer des reload partout dans mon code ?

J'ai essayé de concentrer tous mes imports et reload au début du module main, histoire de confiner le code moche dans un même endroit.

    import repertoire_1.repertoire_2.module_1
    reload(repertoire_1.repertoire_2.module_1)
    import module_2
    reload(module_2)
    ...

Mais ça ne marche pas. Les changements effectués dans le code ne sont pas pris en compte au lancement du script.

Petite précision : le python de la console QGIS est en 2.7.5.
Je met `from __future__ import absolute_import` au début de chacun de mes modules.

#### Commentaire de Nsukami_ (2015-03-07)

Je pense a l'utilisation d'un ou deux decorateurs, mais pas encore tres sur :\


### Réponse de jc (2015-03-11)

Quelque chose du genre :

    import sys, imp
    def reload(pakage_name):
        [imp.reload(v) for k, v in sys.modules.items() if
         k.startswith(pakage_name) and v is not None 
        ]

Qui s'utiliserait avec le nom du module en argument :

    reload('my_root_module')

#### Commentaire de recher (2015-03-14)

Bon, ça ne marche pas très bien.

J'ai un module "main", tous mes autres modules sont dans un répertoire "my_scripts"

Dans le main, après tous les import, je fais ça :

    reload_all_modules('my_scripts')

(J'ai renommé ta fonction "reload" par "reload_all_modules", pour éviter que ça se conflicte avec la fonction built-in "reload"). J'ai commencé à enlever les exécutions de "reload" que j'avais semé un peu partout dans mon code.

Mais j'ai une erreur à l'exécution.

À un moment de mon code, j'ai ça :

    if isinstance(geom, Coord):
        # des trucs ...
    elif isinstance(geom, CoordRect):
        # d'autres trucs ...
    else:
        print("aaaargh")
        print("type(geom) : ", type(geom))
        print("CoordRect : ", CoordRect)
        print("isinstance : ", isinstance(geom, CoordRect))
        raise Exception("type attendu : Coord ou CoordRect")

Et dans la console QGIS, je me récupère ça :

    aaaargh
    type(geom) :  <class 'my_scripts.coord_rect.CoordRect'>
    CoordRect :  <class 'my_scripts.coord_rect.CoordRect'>
    isinstance :  False
    Traceback (most recent call last):
      ...
      File "C:/Recher/projets/git/Odyssey-Map/carte_offline\my_scripts\coord_rect.py", line 143, in intersects
        raise Exception("type attendu : Coord ou CoordRect")
    Exception: type attendu : Coord ou CoordRect        

Le "type(geom)"" et le "CoordRect" sont la même chose, pourtant isinstance ne passe pas. C'est très bizarre.

Je sais, les isinstance, c'est mal. Mais de là à me sortir une erreur aussi vilaine.

Quand je remets tous mes reload dans le code, je n'ai pas cette erreur.

Mon code est là si ça vous intéresse.
https://github.com/darkrecher/Odyssey-Map

Mais il y a plein de choses, c'est pas encore documenté, et je suis en train de bosser dessus donc il change de temps en temps.

Si j'ai le temps, j'essaye d'isoler le problème et de le rendre reproductible dans une console python. Mais ce sera pour plus tard.

#### Commentaire de bubulle (2015-03-17)

Pour ton erreur "isinstance(geom, CoordRect) == False", la seule explication que je vois serait que la classe "CoordRect" soit reconstruite après la création "geom".

Vu comme tu fais des import/reload dans tous les sens, ce ne serait pas étonnant.

Je vois que tu fais certains import dans des fonctions, peut-être est-ce à cause de ça ?

#### Commentaire de sam (2015-03-30)

Je ferais aussi un petit globals().clear() et locals().clear() pour bien virer toute les références.


### Réponse de vasywilly (2015-04-01)

je suis peut être à côté de la plaque mais jette un oeil à ces liens au cas où :

https://plugins.qgis.org/plugins/plugin_reloader/

http://osgeo-org.1560.x6.nabble.com/Changes-to-python-utils-py-td4977090.html

#### Commentaire de recher (2015-12-23)

Merci, mais je ne suis pas sûr que ce soit très utile pour ce que j'ai besoin de faire.

Le premier lien est une fonction pour recharger des plugins QGIS. Ces plugins sont également codé en python, mais je n'en suis même pas à faire ça. J'essaie juste de recharger des modules de code python dans la console de QGIS.

Le deuxième lien mène vers une librairie qui tracke et recharge les modules python. Ca ressemble à ce que fait la fonction reload(pakage_name), de manière un peu plus intelligente.

Sauf que je n'arrive pas à la faire fonctionner correctement, même dans la console python pur. Les modules chargés via "import myscripts.truc" sont trackés et réimportés. Mais pas les modules chargés via "from . import truc".

Et même si ça marchait, j'ai peur qu'on se retrouve avec la même erreur d'isinstance.


### Réponse de recher (2015-12-23)

(Je déterre la question 6 mois plus tard)

J'ai testé une autre méthode, d'après ce commentaire :
http://indexerror.net/976/m%C3%A9thode-pas-trop-sale-pour-recharger-tous-modules-programme?show=1201#c1201

 - Aucun reload dans mon code.
 - Pas de fonction reload(pakage_name)

Dans la console QGIS, j'effectue les actions suivantes :

    import main
    main.main()
    
    # exécution correcte de mon script
    
    # je modifie un fichier de code d'un module 
    # de mon script
    
    globals().clear()
    locals().clear()
    import main
    main.main()

Le script s'exécute sans planter, mais la modif effectuée précédemment n'a pas été prise en compte.

**Autre test :**

 - Aucun reload dans mon code.
 - Présence de la fonction reload(pakage_name), qui est appelée au début de la fonction main.main()

console QGIS :

    import main
    main.main()
    
    # exécution correcte 
    # pas de modif de code
    
    globals().clear()
    locals().clear()
    import main
    main.main()

Ça ne marche pas, j'ai l'erreur sur isinstance(). Le type de la variable geom (classe CoordRect) est considéré comme différent de la classe CoordRect elle-même. J'ai affiché les id, ils sont effectivement différents.

Bref, je n'ai toujours pas de solution propre, et pour l'instant je reste avec mes reload moches disséminés dans l'ensemble du code.

À dans 6 mois peut-être.

