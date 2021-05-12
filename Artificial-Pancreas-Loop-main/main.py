import random
import matplotlib.pyplot as plt
from inputs import *
from functions import *
import copy

# ----------------------------------MAIN FUNC----------------------------------------
def get_user_input():
    carbs_intake = int(input("How many carbs do you eating?:  "))
    eat_time = int(input("When you gonna eat?:  "))
    return carbs_intake, eat_time

def get_total_insulin(carbs_intake, eat_time):
    glucose_data = get_glucose_data(FIRST_GLUCOSE_READING, cycles)
    glucose_data_delta = get_glucose_data_delta(glucose_data)
    basal_data = get_basal_data(glucose_data_delta)
    ratio = insulin_to_carb_ratio(daily_insulin_units, daily_carbs_intake)
    insulin_needed = carbs_intake / ratio

    total_insulin_data = total_insulin(
        basal_data = basal_data,
        insulin_needed = insulin_needed,
        eat_time = eat_time
    )
    return glucose_data, glucose_data_delta, basal_data, total_insulin_data

def get_total_insulin_draw(glucose_data, glucose_data_delta, basal_data, total_insulin_data):
    fig = plt.figure()
    print_data(fig, glucose_data, "Glucose data", 221)
    print_data(fig, glucose_data_delta, "Delta glucose data", 222)
    print_data(fig, basal_data, "Basal insulin units", 223)
    print_data(fig, total_insulin_data, "Total insulin data", 224)

    plt.show()

# ------------------------------------MAIN-----------------------------------------
def main():
    # User input
    carbs_intake, eat_time = get_user_input()

    # Total insulin data
    glucose_data, glucose_data_delta, basal_data, total_insulin_data = get_total_insulin(carbs_intake, eat_time)

    # Total insulin data
    get_total_insulin_draw(glucose_data, glucose_data_delta, basal_data, total_insulin_data)

if __name__ == '__main__':
    main()