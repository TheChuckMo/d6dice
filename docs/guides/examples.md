# Examples




## code examples

Using the dice object in code. 

``python
from d6dice.dice import D6Dice
die = D6Dice('2d6')
print(f'Dice: {die}')
print(f'Die count: {die.count}')
print(f'Die sides: {die.sides}')
print(f'Dice max roll: {die.max}')
print(f'Dice roll: {die.roll()}')
print(f'Dice roll: {die.roll()}')
print(f'Dice roll: {die.roll()}')
print(f'Dice rolls: {die._rolls}')
``
