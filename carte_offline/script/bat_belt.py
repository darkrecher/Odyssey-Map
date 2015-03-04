# -*- coding: utf-8 -*-

"""
    Bat-belt. Tas de petites fonctions utiles partout.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)


def join_unicode(*param):
    param_unicoded = [ unicode(p) for p in param ]
    return "".join(param_unicoded)