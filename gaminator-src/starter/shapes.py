# -*- coding: utf-8 -*-


from gaminator import PTI__Thing, PTI__BLACK, PTI__game


class PTI_starter__Rect(PTI__Thing):

    def PTI__setup(self):
        self.PTI__color = PTI__BLACK
        self.PTI__filled = False
        self.PTI__world = PTI__game.PTI__world

    def PTI__paint(self, c):
        c.PTI__color = self.PTI__color
        c.PTI__rectangle(
            (0, 0),
            self.PTI__width, self.PTI__height,
            self.PTI__filled
        )

    def PTI__step(self):
        self.PTI__repaint()


class PTI_starter__Oval(PTI__Thing):

    def PTI__setup(self):
        self.PTI__color = PTI__BLACK
        self.PTI__filled = False
        self.PTI__world = PTI__game.PTI__world

    def PTI__paint(self, c):
        c.PTI__color = self.PTI__color
        c.PTI__ellipse(
            (self.PTI__width/2, self.PTI__height/2),
            self.PTI__width/2, self.PTI__height/2,
            self.PTI__filled
        )

    def PTI__step(self):
        self.PTI__repaint()
