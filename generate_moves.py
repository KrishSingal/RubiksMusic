from scipy.spatial.transform import Rotation as R
import numpy as np
import json

pos_to_index = {(-2, 2, 3): 0, (0, 2, 3): 1, (2, 2, 3): 2,
                (-2, 0, 3): 3, (0, 0, 3): 4, (2, 0, 3): 5,
                (-2, -2, 3): 6, (0, -2, 3): 7, (2, -2, 3): 8,  # U Face

                (3, -2, 2): 9, (3, 0, 2): 10, (3, 2, 2): 11,
                (3, -2, 0): 12, (3, 0, 0): 13, (3, 2, 0): 14,
                (3, -2, -2): 15, (3, 0, -2): 16, (3, 2, -2): 17,  # R Face

                (-2, -3, 2): 18, (0, -3, 2): 19, (2, -3, 2): 20,
                (-2, -3, 0): 21, (0, -3, 0): 22, (2, -3, 0): 23,
                (-2, -3, -2): 24, (0, -3, -2): 25, (2, -3, -2): 26,  # F Face

                (-2, -2, -3): 27, (0, -2, -3): 28, (2, -2, -3): 29,
                (-2, 0, -3): 30, (0, 0, -3): 31, (2, 0, -3): 32,
                (-2, 2, -3): 33, (0, 2, -3): 34, (2, 2, -3): 35,  # D Face

                (-3, 2, 2): 36, (-3, 0, 2): 37, (-3, -2, 2): 38,
                (-3, 2, 0): 39, (-3, 0, 0): 40, (-3, -2, 0): 41,
                (-3, 2, -2): 42, (-3, 0, -2): 43, (-3, -2, -2): 44,  # L Face

                (2, 3, 2): 45, (0, 3, 2): 46, (-2, 3, 2): 47,
                (2, 3, 0): 48, (0, 3, 0): 49, (-2, 3, 0): 50,
                (2, 3, -2): 51, (0, 3, -2): 52, (-2, 3, -2): 53  # B Face
                }

positions = pos_to_index.keys()


class GMove:
    def __init__(self, name, axis, angle, condition):
        self.name = name
        self.axis = axis
        self.angle = angle
        self.condition = condition

    def apply(self, pos):
        rotation_radians = np.radians(self.angle)
        rotation_axis = np.array(self.axis)

        rotation_vector = rotation_radians * rotation_axis
        rotation = R.from_rotvec(rotation_vector)
        return rotation.apply(pos)

    def cycle_to_perm(self, cycle):
        perm = []
        for i in range(len(cycle) - 1):
            perm.append([cycle[i], cycle[i+1]])
        perm.append([cycle[-1], cycle[0]])
        return perm

    def gmove_to_fmove(self):
        relevant_positions = set()

        for pos in positions:
            if self.condition(pos):
                relevant_positions.add(pos)

        fmove = []

        while len(relevant_positions) != 0:
            curr_pos = list(relevant_positions)[0]
            curr_cycle = []

            while curr_pos in relevant_positions:
                relevant_positions.remove(curr_pos)
                curr_cycle.append(pos_to_index[curr_pos])

                curr_pos = tuple([round(x) for x in self.apply(curr_pos)])

            if len(curr_cycle) > 1:
                fmove += self.cycle_to_perm(curr_cycle)

        return fmove


if __name__ == '__main__':

    def create_gmoves(name, axis, condition):
        return [GMove(name, axis, 90, condition),
                GMove(name + '2', axis, 180, condition),
                GMove(name + "'", axis, 270, condition)]

    moves = []
    moves += create_gmoves('U', (0, 0, 1), lambda pos: pos[2] > 0)
    moves += create_gmoves('u', (0, 0, 1), lambda pos: pos[2] >= 0)
    moves += create_gmoves('D', (0, 0, -1), lambda pos: pos[2] < 0)
    moves += create_gmoves('d', (0, 0, -1), lambda pos: pos[2] <= 0)
    moves += create_gmoves('E', (0, 0, 1), lambda pos: pos[2] == 0)
    moves += create_gmoves('L', (-1, 0, 0), lambda pos: pos[0] < 0)
    moves += create_gmoves('l', (-1, 0, 0), lambda pos: pos[0] <= 0)
    moves += create_gmoves('R', (1, 0, 0), lambda pos: pos[0] > 0)
    moves += create_gmoves('r', (1, 0, 0), lambda pos: pos[0] >= 0)
    moves += create_gmoves('M', (1, 0, 0), lambda pos: pos[0] == 0)
    moves += create_gmoves('F', (0, -1, 0), lambda pos: pos[1] < 0)
    moves += create_gmoves('S', (0, 1, 0), lambda pos: pos[1] == 0)
    moves += create_gmoves('B', (0, 1, 0), lambda pos: pos[1] > 0)

    fmoves = dict()

    for move in moves:
        fmoves[move.name] = move.gmove_to_fmove()

    with open('fmoves.txt', 'w') as f:
        f.write(json.dumps(fmoves))
