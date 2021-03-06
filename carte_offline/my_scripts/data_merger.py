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
import collections

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
from . import point_of_interest
reload(point_of_interest)
PointOfInterest = point_of_interest.PointOfInterest

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
        # TODO : liste de POI (vide au départ)

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
        """
        Objet inutilisable immédiatement après son instanciation.
        Car islands et éventuellement coord_rect peuvent être None.
        C'est au code extérieur de se débrouiller pour les définir
        """
        self.name = sea_twinpedia.name
        self.xp_min = sea_twinpedia.xp_min
        self.xp_max = sea_twinpedia.xp_max
        self.maps_required = sea_twinpedia.maps_required
        self.warning = sea_twinpedia.warning
        self.warning += warning
        self.islands = None
        self.maps_total = None

        if sea_img is None:
            self.coord_rect = None
            self.geom_ok = False
            self.warning +=  (";coordonnées incertaines. " +
                "introuvable dans la copie d'écran de la carte.")
        else:
            self.coord_rect = sea_img.coord_rect
            self.geom_ok = True

    def determine_maps_total(self):
        nb_maps_all_islands = [ island.nb_maps for island in self.islands ]
        if None in nb_maps_all_islands or -1 in nb_maps_all_islands:
            # Il y a une incertitude pour au moins une île.
            # On la propage sur l'ensemble de la mer.
            self.maps_total = -1
        else:
            self.maps_total = sum(nb_maps_all_islands)

    def __unicode__(self):
        sea_desc = join_unicode(self.name)
        islands_desc = [ "    " + unicode(island) for island in self.islands ]
        all_desc = [ sea_desc ] + islands_desc
        return "\n".join(all_desc)

