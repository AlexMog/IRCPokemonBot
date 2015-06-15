#!/usr/bin/env python2

import random
import math
import copy
from Spell import *

class Pokemon:
    def __init__(self, name, baseHp, lifePerLevel, attack, attackPerLevel, baseDef, defencePerLevel, spells, elements):
        self.level = 1
        self.exp = 0
        self.name = name
        self.baseHp = baseHp
        self.lifePerLevel = lifePerLevel
        self.defencePerLevel = defencePerLevel
        self.spells = spells
        self.attackPerLevel = attackPerLevel
        self.baseDef = baseDef
        self.pokeid = 0
        self.attack = attack
        self.active_pokemon = self.pokeid
        self.battle = None
        self.life = self.getMaxLife()
        self.username = self.name
        self.elements = elements


    def getActivePokemon(self):
        return self

    def hasAlivePokemon(self):
        return False

    def removePokemon(self, pokemon):
        self.active_pokemon = None

    def addSpell(self, spell):
        self.spells.append(spell)

    def getSpells(self):
        return self.spells

    def getSpell(self, name):
        for e in self.spells:
            if e.name == name:
                return e
        return False

    def expForNextLevel(self):
#        return 1.2 * (self.level**3) - 15 * (self.level**2) + 100 * self.level - 140
        return 1.25 * (self.level**3) + 50

    def gainExp(self, fromPokemon):
        self.addExp(self.calcGainedExp(fromPokemon))

    def calcGainedExp(self, fromPokemon):
        return 200 * fromPokemon.level / 7

    def addExp(self, exp):
        self.exp += exp
        needed = self.expForNextLevel()
        while self.exp >= needed:
            self.exp = self.exp - needed
            self.level += 1
            self.life = self.getMaxLife()

    def getMaxLife(self):
        return self.lifePerLevel * self.level + self.baseHp

    def getAttack(self):
        return self.attackPerLevel * self.level + self.attack

    def getDefence(self):
        return self.defencePerLevel * self.level + self.baseDef

    def str(self):
        spells = ""
        for elem in self.spells:
            if len(spells) != 0:
                spells += ", "
            spells += elem.name

        elements = ""
        for elem in self.elements:
            if len(elements) != 0:
                elements += ", "
            elements += elem.name

        return "(pokeId(" + str(self.pokeid) + "), Nom(" + self.name + "), Niveau(" + str(self.level) + "), Attaque(" + str(self.getAttack()) + "), VieMax(" + str(self.getMaxLife()) + "), Defense(" + str(self.getDefence()) + "), Sorts: (" + spells + "), Exp: (" + str(self.exp) + " / " + str(self.expForNextLevel()) + "), Elements(" + elements + "))"

    def fight(self, spellName, defencer):
        spell = self.getSpell(spellName)
        if spell == False:
            return "Sort '" + spellName + "' introuvable."
        rep = spell.use(self, defencer)
        return rep[0] + self.name + " utilise " + spell.name + " (" + spell.element.name + ") et fait " + str(rep[1]) + " dommages a " + defencer.name + " (pv: " + str(defencer.life) + " / " + str(defencer.getMaxLife()) + ")"


class PokemonsManager:
    def __init__(self):
        self.pokemons = [
            Pokemon("ZeratoR", 140, 6, 10, 1, 5, 0.1, [
                    Spell("Son_Pere", 10, 90, elementsManager.get("Feu")),
                    Spell("Mute", 15, 50, elementsManager.get("Feu")),
                    Spell("Rend_l'argent", 50, 100, elementsManager.get("Feu")),
                    Spell("Dailymotion_drop", 100, 100, elementsManager.get("Feu"))
                    ], [
                    elementsManager.get("Feu")
                    ]),
            Pokemon("Noxer", 80, 6, 5, 1, 0.5, 0.2, [
                    Spell("Ventre_devoreur", 30, 80, elementsManager.get("Terre")),
                    Spell("Millenium", 50, 80, elementsManager.get("Terre"))
                    ], [
                    elementsManager.get("Terre")
                    ]),
            Pokemon("Furiie", 100, 4, 10, 1, 2, 0.05, [
                    Spell("Cri_strident", 20, 100, elementsManager.get("Eau")),
                    Spell("League_of_legends", 100, 20, elementsManager.get("Terre")),
                    Spell("Bisous", 20, 50, elementsManager.get("Eau"))
                    ], [
                    elementsManager.get("Eau")
                    ]),
            Pokemon("MisterMV", 140, 6, 9, 1, 0.1, 0.1, [
                    Spell("SAUCISSON", 10, 100, elementsManager.get("Terre")),
                    Spell("Speedrun", 20, 80, elementsManager.get("Feu")),
                    Spell("Jeu_a_la_pisse", 100, 30, elementsManager.get("Terre"))
                    ], [
                    elementsManager.get("Terre")
                    ]),
            Pokemon("Leeroy Jenkins", 100, 5, 20, 1, 0.1, 0.1, [
                    Spell("LEEEEEROY_JENKINS", 5000, 10, elementsManager.get("Feu"))
                    ], [
                    elementsManager.get("Feu")
                    ]),
            Pokemon("AlexMog", 180, 5, 20, 1, 3, 0.5, [
                    Spell("Tardbecile", 30, 100, elementsManager.get("Eau")),
                    Spell("Equilibrage_ratte", 70, 10, elementsManager.get("Eau")),
                    Spell("Blague_de_merde", 50, 30, elementsManager.get("Eau"))
                    ], [
                    elementsManager.get("Eau")
                    ]),
            Pokemon("Demoneth", 160, 5, 10, 1, 4, 0.2, [
                    Spell("Molotov_sur_orange", 20, 50, elementsManager.get("Feu")),
                    Spell("Live_o_maniaque", 15, 100, elementsManager.get("Feu")),
                    Spell("La_co_marche", 100, 10, elementsManager.get("Feu"))
                    ], [
                    elementsManager.get("Feu")
                    ])
            ]

    def getRandom(self):
        ret = copy.copy(self.pokemons[random.randint(0, len(self.pokemons) - 1)])
        return ret

    def getFromName(self, name):
        for elem in self.pokemons:
            if elem.name == name:
                return elem
        return False

global pokemonsManager
pokemonsManager = PokemonsManager()
