# -*- coding: utf-8 -*-

"""
    Récupère les données brutes provenant de différentes sources,
    et les rassemble, en détectant les incohérences (plus ou moins).
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info

from .bat_belt import join_unicode
from .coords import Coord
from .coord_rect import CoordRect
from . import reader_twinpedia
from . import reader_data_from_img

class Island(object):

    def __init__(self,
        island_twinpedia, island_img=None, geom_ok=False, warning=""):

        self.name = island_twinpedia.name
        self.nb_maps = island_twinpedia.nb_maps
        self.description = island_twinpedia.description
        self.warning = island_twinpedia.warning
        self.warning += warning
        self.geom_ok = geom_ok

        if island_img is None:
            self.coord_rect = CoordRect(coord_raw=island_twinpedia.coord)
            self.geom_ok = False
            self.warning += (";coordonnées incertaines. " +
                "introuvable dans la copie d'écran de la carte.")
        else:
            self.coord_rect = island_img.coord_rect

    def __unicode__(self):
        return join_unicode(
            self.name, " ",
            "(", self.coord_rect, ") ",
            "W:", self.warning)

class Sea(object):

    def __init__(self, sea_twinpedia, sea_img=None, warning=""):
        self.name = sea_twinpedia.name
        self.xp_min = sea_twinpedia.xp_min
        self.xp_max = sea_twinpedia.xp_max
        self.total_maps_required = sea_twinpedia.total_maps_required
        self.warning = sea_twinpedia.warning
        self.warning += warning
        self.islands = []

        if sea_img is None:
            # TODO : déduire une géométrie incertaine
            # à partir des islands contenues dans sea_twinpedia
            self.coord_rect = None
            self.geom_ok = False
            self.warning +=  (";coordonnées incertaines. " +
                "introuvable dans la copie d'écran de la carte.")
        else:
            self.coord_rect = sea_img.coord_rect
            self.geom_ok = True

    def __unicode__(self):
        sea_desc = join_unicode(self.name)
        islands_desc = [ "    " + unicode(island) for island in self.islands ]
        all_desc = [ sea_desc ] + islands_desc
        return "\n".join(all_desc)


def _twinpedia_candidates_of_island_img(seas_twinpedia, island_img):
    twinpedia_candidates = []
    for sea in seas_twinpedia:
        for island in sea.islands:
            # TODO : on recrée un CoordRect pour chaque islands twinpedia
            # à chaque fois qu'on appelle cette fonction. C'est pas top.
            rect_candidate = CoordRect(coord_raw=island.coord)
            if rect_candidate.intersects(island_img.coord_rect):
                twinpedia_candidates.append((sea, island))
    return twinpedia_candidates

def _check_coherency_one_sea(sea_twinpedia, sea_img):
    islands_twinpedia = list(sea_twinpedia.islands)
    islands_img = list(sea_img.islands)
    islands_ok = []
    islands_img_left = []

    for island_img in islands_img:

        # TODO : permettre d'indiquer le nom d'une île dans img_778N9.py,
        # pour une association directe. Parce que des fois,
        # on aura pas le choix, faudra spécifier l'association manuellement.

        intersecting_islands_twinpedia = []

        for island_twinpedia in islands_twinpedia:
            rect_candidate = CoordRect(coord_raw=island_twinpedia.coord)
            if rect_candidate.intersects(island_img.coord_rect):
                intersecting_islands_twinpedia.append(island_twinpedia)

        if not intersecting_islands_twinpedia:
            # Il manque une île dans twinpedia. On considère que tout est
            # foiré. On se casse.
            sea_twinpedia.warning += (";test échoué avec mer " +
                str(sea_img.coord_rect))
            return None
        elif len(intersecting_islands_twinpedia) == 1:
            # Correspondance super top. 1 pour 1. On crée une île finale.
            chosen_island_twinpedia = intersecting_islands_twinpedia[0]
            islands_ok.append(Island(
                chosen_island_twinpedia,
                island_img,
                True))
            islands_twinpedia.remove(chosen_island_twinpedia)
        else:
            # Plusieurs îles dans twinpedia pour la même île d'image.
            # Tant pis, on met un warning, et on créera des îles aux
            # coordonnées incertaines.
            for island_twinpedia in intersecting_islands_twinpedia:
                island_twinpedia.warning += (";hésitation avec " +
                    str(island_img.coord_rect))
            islands_img_left.append(island_img)

    for island_twinpedia in islands_twinpedia:
        islands_ok.append(Island(island_twinpedia))

    sea_ok = Sea(sea_twinpedia, sea_img)
    sea_ok.islands = islands_ok
    return sea_ok

def _find_first_sea_association(seas_twinpedia, seas_img):
    for current_sea_img in seas_img:
        for current_island_img in current_sea_img.islands:
            candidates = _twinpedia_candidates_of_island_img(
                seas_twinpedia,
                current_island_img)
            if len(candidates) == 1:
                sea_candidate_twinpedia = candidates[0][0]
                coherency_result = _check_coherency_one_sea(
                    sea_candidate_twinpedia, current_sea_img)
                if coherency_result is not None:
                    # Hop c'est cool. On renvoit cette association.
                    # On ne continue pas d'itérer, on s'en fout.
                    return (
                        coherency_result,
                        sea_candidate_twinpedia,
                        current_sea_img)
    return None

def _merge_twinpedia_img(seas_twinpedia, seas_img):
    seas_img_copy = list(seas_img)
    seas_twinpedia_copy = list(seas_twinpedia)
    seas_ok = []
    added_sea = True
    while added_sea:
        sea_association = _find_first_sea_association(
            seas_twinpedia_copy, seas_img_copy)
        if sea_association is not None:
            sea_ok, sea_twinpedia_assoc, sea_img_assoc = sea_association
            seas_ok.append(sea_ok)
            seas_twinpedia_copy.remove(sea_twinpedia_assoc)
            seas_img_copy.remove(sea_img_assoc)
            added_sea = True
        else:
            added_sea = False

    # TODO : prendre toutes les mers de twinpedia qui restent,
    # créer des mers finales avec. (Elles auront des coordonnées incertaines).
    return seas_ok

def build_data():
    seas_twinpedia = reader_twinpedia.parse_islands_and_seas()
    seas_img = reader_data_from_img.parse_data_from_img()
    seas = _merge_twinpedia_img(seas_twinpedia, seas_img)
    return seas


def test():
    seas = build_data()
    for sea in seas:
        info(unicode(sea))
        info("-" * 10)

if __name__ == "__main__":
    test()
