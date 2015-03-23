# -*- coding: utf-8 -*-

"""
    Interpréteur du fichier img_778N9.py,
    contenant les infos saisies à la main,
    à partir de l'image de la carte globale.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info
debug = logging.debug

from . import bat_belt
reload(bat_belt)
join_unicode = bat_belt.join_unicode
from . import coords
reload(coords)
Coord = coords.Coord
from . import coord_rect
reload(coord_rect)
CoordRect = coord_rect.CoordRect
from .donnees_brutes import twinpedia
reload(twinpedia)


class IslandTwinpedia(object):

    def __init__(self, name, coord, nb_maps=0, description="", warning=""):
        self.name = name
        self.coord = coord
        self.nb_maps = nb_maps
        self.description = description
        self.warning = warning

    def __unicode__(self):
        return join_unicode(
            self.name, " ",
            "(", self.coord, ") ",
            "M:", self.nb_maps, " ",
            self.description, " ",
            "W:", self.warning)

class SeaTwinpedia(object):

    def __init__(self, name, xp_min, xp_max, maps_required, warning=""):
        self.name = name
        self.xp_min = xp_min
        self.xp_max = xp_max
        self.maps_required = maps_required
        self.warning = warning
        self.islands = []

    def __unicode__(self):
        sea_desc = join_unicode(
            self.name, " ",
            "XP:", self.xp_min, "-", self.xp_max, " ",
            "M:", self.maps_required)
        islands_desc = [ "    " + unicode(island) for island in self.islands ]
        all_desc = [ sea_desc ] + islands_desc
        return "\n".join(all_desc)


def _parse_sea_line(data_line):
    xp_min = 0
    xp_max = 0
    nb_maps = -1
    warning = ""

    if ("Mer" not in data_line and
        "~" not in data_line and
        "XP" not in data_line and
        "(" not in data_line and
        "carte" not in data_line and
        ")" not in data_line):
        # On veut bien être permissif, mais y'a des limites.
        # Si on ne trouve aucun des tokens attendus dans la description
        # d'une mer, on laisse tomber.
        return None

    sea_name, parenthesis, sea_desc = data_line.partition("(")
    if parenthesis == "":
        warning += ";XP manquant;nb cartes manquant"
        new_sea = SeaTwinpedia(data_line.strip(), 0, 0, 0, warning)
        return new_sea
    sea_name = sea_name.strip()
    sea_desc = sea_desc.rstrip(")")
    xp_data, comma, nb_maps_data = sea_desc.partition(",")

    if xp_data.upper().endswith("XP"):
        xp_data = xp_data[:-2]
    xp_data = xp_data.lstrip("~")
    xp_data = xp_data.strip()
    if xp_data == "?":
        warning += ";XP manquant"
    else:
        xp_min, dash, xp_max = xp_data.partition("-")
        if dash == "":
            xp_max = xp_min
        try:
            xp_min = int(xp_min.strip())
            xp_max = int(xp_max.strip())
        except ValueError:
            info("valeur(s) de XP incorrecte(s)")
            # TODO : autoriser la création de la mer quand même ?
            return None

    nb_maps_data = nb_maps_data.strip()
    if nb_maps_data == "":
        warning += ";nb cartes manquant"
    else:
        nb_maps, space, _ = nb_maps_data.partition(" ")
        if nb_maps == "?":
            warning += ";nb cartes manquant"
            nb_maps = -1
        else:
            try:
                nb_maps = int(nb_maps.strip())
            except ValueError:
                info("valeur de nb cartes incorrecte")
                # TODO : autoriser la création de la mer quand même ?
                return None

    return SeaTwinpedia(sea_name, xp_min, xp_max, nb_maps, warning)

def _parse_island_line(before, coord, after):
    try:
        coord = Coord(odyssey_n=coord)
    except:
        info("valeur de coordonnée incorrecte")
        return None

    island_name = before.strip()
    nb_maps = None
    warning = ""
    after = after.strip()
    nb_maps_data, space, desc = after.partition(" ")
    warning_nb_maps = ""
    if nb_maps_data.endswith("?"):
        nb_maps_data = nb_maps_data[:-1]
        warning_nb_maps = ";nb cartes incertain"
    try:
        nb_maps = int(nb_maps_data)
    except ValueError:
        desc = after
        warning_nb_maps = ";nb cartes manquant ou incorrect"
    warning += warning_nb_maps
    desc = desc.strip()
    return IslandTwinpedia(island_name, coord, nb_maps, desc, warning)

def _manual_correction_before(data_line):
    """ Corrections manuelles du site twinpedia, avant le parsage.
    Il y a deux îles qui ont les caractères de coordonnées inversés.
    Le "°" (degré) et le "'" (apostrophe)
    """
    if data_line.startswith("Ile aux Hynas"):
        data_line = data_line.replace("-5' -22°", "-5° -22'")
    if data_line.startswith("Spegramanie"):
        data_line = data_line.replace("-2' -23°", "-2° -23'")
    return data_line

def _manual_correction_after(seas):
    """ Corrections manuelles du site Twinpedia. (après parsage des données)
    Si je ne les fais pas, je ne peux pas faire toutes les associations de
    mers et d'îles que je pourrais.
    Le but ultérieur serait de corriger Twinpedia pour ne plus avoir
    à faire ce genre de bidouille."""
    # Je vire la mer Orakiti, car manifestement, la seule île qu'elle
    # contient a une coordonnée fausse. (La coordonnée -15° -9 est déjà
    # dans une autre mer). Si je la laisse, je peux pas associer l'autre mer
    # Comme il faut.
    seas = [ sea for sea in seas if sea.name != "Mer Orakiti" ]
    # Ajout d'une île non mentionnée dans Twinpedia, dans la mer Magaos.
    sea_magaos = [ sea for sea in seas if "Magaos" in sea.name ]
    if sea_magaos:
        sea_magaos = sea_magaos[0]
        island_forgotten = IslandTwinpedia(
            "Pas de nom", Coord(x=-12, y=-10),
            nb_maps=0, description="",
            warning=";Non mentionnée dans Twinpedia.")
        sea_magaos.islands.append(island_forgotten)
    return seas

def iterate_not_empty_lines(data):
    # FUTURE : le jour où on aura un split qui renvoie un générateur,
    # faudra l'utiliser.
    for data_line in data.split("\n"):
        data_line = data_line.strip()
        if data_line != "":
            yield data_line

def parse_islands_and_seas(data=twinpedia.ISLANDS_AND_SEAS):

    seas = []
    current_sea = None

    for data_line in iterate_not_empty_lines(data):
        data_line = _manual_correction_before(data_line)
        before, coord, after = Coord.partition_odyssey_coord(data_line)

        if coord == "":
            new_sea = _parse_sea_line(data_line)
            if new_sea is None:
                # TODO : si on a une ligne pourrie, ça peut provoquer
                # des incertitudes sur l'ensemble de la mer en cours
                # (notammente le nombre total de cartes).
                info("Mer incorrecte (à moins que ce soit une île) :")
                info(data_line)
                info("-" * 10)
            else:
                if current_sea is not None:
                    seas.append(current_sea)
                current_sea = new_sea

        else:
            if current_sea is None: raise Exception("fail current sea")
            new_island = _parse_island_line(before, coord, after)
            if new_island is None:
                info("Île incorrecte :")
                info(data_line)
                info("-" * 10)
            else:
                current_sea.islands.append(new_island)

    return _manual_correction_after(seas)

def _parse_coords_only(data):
    coords = []
    for data_line in iterate_not_empty_lines(data):
        before, coord, after = Coord.partition_odyssey_coord(data_line)
        if before.strip() != "":
            raise Exception("ligne mal foutue : " + data_line)
        if after.strip() != "":
            raise Exception("ligne mal foutue : " + data_line)
        coords.append(Coord(odyssey_n=coord))
    return coords

def parse_temples(data=twinpedia.TEMPLES):
    return _parse_coords_only(data)

def parse_libraries(data=twinpedia.LIBRARIES):
    return _parse_coords_only(data)

def parse_fountains(data=twinpedia.FOUNTAINS):
    return _parse_coords_only(data)

def parse_potion_distillers(data=twinpedia.POTION_DISTILLERS):
    return _parse_coords_only(data)

def parse_food_bags(data=twinpedia.FOOD_BAGS):
    return _parse_coords_only(data)

def parse_ruins(data=twinpedia.RUINS):
    ruin_data = []
    for data_line in iterate_not_empty_lines(data):
        if "Nom de l'ile" in data and "Gain en or" in data_line:
            # C'est une ligne d'en-tête. On s'en fout.
            pass
        else:
            before, coord, after = Coord.partition_odyssey_coord(data_line)
            if before.strip() != "":
                raise Exception("ligne de 'ruine' mal foutue : " + data_line)
            # TODO : décomposer la description pour récupérer les attributs.
            description, gold, monsters = after.partition(" or ")
            description += gold
            description = description.strip()
            ruin_data.append( (Coord(odyssey_n=coord), description, monsters) )
    return ruin_data

def parse_inns(data=twinpedia.INNS):
    inn_data = []
    for data_line in iterate_not_empty_lines(data):
        before, coord, after = Coord.partition_odyssey_coord(data_line)
        if before.strip() != "":
            raise Exception("ligne de 'auberge' mal foutue : " + data_line)
        after = after.strip()
        after = after.lstrip("-")
        after = after.lstrip()
        cost, space, _ = after.partition(" ")
        if space != "":
            cost = int(cost)
        else:
            cost = -1
        inn_data.append( (Coord(odyssey_n=coord), cost) )
    return inn_data

def test():
    seas = parse_islands_and_seas()
    for sea in seas:
        info(unicode(sea))
        info("-" * 10)
    info("*" * 20)
    temple_coords = parse_temples()
    for coord in temple_coords:
        info(unicode(coord))
    info("*" * 20)
    ruin_data = parse_ruins()
    for coord, description, monsters in ruin_data:
        info(" : ".join( (unicode(coord), description, monsters) ))
    inn_data = parse_inns()

if __name__ == "__main__":
    test()