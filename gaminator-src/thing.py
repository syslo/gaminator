# -*- coding: utf-8 -*-


from .thing_type import _ThingType
from .picture import PTI__Picture
from .canvas import PTI__Canvas


class PTI__Thing(object):

    __metaclass__ = _ThingType

    def __init__(self, *args, **kwargs):
        self._world = None

        self.x = 0
        self.y = 0
        self.PTI__x_align = 0.5
        self.PTI__y_align = 0.5
        self._width = 20
        self._height = 20

        self._will_repaint = True
        self._will_resize = True
        self._picture = PTI__Picture(20, 20)

        self.PTI_thing__setup(*args, **kwargs)

    @property
    def PTI_thing__world(self):
        return self._world

    @PTI_thing__world.setter
    def PTI_thing__world(self, value):
        if self._world is not None:
            self._world._disconnect_thing(self)
        if value is not None:
            value._connect_thing(self)
        self._world = value

    @PTI_thing__world.deleter
    def PTI_thing__world(self):
        if self._world is not None:
            self._world._disconnect_thing(self)
        self._world = None

    @property
    def PTI__width(self):
        return self._width

    @PTI__width.setter
    def PTI__width(self, PTI__width):
        self._will_resize = True
        self._width = PTI__width

    @property
    def PTI__height(self):
        return self._height

    @PTI__height.setter
    def PTI__height(self, PTI__height):
        self._will_resize = True
        self._height = PTI__height

    @property
    def PTI_thing__border_left(self):
        return self.x + (0-self.PTI__x_align)*self._width

    @property
    def PTI_thing__border_right(self):
        return self.x + (1-self.PTI__x_align)*self._width

    @property
    def PTI_thing__border_up(self):
        return self.y + (0-self.PTI__y_align)*self._height

    @property
    def PTI_thing__border_down(self):
        return self.y + (1-self.PTI__y_align)*self._height

    def PTI_thing__repaint(self):
        self._will_repaint = True

    def _repaint(self, canvas):
        if self._will_resize:
            self._will_repaint = True
            self._picture.PTI_picture__reset(
                PTI__width=self._width, PTI__height=self._height,
            )
            self._will_resize = False
        if self._will_repaint:
            self._picture.PTI_picture__clear()
            self.PTI_thing__paint(PTI__Canvas(self._picture))
            self._will_repaint = False
        canvas.PTI_draw__picture(
            self._picture,
            (self.PTI_thing__border_left, self.PTI_thing__border_up),
        )

    def PTI_thing__setup(self, *args, **kwargs):
        pass

    def PTI_thing__step(self):
        pass

    def PTI_thing__paint(self, PTI__canvas):
        pass
