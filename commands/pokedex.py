#!/usr/bin/env python2

from classes.Pokemons import *

def pokedex(connection, canal, auteur, cmds, canalobj, mogbot):
    user = mogbot.getUserManager().findUser(auteur)
    if user == False:
        connection.privmsg(canal, auteur + " je ne te trouve pas dans la base de donnees :( - erreur 500")
        return

    if len(cmds) > 2:
        pokemon = False
        if cmds[2].isdigit():
            #Its a pokeid
            pokemon = user.getPokemonById(int(cmds[2]))
        else:
            #Its a pokemon name
            pokemon = pokemonsManager.getFromName(cmds[2])
        if pokemon:
            connection.privmsg(canal, auteur + " POKEDEX: " + pokemon.str())
        else:
            connection.privmsg(canal, auteur + " pokemon " + cmds[2] + " introuvable.")
    else:
        connection.privmsg(canal, auteur + " usage: pokedex <nom du pokemon ou pokeId>")

