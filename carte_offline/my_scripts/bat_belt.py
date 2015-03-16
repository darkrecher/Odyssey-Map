# -*- coding: utf-8 -*-

"""
Bat-belt. Tas de petites fonctions utiles partout.

créé par Réchèr. Licence CC-BY ou Art Libre.
https://github.com/darkrecher/Odyssey-Map
je prends les bitcoins : 12wF4PWLeVAoaU1ozD1cnQprSiKr6dYW1G
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)


def join_unicode(*param):
    # TODO : bon, c'est pas pratique comme truc, parce qu'on peut pas définir
    # le séparateur. Faut qu'on voye.
    param_unicoded = [ unicode(p) for p in param ]
    return "".join(param_unicoded)

def enum(enumName, *listValueNames):
    """
    Ma super fonction pour créer des type enums (comme en C++).

    :Example:
    CARROT_STATE = enum(
        "CARROT_STATE",      # il faut répéter le nom du type enum.
        "GRAIN",             # nom de l'état 1
        "GROWING",           # nom de l'état 2
        "OK",                # etc...
        "ROTTEN",
    )
    cst = CARROT_STATE
    current_state = cst.GROWING

    Pour plus de détail, voir mon article :
    http://sametmax.com/faire-des-enums-en-python/
    """
    # Une suite d'entiers, on en crée autant
    # qu'il y a de valeurs dans l'enum.
    listValueNumbers = range(len(listValueNames))
    # création du dictionaire des attributs.
    # Remplissage initial avec les correspondances : valeur d'enum -> entier
    dictAttrib = dict( zip(listValueNames, listValueNumbers) )
    # création du dictionnaire inverse. entier -> valeur d'enum
    dictReverse = dict( zip(listValueNumbers, listValueNames) )
    # ajout du dictionnaire inverse dans les attributs
    dictAttrib["dictReverse"] = dictReverse
    # création et renvoyage du type
    # Attention, la fonction type accepte en premier paramètre une
    # chaîne ASCII, et non pas une chaîne unicode. D'où le "str".
    mainType = type(str(enumName), (), dictAttrib)
    return mainType

""" orientations """
ORI = enum(
    "ORI",
    "RIGHT", "DOWN", "LEFT", "UP")

def first(the_iterable, default_val=None):
    """ Premier élément d'un itérable, quel qu'il soit.
    Renvoie default_val si l'itérable est vide.
    http://stackoverflow.com/a/2364277
    """
    return next( (x for x in the_iterable), default_val)

