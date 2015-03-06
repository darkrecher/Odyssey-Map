# -*- coding: utf-8 -*-

"""
    Interpréteur du fichier twinpedia.py,
    contenant les infos récupérées depuis le site twinpedia.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info

from .bat_belt import join_unicode
from .coord_rect import CoordRect
from .donnees_brutes import img_778N9


class IslandImg(object):
    def __init__(self, coord_rect, descrip):
        self.coord_rect = coord_rect
        self.descrip = descrip
    def __unicode__(self):
        return join_unicode(self.coord_rect, " : ", self.descrip)

class SeaImg(object):
    def __init__(self, coord_rect):
        self.coord_rect = coord_rect
        self.islands = []
    def __unicode__(self):
        sea_desc = unicode(self.coord_rect)
        islands_desc = [ "    " + unicode(island) for island in self.islands ]
        all_desc = [ sea_desc ] + islands_desc
        return "\n".join(all_desc)


def parse_data_from_img(data=img_778N9.DATA):
    seas = []
    current_sea = None

    for data_line in data.split("\n"):
        data_line = data_line.strip()
        if data_line != "":
            data_type = data_line[0]
            data_line = data_line[1:]

            if data_type.upper() == "S":
                coord_rect = CoordRect(recher_n_rect=data_line)
                if current_sea is not None:
                    seas.append(current_sea)
                current_sea = SeaImg(coord_rect)

            elif data_type.upper() == "I":
                coord_rect_data, semicolon, descrip = data_line.partition(":")
                coord_rect = CoordRect(recher_n_rect=coord_rect_data)
                island = IslandImg(coord_rect, descrip)
                current_sea.islands.append(island)

            else:
                raise Exception("Type de donnée inconnu : " + data_type)

    return seas


def test():
    seas = parse_data_from_img()
    for sea in seas:
        info(unicode(sea))
        info("-" * 10)

if __name__ == "__main__":
    test()