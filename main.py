# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Alec Vis')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from random import random, randint

def roll_d6():
    return randint(1,6)

# def roll_gen(num=1, type='d6'):
#     if type = 'd6'
#         result = (rand(1,6) for i in range(num))

def attack(attack_number, ballistic_skill):
    num_hits = 0
    #
    for i in range(attack_number):
        if randint(1, 6) >= ballistic_skill:
            num_hits += 1
    return num_hits


def wound(hit_number, strength, opposing_toughness):
    num_wounds = 0

    if strength < opposing_toughness:
        if strength <= 2 * opposing_toughness:
            threshold = 6
        else:
            threshold = 5
    elif strength == opposing_toughness:
        threshold = 4
    elif strength > opposing_toughness:
        if strength >= 2 * opposing_toughness:
            threshold = 2
        else:
            threshold = 3

    for i in range(hit_number):
        if randint(1, 6) >= threshold:
            num_wounds += 1
    return num_wounds


def casualties(wounds_taken, model_hp):
    cas = wounds_taken//model_hp
    roll_over = wounds_taken%model_hp
    return cas


def morale(num_casualties, unit_leadership):
    if (randint(1,6) + num_casualties) <= unit_leadership:
        return print('Passed Morale Check')
    print('Failed Morale Check')
