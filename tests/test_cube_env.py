import pytest
from sim.cube_env import create_cube, U, U_prime
import numpy as np

def test_order_4_identity():
    starting_cube = create_cube()
    moved_cube = U(U(U(U(create_cube()))))
    assert np.array_equal(moved_cube, starting_cube)

    moved_cube = U_prime(U_prime(U_prime(U_prime(create_cube()))))
    assert np.array_equal(moved_cube, starting_cube)

def test_inverse_identity():
    base_cube = create_cube()
    assert np.array_equal(U(U_prime(create_cube())), base_cube)
    assert np.array_equal(U_prime(U(create_cube())), base_cube)