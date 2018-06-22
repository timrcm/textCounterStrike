# Counter-Strike: Boring Edition
# 05/25/2018
# No sobriety was involved in the creation of this script

from random import choice, randint
from time import sleep

import config
import counterterrorist
import terrorist
import outcomes

allMaps = ['de_dust', 'de_dust2', 'de_inferno', 'de_aztec', 
            'de_rats', 'de_abottabad', 'de_nuke', 'de_iceworld']
config.csmap = choice(allMaps)

def start():

    config.rounds_left -= 1

    print(f"""
    You have joined a Counter-Strike server on the {config.csmap} map.
    Select a team:
    1. Terrorist
    2. Counter-Terrorist
    3. Spectator
    """)

    join_as = input("> ")
    if join_as == "1":
        config.team = 'Terrorist'
        terrorist.welcome()
        terrorist.round()

    elif join_as == "2":
        config.team = 'Counter-Terrorist'
        counterterrorist.welcome()
        counterterrorist.round()

    elif join_as == "3":
        config.team = 'Spectator'
        startSpectator()

    elif join_as == "exit":
        exit(0)

    else:
        print("I have no idea what team you're asking to join. You get to be a spectator.")
        startSpectator()

    
def start_next_round():
    
    # Give a 20% chance of being team-swapped 
    if config.stuck_team != 1:
        swap = randint(1, 10)
        if swap > 8:
            # Swap the team & change the config so that it can only occur once
            config.stuck_team = 1
            if config.team == 'Terrorist':
                config.team = 'Counter-Terrorist'
                print("\nYou have been auto-balanced to the CT team.\n")
            else:
                config.team = 'Terrorist'
                print("\nYou have been auto-balanced to the T team.\n")

    print(f"{config.wins} rounds won, {config.losses} rounds lost.")
    print(f"{config.rounds_left} rounds left until you get bored and don't want to continue.\n")

    while config.rounds_left != 0:
        if config.team == 'Terrorist':
            config.rounds_left -= 1
            terrorist.welcome()
            terrorist.round()
        elif config.team == 'Counter-Terrorist':
            config.rounds_left -= 1
            counterterrorist.welcome()
            counterterrorist.round()
        else: 
            print("Team checking error.")
            exit(1)
    
    print("\nThis effort grows intense. Hitting Alt+F4...")
    exit(0)

def startSpectator():
    x = 0
    while x != 3:
        print("." * 10)
        sleep(1)
        x += 1
    print("\nYou have been kicked for being AFK and must join another server.")
    start()

if __name__ == '__main__':
    start()