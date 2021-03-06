#!/usr/bin/env python2

import random
import math

class Element:
    def __init__(self, name, goodAgainst, badAgainst):
        self.name = name
        self.goodAgainst = goodAgainst
        self.badAgainst = badAgainst

class Spell:
    def __init__(self, name, power, percentage, element):
        self.name = name
        self.power = power
        self.description = ""
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

        for elem in attacker.elements:
            if self.element.name == elem.name:
                m *= 1.5

        for elem in defencer.elements:
            if elem.name in self.element.goodAgainst:
                m *= 2
                message += " C'est tres efficace! "
            elif elem.name in self.element.badAgainst:
                m *= 0.5
                message += " Ca n'est pas tres efficace... "
        
        if random.randint(1, 100) > self.percentage:
            return ("Rate! ", 0)
        power = math.floor((((((attacker.level * 0.4 * c) + 2.0) * (a / d) * (self.power / 50.0)) + 2.0) * m * r / 255.0))
        defencer.life -= power
        return (message, power)

class ElementsManager:
    def __init__(self):
        self.elements = [
            Element("Feu", ["Terre"], ["Eau"]),
            Element("Eau", ["Feu"], ["Terre"]),
            Element("Terre", ["Eau"], ["Feu"])
            ]

    def get(self, name):
        for elem in self.elements:
            if elem.name == name:
                return elem
        return False

global elementsManager
elementsManager = ElementsManager()
