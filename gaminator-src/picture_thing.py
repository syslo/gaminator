# -*- coding: utf-8 -*-


from .thing import PTI__Thing
from .canvas import PTI__Canvas
from .picture import PTI__Picture


class PTI__PictureThing(PTI__Thing):

    def __init__(self):
        PTI__Thing.__init__(self)
        self.PTI__picture = Picture(20, 20)

    @property
    def PTI__picture(self):
        return self._back_picture

    @PTI__picture.setter
    def PTI__picture(self, PTI__picture):
        self._back_picture = PTI__picture
        self._canvas = PTI__Canvas(self._picture)
        self.PTI__width = PTI__picture.width
        self.PTI__height = PTI__picture.height

    @property
    def PTI__canvas(self):
        return self._canvas

    def PTI_thing__paint(self, PTI__canvas):
        PTI__canvas.PTI__picture(self._back_picture, (0, 0))
