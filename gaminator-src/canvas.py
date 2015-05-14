#  -*- coding: utf-8 -*-


from .constants import CONSTANTS
import pygame
import pygame.gfxdraw


class PTI__Canvas:

    def __init__(self, PTI__picture, PTI__color=None):
        self.PTI__color = PTI__color or CONSTANTS['PTI__BLACK']
        self._surface = PTI__picture._surface

    def PTI_draw__line(self, (x1, y1), (x2, y2)):
        pygame.gfxdraw.line(
            self._surface, round(x1), round(y1), round(x2), round(y2),
            self.PTI__color,
        )

    def PTI_draw__pixel(self, (x, y)):
        pygame.gfxdraw.pixel(
            self._surface, round(x), round(y), self.PTI__color,
        )

    def PTI_draw__rectangle(
        self, (x, y), PTI__width, PTI__height, PTI__filled=False
    ):
        params = (
            self._surface,
            (round(x), round(y), round(PTI__width), round(PTI__height)),
            self.PTI__color,
        )
        if PTI__filled:
            pygame.gfxdraw.box(*params)
        else:
            pygame.gfxdraw.rectangle(*params)

    def PTI_draw__ellipse(self, (x, y), rx, ry, PTI__filled=False):
        params = (
            self._surface,
            int(round(x)), int(round(y)), int(round(rx)), int(round(ry)),
            self.PTI__color,
        )
        if PTI__filled:
            pygame.gfxdraw.filled_ellipse(*params)
        else:
            pygame.gfxdraw.ellipse(*params)

    def PTI_draw__polygon(self, PTI__points, PTI__filled=False):
        params = (
            self._surface,
            list(map(lambda (x, y): (round(x), round(y)), PTI__points)),
            self.PTI__color,
        )
        if PTI__filled:
            pygame.gfxdraw.filled_polygon(*params)
        else:
            pygame.gfxdraw.polygon(*params)

    def PTI_draw__picture(self, PTI__picture, (x, y)):
           self._surface.blit(PTI__picture._surface, (round(x), round(y)))
