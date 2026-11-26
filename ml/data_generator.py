from sim.cube_env import scrambler
import numpy as np
#to run: cd.. followed by python -m ml.data_generator



def generate_data(max_depth, num_of_each):
    states_list = []
    labels_list = []
    for i in range(1, max_depth + 1):
        for n in range(1, num_of_each + 1):
            scrambled_cube = scrambler(i)
            states_list.append(scrambled_cube)
            labels_list.append(i)
    labels_array = np.array(labels_list)
    states_array = np.array(states_list)
    return states_array, labels_array


print(generate_data(5, 3))
