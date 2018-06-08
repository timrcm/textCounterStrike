# Counter-Strike: Boring Edition
# 05/25/2018
# No sobriety was involved in the creation of this script

import random
import time

equipmentTerrorist = ['AK47', 'Desert Eagle', 'Explosive Grenade']
equipmentCounterTerrorist = ['M416', 'Desert Eagle', 'Explosive Grenade', 'Defuse Kit']
killedReason = [
    'You have been shot in the head with an AWP.',
    'Some crazy bastard ran around the corner with an AK47 and instantaneously mowed you down.',
    'A flashbang went off in your face, and a knife was subsequently stabbed in to your back.',
    'You tripped on several grenades.',
    'Someone slowly pecked away at your health with an uzi while you were reloading.',
    'You have recieved a .50 cal shell from a desert eagle between the eyes.',
    'A noob crouched in a corner with a pump shotgun ended your spree.'
]
allMaps = ['de_dust', 'de_dust2', 'de_inferno', 'de_aztec', 'de_rats', 'de_abottabad', 'de_nuke', 'de_iceworld']

killed = random.choice(killedReason)
map = random.choice(allMaps)

def victory(team, reason):
    print(reason, team, "win.")
    exit(0)

def death(reason):
    print(reason, "\nYou are very dead and lose the round.\n")
    exit(0)

def start():   
    print(f"""
    You have joined a Counter-Strike server on the {map} map.
    Select a team:
    1. Terrorist
    2. Counter-Terrorist
    3. Spectator
    """)

    while True:
        join_as = input("> ")
        if "terrorist" in join_as or "Terrorist" in join_as or "1" in join_as or "T" in join_as:
            startTerrorist()

        elif "counter-terrorist" in join_as or "Counter-Terrorist" in join_as or "2" in join_as or "CT" in join_as:
            startCounterTerrorist()

        elif "spectator" in join_as or "3" in join_as or "spec" in join_as:
            startSpectator()

        else:
            print("I have no idea what team you're asking to join.")

def startSpectator():
    x = 0
    while x != 3:
        print("." * 10)
        time.sleep(1)
        x += 1
    print("\nYou have been kicked for being AFK and must join another server.")
    start()

def startTerrorist():
    print("""
    You have joined the Terrorist team.
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
            victory("Terrorists", f"Mohammad guided your bullets directly in to {ak47Accuracy} CT heads.")
        else:
            print(f"You sprayed wildly and popped a CT in the dome, but ultimately needed to reload and died.")
            time.sleep(2)
            print("The bomb has been planted.")
            bombDetonates()
            victory("Terrorists", "The bomb has detonated, ensuring that you died for the cause.")

    elif "plant" in proceed or "bomb" in proceed or "2" in proceed:
        bombDetonates()
        victory("Terrorists", "You have died for the cause.")

    elif "follow" in proceed or "3" in proceed:
        death(killed)

    else:
        confused()

def startCounterTerrorist():
    print("""
    You have joined the Counter-Terrorist team.
    Before proceeding, know that you are equipped with:
    """)

    for e in equipmentCounterTerrorist:
        print(e, end="\n")

    print("""
    What shall be your course of action?
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
            bombDetonates()
            victory("Terrorists", "The bomb has detonated.")
        else:
            print(f"You sprayed the M4 wildly, causing multiple {m4Accuracy} damage 'headshots' and killing no one.")
            death(killed)

    elif "defend" in proceed or "bombsites" in proceed or "bomb" in proceed or "2" in proceed:
        bombDetonates()
        print("You failed to prevent the bomb from being planted.")
        death(killed)

    elif "follow" in proceed or "team" in proceed or "3" in proceed:
        death(killed)

    else:
        confused()


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

def confused():
    death("You wander around indecisive and confused until sniped in the head.")

start()
