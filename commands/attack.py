#!/usr/bin/env python2

import copy
import classes
import random
import time

def attack(connection, canal, auteur, cmds, canalobj, mogbot):
    user = mogbot.getUserManager().findUser(auteur)
    if user == False:
        connection.privmsg(canal, auteur + " je ne te trouve pas dans la base de donnees :( - erreur 500")
        return
    if user.battle is None:
        connection.privmsg(canal, auteur + " tu es en combat avec personne.")
        return

    if len(cmds) > 2:
        battle = user.battle
        if battle.accepted == False:
            connection.privmsg(canal, auteur + " le combat n'a pas encore ete accepte")
            return
        if battle.turn.username == user.username:
            connection.privmsg(canal, battle.fight(cmds[2]))
        else:
            connection.privmsg(canal, auteur + " ce n'est pas a toi de jouer.")
        if battle.finished:
            battle.user1.battle = None
            battle.user2.battle = None
        elif battle.auto and battle.turnCount % 2 == 0:
            time.sleep(2)
            connection.privmsg(canal, battle.fight(battle.turn.active_pokemon.spells[random.randint(0, len(battle.turn.active_pokemon.spells) - 1)].name))
    else:
        connection.privmsg(canal, auteur + " usage: fight <nom du sort a utiliser>")
