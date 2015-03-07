# -*- coding: utf-8 -*-

"""
    Définit la classe CoordRect.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info
from fractions import Fraction

from . import coords
reload(coords)
Coord = coords.Coord


class CoordRect(object):
    """"
    Classe définissant les coordonnées d'un rectangle.
    Coin sup gauche, largeur et longueur, comme d'hab'.
    """

    def __init__(self,
        recher_n_rect="", coord_raw=None,
        x=None, y=None, w=None, h=None):

        self.x = Fraction()
        self.y = Fraction()
        self.w = Fraction()
        self.h = Fraction()
        self.set(recher_n_rect, coord_raw, x, y, w, h)

    def set(self,
        recher_n_rect="", coord_raw=None,
        x=None, y=None, w=None, h=None):

        if x is not None and y is not None and w is not None and h is not None:
            self.x = Fraction(x)
            self.y = Fraction(y)
            self.w = Fraction(w)
            self.h = Fraction(h)
        elif coord_raw is not None:
            self.x = Fraction(coord_raw.x)
            self.y = Fraction(coord_raw.y)
            self.w = Fraction(2, 3)
            self.h = Fraction(2, 3)
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
            if coords_rect:
                w = coords_rect.pop(0)
                self.w = converted(w)
            if coords_rect:
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
        elif isinstance(geom, CoordRect):
            return (
                self._contains_point(geom.coord_up_left) and
                self._contains_point(geom.coord_down_right))
        else:
            raise Exception("type attendu : Coord ou CoordRect")

    def intersects(self, geom):
        if isinstance(geom, Coord):
            return self._contains_point(geom)
        elif isinstance(geom, CoordRect):
            return (
                self._contains_point(geom.coord_up_left) or
                self._contains_point(geom.coord_down_right) or
                geom._contains_point(self.coord_up_left) or
                geom._contains_point(self.coord_up_right))
        else:
            raise Exception("type attendu : Coord ou CoordRect")

    def move(self, vector):
        self.x += vector.x
        self.y += vector.y
        self._determine_corners()

    def add_to_size(self, w_inc=0, h_inc=0):
        self.w += w_inc
        self.h += h_inc
        # On ne permet pas d'avoir une taille inférieure à 0.
        self.w = max(self.w, 0)
        self.h = max(self.h, 0)
        self._determine_corners()

    def set_min_size(self, w_min=0, h_min=0):
        self.w = max(self.w, w_min)
        self.h = max(self.h, h_min)
        self._determine_corners()

    def __str__(self):
        coord_size = Coord(x=self.w, y=self.h)
        return ", ".join((str(self.coord_up_left), str(coord_size)))


def test():
    rect = CoordRect("4, 5 1/, 6 2/, 7 2/")
    info(rect)
    info(rect.coord_down_right)
    info(rect.includes(Coord(recher_n="8 1/, 9 2/")))
    info(rect.includes(Coord(recher_n="11, 9 2/")))
    info(rect.includes(Coord(recher_n="8 1/, 13 1/")))
    info("test include et intersect de rects")
    info(rect.includes(CoordRect("7 1/, 9 2/, 2 2/, 2 1/")))
    info(rect.intersects(CoordRect("7 1/, 9 2/, 2 2/, 2 1/")))
    info(rect.includes(CoordRect("7 1/, 9 2/, 12 2/, 2 1/")))
    info(rect.intersects(CoordRect("7 1/, 9 2/, 12 2/, 2 1/")))

    rect = CoordRect("-4, -5 1/, 6 2/, 7 2/")
    info(rect)
    info(rect.coord_down_right)
    info(rect.includes(Coord(recher_n="-3 1/, -4 2/")))
    info(rect.includes(Coord(recher_n="3, -4 2/")))
    info(rect.includes(Coord(recher_n="-3 1/, 3")))
    info(rect.includes(Coord(recher_n="-3 1/, 3 1/")))
    info("test include et intersect de rects")
    info(rect.includes(CoordRect("1/, 2/, 1 2/, 2 1/")))
    info(rect.intersects(CoordRect("1/, 2/, 1 2/, 2 1/")))
    info(rect.includes(CoordRect("1/, 2/, 12 2/, 2 1/")))
    info(rect.intersects(CoordRect("1/, 2/, 12 2/, 2 1/")))

    rect = CoordRect("-4, -5 1/, 1/, 2/")
    info(rect)
    info(rect.coord_down_right)

if __name__ == "__main__":
    test()