# -*- coding: utf-8 -*-


from .thing import PTI__Thing
from .canvas import PTI__Canvas
from .picture import PTI__Picture
from .exceptions import PTI_exception__AssignmentUnsupported


class PTI__PictureThing(PTI__Thing):

    def __init__(self):
        PTI__Thing.__init__(self)
        self.PTI__picture = Picture(20, 20)

    @property
    def PTI__width(self):
        return self._width

    @PTI__width.setter
    def PTI__width(self, PTI__value):
        raise PTI_exception__AssignmentUnsupported()

    @property
    def PTI__height(self):
        return self._height

    @PTI__height.setter
    def PTI__height(self, PTI__value):
        raise PTI_exception__AssignmentUnsupported()

    @property
    def PTI__picture(self):
        return self._picture

    @PTI__picture.setter
    def PTI__picture(self, PTI__picture):
        self._picture = PTI__picture
        self._canvas = PTI__Canvas(self._picture)
        self._width = PTI__picture.width
        self._height = PTI__picture.height

    @property
    def PTI__canvas(self):
        return self._canvas

    def _repaint(self, canvas):
        canvas.PTI_draw__picture(
            self._picture,
            (self.PTI_thing__border_left, self.PTI_thing__border_up),
        )

    def PTI_thing__paint(self, PTI__canvas):
        pass
