# Examples




## code examples

Using the dice object in code. 

```python
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
```

## example - console

Examples using the console interface.

_Roll the dice_

```pythonstub
> dice run roll 3d18
command: roll 3d18
[10, 1, 1]
```

_Multiple Rolls_

```pythonstub
> dice shell
Dice console
<dice> set 4d6
<dice> roll
[5, 2, 1, 6]
<dice> roll
[3, 6, 5, 1]
<dice> roll
[6, 3, 4, 2]
<dice> roll
[5, 1, 5, 1]
<dice> exit
Dice rolls: [['4d6', 5, 2, 1, 6], ['4d6', 3, 6, 5, 1], ['4d6', 6, 3, 4, 2], ['4d6', 5, 1, 5, 1]]
```

## example - object

Example d6dice code

```python
from d6dice.dice import D6Dice
dice = D6Dice('3d6')
dice.dice
<re.Match object; span=(0, 3), match='3d6'>
dice.count
>3
dice.sides
>6
dice.roll()
[4, 5, 1]
dice.rolls
[['3d6', 1, 2, 3], ['3d6', 4, 5, 1]]
```

