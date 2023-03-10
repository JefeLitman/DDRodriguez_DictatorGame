"""File containing utilities functions for every section in the whole app
Version: 1.0
Made By: Edgar RP
"""
# import os
# import random
# import numpy as np
# import pandas as pd

def set_experiment_params(player):
    player.winner_section = str(player.session.winner_section)
    player.treatment = player.session.config["treatment_social"]
