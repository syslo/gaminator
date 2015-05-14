# -*- coding: utf-8 -*-


from collections import defaultdict


class _ThingType(type):

    _classes = dict()

    def __init__(cls, name, bases, dct):
        super(_ThingType, cls).__init__(name, bases, dct)
        cls._gaminator_events = defaultdict(list)
        _ThingType._classes[name] = cls
        for k in dct:
            cls._new_attribute(k, dct[k])

    def _new_attribute(cls, key, value):
        if hasattr(value, '__call__') and hasattr(value, '_gaminator_events'):
            for event in value._gaminator_events:
                cls._gaminator_events[event].append(key)
            del value._gaminator_events
