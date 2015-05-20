# -*- coding: utf-8 -*-


from collections import defaultdict
from operator import attrgetter
import pygame
import time

from .thing import PTI__Thing
from .picture import PTI__Picture
from .canvas import PTI__Canvas
from .window import PTI__window
from .events import _EventEmitterMixim
from .collisions import _CollisionEmitterMixim
from .exceptions import PTI_exception__TopWorldSubworlding
from .exceptions import PTI_exception__SelfSubworlding


class PTI__World(PTI__Thing, _EventEmitterMixim, _CollisionEmitterMixim):

    def __init__(self, **kwargs):
        self._start_time = time.time()
        self._time = 0
        self._ticks = 0

        self._things_by_class = defaultdict(set)
        self._things = set()

        self._things_by_z = None
        self._recalculate_z = True

        _EventEmitterMixim.__init__(self)
        PTI__Thing.__init__(self, **kwargs)

        self.PTI__x_align = 0
        self.PTI__y_align = 0

        self.PTI__background = PTI__Picture(600, 400)

    @property
    def PTI__width(self):
        if self._world == self:
            # @HACK: Top worlds are kids of themselves
            return PTI__window.PTI__width
        return self._width

    @PTI__width.setter
    def PTI__width(self, PTI__value):
        if self._world == self:
            # @HACK: Top worlds are kids of themselves
            PTI__window.PTI__width = PTI__value
        else:
            self._width = PTI__value

    @property
    def PTI__height(self):
        if self._world == self:
            # @HACK: Top worlds are kids of themselves
            return PTI__window.PTI__height
        return self._height

    @PTI__height.setter
    def PTI__height(self, PTI__value):
        if self._world == self:
            # @HACK: Top worlds are kids of themselves
            PTI__window.PTI__height = PTI__value
        else:
            self._height = PTI__value

    @property
    def PTI__background(self):
        return self._picture

    @PTI__background.setter
    def PTI__background(self, PTI__picture):
        self._picture = PTI__picture
        self._canvas = PTI__Canvas(self._picture)

    @property
    def PTI__canvas(self):
        return self._canvas

    @property
    def PTI_world__ticks(self):
        return self._ticks

    @property
    def PTI_world__time(self):
        return self._time

    @property
    def PTI_world__things(self):
        return list(self._things)

    @property
    def PTI_world__subworlds(self):
        return list(self._things_by_class[PTI__World])

    def _repaint(self, canvas):
        my_picture = PTI__Picture(self.PTI__width, self.PTI__height)
        my_canvas = PTI__Canvas(my_picture)

        my_canvas.PTI_draw__picture(
            self._picture,
            (0, 0),
        )

        if self._recalculate_z:
            self._things_by_z = list(
                sorted(self._things, key=lambda x: (x._z, x.id))
            )
            self._recalculate_z = False
        for thing in self._things_by_z:
            thing._repaint(my_canvas)

        canvas.PTI_draw__picture(
            my_picture,
            (self.PTI_thing__border_left, self.PTI_thing__border_up),
        )

    def _connect_thing(self, thing):
        if thing == self:
            # @HACK: Top worlds are kids of themselves
            raise PTI_exception__SelfSubworlding()
        self._recalculate_z = True
        self._things.add(thing)
        for cls in thing.__class__.__mro__:
            self._things_by_class[cls].add(thing)

    def _disconnect_thing(self, thing):
        if thing == self:
            # @HACK: Top worlds are kids of themselves
            raise PTI_exception__TopWorldSubworlding()
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

        if self._world == self:
            self.PTI_thing__step()
        for thing in self._things:
            thing.PTI_thing__step()

        self._tick_collisions()
        self._tick_events()

        for subworld in self._things_by_class[PTI__World]:
            subworld._tick()
