from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

import itertools
import json


author = 'Kevin Trutmann'

doc = ""


def make_scale(label):
    return models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


class Constants(BaseConstants):
    name_in_url = 'ambg_loss'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ambiguity_aversion = make_scale('Bitte geben Sie an, im Allgemeinen, wie gewillt Sie sind, eine Entscheidung zu '
                                    'treffen, wenn die Wahrscheinlichkeit einer Konsequenz nicht bekannt ist.')
    loss_aversion = make_scale('Zu welchem Grad stimmen Sie der folgenden Aussage zu? Ich empfinde den Schmerz, '
                               'Geld zu verlieren, stärker im Vergleich zum Vergnügen, Geld zu gewinnen.')
