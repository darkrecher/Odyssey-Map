# -*- coding: utf-8 -*-

"""
    Interpréteur du fichier twinpedia.py,
    contenant les infos récupérées depuis le site twinpedia.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info

from bat_belt import join_unicode
from coords import Coord
from coord_rect import CoordRect
import reader_twinpedia
import reader_data_from_img

class Island(object):

    def __init__(self, island_twinpedia, island_img, warning):
        self.name = island_twinpedia.name
        self.coord_rect = island_img.coord_rect
        self.nb_maps = island_twinpedia.nb_maps
        self.description = island_twinpedia.description
        self.warning = island_twinpedia.warning
        self.warning += warning
        self.geom_ok = geom_ok
        if not self.geom_ok:
            self.warning += ";coordonnées incertaines"

    def __unicode__(self):
        return join_unicode(
            self.name, " ",
            "(", self.coord, ") ",
            "W:", self.warning)

class Sea(object):

    def __init__(self, sea_twinpedia, sea_img, warning):
        self.name = sea_twinpedia.name
        self.xp_min = sea_twinpedia.xp_min
        self.xp_max = sea_twinpedia.xp_max
        self.total_maps_required = sea_twinpedia.total_maps_required
        self.warning = sea_twinpedia.warning
        self.warning += warning
        self.geom_ok = True
        # TODO : autoriser sea_img == None. Et déduire une géométrie incertaine
        # à partir des islands contenues dans sea_twinpedia
        self.islands = []

    def __unicode__(self):
        sea_desc = join_unicode(self.name)
        islands_desc = [ "    " + unicode(island) for island in self.islands ]
        all_desc = [ sea_desc ] + islands_desc
        return "\n".join(all_desc)


def _merge_twinpedia_img(seas_twinpedia, seas_img):
    return []


def build_data():
    seas_twinpedia = reader_twinpedia.parse_islands_and_seas()
    seas_img = reader_data_from_img.parse_data_from_img()
    seas = _merge_twinpedia_img(seas_twinpedia, seas_img)
    return seas


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    seas = build_data()
    for sea in seas:
        info(unicode(sea))
        info("-" * 10)


