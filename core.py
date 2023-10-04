import numpy as np


def solver(coefficients, initial_condition, my_function, butcher_matrix, x_max, split_number):
    A, B, G = butcher_matrix

    def f(position, y):
        return np.append(y[1:], my_function(position) - np.dot(coefficients, y[::-1]))

    value_matrix = np.array([initial_condition])
    stages_number = len(A)
    initial_cond_len = len(initial_condition)
    x_step = x_max / (split_number - 1)
    for n in range(0, split_number):
        coordinate = x_step * n
        K = np.zeros((stages_number, initial_cond_len))
        K[0] = np.array([x_step * f(coordinate, value_matrix[n])])
        delta_value_matrix = 0
        for i in range(0, stages_number):
            K[i] = x_step * f(coordinate + A[i] * x_step, value_matrix[n] + np.dot(B[i], K))
            delta_value_matrix += G[i] * K[i]
        value_matrix = np.vstack((value_matrix, value_matrix[n]+delta_value_matrix))
    return value_matrix
