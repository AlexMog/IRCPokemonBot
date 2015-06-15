#!/usr/bin/env python2

def change(connection, canal, auteur, cmds, canalobj, mogbot):
    user = mogbot.getUserManager().findUser(auteur)
    if user == False:
        connection.privmsg(canal, auteur + " je ne te trouve pas dans la base de donnees :( - erreur 500")
        return

    if len(cmds) > 2:
        user.active_pokemon = user.getPokemonById(int(cmds[2])).pokeid
        connection.privmsg(canal, auteur + " pokemon change!")
