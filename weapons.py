import config
import random

class Weapons(object):
    def __init__(self):
        self.accuracy = 0
        self.ammo = 0

# When spraying, decrease accuracy by 75% and multiply the accuracy percentage
# by the number of available shells. This is the max number of headshots. 
# Pass that value to randint to get the number of headshots achieved. 
    def spray(self):
        self.sprayaccuracy = self.accuracy * 0.25
        self.maxheadshots = int(self.sprayaccuracy * self.ammo)
        self.headshots = random.randint(0, self.maxheadshots)

        return self.headshots

class AK47(Weapons):
    def __init__(self):
        self.accuracy = config.ak_accuracy
        self.ammo = config.ak_ammo
        
class M416(Weapons):
    def __init__(self):
        self.accuracy = config.m4_accuracy
        self.ammo = config.m4_ammo
