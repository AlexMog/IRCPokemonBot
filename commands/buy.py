#!/usr/bin/env python2

from classes.Item import * 

def buy(connection, canal, auteur, cmds, canalobj, mogbot):
    user = mogbot.getUserManager().findUser(auteur)
    if user == False:
        connection.privmsg(canal, auteur + " je ne te trouve pas dans la base de donnees :( - erreur 500")
        return
    if len(cmds) < 3:
        #User ask list
        tosell = ""
        for elem in itemsManager.items:
            if len(tosell) != 0:
                tosell += ", "
            tosell += "(" + elem.name + ":" + str(elem.price) + "$)"
        connection.privmsg(canal, auteur + " j'ai a vendre: " + tosell)
    else:
        itemName = cmds[2]
        item = itemsManager.getItem(itemName)
        if item == False:
            connection.privmsg(canal, auteur + " je ne trouve pas ton item :(")
        else:
            if user.getMoney() >= item.price:
                uItem = user.getItem(item.name)
                cnt = 0
                if uItem != False:
                    cnt = uItem[1]
                cnt += 1
                user.setItem(item.name, cnt)
                user.setMoney(user.getMoney() - item.price)
                connection.privmsg(canal, auteur + " un " + item.name + " a ete rajoute a ton inventaire. Il te reste " + str(user.getMoney()) + "$")
            else:
                connection.privmsg(canal, auteur + " tu n'a pas assez d'argent :(")
        
