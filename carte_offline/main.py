# -*- coding: utf-8 -*-

"""
    Constructeur de carte. Module principal.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info
debug = logging.debug
logging.basicConfig(format="%(message)s", level=logging.INFO)

# TODO : ne marche pas pour l'instant. Mais ça viendra peut-être plus tard.
#import sys, imp
#def reload_all_modules(pakage_name):
#    modules_reloaded = [
#        imp.reload(v) for k, v in sys.modules.items()
#        if k.startswith(pakage_name) and v is not None
#    ]
#    info(modules_reloaded)

def test_coord_rect():
    import my_scripts.coord_rect
    my_scripts.coord_rect.test()

def test_coords():
    import my_scripts.coords
    my_scripts.coords.test()

def test_reader_data_from_img():
    import my_scripts.reader_data_from_img
    my_scripts.reader_data_from_img.test()

def test_reader_twinpedia():
    import my_scripts.reader_twinpedia
    my_scripts.reader_twinpedia.test()

def test_data_merger():
    import my_scripts.data_merger
    my_scripts.data_merger.test()

def test_qgis_recher_api():
    import my_scripts.qgis_recher_api
    reload(my_scripts.qgis_recher_api)
    my_scripts.qgis_recher_api.test()

def test_geom_tools():
    import my_scripts.geom_tools
    my_scripts.geom_tools.test()

def test_populate_map():
    import my_scripts.map_populator
    reload(my_scripts.map_populator)
    my_scripts.map_populator.test()

def make_map():
    import my_scripts.map_populator
    reload(my_scripts.map_populator)
    my_scripts.map_populator.populate()


def main():
    #function_to_call = test_coords
    #function_to_call = test_coord_rect
    #function_to_call = test_reader_data_from_img
    #function_to_call = test_reader_twinpedia
    #function_to_call = test_data_merger
    #function_to_call = test_qgis_recher_api
    #function_to_call = test_geom_tools
    #function_to_call = test_populate_map
    function_to_call = make_map
    function_to_call()

if __name__ == "__main__":
    main()