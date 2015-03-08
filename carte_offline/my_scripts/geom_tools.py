# -*- coding: utf-8 -*-

"""
    Module générique, avec des fonctions géométriques "pures".
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info
from fractions import Fraction

from . import bat_belt
reload(bat_belt)
enum = bat_belt.enum

""" orientations """
ORI = enum(
    "ORI",
    "RIGHT", "DOWN", "LEFT", "UP")

def garbled_line(coord_start, length, orientation):
    nb_points = int(length * 6)
    coords_x = [ coord_start.x ] * nb_points
    coords_y = [ coord_start.y ] * nb_points
    variation = [ Fraction(1, 6), Fraction(-1, 6) ] * int(nb_points / 2)
    steps = range(nb_points)
    steps = [ Fraction(1, 12) + Fraction(step, 6) for step in steps ]

    if orientation in (ORI.LEFT, ORI.UP):
        steps = [ -step for step in steps ]
    if orientation in (ORI.LEFT, ORI.RIGHT):
        coords_x_and_vect = zip(coords_x, steps)
        coords_y_and_vect = zip(coords_y, variation)
    else:
        coords_x_and_vect = zip(coords_x, variation)
        coords_y_and_vect = zip(coords_y, steps)

    coords_x_final = [ pos + vect for (pos, vect) in coords_x_and_vect ]
    coords_y_final = [ pos + vect for (pos, vect) in coords_y_and_vect ]
    coords_xy = zip(coords_x_final, coords_y_final)
    coords_xy = [ (coord_start.x, coord_start.y) ] + coords_xy
    coords_xy = [ (float(xy[0]), float(xy[1])) for xy in coords_xy ]
    return coords_xy

def points_from_coord_rect(coord_rect, garble_lines):
    if garble_lines:
        dist_x = coord_rect.coord_down_right.x - coord_rect.coord_up_left.x
        dist_y = coord_rect.coord_down_right.y - coord_rect.coord_up_left.y
        line_right = garbled_line(coord_rect.coord_up_left, dist_x, ORI.RIGHT)
        line_down = garbled_line(coord_rect.coord_up_right, dist_y, ORI.DOWN)
        line_left = garbled_line(coord_rect.coord_down_right, dist_x, ORI.LEFT)
        # Modif un peu à l'arrache de mon rectangle garblé. Si je fais pas ça,
        # j'ai des lignes qui se croisent.
        # Ça ne fait plus un garblage "régulier", mais osef complètement.
        del line_left[-1]
        line_up = garbled_line(coord_rect.coord_down_left, dist_y, ORI.UP)
        return line_right + line_down + line_left + line_up
    else:
        return [
            (coord_rect.coord_up_left.x, coord_rect.coord_up_left.y),
            (coord_rect.coord_up_right.x, coord_rect.coord_up_right.y),
            (coord_rect.coord_down_right.x, coord_rect.coord_down_right.y),
            (coord_rect.coord_down_left.x, coord_rect.coord_down_left.y),
        ]


def test():
    from . import coords
    reload(coords)
    Coord = coords.Coord
    garbled = garbled_line(Coord(x=5, y=3), Fraction(4, 3), ORI.RIGHT)
    info(unicode(garbled))

if __name__ == "__main__":
    test()
