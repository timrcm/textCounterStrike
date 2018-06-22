from random import randint
import webbrowser

import config
import outcomes

class Weapons(object):
    def __init__(self):
        self.accuracy = 0
        self.ammo = 0
        self.weapon_name = 'Not chosen'

# When spraying, decrease accuracy by 75% and multiply the accuracy percentage
# by the number of available shells. This is the max number of headshots. 
# Pass that value to randint to get the number of headshots achieved. 
    def spray(self):
        self.sprayaccuracy = self.accuracy * 0.25
        self.maxheadshots = int(self.sprayaccuracy * self.ammo)
        self.headshots = randint(0, self.maxheadshots)
        return self.headshots

    def snipe(self):
        self.snipeaccuracy = self.accuracy * 0.50
        self.maxheadshots = int(self.snipeaccuracy * self.ammo)
        self.headshots = randint(0, self.maxheadshots)
        return self.headshots

    def name(self):
        return self.weapon_name
        

class AK47(Weapons):
    def __init__(self):
        self.weapon_name = "AK47"
        self.accuracy = config.ak_accuracy
        self.ammo = config.ak_ammo
        
class M416(Weapons):
    def __init__(self):
        self.weapon_name = "M416"
        self.accuracy = config.m4_accuracy
        self.ammo = config.m4_ammo

class M249(Weapons):
    def __init__(self):
        self.weapon_name = "M249"
        self.accuracy = config.m249_accuracy
        self.ammo = config.m249_ammo

class Deagle(Weapons):
    def __init__(self):
        self.weapon_name = "Desert Eagle"
        self.accuracy = config.deagle_accuracy
        self.ammo = config.deagle_ammo

class AWP(Weapons):
    def __init__(self):
        self.weapon_name = "AWP"
        self.accuracy = config.awp_accuracy
        self.ammo = config.awp_ammo

def choose_gun():

    if config.team == "Terrorist":
        config.team_assault_rifle = "AK47"
    elif config.team == "Counter-Terrorist":
        config.team_assault_rifle = "M416"

    print(f"""
            What weapon will be your primary?
            1. {config.team_assault_rifle}
            2. M249
            3. Desert Eagle
            4. AWP
        """)
    config.weapon = input("> ")

    if config.weapon == "1":
        if config.team == "Terrorist":
            config.weapon = AK47()
        elif config.team =="Counter-Terrorist":
            config.weapon = M416()
    elif config.weapon == "2":
        config.weapon = M249()
    elif config.weapon == "3":
        config.weapon = Deagle()
    elif config.weapon == "4":
        config.weapon = AWP()
        webbrowser.open('https://www.youtube.com/watch?v=lXMskKTw3Bc')
        outcomes.banned()
    else:
        outcomes.confused()