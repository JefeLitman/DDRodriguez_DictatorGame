"""File containing the effort task for players
Version: 1.1
Made By: Edgar RP
"""
from otree.api import *
from utils import set_experiment_params

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'effort_task'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NRO_SECCION = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    winner_section = models.StringField()
    treatment = models.BooleanField()


# PAGES
class O001_instr(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            nombre_seccion = C.NRO_SECCION,
            points_4_cash = int(player.session.config["real_world_currency_per_point"])
        )

class O002_task(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            nombre_seccion = C.NRO_SECCION
        )

class O003_results(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            nombre_seccion = C.NRO_SECCION
        )
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        set_experiment_params(player)


page_sequence = [O001_instr, O002_task, O003_results]
