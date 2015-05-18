#  -*- coding: utf-8 -*-


import pygame


class _WindowSettings(object):

    def __init__(self):
        self._flags = 0
        self._width = 600
        self._height = 400
        self._changed_mode = True
        self._caption = "Gaminator"
        self._changed_caption = True
        self.fps = 60

    def _set_flag(self, flag):
        self._flags = self._flags | flag

    def _reset_flag(self, flag):
        self._flags = (self._flags | flag) - flag

    def _apply_changes(self):
        if self._changed_mode:
            self._changed_mode = False
            pygame.display.set_mode((self._width, self._height), self._flags)
        if self._changed_caption:
            self._changed_caption = False
            pygame.display.set_caption(self._caption)

    @property
    def PTI__width(self):
        return self._width

    @PTI__width.setter
    def PTI__width(self, _width):
        self._changed_mode = True
        self._width = _width

    @property
    def PTI__height(self):
        return self._height

    @PTI__height.setter
    def PTI__height(self, _height):
        self._changed_mode = True
        self._height = _height

    @property
    def PTI_window__caption(self):
        return self._caption

    @PTI_window__caption.setter
    def PTI_window__caption(self, _nazov):
        self._changed_caption = True
        self._caption = _nazov

    def PTI_window__fullscreen(self):
        self._changed_mode = True
        self._flags = (
            pygame.FULLSCREEN | pygame.DOUBLEBUF |
            pygame.HWSURFACE | pygame.NOFRAME
        )

    def PTI_window__fixed(self):
        self._changed_mode = True
        self._flags = 0

    def PTI_window__resizable(self):
        self._changed_mode = True
        self._flags = pygame.RESIZABLE


PTI__window = _WindowSettings()
