import numpy as np


#Color Scheme Ordering: Indices 0 - 8 represent White, 9 - 17 is green, 18-26 is red, 27-35 is blue, 36-44 is orange, 45 - 53 is yellow
array1 = np.arange(0, 6, 1, dtype=np.int_)
cube_array = np.repeat(array1, 9)

def create_cube():
    array1 = np.arange(0, 6, 1, dtype=np.int_)
    cube_array = np.repeat(array1, 9)
    return cube_array 

#Defining Functions (turns)


def U(cube_state):
    cube_state[[9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38]] = cube_state[[36, 37, 38, 9, 10, 11, 18, 19, 20, 27, 28, 29]]
    return(cube_state)
    
def U_prime(cube_state):
    cube_state[[36, 37, 38, 9, 10, 11, 18, 19, 20, 27, 28, 29]] = cube_state[[9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38]]
    return(cube_state)
    

print(U_prime(U(create_cube())))