# -*- coding: utf-8 -*-

"""
    balance les objets dans la carte, à partir des classes Sea et Island
    créées précédemment.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info
from fractions import Fraction

from . import qgis_recher_api
reload(qgis_recher_api)
QgisRecherApi = qgis_recher_api.QgisRecherApi
from . import data_merger
reload(data_merger)

# géométrie pure. Dans un module à part.

def garbled_line(coord_start, length, direction):
    # TODO : n'importe quelle direction.
    nb_points = int(length * 12)
    coords_x = [ coord_start.x ] * nb_points
    coords_y = [ coord_start.y ] * nb_points
    variation = [ Fraction(1, 12), Fraction(-1, 12) ] * int(nb_points / 2)
    steps = range(nb_points)
    steps = [ Fraction(1, 24) + Fraction(step, 12) for step in steps ]
    coords_x_and_vect = zip(coords_x, steps)
    coords_y_and_vect = zip(coords_y, variation)
    coords_x_final = [ pos + vect for (pos, vect) in coords_x_and_vect ]
    coords_y_final = [ pos + vect for (pos, vect) in coords_y_and_vect ]
    coords_xy = zip(coords_x_final, coords_y_final)
    coords_xy = [ (coord_start.x, coord_start.y) ] + coords_xy
    coords_xy = [ (float(xy[0]), float(xy[1])) for xy in coords_xy ]
    return coords_xy

def points_from_coord_rect(coord_rect, garble_lines):
    if garble_lines:
        dist_x = coord_rect.coord_up_right.x - coord_rect.coord_up_left.x
        points_rect = garbled_line(coord_rect.coord_up_left, dist_x, 0) + [
            (coord_rect.coord_up_right.x, coord_rect.coord_up_right.y),
            (coord_rect.coord_down_right.x, coord_rect.coord_down_right.y),
            (coord_rect.coord_down_left.x, coord_rect.coord_down_left.y),
        ]
    else:
        points_rect = [
            (coord_rect.coord_up_left.x, coord_rect.coord_up_left.y),
            (coord_rect.coord_up_right.x, coord_rect.coord_up_right.y),
            (coord_rect.coord_down_right.x, coord_rect.coord_down_right.y),
            (coord_rect.coord_down_left.x, coord_rect.coord_down_left.y),
        ]
    # TODO : ne pas appeler ça ici.
    return coords_qgis_from_odyssey(points_rect)

# TODO : ce sera mieux avec une classe. Pour stocker les layer et l'api.

def coords_qgis_from_odyssey(points):
    return [ (x, -y) for (x, y) in points ]

def _add_sea(sea, recher_api, layer):
    qgis_points = points_from_coord_rect(sea.coord_rect, not sea.geom_ok)
    recher_api.add_feature(
        layer,
        qgis_points,
        {"identifier" : 12, "nom":sea.name, "carte_req":3, "carte_tot":6, "or_tot":0}) # TODO

def _add_island(island, recher_api, layer):
    qgis_points = points_from_coord_rect(island.coord_rect, not island.geom_ok)
    island_name = island.name
    if not island.geom_ok:
        island_name = "??" + island_name + "??"
    recher_api.add_feature(
        layer,
        qgis_points,
        # TODO : homégénéité des majuscules dans les noms de champs.
        {"identifier" : 13, "Nom":island_name}) # TODO


def populate():

    recher_api = QgisRecherApi()
    layer_mer = recher_api.layers["mer"]
    layer_ile = recher_api.layers["ile"]
    seas = data_merger.build_data()
    recher_api.delete_all_features(layer_mer)
    recher_api.delete_all_features(layer_ile)

    for sea in seas:
        _add_sea(sea, recher_api, layer_mer)
        for island in sea.islands:
            _add_island(island, recher_api, layer_ile)


def test():
    from . import coords
    reload(coords)
    Coord = coords.Coord
    garbled = garbled_line(Coord(x=5, y=3), Fraction(4, 3), 0)
    info(unicode(garbled))

if __name__ == "__main__":
    test()