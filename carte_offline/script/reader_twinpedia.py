# -*- coding: utf-8 -*-

"""
    Interpréteur du fichier twinpedia.py,
    contenant les infos récupérées depuis le site twinpedia.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info
# TODO : foutre ça dans le main.
logging.basicConfig(format="%(message)s", level=logging.INFO)

from coords import Coord
from coord_rect import CoordRect
import donnees_brutes.twinpedia
twinpedia = donnees_brutes.twinpedia


class IslandTwinpedia(object):

    def __init__(self, name, coord, nb_maps, description):
        self.name = name
        self.coord = coord
        self.nb_maps = nb_maps
        self.description = description

    def str(self):
        return "".join((
            self.name, " ",
            "(", self.coord, ") ",
            "M:", self.nb_maps, " ",
            self.description))


class SeaTwinpedia(object):

    def __init__(self, name, xp_min, xp_max, total_maps_required):
        self.name = name
        self.xp_min = xp_min
        self.xp_max = xp_max
        self.total_maps_required = total_maps_required
        self.islands = []

    def str(self):
        sea_desc = "".join((
            self.name, " ",
            "XP:", xp_min, "-", xp_max, " ",
            "M:", total_maps_required))
        islands_desc = [ "    " + str(island) for island in self.islands ]
        all_desc = [ sea_desc ] + islands_desc
        return "\n".join(all_desc)


def parse_islands_and_seas(data):

    seas = []
    current_sea = None

    for data_line in data.split("\n"):
        data_line = data_line.strip()
        if data_line != "":
            before, coord, after = Coord.partition_odyssey_coord(data_line)

            if coord == "":

                info("mer : " + data_line)

            else:

                if current_sea is None: raise Exception("fail current sea")
                info("île : " + data_line)

    return seas


parse_islands_and_seas(twinpedia.ISLANDS_AND_SEAS)