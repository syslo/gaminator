#  -*- coding: utf-8 -*-


import pygame
from threading import Condition
import traceback

from .interactive import interact


class _Gaminator:

    def __init__(self):
        self._end = False
        self._interactive = False
        self._lock = Condition()
        self._screen = None
        self._worlds = []
        self._world_changes = []
        self.FPS = 60
        pass

    @property
    def PTI_gaminator__world(self):
        return self._worlds[-1]

    def PTI_gaminator__end(self):
        self._end = True

    def PTI_gaminator__push_world(self, PTI__world):
        self._world_changes.append((1, PTI__world))

    def PTI_gaminator__swap_world(self, PTI__world):
        self._world_changes.append((0, PTI__world))

    def PTI_gaminator__pop_world(self):
        self._world_changes.append((-1, None))

    def PTI_gaminator__start(self, PTI__world, PTI__interactive=False):
        self._interactive = PTI__interactive
        self.PTI_gaminator__push_world(PTI__world)
        self._loop()

    def _loop(self):

        if self._interactive:
            console = interact(self)

        pygame.init()

        pygame.display.set_mode((600, 400))
        self._screen = pygame.display.get_surface()

        clock = pygame.time.Clock()

        try:
            with self._lock:
                while not self._end:

                    self._handle_world_changes()
                    if not self._worlds:
                        break

                    if self._interactive:
                        self._lock.wait(0)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.PTI_gaminator__end()

                    self._screen.fill((255, 255, 255, 0))

                    self._worlds[-1]._tick()

                    pygame.display.flip()
                    clock.tick(self.FPS)
        except:
            traceback.print_exc()
        finally:
            pygame.quit()

    def _handle_world_changes(self):
        for action, world in self._world_changes:
            if self._worlds:
                self._worlds[-1]._deactivate()
            if action in [-1, 0] and self._worlds:
                self._worlds.pop().znicVsetko()
            if action in [0, 1]:
                self._worlds.append(world)
            if self._worlds:
                self._worlds[-1]._activate()
        self._world_changes = []


gaminator = _Gaminator()
