#! /usr/bin/env python
import random
#import pdb

"""
Author : Allan Davis

Answer to question 3 for CCP Games

run: python dice_game.py
"""

class Die(object):
    """ Represent a die in the game"""
    def __init__(self):
        self.sides = 6
    
    def roll(self):
        self.value= 1 + random.randrange(self.sides)
        return self.value
    
class LoadedDie(Die):
    """ Represent a Cheater's Loaded die """
    def __init__(self, target):
        super(LoadedDie, self).__init__()
        self.target = target
    
    def roll(self):
        self.value = self.target
        return self.value
    
class Player(object):
    """ Represent a player in the system """
    def __init__(self, name):
        self.dice = [Die(), Die()]
        self.name = name
        
    
    def take_turn(self):
        """ Rolls the dice for the Player"""
        self.values = []
        for die in self.dice:
            self.values.append(die.roll())
    
    def print_roll(self):
        print "\t{name} rolled a {die1} and {die2}".format(
            name=self.name, die1=self.values[0], die2=self.values[1])
    
    def rolls_double(self):
        return self.values[0] == self.values[1]
    
    def get_value(self):
        sum = 0
        for value in self.values:
            sum += value
        return sum

class ComputerPlayer(Player):
    def __init__(self):
        super(ComputerPlayer, self).__init__("Computer")
        self.tries = 0
    
    def take_turn(self):
        """ Every other turn the dice get substuted with loaded dice """
        if (self.tries % 2) == 0 :
            target = Die().roll()
            self.dice = [LoadedDie(target), LoadedDie(target)]
        else:
            self.dice = [Die(), Die()]
        self.tries += 1
        return super(ComputerPlayer, self).take_turn()

class DiceGame(object):
    def setup_game(self):
        name = raw_input("Player 1 please enter your name: ")
        self.player1 = Player(name)
        self.player2 = ComputerPlayer()
    
    def evaluate_round(self):
        #pdb.set_trace()
        if self.player1.rolls_double() == self.player2.rolls_double() :
            if self.player1.get_value() > self.player2.get_value():
                winner = self.player1
            else:
                winner = self.player2
        
        elif self.player2.rolls_double():
            winner = self.player2
        else:
            winner = self.player1
        print 
        print "The winner is {0}".format(winner.name)
    
    def play_round(self):
        print "Lets Roll"
        print 
        self.player1.take_turn()
        self.player1.print_roll()
        self.player2.take_turn()
        self.player2.print_roll()
        self.evaluate_round()
        print
        return (raw_input("Do you want to play another round?(Y/n): ") == "Y")
    
    def start_game(self):
        
        print "Welcome to the Dice Game"
        #print intro
        self.setup_game()
        while self.play_round():
            self.player1, self.player2 = self.player2, self.player1
        print "Thank you for playing"

if __name__ == '__main__':
    DiceGame().start_game()
