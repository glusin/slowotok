import copy
import pickle

import numpy as np

N = 4


def main_(map__, cur_pos, used_positions, string=''):
    used_positions.append(cur_pos)
    string += '_'
    string += map__[cur_pos[1], cur_pos[0]]
    yield string

    l_bound = 0
    u_bound = len(map__) - 1

    for x_offset in range(-1, 2):
        new_x_pos = cur_pos[0] + x_offset
        for y_offset in range(-1, 2):
            new_y_pos = cur_pos[1] + y_offset

            if x_offset == y_offset == 0:
                continue
            elif new_x_pos < l_bound or new_x_pos > u_bound or new_y_pos < l_bound or new_y_pos > u_bound:
                continue
            elif (new_x_pos, new_y_pos) in used_positions:
                continue
            else:
                for extended_string in main_(map__, (new_x_pos, new_y_pos), copy.copy(used_positions), string):
                    yield extended_string


map_ = tuple([tuple([str(b*N + a + 1) for a in range(N)]) for b in range(N)])
map_ = np.array(map_)
combinations = set()
for x in range(N):
    for y in range(N):
        for s in main_(map_, (x, y), []):
            combinations.add(s)


combinations = [[int(idx) - 1 for idx in c.split('_') if idx] for c in combinations]
combinations = [c for c in combinations if len(c) > 2]
with open('combinations.pkl', 'wb') as pkl:
    pickle.dump(combinations, pkl)

with open('combinations.pkl', 'rb') as pkl:
    combinations = pickle.load(pkl)
