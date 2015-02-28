# -*- coding: utf-8 -*-

"""
    Définit la classe Coord
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
import re
from fractions import Fraction


class Coord(object):
    """"
    Classe de base, pour manipuler les coordonnées du jeu.
    """

    REGEXP_ODYSSEY_COORDINATES = re.compile("""
        (              # les caractères définissant
                       # la coordonnée odyssienne commencent ici

            # première coordonnée (le X)
            \-?        # éventuellement, le signe "moins"
            [0-9]+     # au moins un chiffre

            # séparateur des coordonnées.
            \s*°\s*    # éventuellement des espaces, le signe "degré",
                       # et encore éventuellement des espaces.

            # deuxième coordonnée (le Y)
            \-?        # éventuellement, le signe "moins"
            [0-9]+     # au moins un chiffre

        )              # les caractères définissant
                       # la coordonnée odyssienne s'arrêtent ici

        .*             # tout et n'importe quoi. On s'en fout.
        """,
        re.VERBOSE)

    @staticmethod
    def may_contain_odyssey_coord(data):
        return "°" in data

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
                # TODO : créer une exception spécifique. BadCoordinateArgument,
                # ou quelque chose comme ça. Ce serait classe.
                raise Exception(
                    "Notation réchèrienne incorrecte. format : 000 0/,000 0/")
            self.x = self._recher_notation_one_coord_converted(x)
            self.y = self._recher_notation_one_coord_converted(y)

        elif odyssey_n != "":
            search_result = Coord.REGEXP_ODYSSEY_COORDINATES.search(odyssey_n)
            if search_result is None:
                raise Exception(
                    "Notation odyssienne incorrecte. format : 000 ° 000")
            search_result_groups = search_result.groups()
            if len(search_result_groups) < 1:
                raise Exception(
                    "Notation odyssienne incorrecte. format : 000 ° 000")
            odyssey_n_extracted = search_result_groups[0]
            x, degree, y = odyssey_n_extracted.partition("°")
            x = x.strip()
            y = y.strip()
            self.x = Fraction(int(x), 1)
            self.y = Fraction(int(y), 1)

    def __str__(self):
        pass # TODO


if __name__ == "__main__":

    info = logging.info
    logging.basicConfig(format="%(message)s", level=logging.INFO)

    # TODO : ajouter des asserts si on est motivé. Ou bien utiliser pytest.

    coord = Coord(x=0, y=0)
    info(coord._recher_notation_one_coord_converted("2 1/"))
    info(coord._recher_notation_one_coord_converted("   -1    "))
    info(coord._recher_notation_one_coord_converted("-5    2/    "))

    info(Coord.may_contain_odyssey_coord("aaaabbb"))
    info(Coord.may_contain_odyssey_coord("aaaa°bbb"))

    coord = Coord()
    info((coord.x, coord.y))

    coord = Coord(recher_n="1 2/, 3 1/")
    info((coord.x, coord.y))
    coord = Coord(recher_n="-1 2/, -3 1/")
    info((coord.x, coord.y))

    coord = Coord(odyssey_n="1°2'")
    info((coord.x, coord.y))
    coord = Coord(odyssey_n="3°4")
    info((coord.x, coord.y))
    coord = Coord(odyssey_n="-5°-6'")
    info((coord.x, coord.y))
    coord = Coord(odyssey_n="blablabla  654654 -77   °   -88  654564'  blabla")
    info((coord.x, coord.y))
    coord = Coord(odyssey_n="blablabla  654654 999   °   111  654564'  blabla")
    info((coord.x, coord.y))
    # Celle-ci est vraiment bizarre, mais si ça fonctionne, pourquoi pas.
    coord = Coord(odyssey_n="bla  654654 ---999   °   111  654564'  bla")
    info((coord.x, coord.y))

