# Craps Nicknames

Craps Nicknames is a tiny Python package that returns a randomized dice roll with it's associated craps nickname. The nicknames are based on the following chart by [Vital Vegas](https://vitalvegas.com/colorful-nicknames-dice-combinations-craps/):

![Craps Nicknames Charts](https://vitalvegas.com/wp-content/uploads/2015/02/craps_dice_rolls_updated.jpg)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install craps-pkg.

```python
pip3 install craps-dice-combos-names
```

## Usage

```python
import craps_pkg

craps_pkg.craps_roll()
# returns {
# "dice_pair": [1,2],
# "nickname": "Australian yo"
# }

craps_pkg.get_combo_name([2,2]) # returns "Ballerina"

craps_pkg.get_dice_combos()
# returns {
#   'Snake Eyes': [1, 1],
#   'Australian yo': [1, 2],
#   ...
#   'Six five no jive': [6, 5],
#   'Midnight': [6, 6]
# }
```

## Process

The following code was implemented once in order to automate the craps combinations dataset. I am just adding it to the documentation for future reference if this ever needs to happen again.

First, I manually stored all of the nicknames into an array in ascending order.

```
DICE_NICKS = [
    "Snake Eyes",
    "Australian yo",
    "Little Joe from Kokomo",
    "No field five",
    "Easy 6",
    "Six one you're done",
    "Ace caught a deuce",
    "Ballerina",
    "The fever",
    "Jimmie Hicks",
    "Bennie Blue",
    "Easy eight!",
    "Easy four",
    "Michael Jordan",
    "Brooklyn Forest",
    "Big Red",
    "Eighter from Decatur",
    "Nina from Pasadena",
    "Little Pheobe",
    "Lumber number",
    "Skinny McKinney",
    "Square pair",
    "Railroad nine",
    "Big one on the end",
    "Sixie from Dixie",
    "Skinny Dugan",
    "Easy eight!!",
    "Jesse James",
    "Puppy paws",
    "Yo",
    "The Devil",
    "Easy eight!!!",
    "Lou Brown",
    "Tennessee",
    "Six five no jive",
    "Midnight"
]
```

Then, I used the following loop function to create a dictionary of key-value pairs with each nickname and it's associated dice combo.
```
def combo_pairs():
    dice_combos = {}
    # Keeps track of how many times the function has
    # looped and doubles as a dice value for each pair.
    iteration = 0
    while iteration < 6:
        # Add to the accumulator
        iteration += 1
        # So that x = 1-6 through the whole loop.
        for x in range(1, 7):
            # Removes the first element from the array
            # and stores it in this value.
            nickname = DICE_NICKS.pop(0)
            # Create key value pair and add it to the
            # dictionary.
            dice_combos[nickname] = [iteration, x]
    return dice_combos
```

Output:
# {
#   'Snake Eyes': [1, 1],
#   'Australian yo': [1, 2],
#   ...
#   'Six five no jive': [6, 5],
#   'Midnight': [6, 6]
# }

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
