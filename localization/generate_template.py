# -*- coding: utf-8 -*-

import os

from tool import generate

root = os.path.join(os.path.dirname(__file__), '..')
src_root = os.path.join(root, 'gaminator-src')
translation_file = os.path.join(root, 'localization', 'data', 'template.py')

generate(src_root, translation_file)
