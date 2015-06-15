#!/usr/bin/env python2

import copy
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
            msg = battle.nextStep()
            if msg != False:
                connection.privmsg(canal, msg)
        else:
            connection.privmsg(canal, auteur + " ce n'est pas a toi de jouer.")
    else:
        connection.privmsg(canal, auteur + " usage: attack <nom du sort a utiliser>")
