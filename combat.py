"""
    this will include the math calculations for combats between units
    a combat should:
        > determine who attackers are (one or more)
        > determine who defenders are (is this always one?)
"""
from random import random, randint

def roll_d6():
    return randint(1,6)

def roll_gen(num=1, type='d6'):
    if type = 'd6'
        result = (rand(1,6) for i in range(num))

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


