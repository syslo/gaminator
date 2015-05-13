# -*- coding: utf-8 -*-


class _ThingType(type):

    _classes = dict()

    def __init__(cls, name, bases, dct):
        super(_ThingType, cls).__init__(name, bases, dct)
        _ThingType._classes[name] = cls


class PTI__Thing(object):

    __metaclass__ = _ThingType

    def __init__(self, *args, **kwargs):
        self._world = None
        self.PTI_thing__setup(*args, **kwargs)

    @property
    def PTI_thing__world(self):
        return self._world

    @PTI_thing__world.setter
    def PTI_thing__world(self, value):
        if self._world is not None:
            self._world._disconnect_thing(self)
        if value is not None:
            value._connect_thing(self)
        self._world = value

    @PTI_thing__world.deleter
    def PTI_thing__world(self):
        if self._world is not None:
            self._world._disconnect_thing(self)
        self._world = None

    def PTI_thing__setup(self, *args, **kwargs):
        pass

    def PTI_thing__step(self):
        pass
