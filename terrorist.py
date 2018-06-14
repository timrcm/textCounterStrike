import random
import time

import outcomes 
import weapons

equipmentTerrorist = ['AK47', 'Desert Eagle', 'Explosive Grenade']

def welcome():
    print("""
    You are on the Terrorist team.
    Before proceeding, know that you are equipped with:
    """)

    for e in equipmentTerrorist:
        print(e, end=", ")

def round():

    print("""
    Round starting. What shall be your course of action?
    1. Charge forwards alone with an AK47, spraying wildly
    2. Plant the bomb, ignoring your team
    3. Follow the team \n
    """)

    proceed = input("> ")

    AK = weapons.AK47()
    spray_headshots = AK.spray()

    if proceed == "1":
        if spray_headshots == 0:
            outcomes.death(outcomes.killed)
        elif spray_headshots > 1:
            outcomes.victory("Terrorists", f"Mohammad guided your bullets directly in to {spray_headshots} CT heads.")
        else:
            print(f"You sprayed wildly and popped a CT in the dome, but ultimately needed to reload and died.")
            time.sleep(2)
            outcomes.bombDetonates()
            outcomes.victory("Terrorists", "The bomb has detonated, ensuring that you died for the cause.")

    elif proceed == "2":
        outcomes.bombDetonates()
        outcomes.victory("Terrorists", "You have died for the cause.")

    elif proceed == "3":
        outcomes.death(outcomes.killed)

    else:
        outcomes.confused()