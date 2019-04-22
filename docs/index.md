# d6Dice

Python dice object: 
  - Uses dice notation '2d6', '3d6', '2d12', '3d8' etc
  - Default dice roller uses numpy
  - Dynamically change how dice are rolled

The d6dice project was created to be used with the d6Engine and OpenD6 games. 

## Install - REQUIRES Python3

python3 -m pip install --user d6dice

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


