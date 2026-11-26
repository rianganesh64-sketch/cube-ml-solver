import numpy as np
import random

mmap_states = np.load('ml/data/states.npy', mmap_mode="r")
mmap_labels = np.load('ml/data/labels.npy', mmap_mode="r")
batch_size = 256


# def load_data(batch_size):
    
#     states_list = []
#     labels_list = []
#     for i in range(batch_size):
#         state = mmap_states[indexes[i]]
#         states_list.append(state)
#         label = mmap_labels[indexes[i]]
#         labels_list.append(label)
#     return states_list, labels_list

# print(load_data(1))