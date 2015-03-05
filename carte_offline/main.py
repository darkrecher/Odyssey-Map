# -*- coding: utf-8 -*-

"""
    Constructeur de carte. Module principal.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info

import my_scripts.map_populator

def main():
    reload(my_scripts.map_populator)
    my_scripts.map_populator.test()

if __name__ == "__main__":
    main()