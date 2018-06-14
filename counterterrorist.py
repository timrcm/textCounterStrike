import random
import time

import outcomes
import weapons

equipmentCounterTerrorist = ['M416', 'Desert Eagle', 'Explosive Grenade', 'Defuse Kit']

def welcome():
    print("""
    You are on the Counter-Terrorist team.
    Before proceeding, know that you are equipped with:
    """)

    for e in equipmentCounterTerrorist:
        print(e, end=", ")

def round():

    print("""
    Round starting. What shall be your course of action?
    1. Charge forwards alone with your M416, spraying wildly
    2. Defend the bombsites
    3. Follow your team
    """)

    proceed = input("> ")

    M4 = weapons.M416()
    spray_headshots = M4.spray()

    if proceed == "1":

        if spray_headshots >= 4:
            print(f"Your M4 somehow managed to not suck and mowed down {spray_headshots} people.")
            outcomes.victory("Counter-Terrorists", "All terrorists are dead.")
        else:
            print(f"You sprayed the M4 wildly, killing {spray_headshots} terrorists.")
            outcomes.death(outcomes.killed)

    elif proceed == "2":

        if spray_headshots >= 3:
            print(f"You killed {spray_headshots} terrorists at the bombsite.")
            outcomes.victory("Counter-Terrorists", "The bomb has been defused.")
        elif spray_headshots == 1 or spray_headshots == 2:    
            print(f"You popped {spray_headshots} in the dome, but ultimately failed to prevent the bomb from being planted.")
            outcomes.bombDetonates()
            outcomes.death(outcomes.killed)
        elif spray_headshots == 0:
            print("You have failed to get any kills.")
            outcomes.death(outcomes.killed)

    elif proceed == "3":
        outcomes.death(outcomes.killed)

    else:
        outcomes.confused()