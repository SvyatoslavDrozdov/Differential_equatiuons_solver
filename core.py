import numpy as np


def Solver(coefficients, initial_condition, my_function, butcher_matrix, x_max, split_number):
    A, B, G = butcher_matrix

    def f(position, y):
        return np.append(y[1:], my_function(position) - np.dot(coefficients, y[::-1]))

    value_vector = np.array([initial_condition])
    stages_number = len(A)
    x_step = x_max / (split_number - 1)
    for n in range(0, split_number):
        coordinate = x_step * n
        K = np.zeros((stages_number, len(initial_condition)))
        K[0] = np.array([x_step * f(coordinate, value_vector[n])])
        for i in range(0, stages_number):
            K[i] = x_step * f(coordinate + A[i] * x_step, value_vector[n] + np.dot(B[i], K))
            value_vector[n] += G[i] * K[i]
        value_vector = np.vstack((value_vector, value_vector[n]))
    return value_vector
