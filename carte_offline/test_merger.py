# -*- coding: utf-8 -*-

"""
    Récupère les données brutes provenant de différentes sources,
    et les rassemble, en détectant les incohérences (plus ou moins).
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import logging
info = logging.info

import my_scripts.data_merger

seas = my_scripts.data_merger.build_data()
for sea in seas:
    info(unicode(sea))
    info("-" * 10)


