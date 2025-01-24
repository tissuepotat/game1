import time
import random

# Game variables
enemies = ["Hyperion", "Cyclops", "Kronos", "Minotaur"]
titans = random.choice(enemies)
items = []
defeated_enemy = 0
player_hp = 100

def health_bar(health):
    bar_length = 20
    complete_size = int(bar_length * health / 100)
    bar = "#" * complete_size + "-" * (bar_length - complete_size)
    print(f"Health: [{bar}] {health}/100")

def timersleep(message):
    print(message)
    time.sleep(2)

def restart_game():
    global player_hp, defeated_enemy, titans
    player_hp = 100
    defeated_enemy = 0
    items.clear()
    titans = random.choice(enemies)
    timersleep("GAME OVER!\n")
    response = input("Try again? (yes/no): ").lower()
    if response == 'yes':
        game()
    elif response == 'no':
        timersleep("Thank you for playing, PercyPy!")
        exit()
    else:
        timersleep("Invalid choice. Restarting...\n")
        restart_game()

def intro():
    timersleep("The Half-Bloods have a pine-scented atmosphere, with distant sounds\n"
                "of water crashing on the shore of Long Island.\n")
    timersleep("They say there is a runaway monster that has gotten away from the\n"
              "Labyrinth and has been causing trouble just at the borders of the camp.\n")
    timersleep("Before you stands the Big House, columns gleaming in the sun, while to\n"
                "your right is the entrance into the forest, dark and shadowy, with rustling leaves.\n")
    timersleep("In your hand remains the celestial bronze dagger, its surface glowing faintly with power.\n")

def startroom():
    global player_hp
    health_bar(player_hp)
    timersleep("Press 'E' to knock on the door of the Big House.\n"
               "Press 'A' to look closely into the forest.\n"
               "Press 'L' to enter the Labyrinth.\n"
               "Press 'P' to use potion.\n")
    response_2 = input("Enter 'E', 'A', 'L', or 'P': ").upper()

    if response_2 == 'E':
        timersleep("You stand before the mysterious house, its door slightly ajar but ominously quiet.\n")
        big_house()
    elif response_2 == 'A':
        timersleep("You stand before a dark, ominous forest, its entrance shrouded in darkness.\n")
        forest()
    elif response_2 == 'L':
        timersleep("You step into the Labyrinth, a twisting maze of stone and shadows.\n")
        labyrinth()
    elif response_2 == 'P':
        potion()
        startroom()
    else:
        timersleep("Invalid choice. Try again.\n")
        startroom()

def big_house():
    global player_hp
    timersleep(f"You're about to knock when the door creaks open... a {titans}!\n"
               f"A giant, its massive arms and legs glinting in the light.\n")
    timersleep(f"Oh no! This is {titans}'s hiding spot!\n")
    health_bar(player_hp)

    if "Riptide" in items:
        timersleep(f"As {titans} moves to attack, you unsheath Riptide, your trusted celestial bronze sword.\n")
        timersleep("With swift strikes, you defeat the monster, sending it back to Tartarus!\n")
        restart_game()
    else:
        timersleep("You feel underprepared, armed only with a small celestial dagger.\n")
        response_3 = input("Would you like to (1) Fight or (2) Run away? ").strip()

        if response_3 == '1':
            player_hp -= 80
            health_bar(player_hp)
            timersleep(f"You did your best, lunging at {titans} with your dagger...\n"
                       f"But it overpowers you.\n")
            if player_hp <= 0:
                timersleep("You have been defeated!\n")
                restart_game()
            else:
                timersleep("You manage to escape back to the start room, heavily wounded.\n")
                startroom()
        elif response_3 == '2':
            timersleep("You quickly turn and run back into the start room, your heart pounding loudly.\n")
            startroom()
        else:
            timersleep("Invalid choice. The monster strikes while you hesitate!\n")
            player_hp = 0
            health_bar(player_hp)
            restart_game()

def forest():
    if "Riptide" in items:
        timersleep("You've been here before and already claimed the useful item.\n"
                   "The forest is now eerily silent. You return to the start room.\n")
        startroom()
    else:
        timersleep("You enter the forest cautiously, moving with more stealth,\n"
                  "for now, the shadows are twisting as if alive...\n"
                   "Your eye catches a glint of celestial bronze behind a rock.\n"
                   "You have found Riptide, a legendary celestial bronze sword!\n"
                   " You dump your little dagger for the might Riptide.\n")
        items.append("Riptide")
        timersleep("Meanwhile, you go exploring, and you find a bottle of Nectar close by. This ought to heal you!  \n")
        items.append("Nectar(For Healing)")
        timersleep("You return to the start room with Riptide and Nectar.\n")
        startroom()

def labyrinth():
    global player_hp
    timersleep("You explore the curving passages of the Labyrinth, the atmosphere heavy with the smell of old stones.\n")
    timersleep("A Drakon materializes! Its golden scales glimmer in the dim light.\n")

    response_4 = input("Press (1) to Fight or (2) to Run: ").strip()
    if response_4 == '1':
        player_hp -= random.randint(10, 30)
        health_bar(player_hp)
        if player_hp <= 0:
            timersleep("The Drakon is stronger than you.\n")
            restart_game()
        else:
            timersleep("You kill the Drakon and push deeper into the Labyrinth!\n")
            labyrinth_2()
    elif response_4 == '2':
        timersleep("You leave the Labyrinth and go back to the starting room.\n")
        startroom()
    else:
        timersleep("Invalid choice. Try again.\n")
        labyrinth()

def labyrinth_2():
    global player_hp
    timersleep(f"When you finally arrive at the center of the Labyrinth, you find {titans} himself!\n")
    response_5 = input(f"Press (1) to Fight {titans} or (2) to Run: ").strip()

    if response_5 == '1':
        player_hp -= random.randint(20, 45)
        health_bar(player_hp)
        if player_hp <= 0:
            timersleep(f"{titans} is too strong. You have been defeated!\n")
            restart_game()
        else:
            timersleep(f"With a final, desperate strike, you defeat {titans}!\n")
            restart_game()
    elif response_5 == '2':
        player_hp -= random.randint(5, 10)
        health_bar(player_hp)
        timersleep("You retreat to the start room, barely escaping with your life.\n")
        startroom()
    else:
        timersleep("Invalid choice. Try again.\n")
        labyrinth_2()

def potion():
    global player_hp
    if "Nectar(For Healing)" in items:
        if player_hp == 100:
            timersleep("Your health is already full! You don't need to use Nectar.\n")
        else:
            items.remove("Nectar(For Healing)")
            restored_health = min(player_hp + 80, 100) - player_hp
            player_hp = min(player_hp + 80, 100)
            timersleep(f"You drank Nectar and restored {restored_health} health points!\n")
            health_bar(player_hp)
    else:
        timersleep("You don't have any Nectar left!\n")


def game():
    intro()
    startroom()

if __name__ == "__main__":
    game()