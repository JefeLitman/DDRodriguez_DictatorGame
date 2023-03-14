"""File containing the simple dictator for players
Version: 1.0
Made By: Edgar RP
"""
from otree.api import *
from utils import set_experiment_params

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'simple_dictator'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NRO_SECCION = 2

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    winner_section = models.StringField()
    treatment = models.BooleanField()
    sd_decision = models.IntegerField()
    sd_expectative = models.IntegerField()

# PAGES
class O001_instr(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            nombre_seccion = C.NRO_SECCION + int(player.session.config["treatment_social"])
        )

class O002_task(Page):
    form_model = 'player'
    form_fields = ['sd_decision']
    
    @staticmethod
    def vars_for_template(player):
        return dict(
            nombre_seccion = C.NRO_SECCION + int(player.session.config["treatment_social"])
        )

class O003_expect(Page):
    form_model = 'player'
    form_fields = ['sd_expectative']
    
    @staticmethod
    def vars_for_template(player):
        return dict(
            nombre_seccion = C.NRO_SECCION + int(player.session.config["treatment_social"])
        )
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        set_experiment_params(player)
        if player.session.winner_section == C.NRO_SECCION + int(player.session.config["treatment_social"]):
            player.payoff = player.sd_decision


page_sequence = [O001_instr, O002_task, O003_expect]
