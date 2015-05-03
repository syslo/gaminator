# -*- coding: utf-8 -*-

import codecs
import os
import re

from collections import defaultdict


PATTERN = re.compile(
    r"PTI(?P<group>(_[a-zA-Z0-9]+)*)?__(?P<name>[_a-zA-Z0-9]*)"
)


def localize(src_root, dest_root, translation_file):

    T = defaultdict(dict)

    with open(translation_file, "rb") as f:
        exec(f.read(), {"T": T})

    def replacer(match):
        group, name = match.group("group")[1:], match.group("name")
        return T.get(group, {}).get(name, name)

    for src_dir, dirnames, filenames in os.walk(src_root):
        dest_dir = os.path.join(dest_root, os.path.relpath(src_dir, src_root))
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for filename in filenames:
            src_filename = os.path.join(src_dir, filename)
            print("processing "+src_filename)
            dest_filename = os.path.join(dest_dir, filename)
            with codecs.open(src_filename, "r", "utf-8") as src_file:
                with codecs.open(dest_filename, "w", "utf-8") as dest_file:
                    dest_file.write(PATTERN.sub(replacer, src_file.read()))


def occurences(src_root):
    result = defaultdict(lambda: defaultdict(list))

    for src_dir, dirnames, filenames in os.walk(src_root):
        for filename in filenames:
            src_filename = os.path.join(src_dir, filename)
            line_number = 0
            with codecs.open(src_filename, "r", "utf-8") as src_file:
                for line in src_file:
                    for m in PATTERN.finditer(line):
                        group, name = m.group("group")[1:], m.group("name")
                        result[group][name].append((
                            os.path.relpath(src_filename, src_root),
                            line_number
                        ))
                    line_number += 1

    return result


def generate(src_root, translation_file):
    data = occurences(src_root)

    with codecs.open(translation_file, "w", "utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n\n")
        f.write("'''This is Gaminator translation file.'''\n\n")

        for group in sorted(data.keys()):
            for name in sorted(data[group].keys()):
                for occurence in data[group][name]:
                    f.write("# %s:%d\n" % occurence)
                f.write("T['%s']['%s'] = ''\n\n" % (group, name))
