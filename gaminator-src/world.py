# -*- coding: utf-8 -*-


from collections import defaultdict
import pygame

from .thing import PTI__Thing
from .events import _EventEmitterMixim


class PTI__World(PTI__Thing, _EventEmitterMixim):

    def __init__(self, *args, **kwargs):
        self._things_by_class = defaultdict(set)
        self._things = set()

        PTI__Thing.__init__(self, *args, **kwargs)
        _EventEmitterMixim.__init__(self)

    def _connect_thing(self, thing):
        self._things.add(thing)
        for cls in thing.__class__.__mro__:
            self._things_by_class[cls].add(thing)

    def _disconnect_thing(self, thing):
        self._things.remove(thing)
        for cls in thing.__class__.__mro__:
            self._things_by_class[cls].remove(thing)

    def _clear_things(self, thing):
        for thing in self._things:
            thing._world = None
        self._things.clear()
        for cls in self._things_by_class:
            self._things_by_class[cls].clear()

    def _activate(self):
        pass

    def _deactivate(self):
        pass

    def _tick(self):
        self._tick_events()
        for thing in self._things:
            thing.PTI_thing__step()
