from cube import *
import sys
from constants import *


class Solver:
    def __init__(self, cube):
        self.cube = cube
        self.group = 0
        self.limits = [10, 10, 13, 14]

    def solve(self):
        t1, s1 = self.phase(0)
        t2, s2 = self.phase(1)
        t3, s3 = self.phase(2)
        t4, s4 = self.phase(3)

        print(f'\n-------- G0 to G4 ({t1 + t2 + t3 + t4} s) --------')
        print(f'Solution ({len(s1 + s2 + s3 + s4)} Moves): {s1 + s2 + s3 + s4}')

    def phase(self, num):
        self.group = num

        with open(f'G{num}.txt') as file:
            data = file.read()

        pruning_table = json.loads(data)

        start = time.time()

        self.cube.apply_mask(masks[num])

        sol = self.iddfs(movesets[num], self.cube.serialize(), pruning_table)

        end = time.time()

        print(f'-------- G{num} to G{num+1} ({end - start} s) --------')
        print(f'Solution ({len(sol)} Moves): {sol}')

        for move in sol:
            self.cube.apply_move(move)

        self.cube.turn_off_mask()
        self.cube.display()

        return end - start, sol

    def iddfs(self, moveset, state, h):
        depth = 6
        sol = None

        while sol is None:
            # print(depth)
            sol = self.search([], moveset, state, [], depth, h)
            if sol is None:
                depth += 1
        return sol

    def search(self, visited, moveset, state, solution, depth_remaining, h):
        visited.append(state)
        lower_bound = -1

        if state in h:
            if h[state] == 0:
                return solution
            else:
                lower_bound = h[state]
        else:
            lower_bound = prune_depths[self.group] + 1

        # if self.group == 1:
            # print(f'state: {state} lower bound: {lower_bound}')

        if lower_bound > depth_remaining:
            return None

        for move in moveset:
            new_state = Cube.apply_move_to_string(move, state)
            if new_state not in visited:
                solution.append(move)
                t = self.search(visited, moveset, new_state, solution, depth_remaining-1, h)
                if t is not None:
                    return t
                solution.pop(-1)
        return None

    '''def IDA_Star(self, moveset, state, h):
        if state in h:
            bound = h[state]
        else:
            bound = prune_depths[self.group] + 1

        while True:
            print(f'bound: {bound}')
            t = self.search([], moveset, state, [], bound, h)
            if isinstance(t, int):
                bound = t
            else:
                return t

    def search(self, visited, moveset, state, solution, bound, h):
        visited.append(state)

        g = len(solution)
        f = -1
        if state in h:
            f = h[state] + g
        else:
            f = prune_depths[self.group] + 1 + g

        if f > bound:
            return f
        if f-g == 0:
            return solution

        new_threshold = sys.maxsize

        for move in moveset:
            new_state = Cube.apply_move_to_string(move, state)
            if new_state not in visited:
                solution.append(move)
                t = self.search(visited, moveset, new_state, solution, bound, h)
                if not isinstance(t, int):
                    return t
                if new_threshold < t:
                    new_threshold = t
                solution.pop(-1)
        return new_threshold'''


