# -*- coding: utf-8 -*-

"""
    balance les objets dans la carte, à partir des classes Sea et Island
    créées précédemment.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info

import qgis._core
import qgis.core
NULL = qgis.core.NULL

from qgis_recher_api import QgisRecherApi

def square_coords(x, y, w, h):
    return [
        (x, y),
        (x + w, y),
        (x + w, y + h),
        (x, y + h)
    ]

def test():

    recher = QgisRecherApi(qgis.utils.iface)
    layer = recher.layers["mer"]

    #recher.add_feature(
    #    layer,
    #    [(-0.5, -1.0), (-0.5, 1.5), (-1.0, 1.5), (-1.0, 0.5)],
    #    {"identifier" : 20, "Nom" : "pouetzz"})

    recher.add_feature(
        layer,
        square_coords(-1 + 2.0/3.0, -(-1 + 2.0/3.0), 2 + 1.0/3.0, -3),
        {"identifier" : 0, "nom":"M. du Destin", "carte_req":3, "carte_tot":6, "or_tot":0})

    recher.add_feature(
        layer,
        square_coords(2, -(-1 + 2.0/3.0), 4 + 2.0/3.0, -3),
        {"identifier":1, "nom":"Kyfi", "carte_req":3, "carte_tot":6, "or_tot":30})

    recher.add_feature(
        layer,
        square_coords(-1, -(2 + 2.0/3.0), 4, -3),
        {"identifier":2, "nom":"Arème", "carte_req":3, "carte_tot":6, "or_tot":0})
