#  -*- coding: utf-8 -*-


from .constants import CONSTANTS
import pygame
import pygame.gfxdraw


def norm(x):
    return int(round(x))


class PTI__Canvas:

    def __init__(self, PTI__picture, PTI__color=None):
        self.PTI__color = PTI__color or CONSTANTS['PTI__BLACK']
        self._surface = PTI__picture._surface

    def PTI_draw__line(self, (x1, y1), (x2, y2)):
        pygame.gfxdraw.line(
            self._surface, norm(x1), norm(y1), norm(x2), norm(y2),
            self.PTI__color,
        )

    def PTI_draw__pixel(self, (x, y)):
        pygame.gfxdraw.pixel(
            self._surface, norm(x), norm(y), self.PTI__color,
        )

    def PTI_draw__rectangle(
        self, (x, y), PTI__width, PTI__height, PTI__filled=False
    ):
        params = (
            self._surface,
            (norm(x), norm(y), norm(PTI__width), norm(PTI__height)),
            self.PTI__color,
        )
        if PTI__filled:
            pygame.gfxdraw.box(*params)
        else:
            pygame.gfxdraw.rectangle(*params)

    def PTI_draw__ellipse(self, (x, y), rx, ry, PTI__filled=False):
        params = (
            self._surface,
            norm(x), norm(y), norm(rx), norm(ry),
            self.PTI__color,
        )
        if PTI__filled:
            pygame.gfxdraw.filled_ellipse(*params)
        else:
            pygame.gfxdraw.ellipse(*params)

    def PTI_draw__polygon(self, PTI__points, PTI__filled=False):
        params = (
            self._surface,
            list(map(lambda (x, y): (norm(x), norm(y)), PTI__points)),
            self.PTI__color,
        )
        if PTI__filled:
            pygame.gfxdraw.filled_polygon(*params)
        else:
            pygame.gfxdraw.polygon(*params)

    def PTI_draw__picture(self, PTI__picture, (x, y)):
        self._surface.blit(PTI__picture._surface, (norm(x), norm(y)))
