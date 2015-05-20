#  -*- coding: utf-8 -*-


from .thing_type import _ThingType


def PTI_decorator__collision(cls):
    def decorator(f):
        if not hasattr(f, "_gaminator_collisions"):
            f._gaminator_collisions = []
        f._gaminator_collisions.append(cls)
        return f
    return decorator


class _CollisionEmitterMixim(object):

    def _tick_collisions(self):
        calls = []
        for cls in self._things_by_class:
            if isinstance(cls, _ThingType):
                for clsi in cls._gaminator_collisions:
                    cls2 = _ThingType._get_class(clsi)
                    for fname in cls._gaminator_collisions[clsi]:
                        for thing in self._things_by_class[cls]:
                            if cls2 in self._things_by_class:
                                for thing2 in self._things_by_class[cls2]:
                                    if thing.PTI_thing__collides(thing2):
                                        calls.append(
                                            (getattr(thing, fname), thing2)
                                        )
        for f, thing2 in calls:
            f(thing2)
