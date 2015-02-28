# -*- coding: utf-8 -*-

"""
    Définit la classe Coord
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
from fractions import Fraction


class Coord(object):
    """"
    Classe de base, pour manipuler les coordonnées du jeu.
    """
    def __init__(self, odyssey_n="", recher_n="", x=None, y=None):
        self.x = Fraction()
        self.y = Fraction()
        self.set(odyssey_n, recher_n, x, y)

    def _recher_notation_one_coord_converted(self, one_coord):
        int_part, space, fract_part = one_coord.strip().partition(" ")
        int_part = int_part.strip()
        int_part = Fraction(int(int_part), 1)
        numerator, divisor, denominator = fract_part.partition("/")

        if divisor == "/":
            denominator = denominator.strip()
            if denominator == "":
                denominator = 3
            else:
                denominator = int(denominator)
            numerator = int(numerator)
            fract_part = Fraction(numerator, denominator)
        else:
            fract_part = Fraction(0, 1)

        return int_part + fract_part

    def set(self, odyssey_n="", recher_n="", x=None, y=None):
        if x is not None and y is not None:
            self.x = Fraction(x)
            self.y = Fraction(y)
        elif recher_n != "":
            x, comma, y = recher_n.partition(",")
            if comma == "":
                raise Exception(
                    "Notation réchèrienne incorrecte. format : 000 0/,000 0/")
            self.x = self._recher_notation_one_coord_converted(x)
            self.y = self._recher_notation_one_coord_converted(y)
        elif odyssey_n != "":
            # TODO
            pass



if __name__ == "__main__":

    info = logging.info
    # TODO : foutre ça dans le main.
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    coord = Coord(x=0, y=0)
    info(coord._recher_notation_one_coord_converted("2 1/"))
    info(coord._recher_notation_one_coord_converted("   -1    "))
    info(coord._recher_notation_one_coord_converted("-5    2/    "))
    coord = Coord(recher_n="1 2/, 3 1/")
    info((coord.x, coord.y))
    coord = Coord()
    info((coord.x, coord.y))

