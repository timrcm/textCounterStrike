import config
import outcomes
import weapons

def welcome():
    print("You are on the Counter-Terrorist team.")


def round():

    weapons.choose_gun()
    if config.weapon.weapon_name == "AWP":
        outcomes.banned()
    spray_headshots = config.weapon.spray()
    snipe_headshots = config.weapon.snipe()

    print(f"""
    Round starting. What shall be your course of action?
    1. Charge forwards alone with your {config.weapon.name()}, spraying wildly
    2. Defend the bombsites 
    3. Follow the team
    4. Use your team as a human shield and crouch behind them, sniping heads with your {config.weapon.name()} \n
    """)

    proceed = input("> ")

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

    elif proceed == "4":
        if snipe_headshots > 6:
            outcomes.victory("Counter-Terrorists", f"Your M4 managed to not suck and popped {snipe_headshots} terrorists in the dome.")
        else:
            outcomes.death(outcomes.killed)

    else:
        outcomes.confused()