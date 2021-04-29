import random, string
from random import randint

letters = string.ascii_uppercase

class Robot:
    def __init__(self):
        self.generateName()

    def generateName(self):
        random.seed()
        #empty the name
        name = ''
        # format like: RX837 or BC811
        name += random.choice(letters)
        name += random.choice(letters)
        name += str(randint(100, 999))
        self.name = name

    def reset(self):
        self.generateName()
