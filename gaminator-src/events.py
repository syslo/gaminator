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
        self._events_queue_id = 0

    def PTI_invoker__timed_event(self, PTI__time, PTI__event, *args, **kwargs):
        heapq.heappush(self._events_queue, (
            self.time + PTI__time, self._events_queue_id,
            PTI__event, args, kwargs,
        ))

        self._events_queue_id += 1

        for subworld in self.PTI_world__subworlds:
            subworld.PTI_invoker__timed_event(
                PTI__time, PTI__event, *args, **kwargs
            )

    def PTI_invoker__event(self, PTI__event, *args, **kwargs):
        self.PTI_invoker__timed_event(0, PTI__event, *args, **kwargs)

    def _tick_events(self):

        heapq.heappush(self._events_queue, (
            self.time, -1, 'PTI__STEP', [], {},
        ))

        calls = []

        while self._events_queue and self._events_queue[0][0] <= self.time:
            (_time, _id, event, args, kwargs) = self._events_queue[0]
            for cls in self._things_by_class:
                if isinstance(cls, _ThingType):
                    for fname in cls._gaminator_events[event]:
                        for thing in self._things_by_class[cls]:
                            calls.append((getattr(thing, fname), args, kwargs))
            for cls in self.__class__.mro():
                if isinstance(cls, _ThingType):
                    for fname in cls._gaminator_events[event]:
                        calls.append((getattr(self, fname), args, kwargs))
            heapq.heappop(self._events_queue)

        for f, args, kwargs in calls:
            f(*args, **kwargs)
