import random
import time

killedReason = [
    'You have been shot in the head with an AWP.',
    'Some crazy bastard ran around the corner with an AK47 and instantaneously mowed you down.',
    'A flashbang went off in your face, and a knife was subsequently stabbed in to your back.',
    'You tripped on several grenades.',
    'Someone slowly pecked away at your health with an uzi while you were reloading.',
    'You have recieved a .50 cal shell from a desert eagle between the eyes.',
    'A noob crouched in a corner with a pump shotgun ended your spree.'
]

killed = random.choice(killedReason)

def death(killed):
        print(killed, "\nYou are very dead and lose the round.\n")
        next_round()

def confused():
    death("You wander around indecisive and confused until sniped in the head.")

def bombDetonates():
    print("The bomb has been planted.")
    x = 3
    while x != 0:
        print(f"{x}...")
        time.sleep(1)
        x -= 1
    print("*" * 100)
    print("=" * 100)
    print("!" * 100)
    print("\nA massive explosion occurs.\n")
    time.sleep(1)

def victory(team, reason):
    print(reason, team, "win.")
    next_round()

def next_round():
    from main import start_next_round
    start_next_round()