class DataMerger(object):
    # TODO : revérifier la limite des 80 caractères, maintenant que j'ai
    # tout foutu dans une classe.

    def __init__(self, seas_twinpedia, seas_img):
        self.seas_twinpedia = seas_twinpedia
        self.seas_img = seas_img
        self._merge_seas_twinpedia_img()
        for sea in self.seas:
            sea.determine_maps_total()
        # Dictionnaire.
        # clé :
        #   une coordonnée en valeur entière, récupérée depuis twinpedia,
        #   help-odyssey, ou autre.
        # valeur :
        #   une liste de PointOfInterest. On sait qu'ils sont dans cette
        #   coordonnée, mais on ne sait pas exactement où, ni dans quelle île.
        #   les POI qu'on sait où placer ne sont pas dans ce dictionnaire,
        #   mais dans l'île elle-même.
        self.pois_unplaced = collections.defaultdict(list)

    def _twinpedia_candidates_of_island_img(self, seas_twinpedia, island_img):
        twinpedia_candidates = []

        # Si l'island_img possède un "supposed_name", on s'en sert
        # pour effectuer directement l'association.
        if island_img.supposed_name != "":
            for sea in seas_twinpedia:
                for island_twinpedia in sea.islands:
                    if island_img.supposed_name in island_twinpedia.name:
                        # TODO : pas de "in" car il y a plein de noms semblables
                        # (par exemple : Aralmi)
                        #
                        # On renvoie direct un seul résultat,
                        # sans chercher plus loin.
                        twinpedia_candidates.append((sea, island_twinpedia))
                        return twinpedia_candidates

        for sea in seas_twinpedia:
            for island_twinpedia in sea.islands:
                # TODO : on recrée un CoordRect pour chaque islands twinpedia
                # à chaque fois qu'on appelle cette fonction. C'est pas top.
                rect_candidate = CoordRect(
                    coord_up_left=island_twinpedia.coord, w=1, h=1)
                if rect_candidate.intersects(island_img.coord_rect, False):
                    twinpedia_candidates.append((sea, island_twinpedia))
        return twinpedia_candidates

    def _check_coherency_one_sea(self, sea_twinpedia, sea_img):
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
                    # TODO : pas de "in" car il y a plein de noms semblables
                    # (par exemple : Aralmi)
                    # Ou peut-être que si, parce que comme on ne travaille que
                    # sur une seule mer, il y a moins de risques.
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
                        coord_up_left=island_twinpedia_found.coord, w=1, h=1)
                    if not rect_twinpedia.intersects(island_img.coord_rect):
                        # Les position img et twinpedia ne sont pas cohérentes.
                        # On garde quand même l'association, mais on le signale.
                        # Et on rend la géométrie incertaine.
                        island_ok.geom_ok = False
                        island_ok.warning += (";association par nom réussie, " +
                            "mais les îles ne sont pas au même endroit.")

            else:

                intersecting_islands_twinpedia = []
                logging.debug("deb ******")
                logging.debug("deb " + unicode(island_img.coord_rect))
                logging.debug("deb ******")

                for island_twinpedia in islands_twinpedia:
                    # On met des longueurs/largeurs de 1. Mais on considère
                    # que ça s'intersecte pas quand y'a que les bords qui
                    # se touchent.
                    rect_candidate = CoordRect(
                        coord_up_left=island_twinpedia.coord, w=1, h=1)
                    logging.debug("deb " + island_twinpedia.name + " " + unicode(rect_candidate))
                    logging.debug("deb " + unicode(island_img.coord_rect))
                    if rect_candidate.intersects(island_img.coord_rect, False):
                        intersecting_islands_twinpedia.append(island_twinpedia)
                        logging.debug("deb ok")
                    logging.debug("deb -----")

                if not intersecting_islands_twinpedia:
                    # Il manque une île dans twinpedia. On considère que tout
                    # est foiré. On se casse.
                    sea_twinpedia.warning += (";test échoué avec mer " +
                        str(sea_img.coord_rect))
                    info(sea_twinpedia.warning)
                    info(island_img.coord_rect)
                    return None
                elif len(intersecting_islands_twinpedia) == 1:
                    # Correspondance top. 1 pour 1. On crée une île finale.
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

    def _find_first_sea_association(self, seas_twinpedia, seas_img):
        for current_sea_img in seas_img:
            for current_island_img in current_sea_img.islands:
                candidates = self._twinpedia_candidates_of_island_img(
                    seas_twinpedia,
                    current_island_img)

                # TODO : logger un warning si plusieurs candidats
                # de mers différentes. Au lieu de ce tas de merde.
                if candidates:
                    logging.debug("find_first deb " + candidates[0][0].name)
                    logging.debug("find_first deb " + candidates[0][1].name)
                    logging.debug("find_first deb " + unicode(candidates[0][1].coord))
                    logging.debug("find_first deb " + str(len(candidates)))
                    if len(candidates) > 1:
                        logging.debug("find_first deb " + candidates[1][0].name)
                        logging.debug("find_first deb " + candidates[1][1].name)
                        logging.debug("find_first deb " + unicode(candidates[1][1].coord))
                        logging.debug("find_first deb " + str(len(candidates)))
                    logging.debug("find_first" + "-"*10)
                else:
                    logging.debug("find_first deb fail " + unicode(current_island_img.coord_rect))
                    logging.debug("find_first" + "-"*10)

                if len(candidates) == 1:
                    sea_candidate_twinpedia = candidates[0][0]
                    coherency_result = self._check_coherency_one_sea(
                        sea_candidate_twinpedia, current_sea_img)
                    if coherency_result is not None:
                        # Hop c'est cool. On renvoit cette association.
                        # On ne continue pas d'itérer, on s'en fout.
                        return (
                            coherency_result,
                            sea_candidate_twinpedia,
                            current_sea_img)
        return None

    def _sea_from_twinpedia_only(self, sea_twinpedia):
        islands = [
            Island(island_twinpedia)
            for island_twinpedia
            in sea_twinpedia.islands ]
        #info("aaaa")
        #info(sea_twinpedia)
        #info(sea_twinpedia.islands)
        #info(islands)
        #machin = [ island.coord_rect for island in islands ]
        #info(machin)
        rect_sea = CoordRect.bounding_rect(
            [ island.coord_rect for island in islands ] )
        if rect_sea is None:
            return None
        rect_sea.inflate(Fraction(1, 3))
        sea_ok = Sea(sea_twinpedia)
        sea_ok.islands = islands
        sea_ok.coord_rect = rect_sea
        return sea_ok

    def _merge_seas_twinpedia_img(self):
        seas_img_copy = list(self.seas_img)
        seas_twinpedia_copy = list(self.seas_twinpedia)
        seas_ok = []
        added_sea = True
        while added_sea:
            sea_association = self._find_first_sea_association(
                seas_twinpedia_copy, seas_img_copy)
            if sea_association is not None:
                sea_ok, sea_twinpedia_assoc, sea_img_assoc = sea_association
                seas_ok.append(sea_ok)
                seas_twinpedia_copy.remove(sea_twinpedia_assoc)
                seas_img_copy.remove(sea_img_assoc)
                added_sea = True
            else:
                added_sea = False

        # On prend toutes les mers de twinpedia qui restent,
        # on crée des mers finales, en leur mettant des coords incertaines.
        for sea_twinpedia in seas_twinpedia_copy:
            sea = self._sea_from_twinpedia_only(sea_twinpedia)
            if sea is not None:
                seas_ok.append(sea)

        self.seas = seas_ok

    def _spread_poi_coords(self):
        # TODO : répartir les points dans les rectangles englobant.
        for raw_coord, pois in self.pois_unplaced.items():
            raw_coord_middle = Coord(
                x=raw_coord.x + Fraction(1, 2),
                y=raw_coord.y + Fraction(1, 2))
            for poi in pois:
                poi.pos = raw_coord_middle


