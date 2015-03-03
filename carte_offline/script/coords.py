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

            # le caractère final.
            \s*'?      # éventuellement des espaces,
                       # et éventuellement une apostrophe.

        )              # les caractères définissant
                       # la coordonnée odyssienne s'arrêtent ici

        .*             # tout et n'importe quoi. On s'en fout.
        """,
        re.VERBOSE)

    @staticmethod
    def may_contain_odyssey_coord(data):
        return "°" in data

    @staticmethod
    def partition_odyssey_coord(data):
        search_result = Coord.REGEXP_ODYSSEY_COORDINATES.search(data)
        if search_result is None:
            return (data, "", "")
        else:
            coord_index_start, coord_index_end = search_result.span(1)
            return (
                data[coord_index_start:],
                data[coord_index_start:coord_index_end],
                data[coord_index_end:])

    @staticmethod
    def recher_n_one_coord_converted(one_coord):
        int_part, space, fract_part = one_coord.strip().partition(" ")
        if space == "":
            # il n'y a qu'une seule partie (ou zero) dans la coordonnée
            # On cherche le slash, pour déterminer si on a que la partie
            # entière, ou que la partie tiers.
            if "/" in one_coord:
                int_part = "0"
                fract_part = one_coord
            # dans le cas contraire, on n'a que la partie entière.
            # la fonction partiton l'a déjà placée dans int_part.

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

    def __init__(self, odyssey_n="", recher_n="", x=None, y=None):
        self.x = Fraction()
        self.y = Fraction()
        self.set(odyssey_n, recher_n, x, y)

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
            self.x = Coord.recher_n_one_coord_converted(x)
            self.y = Coord.recher_n_one_coord_converted(y)

        elif odyssey_n != "":
            x, degree, y = odyssey_n.partition("°")
            if degree == "":
                raise Exception(
                    "Notation odyssienne incorrecte. format : 000 ° 000 '")
            x = x.strip()
            self.x = Fraction(int(x), 1)
            y = y.strip()
            if y.endswith("'"):
                y = y[:-1]
            y = y.rstrip()
            self.y = Fraction(int(y), 1)

    def _extracted_parts(self, coord):
        if coord.denominator == 1:
            return coord.numerator, 0, 0.0
        elif coord.denominator == 3:
            return int(coord), coord.numerator % 3, 0.0
        else:
            return 0, 0, float(coord)

    def _as_notation_recher(self, coord):
        int_part, third, float_part = self._extracted_parts(coord)
        if float_part != 0.0:
            return str(float_part)
        elif third != 0:
            if coord < 0:
                int_part = int_part-1
            return "".join((str(int_part), " ", str(third), "/"))

        else:
            return str(int_part)

    def _as_notation_odyssey(self, coord):
        int_part, third, float_part = self._extracted_parts(coord)
        if float_part != 0.0:
            return str(float_part)
        else:
            sign = ""
            if coord < 0:
                third = 3 - third
                sign = "-"
            STRINGED_THIRD = { 0:"", 1:".333", 2:".666", 3:""}
            return "".join((sign, str(abs(int_part)), STRINGED_THIRD[third]))

    def __str__(self):
        return ", ".join((
            self._as_notation_recher(self.x),
            self._as_notation_recher(self.y)
        ))

    def as_notation_odyssey(self):
        return "".join((
            self._as_notation_odyssey(self.x),
            "°",
            self._as_notation_odyssey(self.y),
            "'"
        ))


if __name__ == "__main__":

    info = logging.info
    logging.basicConfig(format="%(message)s", level=logging.INFO)

    # TODO : ajouter des asserts si on est motivé. Ou bien utiliser pytest.

    info(Coord.recher_n_one_coord_converted("2 1/"))
    info(Coord.recher_n_one_coord_converted("   -1    "))
    info(Coord.recher_n_one_coord_converted("-5    2/    "))

    info(Coord.may_contain_odyssey_coord("aaaabbb"))
    info(Coord.may_contain_odyssey_coord("aaaa°bbb"))

    info(Coord.partition_odyssey_coord("aaaaabbbbbbbb"))
    info(Coord.partition_odyssey_coord("3°4"))
    info(Coord.partition_odyssey_coord("3°4'"))
    info(Coord.partition_odyssey_coord("blablabla  654654 -77   °   -88  654564'  blabla"))
    info(Coord.partition_odyssey_coord("blablabla  654654 -77   °   -88' 654564'  blabla"))
    info(Coord.partition_odyssey_coord("blablabla  654654 999   °   111   654564'  blabla"))
    info(Coord.partition_odyssey_coord("blablabla  654654 999   °   111 ' 654564'  blabla"))
    # Celle-ci est vraiment bizarre, mais si ça fonctionne, pourquoi pas.
    info(Coord.partition_odyssey_coord("bla  654654 ---999   °   111  654564'  bla"))

    def log_coord(coord):
        info("------")
        info((coord.x, coord.y))
        info(coord)
        info(coord.as_notation_odyssey())

    coord = Coord()
    log_coord(coord)

    coord = Coord(recher_n="0 1/, 0 2/")
    log_coord(coord)
    coord = Coord(recher_n="1/, 2/")
    log_coord(coord)
    coord = Coord(recher_n="1 1/, 1 2/")
    log_coord(coord)
    coord = Coord(recher_n="-1 1/, -1 2/")
    log_coord(coord)
    coord = Coord(recher_n="3 2/, 4 1/")
    log_coord(coord)
    coord = Coord(recher_n="-10 2/, -11 1/")
    log_coord(coord)

    coord = Coord(odyssey_n="1°2'")
    log_coord(coord)
    coord = Coord(odyssey_n="3°4")
    log_coord(coord)
    coord = Coord(odyssey_n="-5°-6'")
    log_coord(coord)
    coord = Coord(odyssey_n="  -78  °  -89  '   ")
    log_coord(coord)

