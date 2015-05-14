#  -*- coding: utf-8 -*-


import heapq

from .thing_type import _ThingType


def PTI_decorator__event(name):
    def decorator(f):
        if not hasattr(f, "_gaminator_events"):
            f._gaminator_events = []
        f._gaminator_events.append(name)
        return f
    return decorator


class _EventEmitterMixim(object):

    def __init__(self):
        self._events_queue = []
        self._events_queue_waiting = []
        self._events_queue_id = 0

    def PTI_invoker__event(self, PTI__event, *args, **kwargs):
        self._events_queue_waiting.append(
            (0, PTI__event, self._events_queue_id, args, kwargs)
        )
        self._events_queue_id += 1

    def _tick_events(self):

        while self._events_queue:
            (_time, event, _id, args, kwargs) = self._events_queue[0]
            for cls in self._things_by_class:
                if isinstance(cls, _ThingType):
                    for fname in cls._gaminator_events[event]:
                        for thing in self._things_by_class[cls]:
                            getattr(thing, fname)(*args, **kwargs)

            heapq.heappop(self._events_queue)

        for event in self._events_queue_waiting:
            heapq.heappush(self._events_queue, event)

        self._events_queue_waiting = []
