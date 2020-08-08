# Craps Nicknames

Craps Nicknames is a tiny Python package that returns a randomized dice roll with it's associated craps nickname. The nicknames are based on the following chart by [Vital Vegas](https://vitalvegas.com/colorful-nicknames-dice-combinations-craps/):

![Craps Nicknames Charts](https://vitalvegas.com/wp-content/uploads/2015/02/craps_dice_rolls_updated.jpg)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install craps-pkg.
```python
pip install craps-pkg-sharnajh
```

## Usage

```python
import craps_pkg

craps_pkg.craps_roll()
# returns {
# "dice_pair": [1,2],
# "nickname": "Australian yo"
# }

craps_pkg.get_combo_name([2,2])
# returns "Ballerina"
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
