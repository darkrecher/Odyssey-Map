# -*- coding: utf-8 -*-

"""
    Définit la classe PointOfInterest.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info
debug = logging.debug

from . import bat_belt
reload(bat_belt)
join_unicode = bat_belt.join_unicode

class PointOfInterest(object):
    """"
    POI (Point Of Interest).
    Point d'intérêt sur la carte (héros, temple, ruine, ...)
    La position n'est pas définie à l'initialisation.
    C'est le code extérieur qui s'en occupe, car il doit répartir les POI
    qui sont positionnés au même endroit.
    """

    def __init__(self, kind, attributes):
        self.kind = kind
        self.attributes = attributes
        self.pos = None

    def __unicode__(self):
        return join_unicode(
            self.kind, ". ",
            self.attributes, ". ",
            self.pos)

