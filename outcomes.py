from random import shuffle
from time import sleep

import config

killedReason = [
    'You have been shot in the head with an AWP.',
    'Some crazy bastard ran around the corner with an AK47 and instantaneously mowed you down.',
    'A flashbang went off in your face, and a knife was subsequently stabbed in to your back.',
    'You tripped on several grenades.',
    'Someone slowly pecked away at your health with an uzi while you were reloading.',
    'You have recieved a .50 cal shell from a desert eagle between the eyes.',
    'A noob crouched in a corner with a pump shotgun ended your spree.'
]

killed = "None"

def death(killed):
        config.losses += 1
        shuffle(killedReason)
        killed = killedReason.pop()
        print(killed, "\nYou are very dead and lose the round.\n")
        next_round()

def confused():
    config.losses += 1
    print("You wander around indecisive and confused until sniped in the head.")
    next_round()

def bombDetonates():
    print("The bomb has been planted.")
    x = 3
    while x != 0:
        print(f"{x}...")
        sleep(1)
        x -= 1
    print("*" * 100)
    print("=" * 100)
    print("!" * 100)
    print("\nA massive explosion occurs.\n")
    sleep(1)

def victory(team, reason):
    config.wins += 1
    print(reason, team, "win.")
    next_round()

def next_round():
    from main import start_next_round
    start_next_round()

def banned():
    print("You have been banned from the server.")
    exit(0)