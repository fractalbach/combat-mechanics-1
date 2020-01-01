
import math
import random


class Player:
   
    MAX_ATTACK = 100

    def __init__(self, attack=1, strength=1, defense=1):
        self.hp = 100
        self.attack = attack
        self.strength = strength
        self.defense = defense
    
    def hit():
        multiplier = (2 * MAX_ATTACK / self.attack) + random.random()
        multiplier = math.max(multiplier, 1)
        damage = multiplier * self.strength
        
    def isAlive():
        return (self.hp <= 0)


class Duel:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
       
    def displayHitpoints():
        hp1 = math.round(self.player1, 2)
        hp2 = math.round(self.player2, 2)
        print(f"[HITPOINTS] p1: {hp1}, p2: {hp2}")
        
    def step():
        dmg1 = self.player1.hit()
        dmg2 = self.player2.hit()
        print(f"p1 hits p2 for {math.round(dmg1,2)} damage!")
        print(f"p2 hits p1 for {math.round(dmg2,2)} damage!")
        p2.hp -= p1.hp
        p1.hp -= p2.hp
        self.displayHitpoints()
        
    def run():
        
    

if __name__ == "__main__":
    player1 = Player(10, 10, 1)
    player2 = Player(20, 20, 1)
    
    print("battle begins!")
    
    while player1.isAlive() and player2.isAlive():

        
    
    
