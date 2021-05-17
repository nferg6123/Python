import time
import random


def print_pause(message):
    print(message)
    time.sleep(0)


def valid_input(message, options):
    while True:
        response = input(message).lower()
        time.sleep(1)
        for option in options:
            if option == response:
                return response
        print_pause("I am sorry, I don't understand.")


def intro_game():
    print_pause("Welcome to the Adventure Game!")
    print_pause("Please answer all questions with y or n, for yes or no,\n"
                "unless given other options, then press enter. Enjoy!\n\n")


def intro_play(bad_guy, weapon):
    print_pause("One evening, you decide to head to the tavern down the road.")
    print_pause("While enjoying a bevvy, you overhear some of the locals.")
    print_pause(f"They are telling tales of a {bad_guy[2]} {bad_guy[3]}!")
    print_pause(f"One woman says she has seen them at a dreaded {bad_guy[0]}"
                f" down by the {bad_guy[1]}.\n")
    investigate(bad_guy, weapon)


def antagonist():
    misnomers = ["evil", "wicked", "terrible", "villianous", "foul"]
    descriptions = ["misunderstood", "good", "happy", "caring", "helpful"]
    villains = ["Wizard", "Hag", "Vampire", "Count", "Lich", "Giant"]
    biomes = ["field", "sea", "river"]
    abodes = ["van", "cave", "hut", "lair", "castle"]

    abode = random.choice(abodes)

    if abode == "van":
        biome = "river"
    else:
        biome = random.choice(biomes)

    villain = random.choice(villains)
    misnomer = random.choice(misnomers)
    description = random.choice(descriptions)
    antagonist = [abode, biome, misnomer, villain, description]

    return antagonist


def artifact():
    weapons = ["Staff", "Sword", "Mace", "Tome", "Axe", "Wand", "Ukelele"]
    ofs = ["Morthonius", "Osmanatar", "Horace", "Larraniksis", "Holman",
           "Refeldan"]

    artifact = [random.choice(weapons), random.choice(ofs)]

    return artifact


def fight(bad_guy, weapon):
    if weapon[0] == "dagger":
        print_pause(f"The {bad_guy[3]} easily blocks your first blow,"
                    " and overpowers you.")
        print_pause(f"The End.")
        play_again()
    else:
        print_pause(f"You are easily able to defeat the {bad_guy[3]}.")
        print_pause("You return to the town a hero, and"
                    " people sing your praises!")
        print_pause("The End.")
        play_again()


def friends(bad_guy, weapon):
    print_pause(f"You start talking with the {bad_guy[3]}.\n"
                "You realize he has been alone for a very long time, and\n"
                "people misjudge him since he does not come out anymore.")
    print_pause("After talking with the supposed villain for a few hours,\n"
                f"you find that they are not a {bad_guy[2]} {bad_guy[3]}\n"
                f"but a {bad_guy[4]} {bad_guy[3]}!")
    print_pause("You return to the town.")
    print_pause("You tell all of the people what you learned.")
    print_pause(f"The {bad_guy[3]} is invited to the town, and all is well!")
    print_pause("The End.")
    play_again()


def flee():
    print_pause("You run away!")
    print_pause("The End.")
    play_again()


def what_to_do(bad_guy, weapon):
    decisions = valid_input("Do you fight or flee?\n", ["fight", "flee",
                            "friend", "chat", "talk", "neither"])
    if "fight" == decisions:
        fight(bad_guy, weapon)
    elif "flee" == decisions:
        flee()
    else:
        friends(bad_guy, weapon)


def knocking(bad_guy, weapon):
    print_pause(f"After knocking, the {bad_guy[3]} opens the door.\n"
                "With some hesistation, they motion you forward.")
    enter = valid_input("Do you enter?\n", ["y", "n"])
    if "y" == enter:
        print_pause(f"You enter the {bad_guy[0]}.")
        what_to_do(bad_guy, weapon)
    if "n" == enter:
        print_pause(f"You stand at the entrance of the {bad_guy[0]}.")
        what_to_do(bad_guy, weapon)


def investigate(bad_guy, weapon):
    investigate = valid_input("Would you like to investigate?\n", ["y", "n"])
    if "y" == investigate:
        get_artifact = valid_input("\nYou currently have your old dagger on"
                                   " you.\n"
                                   f"Your famed {weapon[0]} of {weapon[1]} is"
                                   " back at your house.\n"
                                   "But that's in the other direction! Would"
                                   " you like to retrieve it?\n", ["y", "n"])
        if "y" == get_artifact:
            print_pause(f"You head back home and pick up your {weapon[0]}.")
            print_pause(f"You then go to the {bad_guy[0]}"
                        f" by the {bad_guy[1]}.")
            knocking(bad_guy, weapon)
        if "n" == get_artifact:
            weapon = ["dagger", "nothing"]
            print_pause(f"You head to the {bad_guy[0]}"
                        f" by the the {bad_guy[1]}.")
            print_pause("You stand at the entrance,"
                        " and put on your brave face.")
            knocking(bad_guy, weapon)
    else:
        print_pause("You head back to your house,"
                    " and forget about what you heard")
        play_again()


def play_again():
    play = valid_input("\nWould you like to play again?\n", ["y", "n"])

    if "n" == play:
        print("Thank you for playing!")
    else:
        play_game()


def play_game():
    bad_guy = antagonist()
    weapon = artifact()
    intro_play(bad_guy, weapon)


intro_game()
play_game()
