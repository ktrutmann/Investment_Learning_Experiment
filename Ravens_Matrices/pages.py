from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Introduction_1(Page):
    form_model = 'player'
    
    def is_displayed(self):
        return self.player.role() == 'player'
  

class Introduction_2(Page):
    form_model = 'player'
    
    def is_displayed(self):
        return self.player.role() == 'player'
   

class Introduction_3(Page):
    form_model = 'player'
    
    def is_displayed(self):
        return self.player.role() == 'player'
   

class Introduction_4(Page):
    form_model = 'player'
    
    def is_displayed(self):
        return self.player.role() == 'player'
   

class Start(Page):
    def is_displayed(self):
        return self.player.role() == 'player'and self.round_number == 1 

    def before_next_page(self):
        # user has 3 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 3*60


class Matrix_1(Page):
    form_model = 'player'
    form_fields = ['cogn_rpm_matrix_1']
    timer_text = 'Verbleibende Zeit für die Matrizenaufgaben:'
    def get_timeout_seconds(self):
        return self.player.get_timeout_seconds()

    def is_displayed(self):
        return self.player.role() == 'player'and self.round_number == 1 



class Matrix_2(Page):
    form_model = 'player'
    form_fields = ['cogn_rpm_matrix_2']
    timer_text = 'Verbleibende Zeit für die Matrizenaufgaben:'
    def get_timeout_seconds(self):
        return self.player.get_timeout_seconds()

    def is_displayed(self):
        return self.player.role() == 'player'and self.round_number == 1 

    def before_next_page(self):
        if self.request.POST.get('Zurück'):
            if self.request.POST.get('Zurück')[0] == '1':
                self._is_frozen = False
                self._index_in_pages -= 2
                self.participant._index_in_pages -= 2


class Matrix_3(Page):
    form_model = 'player'
    form_fields = ['cogn_rpm_matrix_3']
    timer_text = 'Verbleibende Zeit für die Matrizenaufgaben:'
    def get_timeout_seconds(self):
        return self.player.get_timeout_seconds()

    def is_displayed(self):
        return self.player.role() == 'player'and self.round_number == 1 

    def before_next_page(self):
        if self.request.POST.get('Zurück'):
            if self.request.POST.get('Zurück')[0] == '1':
                self._is_frozen = False
                self._index_in_pages -= 2
                self.participant._index_in_pages -= 2
  

class Matrix_4(Page):
    form_model = 'player'
    form_fields = ['cogn_rpm_matrix_4']
    timer_text = 'Verbleibende Zeit für die Matrizenaufgaben:'
    def get_timeout_seconds(self):
        return self.player.get_timeout_seconds()

    def is_displayed(self):
        return self.player.role() == 'player'and self.round_number == 1 

    def before_next_page(self):
        self.player.add_earnings_to_payoff()

        if self.request.POST.get('Zurück'):
            if self.request.POST.get('Zurück')[0] == '1':
                self._is_frozen = False
                self._index_in_pages -= 2
                self.participant._index_in_pages -= 2


class Overestimation(Page):
    form_model = 'player'
    form_fields = ['pers_rpm_overestimation_answer']

    def is_displayed(self):
        return self.player.role() == 'player'


class Overplacement(Page):
    form_model = 'player'
    form_fields = ['pers_rpm_overplacement_answer']

    def is_displayed(self):
        return self.player.role() == 'player'


page_sequence = [
    Introduction_1,
    Introduction_2,
    Introduction_3,
    Introduction_4,
    Start,
    Matrix_1,
    Matrix_2,
    Matrix_3,
    Matrix_4,
    Overestimation,
    Overplacement]
