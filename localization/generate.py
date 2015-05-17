# -*- coding: utf-8 -*-

import os
import sys

from tool import generate

if len(sys.argv) < 2:
    print('Using: %s <filename>' % sys.argv[0])
    exit(1)

root = os.path.join(os.path.dirname(__file__), '..')
src_root = os.path.join(root, 'gaminator-src')

generate(src_root, sys.argv[1])
