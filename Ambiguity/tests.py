from . import pages
from ._builtin import Bot

class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Page1, {'ambiguity_aversion': 2})
        yield (pages.Page2, {'loss_aversion': 2})
