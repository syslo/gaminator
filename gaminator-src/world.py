# -*- coding: utf-8 -*-


from collections import defaultdict
from operator import attrgetter
import pygame
import time

from .picture_thing import PTI__PictureThing
from .picture import PTI__Picture
from .events import _EventEmitterMixim
from .collisions import _CollisionEmitterMixim


class PTI__World(
    PTI__PictureThing, _EventEmitterMixim, _CollisionEmitterMixim
):

    def __init__(self, *args, **kwargs):
        self._start_time = time.time()
        self._time = 0
        self._ticks = 0

        self._things_by_class = defaultdict(set)
        self._things = set()

        self._things_by_z = None
        self._recalculate_z = True

        PTI__PictureThing.__init__(self, *args, **kwargs)
        _EventEmitterMixim.__init__(self)

        self.PTI__x_align = 0
        self.PTI__y_align = 0

        self.PTI__picture = PTI__Picture(600, 400)

    @property
    def PTI_world__ticks(self):
        return self._ticks

    @property
    def PTI_world__time(self):
        return self._time

    def _repaint(self, canvas):
        if self._recalculate_z:
            self._things_by_z = list(
                sorted(self._things, key=attrgetter('_z'))
            )
            self._recalculate_z = False
        super(PTI__World, self)._repaint(canvas)
        for thing in self._things_by_z:
            thing._repaint(canvas)

    def _connect_thing(self, thing):
        self._recalculate_z = True
        self._things.add(thing)
        for cls in thing.__class__.__mro__:
            self._things_by_class[cls].add(thing)

    def _disconnect_thing(self, thing):
        self._recalculate_z = True
        self._things.remove(thing)
        for cls in thing.__class__.__mro__:
            self._things_by_class[cls].remove(thing)

    def _clear_things(self, thing):
        self._recalculate_z = True
        for thing in self._things:
            thing._world = None
        self._things.clear()
        for cls in self._things_by_class:
            self._things_by_class[cls].clear()

    def _activate(self):
        self._start_time = time.time() - self._time

    def _deactivate(self):
        self._time = time.time() - self._start_time

    def _tick(self):
        self._ticks += 1
        self._time = time.time() - self._start_time
        self.PTI_thing__step()
        for thing in self._things:
            thing.PTI_thing__step()
        self._tick_collisions()
        self._tick_events()
