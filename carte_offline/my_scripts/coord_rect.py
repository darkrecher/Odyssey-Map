# -*- coding: utf-8 -*-

"""
    Définit la classe CoordRect.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info
debug = logging.debug
from fractions import Fraction

from . import coords
reload(coords)
Coord = coords.Coord
from . import bat_belt
reload(bat_belt)
ORI = bat_belt.ORI


class CoordRect(object):
    """"
    Classe définissant les coordonnées d'un rectangle.
    Coin sup gauche, largeur et longueur, comme d'hab'.
    """

    def __init__(self,
        recher_n_rect="", coord_up_left=None,
        x=None, y=None, w=None, h=None):

        self.x = Fraction()
        self.y = Fraction()
        self.w = Fraction()
        self.h = Fraction()
        self.set(recher_n_rect, coord_up_left, x, y, w, h)

    def set(self,
        recher_n_rect="", coord_up_left=None,
        x=None, y=None, w=None, h=None):

        if recher_n_rect != "":
            coords_rect = recher_n_rect.split(",")
            if len(coords_rect) < 2:
                # TODO : créer une exception spécifique. BadCoordArgument,
                # ou quelque chose comme ça. Ce serait classe.
                raise Exception("""
                    Notation réchèrienne incorrecte.
                    format : 000 0/,000 0/,000 0/,000 0/""")
            converted = Coord.recher_n_one_coord_converted
            recher_x = coords_rect.pop(0)
            self.x = converted(recher_x)
            recher_y = coords_rect.pop(0)
            self.y = converted(recher_y)
            if coords_rect:
                recher_w = coords_rect.pop(0)
                self.w = converted(recher_w)
            if coords_rect:
                recher_h = coords_rect.pop(0)
                self.h = converted(recher_h)

        if coord_up_left is not None:
            self.x = Fraction(coord_up_left.x)
            self.y = Fraction(coord_up_left.y)
        if x is not None: self.x = Fraction(x)
        if y is not None: self.y = Fraction(y)
        if w is not None: self.w = Fraction(w)
        if h is not None: self.h = Fraction(h)

        if self.w < 0 or self.h < 0:
            raise Exception("taille de rectangle négative.")
        self._determine_corners()

    def _determine_corners(self):
        self.coord_up_left = Coord(x=self.x, y=self.y)
        self.coord_up_right = Coord(x=self.x+self.w, y=self.y)
        self.coord_down_left = Coord(x=self.x, y=self.y+self.h)
        self.coord_down_right = Coord(x=self.x+self.w, y=self.y+self.h)

    def _contains_point(self,
        coord, bnds_incl=(ORI.UP, ORI.RIGHT, ORI.DOWN, ORI.LEFT)):
        return (
            (
                (ORI.LEFT in bnds_incl and coord.x >= self.coord_up_left.x)
                or coord.x > self.coord_up_left.x
            )
            and
            (
                (ORI.UP in bnds_incl and coord.y >= self.coord_up_left.y)
                or coord.y > self.coord_up_left.y
            )
            and
            (
                (ORI.RIGHT in bnds_incl and coord.x <= self.coord_down_right.x)
                or coord.x < self.coord_down_right.x
            )
            and
            (
                (ORI.DOWN in bnds_incl and coord.y <= self.coord_down_right.y)
                or coord.y < self.coord_down_right.y
            )
        )

    def includes(self, geom):
        if isinstance(geom, Coord):
            return self._contains_point(geom)
        elif isinstance(geom, CoordRect):
            return (
                self._contains_point(geom.coord_up_left) and
                self._contains_point(geom.coord_down_right))
        else:
            raise Exception("type attendu : Coord ou CoordRect")

    def intersects(self, geom, bounds_included=True):
        if isinstance(geom, Coord):
            if bounds_included:
                bounds_included = (ORI.UP, ORI.RIGHT, ORI.DOWN, ORI.LEFT)
            else:
                bounds_included = ()
            return self._contains_point(geom, bounds_included)
        elif isinstance(geom, CoordRect):
            if bounds_included:
                return (
                    self._contains_point(geom.coord_up_left) or
                    self._contains_point(geom.coord_down_right) or
                    geom._contains_point(self.coord_up_left) or
                    geom._contains_point(self.coord_down_right))
            else:
                bnds_ul = (ORI.UP, ORI.LEFT)
                bnds_dr = (ORI.DOWN, ORI.RIGHT)
                return (
                    self._contains_point(geom.coord_up_left, bnds_ul) or
                    self._contains_point(geom.coord_down_right, bnds_dr) or
                    geom._contains_point(self.coord_up_left, bnds_ul) or
                    geom._contains_point(self.coord_down_right, bnds_dr))
        else:
            debug("aaaargh")
            debug("type(geom) : " + str(type(geom)))
            debug("CoordRect : " + str(CoordRect))
            debug("isinstance : " + str(isinstance(geom, CoordRect)))
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

    def inflate(self, w_infl, h_infl=None):
        if h_infl is None:
            h_infl = w_infl
        self.x -= w_infl
        self.y -= h_infl
        self.w += w_infl + w_infl
        self.h += h_infl + h_infl
        self._determine_corners()

    def __str__(self):
        coord_size = Coord(x=self.w, y=self.h)
        return ", ".join((str(self.coord_up_left), str(coord_size)))

    @staticmethod
    def bounding_rect(rects):
        # TODO : accepter des Coord, en plus des CoordRect.
        x_min = []
        x_max = []
        y_min = []
        y_max = []
        for rect in rects:
            x_min.append(rect.coord_up_left.x)
            x_min = [ min(x_min) ]
            x_max.append(rect.coord_down_right.x)
            x_max = [ max(x_max) ]
            y_min.append(rect.coord_up_left.y)
            y_min = [ min(y_min) ]
            y_max.append(rect.coord_down_right.y)
            y_max = [ max(y_max) ]
        if x_min:
            x = x_min[0]
            y = y_min[0]
            w = x_max[0] - x
            h = y_max[0] - y
            return CoordRect(x=x, y=y, w=w, h=h)
        else:
            return None


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
    info("test intersect avec les bords")
    info(rect.intersects(CoordRect("10 2/, 5 2/, 1/, 1/")))
    info(rect.intersects(CoordRect("10 2/, 5 2/, 1/, 1/"), False))
    info(rect.intersects(CoordRect("4 1/, 13, 1/, 1/")))
    info(rect.intersects(CoordRect("4 1/, 13, 1/, 1/"), False))
    info(rect.intersects(CoordRect("3 1/, 5 2/, 2/, 1/")))
    info(rect.intersects(CoordRect("3 1/, 5 2/, 2/, 1/"), False))
    info("test intersect pas tout compris")
    rect_spenes = CoordRect("1 2/, -13 2/, 0 1/, 0 2/")
    rect_img = CoordRect("1, -12, 1, 1")
    info(rect_spenes.intersects(rect_img, False))
    info(rect_img.intersects(rect_spenes, False))


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

    try:
        rect.intersects("hahaha")
    except:
        pass

    rect = CoordRect("-4, -5 1/, 1/, 2/")
    info(rect)
    info(rect.coord_down_right)

    rect = CoordRect.bounding_rect((
        CoordRect("4 1/, 13, 1/, 1/"),
        CoordRect("2 1/, 10, 1/, 1/"),
        CoordRect("3 2/, 12 2/, 10, 10"),
    ))
    info("bounding")
    info(rect)
    rect.inflate(Fraction(1, 3))
    info("inflate")
    info(rect)

if __name__ == "__main__":
    test()