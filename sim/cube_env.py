import numpy as np
#To run, cd sim followed by python cube_env.py

#Color Scheme Ordering: Indices 0 - 8 represent White, 9 - 17 is green, 18-26 is red, 27-35 is blue, 36-44 is orange, 45 - 53 is yellow
array1 = np.arange(0, 6, 1, dtype=np.int_)
cube_array = np.repeat(array1, 9)

def create_cube():
    array1 = np.arange(0, 6, 1, dtype=np.int_)
    cube_array = np.repeat(array1, 9)
    return cube_array 

#Defining Functions (turns)


def U(cube_state):
    cube_state[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38]] = cube_state[[6, 3, 0, 7, 4, 1, 6, 5, 2, 36, 37, 38, 9, 10, 11, 18, 19, 20, 27, 28, 29]]
    return(cube_state)
    
def U_prime(cube_state):
    cube_state[[36, 37, 38, 9, 10, 11, 18, 19, 20, 27, 28, 29]] = cube_state[[9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38]]
    return(cube_state)

def U2(cube_state):
    return U(U(cube_state))

def R(cube_state):
    cube_state[[2, 5, 8, 11, 14, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 33, 47, 50, 53]] = cube_state[[11, 14, 17, 47, 50, 53, 24, 21, 18, 25, 22, 19, 26, 23, 20, 8, 5, 2, 33, 30, 27]]
    return(cube_state)

def R_prime(cube_state):
    cube_state[[11, 14, 17, 47, 50, 53, 24, 21, 18, 25, 22, 19, 26, 23, 20, 8, 5, 2, 33, 30, 27]] = cube_state[[2, 5, 8, 11, 14, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 33, 47, 50, 53]]
    return(cube_state)

def R2(cube_state):
    return R(R(cube_state))

# def L_prime(cube_state):
#     cube_state[[0, 3, 6, 9, 12, 15, 29, 30, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 48, 51]] = cube_state[[9, 12, 15, 45, 48, 51, 6, 3, 0, 38, 41, 44, 37, 40, 43, 36, 39, 42, 33, 32, 29]]
#     return(cube_state)

# print(L_prime(L_prime(L_prime(L_prime(create_cube())))))

