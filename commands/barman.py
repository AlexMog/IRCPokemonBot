#!/usr/bin/env python2

boissons = [
    ("pastis", 2, "%s, et un pastaga! Un!", "%s offre un pastis a %s"),
    ("vodka", 4, "%s, et une vodka pour un homme! Une!", "%s offre une vodka a %s"),
    ("biere", 1, "Voila pour toi, %s, une bonne biere!", "%s offre une biere a %s"),
    ("coca", 0, "Un coca %s? Petite nature!", "%s offre un coca (de tapette) a %s")
    ]

def findboisson(boisson, ident):
    for i in range(len(boissons)):
        if boissons[i][0].lower() == boisson.lower():
            return boissons[i][ident]
    return "Je n'ai pas trouve ta boisson %s, :("

def barman(connection, canal, auteur, cmds, canalobj, mogbot):
    if len(cmds) > 2:
        if cmds[2] == "donne":
            if len(cmds) > 4:
                connection.privmsg(canal, findboisson(cmds[3], 3) % (auteur, cmds[4]))
        else:
            connection.privmsg(canal, findboisson(cmds[2], 2) % auteur)
    else:
        menu = "%s tu veux boire quoi? Voila le menu: "
        for i in range(len(boissons)):
            if i != 0:
                menu += ", "
            menu += boissons[i][0]
        connection.privmsg(canal, menu % auteur)
