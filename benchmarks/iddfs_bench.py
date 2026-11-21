import numpy as np
from solvers.iddfs import solve_iddfs
from sim.cube_env import scrambler
#To run, cd .. followed by python -m solvers.iddfs



for depth in range(1, 6):
    for count in range(20):
        print(solve_iddfs(scrambler(depth)))