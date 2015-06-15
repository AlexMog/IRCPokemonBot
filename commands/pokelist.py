#!/usr/bin/env python2

from classes.Pokemons import Pokemon

def pokelist(connection, canal, auteur, cmds, canalobj, mogbot):
    user = mogbot.getUserManager().findUser(auteur)
    if user == False:
        connection.privmsg(canal, auteur + " je ne te trouve pas dans la base de donnees :( - erreur 500")
        return
    pokemons = ""
    for elem in user.pokemons:
        if len(pokemons) != 0:
            pokemons += ", "
        pokemons += "(pokeId(" + str(elem.pokeid) + ") - " + elem.name + " - level(" + str(elem.level) + "))"
    connection.privmsg(canal, "Liste des pokemons de " + auteur + ": " + pokemons)
