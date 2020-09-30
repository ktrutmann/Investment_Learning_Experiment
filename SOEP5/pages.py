from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import json



class Introduction(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number == 1
    pass

class Page1(Page):
    form_model = 'player'
    form_fields = ['risk_soep_general']
    def is_displayed(self):
        return self.round_number == 1
    pass

class Page2(Page):
    form_model = 'player'
    form_fields = ['risk_soep_drive']
    pass


class Page3(Page):
    form_model = 'player'
    form_fields = ['risk_soep_finance']
    pass


class Page4(Page):
    form_model = 'player'
    form_fields = ['risk_soep_sport']
    pass


class Page5(Page):
    form_model = 'player'
    form_fields = ['risk_soep_career']
    pass


class Page6(Page):
    form_model = 'player'
    form_fields = ['risk_soep_health']
    pass


class Page7(Page):
    form_model = 'player'
    form_fields = ['risk_soep_trust']
    pass


# class Page2(Page):
#     form_model = 'player'
#     form_fields = ['risk_soep_drive', 'risk_soep_finance', 'risk_soep_sport', 'risk_soep_career', 'risk_soep_health', 'risk_soep_trust']
#     pass

start_pages = [Introduction, Page1]

initial_page_sequence = [
    Page2,
    Page3,
    Page4,
    Page5,
    Page6,
    Page7
]

page_sequence = []


class MyPage(Page):
    def inner_dispatch(self):
        page_seq = int(self.__class__.__name__.split('_')[1])
        page_to_show = json.loads(self.player.page_sequence)[page_seq]
        self._is_frozen = False
        self.__class__ = globals()[page_to_show]
        return super(globals()[page_to_show], self).inner_dispatch()


for i, _ in enumerate(initial_page_sequence):
    NewClassName = "Page_{}".format(i)
    A = type(NewClassName, (MyPage,), {})
    locals()[NewClassName] = A
    page_sequence.append(locals()[NewClassName])

page_sequence = start_pages + page_sequence
