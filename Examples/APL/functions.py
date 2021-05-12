import random
import matplotlib.pyplot as plt
from inputs import *

def get_glucose_data(first_glucose_value, CYCLES):
    y = []

    for i in range(CYCLES):
        y.append(first_glucose_value)
        first_glucose_value += (random.choice((-1, 1)) * random.uniform(0, 0.5))
    return y

def get_glucose_data_delta(glucose_data):
    y = []

    for i in range(len(glucose_data)):
        glucose_delta = glucose_data[i] - glucose_data[i-1]
        if glucose_delta < 0:
            glucose_delta = 0
        y.append(glucose_delta)
    return y

def get_insulin_sensitivity(DAILY_INSULIN_UNITS):
    insulin_sensitivity = 100 / DAILY_INSULIN_UNITS
    return insulin_sensitivity

def get_basal_data(glucose_data):
    y = []

    for i in range(len(glucose_data)):
        basal = glucose_data[i] * get_insulin_sensitivity(DAILY_INSULIN_UNITS)
        y.append(basal)
    return y

def print_data(figure, data, graph_title, graph_position):
    x = range(0, len(data))
    y = data

    ax1 = figure.add_subplot(graph_position)
    ax1.plot(x, y)
    ax1.set_title(graph_title)

def insulin_sensitivity():
    insulin_sensitivity = get_insulin_sensitivity(DAILY_INSULIN_UNITS)
    return insulin_sensitivity

def insulin_to_carb_ratio(DAILY_INSULIN_UNITS, daily_carbs_intake):
    result = daily_carbs_intake / DAILY_INSULIN_UNITS
    return result

def total_insulin(basal_data, insulin_needed, eat_time):
    bolus_and_basal_insulin_data = basal_data
    bolus_and_basal_insulin_data[eat_time] += insulin_needed
    return bolus_and_basal_insulin_data