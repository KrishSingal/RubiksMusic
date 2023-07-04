from cube import *
from solver import *


if __name__ == '__main__':
    c = Cube()
    print(f'Scramble: {c.scramble()}')
    c.display()

    s = Solver(c)
    s.solve()