import random


def single_roll(number_of_sides):
    """
    Execute a single die roll.

    :param number_of_sides: int
    :precondition: number_of_sides > 0
    :postcondition: a random integer [1, number_of_sides]
    :return: int
    """

    return random.randint(1, number_of_sides)


# noinspection DuplicatedCode
def roll_die(number_of_rolls, number_of_sides):
    """
    Calculate sum of  die rolls.

    :param number_of_rolls: int
    :param number_of_sides: int
    :precondition: number_of_rolls [1, 3]
    :precondition: number_of_sides > 0
    :postcondition: calculate the sum of all the rolls
    :return: int
    >>> roll_die(0, 1)
    0
    >>> roll_die(1, 0)
    0
    """

    invalid_arg = False

    # Check both arguments, either one of them being 0 should return a 0
    if number_of_rolls == 0:
        invalid_arg = True

    if number_of_sides == 0:
        invalid_arg = True

    # If both arguments are > 0, roll and sum
    if invalid_arg:
        roll_sum = 0
    else:
        roll_sum = single_roll(number_of_sides)  # Since we know there's at least 1 roll, no need to enclose in an "if"
        number_of_sides = number_of_sides - 1

        # Rules are < 4 rolls, so subtraction will suffice to manage the iteration-size
        if number_of_sides:
            roll_sum = roll_sum + single_roll(number_of_sides)
            number_of_sides = number_of_sides - 1

        if number_of_sides:
            roll_sum = roll_sum + single_roll(number_of_sides)
            number_of_sides = number_of_sides - 1

    return roll_sum


def choose_inventory(inventory, selection):
    """
    Provide a random selection of inventory.

    :param inventory: list
    :param selection: int
    :precondition: selection is int, > 0
    :postcondition: generates a sorted, random selection of inventory
    :return: list of strings
    """

    gear_taken = []

    if len(inventory) == 0 or selection == 0:
        pass
    elif selection < 0:
        print("**********FOOL! You may not choose such a ridiculous number!!!. I shall take your life!**********")
        print("~bzzzzzzzt~")
    else:
        if selection > len(inventory):
            print("Getting greedy. Venger would be proud.")
            gear_taken = sorted(inventory)
        elif selection == len(inventory):
            gear_taken = sorted(inventory)
        else:
            iteration_count = 0  # Using this to manage to maximum number of iterations
            for i in range(0, selection):
                gear_choice = random.choice(inventory)

                if iteration_count > (selection * 15):
                    i = selection  # we've been at this long enough; break out
                else:
                    if gear_choice in gear_taken:
                        i = (i - 1)  # decrement i because we couldn't take this gear
                    else:
                        gear_taken.append(gear_choice)

                iteration_count = (iteration_count + 1)

            sorted(gear_taken)

            if len(gear_taken) < selection:
                gear_taken.append("Wha??? The fool fell asleep and short-changed me!")

    return gear_taken


def generate_vowel():
    """
    Return a randomly-selected vowel (incl. y).

    :postcondition: single vowel randomly selected
    :return: string
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    which_vowel = random.choice(vowels)

    return which_vowel


def generate_consonant():
    """
     Return a randomly-selected consonant (incl. y).

    :postcondition: single consonant randomly selected
    :return: string
    """
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                 'z']

    return random.choice(consonant)


def generate_syllable():
    """
    Generate a consonant-vowel pair

    :postcondition: consonant-vowel pair created
    :return: string
    """

    return generate_consonant() + generate_vowel()


def generate_name(syllables):
    """
    Generate string of consonant-vowel pairs.

    :param syllables: int, > 0
    :precondition: syllables is an int, > 0
    :postcondition: generates a syllables consonant-vowel pairs of length 2 * syllables
    :return: string
    """

    name = ""

    for i in range(0, syllables):
        name = name + generate_syllable()

    return name.title()


def create_character(name_length):
    """
    Generate a DnD character.

    :param name_length: int
    :precondition: name_length is int, > 0
    :postcondition: DnD character with a name & attributes (7 elements)
    :return: list
    """

    the_character = [(generate_name(name_length))]

    # create our attributes
    str_list = ["Strength", roll_die(3, 6)]
    dex_list = ["Dexterity", roll_die(3, 6)]
    con_list = ["Constitution", roll_die(3, 6)]
    int_list = ["Intelligence", roll_die(3, 6)]
    wis_list = ["Wisdom", roll_die(3, 6)]
    cha_list = ["Charisma", roll_die(3, 6)]

    # add the attributes
    the_character.append(str_list)
    the_character.append(dex_list)
    the_character.append(con_list)
    the_character.append(int_list)
    the_character.append(wis_list)
    the_character.append(cha_list)

    return the_character


def print_character(character):
    """
    Output DnD character details.

    :param character: list
    :precondition: a character list generated by create_character()
    :postcondition: output about your amazing character
    :return: none
    """

    print(character[0])

    for i in range(1, 7):
        ability = ""

        for j in range(len(character[i])):
            if j == 1:
                add_colon = ": "
            else:
                add_colon = " "

            ability = ability + add_colon + str(character[i][j])

        print(ability.strip() + "!")

    # This will be the inventory list, which should only be output if it exists
    if len(character) > 7:
        for eq in range(0, len(character[7])):
            print(character[7][eq])
