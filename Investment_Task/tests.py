from . import pages
from ._builtin import Bot
from otree.api import Submission
from .models import Constants
import random as rd
from scipy.special import softmax


class PlayerBot(Bot):

    cases = ['model']  # Either 'model' or 'random'
    base_alpha = .2  # What is the learning rat in a "normal" situation
    alpha_effect = .08  # How much lower is the learning rate for the affected situations?
    softmax_sens = 1  # Sensitivity on the softmax function.
    # Extremely sensitive means it's a step function at a 50:50 belief
    risk_aversion_param = .88  # The amount of risk aversion in the expected utility model y = x^param
    cur_up_belief = 50

    def get_model_trade(self):
        current_portfolio = self.player.cash + self.player.hold * self.player.price
        win_utils = [(current_portfolio + i) ** self.risk_aversion_param for i in Constants.updates]
        lose_utils = [(current_portfolio - i) ** self.risk_aversion_param for i in Constants.updates]

        up_belief = self.cur_up_belief / 100

        investing_utility = up_belief * sum(win_utils) / len(Constants.updates) +\
            (1 - up_belief) * sum(lose_utils) / len(Constants.updates)
        shorting_utility = up_belief * sum(lose_utils) / len(Constants.updates) +\
            (1 - up_belief) * sum(win_utils) / len(Constants.updates)

        # Use softmax to decide what to do:
        all_utilities = [shorting_utility, current_portfolio ** self.risk_aversion_param, investing_utility]
        choice_probs = softmax([float(i * self.softmax_sens) for i in all_utilities])
        target_holding = rd.choices(k=1, population=[-1, 0, 1], weights=choice_probs)[0]

        return target_holding - self.player.hold

    def get_model_belief(self):
        if self.player.participant.vars['i_in_block'] == 0:
            return 50

        prev_self = self.player.in_round(self.round_number - 1)
        belief = prev_self.belief / 100
        prev_returns = prev_self.returns

        price_up = self.player.price > prev_self.price
        fav_move = (self.player.hold == 1 and price_up) or\
            (self.player.hold == - 1 and not price_up)
        is_interaction = self.player.hold == prev_self.hold and\
            ((prev_returns > 0 and fav_move) or (prev_returns < 0 and not fav_move))
        new_belief = belief +\
            ((self.base_alpha + self.player.alpha_shift) - is_interaction * self.alpha_effect) *\
            (int(price_up) - belief)

        # Also adding some noise so we don't over-fit the model later
        eta = rd.normalvariate(0, .01)
        new_belief = round((new_belief + eta) * 100)
        return min(max(new_belief, 0), 100)

    def play_round(self):
        yield Submission(pages.initializer_page, check_html=False)

        if self.player.participant.vars['i_in_block'] == 0:
            yield pages.condition_page

        # trading page
        if not self.player.participant.vars['skipper']:
            if self.case == 'model':
                self.cur_up_belief = self.get_model_belief()
                transaction = self.get_model_trade()
            else:
                transaction = rd.randint(-1, 1) - self.player.hold

            yield Submission(pages.trading_page, {'transaction': transaction,
                                                  'time_to_order': 2,
                                                  'unfocused_time_to_order': 0},
                             check_html=False)

        # Belief page
        if self.player.participant.vars['belief_elicitation'] and not self.player.participant.vars['skipper']:
            if self.case == 'model':
                this_belief = self.cur_up_belief
            else:
                this_belief = rd.randint(0, 100)

            yield Submission(pages.belief_page, {'belief': this_belief,
                                                 'time_to_belief_report': 3,
                                                 'unfocused_time_to_belief_report': 0},
                             check_html=False)

        if not self.player.participant.vars['skipper']:
            yield pages.update_page, {'update_time_used': 2}

        if self.round_number == Constants.num_rounds:
            yield pages.end_page
