# -*- coding: utf-8 -*-

"""
    balance les objets dans la carte, à partir des classes Sea et Island
    créées précédemment.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info

from . import qgis_recher_api
reload(qgis_recher_api)
QgisRecherApi = qgis_recher_api.QgisRecherApi
from . import data_merger
reload(data_merger)
from . import geom_tools
reload(geom_tools)

# TODO : ce sera mieux avec une classe. Pour stocker les layer et l'api.

def coords_qgis_from_odyssey(points):
    """
    Inversion de l'axe y, à cause de ces cons de cartographe qui compte
    à l'envers par rapport au reste du monde. Excusez-moi mais l'axe y orienté
    vers le haut, ça correspond pas au sens de lecture, qui est une convention
    à peu près respecté par les gens utilisant l'alphabet latin (voire
    d'autres alphabets).
    """
    return [ (x, -y) for (x, y) in points ]

def _add_sea(sea, recher_api, layer):
    qgis_points = coords_qgis_from_odyssey(geom_tools.points_from_coord_rect(
        sea.coord_rect,
        not sea.geom_ok))
    recher_api.add_feature(
        layer,
        qgis_points,
        {"identifier" : 12, "nom":sea.name, "carte_req":3, "carte_tot":6, "or_tot":0}) # TODO

def _add_island(island, recher_api, layer):
    qgis_points = coords_qgis_from_odyssey(geom_tools.points_from_coord_rect(
        island.coord_rect,
        not island.geom_ok))
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
    pass

if __name__ == "__main__":
    test()
