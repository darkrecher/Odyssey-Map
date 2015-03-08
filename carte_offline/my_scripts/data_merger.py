# -*- coding: utf-8 -*-

"""
    Récupère les données brutes provenant de différentes sources,
    et les rassemble, en détectant les incohérences (plus ou moins).
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info
from fractions import Fraction

from . import bat_belt
reload(bat_belt)
join_unicode = bat_belt.join_unicode
from . import coords
reload(coords)
Coord = coords.Coord
from . import coord_rect
reload(coord_rect)
CoordRect = coord_rect.CoordRect
from . import reader_twinpedia
reload(reader_twinpedia)
from . import reader_data_from_img
reload(reader_data_from_img)

# TODO : peut-être que l'Island et la Sea iront dans un fichier à part.

class Island(object):

    def __init__(self,
        island_twinpedia, island_img=None, geom_ok=False, warning=""):

        self.name = island_twinpedia.name
        self.nb_maps = island_twinpedia.nb_maps
        self.description = island_twinpedia.description
        self.warning = island_twinpedia.warning
        self.warning += warning
        self.geom_ok = geom_ok

        if island_img is None:
            self.coord_rect = CoordRect(
                coord_up_left=island_twinpedia.coord,
                w=1, h=1)
            self.geom_ok = False
            self.warning += (";coordonnées incertaines. " +
                "introuvable dans la copie d'écran de la carte.")
        else:
            self.coord_rect = island_img.coord_rect
            if island_img.warning != "":
                self.geom_ok = False
                self.warning += (";coordonnées incertaines. " +
                "copie d'écran de la carte imprécise.")

    def __unicode__(self):
        return join_unicode(
            self.name, " ",
            "(", self.coord_rect, ") ",
            "W:", self.warning)

    # TODO : ça va dans la classe geom_tools, un truc comme ça. ou CoordRect.
    def clamp_in_rect(self, rect_owner):
        # Si l'île est trop à gauche ou trop haut par rapport au rectangle
        # censé l'englober, on la déplace.
        coord_ul = self.coord_rect.coord_up_left
        dist_ul_isle_owner_x = rect_owner.coord_up_left.x - coord_ul.x
        dist_ul_isle_owner_y = rect_owner.coord_up_left.y - coord_ul.y
        dist_ul_isle_owner_x = max(dist_ul_isle_owner_x, 0)
        dist_ul_isle_owner_y = max(dist_ul_isle_owner_y, 0)
        if dist_ul_isle_owner_x > 0 or dist_ul_isle_owner_y > 0:
            vector_move = Coord(x=dist_ul_isle_owner_x, y=dist_ul_isle_owner_y)
            self.coord_rect.move(vector_move)
            self.geom_ok = False
            self.warning += ";déplacement pour rester dans le rect englobant"
        # Si l'île est trop à droite ou trop en bas, on diminue sa taille.
        # (Tout en conservant une taille minimale de 1/)
        coord_dr = self.coord_rect.coord_down_right
        dist_dr_isle_owner_x = rect_owner.coord_down_right.x - coord_dr.x
        dist_dr_isle_owner_y = rect_owner.coord_down_right.y - coord_dr.y
        dist_dr_isle_owner_x = min(dist_dr_isle_owner_x, 0)
        dist_dr_isle_owner_y = min(dist_dr_isle_owner_y, 0)
        if dist_dr_isle_owner_x < 0 or dist_dr_isle_owner_y < 0:
            self.coord_rect.add_to_size(
                dist_dr_isle_owner_x,
                dist_dr_isle_owner_y)
            self.coord_rect.set_min_size(Fraction(1, 3), Fraction(1, 3))
            self.geom_ok = False
            self.warning += ";retaillage pour rester dans le rect englobant"
        # TODO : la diminution de taille n'a pas forcément fait rentrer l'île
        # dans le rectangle englobant. Si elle n'est toujours pas dedans,
        # il faut la déplacer. C'est jamais censé arriver par rapport à ce
        # que je fais dans le reste du code, donc osef.

class Sea(object):

    def __init__(self, sea_twinpedia, sea_img=None, warning=""):
        self.name = sea_twinpedia.name
        self.xp_min = sea_twinpedia.xp_min
        self.xp_max = sea_twinpedia.xp_max
        self.total_maps_required = sea_twinpedia.total_maps_required
        self.warning = sea_twinpedia.warning
        self.warning += warning
        self.islands = []

        if sea_img is None:
            # TODO : déduire une géométrie incertaine
            # à partir des islands contenues dans sea_twinpedia
            self.coord_rect = None
            self.geom_ok = False
            self.warning +=  (";coordonnées incertaines. " +
                "introuvable dans la copie d'écran de la carte.")
        else:
            self.coord_rect = sea_img.coord_rect
            self.geom_ok = True

    def __unicode__(self):
        sea_desc = join_unicode(self.name)
        islands_desc = [ "    " + unicode(island) for island in self.islands ]
        all_desc = [ sea_desc ] + islands_desc
        return "\n".join(all_desc)


def _twinpedia_candidates_of_island_img(seas_twinpedia, island_img):
    twinpedia_candidates = []
    for sea in seas_twinpedia:
        for island in sea.islands:
            # TODO : on recrée un CoordRect pour chaque islands twinpedia
            # à chaque fois qu'on appelle cette fonction. C'est pas top.
            rect_candidate = CoordRect(
                coord_up_left=island.coord,
                w=Fraction(2, 3), h=Fraction(2, 3))
            if rect_candidate.intersects(island_img.coord_rect):
                twinpedia_candidates.append((sea, island))
    return twinpedia_candidates

def _check_coherency_one_sea(sea_twinpedia, sea_img):
    islands_twinpedia = list(sea_twinpedia.islands)
    islands_img = list(sea_img.islands)
    islands_ok = []
    islands_img_left = []

    for island_img in islands_img:

        if island_img.supposed_name != "":

            # Le nom de l'île est directement indiqué dans img_778N9.py.
            # Ça permet de régler les cas où il y a plusieurs îles sur la
            # même coordonée. Dans ce cas, on cherche directement la bonne
            # île dans twinpedia, et on vérifie que c'est cohérent.
            island_twinpedia_found = None
            for island_twinpedia in islands_twinpedia:
                if island_img.supposed_name in island_twinpedia.name:
                    island_twinpedia_found = island_twinpedia

            if island_twinpedia_found is None:
                # On ne trouve pas l'île dans twinpedia. On oublie
                # cette island_img. On n'essaie même pas de l'associer à une
                # autre île par intersection. C'est violent, mais c'est jamais
                # censé arriver, car c'est moi qui saisi manuellement les noms
                # des îles dans img_778N9.
                info("île twinpedia introuvable : " + island_img.supposed_name)
                islands_img_left.append(island_img)
            else:
                island_ok = Island(island_twinpedia_found, island_img, True)
                islands_twinpedia.remove(island_twinpedia_found)
                islands_ok.append(island_ok)

                rect_twinpedia = CoordRect(
                    coord_up_left=island_twinpedia_found.coord,
                    w=Fraction(2, 3), h=Fraction(2, 3))
                if not rect_twinpedia.intersects(island_img.coord_rect):
                    # Les position img et twinpedia ne sont pas cohérentes.
                    # On garde quand même l'association, mais on le signale.
                    # Et on rend la géométrie incertaine.
                    island_ok.geom_ok = False
                    island_ok.warning += (";association par nom réussie, " +
                        "mais les îles ne sont pas au même endroit.")

        else:

            intersecting_islands_twinpedia = []

            for island_twinpedia in islands_twinpedia:
                # Faut pas indiquer des longueurs/largeurs de 1. Car ça va
                # s'intersecter avec d'éventuels îles de la coordonnée d'à côté
                # (vers la droite ou vers le bas). Ça s'intersectera sur la
                # ligne commune. Donc on met des 2/3.
                rect_candidate = CoordRect(
                    coord_up_left=island_twinpedia.coord,
                    w=Fraction(2, 3), h=Fraction(2, 3))
                if rect_candidate.intersects(island_img.coord_rect):
                    intersecting_islands_twinpedia.append(island_twinpedia)

            if not intersecting_islands_twinpedia:
                # Il manque une île dans twinpedia. On considère que tout est
                # foiré. On se casse.
                sea_twinpedia.warning += (";test échoué avec mer " +
                    str(sea_img.coord_rect))
                return None
            elif len(intersecting_islands_twinpedia) == 1:
                # Correspondance super top. 1 pour 1. On crée une île finale.
                island_twinpedia_found = intersecting_islands_twinpedia[0]
                islands_ok.append(Island(
                    island_twinpedia_found,
                    island_img,
                    True))
                islands_twinpedia.remove(island_twinpedia_found)
            else:
                # Plusieurs îles dans twinpedia pour la même île d'image.
                # Tant pis, on met un warning, et on créera des îles aux
                # coordonnées incertaines.
                for island_twinpedia in intersecting_islands_twinpedia:
                    island_twinpedia.warning += (";hésitation avec " +
                        str(island_img.coord_rect))
                islands_img_left.append(island_img)

    # On a fait toutes les associations qu'on pouvait. On rajoute
    # les îles twinpedia restantes. Elles auront une géométrie incertaine.
    for island_twinpedia in islands_twinpedia:
        islands_ok.append(Island(island_twinpedia))

    sea_ok = Sea(sea_twinpedia, sea_img)
    for island in islands_ok:
        island.clamp_in_rect(sea_ok.coord_rect)
    sea_ok.islands = islands_ok
    return sea_ok

def _find_first_sea_association(seas_twinpedia, seas_img):
    for current_sea_img in seas_img:
        for current_island_img in current_sea_img.islands:
            candidates = _twinpedia_candidates_of_island_img(
                seas_twinpedia,
                current_island_img)
            if len(candidates) == 1:
                sea_candidate_twinpedia = candidates[0][0]
                coherency_result = _check_coherency_one_sea(
                    sea_candidate_twinpedia, current_sea_img)
                if coherency_result is not None:
                    # Hop c'est cool. On renvoit cette association.
                    # On ne continue pas d'itérer, on s'en fout.
                    return (
                        coherency_result,
                        sea_candidate_twinpedia,
                        current_sea_img)
    return None

def _merge_twinpedia_img(seas_twinpedia, seas_img):
    seas_img_copy = list(seas_img)
    seas_twinpedia_copy = list(seas_twinpedia)
    seas_ok = []
    added_sea = True
    while added_sea:
        sea_association = _find_first_sea_association(
            seas_twinpedia_copy, seas_img_copy)
        if sea_association is not None:
            sea_ok, sea_twinpedia_assoc, sea_img_assoc = sea_association
            seas_ok.append(sea_ok)
            seas_twinpedia_copy.remove(sea_twinpedia_assoc)
            seas_img_copy.remove(sea_img_assoc)
            added_sea = True
        else:
            added_sea = False

    # TODO : prendre toutes les mers de twinpedia qui restent,
    # créer des mers finales avec. (Elles auront des coordonnées incertaines).
    return seas_ok

def build_data():
    seas_twinpedia = reader_twinpedia.parse_islands_and_seas()
    seas_img = reader_data_from_img.parse_data_from_img()
    seas = _merge_twinpedia_img(seas_twinpedia, seas_img)
    return seas


def test():
    seas = build_data()
    for sea in seas:
        info(unicode(sea))
        info("-" * 10)

    # test des clamps.
    island_twinpedia = reader_twinpedia.IslandTwinpedia(
        "a", Coord(recher_n="5, 3 2/"))
    island = Island(island_twinpedia)
    info(unicode(island))
    island.clamp_in_rect(CoordRect(recher_n_rect="5 2/, 4, 10, 10"))
    info(unicode(island))
    island.clamp_in_rect(CoordRect(recher_n_rect="6, 4, 10, 10"))
    info(unicode(island))
    info("-" * 3)
    island_twinpedia = reader_twinpedia.IslandTwinpedia(
        "a", Coord(recher_n="5, 3 2/"))
    island = Island(island_twinpedia)
    info(unicode(island))
    island.clamp_in_rect(CoordRect(recher_n_rect="3, 3, 2 2/, 10"))
    info(unicode(island))
    island.clamp_in_rect(CoordRect(recher_n_rect="3, 3, 10, 1/"))
    info(unicode(island))


if __name__ == "__main__":
    test()
