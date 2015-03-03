# -*- coding: utf-8 -*-

"""
    Données brutes, pompée depuis Twinpedia.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)

LEECH_URL = "http://www.twinpedia.com/muxxu/odyssey"
LEECH_DATE = "2015-26-02"


# --- boss ---

BOSSES = """
Envoyé d'Hypérion   -13°-3'     24  3   5   -   Drain?? FureurAttaqueAttente    50  ?
Tristan Roi des Tritons 15°2'   30  2   6   Acide   ProvoqueDrainAttaque bulleAttaqueAttaque bulleAttaqueAttaque bulle  50  ?
Stalskin Pope de Kabal  -3°24'  42  3 BM    12  -   RégénérationRégénérationAttaqueAttenteAttente   50  ?
Galupin doré    14°-4'  24  3 Évasion   5   Volant  Double-attaqueDouble-attaqueAttente     50  ?
Cyclope de Tartan   6°27'   80  -   12  -   Oeil de CyclopeAttaqueAttente   60
Chronatorgh 2°31'   100     -   5   -   AttaqueAttaqueAttaqueAttaqueSouffle enflammé    100     ?
Astérope    20°16'  70  6 BM    5   Contre-attaque  RégénérationAttaque mentaleRégénérationAttaqueFoudreRégénérationAttaque     200     ?
Golem prismatique   22°-9'  150     3 BM    14  -   Double-attaqueAttenteAttenteAttenteAttaqueAttenteAttenteAttente     200     ?
Semerkhet   -23°5'  50  12  8   -       200     ?
"""

# --- mers et îles ---

ISLANDS_AND_SEAS = """
Mer du Destin (~ 10 XP, 3 cartes)
Ile de l'oracle     0° 0'   1   Point de départ de l'aventure
Ile Rékiphie    1° 0'   1   PNJ: Papapapalopoulos (ramener “Viande grillée”, “Fruit appétissant”, “Gros légume”)
Ile du Tahépe   1° 1'   1
Ile Ganes   1° 1'   1
Ile Spelugos    1° 2'   1   PNJ: Euterpe la Musicienne
Récif des Enas  0° 2'   1   Ruines
Mer Kyfi (~ 10 - 18 XP, 3 cartes)
Récif Harpoukon     2° 0'   1   Temple
Ilot Harhéxos   3° 1'   0   Épi de blé (1/5)
Dokios  4° 0'   2   PNJ: Monsieur Coranthin
Ilot aux Epoufi     3° 1'   1   Ruines
Ilot Iron   5° 0'   1   Or: 10+20, Auberge (65 Or)
Récif aux Bakrones  6° 2'   1
Mer Phyhépe (~ ? XP, 3 cartes)
Récif d'Ilogramamaque   1° -2'  0   Ruines, PNJ: Ebos Gratte-Terre (ramener des “Trucs à faire pousser”)
Ile de l'Elogos     0° -1'  2   Ruines, Feuilles de Lotos
Récif Lesakton  0° -4'  1   PNJ: Mademoiselle Flora (ramener une “Rose d'Airain”)
Ile du Gaphie   1° -5'  1
Ilot Galafi     0° -5'  1
Minithion   1° -5'  1   Épi de Blé (1/5)
Mer Arespax (~ 21 - 30 XP, 2 cartes)
Iripsios    -7° 12'     1   Or, Ruines, Augmentation du sac de nourriture, Baguette des Drünes (1/6)
Epe     -7° 12'     1   Or, Ruines
Ile Kareskaos   -7° 13'     1   Ruines
Ile du Thaos    -8° 14'     1   Or, Remplissage de potions, Statue de Déméter
Mer Arème (~ 12 - 18 XP, 3 cartes)
Ile Ilophie     -1° 3'  0   Remplissage de potions, Épi de blé (1/5)
Ile de Pelon    -1° 3'  0   Remplissage de potions
Ile des oiseaux     2° 3'   2   PNJ: Le maitre des oiseaux
Ilot de Dokihon     2° 4'   1
Ilot du Bakronie    1° 4'   1   Bibliothèque, Temple
Ilot de Leson   -1° 4'  2   Fontaine, PNJ: Fou
Mer Karalmien (~ 30 XP, 3 cartes)
Ilot Ekon   -3° 5'  1   Or:4+4+5, Ruines, Auberge (65 Or), Héros: Torkish Perceflanc
Autologos   -2° 6'  1
Ile de la Peste     -3° 7'  2   Or: 4+30, Remplissage de potions, PNJ: Docteur Hippocrate
Ilot de l'Iras  -2° 9'  0
Gati    -2° 9'  1   Or: 4+5+6+20, Remplissage de potions, Balle de coton (1/5)
Mer Ilokixos (~ 10 - 15 XP, 2 cartes)
Ile de Magoulos     -2° 3'  1   Ruines
Kareskone   -2° 3'  1   Ruines, Fontaine
Miniti  -2° 3'  1   Or: 4+4+?? , Ruines, Épi de blé (1/5), PNJ: Nikolaos le Jardinier
Mer Ikaxax (~ 20 - 30 XP, 2 cartes)
Autofi  -6° 3'  1   Or: 4+5+6+30, Ruines, Racines de Moly
Banes   -6° 3'  1   Or: 4+5+20+20, Auberge (55 Or), Augmentation du sac de nourriture, PNJ: Pénélope la Veuve
Dokalmon    -7° 3'  1   Ruines, Marchand (120 Or), Fontaine, PNJ: Mousse Aka
Mer Rékrones (~ 36 - 63 XP, 3 cartes)
Ile aux Telelipoulos    -9° -5'     0
Arion   -8° -6'     2   Ruines, PNJ: Plutarque l'Ecrivain
Ile Spelulème   -8° -4'     1   Ruines, Héros: Gloria Sylve de Drüne
Arien   -8° -4'     1   Ruines
Ile Oros    -7° -6'     1?  Or: 5+15, Remplissage de potions
Ile Hyti    -7° -4'     1   Or: 4+6+6+10, Ruines, Marchand (80 Or), PNJ: Barnabas l'Arnaque (Lance de Zeus 100 Or)
Mer Harmaque (~ 15 - 20 XP, 3 cartes)
Ile Aralmi  -4° -8'     2   Or: 4+4+5, Ruines, Marchand (120 Or), Canne du débutant
Elusyne     -3° -6'     0   Or: 20+4+6+6+5, Ruines, Page de poème (1/4)
Ile aux Epaves  -5° -5'     1   Ruines, PNJ: Chasseur d'épaves, PNJ: Fafox-la-Fouine
Ilot du Harxos  -4° -8'     1   Or: 10+5+15+6, Ruines, Marchand (120 Or)
Magithème   -3° -8'     1   Or: 5+4+4+15+15, Temple
Ile aux Bapoulos    -5° -7'     1   Or: 5+15+15+4+10+15, Héros: Tasulys Maîtresse des Jarres
Mer Orès (~ 25 - 35 XP, 3 cartes)
Ilôt du Spesyne     7° -2'  ?   Or, Remplissage de potions, Page de poème (1/4)
Orors   9° 0'   ?   Remplissage de potions, Statue d'Arès
Ile de l'Autoligma  11° 1'  ?   Ruines
Ile de l'Ilonie     10° 0'  ?   Ruines, PNJ: Démosthène le Bègue
Sarespi     8° -2'  1   Or, Temple, Remplissage de potions
Dokien  9° -1'  2   Or, Ruines, Carte de la mer Sauvage (1/5)
Mer Autoripe (~ 25 - 30 XP, 3 cartes)
Minespème   3° 3'   0   Or: 20, Ruines, Page de Poème (1/4)
Magepisa    3° 4'   1   Héros: Hératus Fermela, Ruines, Marchand (80 or)
Balème  4° 3'   0   Auberge (55 Or), Ruines, PNJ: Moine de Kabal
Ile de Ikeu     3° 4'   2   Remplissage de potions
Ile de l'Iramnesème     4° 4'   2   Ruines
Mer Aroulique (~ 8 - 16 XP, 3 cartes)
Ile Sarix   2° -10'     2   Statue d'Atlas, Ruines
Irique  0° -10'     1   Or: 20+15+5, Ruines, Marchand (??), PNJ: Sage de Drüne
Ile aux Autokigma   1° -9'  1   Or: 4, Ruines
Ile des Marchands   2° -9'  0   PNJ: Mélos le Marchand, PNJ: Fougas la Bricole
Ile des Tagma   0° -7'  0   Or: 4+4+6+15+20+30, Ruines, Marchand (110 Or), Bibliothèque
Spelulogos  1° -7'  2   Ruines, Blason d'Halberti (1/5)
Mer Telelufi (~ 30 XP, 2 cartes)
Ile Fermela     7° 4'   1   PNJ: Cunégorde Fermela (femme d'Hératus)
Ile de Magors   8° 4'   1   Ruines
Ile de Harsis   8° 4'   1   Or: 4+4+6+10, Ruines, PNJ: Phébus l'Illuminateur (vend Amadou 200 or)
Autosis     9° 3'   1   Ruines, Auberge (55 or)
Mer Minithée (~ 10-18 XP, 3 cartes)
Ile des Irique  -3° 1'  2
Ilot de Hylati  -3° 0'  2
Iles des Autorixos  -4° 1'  0   PNJ: Antiphon Maître des Voiles (ramener coton)
Arantée     -4° 1'  1   Ruines, Épi de Blé (1/5)
Ilot du Ikique  -5° -3'     0   Augmentation du sac de nourriture
Telephie    -2° -2'     1   Or: 30? , PNJ: Panos
Mer Ariti (~10 - 17 XP, 3 cartes)
Iloluphie   4° -5'  1   PNJ: Pouscale le Pêcheur
Ilot de Hynas   3° -4'  2   Or: 5, Ruines , Marchand (110 or)
Pelax   4° -3'  1   Or: 5*5 , Remplissage de potions
Ile de l'Aralmie    3° -3'  1   Or: 6+6, Ruines, PNJ: Apollinaire le Poète
Ilot de Telelogos   4° -2'  0   Or: 6+15, Ruines, Temple
Ikeskone    5° -2'  1   Ruines
Mer Orème (~ 20 - 38 XP, 3 cartes)
Ilot de l'Ilokroné  10° -5'     1   Or: 20+5+20, Remplissage de potions, Marchand (110 Or), PNJ: Dédale l'Égaré
Ilot du Karée   11° -6'     1   Or: 6+5+4, Ruines, Hache Brisée d'Hephaïstos (1/8), Augmentation du sac de nourriture
Ile Thaxie  9° -6'  1   Or: 15+5, Ruines, Marchand (110 Or), Héros: Céleïde
Ile des Saron   8° -6'  1   Page de poème (1/4)
Ile Balême  8° -5'  1   Or: 15+15+10, Ruines, Auberge (55 Or), Potion Vide (1/5)
Ile des Zikas   7° -5'  1
Mer Taron (~ 10 - 18 XP, 3 cartes)
Dokaxaos    -7° -3'     1
Ile du Saraxas  -9° -1'     1   Ruines, Auberge (40 Or)
Ile Kylilème    -8° -1'     1   Auberge (45 Or)
Ile de Karithien    -7° -1'     1   Ruines
Ile de Minipsas     -9° 0'  1   Or: 4+5+6+30, Ruines, Héros: Dolskin Kabbaliste aveugle
Ile du Tariphie     -8° 0'  1   Or: 5, Remplissage de potions, PNJ: Boudine l'Assoiffée
Mer Kareskiti (~ 18 - 36 XP, 3 cartes)
Ile d'Epouné    -7° 7'  0   Or: 5+6, Augmentation du sac de nourriture, Bibliothèque
Ile de l'Arantée    -6° 9'  1   Or: 4, Remplissage de potions, Hache Brisée d'Hephaïstos (1/8)
Ilot de l'Aralmix   -8° 6'  1   Or: 5+20, Marchand (110 Or), Augmentation du sac de nourriture
Pelaktème   -8° 6'  1   Or: 4+4+5+20, Ruines, Marchand (110 Or)
Ile de Thaos    -5° 6'  2   Hache Brisée d'Hephaïstos (1/8)
Orakas  -7° 6'  1   Ruines, PNJ: Dimitri le Croyant
Mer Ilosyne (~ 26 - 36 XP, 2 cartes)
Ile Saralmique  -9° 7'  1   Or, Ruines, Médaille de Kabal
Bakimaque   -10° 9'     1   Ruines, Augmentation du sac de nourriture, Balle de coton (1/5)
Ile Phyliti     -9° 7'  1   Or, Augmentation du sac de nourriture, Remplissage de potions, Balle de coton (1/5)
Mer Iko (~ 20 - 38 XP, 3 cartes)
Magix   -12° 7'     0   Or: 20+15+4, Ruines, Auberge (50 Or), Augmentation du sac de nourriture, PNJ: Tespsichore la danseuse
Aron    -13° 8'     2   Or: 6, Remplissage de potions
Ile de Menakax  -12° 8'     1   Journal de bord du Cpt. Paxos (1/7)
Autophie    -14° 6'     1   Statue de Hermès
Ile de Sarakème     -15° 5'     2   Or: 5+10, Ruines
Phypoulème  -15° 5'     0   Or: 4+6+10, Ruines
Mer Minée (~ 18 - 38 XP, 3 cartes)
Ile Karespon    4° 9'   1   Or: 5+5+15, Ruines, Marchand (110 Or), Petits Cailloux (1/3)
Iloxos  2° 8'   2   Or
Hyxos   6° 8'   1   Or, Ruines, PNJ: Haristas l'Ingénue
Ekronie     5° 8'   1   Or, Ruines
Minespos    3° 7'   0   Ruines, Carte de la Mer Sauvage (1/5)
Irithi  5° 6'   1   Ruines, Auberge (45 Or), Marchand (110 Or), Hache Brisée d'Hephaïstos (1/8)
Mer Autogios (~ 30 XP, 2 cartes)
Ile Hypouné     9° 9'   1   Marchand (110 Or), Remplissage de potions, Carte de la Mer Sauvage (1/5)
Ile de Talusyne     9° 8'   1   Remplissage de potions
Ile Menos   9° 9'   1   Or: 6, Ruines, Auberge (50 Or)
Ile Tanes   9° 6'   1   Journal de bord du Cpt. Paxos (1/7)
Mer Telero (69 - 111 XP, 3 cartes)
Ile aux Bané    9° 11'  1   Marchand (80 or), Baguette des Drünes (1/6)
Phykroti    8° 12'  1   Ruines, Marchand (? or)
Ilot Ikantios   8° 13'  2   auberge (45 or)
Ile Réron   8° 14'  1   auberge (65 or), agrandissement du sac de nourriture
Phylunas    8° 11'  1   agrandissement du sac de nourriture, Clochette translucide (1/6), ruines
Mer Iloti
Rélunes     11° 6'  1   Or: 6+6+6, Ruines, Auberge (40 Or), Carte de la Mer Sauvage (1/5)
Ile de Pointecendre     12° 7'  1   Or: 4+4+5+6+20, Remplissage de potions, PNJ: Sagitor Pointecendre
Ile du Thaki    12° 5'  ?   Or, Auberge (40 Or), Fontaine
Orideasi    11° 5'  ?   Or, Remplissage de potions
Ile aux Dokien  12° 4'  2   Or, Ruines, Auberge (50 Or)
Ile de l'Enos   12° 3'  ?   Or, Ruines, Auberge (50 Or)
Mer Zikien (~ 20 - 35 XP, 3 cartes)
Ile de l'Arkrokon   15° -2'     2   Augmentation du sac de nourriture, Potion vide (1/5), Carte de la Mer Sauvage (1/5)
Menique     15° -1'     1   Or: 5+5+6+6, Ruines, Marchand (120 Or), Fontaine
Dokithien   15° -1'     0   Or: 4+4+5+6+10+10+15+20+20, Ruines, Héros: Maugrine la Vipère
Ile de Menors   14° 0'  1   Or, Ruines
Ile des Tritons     15° 1'  1   Or, Ruines, BOSS: Tristan Roi des Tritons
Mer Sauvage (~ 15 - 42 XP, 2 cartes) 2)
Ile Lesithone   14° -4'     0   Or, Remplissage de potions, BOSS: Galupin doré
Sarespion   13° -4'     2   Or, Marchand (110 or), Remplissage de potions
Ile d'Iraktien  13° -3'     2   Or, Ruines, Augmentation du sac de nourriture
Ile aux Ilopoulogos     15° -4'     0   Or
Mer Autogax (~ 21 - 30 Xp, 3 cartes)
Ekiti   -5 ° 12'    1   Or, Ruines, Fontaine, Auberge (40 Or), Balle de coton (1/5)
Ile de Dokalmiti    -4° 12'     2   Ruines, Auberge (50 Or), Marchand (90 Or)
Ile Harkiro     -3° 13'     1   Or, Ruines
Ilot Pelion     -2° 12'     0   Or, PNJ: Moine de Kabal
Ile Ilope   -2° 14'     1   Or, PNJ: Phocion le Séducteur
Ile de Pelien   -3° 15'     1
Mer Magaos (~ 40 - 78 XP, 3 cartes)
Ile Tané    -14° -7'    1   Statue d'Hermès, Ruines, Marchand (110 or)
Ile Theskande   -12° -6'    2   Hache Brisée d'Hephaïstos (1/8), Ruines
Régma   -16° -6'    1   Marchand (80 or), Or: 4+25, Auberge (45 or), Ruines, Journal de bord du Cpt. Paxos(1/7)
Ile aux Phykroro    -15° -9'    0   Canne intermédiaire, remplissage de potions, Clochette translucide (1/6)
Mer Ari (~ 45 - 72 XP, 3 cartes)
Ilot du Telelulogos     4° -9'  1   Or: 20+6, Remplissage de potions, Héros: Antones Prince de Halberti
Ile aux Pelon   4° -10'     2
Ile de l'Irithios   6° -9'  0   Or: 6, Ruines, Auberge (40 Or)
Ile aux Harpe   5° -7'  2   Or, Ruines, Auberge (55 Or), PNJ: Héron l'Ingenieur
Ile des Arie    5° -8'  0   Ruines, Hache Brisée d'Hephaïstos (1/8)
Mer Karagha (~ 108 - 183 XP, 3 cartes)
Phynie  17° 1'  2   Or: 6+?+? , Ruines, Baguette des Drünes (1/6)
Ile aux Dokaktos    18° 0'  0   Or: ?+?+plein
Ilot Gasyne     19° 1'  ?
Ilot du Lesors  18° -3'     1   Or: 10+… , Ruines
Ireskax     18° -1'     1   Ruines
Gaxos   17° -2'     1   Ruines, PNJ: Albatoros le Grand Pirate
Mer Dokique (~ 30 XP, 2 cartes)
Ile de Hysyne   -9° 5'  1   Or, Remplissage de potions, Hache Brisée d'Hephaïstos (1/8), Balle de coton (1/5)
Irème   -9° 4'  1
Ile aux Iraos   -10° 3'     1   Auberge (65 Or)
Mer Eti (75 - 135 XP, 3 cartes)
Erimaque    -1° 12'     0   Journal de bord du Cpt. Paxos (1/7), Remplissage de potions
Ile du Kylukon  0° 12'  1   Ruines
Ile aux Magotisone  1° 12'  0   PNJ: Télémaque Apprenti Pirate
Ile Aroulos     0° 14'  2   Clochette translucide (1/6), Marchand (?? Or)
Mer Arix (~ 80 - 132 XP, 3 cartes)
Karande     -1° -10'    1   Auberge (55 Or)
Ilot Ikaphosors     -2° -11'    ?   Or: 10+6+5+4+? , Remplissage de potions, Petits Cailloux (1/3)
Ile des Ikie    -3° -10'    1   Or: 5+?+?+? , Ruines, PNJ: Queshua le Campeur
Ile Tati    -4° -10'    1   Or, Ruines, Statue de Déméter
Ile d'Autohéron     -5° -12'    2   Marchand (120 Or), Augmentation du sac de nourriture, Héros: Tiber
Ile des Orion   -2° -13'    1   Ruines, Marchand (90 Or), Temple
Mer Sarique (~ 33 - 63 XP, 2 cartes)
Oraos   -9° -10'    1   Rose d'Airain
Ile Harluxos    -8° -9'     1   Or: 5+5+6+6+6+6+6+10+10+15+20+20+20, Ruines
Ile Autolème    -7° -9'     1   Or: 4+4+5+6+6+6+10+10, Ruines, Auberge (50 Or), Héros: Horas le Fou
Ile du Garinos  -7° -10'    0   Or, Ruines, Marchand (80 Or)
Mer Ikipsios (~ 70 - 136 XP, 3 cartes)
Ile de Minitha  0° 9'   0   Or: 15+10, Ruines, Auberge (65 Or), PNJ: Cassandre la Prophétesse
Kygone  1° 9'   3   Ruines, PNJ: Estebanos
Ile Réfi    1° 9'   0   Or: 20+10, Ruines
Ilot Dokespone  -1° 10'     1   Ruines, Héros: Epivone
Mer Autones (~ 48 - 80 XP, 3 cartes)
Ile aux Réro    2° -12'     2
Ilot du Pelespa     2° -12'     0   Or: 5+5+4+4, Ruines, Marchand (??), Courrier Égaré (1/5)
Telegenesikon   2° -12'     1   Or: 20, Ruines, Auberge (65 Or)
Spenes  1° -12'     1   Or: 4, Ruines, Auberge (65 Or)
Gakrosyne   2° -13'     1   Or: 10+4, Ruines, PNJ: Agape Prêtresse de Zeus, Petits Cailloux (1/3)
Mer Dokaxi (~70-105 xp)
Ile Irespiti    14° 5'  1   Or: 20+10+5+5+5+5+4+?+?+?+? , Ruines, Potion Vide (1/5)
Autokrokon  17° 5'  ?   ?
Ile Karaktors   16° 7'  1   remplissage de potions
Zikaktique  14° 7'  0   marchand (120), ruines
Ile d'Emathéxos     14° 7'  2   ruines, auberge (55 or)
Mer Eliné (~ 40 - 78 XP, 3 cartes)
Ile de Karas    -15° -4'    1   Stand de remplissage de potions, Cristaux de Mecha (1/6)
Ile de Phylugma     -15° -2'    1   Or: 30+15+15+6+6+6+6+6+4, Marchand, Ruines, Héros: Egoïne la Panseuse
Ile Pelande     -14° -3'    1   Or: 5+6+10+20+30, Ruines, Auberge (40 Or), Augmentation du sac de nourriture, Hache Brisée d'Hephaïstos (1/8)
Ile aux Phykiti     -13° -1'    1   Or: 30+20+15+10+6+6+6+5+4+4, Ruines
Mines de Mecha  -13° -3'    1   Or: 10+10+6+6+5+5+4+4, Remplissage de potions, BOSS: Envoyé d'Hypérion
Ile aux Thors   -12° -3'    ?   Or: 15+15+15+5?+4, Ruines
Mer Telekrophie (~ 21 - 36 XP, 3 cartes)
Magos   -4° 19'     1   Or: 10+4+4+5+10+4+… , Marchand (80 Or), Remplissage de potions, Augmentation du sac de nourriture, Bibliothèque
Rékon   -7° 19'     1   Ruines
Ilot du Ikix    -7° 19'     1   Or: 4+5+10+5+15+…
Ile du Sarique  -3° 20'     1
Ile de Kari     -3° 16'     1   Ruines
Kyfi    -4° 18'     1   Statue de Hermès, Auberge (40 Or)
Mer Phygma (~ 12 - 39 XP, 3 cartes)
Ile Minios  -13° 4'     2   Or: 6+6, Ruines, PNJ: Ariane la Tisserande
Ile de Zikipson     -15° 1'     1   Or: 15+15, Ruines, Héros: Espiroth Banni des Dieux
Ile de l'Orantaos   -14° 0'     2
Ilot du Hyné    -14° 2'     0   Or: 15+10+10+5+5+4+4+4, Remplissage de potions, Baguette des Drünes (1/6)
Ile de l'Autopougique   -12° 0'     0   Or: 20+10+10+4+4, Remplissage de potions
Hylufi  -12° 1'     1   Or: 20+6, Auberge (40 Or), Marchand (90 Or), PNJ: Sage de Drüne
Mer Rénos (~ 18 - 36 XP, 2 cartes)
Harro   -9° 13'     1   Or:20+20+6+6+6+4, PNJ: Néophyte la Destinée, Ruines
Ilot de l'Irakon    -9° 12'     2   Or: 10+6, Remplissage de potions
Ile du Magique  -10° 11'    0   Or: 30+6, Ruines
Mer Iron (~ 50 - 75 XP, 3 cartes)
Ariti   10° -8'     1   Ruines, Potion Vide (1/5)
Récif de Pelique    9° -9'  1   Crâne de Ptéros
Récif aux Galukons  9° -10'     1   Ruines, Journal de bord du Cpt. Paxos (1/7)
Ilot Spesyne    7° -10'     1   Bibliothèque
Ile d'Efi   8° -10'     1
Bahéti  9° -10'     1   Ruines
Mer Elifi (~ 60 - 120 XP, 3 cartes)
Harkrogie   -7° -14'    1   Or: 30+15+6+6+4, PNJ: Europe Nymphe de l'Océan
Ilot de Harhélème   -8° -12'    0   Or: 20+20+6+4+4, Ruines, Auberge (55 Or), Carottes de Drüne (1/5)
Ile Autoro  -9° -13'    1   Or: 4, Ruines
Ile Iloné   -9° -13'    1   Or: 10+5+4, Ruines, Auberge (65 Or)
Ile Sarespon    -8° -14'    1   Or: 20+6+6, Fontaine, Remplissage de potions
Autopoulos  -10° -15'   2
Mer Gakronas (~ 21 - 39 XP, 2 cartes)
Autohélogos     -11° 12'    0   Ruines, Marchand (110 Or), Fontaine, PNJ: Sage de Drüne
Repoulos    -11° 11'    2   Or: 20+10+10+10+6+6+5+5+4+4+4, Ruines
Ile des Telené  -13° 12'    2   Or: 30+30+15+15+6+5+4+4
Ile du Peliti   -13° 10'    0   Or: 20+20+20+15+15+10+10+10+6+6+6+5+5+4+4, Remplissage de potions, Potion Vide (1/5)
Mer Zikéidos (~ 81 - 138 XP, 2 cartes)
Ile aux Rélogos     -2° -16'    1   Or: 20+15+15+5+5+5+5+5+4+4, Auberge (65 Or), Remplissage de potions, Carottes de Drüne (1/5)
Iroulon     -3° -16'    1   Or: 20+15+15+15, Auberge (45 Or), Remplissage de potions, Carottes de Drüne (1/5)
Autolanas   -4° -16'    1   Or: 30+6+5+5+5
Ile aux Kylème  -2° -15'    1   Or: 20+10+6, Ruines, Marchand (??), Statue de Poséidon
Mer Sarix (~ 39 - 75 XP, 3 cartes)
Ile Peloulax    2° -15'     1   Or: 10+10+6+5, Remplissage de potions, Héros: Keperi Liche Vagabonde
Galafi  1° -15'     1   Or: 20+6+6+5+4, Remplissage de potions
Iralmax     3° -17'     1   Or: 20+5+4, Ruines, Augmentation du sac de nourriture, Bibliothèque
Ilot du Garimaque   0° -18'     0   Or: 10+6+4+4, Ruines, Courrier Égaré (1/5)
Ile des Minande     2° -18'     2   Or: 10+5+6, Ruines
Réfi    3° -20'     1   Or: 20+20+10+6+6+6+5+4, Remplissage de potions
Mer Ilologos (~ 50 - 60 XP, 3 cartes)
Ile de la désolation    4° -15'     1   Héros: Stirenx l'Ombre de Krusk, aucun combat
Récif Iriti     5° -15'     1   Remplissage de potions, Journal de bord du Cpt. Paxos (1/7)
Ile de l'Irande     6° -14'     2   Ruines, Temple
Takroron    5° -14'     0   Statue de Poséidon
Récif de Spélikon   4° -15'     1
Régée   4° -17'     1   Carte de la mer d'Hypothésis (1/12)
Mer Ireskors (~ 50 - 70 XP, 4 cartes)
Maison royale d'Halberti    8° -15'     1   Or: 20+20+15+6+6+5, Auberge (45 Or), Remplissage de potions, PNJ: Roi Phéros IV de Halberti, PNJ: Cléomène l'administrateur, aucun combat
Ile des Harliro     9° -16'     1   Or: 6+6+6+6+5+5+4+4, Remplissage de potions
Ile d'Iroulès   9° -15'     0   Or: 15+6+4, Carte de la mer d'Hypothésis (1/12)
Eriné   10° -14'    1   Or: 25+20+20+10+6+6+4, Ruines, Temple
Ile d'Ilosine   10° -14'    1   Or: 20+10+10+10+6+5+4+4, Blason d'Halberti (1/5)
Tha     11° -13'    1   Or: 4+5+4+6+… , Ruines, Marchand (?? Or)
Ile du Lesespès     11° -16'    2   Auberge (45 Or), Ruines, Augmentation du sac de nourriture
Mer Phynes (~ 111 - 180 XP, 4 cartes)
Irakors     14° -14'    1   Or: 20+15, Auberge (50 Or), Remplissage de potions
Ile de Menien   14° -13'    1   Ruines, Marchand (90 Or), Baguette des Drünes (1/6)
Ile d'Irique    15° -14'    1   Ruines
Ile des Magien  16° -15'    1   Remplissage de potions
Ile aux Harrikon    17° -15'    1   Remplissage de potions, Agrandissement du sac de nourriture
Mer Leseskique (~ 80 - 110 XP, 3 cartes)
Enos    3° 10'  1   Or: 20+10, Marchand (110 Or), Temple, Remplissage de potions
Autogma     ?° ?'   ?   ?
Ile Orion   4° 13'  2   Héros: Tatsi
Orien   ?° ?'   ?   ?
Irien   ?° ?'   1   Ruines, Fontaine
Mer Dokion (81 - 198 XP, 3 cartes)
Ile des Menès   3° 17'  1   Or: 15+4+?+5, Ruines, Carte de la Mer d'Hypothésis (1/12)
Ile de Sarideasande     1° 18'  0   Or: 5+5, Baguette des Drünes (1/6), Ruines
Ile Phyriné     1° 19'  1   Auberge (65 Or), Collier d'Harmonie (1/5)
Ilot d'Ora  0° 20'  2   Or: 5+20+6+6+6+? , Marchand (120 Or)
Ilot des Arique     3° 20'  1
Mer Spelipe (72 - 105 XP, 3 cartes)
Grand Temple de Kabal   -3° 23'     1   Augmentation du sac de nourriture, Remplissage de potions, PNJ: 2x Moine de Kabal, BOSS: Stalskin Pope de Kabal
Ile de Magaxone     -3° 23'     1   Or: 4+20+5+4+? , Ruines, Auberge (60 Or)
Ile du Thaphoseu    -3° 22'     1   Or: 5+5+4+? , Ruines
Ile aux Orès    -4° 24'     1   Augmentation du sac de nourriture, Ruines, Auberge (40 Or)
Ile des Iries   -5° 24'     1   Choux de Kabal (1/5), marchand (90)
Mer Zikax (60 - 111 XP, 2 cartes)
Araki   -9° 22'     1   Or: 5+5+15+4+10+5+… , Remplissage de potions, Statue de Poséidon, Auberge (65 Or)
Ile de Hygi     -9° 23'     ?   ?
Ile des Bapounas    -9° 23'     1   Or: 15+15+… , Remplissage de potions
Ile du Pealos   -9° 24'     0?  Or: 20+5+4+5+4+10+… , Ruines (330 Or/165 xp)
Mer Speron (105 - 192 XP, 3 cartes)
Ile de Régma    -18° 8'     0   Marchand (120 Or), Ruines
Ile des Karipsème   -19° 8'     1   Ruines, Temple
Ile aux Ilokisis    -18° 7'     2   Ruines, Augmentation du sac de nourriture, Statue d'Arès
Ile Ilopounes   -21° 7'     1   Or: 5, Marchand (90 Or), Cristaux altérés
Ile aux Speluro     -20° 8'     ?
Mer Ikantors (~ 21 - 39 XP, 3 cartes)
Ile désertique  -17° 11'    1   PNJ: Panagis du Désert, Fontaine
Ile du Thatomas     -15° 11'    0   Ruines, Perce-sable
Ile de l'Orie   -17° 12'    0   Auberge (45 Or), Ruines
Menamnesée  -18° 11'    3   Remplissage de potions, Augmentation du sac de nourriture
Mer Orax (72 - 126 XP, 3 cartes)
Tagma   -5° -23'    1   Statue de Poséidon
Ile aux Hynas   -5' -22°    1   Remplissage de potions, Blason d'Halberti (1/5)
Spegramanie     -2' -23°    1   Auberge (50 Or), Remplissage de potions
Hymaque     -3° -25'    1   Ruines, Auberge (55 Or), Carte de la mer d'Hypothésis (1/12)
Ile de Pelande  -4° -25'    1   Ruines
Ile de Ganes    -4° -25'    1   Auberge (45 Or), Ruines
Mer Arion (39 - 78 XP, 2 cartes)
Ile Spethropofi     4° -20'     1   Ruines, Clochette translucide (1/6)
Ilot Orespios   5° -19'     1   Marchand (80 Or), PNJ: Zénon le Messager
Ile des Phyro   5° -18'     2   Statue d'Arès, Ruines
Ile du Harhékon     6° -19'     0   Ruines, Auberge (60 Or)
Mer Baron (45 - 75 XP, 4 cartes)
Ilot Bapougas   5° -21'     1   Ruines, Auberge (40 Or), Augmentation du sac de nourriture, Courrier Égaré (1/5)
Ile du Magéidors    5° -22'     0?  Ruines, Augmentation du sac de nourriture, Courrier Égaré (1/5)
Ile du Bané     4° -24'     2   Remplissage de potions, Marchand (80 Or), Carte de la mer d'Hypothésis (1/12)
Ile de l'Orakon     6° -25'     1   Remplissage de potions
Iraghon     6° -25'     1   Blason d'Halberti (1/5)
Sarix   8° -22'     1   Ruines, Marchand (80 Or), Temple
Mer Thaghos (45 - 72 XP, 2 cartes)
Lesalmors   9° -19'     1   Courrier Égaré (1/5)
Ero     ?° -?'  2   Ruines, Marchand (120 or)
Mer du Nord (~ 75 - 132 XP, 2 cartes) 3)
Erisis  -4° -19'    1   Ruines, Marchand (120 Or), Lettre royale
Pelix   -3° -19'    1   Bibliothèque
Mer Gagma (~ 111 - 198 XP, 2 cartes)
Ile Zikakios    2° 23'  1   Marchand (100 Or), Collier d'Harmonie (1/5)
Ile de Minanton     -1° 23'     0?  Marchand (110 Or), Ruines, Collier d'Harmonie (1/5)
Teleti  4° 24'  1   Ruines
Dokoula     4° 23'  2   Ruines
Mer Peleskès (~ 75 - 117 XP, 3 cartes)
Ené     6° 20'  1   Auberge (40 Or)
Ilot de Ika     6° 18'  1
Irée    7° 17'  2
Ile de Pak 4)   7° 17'  1   Ruines, Mémoires de Paxos
Ile de Menème   9° 17'  1   Ruines
Mer Répoufi (~ 100 - 196 XP, 2 cartes)
Oreu    12° 16'     0?  Ruines
Ile Aralmion    14° 16'     2   Ruines
Mer Pelaktix (~ 110 - 201 XP, 3 cartes)
Ile d'Asterope  19° 16'     1   Ruines, Auberge (45 Or), BOSS: Astérope
Ilot aux Gakrofi    18° 14'     2   Ruines, Carte de la mer d'Hypothésis (1/12)
Ile du Lesi     23° 14'     0   Auberge (50 Or)
Ilot Gafi   23° 16'     1   Ruines
Mer Harkropoulos (~ 96 - 192 XP, 3 cartes)
Ile des Epouné  1° 31'  2   Ruines, Statue de Poséidon
Ile du Temps    2° 31'  1   Marchand (90 Or), Ruines, Augmentation du sac de nourriture, BOSS: Chronatorg
Mer Phype (~ 117 - 180 XP, 3 cartes)
Ile Arone   -17° 1'     2   Ruines, Statue d'Atlas, Augmentation du sac de nourriture
Ile du Phylufi  -21° 4'     0   Marchand (?? Or), Remplissage de potions
Lesaxande   -21° 4'     0   Ruines
Ile des Rékon   -20° 4'     1
Theskie     -20° 1'     2   Ruines
Mer Harnos (~ 102 - 174 XP, 4 cartes)
Ile de Semerkhet    -23° 5'     1   Ruines, BOSS: Momie de Semerkhet
Ile Irien   -25° 4'     1   Remplissage de potions
Mer Minon (~ 132 - 180 XP, 4 cartes)
Ile du Golem    22° -9'     1   Augmentation du sac de nourriture, Auberge (45 Or), Ruines, BOSS: golem prismatique
Ile des Zikeu   21° -8'     2   Remplissage de potions
Ikios   19° -6'     1   Remplissage de potions
Ile Oraghone    17° -10'    0   Marchand (110 Or), Ruines, Carte de la mer d'Hypothésis (1/12), Fontaine, Augmentation du sac de nourriture
Harlème     21° -6'     0   Marchand (100 Or), Ruines
Mer Karios (~ 66 - 120 XP, 2 cartes)
Ile de Hyrixos  -9° 18'     0   Marchand (80 Or), Ruines, Choux de Kabal (1/5)
Ile aux Harphie     -10° 18'    ?   Ruines, Miroir de Circé
Spepouxos   -10° 16'    2
Ile aux Ilorikon    -8° 20'     1
Mer Oranta (~ 90 - 192 XP, 3 cartes)
Ile-Prison de Tartan    6° 27'  0   Marchand (110 Or), Ruines, BOSS: 3x Cyclope de Tartan, PNJ: Prisonniers de Tartan
Ile de l'Orion  5° 29'  1   Collier d'Harmonie (1/5), Ruines
Ile du Tholos   8° 28'  1   Marchand (100 Or), Ruines, PNJ: Tholos (aucun combat)
Phype   6° 30'  2   Ruines, Statue d'Arès, Augmentation du sac de nourriture
Mer Thien (~ 81 - 168 XP, 5 cartes)
Hykipoulos  8° 24'  2
Ile aux Bahélogos   8° 24'  0   Auberge (45 Or), Augmentation du sac de nourriture
Aro     7° 24'  1   Ruines
Ile du Thée     6° 24'  1   Remplissage de potions
Ilot d'Oro  6° 23'  1   Ruines
Ile Hyluné  7° 23'  2
Ile Thande  10° 22'     1   Ruines
Mer Hynos (~ 120 - 180 XP, 4 cartes)
Ile aux Irie    13° 22'     1?  Ruines, Marchand (110 Or), Augmentation du sac de nourriture, Canne Professionnelle
Ile aux Araxos  13° 23'     0?  Ruines, Collier d'Harmonie (1/5)
Mer Magors (~ 171 - 267 XP, 5 cartes)
Minien  -19° -12'   1   Ruines
Ile Autogeu     -18° -12'   1   Fontaine
Ile Arakton     -20° -13'   1   Ruines
Menipsi     -19° -14'   1   Ruines
Ile des Spelunes    -18° -15'   2
Ile du Sarande  -21° -14'   1
Ile aux Oripsion    -21° -14'   1   Ruines
Ile Sarème  -21° -15'   1   Remplissage de potions
Mer Pelaxone (~ 51 - 69 XP, 4 cartes)
Ile de l'Arithème   -18° -1'    0   Ruines (320 Or/160 xp)
Ile des Oraki   -21° -1'    0
Ile Rénes   -21° -1'    1   Ruines (226 Or/113 xp)
Ilot des Spegios    -19° -2'    1
Résyne  -19° -3'    2   Ruines (220 Or/110 xp)
Ile du Karantès     -18° -3'    1
Mer Dokas (~ 30 - 66 XP, 3 cartes)
Kyhéro  -20° -6'    1   Cristaux de Mecha (1/6), Ruines (240 Or/120 xp)
Ile du Tagenesiron  -20° -8'    0   Marchand (90 Or), Ruines
Ilokigma    -18° -9'    2   Cristaux de Mecha (1/6)
Ile Ikios   -19° -9'    1   Ruines (186 Or/93 xp), Marchand (120 Or)
Mer Zikandros (~ 141 - 312 XP, 5 cartes)
Saraktors   -19° -21'   1   Ruines, Statue d'Arès
Ile de Bakon    -17° -20'   1   Ruines
Ile Kykixos     -16° -21'   0   Ruines, Auberge (40 Or)
Ile Gapousyne   -21° -18'   0   Remplissage de potions
Ile du Mini     -17° -18'   2   Ruines, Marchand (120 Or)
Ile Irès    -18° -17'   1   Marchand (100 Or)
Ile de l'Epougion   -15° -22'   2   Temple, Marchand (80 Or)
Ile du Harkromaque  -19° -18'   1   Ruines
Magie   -17° -16'   1   Ruines, Auberge (50 Or)
Mer Menalmie (~ 72 - 141 XP, 2 cartes)
Lesès   -7° -20'    1   Ruines, Marchand (80 Or), Carte de la mer d'Hypothésis (1/12)
Ile aux Bakrolème   -7° -19'    1   Marchand (80 Or), Auberge (65 Or)
Ile du Lesoula  -8° -19'    1   Ruines, Carottes de Drüne (1/5)
Ile aux Ehéti   -10° -20'   1   Carottes de Drüne (1/5), Auberge (65 Or)
Mer Aréidique (~ 75 - 120 XP, 3 cartes)
Ile du Kykiron  -13° -19'   1   Ruines
Ile de Drüne    -12° -20'   1   Ruines, PNJ: Mage Drüne, PNJ: Sage Drüne (aucun combat)
Ile aux Spegma  -12° -21'   1   Remplissage de potions, Augmentation du sac de nourriture
Ikiti   -12° -21'   1   Ruines, Auberge (65 Or)
Mer Bapoulos (~ 72 - 120 XP, 3 cartes)
Ile Harpouhie   23° 4'  1   Statue de Hermès
Bamaque     24° 3'  1   Ruines, PNJ: Antigone la Coiffeuse
Phyrisis    19° 6'  1   Remplissage de potions, Marchand (?? or), Ciseaux fins
Mer Hyrimaque (~ 102 - 186 XP, 5 cartes)
Iras    21° -2'     1   Carte de la mer d'Hypothésis (1/12)
Ilot des Ariti  24° -1'     0   Remplissage de potions, Temple, Marchand (90 Or)
Ile aux Hykrokon    24° -2'     3   Fontaine, Remplissage de potions
Ile Ekroné  24° -4'     0   Statue de Déméter
Takipe  24° -4'     1   Ruines
Mer Lesien (~ 96 - 195 XP, 2 cartes)
Volcan d'Héphaïstos     15° -9'     1   Ruines, PNJ: Esprit du Volcan
Ile de l'Ilosis     14° -10'    1   Ruines, Clochette Translucide (1/6)
Ilokrosis   13° -7'     1   ruines
Mer Oriti (~ 57 - 132 XP, 4 cartes)
Ile de l'Iri    -5° 28'     1   Bibliothèque, Remplissage de potions
Autoti  -7° 28'     1   Ruines
Ile de Peleskon     -7° 27'     1   Remplissage de potions, Choux de Kabal (1/5)
Ile Autologos   -10° 28'    1   Ruines, Choux de Kabal (1/5)
Harmaque    -9° 30'     0   Ruines
Dokakon     -3° 30'     1   Ruines
Ehépoulos   -3° 31'     1   Remplissage de potions
Ile Saroulax    -3° 28'     2   Auberge (35 or), marchand (80 or), Augmentation du sac de nourriture, Remplissage de potions
Mer Autoron (~ 48 - 87 XP, 3 cartes)
Sarème  -12° -14'   0   Ruines, Clochette Translucide (1/6)
Ile Ero     -15° -14'   1   Ruines, Carte de la mer d'Hypothésis (1/12)
Orotisa     -15° -13'   0
Ile d'Orekisque     -14° -12'   1   Auberge (40 Or), Cristaux de Mecha (1/6), ruines
Ile Irespie     -12° -13'   2   Ruines, Journal de bord du Cpt. Paxos (1/7)
Mer Spenes (~ 42 - 81 XP, 4 cartes)
Ilolème     0° -24'     1   Carte de la mer d'Hypothésis (1/12), remplissage de potions, auberge (55 or)
Ilot de l'Ilogma    0° -25'     1   Ruines
Ile de Hargenesiné  2° -25'     1   Agrandissement du sac de nourriture, auberge (50 Or), ruines
Orako   1° -26'     1   Ruines
Ile Magiti  1° -22'     1   Auberge (65 Or), ruines, Blason d'Halberti (1/5)
Mer Pelo (~ 72 - 102 XP, 2 cartes)
Ile aux Epoulos     -13° 17'    1   Remplissage de potions
Ile Ekroti  -13° 15'    2   Ruines
Mer Basyne (~ 12 - 36 XP, 3 cartes)
Ilot de Lesas   -18° 14'    1   Carte de la mer d'Hypothésis (1/12)
Ile Pelideasa   -20° 15'    1   Statue d'Hermès, Auberge (60 Or), Ruines
Phyron  -17° 16'    0   Bibliothèque, Ruines, Marchand (120 Or)
Ile aux Saroulie    -21° 17'    1   Ruines
Mer Ilokon (~ 123 - 177 XP, 4 cartes)
Ilot Ilogma     21° 13'     2   Ruines, Bibliothèque, Agrandissement du sac de nourriture
Ilot Iloxos     23° 11'     1   Ruines
Ile aux Rédeutenas  22° 10'     1   Ruines
Mer Iki (~ 70 - 126 XP, 3 cartes)
Autodeutené     -13° 20'    0   Ruines, Auberge (40 Or), Choux de Kabal (1/5)
Ganas   -14° 20'    0   Ruines, Auberge (55 Or)
Ile Kariti  -15° 21'    2   Remplissage de potions
Ile aux Dokas   -13° 18'    1   Ruines, Augmentation du sac de nourriture
Archipel Sombre (~ 86 - 106 XP, 5 cartes)
Gasis   -17° 20'    1   Auberge (45 Or), Sceau de la maison royale
Mer Irespax (~ 51 - 63 XP, ? cartes)
Automaque   -25° -4'    0   Remplissage de potions, Nectar
Lesas   -25° -1'    1   PNJ : Clio l'Historienne
Mer Enas (~ 138 - 180 XP, 2 cartes)
Ilot Oreskeu    -20° 11'    1   Auberge (55 Or)
Ilot Phyphie    -20° 10'    1   Ruines
Mer Autosyne (~ 126 - 192 XP, 2 cartes)
Zikaghos    -26° 11'    0   Ruines, Statue de Déméter
Mer Galème (~ 72 - 138 XP, 2 cartes)
Minique     -9° -25'    0   Marchand (90 Or), PNJ : Ancien Arbre-Drüne
Ile du Sarax    -7° -23'    0   Marchand (100 Or), Auberge (65 Or), Ruines
Ile du Iki  -8° -23'    2   Ruines, PNJ : Grand Maître (désapprendre une compétence)
Mer Sarespax (~ 132 - 267 XP, 2 cartes)
Eron    17° -18'    0   Marchand (80 Or), Ruines
Ile d'Araghon   16° -19'    1   Marchand (90 Or), Ruines, Auberge (50 Or)
Galunes     14° -19'    1   Remplissage de potions
Mer Galugion (~ 180 XP, 5 cartes)
Autopapasis     18° -23'    1?  Statue de Déméter
Mer Orakiti (~ 105 - 156 XP, 2 cartes)
Hylaron     -15° -9'    1   agrandissement du sac de nourriture, PNJ : Alcméon le Crouton, remplissage de potions
Mer Régma (~ 60 - 132 XP, 3 cartes)
Ilot aux Spegma     16° 11'     2   ruines, fontaine
Hynos   15° 11'     1   remplissage de potions
Ilot Aroula     14° 12'     0   ruines
Dokitheu    14° 12'     1   remplissage de potions
"""

# --- objets ---

ITEMS = """
    Planche Île de l'oracle, 5 exemplaires  Une solide planche en bois, utilisée en construction navale. Nécessaires pour débloquer le bateau.
    Canne du Débutant   Mer Harmaque - Ile Aralmi -4°-8'    Cette canne-à-pêche est très pratique pour pêcher, mais uniquement les petits poissons sur les mers calmes !
