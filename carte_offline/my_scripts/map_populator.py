# -*- coding: utf-8 -*-

"""
    balance les objets dans la carte, à partir des classes Sea et Island
    créées précédemment.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info

# TODO : plus tard
#from .qgis_recher_api import QgisRecherApi
from .data_merger import build_data

def test():
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    seas = build_data()
    for sea in seas:
        info(unicode(sea))
        info("-" * 10)