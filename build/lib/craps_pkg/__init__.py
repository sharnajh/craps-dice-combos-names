import random

dice_combos = {
    'Snake Eyes': [1, 1],
    'Australian yo': [1, 2],
    'Little Joe from Kokomo': [1, 3],
    'No field five': [1, 4],
    'Easy 6': [1, 5],
    "Six one you're done": [1, 6],
    'Ace caught a deuce': [2, 1],
    'Ballerina': [2, 2],
    'The fever': [2, 3],
    'Jimmie Hicks': [2, 4],
    'Bennie Blue': [2, 5],
    'Easy eight!': [2, 6],
    'Easy four': [3, 1],
    'Michael Jordan': [3, 2],
    'Brooklyn Forest': [3, 3],
    'Big Red': [3, 4],
    'Eighter from Decatur': [3, 5],
    'Nina from Pasadena': [3, 6],
    'Little Pheobe': [4, 1],
    'Lumber number': [4, 2],
    'Skinny McKinney': [4, 3],
    'Square pair': [4, 4],
    'Railroad nine': [4, 5],
    'Big one on the end': [4, 6],
    'Sixie from Dixie': [5, 1],
    'Skinny Dugan': [5, 2],
    'Easy eight!!': [5, 3],
    'Jesse James': [5, 4],
    'Puppy paws': [5, 5],
    'Yo': [5, 6],
    'The Devil': [6, 1],
    'Easy eight!!!': [6, 2],
    'Lou Brown': [6, 3],
    'Tennessee': [6, 4],
    'Six five no jive': [6, 5],
    'Midnight': [6, 6]
}


def check_combo(dice_pair):
    for nickname, combo in dice_combos.items():
        if dice_pair == combo:
            return nickname


def craps_roll():
    dice_pair = []
    dice_pair.append(random.randint(1, 6))
    dice_pair.append(random.randint(1, 6))
    combo_name = check_combo(dice_pair)
    return {
        "dice_pair": dice_pair,
        "nickname": combo_name
    }


def get_combo_name(dice_pair):
    return check_combo(dice_pair)

def get_dice_combos():
    return dice_combos
