# -*- coding: utf-8 -*-

from .constants import CONSTANTS

from .game import PTI__game
from .thing import PTI__Thing
from .world import PTI__World

from .events import PTI_decorator__event
from .collisions import PTI_decorator__collision

from .color import PTI__Color
from .picture import PTI__Picture, PTI__open_picture, PTI__text_to_picture
from .canvas import PTI__Canvas

from .window import PTI__window


import pygame as _pygame
for name in dir(_pygame):
    if name.startswith("K_"):
        CONSTANTS[name] = getattr(_pygame, name)

import sys as _sys
_module = _sys.modules[__name__]
for key, value in CONSTANTS.items():
    setattr(_module, key, value)

_pygame.font.init()
