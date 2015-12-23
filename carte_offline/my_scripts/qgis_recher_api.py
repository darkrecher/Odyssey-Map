# -*- coding: utf-8 -*-

"""
    Interface entre QGis et les trucs que je veux faire.
"""

# TODO : commenter tout ce bordel

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import qgis._core
import qgis.core
NULL = qgis.core.NULL


class QgisRecherApi(object):

    def __init__(self):
        self.iface = qgis.utils.iface
        self.layers = {}
        self._fill_layer_dict()

    def _fill_layer_dict(self):
        # Attention, on ne récupère que les layers visibles.
        # Ceux qui sont cochés dans QGIS.
        list_layers = self.iface.mapCanvas().layers()
        for layer in list_layers:
            if layer.type() == qgis._core.QgsMapLayer.VectorLayer:
                name = layer.name()
                self.layers[name] = layer

    def add_feature(self,
        layer, geom_points, attributes,
        attrib_name_identifier="identifier"):

        layer.startEditing()
        pr = layer.dataProvider()
        feature_creating = qgis._core.QgsFeature()

        if len(geom_points) == 1:
            # On ajoute un point
            x, y = geom_points[0]
            qgs_geom_point = qgis._core.QgsPoint(x, y)
            feature_creating.setGeometry(
                qgis._core.QgsGeometry.fromPoint(qgs_geom_point))
        else:
            # On ajoute un polygone.
            # TODO : pour l'instant on peut pas ajouter de ligne.
            # L'API va forcément changer quand je rajouterai cette fonction.
            # C'est vilain de pas le prévoir tout de suite, mais on fera avec.
            qgs_geom_points = [ qgis._core.QgsPoint(x, y) for x, y in geom_points ]
            feature_creating.setGeometry(
                qgis._core.QgsGeometry.fromPolygon([qgs_geom_points]))

        pr.addFeatures([feature_creating])
        layer.updateExtents()
        layer.commitChanges()

        feature_created = None
        for feat in layer.getFeatures():
            if feat.attribute(attrib_name_identifier) == NULL:
                feature_created = feat

        if feature_created is not None:
            layer.startEditing()
            for key_attr, val_attr in attributes.items():
                feat[key_attr] = val_attr
            layer.updateFeature(feat)
            layer.commitChanges()

    def delete_all_features(self, layer_to_clean):
        list_id_to_delete = [ f.id() for f in layer_to_clean.getFeatures() ]
        layer_to_clean.startEditing()
        layer_to_clean.dataProvider().deleteFeatures(list_id_to_delete)
        layer_to_clean.commitChanges()


def test():

    def square_coords(x, y, w, h):
        return [
            (x, y),
            (x + w, y),
            (x + w, y + h),
            (x, y + h)
        ]

    recher = QgisRecherApi()
    layer = recher.layers["mer"]
    recher.delete_all_features(layer)

    recher.add_feature(
        layer,
        square_coords(-1 + 2.0/3.0, -(-1 + 2.0/3.0), 2 + 1.0/3.0, -3),
        {
            "identifier" : 0, "nom":"M. Destin", "carte_req":3, "carte_tot":6})
    recher.add_feature(
        layer,
        square_coords(2, -(-1 + 2.0/3.0), 4 + 2.0/3.0, -3),
        {
            "identifier":1, "nom":"Kyfi", "carte_req":3, "carte_tot":6})
    recher.add_feature(
        layer,
        square_coords(-1, -(2 + 2.0/3.0), 4, -3),
        {
            "identifier":2, "nom":"Arème", "carte_req":3, "carte_tot":6})

    layer = recher.layers["ile"]
    recher.delete_all_features(layer)

    recher.add_feature(
        layer,
        square_coords(0, -(0), 2.0/3.0, -2.0/3.0),
        {"identifier" : 100, "nom" : "Île de l'oracle"})
    recher.add_feature(
        layer,
        square_coords(1 + 1.0/3.0, -(1.0/3.0), 1.0/3.0, -1.0/3.0),
        {"identifier" : 100, "nom" : "Île Rékiphie"})
    recher.add_feature(
        layer,
        square_coords(1, -(2), 1.0/3.0, -1.0/3.0),
        {"identifier" : 100, "nom" : "Île Spelulogos"})
    recher.add_feature(
        layer,
        square_coords(0, -(2), 1.0/3.0, -1.0/3.0),
        {"identifier" : 100, "nom" : "Récif des Enas"})
    recher.add_feature(
        layer,
        square_coords(1, -(1), 1.0/3.0, -1.0/3.0),
        {"identifier" : 100, "nom" : "Île du Tahépe"})
    recher.add_feature(
        layer,
        square_coords(1 + 1.0/3.0, -(1), 1.0/3.0, -1.0/3.0),
        {"identifier" : 100, "nom" : "Île Ganes"})

    layer = recher.layers["temple"]
    recher.delete_all_features(layer)
    recher.add_feature(
        layer,
        [(1, 1)],
        {"identifier" : 200})

if __name__ == "__main__":
    test()
