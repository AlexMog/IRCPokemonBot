#!/bin/env python2

import copy
from commands.classes.Pokemons import *
import random

class UserManager:
    def __init__(self):
        self.userlist = []
    
    def addUser(self, user):
        self.userlist.append(user)

    def remUser(self, username):
        self.userlist.remove(self.findUser(username))

    def findUser(self, username):
        for elem in self.userlist:
            if elem.getUsername() == username:
                return elem
        return False

class User:
    def __init__(self, username):

        self.username = username
        self.vars = []
        self.pokemons = []
        self.money = 5000
        self.items = []
        self.pokeid = 0
        self.battle = None
        self.active_pokemon = None
        self.addPokemon(copy.copy(pokemonsManager.pokemons[random.randint(0, len(pokemonsManager.pokemons) - 1)]))

    def hasAlivePokemon(self):
        for elem in self.pokemons:
            if elem.life > 0:
                return True
        return False

    def getItems(self):
        return self.items

    def getItem(self, itemName):
        for elem in self.items:
            if elem[0] == itemName:
                return elem
        return False

    def setItem(self, itemName, number):
        elem = self.getItem(itemName)
        if elem == False:
            elem = [itemName, number]
            self.items.append(elem)
        else:
            elem[1] = number

    def getMoney(self):
        return self.money

    def setMoney(self, money):
        self.money = money

    def getPokemons(self):
        return self.pokemons

    def addPokemon(self, pokemon):
        pokemon.pokeid = self.pokeid
        self.pokemons.append(pokemon)
        self.active_pokemon = pokemon
        self.pokeid += 1

    def removePokemon(self, pokemon):
        i = 0
        for i in range(len(self.pokemons)):
            if self.pokemons[i].pokeid == pokemon.pokeid:
                self.pokemons.pop(i)
                return

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def setVar(self, varname, value):
        val = self.getVar(varname)
        if val != False:
            val[1] = value
        else:
            self.vars.append([varname, value])

    def getVar(self, varname):
        for elem in self.vars:
            if elem[0] == varname:
                return elem
        return False
