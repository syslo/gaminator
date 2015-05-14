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

        self.PTI__width = 600
        self.PTI__height = 400

    @property
    def PTI_world__background(self):
        return self._picture

    def _repaint(self, canvas):
        super(PTI__World, self)._repaint(canvas)
        for thing in self._things:
            thing._repaint(canvas)

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
        self.PTI_thing__step()
        for thing in self._things:
            thing.PTI_thing__step()
