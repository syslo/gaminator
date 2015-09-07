#  -*- coding: utf-8 -*-


import pygame
from threading import Condition
import traceback

from .interactive import interact
from .picture import PTI__Picture
from .canvas import PTI__Canvas
from .window import PTI__window


class _Game:

    def __init__(self):
        self._end = False
        self._interactive = False
        self._lock = Condition()
        self._screen = None
        self._worlds = []
        self._world_changes = []
        self.tps = 60
        self.PTI__autoescape = True
        pass

    @property
    def PTI_game__world(self):
        return self._worlds[-1]

    def PTI_game__end(self):
        self._end = True

    def PTI_game__push_world(self, PTI__world):
        self._world_changes.append((1, PTI__world))

    def PTI_game__swap_world(self, PTI__world):
        self._world_changes.append((0, PTI__world))

    def PTI_game__pop_world(self):
        self._world_changes.append((-1, None))

    def PTI_game__start(self, PTI__world, PTI__interactive=False):
        self._interactive = PTI__interactive
        self.PTI_game__push_world(PTI__world)
        self._loop()

    def PTI_game__pressed(self, PTI__key):
        return self._pressed_keys[PTI__key]

    def _loop(self):

        if self._interactive:
            console = interact(self)

        pygame.init()

        PTI__window._apply_changes()
        self._screen = PTI__Picture(pygame.display.get_surface(), None)

        clock = pygame.time.Clock()

        try:
            with self._lock:
                while not self._end:

                    self._handle_world_changes()
                    if not self._worlds:
                        break

                    PTI__window._apply_changes()

                    if self._interactive:
                        self._lock.wait(0)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.PTI_game__end()
                        elif event.type == pygame.VIDEORESIZE:
                            PTI__window._height = event.h
                            PTI__window._width = event.w
                        elif event.type == pygame.KEYDOWN:
                            if (
                                self.PTI__autoescape and
                                event.key == pygame.K_ESCAPE
                            ):
                                self.PTI_game__end()

                            self._worlds[-1].PTI_invoker__event(
                                ("PTI__KEYDOWN", event.key), event.unicode
                            )
                            self._worlds[-1].PTI_invoker__event(
                                "PTI__KEYDOWN", event.key, event.unicode
                            )
                        elif event.type == pygame.KEYUP:
                            self._worlds[-1].PTI_invoker__event(
                                ("PTI__KEYUP", event.key)
                            )
                            self._worlds[-1].PTI_invoker__event(
                                "PTI__KEYUP", event.key
                            )

                    self._pressed_keys = pygame.key.get_pressed()

                    self._worlds[-1]._tick()

                    self._screen._surface.fill((255, 255, 255, 0))
                    self._worlds[-1]._repaint(PTI__Canvas(self._screen))

                    pygame.display.flip()
                    clock.tick(self.tps)
        except:
            traceback.print_exc()
        finally:
            pygame.quit()

    def _handle_world_changes(self):
        for action, world in self._world_changes:
            if self._worlds:
                self._worlds[-1]._deactivate()
            if action in [-1, 0] and self._worlds:
                w = self._worlds.pop()
                w._world = None  # @HACK: Topworlds are kids of themselves
            if action in [0, 1]:
                self._worlds.append(world)
                world.world = None  # Disconect world from its parent
                world._world = world  # @HACK: Topworlds are kids of themselves
            if self._worlds:
                self._worlds[-1]._activate()
        self._world_changes = []


PTI__game = _Game()
