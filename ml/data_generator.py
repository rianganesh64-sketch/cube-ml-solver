from sim.cube_env import scrambler
import numpy as np
import time
#to run: cd.. followed by python -m ml.data_generator



def generate_data(max_depth, num_of_each):
    states_list = []
    labels_list = []
    start_time = time.perf_counter()
    for i in range(1, max_depth + 1):
        for n in range(1, num_of_each + 1):
            scrambled_cube = scrambler(i)
            states_list.append(scrambled_cube)
            labels_list.append(i)
    elapsed_time = time.perf_counter() - start_time
    labels_array = np.array(labels_list)
    states_array = np.array(states_list)
    np.save("ml/data/labels", labels_array)
    np.save("ml/data/states", states_array)
    print(elapsed_time)
    return states_array, labels_array


generate_data(20, 50000)
