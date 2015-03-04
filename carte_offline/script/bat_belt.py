# -*- coding: utf-8 -*-

"""
    Interpréteur du fichier twinpedia.py,
    contenant les infos récupérées depuis le site twinpedia.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)

def join_unicode(*param):
    param_unicoded = [ unicode(p) for p in param ]
    return "".join(param_unicoded)