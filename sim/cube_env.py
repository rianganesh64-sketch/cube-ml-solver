import numpy as np


#Color Scheme Ordering: Indices 0 - 8 represent White, 9 - 17 is green, 18-26 is red, 27-35 is blue, 36-44 is orange, 45 - 53 is yellow
array1 = np.arange(0, 6, 1, dtype=np.int_)
cube_array = np.repeat(array1, 9)


#Defining Functions (turns)

print(cube_array)


def U(cube_state):
    cube_state[[9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38]] = cube_state[[36, 37, 38, 9, 10, 11, 18, 19, 20, 27, 28, 29]]
    return(cube_state)
    
    
    
    
    # green = cube_state[[9, 10, 11]]
    # red = cube_state[[18, 19, 20]]
    # blue = cube_state[[27, 28, 29]]
    # orange = cube_state[[36, 37, 38]]
    # cube_state[green] = cube_state[orange]
    # cube_state[red] = cube_state[green]
    # cube_state[blue] = cube_state[red]
    # cube_state[orange] = cube_state[blue]
    # return cube_state

print(U(cube_array))