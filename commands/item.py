#!/usr/bin/env python2

from classes.Item import *

def item(connection, canal, auteur, cmds, canalobj, mogbot):
    user = mogbot.getUserManager().findUser(auteur)
    if user == False:
        connection.privmsg(canal, auteur + " je ne te trouve pas dans la base de donnees :( - erreur 500")
        return
    battle = user.battle
    if battle is None or battle.accepted == False:
        connection.privmsg(canal, auteur + " tu n'a aucun combat en cours.")
        return
    if battle.turn.username != auteur:
        connection.privmsg(canal, auteur + " ce n'est pas ton tour.")
        return

    if len(cmds) > 2:
        item = user.getItem(cmds[2])
        if item == False or item[1] == 0:
            connection.privmsg(canal, auteur + " vous n'avez pas cet item.")
            return
        itemObj = itemsManager.getItem(item[0])
        msg = itemObj.use(battle)
        connection.privmsg(canal, msg)
        battle.itemUsed()
        msg = battle.nextStep()
        if msg != False:
            connection.privmsg(canal, msg)
    else:
        items = ""
        for elem in user.items:
            if elem[1] > 0:
                if len(items) > 0:
                    items += ", "
                items += "(" + elem[0] + ", " + str(elem[1]) + ")"
        connection.privmsg(canal, auteur + " vos items: " + items)

