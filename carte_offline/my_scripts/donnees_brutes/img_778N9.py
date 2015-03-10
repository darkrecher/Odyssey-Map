# -*- coding: utf-8 -*-

"""
    Analyse manuelle de l'image 778N9.png.
    Carte des auberges, faite par 3l3ktr0
    Mentionnée sur le site de help-odyssey.
    http://muxxu.com/g/help-odyssey?page=37633
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)

LEECH_URL = "http://i.imgur.com/778N9.png"
LEECH_DATE = "2015-22-02"

# TODO : expliquer pourquoi on peut indiquer directement un nom d'île.

# TODO
# Île à indiquer explicitement là dedans, car elle incertaines.
# Harxos. 2/, 2/. au-dessus de :
# Aralmi. 2/, 2/
#
# Saraxas : w = 2/, h = 1/. au-dessus de :
# Minipsas : w = 2/, h = 2/

# s = sea
# i = islands
DATA = """

s -1 2/, -21 2/, 4 2/, 7
i 3 1/, -17 1/, 2/, 2/
i 2, -15, 2/, 2/

s 4 1/, -17, 3, 6 2/
i 6, -14, 1/, 1/
i 5, -14 2/, 1/, 1/

s -10, -17 2/, 4 2/, 5 1/
i -8 2/, -14 1/, 2/, 2/ ; W:incertain
i -8 1/, -12, 2/, 2/

s -17 1/, -15, 6 2/, 4 2/
i -14, -12, 1, 1 ; W:incertain

s -6 2/, -14 2/, 5, 4 1/
i -2, -13, 2/, 2/
i -2 1/, -12 2/, 2/, 2/
i -4 2/, -11 2/, 2/, 2/

s -1 2/, -14 2/, 4 2/, 3
i 1 2/, -13 1/, 2/, 1/
i 0 2/, -13 2/, 2/, 2/
i 1 2/, -13 2/, 1/, 2/ ; W:incertain ; I:Réro ; C:caché par un drapeau d'auberge, association arbitraire sinon mélangeage de pinceau
i 2, -12 1/, 1/, 1/
i 2 2/, -12 1/, 1/, 2/

s -10, -11, 4 2/, 4 1/
i -10 2/, -11 2/, 1, 1
i -7 1/, -10, 2/, 2/
i -8, -9 1/, 1, 1
i -7 1/, -9 1/, 1, 1

s -17 1/, -11 2/, 6 2/, 6
i -12, -10, 1, 1
i -15 1/, -9, 1, 1

s -1 2/, -11 2/, 4, 4 1/
i 1/, -10, 2/, 2/
i 2, -10 1/, 1/, 2/
i 1 1/, -9, 1/, 2/
i 2 2/, -9, 1/, 1/
i 1/, -8 2/, 2/, 2/

s 3 2/, -11 2/, 3, 4 1/
i 4 2/, -10 2/, 2/, 1/
i 4 1/, -9 1/, 2/, 2/
i 6, -9 2/, 1/, 2/ ; W:incertain
i 5, -8 2/, 2/, 1/ ; W:incertain

s 6 2/, -11 2/, 6 1/, 4 1/
i 10, -8, 2/, 2/ ; W:incertain ; C:ajout manuel car j'ai rien dans mon screenshot

s  -1 2/, -1 2/, 2 1/, 3
i  0, 0, 2/, 2/
i  1 1/, 1/, 1/, 1/
i  1, 2, 1/, 1/
i  0, 2, 1/, 1/
i  1, 1, 1/, 1/ ; I:Ganes
i  1 1/, 1, 1/, 1/ ; I:Tahépe

s  2, -1 2/, 4 2/, 3

s  -1, 2 2/, 4, 3

"""
