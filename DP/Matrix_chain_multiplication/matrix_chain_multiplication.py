import numpy as np


def matrix_chain_multiplication(dimensions):
    n = len(dimensions)
    cost = np.ones((n-1, n-1)) * np.inf
    index = np.ones((n-2, n-2)) * np.inf

    for i in range(len(cost)):
        cost[i, i] = 0

    for length in range(2, n):
        for i in range(1, n-length+1):
            j = i + length - 1
            for k in range(i, j):
                if cost[i-1, j-1] > cost[i-1, k-1] + cost[k, j-1] + dimensions[i-1] * dimensions[k] * dimensions[j]:
                    cost[i-1, j-1] = cost[i-1, k-1] + cost[k, j-1] + dimensions[i-1] * dimensions[k] * dimensions[j]
                    index[i-1, j-2] = k

    print(cost)
    print(index)
    print_optimal_parens(index, 1, n-1)


def print_optimal_parens(index, i, j):
    if i == j:
        print('A' + str(i), end='')
    else:
        print('(', end='')
        if i-1 < index.shape[0] and j-2 < index.shape[1]:
            k = int(index[i-1, j-2])
            print_optimal_parens(index, i, k)
            print_optimal_parens(index, k + 1, j)
        print(')', end='')


dimensions = [30, 35, 15, 5, 10, 20, 25]
matrix_chain_multiplication(dimensions)
