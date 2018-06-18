import random
import time

import config
import outcomes 
import weapons

def welcome():
    print("You are on the Terrorist team.")


def round():

    weapons.choose_gun()
    if config.weapon.weapon_name == "AWP":
        outcomes.banned()
    spray_headshots = config.weapon.spray()
    snipe_headshots = config.weapon.snipe()

    print(f"""
    Round starting. What shall be your course of action?
    1. Charge forwards alone with your {config.weapon.name()}, spraying wildly
    2. Plant the bomb, ignoring your team
    3. Follow the team
    4. Use your team as a human shield and crouch behind them, sniping heads with your {config.weapon.name()} \n
    """)

    proceed = input("> ")

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

    elif proceed == "4":
        if snipe_headshots > 4:
            outcomes.victory("Terrorists", f"Mohammad guided your bullets directly in to {snipe_headshots} CT heads.")
        else:
            outcomes.death(outcomes.killed)

    else:
        outcomes.confused()