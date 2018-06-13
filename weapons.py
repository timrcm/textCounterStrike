import config

class Weapons(object):
    def __init__(self):
        self.ammo = 30

class AK47(Weapons):
    def __init__(self):
        self.accuracy = 8

class M416(Weapons):
    def __init__(self):
        self.accuracy = 6