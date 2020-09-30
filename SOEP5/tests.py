from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import json

class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Introduction)
        yield (pages.Page1, {'risk_soep_general': 2})
        yield (pages.Page_0, {'risk_soep_drive': 2})
        yield (pages.Page_1, {'risk_soep_finance': 2})
        yield (pages.Page_2, {'risk_soep_sport': 2})
        yield (pages.Page_3, {'risk_soep_career': 2})
        yield (pages.Page_4, {'risk_soep_health': 2})
        yield (pages.Page_5, {'risk_soep_trust': 2})
