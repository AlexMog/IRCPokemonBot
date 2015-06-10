#!/usr/bin/env python2

import sys
import irclib
import ircbot
import random
import importlib
from User import *

class MogBot(ircbot.SingleServerIRCBot):
    def __init__(self, server, port, nickname, target, commandstarter, password):
        ircbot.SingleServerIRCBot.__init__(self, [(server, port, password)], nickname, "MogBot")
        self.target = target
        self.commandstarter = commandstarter
        self.modules = []
        self.userManager = UserManager()

    def getUserManager(self):
        return self.userManager
    
    def on_welcome(self, connection, event):
        if irclib.is_channel(self.target):
            connection.join(self.target)
        else:
            print "Not a channel."
            sys.exit(0)
    
    def on_disconnect(self, connection, event):
        sys.exit(0)

    def on_join(self, connection, event):
        auteur = irclib.nm_to_n(event.source())
        canal = event.target()
        if auteur == connection.get_nickname():
            print "Bot joined the channel."
    
    def find_module(self, modulename):
        for i in range(len(self.modules)):
            if self.modules[i][0] == modulename:
                return self.modules[i][1]
        return False

    def reload_commands(self):
        print "Reloading commands..."
        for i in range(len(self.modules)):
            self.modules[i][1] = importlib.reload(self.modules[i][1])
        print "Commands reloaded."

    def on_pubmsg(self, connection, event):
        """ Reception d'un message du channel """
        auteur = irclib.nm_to_n(event.source())
        canal = event.target()
        canalobj = self.channels[event.target()]
        message = event.arguments()[0]
        if auteur != connection.get_nickname() and self.userManager.findUser(auteur) == False:
            self.userManager.addUser(User(auteur))
        print "<< " + auteur + " " + canal + " : " + message
        if connection.get_nickname().lower() in message.lower():
            self.on_msg_to_bot(connection, canal, auteur, message, canalobj)
        if message.startswith(self.commandstarter + " "):
            try:
                cmds = message.split(" ")
                if len(cmds) > 1:
                    cmd = cmds[1]
                    module = self.find_module(cmd)
                    if module == False:
                        print "Module '" + cmd + "' didn't exist. Adding it."
                        module = importlib.import_module('commands.%s' % cmd)
                        self.modules.append((cmd, module))
                    function = getattr(module, cmd)
                    function(connection, canal, auteur, cmds, canalobj, self)
            except Exception, e:
                print e

    def on_nicknameinuse(self, connection, event):
        print "Nickname in use!"
        self.connection.quit("Nickname in use!")
        
    def on_privmsg(self, connection, event):
        auteur = irclib.nm_to_n(event.source())
        message = event.arguments()[0]
        print "<<! " + auteur + " : " + message

    def on_msg_to_bot(self, connection, canal, auteur, message, canalobj):
        print "<<mtb " + auteur + " : " + message

    def on_kick(self, connection, event):
        if event.arguments()[0] == connection.get_nickname():
            print "Bot kicked!"
            connection.join(self.target)

def main():
    if len(sys.argv) < 4:
        print "Usage: " + sys.argv[0] + " <server[:port]> <botname> <target> [command starter(without !)] [password]"
        print "Target need to be a nickname, or a channel (starts with #)"
        print "The default command starter is !bot, it is used to interract with the bot"
        sys.exit(1)
    password = None
            
    commandstarter = "!bot"
    if len(sys.argv) > 4:
        commandstarter = "!" + sys.argv[4]
    if len(sys.argv) > 5:
        password = sys.argv[5]
    s = sys.argv[1].split(":", 1)
    server = s[0]
    if len(s) == 2:
        try:
            port = int(s[1])
        except ValueError:
            print "Error: Port need to be numeric!"
            sys.exit(1)
    else:
        port = 6667
    nickname = sys.argv[2]
    target = sys.argv[3]

    conn = MogBot(server, port, nickname, target, commandstarter, password)
    print "Starting bot..."
    conn.start()

if __name__ == "__main__":
    main()
