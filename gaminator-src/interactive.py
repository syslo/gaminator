#  -*- coding: utf-8 -*-


from code import InteractiveConsole
from threading import Thread
import traceback
import readline
import rlcompleter
import sys

from .thing_type import _ThingType


class _GaminatorInteractiveConsole(InteractiveConsole):

    def __init__(self, game):
        self.game = game
        locals = {}
        exec('from gaminator import *', locals)
        locals.update(_ThingType._classes)
        readline.set_completer(rlcompleter.Completer(locals).complete)
        readline.parse_and_bind("tab: complete")
        InteractiveConsole.__init__(self, locals)

    def runcode(self, code):
        with self.game._lock:
            InteractiveConsole.runcode(self, code)


def interact(game):
    console = _GaminatorInteractiveConsole(game)

    def run():
        try:
            console.interact()
        finally:
            with game._lock:
                game.PTI_gaminator__end()
    thread = Thread(target=run)
    thread.start()

    return console
