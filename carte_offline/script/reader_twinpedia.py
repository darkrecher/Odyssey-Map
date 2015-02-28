# -*- coding: utf-8 -*-

"""
    Interpréteur du fichier twinpedia.py,
    contenant les infos récupérées depuis le site twinpedia.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info
# TODO : foutre ça dans le main.
logging.basicConfig(format="%(message)s", level=logging.INFO)

import donnees_brutes.twinpedia
twinpedia = donnees_brutes.twinpedia

info(twinpedia.BOSSES)

