import numpy as np
from sim.cube_env import MOVES, step, is_solved, valid_next_moves, apply_sequence, create_cube, scrambler

#IDDFS (Interative Deepening Depth-First Search) is a baseline, graph and treee search algorithm that essentially checks every move for a given depth. Works well for low-depth
#To run, cd .. followed by python -m solvers.iddfs

ALL_MOVES = MOVES.keys()


def dls(current_state, remaining_depth, path, stats):
    stats["nodes"] += 1
    length = len(path)
    if (remaining_depth == 0):
        if (is_solved(current_state)):
            return path
        else:
            return None
    if (remaining_depth > 0):
        if (length >= 2):
            second_last_move = path[-2]
            last_move = path[-1]
        elif (length >= 1):
            second_last_move = None
            last_move = path[-1]
        else:
            second_last_move = None
            last_move = None
        good_moves = [x for x in ALL_MOVES if x not in valid_next_moves(last_move, second_last_move)]
        for move in good_moves:
            next_state = step(current_state, move)
            result = dls(next_state, remaining_depth - 1, path + [move], stats)
            if result is not None:
                return result
        return None

print(dls(scrambler(5), 5, [], {"nodes": 0}))