Permet de pêcher une fois par jour dans les ports de mers proches. Gain entre 0 et 16 rations.
    Canne Intermédiaire -14° -9'    Cette canne-à-pêche permet de pêcher les poissons de taille intermédiaire dans les mers peu agitées !
?   Canne Professionelle    13° 22' Cette canne-à-pêche permet de pêcher les poissons de grande taille intermédiaire dans les mers très agitées !
    Épi de Blé  Mer Minithée - Aranthée -4°1'
Mer Arème - Ile Ilophie -1°3'
Mer Ilokixos - Miniti -2°3'
Mer Kyfi - Ilot Harhéxos 3°1'
Mer Phyhépe - Minithion 1°-5'   Un simple épi de blé, sans pesticides, tout ce qu'il y a de plus naturel.
    Feuilles de Lotos   Mer Phyhépe - Ile de l'Elogos 0°-1' Ces larges feuilles sont assez rares. Elles sont parfois utilisées pour guérir des blessures graves
Nécessaires pour guérir Dolskin.
    Racines de Moly Mer Ikaxas - Autofi -6°3'   Les racines de Moly sont connues pour être efficaces contre de nombreuses maladies.
Nécessaires pour guérir Dolskin.
    Lance de Zeus   Mer Rekrones - Ile Hyti -7°-4'  Il parait qu'elle lance des éclairs… Mais il faudrait être niais pour y croire !