def build_data():
    seas_twinpedia = reader_twinpedia.parse_islands_and_seas()
    seas_img = reader_data_from_img.parse_data_from_img()
    data_merger = DataMerger(seas_twinpedia, seas_img)

    # TODO : factoriser ça.
    temple_coords = reader_twinpedia.parse_temples()
    for coord in temple_coords:
        poi = PointOfInterest("lieu__temple")
        data_merger.pois_unplaced[coord].append(poi)

    library_coords = reader_twinpedia.parse_libraries()
    for coord in library_coords:
        poi = PointOfInterest("lieu__librairie")
        data_merger.pois_unplaced[coord].append(poi)

    fountain_coords = reader_twinpedia.parse_fountains()
    for coord in fountain_coords:
        poi = PointOfInterest("lieu__fontaine")
        data_merger.pois_unplaced[coord].append(poi)

    pot_distillers_coords = reader_twinpedia.parse_potion_distillers()
    for coord in pot_distillers_coords:
        poi = PointOfInterest("lieu__distillateur")
        data_merger.pois_unplaced[coord].append(poi)

    food_bags_coords = reader_twinpedia.parse_food_bags()
    for coord in food_bags_coords:
        poi = PointOfInterest("lieu__sac_nourriture")
        data_merger.pois_unplaced[coord].append(poi)

    ruin_data = reader_twinpedia.parse_ruins()
    for coord, description, monsters in ruin_data:
        poi = PointOfInterest(
            "lieu__ruines",
            {"descrip":description, "monstres":monsters})
        data_merger.pois_unplaced[coord].append(poi)

    inn_data = reader_twinpedia.parse_inns()
    for coord, cost in inn_data:
        poi = PointOfInterest(
            "lieu__auberge",
            {"prix":cost})
        data_merger.pois_unplaced[coord].append(poi)

    data_merger._spread_poi_coords()
    return data_merger.seas, data_merger.pois_unplaced


def test_0():
    seas, pois_unplaced = build_data()
    for sea in seas:
        info(unicode(sea))
        info("-" * 10)

def test_1():
    # test des clamps.
    # TODO : à foutre ailleurs quand la fonction du clamp sera foutue ailleurs.
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

def test_2():
    seas_twinpedia = reader_twinpedia.parse_islands_and_seas()
    seas_img = reader_data_from_img.parse_data_from_img()
    data_merger = DataMerger(seas_twinpedia, seas_img)
    data_merger.pois_unplaced[Coord(x=1, y=1)].append(
        PointOfInterest("ruines", {}))
    data_merger.pois_unplaced[Coord(x=1, y=2)].append(
        PointOfInterest("temple", {}))
    data_merger.pois_unplaced[Coord(x=1, y=1)].append(
        PointOfInterest("ruines", {}))
    data_merger._spread_poi_coords()
    for k, v in data_merger.pois_unplaced.items():
        info(unicode(k))
        info(" ; ".join( (unicode(elem) for elem in v) ))
        info("--------")

def test(numtest):
    func_test_from_num = { 0:test_0, 1:test_1, 2:test_2 }
    func_test_from_num[numtest]()

if __name__ == "__main__":
    test(0)
    test(1)
    test(2)
