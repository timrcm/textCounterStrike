import random
import time

import outcomes

equipmentCounterTerrorist = ['M416', 'Desert Eagle', 'Explosive Grenade', 'Defuse Kit']

def welcome():
    print("""
    You are on the Counter-Terrorist team.
    Before proceeding, know that you are equipped with:
    """)

    for e in equipmentCounterTerrorist:
        print(e, end="\n")

def round():

    print("""
    Round starting. What shall be your course of action?
    1. Charge forwards alone with your M416, spraying wildly
    2. Defend the bombsites
    3. Follow your team
    """)

    proceed = input("> ")

    if "charge" in proceed or "M416" in proceed or "M4" in proceed or "spray" in proceed or "1" in proceed:
        m4Accuracy = random.randrange(1, 10, 1)
        if m4Accuracy >= 8:
            print(f"Your M4 somehow managed to not suck and mowed down {m4Accuracy} people.")
            print("Counter-Terrorists wi...")
            time.sleep(1)
            print("wait, what's this?!")
            time.sleep(1)
            outcomes.bombDetonates()
            outcomes.victory("Terrorists", "The bomb has detonated.")
        else:
            print(f"You sprayed the M4 wildly, causing multiple {m4Accuracy} damage 'headshots' and killing no one.")
            outcomes.death(outcomes.killed)

    elif "defend" in proceed or "bombsites" in proceed or "bomb" in proceed or "2" in proceed:
        outcomes.bombDetonates()
        print("You failed to prevent the bomb from being planted.")
        outcomes.death(outcomes.killed)

    elif "follow" in proceed or "team" in proceed or "3" in proceed:
        outcomes.death(outcomes.killed)

    else:
        outcomes.confused()