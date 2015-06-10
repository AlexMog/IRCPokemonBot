#!/usr/bin/env python2

class Battle:
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
        self.turn = user1
        self.notTurn = user2
        self.accepted = False
        self.finished = False
        self.auto = False
        self.turnCount = 1

    def fight(self, spell):
        attacker = self.turn.active_pokemon
        defender = self.notTurn.active_pokemon
        message = attacker.fight(spell, defender)
        if defender.life <= 0:
            message += defender.name + " n'a plus de points de vie. "
            if self.notTurn.hasAlivePokemon():
                message += self.notTurn.username + " doit invoquer un nouveau pokemon. "
            else:
                message += self.notTurn.username + " a perdu. " + self.turn.username + " a gagne. "
            message += attacker.name + " gagne " + str(attacker.calcGainedExp(defender)) + " points d'experience. "
            old = attacker.level
            attacker.gainExp(defender)
            if attacker.level != old:
                message += attacker.name + " passe niveau " + str(attacker.level) + "!"
            self.finished = True
        self.turn, self.notTurn = self.notTurn, self.turn
        self.turnCount += 1
        return message
            
