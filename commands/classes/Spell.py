#!/usr/bin/env python2

import random
import math

class Element:
    def __init__(self, name):
        self.name = name
        self.goodAgainst = []
        self.badAgainst = []

class Spell:
    def __init__(self, name, power, percentage, element):
        self.name = name
        self.power = power
        self.percentage = percentage
        self.element = element

    def use(self, attacker, defencer):
        c = 2 if random.randint(0, 5) == 0 else 1
        a = attacker.getAttack()
        d = defencer.getDefence()
        r = random.randint(217, 255)
        m = 1.0
        message = ""
        if c == 2:
            message += "C'est un coup critique! "

        #m = modificateur by type. TODO
        if self.element == attacker.element:
            m *= 1.5

        if defencer.element in self.element.goodAgainst:
            m *= 2
            message += " C'est tres efficace! "
        elif defencer.element in self.element.badAgainst:
            m *= 0.5
            message += " Ca n'est pas tres efficace... "
        

        if random.randint(1, 100) > self.percentage:
            return ("Rate! ", 0)
        power = math.floor((((((attacker.level * 0.4 * c) + 2.0) * (a / d) * (self.power / 50.0)) + 2.0) * m * r / 255.0))
        defencer.life -= power
        return (message, power)

class ElementsManager:
    def __init__(self):
        fire = Element("Feux")
        water = Element("Eau")
        dirt = Element("Terre")
        fire.goodAgainst = [
            dirt
            ]
        fire.badAgainst = [
            water
            ]
        water.goodAgainst = [
            fire
            ]
        water.badAgainst = [
            dirt
            ]
        dirt.goodAgainst = [
            water
            ]
        dirt.badAgainst = [
            fire
            ]

        self.elements = [
            fire,
            water,
            dirt
            ]

    def get(self, name):
        for elem in self.elements:
            if elem.name == name:
                return elem
        return False

global elementsManager
elementsManager = ElementsManager()
