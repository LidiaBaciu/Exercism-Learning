import random

class Character:

    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = modifier(self.constitution) + 10

    def ability(self):
        return sum(sorted([random.randint(1, 6) for i in range(0, 4)], reverse=True)[0:3])

def modifier(constitution):
    return (constitution - 10) // 2