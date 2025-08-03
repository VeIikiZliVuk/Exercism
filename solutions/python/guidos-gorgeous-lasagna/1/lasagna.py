"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This module contains functions to calculate baking and preparation times
for making lasagna.
"""

# Define constants
EXPECTED_BAKE_TIME = 40  # Expected bake time in minutes
PREPARATION_TIME = 2  # Time per layer in minutes

def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining bake time.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).

    This function takes the number of minutes the lasagna has already been in 
    the oven and returns how many minutes are still needed to reach the 
    `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the total preparation time.

    :param number_of_layers: int - number of layers of lasagna.
    :return: int - total preparation time (in minutes).

    Each layer takes `PREPARATION_TIME` minutes to prepare.
    This function calculates the total preparation time for the given layers.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    :param number_of_layers: int - number of layers prepared.
    :param elapsed_bake_time: int - minutes the lasagna has been baking.
    :return: int - total elapsed time (in minutes).

    This function adds the preparation time (based on the number of layers) 
    to the time the lasagna has already been in the oven.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
