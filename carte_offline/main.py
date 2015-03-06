# -*- coding: utf-8 -*-

"""
    Constructeur de carte. Module principal.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info

def main():

    import my_scripts.map_populator
    reload(my_scripts.map_populator)
    my_scripts.map_populator.test()

    #import my_scripts.qgis_recher_api
    #reload(my_scripts.qgis_recher_api)
    #my_scripts.qgis_recher_api.test()

if __name__ == "__main__":
    main()