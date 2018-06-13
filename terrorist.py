import random
import time

import outcomes 

equipmentTerrorist = ['AK47', 'Desert Eagle', 'Explosive Grenade']

def welcome():
    print("""
    You are on the Terrorist team.
    Before proceeding, know that you are equipped with:
    """)

    for e in equipmentTerrorist:
        print(e, end="\n")

def round():

    print("""
    Round starting. What shall be your course of action?
    1. Charge forwards alone with an AK47, spraying wildly
    2. Plant the bomb, ignoring your team
    3. Follow the team \n
    """)

    proceed = input("> ")

    if proceed == "1":
        ak47Accuracy = random.randrange(1, 10, 1)
        if ak47Accuracy > 1:
            outcomes.victory("Terrorists", f"Mohammad guided your bullets directly in to {ak47Accuracy} CT heads.")
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