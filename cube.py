from graphics import *
import copy
import json
import random
from constants import *


class Facelet:
    def __init__(self, index, color, mask_color):
        self.index = index
        self.color = color
        self.mask_color = mask_color


'''
            U
          L F R B
            D
            
            0 1 2
            3 4 5
            6 7 8
        
36 37 38    18 19 20    9 10 11     45 46 47
39 40 41    21 22 23    12 13 14    48 49 50
42 43 44    24 25 26    15 16 17    51 52 53
    
            27 28 29 
            30 31 32
            33 34 35
            
URFDLB
            
'''

with open('fmoves.txt') as f:
    data = f.read()
fmoves = json.loads(data)


class Cube:
    def __init__(self):
        self.colors = ['white', 'red', 'green', 'yellow', 'orange', 'blue']
        self.cube = []  # string of 54 facelets
        self.mask = False

        for i in range(54):
            self.cube.append(Facelet(i, self.colors[i//9], self.colors[i // 9]))

    def display(self):
        win = GraphWin('Cube Display', 1000, 1000)
        win.setBackground('black')

        side_length = 50
        space = 10
        padding = 3*(side_length + space)
        start = Point(300, 300)

        start_tl = [start, Point(start.x + padding, start.y + padding), Point(start.x, start.y + padding),
                    Point(start.x, start.y + 2*padding), Point(start.x - padding, start.y + padding),
                    Point(start.x + 2*padding, start.y + padding)]
        start_br = []

        for p in start_tl:
            start_br.append(Point(p.x + side_length, p.y + side_length))

        for i in range(6):
            tl = start_tl[i]
            br = start_br[i]

            for j in range(9):
                top_left = Point(tl.x + (j % 3)*(side_length + space), tl.y + (j // 3)*(side_length + space))
                bottom_right = Point(br.x + (j % 3)*(side_length + space), br.y + (j // 3)*(side_length + space))

                cubie = Rectangle(top_left, bottom_right)
                if self.mask:
                    cubie.setFill(self.cube[i*9 + j].mask_color)
                else:
                    cubie.setFill(self.cube[i*9 + j].color)
                cubie.draw(win)

        win.getMouse()
        win.close()

    def apply_move(self, move):
        fmove = fmoves[move]
        new_cube = copy.deepcopy(self.cube)

        for m in fmove:
            new_cube[m[1]] = self.cube[m[0]]

        self.cube = new_cube

    def apply_mask(self, mask):  # expects map from indices to color -- color "original" leaves the facelet unchanged
        self.mask = True

        for i in range(54):
            index = self.cube[i].index

            if index in mask:
                if mask[index] == "original":
                    self.cube[i].mask_color = self.cube[i].color
                else:
                    self.cube[i].mask_color = mask[index]
            else:
                self.cube[i].mask_color = 'gray'

    def turn_off_mask(self):
        self.mask = False

    def turn_on_mask(self):
        self.mask = True

    def serialize(self):
        rep = ''
        for i in range(54):
            if self.mask:
                if self.cube[i].mask_color == 'gray':
                    rep += 'X'
                else:
                    rep += self.cube[i].mask_color[0]
            else:
                rep += self.cube[i].color[0]
        return rep.upper()

    def scramble(self):
        num_moves = random.randint(20, 30)
        scramble = []

        for i in range(num_moves):
            scramble.append(random.choice(movesets[0]))
            self.apply_move(scramble[-1])
        return scramble

    @staticmethod
    def apply_move_to_string(move, state):
        fmove = fmoves[move]
        new_state = copy.deepcopy(state)

        for m in fmove:
            new_state = new_state[:m[1]] + state[m[0]] + new_state[m[1] + 1:]

        return new_state


if __name__ == '__main__':
    c = Cube()

    eo_mask = {1: 'orange', 3: 'orange', 5: 'orange', 7: 'orange', 21: 'orange', 23: 'orange', 28: 'orange', 30: 'orange',
               32: 'orange', 34: 'orange', 48: 'orange', 50: 'orange'}
    c.apply_mask(eo_mask)
    print(c.serialize())

    # c.apply_move('E')
    # c.apply_move('M')
    c.display()
