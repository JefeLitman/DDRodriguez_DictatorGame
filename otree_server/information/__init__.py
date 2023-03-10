"""File containing the general and payments information for players
Version: 1.0
Made By: Edgar RP
"""
import random
from otree.api import *
from utils import set_experiment_params

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'information'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    winner_section = models.StringField()
    treatment = models.BooleanField()

def creating_session(subsession):
    sections = list(range(1,5))
    if subsession.session.config["treatment_social"]:
        sections += [5]
    random.seed(subsession.session.config["seed"]) #Implement the seed to replicate when creating sessions
    winner_section = random.choice(sections)
    subsession.session.winner_section = winner_section
    subsession.session.dices_numbers = []
    selected = random.choice(range(1,7))
    while selected !=  winner_section:
        if selected not in sections:
            subsession.session.dices_numbers += [selected]
        selected = random.choice(range(1,7))
    subsession.session.dices_numbers += [winner_section]
    print(subsession.session.dices_numbers)

# PAGES
class O001_general(Page):
    pass
    

class O002_pago(Page):
    @staticmethod
    def vars_for_template(player):
        p_4_c = int(player.session.config["real_world_currency_per_point"])
        fee_as_points = int(player.session.config["participation_fee"]) // p_4_c
        return dict(
            points_4_cash = p_4_c,
            fee = fee_as_points,
            treatment = player.session.config["treatment_social"]
        )
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        set_experiment_params(player)

page_sequence = [O001_general, O002_pago]
