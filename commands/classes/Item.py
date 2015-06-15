#!/bin/env python2

import random

class Item:
    def __init__(self, name):
        self.name = name
        self.price = 0

    def use(self, battle):
        return ("Nothing to do :(", True)

class Pokeball(Item):
    def __init__(self, name, percent, price):
        Item.__init__(self, name)
        self.percent = percent
        self.price = price

    def use(self, battle):
        msg = "La capture de " + battle.user2.getActivePokemon().name + " a ratte, il a fuit. Combat termine."
        if random.randint(0, 100) <= self.percent:
            msg = battle.user1.username + " a capture " + battle.user2.getActivePokemon().name
            battle.user1.addPokemon(battle.user2.getActivePokemon())
            battle.user2.removePokemon(battle.user2.getActivePokemon())
        battle.user1.battle.finished = True
        battle.user2.battle.finished = True
        return msg

class ItemsManager:
    def __init__(self):
        self.items = [
            Pokeball("pokeball", 10, 300),
            Pokeball("masterball", 30, 700),
            Pokeball("ultraball", 50, 1000),
            Pokeball("mogball", 100, 10000000)
            ]
        
    def getItem(self, itemName):
        for elem in self.items:
            if elem.name == itemName:
                return elem
        return False

global itemsManager
itemsManager = ItemsManager()

