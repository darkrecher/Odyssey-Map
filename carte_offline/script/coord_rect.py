# -*- coding: utf-8 -*-

"""
    Définit la classe CoordSquare
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
from fractions import Fraction

from coord import Coord

class CoordRect(object):
    """"
    Classe définissant les coordonnées d'un rectangle.
    Coin sup gauche, largeur et longueur, comme d'hab'.
    """

    def __init__(self, recher_n_rect="", x=None, y=None, w=None, h=None):
        self.x = Fraction()
        self.y = Fraction()
        self.w = Fraction()
        self.h = Fraction()
        self.set(recher_n_rect, x, y, w, h)

    def set(self, recher_n_rect="", x=None, y=None, w=None, h=None):
        if x is not None and y is not None and w is not None and h is not None:
            self.x = Fraction(x)
            self.y = Fraction(y)
            self.w = Fraction(w)
            self.h = Fraction(h)
        else:
            coords_rect = recher_n_rect.split(",")
            if len(coords_rect) < 2:
                # TODO : créer une exception spécifique. BadCoordinateArgument,
                # ou quelque chose comme ça. Ce serait classe.
                raise Exception("""
                    Notation réchèrienne incorrecte.
                    format : 000 0/,000 0/,000 0/,000 0/""")
            converted = Coord.recher_n_one_coord_converted
            x = coords_rect.pop(0)
            self.x = converted(x)
            y = coords_rect.pop(0)
            self.y = converted(y)
            if len(coords_rect):
                w = coords_rect.pop(0)
                self.w = converted(w)
            if len(coords_rect):
                h = coords_rect.pop(0)
                self.h = converted(h)
        self._determine_corners()

    def _determine_corners(self):
        self.coord_up_left = Coord(x=self.x, y=self.y)
        self.coord_up_right = Coord(x=self.x+self.w, y=self.y)
        self.coord_down_left = Coord(x=self.x, y=self.y+self.h)
        self.coord_down_right = Coord(x=self.x+self.w, y=self.y+self.h)








