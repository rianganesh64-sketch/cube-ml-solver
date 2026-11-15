import numpy as np
#To run, cd sim followed by python cube_env.py

#Color Scheme Ordering: Indices 0 - 8 represent White, 9 - 17 is green, 18-26 is red, 27-35 is blue, 36-44 is orange, 45 - 53 is yellow
array1 = np.arange(0, 6, 1, dtype=np.int_)
cube_array = np.repeat(array1, 9)

#Function to create a solved cube
def create_cube():
    array1 = np.arange(0, 6, 1, dtype=np.int_)
    cube_array = np.repeat(array1, 9)
    return cube_array 


#Defining Functions (turns)

def U(cube_state):
    cube_state[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38]] = cube_state[[6, 3, 0, 7, 4, 1, 6, 5, 2, 36, 37, 38, 9, 10, 11, 18, 19, 20, 27, 28, 29]]
    return(cube_state)
    
def U_prime(cube_state):
    cube_state[[0, 1, 2, 3, 4, 5, 6, 7, 8, 36, 37, 38, 9, 10, 11, 18, 19, 20, 27, 28, 29]] = cube_state[[2, 5, 8, 1, 4, 7, 0, 3, 6, 9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38]]
    return(cube_state)

def U2(cube_state):
    return U(U(cube_state))

def D(cube_state):
    cube_state[[15, 16, 17, 24, 25, 26, 33, 34, 35, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]] = cube_state[[42, 43, 44, 15, 16, 17, 24, 25, 26, 33, 34, 35, 51, 48, 45, 52, 49, 46, 53, 50, 47]]
    return(cube_state)

def D_prime(cube_state):
    cube_state[[42, 43, 44, 15, 16, 17, 24, 25, 26, 33, 34, 35, 51, 48, 45, 52, 49, 46, 53, 50, 47]] = cube_state[[15, 16, 17, 24, 25, 26, 33, 34, 35, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]]
    return(cube_state)

def D2(cube_state):
    return D(D(cube_state))

def R(cube_state):
    cube_state[[2, 5, 8, 11, 14, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 33, 47, 50, 53]] = cube_state[[11, 14, 17, 47, 50, 53, 24, 21, 18, 25, 22, 19, 26, 23, 20, 8, 5, 2, 33, 30, 27]]
    return(cube_state)

def R_prime(cube_state):
    cube_state[[11, 14, 17, 47, 50, 53, 24, 21, 18, 25, 22, 19, 26, 23, 20, 8, 5, 2, 33, 30, 27]] = cube_state[[2, 5, 8, 11, 14, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 33, 47, 50, 53]]
    return(cube_state)

def R2(cube_state):
    return R(R(cube_state))

def L(cube_state):
    cube_state[[9, 12, 15, 45, 48, 51, 6, 3, 0, 38, 41, 44, 37, 40, 43, 36, 39, 42, 35, 32, 29]] = cube_state[[0, 3, 6, 9, 12, 15, 29, 30, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 48, 51]]
    return(cube_state)

def L_prime(cube_state):
    cube_state[[0, 3, 6, 9, 12, 15, 29, 30, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 48, 51]] = cube_state[[9, 12, 15, 45, 48, 51, 6, 3, 0, 38, 41, 44, 37, 40, 43, 36, 39, 42, 35, 32, 29]]
    return(cube_state)

def L2(cube_state):
    return L(L(cube_state))

def F(cube_state):
    cube_state[[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 24, 38, 41, 44, 45, 46, 47]] = cube_state[[44, 41, 38, 15, 12, 9, 16, 13, 10, 17, 14, 11, 6, 7, 8, 45, 46, 47, 24, 21, 18]]
    return(cube_state)

def F_prime(cube_state):
    cube_state[[44, 41, 38, 15, 12, 9, 16, 13, 10, 17, 14, 11, 6, 7, 8, 45, 46, 47, 24, 21, 18]] = cube_state[[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 24, 38, 41, 44, 45, 46, 47]]
    return(cube_state)

def F2(cube_state):
    return F(F(cube_state))

def B(cube_state):
    cube_state[[0, 1, 2, 20, 23, 26, 35, 34, 33, 32, 31, 30, 29, 28, 27, 36, 39, 42, 51, 52, 53]] = cube_state[[20, 23, 26, 53, 52, 51, 29, 32, 35, 28, 31, 34, 27, 30, 33, 2, 1, 0, 36, 39, 42]]
    return(cube_state)

def B_prime(cube_state):
    cube_state[[20, 23, 26, 53, 52, 51, 29, 32, 35, 28, 31, 34, 27, 30, 33, 2, 1, 0, 36, 39, 42]] = cube_state[[0, 1, 2, 20, 23, 26, 35, 34, 33, 32, 31, 30, 29, 28, 27, 36, 39, 42, 51, 52, 53]]
    return(cube_state)

def B2(cube_state):
    B(B(cube_state))



