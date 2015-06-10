#!/usr/bin/env python2

import copy
import classes
import random
from classes.Pokemons import *
from classes.Battle import *

def fight(connection, canal, auteur, cmds, canalobj, mogbot):
    user = mogbot.getUserManager().findUser(auteur)
    if user == False:
        connection.privmsg(canal, auteur + " je ne te trouve pas dans la base de donnees :( - erreur 500")
        return
    if user.battle is not None:
        connection.privmsg(canal, auteur + " tu es deja en combat avec quelqu'un!")
        return

    if len(cmds) > 2:
        if cmds[2] == "nature":
            u = pokemonsManager.getRandom()
            mini = user.active_pokemon.level - 5
            if mini <= 0:
                mini = 1
            maxi = mini + 10
            u.level = random.randint(mini, maxi)
            battle = Battle(user, u)
            battle.auto = True
            user.battle = u.battle = battle
            user.battle.accepted = True
            connection.privmsg(canal, user.username + " tu es tombe sur un " + u.username + " sauvage (lvl: " + str(u.level) + " )! Attention!")
        else:
            u = mogbot.getUserManager().findUser(cmds[2])
            if u == False:
                connection.privmsg(canal, user.username + " adversaire introuvable.")
                return
            user.battle = u.battle = Battle(user, u)
            connection.privmsg(canal, user.username + " a defie " + u.username + " en duel! Va-t-il accepter? (utilise accept pour accepter le duel et refuse pour refuser)")
    else:
        connection.privmsg(canal, auteur + " usage: fight <nature ou pseudo>")

