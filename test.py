import matplotlib.pyplot as plt
from Differential_equatiuons_solver.core import *

method = "Hoyn"
match method:
    case "Euler":
        our_A = np.array([0, 1])
        our_B = np.array([[0, 0], [1, 0]])
        our_G = np.array([1 / 2, 1 / 2])
    case "Hoyn":
        our_A = np.array([0, 1 / 3, 2 / 3])
        our_B = np.array([[0, 0, 0], [1 / 3, 0, 0], [0, 2 / 3, 0]])
        our_G = np.array([1 / 4, 0, 3 / 4])
    case _:
        our_A = np.array([0, 1])
        our_B = np.array([[0, 0], [1, 0]])
        our_G = np.array([1 / 2, 1 / 2])

butcher_matrix = [our_A, our_B, our_G]

our_a = np.array([0.05, 1])

our_Y_0 = [0.0, 0.0]  # must have float type

our_x_max = 200
our_N = 2000


def our_u(coordinate):
    return np.sin(coordinate)


solution = Solver(our_a, our_Y_0, our_u, butcher_matrix, our_x_max, our_N)
X = np.linspace(0, our_x_max, our_N + 1)
plt.plot(X, solution[:, 0])
plt.show()
