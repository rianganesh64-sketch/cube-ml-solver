import numpy as np
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




