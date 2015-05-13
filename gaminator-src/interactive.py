#  -*- coding: utf-8 -*-


from code import InteractiveConsole
from threading import Thread
import traceback
import readline
import rlcompleter
import sys

from .thing import _ThingType


class _GaminatorInteractiveConsole(InteractiveConsole):

    def __init__(self, gaminator):
        self.gaminator = gaminator
        locals = {}
        locals.update(_ThingType._classes)
        locals['g'] = gaminator
        readline.set_completer(rlcompleter.Completer(locals).complete)
        readline.parse_and_bind("tab: complete")
        InteractiveConsole.__init__(self, locals)

    def runcode(self, code):
        with self.gaminator._lock:
            InteractiveConsole.runcode(self, code)


def interact(gaminator):
    console = _GaminatorInteractiveConsole(gaminator)

    def run():
        try:
            console.interact()
        finally:
            with gaminator._lock:
                gaminator.PTI_gaminator__end()
    thread = Thread(target=run)
    thread.start()

    return console
