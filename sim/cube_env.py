import numpy as np
import random as rand
from sim.turns import U, U_prime, U2, D, D_prime, D2, R, R_prime, R2, L, L_prime, L2, F, F_prime, F2, B, B2, B_prime
#To run, cd .. followed by python -m sim.cube_env

#Color Scheme Ordering: Indices 0 - 8 represent White, 9 - 17 is green, 18-26 is red, 27-35 is blue, 36-44 is orange, 45 - 53 is yellow
array1 = np.arange(0, 6, 1, dtype=np.int_)
cube_array = np.repeat(array1, 9)

#Function to create a solved cube
def create_cube():
    array1 = np.arange(0, 6, 1, dtype=np.int_)
    cube_array = np.repeat(array1, 9)
    return cube_array

#Dictionary of moves

MOVES = {
    "U": U,
    "U'": U_prime,
    "U2": U2,
    "D": D,
    "D'": D_prime,
    "D2": D2,
    "R": R,
    "R'": R_prime,
    "R2": R2,
    "L": L,
    "L'": L_prime,
    "L2": L2,
    "F": F,
    "F'": F_prime,
    "F2": F2,
    "B": B,
    "B'": B_prime,
    "B2": B2
}

opposite_faces = {
    "U": "D",
    "D": "U",
    "R": "L",
    "L": "R",
    "F": "B",
    "B": "F"
}

#Step Function to apply a turn

def step(cube_state, move):
    turn = MOVES[move]
    return turn(cube_state)

#apply_sequence function to apply sequence onto cube

def apply_sequence(cube_state, sequence):
    sequence_list = sequence.split()
    for move in sequence_list:
        cube_state = step(cube_state, move)
    return cube_state

def is_solved(cube_state):
    solved_cube = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 
        1, 1, 1, 1, 1, 1, 1, 1, 1, 
        2, 2, 2, 2, 2, 2, 2, 2, 2, 
        3, 3, 3, 3, 3, 3, 3, 3, 3, 
        4, 4, 4, 4, 4, 4, 4, 4, 4, 
        5, 5, 5, 5, 5, 5, 5, 5, 5
    ])
    return np.array_equal(solved_cube, cube_state)

def scrambler(depth):
    history = []
    all_moves = list(MOVES.keys())
    for i in range(depth):
        if len(history) == 0:
            history.append(rand.choice(all_moves))
        elif len(history) == 1:
            forbidden_moves = valid_next_moves(history[0], None)
            possible_moves = list(set(all_moves) - set(forbidden_moves))
            random_move = rand.choice(possible_moves)
            history.append(random_move)
        else:
            forbidden_moves = valid_next_moves(history[-1], history[-2])
            possible_moves = list(set(all_moves) - set(forbidden_moves))
            random_move = rand.choice(possible_moves)
            history.append(random_move)
    proper_history = " ".join(history)
    scrambled_cube = apply_sequence(create_cube(), proper_history)
    #print(proper_history)
    return scrambled_cube


#helper for pruning repeat moves and opposite face repeat moves
def valid_next_moves(last_move, second_last_move):
    if (last_move is None):
            return []
    endings = ["", "'", "2"]
    forbidden_faces = []
    last_move_first = last_move[0]
    forbidden_faces.append(last_move_first)
    if second_last_move is not None and (opposite_faces[last_move_first] == second_last_move[0]):
        second_last_first = second_last_move[0]
        forbidden_faces.append(second_last_first)
    forbidden_moves = [
        face + ending

        for face in forbidden_faces
        for ending in endings
    ]
    return forbidden_moves


#helper function for easily visualizing a cube
def basic_render(cube_state):
    #printing orange pieces (top)
    for piece in range(9):
        if (piece % 3 == 0):
            print(f'      {cube_state[piece + 36]}', end=" ")
        elif (piece % 3 == 2):
            print(cube_state[piece + 36])
        else:
            print(cube_state[piece + 36], end=" ")
    #printing three rows of green, white, blue
    for i in range(3):
        for piece in range(9):
            if (piece < 3):
                print(cube_state[piece + 9 + (3 * i)], end=" ")
            elif (piece < 6):
                print(cube_state[(piece - 3) + (3 * i)], end=" ")
            else:
                if (piece == 8):
                    print(cube_state[(piece - 6) + 27 + (3* i)])
                else:
                    print(cube_state[(piece - 6) + 27 + (3* i)], end= " ")
    #printing red face
    for piece in range(9):
            if (piece % 3 == 0):
                print(f'      {cube_state[piece + 18]}', end=" ")
            elif (piece % 3 == 2):
                print(cube_state[piece + 18])
            else:
                print(cube_state[piece + 18], end=" ")
    #printing yellow
    for piece in range(9):
            if (piece % 3 == 0):
                print(f'      {cube_state[piece + 45]}', end=" ")
            elif (piece % 3 == 2):
                print(cube_state[piece + 45])
            else:
                print(cube_state[piece + 45], end=" ")
        
   