Vendu par Barnabas l'Arnaque pour 100 Pièces d'or.
    Conque des Tritons  2°-9'   Vendu par Mélos le marchand pour 200 Pièces d'or.
    Pendentif de Zeus   Mer Kareskiti - Orakas -6°6'    Un petit medaillon quelconque à l'image de Zeus.
Montrer la Lance de Zeus à Dimitri le Croyant. Il faut le donner à Agape Prêtresse de Zeus en 2-.13 qui cherche tout objet à effigie de Zeus pour avoir un morceau de l'Etoile du Nord .
    Page de Poème   Mer Harmaque - Elusyne -3°-6'
Mer Autoripe - Minespème 3°3'
Mer Orès - Ilôt du Spesyne 7°-2'
8°-6'   La page d'un poème, raturée mille fois: seul son auteur pourra la déchiffrer.
Les apporter à Apollinaire le Poète sur l'île de l'Aralmie (3°-3').
    Médaille de Kabal   Mer Ilosyne - Ile Saralmique -9°6'  Cette petite médaille discrète est frappée de l'emblème des moines de Kabal. Elle indique les récifs avec précisions.
    Carte des Mines Mer ? - Autohélogos -11°12' Cette carte vous permettre d'accéder aux Mines
    Balle de Coton  Mer Dokique - Ile de Hysyne -9°4'
Mer ? - Ile Phyliti -9°7'
Mer ? - Ile Bakimaque -9°9'
Mer ? - Gati -2°8'
Mer ? - Ekiti -4°12'    Bien tissé, ce coton de bonne qualité devrait être solide.
Nécessaire pour la Voile Antiphon.
    Voile Antiphon  -4°1'   Double la vitesse du bateau.
    Crâne de Ptéros     Mer Iron - Récif de Pelique 9°-9'   Le crâne effrayant d'un animal depuis longtemps éteint, qui vivait jadis dans un autre monde.
    Carte de la Mer Sauvage Mer Orès - Dokien 9°-1'
Mer Minée - Minespos 3°7'
Mer Autogios - Ile Hypouné 9°9'
Mer Iloti - Rélunes 11°6'
Mer Zikien - Ile Harkrokon 15°-2'   Cette carte, une fois complétée, vous permettra d'accéder à la Mer Sauvage.
    Blason d'Halberti   Mer Aroulique - Spelulogos 1°-7'
Mer Ireskors - Ile d'Ilosyne 10°-14'
Mer Orax - Ile aux Hynax -5°-23'
Mer Spenes - Ile Magiti 2°-22'
Mer Baron - Iragon 6°-26'   Ce blason représente l'emblème de la Maison Royale d'Halberti. Ancienne noblesse des hommes de l'Olympe.
    Rose d'Airain   Mer Sarique - Oraos -9°-10' a donné a flora la fleuriste pour obtenir Ruban de flora
    Ruban de Flora  Mer Phyhèpe - Récif Leksatone 0°-4' Imprégné d'une douce odeur de fleurs. A emmener à Nikolaos le Jardinier (ile Miniti -2°3', mer Ilokixos)
    Petits Cailloux Mer ? - Ile Karespone 4°9'
Mer ? - Gakrosyne 2°-13'
Mer ? - -2°-11  De simples petits cailloux bien ronds, mais pour faire quoi ?
    Pierre de Cronos    Mer ? - Mines de Mecha -13°-3'  Cette pierre a permis au Titan Hypérion de produire de grandes quantités de Mecha.
Objet de quête final de Gloria.
    Bague de Mariage    15°1'   Objet de quête final de Hératus.
S'obtient donnat Conque des Tritons au Triton, se rend à Cunegorde en 7°4'.
    Cocon de Ver    Mer Telekrophie - Rékon -7°18'  Un cocon dont ne sortira pas un papillon, mais un ver des sables de plusieurs kilos !
L'amener à Ariane la Tisserande.
    Hache Brisée d’Héphaïstos   Mer Orème - Ilôt du Karée 11° -6'
Mer ? - Irithi 5°6'
Mer Dokique - Ile de Hysyne -9°4'
Ile de Theskande -12°-7'
Ile Thaos -5°6'
-8°6'
?
?   La célèbre hache du Dieu Hephaïstos, forgée dans le feu d'un volcan.
Quête du héros Torkish.
    Hache d’Héphaïstos  ?   Objet de quête final de Torkish.
    Mal à la Tête   Mer ? - Ile de l'Aralmie 3°-2'  Ouille ouille ouille !
Finir la quête d'Apollinaire le Poète. A donner a Cassandre la Prophétesse en 0°9'
    Plume de Galupin    Mer Sauvage - Ile Lesithone 14°-3'  La preuve indéniable du succès de la chasse au Galupin.
Objet de quête final de Céleïde.
    Carte de Marchand   -12° 8' Cette carte de membre de la Guilde des Marchands vous permet d'obtenir 20% de réduction chez tout les marchands !
Faire la quête de Tespsichore la Danseuse.
    Perce-sable Mer Ikantors 15°12'     Une simple fleur blanche, mais à l'odeur très sucrée
    Amadou Allume-feu   8°4'    Indispensable pour allumer un joli feu de bois !
Vendu par Phébus l'Illuminateur pour 200 Pièces d'or.
À donner à un campeur en -3°-10' pour obtenir Viande Grillée.
    Cristaux de Mecha   Mer ? - Ile de Karas -15°-4'
-20° -3'
-21° -7'
-18° -9'
-14° -12'
-12° -10'   Ces étranges cristaux semblent contenir de l'énergie à l'état pur.
    Fruit Appétissant   Mer ? - Ile du Tariphie -8°0    Il a l'air drôlement bon !
Faire la quête de Boudine l'Assoiffée, le donner à Papapapapapalopoulos 1°0'.
    Gros Légume ?   ?
    Viande Grillée  Mer ? - Ile de Ikie -4°-10' Seul les gourmets sauront l'apprécier.
[Donnez un Amadou Allume-Feu à Queshua le Campeur.
    Bêche à Légume  Mer Thaghos - Ile de Spesyne 8°-20  Un outil fort pratique pour la récolte des légumes.
    Courrier Égaré  ?   ?
    Timbres Royaux  ?   ?
    Fil d'Ariane    Mer ? - Ile Minios -13°4'   Une pelote d'un fil très résistant tissé par Ariane elle-même !
Faire la quête d'Ariane la Tisserande, ensuite disponible pour 100 pièces d'or.
    Miroir de Circé Mer Karios - Ile aux Harphies -9°18'    Permet de voler des runes aux monstres !
Donne une rune spéciale en jeu.
    Collier d'Harmonie  ?   ?
    Clochette Translucide   Mer ? - Ile aux Phykroko -14°-9'    Une simple petite clochette, mais légèrement transparente, comme si elle n'appartenait pas tout à fait à ce monde.
Objet de quête final de Stirenx.
    Sceau de la Maison Royale   Archipel Sombre - Ile Gasis -17°20'     Objet de quête final de Tiber.
    Corail Arc-en-Ciel  10°0' ×3    Ce corail est extrêmement rare et très apprécié des collectionneurs.
Finir la quête de Démosthène le Bègue.
    Casque d'Orichalque Mer ? - Ilot aux Epoufi 3°1'    Un casque d'une grande puissance, très utile dans les combats contre les monstres !
Baisse la difficulté du jeu ?
Donner un Corail Arc-en-Ciel à Papy Pyrhus.
    Épée d'Orichalque   ?   ?
    Baguette des Drünes Mer ? - Ilot du Hyné -14°2'
Mer Arespax - Ile Irispsios -8°12'  Cette baguette magique peut créer une source d'eau à l'endroit où elle est plantée ! (A donner sans doute à Panos, île Téléphie en -2°,-2')
objets  Journal de bord du Cpt. Paxos   Mer Autogios - Ile Tanes 9°6'
Mer Iron - Récif aux Galukon 9°-10'
Mer Iko - Ile de Menakax -12°8'
à verifier -16°-6 et -12° -13° (7 en tout)  Les feuillets du journal de bord du Capitaine Paxos, dont le trésor n'a jamais été retrouvé ! A rapporter à Plutarque l'écrivain -8° -6'
    Étoile du Nord  Mer ? - Miniti -2°3'    Cette étoile, une fois complète, permettra d'accéder à de nouvelles mers !
Quête de Nikolaos le Jardinier.
    Choux de Kabal  Mer Karios - Ile de Hyrixos -9°17' ×5   De magnifiques choux, prêts à planter !
objets  Potion  -13° 10' ile de Peliti mer Gakronas
10° -8' Ile Ariti Mer Iron
8° -4' Ile de Balème mer Orème
14° 5' Ile de Irespiti mer Dokaxi
    Chaque potion vous permet de stocker 10 Runes pour régénérer vos héros.
Remplir vos potions dans les bâtiments adéquat. Utiliser hors combat.
    Ciseaux Fins    ?   Objet de quête final de Horas.
    Lettre Royale   ?   ?
    Bouclier Rouillé    ?   ?
    Etoile de Mer à Sept Branches   ?   ?
    Carottes de Drüne   ?   ?
objets  Carte de la mer d'Hypothésis    Ilot de Lesas -18°15' (12 éléments)     Cette carte une fois complétée vous permettra d'accéder à la mer d'Hypothésis
objets      ?   ?
"""

# --- ruines ---

RUINS = """
Coordonnées positives   Nom de l'ile    Gain en or  Liste des ennemis
0° 2'   Récif des Enas  196 or  Bulot maudit, Raide momie, Panthère, Blob féroce, Foudrine, Araignée géante
0° 9'   Ile de Minitha  280 or  Sado-gorgogne, Panthère, Raide momie, Golem d'argile, Foudrine
0° -1'  Ile de l'Elogos     60 or   Apprenti, Araignée géante
0° -8'  Ile des Tagma   54 or   Diablotin sournois, Blob puissant
0° -10'     Irique  290 or  Homme lézard, Poisillon, Squelette vengeur, Ame en peine, Diablotin sournois, Squelette vengeur, Frisquette
0° -18'     Ilot du Garimaque   236 or  Shaman-poussière, Blob féroce, Renard laineux, Ame en peine, Bulot maudit, Renard laineux
1° 9'   Kygone  320 or  Minotaure, Diablotin sournois, Rototo, Armanite puante, Picounet, Foudrine
1° 9'   Ile Réfi    270 or  Apprenti, Chauve-chat farceur, Scarabée géant, Pygmé incrédule, Bulot maudit, Fulgor
1° 27'  Taro    604 or  Squelette vengeur, Pygmé incrédule, Diablotin sournois, Poisillon, Scarabée géant, Tape-Taupe, Apprenti, Apprenti, Fulgor, Sorcier de l'Aurore, Apprenti, Blob Puissant, Sorcier de l'Aurore
1° -2'  Récif d'Ilogramamaque   60 or   Serpent venimeux, Serpent venimeux, Serpent venimeux
1° -7'  Spelulogos  160 or  Mouskito family, Tape-Taupe, Bulot maudit, Renard laineux
1° -9'  Ile aux Autokigma   190 or  Homme lézard, Frisquette, Scarabée géant, Seigneur cobra
1° -12' Spenes  320 or  Fulgor, Serpent venimeux, Serpent venimeux, Homme lézard, Panthère, Foudrine, Galupiote, Araignée géante, Panthère
1° -12' Telegenesikon   180 or  Homme lézard, Squelette vengeur, Poisillon, Picounet
1° -12' Ilot du Pelespa     216 or  Seigneur cobra, Foudrine, Panthére, Apprenti, Foudrine, Blob féroce, Foudrine
1° -13' Gakrosyne   190 or  Fulgor, Frisquette, Poisillon, Araignée géante, Bulot maudit, Araignée géante
2° 27'  Ilosis  396 or  Rototo, Fulgor, Raide Momie, Blob Féroce, Ame en peine, Ame en peine, Sado-gorgogne, Panthère
2° 31'  Ile du Temps    370 or  Chauve-chat farceur, Guêpe géante, Pygmé incrédule, Sado-gorgogne, Apprenti, Sorcier du crépuscule
2° -10' Ile Sarix   50 or   Serpent venimeux, Blob féroce, Blob puissant
2° -15'     Ile de Hargenesiné  260 or  Apprenti, Guêpe géante, Poisillon, Sado-gorgogne, Foudrine, Squelette vengeur
2° -18' Ile des Minande     200 or  Raide momie, Armanite puante, Bulot maudit, Scarabée géant
3° 1'   Ilot aux Epoufi     300 or  Apprenti, Sorcier du crépuscule, Pygmé incrédule, Homme lézard, Renard laineux, Ame en peine, Frisquette
3° 4'   Magepisa    500 or  Sado-gorgogne, Armanite puante, Galupiote, Mouskito family, Mouskito family, Raide Momie, Fulgor, Sorcier du crépuscule
3° 7'   Minespos    184 or  Mouskito Family, Scarabée géant, Galupiote, Foudrine, Blob puissant, Blob
3° -3'  Ile de l'Aralmie    54 or   Ame en peine, Blob puissant
3° -4'  Ilot de Hynas   20 or   Araignée géante
3° -17'     Iralmax     490 or  Scarabée géant, Diablotin sournois, Picounet, Sorcier du crépuscule, Poisillon, Scarabée géant, Frisquette, Galupiote, Mouskito family, Golem d'argile
4° 3'   Minespème   210 or  Frisquette, Galupiote, Scarabée géant, Homme lézard, Foudrine, Bulot maudit
4° 3'   Balème  110 or  Seigneur cobra, Araignée géante, Pygmé incrédule
4° 4'   Ile de l'Iramnesème     280 or  Picounet, Scarabée géant, Mouskito family, Âme en peine, Guêpe géante, Renard laineux, Araignée géante
4° 9'   Karespon    196 or  Fulgor, Ame en peine, Poisillon, Scarabée géant, Blob féroce
4° -2'  Ilot de Telelogos   300 or  Minotaure, Ame en peine, Raide Momie, Apprenti, Renard laineux, Araignée géante
4° -7'  Ile aux Harpe   240 or  Homme lézard, Scarabée géant, Squelette vengeur, Sorcier du crépuscule, Foudrine
5° 6'   Irithi  114 or  Scarabée géant, Bulot maudit, Blob puissant, Renard laineux, Serpent venimeux
5° 8'   Ekronie     116 or  Araignée géante, Diablotin sournois, Renard laineux, Blob féroce, Serpent venimeux
5° -2'  Ikeskone    180 or  Seigneur Cobra, Shaman-poussière
5° -8'  Ile des Arie    210 or  Scarabée géant, Pygmé incrédule, Armanite puante, Picounet, Serpent venimeux, Serpent venimeux
6° 8'   Hyxos   340 or  Chauve-chat farceur, Panthère, Kevinathan biblique, Bulot maudit
6° 30'  Phype   390? or     Poisillon, Galupiote, Renard laineux, Homme lézard, Pygmé incrédule, Shaman-poussière, Sorcier de l'Aurore
6° -8'  Ile de l'Irithios   290 or  Araignée géante, Fulgor, Apprenti, Araignée géante, Frisquette, Pygmé incrédule, Frisquette, Tape-taupe
6° -14'     Ile de l'Irande     224 or  Blob puissant, Scarabée géant, Renard laineux, Seigneur cobra, Seigneur cobra, Frisquette
7° 17'  Ile de Pax  280 or  Tape-taupe, Armanite puante, Âme en peine, Bulot maudit, Chauve-chat farceur, Bulot maudit
8° 4'   Ile de Magors   180 or  Picounet, Guêpe géante, Panthère, Fulgor
8° 4'   Ile de Harsis   260 or  Tape-Taupe, Diablotin sournois, Raide Momie, Chauve-chat farceur
9° 3'   Autosis     296 or  Âme en peine, Scarabée géant, Sorcier ??? , Fulgor
9° 9'   Ile Menos   480 or  Mouskito family, Chauve-chat farceur, Picounet, Homme lézard, Galupiote, Scarabée géant, Scarabée géant, Diablotin sournois, Sorcier du crépuscule
9° -1'  Dokien  114 or  Seigneur cobra, Squelette vengeur, Blob puissant
9° -4'  Ile Balème  500 or  Fulgor, Shaman-poussière, Sado-gorgogne, Picounet, Âme en peine, Rototo, Shaman-poussière
9° -6'  Ile Thaxie  106 or  Panthère, Frisquette, Blob féroce, Araignée géante
9° -10'     Récif aux Galukon   260 or  Chauve-chat farceur, Mouskito family, Armanite puante, Sado-gorgogne
10° 0'  Ile de l'Ilonie     120 or  Squelette vengeur, Galupiote, Serpent venimeux, Araignée géante
10° -8'     Ariti   280 or  Sorcier de l'aurore, Diablotin sournois, Galupiote, Sado-gorgogne, Frisquette
10° -14'    Eriné   240 or  Homme lézard, Armanite puante, Sado-gorgogne, Serpent venimeux, Araignée géante, Foudrine
10° -16'    Ile d'Iroulès   190 or  Sorcier du crépuscule, Mouskito family, Pygmé incrédule, Bulot maudit
11° -16'    Ile du Lesespès     460 or  Golem d'argile, Shaman poussière, Serpent venimeux, Fulgor, Fulgor, Rototo, Armanite puante
11° -13'    Tha     200 or  Foudrine, Squelette vengeur, Sado-gorgogne, Serpent venimeux, Pygmé incrédule, Pygmé incrédule
11° -6'     Ilot du Karée   156 or  Blob féroce, Armanite puante, Panthère, Galupiote
11° 1'  Ile de l'Autoligma  334 or  Seigneur cobra, Raide Momie, Squelette vengeur, Bulot maudit, Tape-taupe, Renard laineux, Blob puissant, Poisillon
11° 6'  Rélunes     110 or  Foudrine, Picounet, Araignée géante, Frisquette
12° 3'  Ilot de l'Enos  120 or  Rototo, Diablotin, Serpent venimeux
12° 4'  Ile aux Dokien  330 or  Mouskito family, Scarabée géant, Seigneur cobra, Foudrine, Ame en peine, Pygmé incrédule, Picounet, Renard laineux, Serpent venimeux
13° -3'     Ile d'Iraktien  210 or  Galupiote, Chauve-chat farceur, Galupiote, Blob puissant, Blob féroce
14° 0'  Ile de Menors   340? or     Homme lézard, Ame en peine, Raide momie, Mouskito family, Renard laineux, Bulot maudit, Rototo
14° -7'     Autolinie   520? or     Diablotin sournois, Tape-taupe, Seigneur cobra, Minotaure, Shaman-poussière, Serpent venimeux, Apprenti, Serpent venimeux, Rototo
15° 1'  Ile des Tritons     100 or  Foudrine, Pygmé incrédule, Serpent venimeux, Frisquette
15° 2'  Ile des Tritons     100 or  Foudrine, Pygmé incrédule, Serpent venimeux, Frisquette
15° -1'     Ménique     116 or  Renard laineux, Blob féroce, Scarabée géant, Squelette vengeur
15° -1'     Dokithien   320 or  Frisquette, Seigneur cobra, Frisquette, Guêpe géante, Squelette vengeur, Foudrine, Seigneur cobra, Bulot maudit
15° -14'    Ile d'Irique    430 or  Pygmé incrédule, Raide momie, Sado-gorgogne, Apprenti, Mouskito family, Poisillon, Galupiote, Golem d'argile
17° 0'  Dokaktos    340 or  Shaman-poussière, Frisquette, Mouskito family, Foudrine, Frisquette, Raide momie
17° -2'     Gaxos   430 or  Frisquette, Homme-lézard, Shaman-poussière, Poisillon, Apprenti, Golem d'argile, Mouskito family
18° -3'     Ilot du Lesors  480? or     Sorcier de l'aurore, Mouskito family, Squelette vengeur, Golem d'argile, Apprenti, Apprenti, Fulgor, Chauve-chat farceur
Coordonnées négatives   Nom de l'ile    Gain en or  Liste des ennemis
-2° 3'  Ile de Magoulos     110 or  Ame en peine, Scarabée géant, Blob féroce, Blob puissant
-2° 3'  Miniti  40 or   Araignée géante, Araignée géante
-2° 4'  Kareskone   300 or  Minotaure, Guêpe géante, Rototo, Sorcier de l'Aurore
-2° -13'    Ile des Orion   298 or  Frisquette, Apprenti, Blob puissant, Mouskito family, Âme en peine, Blob puissant, Picounet, Âme en peine, Araignée géante
-2° -15'    Ile aux Kylème  256 or  Raide momie, Golem d'argile, Blob féroce, Scarabée géant, Picounet
-3° 5'  Ilot Ekon   110 or  Picounet, Âme en peine, Pygmé incrédule
-3° 13'     Ile Harkiro     80 or   Araignée géante, Renard laineux, Picounet
-3° 17'     Ile de Kari     100 or  Rototo, Poisillon
-3° 30'     Dokakon     230 or  Frisquette, Golem d'argile, Foudrine, Scarabée géant, Armanite Puante
-3° -6' Elusyne     170 or  Sorcier du crépuscule, Squelette vengeur, Serpent venimeux, Frisquette
-3° -11'    Ile des Ikie    290 or  Pygmé incrédule, Seigneur cobra, Raide Momie, Seigneur cobra
-4° -1'     Arantée     154 or  Apprenti, Picounet, Araignée, Scarabée, Blob puissant
-4° -8'     Ile Aralmi  370 or  Sorcier de l'aurore, Fulgor, Squelette vengeur, Renard laineux, Homme lézard, Pygmé incrédule, Guêpe géante, Araignée géante
-4° -8'     Ilot du Harxos  210 or  Tape-taupe, Homme lézard, Apprenti, Panthère, Blob
-4° -11'    Ile Tati    294 or  Frisquette, Âme en peine, Foudrine, Blob puissant, Seigneur cobra, Armanite puante, Renard laineux, Bulot maudit, Frisquette
-4° 12'     Ile de Dokalmiti    140 or  Apprenti, Homme lézard, Poisillon
-4° 23'     Ile de Magaxone     300 or  Homme lézard, Seigneur Cobra, Guêpe géante, Galupiote, Foudrine, Renard laineux, Renard laineux, Araignée Géante
-5° 5'  Ile aux Epaves  40 or   Picounet
-5° 12'     Ekiti   310 or  Fulgor, Shaman-poussière, Seigneur cobra, Pygmé incrédule, Scarabée géant
-6° 3'  Autofi  120 or  Galupiote, Squelette vengeur, Squelette vengeur
-7° 3'  Dokalmon    200 or  Diablotin sournois, Diablotin sournois, Picounet, Scarabée géant, Ame en peine, Araignée géante, Foudrine
-7° 6'  Orakas  440 or  Squelette vengeur, Fulgor, Chauve-chat farceur, Armanite puante, Scarabée géant, Chauve-chat farceur, Golem d'argile
-7° 12'     Iripsios    110 or  Scarabée géant, Blob, Araignée géante, Araignée géante, Serpent venimeux
-7° 12'     Epe     390 or  Ame en peine, Rototo, Fulgor, Rototo, Frisquette, Frisquette, Picounet, Diablotin sournois, Frisquette
-7° 13'     Ile Kareskaos   90 or   Serpent venimeux, Frisquette, Squelette vengeur
-7° 19'     Rékon   180 or  Panthère, Diablotin sournois, Apprenti, Serpent venimeux, Bulot maudit, Bulot maudit
-7° 28'     Autoti  300 or  A compléter/corriger : Ame en peine, Poisillon, Sado-gorgogne??, ??, Seigneur Cobra, Pygmé incrédule, Bulot Maudit, Bulot Maudit
-7° -4'     Ile Hyti    290 or  Seigneur Cobra, Mouskito Family, Ame en peine, Bulot maudit, Squelette vengeur, Frisquette
-7° -9'     Ile Autolème    180 or  Panthère, Homme lézard, Diablotin sournois, Poisillon
-7° -23'    Ile du Sarax    430 or  Poisillon, Golem d'argile, Frisquette, Shaman-poussière, Panthère, Poisillon, Golem d'argile
-8° -1'     Ile de Karithien    66 or   Frisquette, Serpent venimeux, Blob Féroce
-8° 6'  Pelaktème   150 or  Fulgor, Guêpe géante, Pygmé incrédule
-8° -6'     Arion   194 or  Squelette vengeur, Picounet, Raide momie, Blob puissant, Araignée géante
-8° -9'     Ile Harluxos    240 or  Shaman-poussière, Guêpe géante, Scarabée géant, Serpent venimeux
-8° -12'    Ilot de Harhélème   176 or  Shaman-poussière, Âme en peine, Blob féroce
-9° 0'  Ile de Minipsas     56 or   Squelette vengeur, Blob féroce
-9° -1'     Ile du Saraxas  190 or  Sorcier du crépuscule, Raide momie, Frisquette
-9° 7'  Ile Saralmique  120 or  Armanite puante, Renard laineux, Renard laineux, Bulot maudit
-9° 13'     Harro   330 or  Frisquette, Sorcier de l'Aurore, Panthère, Seigneur Cobra, Panthère, Foudrine, Galupiote, Foudrine
-9° 17'     Ile de Hyrixos  304 or  Mouskito Family, Rototo, Blob Puissant?, Panthère, Diablotin sournois, Diablotin sournois, Poisillon, Blob
-9° -13'    Ile Autoro  250 or  Sado-gorgogne, Picounet, Rototo, Serpent venimeux, Apprenti, Pygmé incrédule
-9° -13'    Ile Iloné   290 or  Diablotin sournois, Homme lézard, Fulgor, Homme lézard, Pygmé incrédule, Âme en peine
-10° 9'     Bakimaque   114 or  Sado-gorgogne, Blob puissant, Squelette vengeur
-10° 12'    Harro   330 or  Frisquette, Sorcier de l'Aurore, Panthère, Seigneur Cobra, Panthère, Foudrine, Galupiote, Foudrine
-10° 11'    Ile du Magique  100 or  Poisillon, Serpent venimeux, Galupiote
-10° 18'    Ile aux Harphie     270 or  Blob, Raide Momie, Diablotin sournois, Homme lézard, Poisillon, Poisillon
-12° -3'    Ile aux Thors   236 or  Sado-gorgogne, Mouskito family, Guêpe géante, Ame en peine, Blob féroce
-12° 6'     Phypoulème  160 or  Rototo, Scarabée Géant, Scarabée Géant, Bulot Maudit
-12° 11'    Répoulos    180 or  Seigneur Cobra, Guêpe géante, Sado-gorgogne
-12° 12'    Autohélogos     130 or  Tape-Taupe, Tape-Taupe, Blob
-13° -1'    Ile aux Phykiti     270 or  Âme en peine, Galupiote, Sado-gorgogne, Diablotin sournois, Renard laineux, Squelette vengeur, Frisquette
-13° 4'     Ile Minios  160 or  Frisquette, Frisquette, Picounet, Homme lézard
-13° 7'     Magix   320 or  Tape-Taupe, Mouskito family, Armanite Puante, Poisillon, Chauve-chat farceur, Araignée géante
-13° 18'    Ile aux Dokas   400 or  Sado-gorgogne, Ame en peine, Diablotin sournois, Fulgor, Panthère, Galupiote, Galupiote, Raide Momie
-13° 20'    Autodeutené     240 or  Apprenti, Raide Momie, Diablotin sournois, Ame en peine, Diablotin sournois
-14° -3'    Ile Pelande     220 or  Armanite puante, Homme lézard, Picounet, Renard laineux, Panthère
-14° 20'    Ganas   270 or  Pygmé incrédule, Raide Momie, Seigneur Cobra, Bulot Maudit, Diablotin sournois, Serpent venimeux, Araignée Géante
-15° 1'     Ile de Zikipson     116 or  Galupiote, Serpent venimeux, Scarabée géant, Blob féroce
-15° 6'     Ile de Sarakème     220 or  Raide momie, Guêpe géante, Armanite puante, Renard laineux
-15° 11'    Ile du Thatomas     320 or  Scarabée géant, Sorcier de l'aurore, Scarabée géant, Squelette vengeur, Scarabée géant, Diablotin sournois, Panthère
-15° 13'    Ile de l'Iraka  420 or  Tape-Taupe, Sorcier du Crépuscule, Galupiote, Sorcier de l'Aurore, Sorcier de l'Aurore, Poisillon, Scarabée géant
-17° 11'    Ile Désertique  270 or  Raide Momie, Chauve-chat farceur, Diablotin sournois, Frisquette, Renard laineux, Araignée Géante
-17° 12'    Ile de l'Orie   296 or  Blob féroce, Diablotin sournois, Apprenti, Squelette vengeur, Armanite puante, Apprenti, Araignée géante, Renard laineux
-17° 16'    Phyron  200 or  Panthère, Diablotin sournois, Pygmé incrédule, Apprenti, Pygmé incrédule, Foudrine
-20° 15'    Ile Pelideasa   200 or  Kevinathan biblique
"""

# --- bâtiments ---

# ---- Temples ----
# L'éveil du personnage augmente. Il gagne une ligne à sa grille de runes. Emplacement:

TEMPLES = """
2°0'

3°10'

4°-2'

8°-2'

3°-17'

6°-14'

11°-14'

8°-21'

-19°8'

-19°22'

-3°-8'

-2°-13'

-15°-22'
"""

# ---- Bibliothèques ----
# La connaissance du personnage augmente. Il gagne une colonne à sa grille de runes. Emplacement:

LIBRARIES = """
1°4'

0°-8'

3°-17'

7°-10'

24°-1'

-7°7'

-4°19'

-5°28'

-17°24'
"""

# ---- Fontaines ----
# Régénère vos runes et vos 10 combats du jour gratuitement. Emplacement :

FOUNTAINS = """
11°5'

15°-1'

24°-2'

-1°4'

-2°4'

-7°3'

-12°4'

-4°12'

-12°12'

-8°-14'

-18°-12'
"""

# ---- Distillateur de potions ----
# Permet de remplir vos potions vides si vous en possédez.

POTION_DISTILLERS = """
9°0'

9°8'

11°4'

22°1'

8°24'

8°-2'

24°-1'

24°-2'

3°-20'

-1°3'

-3°7'

-2°9'

-6°9'

-9°12'

-4°19'

-8°14'

-12°1'

-14°1'

-5°28'

-7°27'

-14°-9'

-2°8'

-8°0'

-13°8'

-2°-16'

-21°-15'
"""

# ---- Augmentation de sac de nourriture ----
# Permet d'agrandir son sac de plus de 5 nourriture maximal. Emplacement :

FOOD_BAGS = """
2°30'

8°11'

8°14'

8°24'

-7°7'

-6°3'

-8°6'

-9°7'

-9°9'

-18°11'

-18°6'

-13°18'

-8°12'

-13°7'

-4°19'

-3°27'

14°-3'

11°-6'

11°-16'

17°-14'

2°-25'

5°-21'

5°-22'

3°-17'

15°-2'

18°-3'

-5°-3'

-15°-3'

-11°-16'

-5°-12'

-21°-15'
"""

# ---- Auberges ----
# Auberge: Dormir à l'auberge vous permet un regain de vos runes et de vos dix combats contre des pièces d'or. Le prix d'une auberge dépend du nombre de héros dans l'équipe (Avoir deux personnages double le prix, en avoir trois le triple) . Les prix indiqués ci-dessous sont ceux pour un seul personnage. Voir aussi la Carte des Auberges, recensant les auberges découvertes. Emplacement:

INNS = """
0°9' - 65 pièces d'or

4°3' - 55 pièces d'or

0°6' - 65 pièces d'or

5°0' - 65 pièces d'or

5°6' -

9°9' - 50 pièces d'or

8°14' - 65 pièces d'or

11°5' - 40 pièces d'or

12°4' - 50 pièces d'or

16°5' - 65 pièces d'or

1°19' -

8°24' -

22°1' - 45 pièces d'or

5°-7' - 55 pièces d'or

1°-12' - 65 pièces d'or

6°-8' - 40 pièces d'or

10°-14' - 50 pièces d'or

11°-16' -

14°-15' - 50 pièces d'or

5°-21' -

6°-19' - 60 pièces d'or

8°-15' -

9°-5' - 55 pièces d'or

8°-15' - 45 pièces d'or

20°16 - 45 pièces d'or

21°-2' - 60 pièces d'or

23°-1' - 65 pièces d'or

-3°5' - 65 pièces d'or

-6°3' - 55 pièces d'or

-9°3' - 65 pièces d'or

-12°7' - 50 pièces d'or

-4°12' - 40 pièces d'or

-4°18' - 40 Pièces d'or

-5°12' -

-13°20' - 40 pièces d'or

-3°22' - 60 pièces d'or

-4°24' - 40 pièces d'or

-20°11' - 55 pièces d'or

-20°13' - 65 pièces d'or

-22°22' - 65 pièces d'or

-1°-10' - 55 pièces d'or

-9°-1' - 40 pièces d'or

-8°-1' - 45 pièces d'or

-3°5' -

-7°-9'

-15°-3' - 40 pièces d'or

-18°-4' -

-13°-12' - 40 pièces d'or

-10°-20' - 65 pièces d'or

-2°-16' - 65 pièces d'or
"""

# --- Autels ---

ALTARS = """
Arès :

    9° 0' : Orors (mer Orès)
    6° 30' : Phype (mer Oranta)
    5° -18' : Ile des Phyro (mer Arion)
    -18° 7' : Ile aux Ilokisis (mer Speron)
    -19° -22' : Saraktors (mer Zikandros)

Déméter :

    23° -4' : Ile Ekroné (mer Hyrimaque)
    18° -23' : Autopapasis (Mer Galugion)
    -8° 14' : Ile du Thaos (mer Arespax)
    -26° 11' : Zikaghos (mer Autosyne)
    -4° -10' : Ile Tati (mer Arix)

Hermès :

    23° 4' : Ile Harpouphie (mer Bapoulos)
    -4° 18' : Kyfi (mer Telekrophie)
    -14° 6' : Autophie (mer Iko)
    -20° 15' : Ile Pelideasa (mer Basyne)
    -14° -7': Ile Tané (mer Magaos)

Atlas :

    15° 15' : Ile Telelilème (mer Répoufi)
    2° -10' : Ile Sarix (mer Aroulique)
    -17° 1' : Ile Arone (mer Phype)
    -17° 20' : Ile du Saros (Archipel Sombre)
    -27° -5' : Récif aux Thotisios (mer Irespax)

Poséidon :

    1° 31' : Ile des Epouné (mer Harkropoulos)
    5° -14' : Takroron (mer Ilologos)
    -9° 22' : Araki (mer Zikax)
    -2° -15' : Ile aux Kylème (mer Zikeidos)
    -5° -23' : Tagma (mer Orax)
"""
