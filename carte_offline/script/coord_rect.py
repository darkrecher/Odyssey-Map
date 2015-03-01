# -*- coding: utf-8 -*-

"""
    Définit la classe CoordSquare
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
from fractions import Fraction

from coords import Coord

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
        if self.w < 0 or self.h < 0:
            raise Exception("taille de rectangle négative.")
        self._determine_corners()

    def _determine_corners(self):
        self.coord_up_left = Coord(x=self.x, y=self.y)
        self.coord_up_right = Coord(x=self.x+self.w, y=self.y)
        self.coord_down_left = Coord(x=self.x, y=self.y+self.h)
        self.coord_down_right = Coord(x=self.x+self.w, y=self.y+self.h)

    def _contains_point(self, coord):
        return (
            coord.x >= self.x and
            coord.y >= self.y and
            coord.x <= self.coord_down_right.x and
            coord.y <= self.coord_down_right.y)

    def includes(self, geom):
        if isinstance(geom, Coord):
            return self._contains_point(geom)
        else:
            raise Exception("type attendu : Coord ou CoordRect")

    def intersects(self, geom):
        if isinstance(geom, Coord):
            return self._contains_point(geom)
        else:
            raise Exception("type attendu : Coord ou CoordRect")


    def __str__(self):
        coord_size = Coord(x=self.w, y=self.h)
        return ", ".join((str(self.coord_up_left), str(coord_size)))


if __name__ == "__main__":

    info = logging.info
    logging.basicConfig(format="%(message)s", level=logging.INFO)

    rect = CoordRect("4, 5 1/, 6 2/, 7 2/")
    info(rect)
    info(rect.coord_down_right)
    info(rect.includes(Coord(recher_n="8 1/, 9 2/")))
    info(rect.includes(Coord(recher_n="11, 9 2/")))
    info(rect.includes(Coord(recher_n="8 1/, 13 1/")))

    rect = CoordRect("-4, -5 1/, 6 2/, 7 2/")
    info(rect)
    info(rect.coord_down_right)
    info(rect.includes(Coord(recher_n="-3 1/, -4 2/")))
    info(rect.includes(Coord(recher_n="3, -4 2/")))
    info(rect.includes(Coord(recher_n="-3 1/, 3")))
    info(rect.includes(Coord(recher_n="-3 1/, 3 1/")))

    rect = CoordRect("-4, -5 1/, 1/, 2/")
    info(rect)
    info(rect.coord_down_right)



