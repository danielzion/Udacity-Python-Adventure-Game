import time
import random
import string


def typewritter_simulator(messages):
    for char in messages:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')


def print_pause(messages, delay=1):
    typewritter_simulator(messages)
    time.sleep(delay)


def field():
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.\n")
    print_pause("Rumor has it that a wicked fairie is somewhere "
                "around here, and has been terrifying the nearby village.\n")
    print_pause("...\n")


def house(weapons, enemy):
    field()

    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.\n"
                "What would you like to do? \n")
    player_choice = validate_input(weapons, enemy,
                                   "(Please enter 1 or 2). \n", ['1', '2'])
    if player_choice == '1':
        first_choice(weapons, enemy)
    elif player_choice == '2':
        cave(weapons, enemy)
    # validate_player_choice(weapons, enemy)


def validate_input(weapons, enemy, prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option


def first_choice(weapons, enemy):
    print_pause('You approach the door of the house')
    print_pause(f"You are about to knock when the door opens "
                f"and out steps a {enemy}")
    print_pause(f"Eep! This is the {enemy} house!")
    print_pause("You feel a bit under-prepared for this."
                " What's with only having a tiny dagger")
    response = validate_input(weapons, enemy,
                              "Would you like to (1) fight or (2) "
                              "runaway?]\n", ['1', '2'])
    if response == '1':
        fight(weapons, enemy)

    elif response == '2':
        runaway(weapons, enemy)


def fight(weapons, enemy):
    if weapons in ['Sword', 'Axe', 'Spear']:
        print_pause(f"As the {enemy} moves to attack, you unsheath your"
                    f" new {weapons}")
        print_pause(f"The {weapons} of Ogorothshines brightly "
                    "in your hands as you brace yourself for the attack")
        print_pause(f"But the {enemy} takes one look at your "
                    "shining new toy and runs away")
        print_pause(f"You have rid the town of the {enemy}. "
                    "You are victorious")
        play_again()

    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {enemy}.")
        print_pause("You have been defeated!")
        play_again()


def runaway(weapons, enemy):
    print_pause("You run back into the field. Luckily, "
                "you don't seem to be followed.")
    house(weapons, enemy)


def play_again():
    response = input("Would you like to play again? (y/n)")
    if response == 'y':
        print_pause("Excellent! Restarting the game...\n")
        play_game()
    elif response == 'n':
        print_pause("Thanks for playing the game")


def cave(weapons, enemy):
    weapon = ['Sword', 'Axe', 'Spear']
    weapons = random.choice(weapon)
    print_pause("You peer cauiously into the cave, it turns out to "
                "be only a very small cave.")
    print_pause("Your eyes catches a glint of metal behind a rock.")
    print_pause(f"You have found the magical {weapons} of Ogoroth!")
    print_pause(f"You discard your silly old dagger and take "
                f"the {weapons} with you \n")
    print_pause("You walk back out of the field")
    house(weapons, enemy)


def play_game():
    weapons = ''
    enemies = ['troll', 'pirate', 'ghost', 'dragon', 'beast']
    enemy = random.choice(enemies)
    house(weapons, enemy)


play_game()
