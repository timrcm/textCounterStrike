import random
import time

import outcomes 

equipmentTerrorist = ['AK47', 'Desert Eagle', 'Explosive Grenade']

def start():
    print("""
    You are on the Terrorist team.
    Before proceeding, know that you are equipped with:
    """)

    for e in equipmentTerrorist:
        print(e, end="\n")

    print("""
    What shall be your course of action?
    1. Charge forwards alone with an AK47, spraying wildly
    2. Plant the bomb, ignoring your team
    3. Follow the team \n
    """)

    proceed = input("> ")

    if "charge" in proceed or "AK47" in proceed or "spray" in proceed or "1" in proceed:
        ak47Accuracy = random.randrange(1, 10, 1)
        if ak47Accuracy > 1:
            outcomes.victory("Terrorists", f"Mohammad guided your bullets directly in to {ak47Accuracy} CT heads.")
        else:
            print(f"You sprayed wildly and popped a CT in the dome, but ultimately needed to reload and died.")
            time.sleep(2)
            print("The bomb has been planted.")
            outcomes.bombDetonates()
            outcomes.victory("Terrorists", "The bomb has detonated, ensuring that you died for the cause.")

    elif "plant" in proceed or "bomb" in proceed or "2" in proceed:
        outcomes.bombDetonates()
        outcomes.victory("Terrorists", "You have died for the cause.")

    elif "follow" in proceed or "3" in proceed:
        outcomes.death(outcomes.killed)

    else:
        outcomes.confused()