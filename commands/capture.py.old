#!/usr/bin/env python2

import random
import time
import copy
from classes.Pokemons import Pokemon

capture_list = [
    Pokemon("ZeratoR", 10, 40, 5, []),
    Pokemon("Noxer", 3, 20, 0.5, []),
    Pokemon("Furiie", 9, 12, 2, []),
    Pokemon("MisterMV", 1, 40, 0.1, []),
    Pokemon("DFG", 10, 8, 2.5, []),
    Pokemon("LRB", 4, 10, 1.5, []),
    Pokemon("Fuka", 5, 15, 1, []),
    Pokemon("Xanf", 10, 40, 5, []),
    Pokemon("Leeroy Jenkins", 10, 5, 0.1, []),
    Pokemon("AlexMog", 100, 100, 100, [])
]
pokeballs = [
    ("pokeball", 10),
    ("masterball", 30),
    ("ultraball", 50),
    ("mogball", 100)
]

def get_pokeball(pokeball):
    for elem in pokeballs:
        if elem[0] == pokeball:
            return elem
    return False

def capture(connection, canal, auteur, cmds, canalobj, mogbot):
    if len(cmds) > 2:
        user = mogbot.getUserManager().findUser(auteur)
        if user == False:
            connection.privmsg(canal, auteur + " je ne te trouve pas dans la base de donnees :( - erreur 500")
            return
        pokeball = get_pokeball(cmds[2])
        if pokeball != False:
            itemStack = user.getItem(pokeball[0])
            if itemStack == False or itemStack[1] <= 0:
                connection.privmsg(canal, auteur + " tu n'as plus de " + pokeball[0] + " :(")
                return
            user.setItem(pokeball[0], itemStack[1] - 1)
            mob = capture_list[random.randint(0, len(capture_list) - 1)]
            connection.privmsg(canal, auteur + " essaye de capturer " + mob.getName() + " sauvage... (chance: " + str(pokeball[1]) + "%)")
            time.sleep(2)
            if random.randint(0, 100) <= pokeball[1]:
                user.addPokemon(copy.copy(mob))
                spells = ""
                for elem in mob.getSpells():
                    if len(spells) != 0:
                        spells += ","
                    spells += " " + elem
                connection.privmsg(canal, auteur + " a reussi a capturer " + mob.getName() + " ! (stats: Niveau(" + str(mob.getLevel()) + "), Force(" + str(mob.getStrength()) + "), VieMax(" + str(mob.getMaxLife()) + "), Esquive(" + str(mob.getDodgePercent()) + "%), Sorts: (" + spells + "))")
            else:
                connection.privmsg(canal, auteur + " n'a pas reussi a capturer " + mob.getName() + " :(")
        else:
            pokelist = ""
            for elem in pokeballs:
                if len(pokelist) != 0:
                    pokelist += ","
                pokelist += " " + elem[0] + "(" + str(elem[1]) + "%)"
            connection.privmsg(canal, auteur + " ce n'est pas une pokeball connue :( Voici une liste de pokeballs:" + pokelist)
    else:
        connection.privmsg(canal, auteur + " il faut que tu choisisse une pokeball pour capturer!")
