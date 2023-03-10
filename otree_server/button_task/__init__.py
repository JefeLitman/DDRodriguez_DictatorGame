"""File containing the button task for players
Version: 1.0
Made By: Edgar RP
"""
from otree.api import *
from utils import set_experiment_params

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'button_task'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    NOMBRE_SECCION = 2
    NOMBRE_BOTON = "destruir"

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    winner_section = models.StringField()
    treatment = models.BooleanField()
    button_pressed = models.BooleanField()
    button_expectative = models.BooleanField()

# PAGES
class O001_instr(Page):
    @staticmethod
    def is_displayed(player):
        return player.session.config["treatment_social"]
    
    @staticmethod
    def vars_for_template(player):
        return dict(
            nombre_seccion = C.NOMBRE_SECCION,
            nombre_boton = C.NOMBRE_BOTON
        )

class O002_task(Page):
    form_model = 'player'
    form_fields = ['button_pressed']

    @staticmethod
    def is_displayed(player):
        return player.session.config["treatment_social"]
    
    def vars_for_template(player):
        return dict(
            nombre_seccion = C.NOMBRE_SECCION,
            nombre_boton = C.NOMBRE_BOTON.capitalize()
        )

class O003_expect(Page):
    form_model = 'player'
    form_fields = ['button_expectative']

    @staticmethod
    def is_displayed(player):
        return player.session.config["treatment_social"]
    
    def vars_for_template(player):
        return dict(
            nombre_seccion = C.NOMBRE_SECCION,
            nombre_boton = C.NOMBRE_BOTON
        )
    
class ResultsWaitPage(WaitPage):
    @staticmethod
    def is_displayed(player):
        return player.session.config["treatment_social"]
    
    @staticmethod
    def after_all_players_arrive(group):
        if group.session.winner_section == 1:
            if p1.button_pressed:
                p0.payoff = 0
        p0, p1 = group.get_players()
        
        for p in group.get_players():
            p.payoff = 100

class O004_results(Page):
    @staticmethod
    def is_displayed(player):
        return player.session.config["treatment_social"]
    
    def vars_for_template(player):
        return dict(
            nombre_seccion = C.NOMBRE_SECCION
        )
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        set_experiment_params(player)


page_sequence = [O001_instr, O002_task, O003_results]
