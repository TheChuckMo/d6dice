#!/usr/bin/env python3

import numpy as np


class D6Dice(object):
    """

    Attributes
    ----------
    count: int 
    sides: int = 6

    """
    _rand_count: int = 100 

    def __init__(self, count: int, sides: int = 6):
        self.count = count
        self.sides = sides

    def __repr__(self):
        return f'{self.__class__.__name__}(count={self.count}, sides={self.sides})'

    def __str__(self):
        return f'{self.count}d{self.sides}'

    def role(self):
        roles = []
        for i in range(self.count):
            roles.append(self._rand_role())

        return roles

    def _rand_role(self):
        _rand_roles: list = []
        for r in range(self._rand_count):
            _rand_roles.append(np.random.randint(1,self.sides))

        return np.random.randint(1, self.sides, 1)[0]

    def max(self):
        return self.count * self.sides


die = D6Dice(3, 6)
print(f'Dice: {die}')
print(f'Role: {die.role()}')
print(f'Max: {die.max()}')
print(f'{type(die)}')


