#!/bin/env python2

class Item:
    def __init__(self, name):
        self.name = name
        self.price = 0

    def use(self, user, pokemon, user2, pokemon2):
        pass

class Pokeball(Item):
    def __init__(self, name, percent, price):
        Item.__init__(self, name)
        self.percent = percent
        self.price = price

    def use(self, user, pokemon, user2, pokemon2):
        if random.randint(0, 100) <= self.percent:
            user.addPokemon(pokemon2)
            if user2 is not None:
                user2.removePokemon(pokemon2)
            return True
        else:
            return False

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

