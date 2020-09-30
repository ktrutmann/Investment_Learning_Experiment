from ._builtin import Page, WaitPage


class Page1(Page):
    form_model = 'player'
    form_fields = ['ambiguity_aversion']


class Page2(Page):
    form_model = 'player'
    form_fields = ['loss_aversion']


page_sequence = [Page1, Page2]
