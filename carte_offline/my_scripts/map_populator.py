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
# et incrémenter les identifieurs.

def coords_qgis_from_odyssey(points):
    """
    Inversion de l'axe y, à cause de ces cons de cartographe qui compte
    à l'envers par rapport au reste du monde. Excusez-moi mais l'axe y orienté
    vers le haut, ça correspond pas au sens de lecture, qui est une convention
    à peu près respecté par les gens utilisant l'alphabet latin (voire
    d'autres alphabets).
    """
    return [ (x * 1000, -y * 1000) for (x, y) in points ]

def _add_sea(sea, recher_api, layer):
    qgis_points = coords_qgis_from_odyssey(geom_tools.points_from_coord_rect(
        sea.coord_rect,
        not sea.geom_ok))
    recher_api.add_feature(
        layer,
        qgis_points,
        {
            # Toutes les données sont castées dans le type attendu par QGIS.
            # Comme ça, si on envoie de la merde, on s'en rend compte au
            # moment du cast. Et pas au moment de l'envoyer à QGIS, car je ne
            # sais pas comment il pourrait réagir.
            "identifier" : 12,
            "nom":unicode(sea.name),
            "carte_req":int(sea.maps_required),
            "carte_tot":int(sea.maps_total),
            "xp_min":int(sea.xp_min),
            "xp_max":int(sea.xp_max)})

def _add_island(island, recher_api, layer):
    qgis_points = coords_qgis_from_odyssey(geom_tools.points_from_coord_rect(
        island.coord_rect,
        not island.geom_ok))
    recher_api.add_feature(
        layer,
        qgis_points,
        {
            "identifier" : 13,
            "nom":unicode(island.name)})

def _layer_of_poi(poi, recher_api):
    layer_name = poi.kind
    return recher_api.layers[layer_name]

def _add_poi(poi, recher_api, layer):
    qgis_points = coords_qgis_from_odyssey( [ (poi.pos.x, poi.pos.y) ] )
    attributes = dict(poi.attributes)
    attributes["identifier"] = 14
    recher_api.add_feature(layer, qgis_points, attributes)

def populate(add_seas_islands=False, add_pois=False):

    recher_api = QgisRecherApi()
    seas, pois_unplaced = data_merger.build_data()

    if add_seas_islands:
        layer_mer = recher_api.layers["mer__pos"]
        layer_ile = recher_api.layers["ile__pos"]
        recher_api.delete_all_features(layer_mer)
        recher_api.delete_all_features(layer_ile)
        for sea in seas:
            _add_sea(sea, recher_api, layer_mer)
            for island in sea.islands:
                _add_island(island, recher_api, layer_ile)

    if add_pois:
        layers_cleaned = []
        # TODO : demander à la fonction build_data de balancer les poi
        # sous forme d'une liste simple.
        for raw_coord, pois_in_coord in pois_unplaced.items():
            for poi in pois_in_coord:
                layer = _layer_of_poi(poi, recher_api)
                if layer not in layers_cleaned:
                    recher_api.delete_all_features(layer)
                    layers_cleaned.append(layer)
                _add_poi(poi, recher_api, layer)

def test():
    pass

if __name__ == "__main__":
    test()
