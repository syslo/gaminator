# -*- coding: utf-8 -*-

from .constants import CONSTANTS

from .gaminator import gaminator
from .thing import PTI__Thing
from .world import PTI__World

from .events import PTI_decorator__event
from .collisions import PTI_decorator__collision

from .color import PTI__Color
from .picture import PTI__Picture
from .canvas import PTI__Canvas


import pygame as _pygame
for name in dir(_pygame):
    if name.startswith("K_"):
        CONSTANTS[name] = getattr(_pygame, name)

for key, value in CONSTANTS.items():
    setattr(gaminator, key, value)
