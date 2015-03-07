# -*- coding: utf-8 -*-

"""
    Constructeur de carte. Module principal.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info
logging.basicConfig(format="%(message)s", level=logging.INFO)


def main():

    #import my_scripts.coord_rect
    #my_scripts.coord_rect.test()

    #import my_scripts.coords
    #my_scripts.coords.test()

    #import my_scripts.reader_data_from_img
    #my_scripts.reader_data_from_img.test()

    #import my_scripts.reader_twinpedia
    #my_scripts.reader_twinpedia.test()

    #import my_scripts.data_merger
    #my_scripts.data_merger.test()

    #import my_scripts.qgis_recher_api
    #reload(my_scripts.qgis_recher_api)
    #my_scripts.qgis_recher_api.test()

    import my_scripts.map_populator
    reload(my_scripts.map_populator)
    # TODO forcer ce con de QGIS à recharger mes trucs. Mais là, ça marche pô.
    import my_scripts.donnees_brutes.img_778N9
    reload(my_scripts.donnees_brutes.img_778N9)
    my_scripts.map_populator.populate()

if __name__ == "__main__":
    main()