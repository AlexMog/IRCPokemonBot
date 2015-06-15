#!/usr/bin/env python2

def heal(connection, canal, auteur, cmds, canalobj, mogbot):
    user = mogbot.getUserManager().findUser(auteur)
    if user == False:
        connection.privmsg(canal, auteur + " je ne te trouve pas dans la base de donnees :( - erreur 500")
        return
    if user.battle != None:
        connection.privmsg(canal, auteur + " tu ne peux pas soigner tes pokemons en combat.")
        return
    for elem in user.pokemons:
        elem.life = elem.getMaxLife()
    connection.privmsg(canal, "Tous les pokemons de " + auteur + " ont ete soignes")
