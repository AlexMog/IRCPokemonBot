#!/usr/bin/env python2

def accept(connection, canal, auteur, cmds, canalobj, mogbot):
    user = mogbot.getUserManager().findUser(auteur)
    if user == False:
        connection.privmsg(canal, auteur + " je ne te trouve pas dans la base de donnees :( - erreur 500")
        return
    if user.battle == None:
        connection.privmsg(canal, auteur + " vous n'avez pas recu d'invitations.")
        return
    elif user.battle.accepted:
        connection.privmsg(canal, auteur + " vous etes deja en combat.")
        return
    user.battle.accepted = True
    connection.privmsg(canal, auteur + " a accepte le duel contre " + user.battle.user1.username + ". Que le combat commence!")
