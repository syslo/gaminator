# -*- coding: utf-8 -*-


from collections import defaultdict

from .thing import PTI__Thing


class PTI__World(PTI__Thing):

    def __init__(self, *args, **kwargs):
        self._things_by_class = defaultdict(set)
        self._things = set()
        super(PTI__World, self).__init__(*args, **kwargs)

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
        for thing in self._things:
            thing.PTI_thing__step()
