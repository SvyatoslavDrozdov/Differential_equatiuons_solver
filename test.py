import matplotlib.pyplot as plt
from Differential_equatiuons_solver.core import *

method = "Hoyn"
match method:
    case "Euler":
        A = np.array([0, 1])
        B = np.array([[0, 0], [1, 0]])
        G = np.array([1 / 2, 1 / 2])
    case "Hoyn":
        A = np.array([0, 1 / 3, 2 / 3])
        B = np.array([[0, 0, 0], [1 / 3, 0, 0], [0, 2 / 3, 0]])
        G = np.array([1 / 4, 0, 3 / 4])
    case "Classic":
        A = np.array([0, 1 / 2, 1 / 2, 1])
        B = np.array([[0, 0, 0, 0], [1 / 2, 0, 0, 0], [0, 1 / 2, 0, 0], [0, 0, 1, 0]])
        G = np.array([1 / 6, 2 / 6, 2 / 6, 1 / 6])
    case _:
        A = np.array([0, 1 / 2, 1 / 2, 1])
        B = np.array([[0, 0, 0, 0], [1 / 2, 0, 0, 0], [0, 1 / 2, 0, 0], [0, 0, 1, 0]])
        G = np.array([1 / 6, 2 / 6, 2 / 6, 1 / 6])

butcher_matrix = [A, B, G]

coefficients = np.array([0.05, 1])

initial_condition = [0.0, 0.0]  # must have float type

x_max = 200
split_number = 2000


def my_function(coordinate):
    return np.sin(coordinate)


solution = Solver(coefficients=coefficients, initial_condition=initial_condition, my_function=my_function,
                  butcher_matrix=butcher_matrix, x_max=x_max, split_number=split_number)
X = np.linspace(0, x_max, split_number + 1)
plt.plot(X, solution[:, 0])
plt.xlabel("time")
plt.ylabel("position")
plt.show()
