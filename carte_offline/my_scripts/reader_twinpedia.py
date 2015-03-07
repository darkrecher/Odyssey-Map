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

    def __init__(self, name, coord, nb_maps, description, warning):
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

    def __init__(self, name, xp_min, xp_max, total_maps_required, warning=""):
        self.name = name
        self.xp_min = xp_min
        self.xp_max = xp_max
        self.total_maps_required = total_maps_required
        self.warning = warning
        self.islands = []

    def __unicode__(self):
        sea_desc = join_unicode(
            self.name, " ",
            "XP:", self.xp_min, "-", self.xp_max, " ",
            "M:", self.total_maps_required)
        islands_desc = [ "    " + unicode(island) for island in self.islands ]
        all_desc = [ sea_desc ] + islands_desc
        return "\n".join(all_desc)


def _parse_sea_line(data_line):
    xp_min = 0
    xp_max = 0
    nb_maps = 0
    warning = ""

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
            return None

    nb_maps_data = nb_maps_data.strip()
    if nb_maps_data == "":
        warning += ";nb cartes manquant"
    else:
        nb_maps, space, _ = nb_maps_data.partition(" ")
        if nb_maps == "?":
            warning += ";nb cartes manquant"
        else:
            try:
                nb_maps = int(nb_maps.strip())
            except ValueError:
                info("valeur de nb cartes incorrecte")
                return None

    return SeaTwinpedia(sea_name, xp_min, xp_max, nb_maps, warning)

def parse_island_line(before, coord, after):
    try:
        coord = Coord(odyssey_n=coord)
    except:
        info("valeur de coordonnée incorrecte")
        return None

    island_name = before.strip()
    nb_maps = -1
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

def parse_islands_and_seas(data=twinpedia.ISLANDS_AND_SEAS):

    seas = []
    current_sea = None

    for data_line in data.split("\n"):
        data_line = data_line.strip()
        if data_line != "":
            before, coord, after = Coord.partition_odyssey_coord(data_line)

            if coord == "":
                new_sea = _parse_sea_line(data_line)
                if new_sea is None:
                    info("Mer incorrecte (à moins que ce soit une île) :")
                    info(data_line)
                    info("-" * 10)
                else:
                    if current_sea is not None:
                        seas.append(current_sea)
                    current_sea = new_sea

            else:
                if current_sea is None: raise Exception("fail current sea")
                new_island = parse_island_line(before, coord, after)
                if new_island is None:
                    info("Île incorrecte :")
                    info(data_line)
                    info("-" * 10)
                else:
                    current_sea.islands.append(new_island)

    return seas


def test():
    seas = parse_islands_and_seas()
    for sea in seas:
        info(unicode(sea))
        info("-" * 10)

if __name__ == "__main__":
    test()