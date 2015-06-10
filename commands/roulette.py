#!/usr/bin/env python2

import random

def roulette(connection, canal, auteur, cmds, canalobj, mogbot):
    if random.randint(0, 6) == 1:
        connection.privmsg(canal, "*PAN* " + auteur + " est mort :'(")
        connection.kick(canal, auteur, "t'es mort :(")
    else:
        connection.privmsg(canal, "*CLICK* " + auteur + " a eu de la chance ;)")

