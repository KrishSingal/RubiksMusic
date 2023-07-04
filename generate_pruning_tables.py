from cube import *
import time


def prune(moves, states, depth):
    visited = set(states)
    q = []
    for state in states:
        q.append((state, 0))
    prune_table = dict()

    reached_depths = set()

    start = time.time()
    while len(q) != 0:
        curr_state, distance = q.pop(0)
        visited.add(curr_state)

        prune_table[curr_state] = distance

        if distance not in reached_depths:
            end = time.time()
            print(f'---- depth {distance} -----')
            print(f'{end - start} s')
            reached_depths.add(distance)
            start = time.time()

        if distance == depth:
            continue

        for move in moves:
            new_state = Cube.apply_move_to_string(move, curr_state)
            if new_state not in visited:
                q.append((new_state, distance + 1))

    return prune_table


if __name__ == '__main__':
    c = Cube()

    # ----------- G0 ----------- #
    '''g0_mask = {1: 'orange', 3: 'orange', 5: 'orange', 7: 'orange', 21: 'orange', 23: 'orange', 28: 'orange',
               30: 'orange', 32: 'orange', 34: 'orange', 48: 'orange', 50: 'orange'}

    c.apply_mask(g0_mask)

    g0_table = prune(['L', "L'", 'L2', 'R', "R'", 'R2', 'U', "U'", 'U2', 'B', "B'", 'B2', 'D',
                      "D'", 'D2', 'F', "F'", 'F2'], [c.serialize()], 10)

    with open('G0.txt', 'w') as f:
        f.write(json.dumps(g0_table))'''

    # ----------- G1 ----------- #

    '''g1_mask = {0: 'orange', 1: 'orange', 2: 'orange', 3: 'orange', 5: 'orange', 6: 'orange', 7: 'orange',
               8: 'orange', 27: 'orange', 28: 'orange', 29: 'orange', 30: 'orange', 32: 'orange', 33: 'orange',
               34: 'orange', 35: 'orange', 21: 'pink', 23: 'pink', 48: 'pink', 50: 'pink'}

    c.apply_mask(g1_mask)

    g1_table = prune(['L', "L'", 'L2', 'R', "R'", 'R2', 'U', "U'", 'U2', 'D',
                      "D'", 'D2', 'F2', 'B2'], [c.serialize()], 6)

    with open('G1.txt', 'w') as f:
        f.write(json.dumps(g1_table))'''

    # ----------- G2 ----------- #

    '''g2_mask = {0: 'original', 2: 'original', 6: 'original', 8: 'original',
               9: 'original', 11: 'original', 15: 'original', 17: 'original',
               18: 'original', 20: 'original', 24: 'original', 26: 'original',
               27: 'original', 29: 'original', 33: 'original', 35: 'original',
               36: 'original', 38: 'original', 42: 'original', 44: 'original',
               45: 'original', 47: 'original', 51: 'original', 53: 'original',

               37: 'red', 39: 'red', 41: 'red', 43: 'red',
               19: 'original', 21: 'original', 23: 'original', 25: 'original',
               10: 'original', 12: 'original', 14: 'original', 16: 'original',
               46: 'green', 48: 'green', 50: 'green', 52: 'green'
               }

    c.apply_mask(g2_mask)

    g3_solved_states = prune(['U2', 'L2', 'F2', 'R2', 'D2', 'B2'], [c.serialize()], 10).keys()

    print(len(g3_solved_states) == 96)

    g2_table = prune(['U', "U'", 'U2', 'D', "D'", 'D2', 'L2', 'F2', 'R2', 'B2'], g3_solved_states, 5)

    with open('G2.txt', 'w') as f:
        f.write(json.dumps(g2_table))'''

    # ----------- G3 ----------- #

    '''g3_table = prune(['U2', 'L2', 'F2', 'R2', 'D2', 'B2'], [c.serialize()], 6)

    with open('G3.txt', 'w') as f:
        f.write(json.dumps(g3_table))'''

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