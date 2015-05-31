# -*- coding: utf-8 -*-

import os
from setuptools import setup

from localization.tool import localize

LOCALES = [
    ('default.py', 'gaminator'),
]

PACKAGES = [
    '%s',
    '%s.starter',
]

DESCRIPTION = """A library for easy and fast development of simple games.
For educational purposes.
"""


ROOT = os.path.dirname(__file__)

for trans_file, dest_root in LOCALES:
    trans_file = os.path.join(ROOT, 'localization', 'data', trans_file)
    dest_root = os.path.join(ROOT, dest_root)
    src_root = os.path.join(ROOT, 'gaminator-src')
    localize(src_root, dest_root, trans_file)

def get_packages():
    for _, dest_root in LOCALES:
        for package in PACKAGES:
            yield package % dest_root

setup(
    name="gaminator",
    version="0.0.4",
    author=u"Marián Horňák",
    author_email="marian.sysel.hornak@gmail.com",
    description=DESCRIPTION,
    license="MIT",
    keywords=["education", "game"],
    url="https://github.com/syslo/gaminator",
    download_url="https://github.com/syslo/gaminator/tarball/v0.0.4",
    packages=list(get_packages()),
    classifiers=[
        "Development Status :: 4 - Beta",
    ],
)
