"""
Sudoku solver code.

Credits : https://norvig.com/sudoku.html
"""


import numpy as np


class AR_Sudoku:
    def __init__(self, puzzle):
        self.ARsudoku = puzzle 
        self.ARdigits = '123456789'
        self.ARrows = 'ABCDEFGHI'
        self.ARcols = self.ARdigits
        self.ARsquares = self.cross(self.ARrows, self.ARcols)
        self.ARunitlist = (
                          [self.cross(self.ARrows, c) for c in self.ARcols] +
                          [self.cross(r, self.ARcols) for r in self.ARrows] +
                          [self.cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
                        )
        self.ARunits = dict(
                          (s, [u for u in self.ARunitlist if s in u])
                          for s in self.ARsquares
                        )
        self.ARpeers = dict(
                          (s, set(sum(self.ARunits[s], [])) - set([s]))
                          for s in self.ARsquares
                         )


    def cross(self, A, B):
        "Cross product of elements in A and elements in B."

        return [a + b for a in A for b in B]


    def grid_values(self, grid):
        "Convert grid into a dict of {square: char} with '0' or '.' for empties."

        chars = [c for c in grid if c in self.ARdigits or c in '0.']
        assert len(chars) == 81
        return dict(zip(self.ARsquares, chars))


    def eliminate(self, values, s, d):
        """
        Eliminate d from values[s]; propagate when values or places <= 2.
        Return values, except return False if a contradiction is detected.
        """

        if d not in values[s]:
            return values  

        values[s] = values[s].replace(d, '')
        if len(values[s]) == 0:
            return False  

        elif len(values[s]) == 1:
            d2 = values[s]
            if not all(self.eliminate(values, s2, d2) for s2 in self.ARpeers[s]):
                return False

        for u in self.ARunits[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces) == 0:
                return False  
            elif len(dplaces) == 1:
                if not self.assign(values, dplaces[0], d):
                    return False

        return values


    def assign(self, values, s, d):
        """
        Eliminate all the other values (except d) from values[s] and propagate.
        Return values, except return False if a contradiction is detected.
        """

        other_values = values[s].replace(d, '')
        if all(self.eliminate(values, s, d2) for d2 in other_values):
            return values
        else:
            return False


    def parse_grid(self, grid):
        """
        Convert grid to a dict of possible values, {square: digits}, or
        return False if a contradiction is detected.
        """

        values = dict((s, self.ARdigits) for s in self.ARsquares)
        for s, d in self.grid_values(grid).items():
            if d in self.ARdigits and not self.assign(values, s, d):
                return False  

        return values


    def solve(self):
        tmp = self.search(self.parse_grid(self.ARsudoku))
        if tmp!=False:
            return np.array([tmp[s] for s in self.ARsquares])
        else:
            return False


    def search(self, values):
        "Using depth-first search and propagation, try all possible values."

        if values is False:
            return False  
        if all(len(values[s]) == 1 for s in self.ARsquares):
            return values 
        n, s = min((len(values[s]), s) for s in self.ARsquares if len(values[s]) > 1)

        return self.some(self.search(self.assign(values.copy(), s, d)) for d in values[s])


    def some(self, seq):
        "Return some element of seq that is true."

        for e in seq:
            if e: 
                return e
        return False
