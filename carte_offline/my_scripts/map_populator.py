# -*- coding: utf-8 -*-

"""
    balance les objets dans la carte, à partir des classes Sea et Island
    créées précédemment.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info

from .qgis_recher_api import QgisRecherApi
from .data_merger import build_data

# TODO : ce sera mieux avec une classe. Pour stocker les layer et l'api.

def _qgis_points_from_coord_rect(coord_rect):
    return [
        (coord_rect.coord_up_left.x, -coord_rect.coord_up_left.y),
        (coord_rect.coord_up_right.x, -coord_rect.coord_up_right.y),
        (coord_rect.coord_down_right.x, -coord_rect.coord_down_right.y),
        (coord_rect.coord_down_left.x, -coord_rect.coord_down_left.y),
    ]

def _add_sea(sea, recher_api, layer):
    qgis_points = _qgis_points_from_coord_rect(sea.coord_rect)
    recher_api.add_feature(
        layer,
        qgis_points,
        {"identifier" : 12, "nom":sea.name, "carte_req":3, "carte_tot":6, "or_tot":0}) # TODO

def _add_island(island, recher_api, layer):
    qgis_points = _qgis_points_from_coord_rect(island.coord_rect)
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
    seas = build_data()
    recher_api.delete_all_features(layer_mer)
    recher_api.delete_all_features(layer_ile)

    for sea in seas:
        _add_sea(sea, recher_api, layer_mer)
        for island in sea.islands:
            _add_island(island, recher_api, layer_ile)

if __name__ == "__main__":
    populate()