# Counter-Strike: Boring Edition
# 05/25/2018
# No sobriety was involved in the creation of this script

import random
import time

import terrorist
import counterterrorist

allMaps = ['de_dust', 'de_dust2', 'de_inferno', 'de_aztec', 
            'de_rats', 'de_abottabad', 'de_nuke', 'de_iceworld']
map = random.choice(allMaps)

team = None
rounds_left = 5

def start():   
    global team
    global rounds_left
    rounds_left -= 1

    print(f"""
    You have joined a Counter-Strike server on the {map} map.
    Select a team:
    1. Terrorist
    2. Counter-Terrorist
    3. Spectator
    """)

    join_as = input("> ")
    if "terrorist" or "Terrorist" or "1" or "T" in join_as:
        team = 'Terrorist'
        terrorist.start()

    elif "counter-terrorist" or "Counter-Terrorist" or "2" or "CT" in join_as:
        team = 'Counter-Terrorist'
        counterterrorist.start()

    elif "spectator" or "3" or "spec" in join_as:
        team = 'Spectator'
        startSpectator()

    elif "exit" in join_as:
        exit(0)

    else:
        print("I have no idea what team you're asking to join. You get to be a spectator.")
        startSpectator()

def start_next_round():
    global team 
    global rounds_left

    print("{} rounds left.".format(rounds_left))

    while rounds_left != 0:
        if team == 'Terrorist':
            rounds_left -= 1
            terrorist.start()
        elif team == 'Counter-Terrorist':
            rounds_left -= 1
            counterterrorist.start()
        else: 
            print("Error.")
            exit(1)
    
    print("This effort grows intense. Hitting Alt+F4...")
    exit(0)

def startSpectator():
    x = 0
    while x != 3:
        print("." * 10)
        time.sleep(1)
        x += 1
    print("\nYou have been kicked for being AFK and must join another server.")
    start()
