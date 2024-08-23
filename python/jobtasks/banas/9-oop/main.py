import random
import math


'''

game of warriors

example output:
sam attack paul dealing 9 dmg
paul is down to 10hp 
...
paul died
sam victorious
game over

algorithm:

    create 2 warrior objects with properties:
     name, health, shield, weapon
     capabilities:
     attack 
    start battle object that takes Warrior objects and uses their attack methods
'''

class Battle: 
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break
    
    @staticmethod 
    def getResult(warriorA, warriorB):
        warriorAatk = warriorA.attack()
        warriorBblock = warriorB.defense()
        damage = math.ceil(warriorAatk - warriorBblock)
        warriorB.health = warriorB.health - damage
        
        print("{} attack {} and deals {} dmg".format(warriorA.name, warriorB.name, damage))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has died and {} is Victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"

class Warrior: 

    def __init__(self, name="warrior", health=0, shield=0, weapon=0):
        self.name = name
        self.health = health
        self.shield = shield
        self.weapon = weapon

    def attack(self):
        weapon = self.weapon * (random.random() + .5)
        return weapon

    def defense(self):
        shield = self.shield * (random.random())
        return shield

       
def main():
    war1 = Warrior("war1", 50, 20, 10)
    war2 = Warrior("war2", 50, 20, 10)
    
    battle = Battle() 

    battle.startFight(war1, war2) 

main() 











