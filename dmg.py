
import math
import random


class Player:
   
    MAX_ATTACK = 100
    MAX_STRENGTH = 100

    def __init__(self, attack=1, strength=1, defense=1):
        self.baseHitpoints = 100
        self.hp = 100
        self.attack = attack
        self.strength = strength
        self.defense = defense
    
    def hit(self):
        multiplier = (self.attack / self.MAX_ATTACK) + random.random()
        multiplier = min(multiplier, 1)
        effectiveStrength = (30 + self.strength) / (self.MAX_STRENGTH) * random.random()
        damage = multiplier * effectiveStrength * 10
        return damage
        
    def isAlive(self):
        return (self.hp > 0)
        
    def __repr__(self):
        return f"HP={self.hp}, ATK={self.attack}, STR={self.strength}, DEF={self.defense}"




class Duel:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.silent_mode = False
       
    def displayHitpoints(self):
        hp1 = self.player1.hp
        hp2 = self.player2.hp
        print(
            f"[HITPOINTS]"
            f"PLAYER1: {self.player1.hp:5.2f},  "
            f"PLAYER2: {self.player2.hp:5.2f}"
        )
        
    def displayStats(self):
        print(f"[STATS][PLAYER 1]: {player1}")
        print(f"[STATS][PLAYER 2]: {player2}")
    
    def displayDefeatMessage(self):
        if not self.player1.isAlive():
            print("player 1 has been defeated!")
        if not self.player2.isAlive():
            print("player 2 has been defeated!")   
    
    def step(self):
        p1 = self.player1
        p2 = self.player2
        dmg1 = p1.hit()
        dmg2 = p2.hit()
        p2.hp -= dmg1
        p1.hp -= dmg2
        
    def run(self):
    
        if not self.silent_mode: 
            print("___!!!  D U E L   B E G I N S   !!!___")
            self.displayStats()
            
        while self.player1.isAlive() and self.player2.isAlive():
            self.step()
            if not self.silent_mode: 
                self.displayHitpoints()
                
        if not self.silent_mode: 
            self.displayDefeatMessage()

    
    

if __name__ == "__main__":
    player1 = Player(15, 5, 1)
    player2 = Player(5, 10, 1)
    record = {
        1: 0,
        2: 0,
        "draws": 0,
    }
    
    for _ in range(1000):
        player1.hp = 10
        player2.hp = 10
        duel = Duel(player1, player2)
        duel.silent_mode = True
        duel.run()
        if player1.isAlive():
            record[1] += 1
        elif player2.isAlive():
            record[2] += 1
        else:
            record["draws"] += 1
        
    print(
        f"________________________________________________\n"
        f"================ DUEL RECORD ===================\n"
        f"________________________________________________\n"
        f"PLAYER 1 VICTORIES  : {record[1]}\n"
        f"PLAYER 2 VICTORIES  : {record[2]}\n"
        f"DUELS ENDED IN DRAW : {record['draws']}"
    )


        
    
        
