#  -*- coding: utf-8 -*-


from . import color
from .constants import CONSTANTS
import pygame
import os


class PTI__Picture:

    def __init__(self, PTI__width, PTI__height, PTI__has_alpha=False):

        self._width = 0
        self._height = 0
        self._has_alpha = False

        if isinstance(PTI__width, pygame.Surface) and PTI__height is None:
            self._set_surface(PTI__width)
        else:
            self.PTI_picture__reset(PTI__width, PTI__height, PTI__has_alpha)

    def PTI_picture__reset(
        self, PTI__width=None, PTI__height=None, PTI__has_alpha=None
    ):
        if PTI__width is not None:
            self._width = PTI__width
        if PTI__height is not None:
            self._height = PTI__height
        if PTI__has_alpha is not None:
            self._has_alpha = PTI__has_alpha

        dims = (self._width, self._height)

        flags = 0
        if self._has_alpha:
            self._surface = pygame.Surface(dims, pygame.SRCALPHA, 32)
            self._surface.convert_alpha()
        else:
            self._surface = pygame.Surface(dims)
            self._surface.set_colorkey((0, 1, 0))

        self.PTI_picture__clear()

    def PTI_picture__clear(self):
        self._surface.fill((0, 1, 0, 0))

    @property
    def PTI__width(self):
        return self._width

    @property
    def PTI__height(self):
        return self._height

    @property
    def PTI__has_alpha(self):
        return self._has_alpha

    def _set_surface(self, surface):
        self._surface = surface
        self._width = surface.get_width()
        self._height = surface.get_height()


def PTI__open_picture(*path):
    surface = pygame.image.load(os.path.join(*path))
    return PTI__Picture(surface, None)


def PTI__text_to_picture(
    PTI__text="", PTI_text__size=10, PTI__color=CONSTANTS["PTI__BLACK"],
    PTI_text__bold=False, PTI_text__italic=False,
):
    font = pygame.font.SysFont(
        None, PTI_text__size, bold=PTI_text__bold, italic=PTI_text__italic,
    )
    surface = font.render(PTI__text, False, PTI__color)
    return PTI__Picture(surface, None)
