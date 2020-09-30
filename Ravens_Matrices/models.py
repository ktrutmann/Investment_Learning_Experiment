from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import time

author = 'Adrian Leuenberger'

doc = """
Raven’s Progressive Matrices (RPM)
Civalli, A. & Deck, S. (2017). A Flexible and Customizable Method for Assessing Cognitive Abilities:
https://digitalcommons.chapman.edu/cgi/viewcontent.cgi?article=1220&context=esi_working_papers
"""


class Constants(BaseConstants):
    name_in_url = 'RPM'
    players_per_group = None
    num_rounds = 1
    endowment = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



def scale_1(label):
    return models.IntegerField(
        choices=[
            [0, 'A'],
            [1, 'B'],
            [0, 'C'],
            [0, 'D'],
            [0, 'E'],
            [0, 'F'],
        ],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

def scale_2(label):
    return models.IntegerField(
        choices=[
            [0, 'A'],
            [0, 'B'],
            [0, 'C'],
            [0, 'D'],
            [1, 'E'],
            [0, 'F'],
        ],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

def scale_3(label):
    return models.IntegerField(
        choices=[
            [1, 'A'],
            [0, 'B'],
            [0, 'C'],
            [0, 'D'],
            [0, 'E'],
            [0, 'F'],
        ],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


def scale_4(label):
    return models.IntegerField(
        choices=[
            [1, 'A'],
            [0, 'B'],
            [0, 'C'],
            [0, 'D'],
            [0, 'E'],
            [0, 'F'],
        ],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

class Player(BasePlayer):
    cogn_rpm_matrix_1 = scale_1('Wählen Sie das Element, welches das Bild oben sinnvoll ergänzt:')
    cogn_rpm_matrix_2 = scale_2('Wählen Sie das Element, welches das Bild oben sinnvoll ergänzt:')
    cogn_rpm_matrix_3 = scale_3('Wählen Sie das Element, welches das Bild oben sinnvoll ergänzt:')
    cogn_rpm_matrix_4 = scale_4('Wählen Sie das Element, welches das Bild oben sinnvoll ergänzt:')
    cogn_rpm_total_points = models.IntegerField(initial=None)
    pers_rpm_overestimation_answer = models.IntegerField(label='Anzahl:', min=0, max=4)
    pers_rpm_overestimation_score = models.IntegerField()
    pers_rpm_overplacement_answer = models.IntegerField(label='Rang:', min=1, max=100)

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry'] - time.time() > 0
    
    def role(self):
        return 'player'

    def add_earnings_to_payoff(self):
        # Calculate the points:
        self.cogn_rpm_total_points = self.cogn_rpm_matrix_1 + self.cogn_rpm_matrix_2 +\
                                            self.cogn_rpm_matrix_3 + self.cogn_rpm_matrix_4
        self.payoff = c(self.cogn_rpm_total_points * Constants.endowment)
        self.participant.vars['payoff_dict']['ravens_bonus'] = self.payoff

        # Update the total payoff
        self.participant.vars['payoff_dict']['payoff_total'] = self.participant.payoff_plus_participation_fee()
